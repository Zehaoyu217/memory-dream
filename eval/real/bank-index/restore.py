#!/usr/bin/env python3
"""Rebuild the real Haiku index of the 1,677-note bank with no model calls: the dreamer's readings (one JSON per note
content, keyed by sha) and the registries the review produced, as they were on 2026-11-02 ($2.72 of Haiku; RESULTS
phase I). Usage:

  python3 eval/bank/assemble.py eval/bank/generated tests/fixture/memory <out>/memory
  python3 eval/real/bank-index/restore.py <out>/memory          # copies the readings and registries into the memory
  python3 skills/memory-dream/scripts/memory.py --root <out>/memory dream    # 0 calls: the graph is derived from them

The notes stay the truth; a reading is used only for a note whose content hash matches (an edited note is unindexed again).
The registries carry types on probation dated 2026-11-02; after 60 days a later dream may demote the ones still under the
bar (0 calls), which changes the graph slightly. Pass --no-registries to restore the readings only.
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
        for f in ("KINDS.md", "TYPES.md", "EDGES.md", "ALIASES.md", "CONFLICTS.md"):
            if (HERE / f).exists():
                shutil.copy2(HERE / f, root / f)
                regs.append(f)
    print(f"restored {n} readings and {len(regs)} registries into {root}; run `memory.py --root {root} dream` (0 calls)")


if __name__ == "__main__":
    main(sys.argv)
