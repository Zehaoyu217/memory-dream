#!/usr/bin/env python3
"""Where a dream with nothing new to index spends its time (cProfile, file mode, no model), and how big
each part of graph.json is.

  profile_dream.py <memory root> [top N]
"""
import cProfile
import contextlib
import importlib.util
import io
import json
import os
import pstats
import sys
import time
from pathlib import Path

spec = importlib.util.spec_from_file_location("m", Path(__file__).resolve().parents[2] / "skills/memory-dream/scripts/memory.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
os.environ.pop("MEMORY_LLM", None)
root = sys.argv[1]
pr = cProfile.Profile()
t = time.time()
with contextlib.redirect_stdout(io.StringIO()):
    pr.enable()
    m.main(["dream", "--root", root])
    pr.disable()
print(f"no-op dream: {time.time() - t:.0f}s")
st = pstats.Stats(pr)
st.sort_stats("cumulative").print_stats(r"memory\.py", int(sys.argv[2]) if len(sys.argv) > 2 else 25)
g = json.load(open(Path(root) / "_dream/graph.json"))
for k, v in g.items():
    print(f"  graph.json {k}: {len(json.dumps(v)) / 1e6:.1f} MB" + (f" ({len(v)} items)" if isinstance(v, list) else ""))
