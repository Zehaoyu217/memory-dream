#!/usr/bin/env python3
"""The worn bank's memory with no model call: what Haiku 5.5 read in its 1,677 notes on 2026-11-12 (142 packets of a
dozen notes, $1.27; then every line that states lineage read a second time, 1,462 lines in 50 calls, $0.18; RESULTS
phase S) and the registries its curator and review left ($0.12). Usage:

  python3 eval/bank/assemble.py eval/bank/generated tests/fixture/memory <tidy>/memory
  python3 eval/real/bank-index/restore.py <tidy>/memory
  python3 skills/memory-dream/scripts/memory.py --root <tidy>/memory dream      # the tidy bank, its links on frontmatter
  python3 eval/hard/make_hard.py <tidy>/memory <worn>                           # the worn bank and truth.json, no model
  python3 eval/real/worn-index/restore.py <worn>/memory                         # the readings and registries
  python3 skills/memory-dream/scripts/memory.py --root <worn>/memory dream      # 0 calls: lineage as the keepers read it
  python3 eval/hard/lineage_score.py <worn>/memory <worn>/truth.json

A reading is used only for a note whose text has the hash it was made from, so this works because make_hard.py
writes the same notes every time (a seed, and the phrases kept in eval/hard/handles.json). `SETUP.md` is the page the
memory was set up with, with its five proof questions. Pass --no-registries to restore the readings only.
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
