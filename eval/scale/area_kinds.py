#!/usr/bin/env python3
"""Share of project-work kinds (question … model) per area: do kinds tell general areas from projects?

  area_kinds.py <memory root>
"""
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

PROJ = {"question", "experiment", "finding", "decision", "dataset", "feature", "model", "metric"}
g = json.load(open(Path(sys.argv[1]) / "_dream/graph.json"))
k = defaultdict(Counter)
for n in g["notes"]:
    k[n["project"]][n["kind"]] += 1
rows = sorted((sum(v for kk, v in c.items() if kk in PROJ) / sum(c.values()), a, sum(c.values()), dict(c.most_common(4)))
              for a, c in k.items())
for r in rows[:10] + [None] + rows[-3:]:
    print("..." if r is None else f"{r[0]:.2f} {r[1]:28} {r[2]:4} {r[3]}")
