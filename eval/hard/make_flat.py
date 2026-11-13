#!/usr/bin/env python3
"""The flat bank: the worn bank with its forty project folders poured into one. No model here.

  python3 eval/hard/make_flat.py <worn dir (make_hard.py)> <questions.jsonl> <out dir> [--folder work]

In the worn bank a project is a folder of thirty short notes, about 3,500 tokens. An agent with grep reads such a
folder whole, and a keeper is shown all of it by name. Neither holds once a folder is too large to read: here every
project note is in one folder (1,224 notes, about 130,000 tokens, more than a 100,000-token window), with nothing
that says which project a note belongs to but its own name and words. The general folders (prefs, reporting,
glossary, corrections, howto, qa, log) stay as they are.

What changes in a note, and nothing else:
  - 38 experiment ids are used by several projects (`exp-401` in seven). Such a note gets its old folder at the end
    of its name (`exp-401-aml-alerts`), and the notes of that project that name it are rewritten to say so.
  - A note of another project was named with its folder (`income-estimation/inc-gbm-v3`): it is named by its id.

<out>/memory is the flat bank (notes only), <out>/truth.json the answer key of the worn bank with the new paths,
<out>/questions.jsonl the linkage questions that do not need a project to be asked (what a note rests on, what rests
on it, the note in force at the end of a line of replacements, the features two models share, and three across the
whole memory), reworded without their project and with the notes they name under `key`, and <out>/map.json the old
path of every note against the new one. The script checks its own work: every name is used once, every link the key
says is stated by an id finds that id in the note, and no project note is still named with a folder.
Quoted in RESULTS.md phase S.
"""
import collections
import json
import re
import sys
from pathlib import Path

GENERAL = {"prefs", "reporting", "glossary", "corrections", "howto", "qa", "people", "log"}
KEEP = ("rests-on", "downstream", "in-force", "shared", "stale-input-all", "replaced-twice")
EDGE = lambda s: r"(?<![\w/.-])" + re.escape(s) + r"(?![\w-])"  # noqa: E731


def main(argv):
    worn, qfile, out = Path(argv[1]), Path(argv[2]), Path(argv[3])
    folder = argv[argv.index("--folder") + 1] if "--folder" in argv else "work"
    src, mem = worn / "memory", out / "memory"
    if mem.exists():
        raise SystemExit(f"{mem} exists: give a fresh out dir")
    notes = sorted(str(p.relative_to(src)) for p in src.rglob("*.md") if len(p.relative_to(src).parts) == 2)
    proj = [p for p in notes if p.split("/")[0] not in GENERAL]
    used = collections.Counter(Path(p).stem for p in proj)
    new = {}  # old path -> new path
    for p in notes:
        f, stem = p.split("/")[0], Path(p).stem
        new[p] = p if f in GENERAL else f"{folder}/{stem}-{f}.md" if used[stem] > 1 else f"{folder}/{stem}.md"
    assert len(set(new.values())) == len(new), "a name is used twice"
    renamed = collections.defaultdict(dict)  # project folder -> {old id: new id}
    for p in proj:
        if used[Path(p).stem] > 1:
            renamed[p.split("/")[0]][Path(p).stem] = Path(new[p]).stem

    def cross(m):  # a note of another project, named with its folder
        q = f"{m.group(1)}/{m.group(2)}.md"
        return Path(new[q]).stem if q in new and m.group(1) not in GENERAL else m.group(0)
    changed = 0
    for p in notes:
        text = (src / p).read_text()
        was = text
        text = re.sub(r"(?<![\w/.-])([a-z0-9][a-z0-9-]*)/([a-z0-9][a-z0-9-]*[a-z0-9])(?![\w/-])", cross, text)
        for old, to in renamed.get(p.split("/")[0], {}).items():
            text = re.sub(EDGE(old), to, text)
        changed += text != was
        (mem / new[p]).parent.mkdir(parents=True, exist_ok=True)
        (mem / new[p]).write_text(text)

    truth = json.loads((worn / "truth.json").read_text())
    how = {"by its id, with its folder": "by its id, where the worn bank gave its folder"}
    edges = [{"src": new[e["src"]], "dst": new[e["dst"]], "rel": e["rel"]} for e in truth["edges"]]
    stated = {}
    for k, v in truth["stated"].items():
        s, r, d = k.split(" ")
        stated[f"{new[s]} {r} {new[d]}"] = how.get(v, v) if s.split("/")[0] not in GENERAL else v
    (out / "truth.json").write_text(json.dumps({"edges": edges, "stated": stated}, indent=0))
    (out / "map.json").write_text(json.dumps(new, indent=0))

    # the script's own check of its work
    bad = 0
    for e in edges:
        if "by its id" in stated[f"{e['src']} {e['rel']} {e['dst']}"] and e["src"].startswith(folder + "/"):
            name = Path(e["dst"]).stem if e["dst"].startswith(folder + "/") else e["dst"][:-3]
            bad += not re.search(EDGE(name), (mem / e["src"]).read_text())
    left = sum(1 for p in proj for m in re.finditer(r"(?<![\w/.-])([a-z0-9][a-z0-9-]*)/([a-z0-9][a-z0-9-]*[a-z0-9])(?![\w/-])", (mem / new[p]).read_text())
               if f"{m.group(1)}/{m.group(2)}.md" in new and m.group(1) not in GENERAL)
    if bad or left:
        raise SystemExit(f"{bad} links stated by an id that the note no longer has; {left} project notes still named with a folder")

    # the questions that can be asked without a project
    rx = {"rests-on": r"In project (?P<a>\S+), follow everything (?P<n>\S+) was built on", "downstream": r"rest on (?P<n>\S+) of project (?P<a>\S+?),",
          "in-force": r"^(?P<n>\S+) of project (?P<a>\S+) was replaced", "shared": r"Which feature notes do (?P<n>\S+) and (?P<n2>\S+) of project (?P<a>\S+) both"}
    qs, kept = [json.loads(x) for x in qfile.read_text().splitlines() if x.strip()], []
    for q in qs:
        t = q["type"]
        if t not in KEEP:
            continue
        m = re.search(rx[t], q["q"]) if t in rx else None
        key = [new[f"{m.group('a')}/{m.group(k)}.md"] for k in ("n", "n2") if k in m.groupdict()] if m else []
        ids = [Path(k).stem for k in key]
        text = {"rests-on": lambda: f"Follow everything {ids[0]} was built on, back to the start. Which dataset notes does it rest on, directly or through other notes?",
                "downstream": lambda: f"Which decision notes rest on {ids[0]}, directly or through other notes that were built on it?",
                "in-force": lambda: f"{ids[0]} was replaced, and so was its replacement. Which note is in force now at the end of that line, and which notes is that one built on?",
                "shared": lambda: f"Which feature notes do {ids[0]} and {ids[1]} both build on directly?",
                "stale-input-all": lambda: "Across the whole memory, which model notes that are still current build directly on a feature or dataset note that has since been replaced?",
                "replaced-twice": lambda: re.sub(r"^Across every project,", "Across the whole memory,", q["q"])}[t]()
        gold = [new[g] for g in q["gold"]]
        kept.append({"type": t, "q": text, "gold": gold, "notes": gold, "a": ", ".join(gold), **({"key": key} if key else {}),
                     **({"chain": [new[c] for c in q["chain"]]} if q.get("chain") else {})})
    (out / "questions.jsonl").write_text("".join(json.dumps(q) + "\n" for q in kept))
    size = sum((mem / new[p]).stat().st_size for p in proj)
    by = collections.Counter(q["type"] for q in kept)
    print(f"{len(notes)} notes in {mem}: {len(proj)} in {folder}/ ({size:,} bytes, about {size // 4:,} tokens), {len(notes) - len(proj)} in the general folders · "
          f"{sum(len(v) for v in renamed.values())} notes renamed, {changed} notes reworded · {len(edges)} links in the key, every id-stated one found · "
          f"{len(kept)} questions of {len(qs)}: " + ", ".join(f"{t} {n}" for t, n in sorted(by.items())))


if __name__ == "__main__":
    main(sys.argv)
