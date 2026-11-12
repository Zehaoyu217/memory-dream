#!/usr/bin/env python3
"""One run from an empty folder to a memory that has lost notes on purpose and by accident. No model, a few seconds.

  python3 tests/e2e.py            both read paths: the graph in memory, and rows on demand (MEMORY_WIDE=5)
  python3 tests/e2e.py --keep     leave the two worlds on disk and print where

It writes fourteen small notes, dreams, asks, deletes a note by hand, drops notes and a folder with `memory.py drop`,
and checks after each step what a reader is shown. The plan's proof (PLAN.md §14) grows here step by step; this is
step 0: a note that leaves must not bring back the note it had replaced, and `ask` must survive a missing file.
Exit 1 when a line fails.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

MEM = Path(__file__).resolve().parent.parent / "skills/memory-dream/scripts/memory.py"
NOTES = {  # path: (frontmatter lines, title)
    "proj/exp-1.md": ("", "exp-1: baseline run, AUC 0.71"),
    "proj/exp-2.md": ("", "exp-2: leak check, AUC 0.74"),
    "proj/a-v1.md": ("from: [exp-1]", "a-v1: first model, AUC 0.71"),
    "proj/a-v2.md": ("from: [exp-1]\nsupersedes: [a-v1]", "a-v2: second model, AUC 0.81"),
    "proj/a-v3.md": ("from: [a-v2, exp-2]\nsupersedes: [a-v2]", "a-v3: third model, AUC 0.76 with no leak"),
    "proj/dec-ship.md": ("from: [a-v2]", "Decision: ship the second model to scoring"),
    "proj/claim-1.md": ("source: [proj/a-v2.md]", "The second model reached AUC 0.81"),
    "proj/claim-2.md": ("source: [proj/a-v2.md, proj/exp-1.md]", "The second model beat the baseline by 0.10"),
    "proj/uses-x.md": ("from: [ext/x-1]", "A check that borrows the outside list x-1"),
    "other/b-v1.md": ("", "b-v1: tier cut at 0.20"),
    "other/b-v2.md": ("supersedes: [b-v1]", "b-v2: tier cut at 0.25"),
    "ext/x-1.md": ("", "x-1: an outside list of holidays"),
    "ext/x-2.md": ("from: [x-1]", "x-2: the list with regional days added"),
    "ext/x-3.md": ("supersedes: [x-2]", "x-3: the list for 2027"),
}


class World:
    def __init__(self, wide):
        self.dir = Path(tempfile.mkdtemp(prefix="memory-e2e-"))
        self.root = self.dir / "memory"
        self.env = {k: v for k, v in os.environ.items() if not k.startswith("MEMORY_")}
        if wide:
            self.env["MEMORY_WIDE"] = "5"
        self.bad = 0
        for p, (fm, title) in NOTES.items():
            self.write(p, fm, title)

    def write(self, p, fm, title):
        f = self.root / p
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(f"---\nupdated: 2026-01-0{1 + len(p) % 9}\n{fm + chr(10) if fm else ''}---\n# {title}\nA line about {title.split(':')[0]}.\n")

    def run(self, *args):
        r = subprocess.run([sys.executable, str(MEM), "--root", str(self.root), *args], env=self.env, capture_output=True, text=True)
        return r.stdout + r.stderr

    def head(self, out, note):
        """The header line of a note in what ask printed."""
        return next((ln for ln in out.split("\n") if ln.startswith(f"▸ {note}")), "")

    def ok(self, what, cond, shown=""):
        self.bad += not cond
        print(f"  {'ok  ' if cond else 'FAIL'} {what}" + (f"\n       {shown.strip()[:300]}" if not cond else ""))


def scenario(w):
    out = w.run("dream")
    w.ok("a dream of fourteen notes", "dream: 14 notes" in out, out)
    out = w.run("check")
    w.ok("the graph meets the contract", "contract: schema 1 ok" in out, out)
    out = w.run("ask", "what came of a-v1?")
    w.ok("a-v1 is history, to the end of its line", "SUPERSEDED → a-v2 → a-v3" in w.head(out, "proj/a-v1.md"), out)
    out = w.run("ask", "--list", "-p", "proj")
    w.ok("the map marks an input that was replaced", "a-v2 (replaced)" in w.head(out, "proj/dec-ship.md"), out)

    (w.root / "proj/a-v2.md").unlink()  # by hand, the way a branch switch or a wrong `rm` does it
    out = w.run("ask", "what came of a-v1?", "what is a-v3 built on?")
    w.ok("ask survives a file that is gone", "Traceback" not in out and w.head(out, "proj/a-v1.md") != "", out)
    out = w.run("dream") + w.run("check")
    w.ok("the dream says the note is gone and names the command", "C15" in out and "drop proj/a-v2.md --yes" in out, out)
    w.ok("nothing was written for it", "dropped:" not in ((w.root / "CONFLICTS.md").read_text() if (w.root / "CONFLICTS.md").exists() else ""))

    before = sorted(str(p) for p in w.root.rglob("*.md"))
    out = w.run("drop", "proj/a-v2.md")
    w.ok("drop without --yes prints the plan and changes nothing",
         "nothing is changed yet" in out and "a-v3.md replaced it" in out and before == sorted(str(p) for p in w.root.rglob("*.md")), out)
    out = w.run("drop", "proj/a-v2.md", "--yes")
    line = [ln for ln in (w.root / "CONFLICTS.md").read_text().split("\n") if ln.startswith("dropped: proj/a-v2.md")]
    w.ok("one tombstone, with what it had replaced", len(line) == 1 and line[0].endswith("> proj/a-v1.md"), out + str(line))
    w.ok("made from it alone: dropped as well; made from two: kept",
         not (w.root / "proj/claim-1.md").exists() and (w.root / "proj/claim-2.md").exists(), out)
    out = w.run("ask", "what came of a-v1?", "what is a-v3 built on?", "why did we ship in dec-ship?")
    w.ok("the chain holds: a-v3 now replaces a-v1", "SUPERSEDED → a-v3" in w.head(out, "proj/a-v1.md"), out)
    w.ok("notes built on it stay and say so", "a-v2 (dropped)" in w.head(out, "proj/a-v3.md")
         and "a-v2 (dropped)" in w.head(out, "proj/dec-ship.md"), out)
    out = w.run("check")
    w.ok("C14 for what was built on it, no C15 and no 'not found' left",
         "C14" in out and "C15" not in out and "a-v2 not found" not in out and "contract: schema 1 ok" in out, out)

    out = w.run("drop", "b-v2", "--yes") + w.run("ask", "what is the tier cut in b-v1?")
    w.ok("a note named by its id; the end of a line dropped: the one before is the newest left, and says so",
         "its replacement b-v2 was dropped" in w.head(out, "other/b-v1.md") and "SUPERSEDED" not in w.head(out, "other/b-v1.md"), out)

    out = w.run("drop", "ext", "--yes")
    text = (w.root / "CONFLICTS.md").read_text()
    w.ok("a folder: one line for it, one more for the note someone outside had built on",
         "dropped: ext/ (" in text and "dropped: ext/x-1.md (" in text and "dropped: ext/x-2.md" not in text and not (w.root / "ext").exists(), out + text)
    out = w.run("ask", "--list", "-p", "proj")
    w.ok("the note built on the folder stays and says so", "x-1 (dropped)" in w.head(out, "proj/uses-x.md"), out)

    shutil.rmtree(w.root / "_dream")  # a fresh clone: the notes and CONFLICTS.md, no old graph
    first = w.run("dream")
    out = first + w.run("ask", "what came of a-v1?")
    w.ok("the same from the files alone", "dream: 8 notes" in out and "SUPERSEDED → a-v3" in w.head(out, "proj/a-v1.md"), out)
    lines = (w.root / "CONFLICTS.md").read_text()
    out = w.run("dream")
    w.ok("a second dream reports the same; five tombstones, all written by drop",
         out == first and (w.root / "CONFLICTS.md").read_text() == lines and lines.count("\ndropped: ") == 5, first + out + lines)

    w.write("proj/a-v2.md", "from: [exp-1]\nsupersedes: [a-v1]", "a-v2: second model, AUC 0.81")  # undo: the file is back
    out = w.run("dream") + w.run("check") + w.run("ask", "what came of a-v1?")
    w.ok("the file put back counts again, and its stale line is reported",
         "SUPERSEDED → a-v2 → a-v3" in w.head(out, "proj/a-v1.md") and re.search(r"dropped: proj/a-v2\.md names a note that exists", out) is not None, out)


def main():
    keep, bad = "--keep" in sys.argv, 0
    for wide in (False, True):
        w = World(wide)
        print("rows on demand (MEMORY_WIDE=5)" if wide else "the graph in memory")
        scenario(w)
        bad += w.bad
        print(f"  world kept: {w.dir}") if keep else shutil.rmtree(w.dir)
    print("e2e ok" if not bad else f"e2e FAILED: {bad} lines")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
