#!/usr/bin/env python3
"""Wall time and output size of one `ask` call per batch of 10 questions, for memories of different sizes.

  time_ask.py <memory root> [<memory root> ...]
"""
import json
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
MEM = HERE.parent / "skills/memory-dream/scripts/memory.py"
BATCHES = {b: [json.loads(x)["q"] for x in open(HERE / "agent/batches" / f"{b}.jsonl")] for b in ("P1", "P2", "C-orig")}
for r in sys.argv[1:]:
    for b, qs in BATCHES.items():
        extra = ["-p", "churn-2026"] if b == "C-orig" else []
        t = time.time()
        out = subprocess.run(["python3", str(MEM), "--root", r, "ask", *extra, *qs], capture_output=True, text=True).stdout
        print(f"{Path(r).parent.name} {b}: {time.time() - t:.1f}s · {len(out):,} chars printed")
