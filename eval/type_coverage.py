#!/usr/bin/env python3
"""How much of what the dreamer extracted fits the relation vocabulary? Instance-level, from the cache.

  type_coverage.py <memory root> [EDGES.md to judge with; default the root's]
Every extracted relation instance of a current note is: a listed type, an alias of one, on the drop
list, or unknown. Prints shares and the unknown tail with an example quote each.
"""
import importlib.util
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

MEM = Path(__file__).resolve().parent.parent / "skills/memory-dream/scripts/memory.py"
spec = importlib.util.spec_from_file_location("memory", MEM)
mem = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mem)

root = Path(sys.argv[1])
edges = Path(sys.argv[2]).read_text() if len(sys.argv) > 2 else (root / "EDGES.md").read_text()
types, alias, drop, _, _ = mem.parse_edges(edges)
man = json.loads((root / "_dream/manifest.json").read_text())
cls, unknown, ex, per_type = Counter(), Counter(), {}, defaultdict(Counter)
for rel, f in man["files"].items():
    p = root / "_dream/notes" / f"{f['sha'][:12]}.json"
    if not p.exists():
        continue
    for r in json.loads(p.read_text()).get("relations", []):
        t = mem.fold(r["type"]).lstrip("~")
        if t in types:
            c = "listed type"
        elif t in alias:
            c = "alias of a listed type"
        elif t in drop:
            c = "drop list"
        else:
            c = "unknown"
            unknown[t] += 1
            ex.setdefault(t, f"{r['s']} —{t}→ {r['o']}: {r['quote'][:70]}")
        cls[c] += 1
        if c in ("listed type", "alias of a listed type"):
            per_type[alias[t][0]][t] += 1
n = sum(cls.values())
print(json.dumps({"relation_instances": n, "share": {k: round(v / n, 3) for k, v in cls.most_common()},
                  "per_listed_type": {k: sum(v.values()) for k, v in sorted(per_type.items(), key=lambda z: -sum(z[1].values()))},
                  "unknown_types": len(unknown)}, indent=1))
print("top unknown:")
for t, k in unknown.most_common(25):
    print(f"  {k:4}  {ex[t]}")
