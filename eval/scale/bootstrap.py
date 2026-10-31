#!/usr/bin/env python3
"""First dream of a made-up big world, timed. Its review history is taken as done (a memory that grew
note by note would have reviewed each entity once, as it arrived), so the all-pairs check is skipped here.

  bootstrap.py <memory root>
"""
import importlib.util
import os
import sys
import time
from pathlib import Path

spec = importlib.util.spec_from_file_location("m", Path(__file__).resolve().parents[2] / "skills/memory-dream/scripts/memory.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
os.environ.pop("MEMORY_LLM", None)
m.candidates = lambda *a, **k: set()
t = time.time()
m.main(["dream", "--root", sys.argv[1]])
print(f"bootstrap dream: {time.time() - t:.0f}s")
