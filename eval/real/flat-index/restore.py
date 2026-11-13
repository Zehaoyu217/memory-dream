#!/usr/bin/env python3
"""The flat bank's memory with no model call: what Haiku 5.5 read in its 1,677 notes on 2026-11-12, when the 1,224
project notes were in one folder too large to list (RESULTS phase S, S7), and the registries its curator and review
left. Usage:

  python3 eval/bank/assemble.py eval/bank/generated tests/fixture/memory <tidy>/memory
  python3 eval/real/bank-index/restore.py <tidy>/memory
  python3 skills/memory-dream/scripts/memory.py --root <tidy>/memory dream      # the tidy bank, its links on frontmatter
  python3 eval/hard/make_hard.py <tidy>/memory <worn>                           # the worn bank and truth.json, no model
  python3 eval/hard/make_flat.py <worn> eval/questions/linkage-100.jsonl <flat> # the flat bank, its key and its questions
  python3 eval/real/flat-index/restore.py <flat>/memory                         # the readings and registries
  python3 skills/memory-dream/scripts/memory.py --root <flat>/memory dream      # 0 calls: lineage as the keepers read it
  python3 eval/hard/lineage_score.py <flat>/memory <flat>/truth.json
  python3 eval/linkage.py lineage <flat>/memory <flat>/questions.jsonl

A reading is used only for a note whose text has the hash it was made from, so this works because make_hard.py and
make_flat.py write the same notes every time. `SETUP.md` is the page the memory was set up with. Pass
--no-registries to restore the readings only.
"""
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main(argv):
    if len(argv) < 2:
        raise SystemExit(__doc__)
    root = Path(argv[1]).resolve()
    dd = root / "_dream" / "notes"
    dd.mkdir(parents=True, exist_ok=True)
    n = 0
    for p in (HERE / "notes").glob("*.json"):
        shutil.copy2(p, dd / p.name)
        n += 1
    regs = []
    if "--no-registries" not in argv:
        for f in ("KINDS.md", "TYPES.md", "EDGES.md", "ALIASES.md", "CONFLICTS.md", "SETUP.md"):
            if (HERE / f).exists():
                shutil.copy2(HERE / f, root / f)
                regs.append(f)
    print(f"restored {n} readings and {len(regs)} registries into {root}; run `memory.py --root {root} dream` (0 calls)")


if __name__ == "__main__":
    main(sys.argv)
