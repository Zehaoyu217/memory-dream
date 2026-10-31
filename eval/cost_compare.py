#!/usr/bin/env python3
"""Compare indexing runs: cost per note, tokens, time, and what the extraction kept (entities, relations, held back).

  cost_compare.py <world dir> [<world dir> ...]     (each holds cost.jsonl and memory/)
"""
import json
import statistics as st
import sys
from collections import Counter
from pathlib import Path

for w in map(Path, sys.argv[1:]):
    rows = [json.loads(x) for x in (w / "cost.jsonl").read_text().splitlines()]
    ex = [r for r in rows if r["kind"] == "extract"]
    g = json.loads((w / "memory/_dream/graph.json").read_text())
    raw = Counter()
    for f in (w / "memory/_dream/notes").glob("*.json"):
        for r in json.loads(f.read_text()).get("relations", []):
            raw[r["type"]] += 1
    print(json.dumps({
        "world": w.name, "calls": len(rows), "usd_total": round(sum(r["cost"] or 0 for r in rows), 4),
        "usd_per_note": round(sum(r["cost"] or 0 for r in ex) / len(ex), 5),
        "median_in": st.median(r["in"] for r in ex), "median_out": st.median(r["out"] for r in ex),
        "median_s": round(st.median(r["ms"] for r in ex) / 1000, 1),
        "entities": len(g["entities"]), "with_home": sum(1 for e in g["entities"] if e.get("home")),
        "relations_kept": len(g["relations"]), "relations_extracted": sum(raw.values()),
        "types_written": len(raw), "kept_types": Counter(r["type"] for r in g["relations"]).most_common(8),
        "held_back": [c["msg"] for c in g["checks"] if c["code"] == "C7"][:4],
        "c4": sum(1 for c in g["checks"] if c["code"] == "C4")}))
