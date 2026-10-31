#!/usr/bin/env python3
"""Where an incremental dream spends its time at scale: clone a memory, drop N notes' extractions, re-index them with
the local fake dreamer (no model cost), profile.

  profile_incremental.py <memory root> <scratch dir> [area] [top N]
"""
import contextlib
import cProfile
import importlib.util
import io
import json
import os
import pstats
import shutil
import subprocess
import sys
import time
from pathlib import Path

WT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("m", WT / "skills/memory-dream/scripts/memory.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
src, scratch = Path(sys.argv[1]), Path(sys.argv[2])
area = sys.argv[3] if len(sys.argv) > 3 else "fraud-2026"
if scratch.exists():
    shutil.rmtree(scratch)
scratch.mkdir(parents=True)
subprocess.run(["cp", "-cR", str(src), str(scratch / "memory")], check=True)
root = scratch / "memory"
man = json.loads((root / "_dream/manifest.json").read_text())
n = 0
for rel, f in man["files"].items():
    if rel.startswith(area + "/"):
        p = root / "_dream/notes" / f"{f['sha'][:12]}.json"
        if p.exists():
            p.unlink()
            n += 1
os.environ["MEMORY_LLM"] = f"{sys.executable} {WT / 'tests/fake_dreamer.py'}"
pr = cProfile.Profile()
t = time.time()
out = io.StringIO()
with contextlib.redirect_stdout(out):
    pr.enable()
    m.main(["dream", "--root", str(root), "-j", "10"])
    pr.disable()
print(out.getvalue().strip())
print(f"incremental dream ({n} notes re-indexed by the fake dreamer): {time.time() - t:.0f}s")
pstats.Stats(pr).sort_stats("cumulative").print_stats(r"memory\.py", int(sys.argv[4]) if len(sys.argv) > 4 else 25)
