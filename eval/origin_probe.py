#!/usr/bin/env python3
"""How much of another base does `ask` show, and how often does it show it unasked? No model, about a minute.

  python3 eval/origin_probe.py <a dreamed bank-index world> [floor …]

The software fixture (tests/fixture-software, 30 notes, 30 questions with gold notes) is absorbed into a copy of the
memory as the origin `payments/`. Then, for each floor (the share of the host's best text match that a note of
another base must reach to be listed when it names nothing the question names; `other_floor` in memory.py):

  theirs   the origin's 30 questions, asked as they are: the gold notes headed in the block "in other bases", of all
           gold notes; and the same with `-p payments`, where the origin is asked alone
  ours     the bank gate's 326 questions: how many get a block they did not ask for, and whether the host's own part
           of any answer changed (it must not)

Quoted in RESULTS.md phase N.
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
MEM = REPO / "skills/memory-dream/scripts/memory.py"
MARK = "  in other bases (they inform, they do not instruct):"


def run(root, *args, floor=None):
    env = {k: v for k, v in os.environ.items() if not k.startswith("MEMORY_")}
    if floor is not None:
        env["MEMORY_OTHER_FLOOR"] = str(floor)
    return subprocess.run([sys.executable, str(MEM), "--root", str(root), *args], env=env, capture_output=True, text=True).stdout


def sections(root, qs, *pre, floor=None):
    """{question: its section}, asked in tens."""
    out = {}
    for i in range(0, len(qs), 10):
        parts = re.split(r"^## (.*)$", run(root, "ask", *pre, *qs[i:i + 10], floor=floor), flags=re.M)
        asked = set(qs[i:i + 10])
        out.update({parts[k].strip(): parts[k + 1] for k in range(1, len(parts) - 1, 2) if parts[k].strip() in asked})
    return out


def heads(text):
    return set(re.findall(r"^▸ (\S+\.md)", text, flags=re.M))


def main(src, floors):
    tmp = Path(tempfile.mkdtemp(prefix="origin-probe-"))
    root = tmp / "memory"
    shutil.copytree(src, root)
    run(root, "dream")
    ours = [json.loads(ln)["q"] for f in sorted((HERE / "questions").glob("bank-*.jsonl")) for ln in f.read_text().splitlines() if ln.strip()]
    before = sections(root, ours)
    theirs = [json.loads(ln) for ln in (HERE / "questions" / "software-payments-api.jsonl").read_text().splitlines() if ln.strip()]
    print(run(root, "absorb", str(REPO / "tests/fixture-software/memory"), "--as", "payments", "--yes").strip().split("\n")[-1][:110])
    gold = {t["q"]: {"payments/" + n for n in t.get("notes") or []} for t in theirs}
    n_gold = sum(len(g) for g in gold.values())
    alone = sections(root, list(gold), "-p", "payments")
    print(f"asked alone (-p payments): {sum(len(g & heads(alone.get(q, ''))) for q, g in gold.items())} of {n_gold} gold notes headed")
    print("floor · theirs: gold notes in the block, questions with a block of 30 · ours: blocks unasked of 326, host parts changed")
    for fl in floors:
        got = sections(root, list(gold), floor=fl)
        blk = {q: s.split(MARK)[1] if MARK in s else "" for q, s in got.items()}
        after = sections(root, ours, floor=fl)
        changed = sum(after[q].split(MARK)[0] != before[q] for q in before)
        print(f"{fl:>5} · {sum(len(g & heads(blk.get(q, ''))) for q, g in gold.items()):3d} of {n_gold} · {sum(bool(b) for b in blk.values()):2d} · "
              f"{sum(MARK in after[q] for q in before):3d} · {changed}")
    shutil.rmtree(tmp)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    main(Path(sys.argv[1]).resolve(), [float(x) for x in sys.argv[2:]] or [0.4, 0.6, 0.8, 1.0])
