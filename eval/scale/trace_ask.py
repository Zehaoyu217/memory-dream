#!/usr/bin/env python3
"""Where one `ask` call spends its time on a big memory: load, routing per question, each grep.

  trace_ask.py <memory root> <batch name: P1|P2|C-orig>
"""
import contextlib
import importlib.util
import io
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("m", HERE.parent / "skills/memory-dream/scripts/memory.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
log = []
for name in ("load", "grep_lines", "route", "catalog", "rank"):
    f = getattr(m, name)

    def wrap(*a, _f=f, _n=name, **k):
        t = time.time()
        r = _f(*a, **k)
        extra = ""
        if _n == "grep_lines":
            extra = f" {len(a[1])} pats over {'EVERYTHING' if len(a) < 3 or a[2] is None else len(a[2])} areas → {sum(map(len, r.values()))} lines"
        if _n == "route":
            extra = f" → {r[0]} {r[1]}"
        log.append((_n, time.time() - t, extra))
        return r
    setattr(m, name, wrap)
qs = [json.loads(x)["q"] for x in open(HERE / "agent/batches" / f"{sys.argv[2]}.jsonl")]
t = time.time()
with contextlib.redirect_stdout(io.StringIO()):
    m.main(["ask", "--root", sys.argv[1], *qs])
total = time.time() - t
agg = {}
for n, s, e in log:
    agg[n] = agg.get(n, 0) + s
    if n in ("grep_lines", "route") and (s > 0.3 or "EVERYTHING" in e or "None" in e):
        print(f"  {n} {s:.1f}s{e}")
print(f"total {total:.1f}s · " + " · ".join(f"{k} {v:.1f}s" for k, v in agg.items()) + f" · other {total - sum(agg.values()):.1f}s")
