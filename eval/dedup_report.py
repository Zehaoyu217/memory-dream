#!/usr/bin/env python3
"""What did dedup do on an indexed memory, and what did it cost? Samples of each merge rule for a manual check.

  dedup_report.py <memory root> [cost.jsonl ...]
"""
import importlib.util
import json
import random
import sys
from collections import defaultdict
from pathlib import Path

spec = importlib.util.spec_from_file_location("m", Path(__file__).resolve().parent.parent / "skills/memory-dream/scripts/memory.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
root = Path(sys.argv[1])
g = m.load(root)[0]
rnd = random.Random(7)
alines = m.parse_aliases((root / "ALIASES.md").read_text())[0]
alias_ids = {m.fold(i) for ids in alines for i in ids}
fold_merges, surface_merges = [], []
for e in g["entities"]:
    ids = [e["id"]] + e["aka"]
    folded = defaultdict(list)
    for i in ids:
        folded[m.fold(i)].append(i)
    fold_merges += [v for v in folded.values() if len(v) > 1]
    keys = {m.fold(i) for i in ids}
    if len(keys) > 1 and not (keys & alias_ids):
        surface_merges.append(ids)
print("dedup counts:", json.dumps(g.get("dedup", {})))
print(f"\nspelling-fold merges ({len(fold_merges)}), sample:")
for v in rnd.sample(fold_merges, min(8, len(fold_merges))):
    print("  ", " = ".join(v))
print(f"\nsurface-rule merges ({len(surface_merges)} entities), sample:")
for v in rnd.sample(surface_merges, min(15, len(surface_merges))):
    print("  ", " = ".join(v[:4]))
print(f"\nALIASES.md: {len(alines)} merge lines, "
      f"{sum(1 for ln in (root / 'ALIASES.md').read_text().split(chr(10)) if ln.startswith('not:'))} not: lines")
for f in sys.argv[2:]:
    rows = [json.loads(x) for x in Path(f).read_text().splitlines()]
    rv = [r for r in rows if r["kind"] == "review"]
    print(f"review calls in {Path(f).parent.name}: {len(rv)}, ${sum(r['cost'] for r in rv):.4f}")
ents = {e["id"]: e for e in g["entities"]}
sizes = [len(m.known_lines(ents, p)) for p in sorted({n["project"] for n in g["notes"]})]
print(f"\nKNOWN list per extraction prompt now: median {sorted(sizes)[len(sizes) // 2]} chars "
      f"(~{sorted(sizes)[len(sizes) // 2] // 4} tokens); before the cap (300 entities): "
      f"~{len(m.known_lines(ents, 'fraud-2026', local=300, shared=0)) // 4} tokens")
