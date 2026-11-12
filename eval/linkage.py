#!/usr/bin/env python3
"""Questions that need linkage across notes, with answers that can be scored exactly. No model.

  python3 eval/linkage.py make  <a dreamed memory> <out.jsonl> [--n 5] [--keep old.jsonl]   questions and true answers
                                                     (--keep: the questions of an earlier file, answers computed again)
  python3 eval/linkage.py global <a dreamed memory> <out.jsonl>             questions over the whole memory
  python3 eval/linkage.py score <questions.jsonl> <answers.md> [more.md …]  recall, precision, exact, per answer file
  python3 eval/linkage.py ask   <a dreamed memory> <questions.jsonl>        what `ask` alone shows: no agent, no model

The thirty questions of the agent eval can mostly be answered from one note. These cannot: each asks for a set of
notes reached through several links — everything a model rests on, every decision downstream of a dataset, the note
in force at the end of a line of replacements and what it is built on, the features two models share, the notes
other projects built on one, the current models that still build on a replaced input. The true answer is computed
from the notes' own `from:` and `supersedes:` lines (the lineage in graph.json, which no model writes), so an
answer is scored by its note paths and no judge is needed.

An answer file has sections "## Q1" … and in each a line "Notes: path, path, …". An answer is exact when the notes it
lists are the true set. Two kinds of note on that line are support and not part of the answer: a note of another
kind than the question asks for (a model beside the datasets it rests on), and the note the question itself names.
`score` prints the count without the second allowance as well. Quoted in RESULTS.md phase L.
"""
import collections
import json
import os
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
MEM = REPO / "skills/memory-dream/scripts/memory.py"
ENV = {k: v for k, v in os.environ.items() if not k.startswith("MEMORY_")}
GENERAL = {"prefs", "reporting", "glossary", "corrections", "howto", "qa", "people", "log", ""}
ASKS = {"rests-on": "ds-", "downstream": "dec-", "shared": "feat-"}  # the kind of note a question asks for, by file name


def lineage(root):
    g = json.loads((Path(root) / "_dream" / "graph.json").read_text())
    notes = {n["path"]: n for n in g["notes"]}
    up, down, sup = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set)
    for e in g["edges"]:
        if e["rel"] == "from":
            up[e["src"]].add(e["dst"])
            down[e["dst"]].add(e["src"])
        elif e["rel"] == "supersedes":
            sup[e["src"]].add(e["dst"])
    return notes, up, down, sup


def closure(start, nxt):
    """{note: depth} of everything reached from start."""
    seen, todo = {}, [(start, 0)]
    while todo:
        p, d = todo.pop(0)
        for q in sorted(nxt[p]):
            if q not in seen and q != start:
                seen[q] = d + 1
                todo.append((q, d + 1))
    return seen


def spread(cands, n):
    """n of the candidates, evenly through the sorted list and never two from one project while others remain."""
    cands = sorted(cands, key=lambda c: c["key"])
    out, areas = [], set()
    step = max(1, len(cands) // (n * 3))
    for c in cands[::step] + cands:
        if len(out) < n and c["area"] not in areas and c not in out:
            out.append(c)
            areas.add(c["area"])
    return out


def make(root, n, keep=None):
    notes, up, down, sup = lineage(root)
    # what a note is, for the true answers, is read from its file name, which the writer chose (ds-, dec-, feat-): the
    # kind in the graph may come from a keeper's reading, and a model must not write the answer key
    by_name = {"ds": "dataset", "dec": "decision", "feat": "feature"}
    kind = lambda p: by_name.get(notes[p]["id"].split("-")[0], notes[p]["kind"] if notes[p]["kind"] not in by_name.values() else "note")  # noqa: E731
    area = lambda p: notes[p]["project"]  # noqa: E731
    nid = lambda p: notes[p]["id"]  # noqa: E731
    live = lambda p: not notes[p]["superseded_by"]  # noqa: E731
    T = collections.defaultdict(list)
    for p in sorted(notes):
        if area(p) in GENERAL:
            continue
        ups, downs = closure(p, up), closure(p, down)
        if kind(p) == "model":
            ds = sorted(q for q in ups if kind(q) == "dataset")
            if 2 <= len(ds) <= 6 and max(ups[q] for q in ds) >= 2:
                T["rests-on"].append({"key": p, "area": area(p), "gold": ds, "q": f"In project {area(p)}, follow everything {nid(p)} was "
                                      f"built on, back to the start. Which dataset notes does it rest on, directly or through other notes?"})
        if kind(p) in ("dataset", "feature"):
            dec = sorted(q for q in downs if kind(q) == "decision")
            if 2 <= len(dec) <= 6 and max(downs[q] for q in dec) >= 2:
                T["downstream"].append({"key": p, "area": area(p), "gold": dec, "q": f"Which decision notes rest on {nid(p)} of project "
                                        f"{area(p)}, directly or through other notes that were built on it?"})
        if notes[p]["superseded_by"] and not sup[p]:
            end, hops = p, 0
            while notes[end]["superseded_by"] and hops < 9:
                end, hops = sorted(notes[end]["superseded_by"])[0], hops + 1
            base = sorted(up[end])
            if hops >= 2 and 1 <= len(base) <= 5:
                T["in-force"].append({"key": p, "area": area(p), "gold": [end] + base, "q": f"{nid(p)} of project {area(p)} was replaced, and "
                                      f"so was its replacement. Which note is in force now at the end of that line, and which notes is that one built on?"})
        cross = sorted(q for q in down[p] if area(q) != area(p) and area(q) not in GENERAL)
        if 1 <= len(cross) <= 5:
            T["other-projects"].append({"key": p, "area": area(p), "gold": cross,
                                        "q": f"Which notes of other projects were built directly on {nid(p)} of project {area(p)}?"})
    by_area = collections.defaultdict(list)
    for p in notes:
        if kind(p) == "model" and area(p) not in GENERAL:
            by_area[area(p)].append(p)
    for a, ms in sorted(by_area.items()):
        ms = sorted(ms)
        for i, m1 in enumerate(ms):
            for m2 in ms[i + 1:]:
                both = sorted(q for q in up[m1] & up[m2] if kind(q) == "feature")
                if 2 <= len(both) <= 5:
                    T["shared"].append({"key": m1 + m2, "area": a, "gold": both,
                                        "q": f"Which feature notes do {nid(m1)} and {nid(m2)} of project {a} both build on directly?"})
        stale = sorted(m for m in ms if live(m) and any(not live(q) and kind(q) in ("feature", "dataset") for q in up[m]))
        if 1 <= len(stale) <= 5 and len([m for m in ms if live(m)]) >= 2:
            T["stale-input"].append({"key": a, "area": a, "gold": stale, "q": f"In project {a}, which model notes that are still current "
                                     f"build directly on a feature or dataset note that has since been replaced?"})
    if keep:  # the questions of an earlier file, in its order, with their answers computed again
        by_text = {c["q"]: (t, c) for t, cs in T.items() for c in cs}
        old = [json.loads(x) for x in Path(keep).read_text().splitlines() if x.strip()]
        lost = [q["q"][:60] for q in old if q["q"] not in by_text]
        if lost:
            raise SystemExit(f"no longer a candidate: {lost}")
        return [{"type": by_text[q["q"]][0], "q": q["q"], "gold": by_text[q["q"]][1]["gold"], "notes": by_text[q["q"]][1]["gold"],
                 "a": ", ".join(by_text[q["q"]][1]["gold"])} for q in old], {t: len(c) for t, c in sorted(T.items())}
    picked = {t: spread(c, n) for t, c in sorted(T.items())}
    out = []
    for i in range(n):  # one of each kind in turn, so every batch of ten mixes them
        for t in sorted(picked):
            if i < len(picked[t]):
                c = picked[t][i]
                out.append({"type": t, "q": c["q"], "gold": c["gold"], "notes": c["gold"], "a": ", ".join(c["gold"])})
    return out, {t: len(c) for t, c in sorted(T.items())}


def make_global(root):
    """Questions over the whole memory: the answer is a set of notes from many projects, so no folder can be read whole
    to find it. Same source of truth: the notes' `from:` and `supersedes:` lines, and what a note is by its file name."""
    notes, up, down, sup = lineage(root)
    by_name = {"ds": "dataset", "dec": "decision", "feat": "feature"}
    cls = lambda p: by_name.get(notes[p]["id"].split("-")[0], notes[p]["kind"] if notes[p]["kind"] not in by_name.values() else "note")  # noqa: E731
    area = lambda p: notes[p]["project"]  # noqa: E731
    live = lambda p: not notes[p]["superseded_by"]  # noqa: E731
    proj = sorted(p for p in notes if area(p) not in GENERAL)

    def hops(p):
        n, end = 0, p
        while notes[end]["superseded_by"] and n < 9:
            end, n = sorted(notes[end]["superseded_by"])[0], n + 1
        return n
    out = [("stale-input-all", "Across every project in the memory, which model notes that are still current build directly on a "
            "feature or dataset note that has since been replaced?",
            [p for p in proj if cls(p) == "model" and live(p) and any(not live(q) and cls(q) in ("dataset", "feature") for q in up[p])])]
    reach = {a: sorted({q for p in proj if area(p) == a for q in closure(p, down) if area(q) != a and area(q) not in GENERAL})
             for a in sorted({area(p) for p in proj})}
    for a in sorted(reach, key=lambda a: (-len(reach[a]), a))[:3]:
        out.append(("reach", f"Which notes outside project {a} rest on a note of {a}, directly or through other notes built on it?", reach[a]))
    for word, c in (("decision", "decision"), ("model", "model")):
        out.append(("replaced-twice", f"Across every project, which {word} notes were replaced by a note that was itself replaced later? "
                    f"Give the first note of each such line of replacements.",
                    [p for p in proj if cls(p) == c and notes[p]["superseded_by"] and not sup[p] and hops(p) >= 2]))
    out.append(("shared-dataset", "Which dataset notes are built on directly by notes of at least two projects other than their own?",
                [p for p in proj if cls(p) == "dataset"
                 and len({area(q) for q in down[p] if area(q) != area(p) and area(q) not in GENERAL}) >= 2]))
    out.append(("crossings", "Across every project, which notes are built directly on a note of another project? "
                "Leave out the general folders (prefs, reporting, glossary, corrections, howto, qa, log).",
                [p for p in proj if any(area(q) != area(p) and area(q) not in GENERAL for q in up[p])]))
    return [{"type": t, "q": q, "gold": sorted(g), "notes": sorted(g), "a": ", ".join(sorted(g))} for t, q, g in out if g]


def listed(section, gold):
    """The paths on the answer's "Notes:" line, normalised; a bare id counts as the gold note of that id if there is one."""
    m = re.search(r"^\s*Notes?:\s*(.*)$", section, flags=re.M | re.I)
    got = set()
    stems = {Path(gp).stem: gp for gp in gold}
    for tok in re.split(r"[,;\s]+", m.group(1) if m else ""):
        tok = tok.strip("`'\"()[]. ")
        if not tok or tok.lower() in ("none", "-"):
            continue
        tok = tok.split("memory/")[-1]
        tok = tok if tok.endswith(".md") else tok + ".md"
        got.add(tok if "/" in tok else stems.get(tok[:-3], tok))
    return got


def tally(qs, text, strict=False):
    """One answer file against its questions → (exact, whole set named, mean recall, mean precision, exact by kind).
    strict=True also counts against an answer the note its question names, when the answer lists it beside the set."""
    parts = re.split(r"^##\s*Q(\d+)\b.*$", text, flags=re.M)
    secs = {int(parts[i]): parts[i + 1] for i in range(1, len(parts) - 1, 2)}
    rec, pre, exact, full, by = [], [], 0, 0, collections.defaultdict(lambda: [0, 0])
    if True:
        for i, q in enumerate(qs, 1):
            gold, got = set(q["gold"]), listed(secs.get(i, ""), q["gold"])
            # a question that asks for one kind of note is scored on that kind: notes of another kind on the line are
            # the answer's support, not part of it
            pre_ = ASKS.get(q["type"])
            stem_ = lambda g: Path(g).stem  # noqa: E731
            if pre_:
                got = {g for g in got if stem_(g).startswith(pre_)}
            elif q["type"] == "stale-input":
                got = {g for g in got if not stem_(g).startswith(("ds-", "feat-"))}
            if not strict:  # the note a question names is its subject: listed beside the answer, it is not part of it
                got -= {g for g in got - gold if re.search(r"(?<![\w-])" + re.escape(stem_(g)) + r"(?![\w-])", q["q"])}
            r = len(gold & got) / len(gold)
            p = len(gold & got) / len(got) if got else 0.0
            rec.append(r)
            pre.append(p)
            exact += r == 1 and p == 1
            full += r == 1
            by[q["type"]][0] += r == 1 and p == 1
            by[q["type"]][1] += 1
    return exact, full, sum(rec) / len(rec), sum(pre) / len(pre), dict(by)


def score(qfile, files):
    qs = [json.loads(x) for x in Path(qfile).read_text().splitlines() if x.strip()]
    for f in files:
        exact, full, rec, pre, by = tally(qs, Path(f).read_text())
        hard = tally(qs, Path(f).read_text(), strict=True)[0]
        print(f"{Path(f).name}: {len(qs)} questions · exact {exact} ({hard} if the note a question names may not be listed) · "
              f"whole set named {full} · recall {rec:.2f} · precision {pre:.2f} · exact by kind: "
              + ", ".join(f"{t} {a}/{b}" for t, (a, b) in sorted(by.items())))


def ask_only(root, qfile):
    """With no agent at all: are the gold notes headed in what one `ask` call (ten questions) prints?"""
    qs = [json.loads(x) for x in Path(qfile).read_text().splitlines() if x.strip()]
    full, rec, chars = 0, [], 0
    for i in range(0, len(qs), 10):
        out = subprocess.run([sys.executable, str(MEM), "--root", str(root), "ask", *[q["q"] for q in qs[i:i + 10]]],
                             env=ENV, capture_output=True, text=True).stdout
        chars += len(out)
        parts = re.split(r"^## (.*)$", out, flags=re.M)
        for q, sec in zip(qs[i:i + 10], [parts[k + 1] for k in range(1, len(parts) - 1, 2)]):
            heads = set(re.findall(r"^▸ (\S+\.md)", sec, flags=re.M))
            ids = {h for h in heads} | {g for g in q["gold"] if Path(g).stem in sec}
            r = len(set(q["gold"]) & ids) / len(q["gold"])
            rec.append(r)
            full += r == 1
    print(f"ask alone: {len(qs)} questions · every gold note headed or named for {full} · recall {sum(rec) / len(rec):.2f} · "
          f"{chars / len(qs):,.0f} characters a question")


if __name__ == "__main__":
    a = sys.argv[1:]
    if len(a) >= 3 and a[0] == "make":
        n = int(a[a.index("--n") + 1]) if "--n" in a else 5
        qs, pool = make(a[1], n, a[a.index("--keep") + 1] if "--keep" in a else None)
        Path(a[2]).write_text("".join(json.dumps(q) + "\n" for q in qs))
        print(f"{len(qs)} questions to {a[2]} · candidates by kind: {pool} · gold notes a question: "
              f"{sum(len(q['gold']) for q in qs) / len(qs):.1f}")
    elif len(a) == 3 and a[0] == "global":
        qs = make_global(a[1])
        Path(a[2]).write_text("".join(json.dumps(q) + "\n" for q in qs))
        print(f"{len(qs)} questions to {a[2]} · gold notes: " + ", ".join(f"{q['type']} {len(q['gold'])}" for q in qs))
    elif len(a) >= 3 and a[0] == "score":
        score(a[1], a[2:])
    elif len(a) == 3 and a[0] == "ask":
        ask_only(a[1], a[2])
    else:
        raise SystemExit(__doc__)
