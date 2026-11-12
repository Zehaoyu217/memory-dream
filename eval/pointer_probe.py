#!/usr/bin/env python3
"""How long does a pointer into code stay right? Measured on this repository's own history. No model, git only.

  python3 eval/pointer_probe.py [file ...]        default: skills/memory-dream/scripts/memory.py and stores.py

A note about code points at it: `memory.py:2440`, or `memory.py#grep_lines`. For each earlier version of a file, every
definition line (`def`, `class`, a top-level NAME =) is taken as a pointer written that day, in three forms, and
looked up in the file as it is now:

  by line     the same text is still on the same line
  by quote    the same text is on exactly one line of the file, wherever it moved to
  by symbol   a definition of the same name still exists

  python3 eval/pointer_probe.py --built [file ...]

The same history put to the lookup that ships (`pointer_states` in memory.py, phase O). Every definition whose name
is defined once in the old version is pointed at in the three forms a note can use, seen once with the old file in
place as a dream would see it, and looked up again with today's file in place as `ask` does. Scored against where
that definition is today:

  right line        the state is intact or moved, and the line it gives is the definition's line today
  gone, said        the definition no longer exists and the state is changed
  edited, said      the definition exists, its line was edited, and the state is changed (the words are not there)
  wrong line        the state is intact or moved and the line it gives is not the definition's: the one harmful answer

Quoted in .specs/memory-dream/PLAN.md (rev 3) and RESULTS.md phases K and O.
"""
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DEF = re.compile(r"^\s*(?:def|class)\s+(\w+)|^([A-Z][A-Z0-9_]+)\s*=")


def git(*args):
    return subprocess.run(["git", *args], cwd=REPO, capture_output=True, text=True).stdout


def anchors(text):
    """[(line number, line text, symbol)] for every definition line."""
    out = []
    for i, ln in enumerate(text.split("\n"), 1):
        m = DEF.match(ln)
        if m:
            out.append((i, ln.rstrip(), m.group(1) or m.group(2)))
    return out


def probe(path):
    now = (REPO / path).read_text().split("\n")
    now_r = [ln.rstrip() for ln in now]
    count = {}
    for ln in now_r:
        count[ln] = count.get(ln, 0) + 1
    names = {a[2] for a in anchors("\n".join(now))}
    shas = [x.split(" ", 1) for x in git("log", "--format=%h %ad", "--date=short", "--", path).splitlines()]
    print(f"{path}: {len(now)} lines now, {len(shas)} versions in git")
    print("  versions back · date · pointers · right by line · found by quote · found by symbol · gone")
    for back in (1, 2, 5, 10, 20, len(shas) - 1):
        if back >= len(shas) or back < 1:
            continue
        sha, date = shas[back]
        old = anchors(git("show", f"{sha}:{path}"))
        if not old:
            continue
        line = sum(1 for i, t, _ in old if i <= len(now_r) and now_r[i - 1] == t)
        quote = sum(1 for _, t, _ in old if count.get(t) == 1)
        sym = sum(1 for _, _, s in old if s in names)
        n = len(old)
        print(f"  {back:>3} · {date} · {n:>3} · {line / n:5.0%} · {quote / n:5.0%} · {sym / n:5.0%} · {(n - sym) / n:4.0%}")


def quote_of(line):
    """The few words an agent would quote from a definition line: up to its first double quote, 80 characters, whole
    words."""
    q = " ".join(line.split('"')[0].split())
    return (q if len(q) <= 80 else q[:80].rsplit(" ", 1)[0]).strip()


def built(path):
    sys.path.insert(0, str(REPO / "skills/memory-dream/scripts"))
    import memory as M
    name = Path(path).name
    today = (REPO / path).read_text()
    where = {}
    for i, _, s in anchors(today):
        where.setdefault(s, []).append(i)
    shas = [x.split(" ", 1) for x in git("log", "--format=%h %ad", "--date=short", "--", path).splitlines()]
    print(f"{path}: {len(today.splitlines())} lines now, {len(shas)} versions in git · the lookup that ships")
    print("  versions back · pointers · form · right line · gone, said · edited, said · wrong line")
    for back in (1, 2, 5, 10, 20, len(shas) - 1):
        if back >= len(shas) or back < 1:
            continue
        old = git("show", f"{shas[back][0]}:{path}")
        seen = {}
        for i, t, s in anchors(old):
            seen.setdefault(s, []).append((i, t))
        defs = [(s, v[0][0], v[0][1]) for s, v in seen.items() if len(v) == 1 and len(where.get(s, [])) <= 1
                and len(quote_of(v[0][1])) >= 3]
        forms = {"symbol": [{"to": name, "symbol": s} for s, _, _ in defs],
                 "quote": [{"to": name, "line": i, "quote": quote_of(t)} for _, i, t in defs],
                 "bare line": [{"to": name, "line": i, "quote": None} for _, i, _ in defs]}
        with tempfile.TemporaryDirectory() as tmp:
            proj = Path(tmp) / "proj"
            (proj / "memory").mkdir(parents=True)
            os.environ["MEMORY_CODE"] = str(proj)
            (proj / name).write_text(old)
            first = M.pointer_states(proj / "memory", forms, {})[0]      # as the dream that first saw them
            (proj / name).write_text(today)
            now = M.pointer_states(proj / "memory", forms, first)[0]     # as `ask` looks them up today
        for form in forms:
            c = {"right": 0, "gone": 0, "edited": 0, "wrong": 0}
            for (s, _, _), r in zip(defs, now.get(form, [])):
                truth = (where.get(s) or [None])[0]
                if r["state"] in ("intact", "moved"):
                    c["right" if r["now"] == truth else "wrong"] += 1
                else:
                    c["gone" if truth is None else "edited"] += 1
            n = len(defs)
            print(f"  {back:>3} · {n:>3} · {form:<9} · {c['right'] / n:5.0%} · {c['gone'] / n:5.0%} · {c['edited'] / n:5.0%} · "
                  f"{c['wrong'] / n:5.1%} ({c['wrong']})")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--built"]
    for p in args or ["skills/memory-dream/scripts/memory.py", "skills/memory-dream/scripts/stores.py"]:
        (built if "--built" in sys.argv else probe)(p)
