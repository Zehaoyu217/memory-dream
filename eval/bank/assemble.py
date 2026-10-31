#!/usr/bin/env python3
"""Big bank = generated notes + the churn-2026 fixture; log days present in both are merged.

  assemble.py <generated dir> <fixture memory dir> <out memory dir>
"""
import shutil
import sys
from pathlib import Path

gen, fix, out = (Path(a) for a in sys.argv[1:4])
if out.exists():
    shutil.rmtree(out)
shutil.copytree(gen, out)
n = 0
for p in fix.rglob("*.md"):
    rel = p.relative_to(fix)
    dst = out / rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    if rel.parts[0] == "log" and dst.exists():
        items = [ln for ln in p.read_text().split("\n") if ln.startswith("- ")]
        have = [ln for ln in dst.read_text().split("\n") if ln.startswith("- ")]
        dst.write_text(dst.read_text().split("\n")[0] + "\n\n" + "\n".join(sorted(have + items)) + "\n")
    else:
        shutil.copy2(p, dst)
    n += 1
print(f"{sum(1 for _ in out.rglob('*.md'))} notes in {out} ({n} from the fixture)")
