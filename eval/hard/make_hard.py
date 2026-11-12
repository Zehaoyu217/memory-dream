#!/usr/bin/env python3
"""The worn bank: the same 1,677 notes as written by people who do not keep frontmatter. No model here.

  python3 eval/hard/make_hard.py <dreamed tidy bank> <out dir> [--handles eval/hard/handles.json] [--by-phrase 0.35] [--seed 7]

In the tidy bank every link between notes is a line of frontmatter: `from: [a, b]`, `supersedes: [c]`. Half of those
links are stated nowhere else (measured: 1,110 of 2,213 `from` links and 104 of 216 `supersedes` are not in the
note's prose), which is why grep reads that bank exactly: one line a note lists them all by id. Here the two
frontmatter lines are gone from every note, and the note says the same thing in a closing sentence, as people do:
"Builds on a, b and the KYC band feature." and "Replaces c." Each other note is named by its id, or with the share
--by-phrase by the short phrase a colleague would use for it, taken from handles.json, which a cheap model wrote once
from the titles (eval/hard/handles.py). So every link is still stated, once, as a link; what is lost is the fixed
place and, for a third of them, the id. Nothing else in a note changes, and no note moves.

<out>/memory is the worn bank: notes only, no registry and no readings. <out>/truth.json keeps what the frontmatter
said (the answer key: it is never copied into a memory or an agent's workspace) and how each link is now stated.
Quoted in RESULTS.md phase S.
"""
import collections
import json
import random
import re
import shutil
import sys
from pathlib import Path

REG = {"KINDS.md", "TYPES.md", "EDGES.md", "ALIASES.md", "CONFLICTS.md", "DIGEST.md", "TAGS.md", "SETUP.md"}


def split(text):
    """-> (frontmatter lines without the fences, body)."""
    if text.startswith("---\n") and "\n---\n" in text[4:]:
        fm, body = text[4:].split("\n---\n", 1)
        return fm.split("\n"), body
    return [], text


def main(argv):
    src, out = Path(argv[1]), Path(argv[2])
    opt = lambda k, d: argv[argv.index(k) + 1] if k in argv else d  # noqa: E731
    handles = json.loads(Path(opt("--handles", Path(__file__).parent / "handles.json")).read_text())
    share, rnd = float(opt("--by-phrase", 0.35)), random.Random(int(opt("--seed", 7)))
    g = json.loads((src / "_dream" / "graph.json").read_text())
    notes = {n["path"]: n for n in g["notes"]}
    links = collections.defaultdict(lambda: {"from": [], "supersedes": []})
    for e in sorted(g["edges"], key=lambda e: (e["src"], e["rel"], e["dst"])):
        if e["rel"] in ("from", "supersedes") and e.get("by") in (None, "review"):
            links[e["src"]][e["rel"]].append(e["dst"])
    mem = out / "memory"
    if mem.exists():
        raise SystemExit(f"{mem} exists: give a fresh out dir")
    stated, count = {}, collections.Counter()
    join = lambda xs: xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " and " + xs[-1]  # noqa: E731
    for p in sorted(notes):
        fm, body = split((src / p).read_text())
        fm = [ln for ln in fm if not re.match(r"\s*(from|supersedes)\s*:", ln)]
        said = {"from": [], "supersedes": []}
        for rel in ("from", "supersedes"):
            for q in links[p][rel]:
                h = handles.get(q)
                by_phrase = bool(h) and rnd.random() < share
                said[rel].append(h if by_phrase else notes[q]["id"])
                stated[f"{p} {rel} {q}"] = "by a phrase" if by_phrase else "by its id"
                count[stated[f"{p} {rel} {q}"]] += 1
        tail = (f"Builds on {join(said['from'])}.\n" if said["from"] else "") + (f"Replaces {join(said['supersedes'])}.\n" if said["supersedes"] else "")
        f = mem / p
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(("---\n" + "\n".join(fm) + "\n---\n" if fm else "") + body.rstrip("\n") + "\n" + tail)
    top = {Path(p).name for p in notes if "/" not in p}
    for f in src.iterdir():  # nothing but notes goes over: the worn bank is set up from scratch
        if f.is_file() and f.suffix == ".md" and f.name not in REG and f.name not in top:
            shutil.copy2(f, mem / f.name)
    (out / "truth.json").write_text(json.dumps({"edges": [{"src": s_, "dst": d, "rel": r} for s_, v in sorted(links.items()) for r in ("from", "supersedes") for d in v[r]],
                                                "stated": stated}, indent=0))
    print(f"{len(notes)} notes in {mem}; {sum(count.values())} links stated in a closing sentence: " + ", ".join(f"{n} {k}" for k, n in sorted(count.items())))


if __name__ == "__main__":
    main(sys.argv)
