#!/usr/bin/env python3
"""How long does a pointer into code stay right? Measured on this repository's own history. No model, git only.

  python3 eval/pointer_probe.py [file ...]        default: skills/memory-dream/scripts/memory.py and stores.py

A note about code points at it: `memory.py:2440`, or `memory.py#grep_lines`. For each earlier version of a file, every
definition line (`def`, `class`, a top-level NAME =) is taken as a pointer written that day, in three forms, and
looked up in the file as it is now:

  by line     the same text is still on the same line
  by quote    the same text is on exactly one line of the file, wherever it moved to
  by symbol   a definition of the same name still exists

Quoted in .specs/memory-dream/PLAN.md (rev 3) and RESULTS.md phase K.
"""
import re
import subprocess
import sys
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


if __name__ == "__main__":
    for p in sys.argv[1:] or ["skills/memory-dream/scripts/memory.py", "skills/memory-dream/scripts/stores.py"]:
        probe(p)
