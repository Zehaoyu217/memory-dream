#!/usr/bin/env python3
"""A22 summary per cell (S/B × mem/grep): accuracy from judge-*.json, cost from usage-*.jsonl, time from harness.json.

Cost units weight tokens by Opus price ratios: fresh input 1, cache read 0.1, cache write 1.25, output 5.
"""
import json
from collections import defaultdict
from pathlib import Path

D = Path(__file__).resolve().parent
usage = {}
for f in D.glob("usage-*.jsonl"):
    for ln in f.read_text().splitlines():
        r = json.loads(ln)
        usage[r["run"]] = r
harness = {k: v for k, v in json.loads((D / "harness.json").read_text()).items() if not k.startswith("_")}
grades = {}
for f in D.glob("judge-*.json"):
    for path, r in json.loads(f.read_text()).items():
        grades[Path(path).stem] = r


def units(r):
    return r["input"] + 0.1 * r["cache_read"] + 1.25 * r["cache_write"] + 5 * r["output"]


cells = defaultdict(list)
for run in usage:
    cell = run.rsplit("-", 2)[0] if run.count("-") >= 3 else run
    cell = "-".join(run.split("-")[:2])
    cells[cell].append(run)
out = {}
for cell, runs in sorted(cells.items()):
    n = len(runs)
    g = [grades.get(r, {}) for r in runs]
    out[cell] = {
        "runs": n, "questions": 10 * n,
        "correct": sum(x.get("correct", 0) for x in g), "partial": sum(x.get("partial", 0) for x in g),
        "wrong": sum(x.get("wrong", 0) for x in g),
        "tool_calls": round(sum(usage[r]["tool_calls"] for r in runs) / n, 1),
        "requests": round(sum(usage[r]["requests"] for r in runs) / n, 1),
        "processed_tokens": round(sum(usage[r]["total"] for r in runs) / n),
        "cost_units": round(sum(units(usage[r]) for r in runs) / n),
        "secs": round(sum(harness[r]["ms"] for r in runs if r in harness) / max(1, sum(r in harness for r in runs)) / 1000),
    }
for size in ("S", "B", "Bn", "X"):
    m, gname = out.get(f"{size}-mem"), out.get(f"{'B' if size == 'Bn' else size}-grep")
    if m and gname:
        out[f"{size}-mem/grep"] = {k: round(m[k] / gname[k], 2) for k in ("tool_calls", "requests", "processed_tokens", "cost_units", "secs")}
(D / "summary.json").write_text(json.dumps(out, indent=1))
for k, v in out.items():
    print(k, json.dumps(v))
