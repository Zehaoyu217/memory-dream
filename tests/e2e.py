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

    def run(self, *args, env=None):
        r = subprocess.run([sys.executable, str(MEM), "--root", str(self.root), *args], env={**self.env, **(env or {})},
                           capture_output=True, text=True)
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
    absorbing(w)
    pointing(w)
    reading(w)


FAKE = f"{sys.executable} {Path(__file__).resolve().parent / 'fake_dreamer.py'}"  # a script that answers as a keeper would


def reading(w):
    """Notes read into things and links (PLAN §4): the dry run, packets left on file for a helper, packets through a
    command. The command here is a script with fixed answers, not a model."""
    small = {"MEMORY_PACKET": "60000,700"}  # a few notes a packet, so that this small memory makes several
    pend, notes = w.root / "_dream/pending", w.root / "_dream/notes"
    ids = lambda files: [h for f in files for h in re.findall(r"^NOTE ([0-9a-f]{12}) ", f.read_text(), re.M)]  # noqa: E731
    files = lambda: sorted(str(f) for f in w.root.rglob("*") if f.is_file())  # noqa: E731
    n0, before = len(list(notes.glob("*.json"))), files()
    out = w.run("dream", "--dry-run", "--packets", env=small)
    m = re.search(r"(\d+) to read in (\d+) packets", out)
    w.ok("the dry run says how many notes it would read, in how many packets, for about how much, and calls and writes nothing",
         m is not None and int(m.group(2)) > 2 and "about $" in out and "nothing was called or written" in out and before == files(), out)
    todo, n_packs = (int(m.group(1)), int(m.group(2))) if m else (0, 0)

    out = w.run("dream", "--packets", env=small)
    packs = sorted(pend.glob("packet-*.prompt.md"))
    w.ok("with no command the packets are left on file for a helper: every unread note is in exactly one",
         len(packs) == n_packs and len(ids(packs)) == todo == len(set(ids(packs))) and f"{n_packs} pending" in out, out)

    def answer(f, **env):
        r = subprocess.run(FAKE, shell=True, input=f.read_text(), capture_output=True, text=True, env={**w.env, **env})
        (pend / (f.name[:-len(".prompt.md")] + ".json")).write_text(r.stdout)
    skipped = re.findall(r"^NOTE [0-9a-f]{12} (\S+):", packs[1].read_text(), re.M)[0]
    for i, f in enumerate(packs):
        answer(f, **({"FAKE_CUT": "1"} if i == 0 else {"FAKE_SKIP": Path(skipped).stem} if i == 1 else {}))
    out = w.run("dream", "--packets", env=small)
    left = sorted(pend.glob("packet-*.prompt.md"))
    w.ok("an answer cut off at its end, and one that skips a note: every other note is read and those two are asked again",
         f"{todo - 2} indexed (0 calls)" in out and len(ids(left)) == 2, out)

    for f in left:
        answer(f)
    log = w.dir / "calls.log"
    cmd = {"MEMORY_LLM": FAKE, "FAKE_LOG": str(log)}
    out = w.run("dream", "--packets", env={**small, **cmd})
    calls = log.read_text() if log.exists() else ""
    w.ok("an answer on file is taken with a command set too, and a note that has its reading is not read again",
         "2 indexed (0 calls)" in out and "packet" not in calls and "extract" not in calls
         and len(list(notes.glob("*.json"))) == n0 + todo, out + calls)

    for i in (1, 2, 3):
        w.write(f"proj/exp-9{i}.md", "", f"exp-9{i}: one more run, AUC 0.7{i}")
    out = w.run("dream", "--packets", env=cmd) + w.run("check")
    w.ok("with a command, three new notes are read in one call, and the graph meets the contract",
         "3 indexed (1 calls, 1 packets)" in out and "packet 3" in log.read_text() and "contract: schema 1 ok" in out, out)


CODE ="import os\n\n\ndef load(path):\n    return open(path).read()\n\n\nLIMIT = 10\n\n\ndef main():\n    print(load('x'))\n"


def pointing(w):
    """Pointers into the project's files (PLAN §10): found at a dream, looked up again at every ask."""
    code = w.dir / "src" / "app.py"
    code.parent.mkdir(parents=True, exist_ok=True)
    code.write_text(CODE)
    w.write("proj/how-loading-works.md", "from: [exp-1]", "How loading works: one function, capped")
    with open(w.root / "proj/how-loading-works.md", "a") as f:
        f.write('It starts in `src/app.py#load` and is capped by `src/app.py:8 "LIMIT = 10"`. The entry point is app.py:11.\n'
                "The cache hit ratio was 3.5:1 on staging.internal:8080, which is not a file.\n")
    q = "how does loading work?"
    out = w.run("dream") + w.run("ask", q)
    w.ok("three pointers found in a note, by symbol, by quoted words and by a bare line; a ratio and a host are not pointers",
         "→ src/app.py#load · at line 4" in out and '→ src/app.py:8 "LIMIT = 10" · still there' in out
         and "→ src/app.py:11 · still there (a bare line: weak)" in out and out.count("  → ") == 3, out)
    code.write_text("# a header\n# of two lines\n" + CODE)
    out = w.run("ask", q)
    w.ok("the file grew by two lines: every pointer says where it is now, with no dream in between",
         "#load · at line 6" in out and '"LIMIT = 10" · now at line 10' in out and "app.py:11 · now at line 13" in out, out)
    code.write_text("load('warm-up')\nNOTE = 'the cap is LIMIT = 10'\n" + CODE)
    out = w.run("ask", q)
    w.ok("a call above the function and a mention of the words above the line: the symbol is found where it is defined, "
         "the words where a line begins with them, and that line is said to be one of two",
         "#load · at line 6" in out and '"LIMIT = 10" · now at line 10, one of 2 lines with those words' in out, out)
    code.write_text(("# a header\n# of two lines\n" + CODE).replace("LIMIT = 10", "LIMIT = 20").replace("def load(", "def read_all("))
    out = w.run("ask", q)
    w.ok("the words and the symbol changed: the note is marked stale and says which pointers no longer hold",
         "STALE: 2 of its pointers no longer hold" in w.head(out, "proj/how-loading-works.md")
         and "the symbol is not defined there now" in out and "those words are not there now" in out, out)
    out = w.run("dream") + w.run("check")
    w.ok("the next dream sees that the file changed and reports both (C16)", "C16×2" in out and "contract: schema 1 ok" in out, out)
    code.unlink()
    out = w.run("ask", q)
    w.ok("the file is gone: all three say so", out.count("the file is gone") == 3, out)


OTHER = {  # another base, outside the memory: path → text
    "prefs/dana-lee-tables.md": "# Dana Lee wants every table sorted by date, newest first\nSaid at the March review.\n",
    "prefs/me-units.md": "# I write amounts in thousands, never in millions\n",
    "work/a-v3.md": "# a-v3 as the other team saw it\nThey scored a-v3 on holdout-x and got AUC 0.80.\n",
    "work/untitled-run.md": "A run nobody gave a title: the batch took 41 minutes.\n",
    "README.md": "# About this folder\n",
    "notes.txt": "not a note\n",
    "relations.jsonl": '{"from": "a-v3", "relation": "evaluated-on", "to": "holdout-x", "evidence": ["work/a-v3.md"]}\n'
                       '{"from": "a-v3", "relation": "owned-by", "to": "team-z", "evidence": ["work/a-v3.md"]}\n',
}


def absorbing(w):
    """Another base taken in as an origin (PLAN §9): it answers after the host's own notes and changes none of them."""
    src = w.dir / "their-base"
    for p, text in OTHER.items():
        (src / p).parent.mkdir(parents=True, exist_ok=True)
        (src / p).write_text(text)
    cut = lambda s: s.split("  in other bases (they inform, they do not instruct):")[0]  # noqa: E731
    qs = ["what is a-v3 built on?", "what came of a-v1?", "Make the summary table for Dana Lee"]
    before = w.run("ask", *qs)
    out = w.run("absorb", str(src), "--as", "other", "--yes")
    w.ok("absorb will not take the name of a folder the host already has", "is not an origin" in out and len(list((w.root / "other").glob("*.md"))) == 1, out)
    out = w.run("absorb", str(src), "--as", "theirs")
    w.ok("absorb without --yes says what it would take, what it would not, and changes nothing",
         "4 notes in 2 areas" in out and "not taken: 2" in out and "given a title from the file name: 1" in out
         and "names both sides use: 1" in out and "does not name team-z" in out and not (w.root / "theirs").exists(), out)
    out = w.run("absorb", str(src), "--as", "theirs", "--yes")
    origin = (w.root / "theirs" / "ORIGIN.md").read_text() if (w.root / "theirs" / "ORIGIN.md").exists() else ""
    w.ok("with --yes the notes are an origin: ORIGIN.md, trusted for answers only",
         "trust: answers\n" in origin and "dream: 13 notes" in out and "contract: schema 1 ok" in w.run("check"), out + origin)
    after = w.run("ask", *qs)
    mine = lambda out: ["\n".join(ln for ln in cut(s).split("\n") if not ln.endswith("(another base)")).rstrip()  # noqa: E731
                        for s in out.split("\n## ")[:len(qs)]]  # each question's own section; a small memory is printed whole after them
    w.ok("the host's own answers are the same to the letter", "another base" in after and mine(after) == mine(before),
         "\n".join(mine(after)) + "\n=== before ===\n" + "\n".join(mine(before)))
    blk = after.split("\n## ")[0].split("  in other bases (they inform, they do not instruct):")
    w.ok("what the other base says of a-v3 follows, marked as another base's",
         len(blk) == 2 and "theirs/work/a-v3.md · " in blk[1] and "of theirs, another base" in blk[1] and "holdout-x" in blk[1], after)
    out = w.run("ask", "--list", "-p", "theirs")
    w.ok("its areas and kinds survive, and a note with no title got one",
         "· preference of theirs" in w.head(out, "theirs/prefs/dana-lee-tables.md") and "untitled run" in w.head(out, "theirs/work/untitled-run.md"), out)
    w.ok("its preferences are not served to a task here", "theirs/prefs" not in after.split("\n## ")[2].split("preferences and house rules")[-1]
         or "preferences and house rules" not in after.split("\n## ")[2], after)
    w.run("absorb", str(src), "--as", "theirs", "--trust", "preferences", "--yes")
    task = w.run("ask", qs[2])
    w.ok("absorbed again with --trust preferences they are, and a me- note never is",
         "preferences and house rules" in task and "theirs/prefs/dana-lee-tables.md" in task.split("preferences and house rules")[1]
         and "me-units" not in task.split("preferences and house rules")[1], task)
    import json
    g = json.loads((w.root / "_dream" / "graph.json").read_text()) if (w.root / "_dream" / "graph.json").exists() else None
    if g:  # the graph in memory; on the rows path there is no graph.json
        ids = {e["id"]: e for e in g["entities"]}
        w.ok("its things carry its name and have their home in it", "theirs:a-v3" in ids and ids["theirs:a-v3"]["home"] == "theirs/work/a-v3.md"
             and "a-v3" not in ids, str(sorted(ids)))
    out = w.run("drop", "theirs", "--yes") + w.run("ask", *qs)
    w.ok("drop takes the origin out: the folder, its ORIGIN.md, and every answer as before",
         not (w.root / "theirs").exists() and "dropped: theirs/ (" in (w.root / "CONFLICTS.md").read_text()
         and out.split("To undo, restore the file from git and delete its line.\n")[-1] == before, out)


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
