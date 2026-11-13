#!/usr/bin/env python3
"""One run from an empty folder to a memory that has lost notes on purpose and by accident. No model, a few seconds.

  python3 tests/e2e.py            both read paths: the graph in memory, and rows on demand (MEMORY_WIDE=5)
  python3 tests/e2e.py --keep     leave the two worlds on disk and print where

It writes fourteen small notes, dreams, asks, deletes a note by hand, drops notes and a folder with `memory.py drop`,
and checks after each step what a reader is shown. The plan's proof (PLAN.md §14) grows here step by step; this is
step 0: a note that leaves must not bring back the note it had replaced, and `ask` must survive a missing file.
Exit 1 when a line fails.
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
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
    vocabulary(w)
    naming(w)
    placing(w)
    proving(w)


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

    w.write("proj/exp-94.md", "", "exp-94: a run that no command will read")
    pid_file, t0 = w.dir / "hang.pid", time.time()
    out = w.run("dream", env={"MEMORY_LLM": f"{sys.executable} {Path(__file__).resolve().parent / 'hang_cmd.py'}",
                              "MEMORY_TIMEOUT": "2", "HANG_PID": str(pid_file)})
    took, alive = time.time() - t0, True
    for _ in range(40):  # what the command started is ended with it; give the system a moment to clear it away
        try:
            os.kill(int(pid_file.read_text()), 0)
            time.sleep(0.1)
        except (OSError, ValueError):
            alive = False
            break
    w.ok("a command that never answers is ended after MEMORY_TIMEOUT with everything it started, tried once more, and the "
         "dream goes on with the note left unread", took < 60 and not alive and "1 pending" in out and "dream:" in out, f"{took:.0f} s · {out}")
    (w.root / "proj/exp-94.md").unlink()  # by hand, and recorded: the lines that follow count notes
    w.run("drop", "proj/exp-94.md", "--yes")


def vocabulary(w):
    """Words that belong to one base, on registry lines (PLAN §5 and §11): tags with their definitions, and the words
    of a question that make `ask` follow a type of link."""
    (w.root / "TAGS.md").write_text("# TAGS\n- risk: something that could go wrong, and who watches it | aka: risks, exposure\n")
    w.write("proj/risk-drift.md", "tags: [risk]", "risk-drift: the score drifts when the feed is late")
    w.write("proj/q-holdout.md", "tags: risks, open", "q-holdout: is the holdout still clean?")
    out = w.run("dream") + w.run("check")
    w.ok("a word that TAGS.md does not list is reported, the listed one is not, and TAGS.md is not taken for a note",
         "C17×1" in out and "tag `open` on 1 note" in out and "tag `risk`" not in out and "▸ TAGS.md" not in w.run("ask", "--list"), out)
    out = w.run("ask", "--list", "--tag", "exposure")
    w.ok("a tag is asked for by any of its spellings and comes with its definition",
         "## 2 notes tagged risk (something that could go wrong" in out and w.head(out, "proj/risk-drift.md") != ""
         and "#risk" in w.head(out, "proj/q-holdout.md"), out)
    out = w.run("ask", "--list", "--tag", "open") + w.run("ask", "--list", "--tag", "nothing")
    w.ok("an unlisted word still filters and says that it has no definition; an unknown one names the tags in use",
         "## 1 notes tagged open (not in TAGS.md" in out and "no note carries the tag nothing · tags in use: open (1), risk (2)" in out, out)

    edges = w.root / "EDGES.md"  # a type of link of this base's own, with the question words that follow it
    edges.write_text(edges.read_text() + "- cites: X refers to Y as a source | walk: cite*, ~cited by | hops: 2\n")
    w.write("lib/paper-a.md", "", "paper-a: a survey of drift tests")
    w.write("lib/paper-b.md", "", "paper-b: the first drift test")
    with open(w.root / "lib/paper-a.md", "a") as f:
        f.write("paper-a cites paper-b for the test it starts from.\n")
    sha = hashlib.sha256((w.root / "lib/paper-a.md").read_bytes()).hexdigest()[:12]
    (w.root / "_dream/pending").mkdir(parents=True, exist_ok=True)
    (w.root / "_dream/pending" / f"{sha}.json").write_text(json.dumps({  # a reading left on file, as any keeper may leave one
        "kind": "note", "entities": [{"id": "paper-a", "type": "document", "as": ["paper-a"]}, {"id": "paper-b", "type": "document", "as": ["paper-b"]}],
        "relations": [{"s": "paper-a", "type": "cites", "o": "paper-b", "quote": "paper-a cites paper-b"}], "refs": []}))
    out = w.run("dream") + w.run("ask", "what does paper-a cite?", env={"MEMORY_DEBUG": "1"})
    w.ok("a type of link this base added, with its own question words: `ask` follows it to the note of the thing cited",
         "cued=['cites']" in out and "added=['lib/paper-b.md']" in out, out)

    w.write("lib/paper-c.md", "", "paper-c: the drift test, run on card data")  # no frontmatter says what it rests on
    with open(w.root / "lib/paper-c.md", "a") as f:
        f.write("It takes the first drift test as its starting point.\n")
    sha = hashlib.sha256((w.root / "lib/paper-c.md").read_bytes()).hexdigest()[:12]
    (w.root / "_dream/pending" / f"{sha}.json").write_text(json.dumps({
        "kind": "note", "entities": [{"id": "paper-c", "type": "document", "as": ["paper-c"]}], "relations": [], "refs": [],
        "built_on": [{"what": "paper-b", "quote": "takes the first drift test as its starting point"},
                     {"what": "exp-1", "quote": "words that are not in the note"}]}))
    out = w.run("dream") + w.run("ask", "--list", "-p", "lib")
    w.ok("what a note says it starts from, in its prose alone, is lineage once a keeper has read it with the words that "
         "say so; an item whose words are not in the note is refused",
         "from paper-b" in w.head(out, "lib/paper-c.md") and "exp-1" not in w.head(out, "lib/paper-c.md"), out)


def naming(w):
    """Two names for one thing (PLAN §7): a curator reads a folder's things together and the join is a line with its
    reason. Nothing is proposed from how two names are spelled."""
    for i, words in enumerate(("risk-tier cuts", "risk-tier cuts", "risk tier cutoffs", "risk tier cutoffs"), 1):
        w.write(f"tiers/dec-tier-{i}.md", "", f"dec-tier-{i}: where the tiers are cut, part {i}")
        with open(w.root / f"tiers/dec-tier-{i}.md", "a") as f:
            f.write(f"The {words} were reviewed in month {i}.\n")
    log = w.dir / "naming.log"
    cmd = {"MEMORY_LLM": FAKE, "FAKE_LOG": str(log)}
    out = w.run("dream", env=cmd)
    line = next((ln for ln in (w.root / "ALIASES.md").read_text().split("\n") if "risk-tier" in ln), "")
    w.ok("two unlike names for one thing: the curator reads the folder's things together and joins them on one line, with "
         "its reason and its name on it", "curator: " in out and " | why: " in line and " | by: curator " in line
         and "curate" in log.read_text(), out + line)
    aliases = w.root / "ALIASES.md"
    aliases.write_text(aliases.read_text().replace(line + "\n", "") + "not: risk-tier-cuts / risk-tier-cutoffs\n")
    out = w.run("dream", env=cmd) + w.run("check")
    w.ok("a person's `not:` line overrules it: the folder is read again, the same answer comes back, and the script "
         "does not write the join a second time", "risk-tier-cuts = " not in aliases.read_text().replace("not: ", "")
         and "= risk-tier-cutoffs" not in aliases.read_text() and "contract: schema 1 ok" in out, out + aliases.read_text())


def placing(w):
    """A link the first reading could not place (RESULTS phase S): listed, and with a command read once more."""
    w.write("lib/paper-d.md", "", "paper-d: the drift test on loan data")
    with open(w.root / "lib/paper-d.md", "a") as f:
        f.write("Builds on the first drift test. It also builds on the lost appendix.\n")
    sha = hashlib.sha256((w.root / "lib/paper-d.md").read_bytes()).hexdigest()[:12]
    (w.root / "_dream/pending" / f"{sha}.json").write_text(json.dumps({
        "kind": "note", "entities": [{"id": "paper-d", "type": "document", "as": ["paper-d"]}], "relations": [], "refs": [],
        "built_on": [{"what": "first-drift-test", "quote": "Builds on the first drift test"},
                     {"what": "lost-appendix", "quote": "builds on the lost appendix"}]}))
    out = w.run("dream") + w.run("check")
    w.ok("a note says it builds on something by a phrase and the reading names no note: both are listed, with the words",
         "C18×2" in out and "says it builds on 'first-drift-test'" in out and "from" not in w.head(w.run("ask", "--list", "-p", "lib"), "lib/paper-d.md"), out)
    out, listed = w.run("ask", "what is paper-d built on?"), w.run("ask", "--list", "-p", "lib")
    w.ok("ask does not pass over it in silence: the note's own words are printed with the note, the chain says it is not "
         "whole, and the map carries them",
         "? it builds on «Builds on the first drift test», in its own words" in out and "not the whole chain: paper-d also builds on" in out
         and "builds on «builds on the lost appendix», no note placed" in w.head(listed, "lib/paper-d.md"), out + listed)
    log = w.dir / "placing.log"
    out = w.run("dream", "--review", env={"MEMORY_LLM": FAKE, "FAKE_LOG": str(log)})
    after = w.run("ask", "--list", "-p", "lib") + w.run("check")
    w.ok("with a command the line is read once more beside the folder's notes, every member of it: the one a note answers "
         "to becomes lineage, the other stays listed with its own words, and the line is not read a third time",
         "second reading: 1 line read once more, +1 link (1 call)" in out and "from paper-b" in w.head(after, "lib/paper-d.md")
         and "C18 ×1" in after and "says it builds on 'the lost appendix'" in after
         and "second reading" not in w.run("dream", "--review", env={"MEMORY_LLM": FAKE, "FAKE_LOG": str(log)}), out + after)
    w.write("lib/paper-e.md", "", "paper-e: a correction to the drift test")
    with open(w.root / "lib/paper-e.md", "a") as f:
        f.write("Replaces lib/paper-d.\n")
    sha = hashlib.sha256((w.root / "lib/paper-e.md").read_bytes()).hexdigest()[:12]
    (w.root / "_dream/pending" / f"{sha}.json").write_text(json.dumps({
        "kind": "note", "entities": [], "relations": [], "refs": [], "replaces": [{"what": "lib-paper-d", "quote": "Replaces lib/paper-d."}]}))
    out = w.run("dream") + w.run("ask", "--list", "-p", "lib")
    w.ok("an item named by something no note answers to, whose own words give one note's path: that note, with no call",
         "supersedes paper-d" in w.head(out, "lib/paper-e.md") and "C18×1" in out, out)
    w.write("lib/paper-f.md", "", "paper-f: drift on card data, a second look")
    with open(w.root / "lib/paper-f.md", "a") as f:
        f.write("Builds on the first drift test and paper-a.\n")
    sha = hashlib.sha256((w.root / "lib/paper-f.md").read_bytes()).hexdigest()[:12]
    (w.root / "_dream/pending" / f"{sha}.json").write_text(json.dumps({
        "kind": "note", "entities": [], "relations": [], "refs": [], "built_on": [{"what": "paper-a", "quote": "Builds on the first drift test and paper-a"}]}))
    save = w.dir / "placing-prompts"
    out = w.run("dream", "--review", env={"MEMORY_LLM": FAKE, "FAKE_LOG": str(log), "FAKE_SAVE": str(save), "MEMORY_FOLDER": "3"})
    asked = "".join(f.read_text() for f in sorted(save.glob("*-place.txt")))
    head = w.head(w.run("ask", "--list", "-p", "lib"), "lib/paper-f.md")
    w.ok("a folder with more notes than a prompt can list: the keeper is shown the notes near the line (those it names, and "
         "those whose first line shares its rarest words), and the phrase the first reading left out is placed",
         "too many to list. NEAR" in asked and "\npaper-b: " in asked and "paper-a" in head and "paper-b" in head,
         out + asked[asked.find("FOLDER"):] + head)


def proving(w):
    """A memory's own test (PLAN §13 item 6): questions kept in SETUP.md with the note that answers each."""
    (w.root / "SETUP.md").write_text("# SETUP\nfor: the end-to-end run.\n\n## proof\n"
                                     "- what does paper-a cite? -> lib/paper-b.md\n"
                                     "- is the holdout still clean? -> q-holdout\n"
                                     "- what is the tier cut? -> lib/paper-a.md\n")
    out = w.run("dream") + w.run("check") + w.run("ask", "--list")
    w.ok("check puts the questions of SETUP.md to ask and names the one its note does not answer; SETUP.md is no note",
         "proof: 2 of 3 questions of SETUP.md are answered by their note" in out
         and "not by lib/paper-a.md: what is the tier cut?" in out and "▸ SETUP.md" not in out, out)


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
