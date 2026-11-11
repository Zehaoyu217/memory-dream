#!/usr/bin/env python3
"""An experiment, not shipped code: `ask` for a cheap reader. The same call and the same notes as memory.py ask, but the
first notes of each question are printed whole instead of as two to four lines, because on a model that costs a
fortieth per token the expensive thing is another request, not more text.

  askfull.py --root <memory> ask "q1" "q2" ...        ASKFULL_NOTES (default 6) notes a question are printed whole
"""
import os
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
args = sys.argv[1:]
root = Path(args[args.index("--root") + 1]) if "--root" in args else None
out = subprocess.run([sys.executable, str(HERE / "memory.py"), *args], capture_output=True, text=True)
sys.stderr.write(out.stderr)
if "ask" not in args or root is None:
    sys.stdout.write(out.stdout)
    sys.exit(out.returncode)
FULL = int(os.environ.get("ASKFULL_NOTES", "6"))
res, n, skipping, shown = [], 0, False, set()
for ln in out.stdout.split("\n"):
    if ln.startswith("## "):
        n, skipping = 0, False
        res.append(ln)
        continue
    m = re.match(r"▸ (\S+\.md)", ln)
    if m:
        n += 1
        skipping = False
        res.append(ln)
        p = root / m.group(1)
        if n <= FULL and p.exists() and m.group(1) not in shown:
            shown.add(m.group(1))
            text = p.read_text().split("\n")
            body = 0
            if text and text[0].strip() == "---":
                body = next((i + 1 for i in range(1, len(text)) if text[i].strip() == "---"), 0)
            res += [f"  {i + 1}: {t}" for i, t in enumerate(text) if i >= body and t.strip()]
            skipping = True  # the excerpt lines that follow are already in the whole note
        continue
    if skipping and re.match(r"\s+\d+: ", ln):
        continue
    skipping = False
    res.append(ln)
sys.stdout.write("\n".join(res))
