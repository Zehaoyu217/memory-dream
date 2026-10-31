#!/usr/bin/env python3
"""Taste agent eval summary: share of applicable notes each arm's plans followed (person preferences and house rules
separately), notes contradicted, and cost/time from usage-*.jsonl and harness.json.

  summarize.py
"""
import json
from collections import defaultdict
from pathlib import Path

D = Path(__file__).resolve().parent
batches = {b.stem: [json.loads(x) for x in b.read_text().splitlines() if x.strip()] for b in (D / "batches").glob("*.jsonl")}
judged = {}
for f in D.glob("judge-*.json"):
    for path, r in json.loads(f.read_text()).items():
        judged[Path(path).stem] = r["verdicts"]
usage = {}
for f in D.glob("usage-*.jsonl"):
    for ln in f.read_text().splitlines():
        r = json.loads(ln)
        usage[r["run"]] = r
harness = json.loads((D / "harness.json").read_text()) if (D / "harness.json").exists() else {}
cells = defaultdict(lambda: defaultdict(float))
for run, v in sorted(judged.items()):
    arm, b = run.split("-")[1], run.split("-")[2]
    c = cells[arm]
    for i, t in enumerate(batches[b], 1):
        fol, con = set(v.get(f"T{i}", {}).get("followed", [])), set(v.get(f"T{i}", {}).get("contradicted", []))
        for n in t["notes"]:
            k = "prefs" if n.startswith("prefs/") else "rules"
            c[f"{k}_gold"] += 1
            c[f"{k}_followed"] += n in fol
            c["contradicted"] += n in con
    u = usage.get(run)
    if u:
        c["runs"] += 1
        c["tool_calls"] += u["tool_calls"]
        c["cost_units"] += u["input"] + 0.1 * u["cache_read"] + 1.25 * u["cache_write"] + 5 * u["output"]
    if run in harness:
        c["secs"] += harness[run]["ms"] / 1000
for arm, c in sorted(cells.items()):
    n = c["runs"] or 1
    print(f"{arm}: person preferences followed {int(c['prefs_followed'])}/{int(c['prefs_gold'])} = "
          f"{c['prefs_followed'] / max(1, c['prefs_gold']):.2f} · house rules {int(c['rules_followed'])}/{int(c['rules_gold'])} = "
          f"{c['rules_followed'] / max(1, c['rules_gold']):.2f} · contradicted {int(c['contradicted'])} · per batch: "
          f"{c['tool_calls'] / n:.1f} tool calls, {c['cost_units'] / n / 1000:.0f}k cost units, {c['secs'] / n:.0f} s")
