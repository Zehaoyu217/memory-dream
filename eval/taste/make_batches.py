#!/usr/bin/env python3
"""Two agent batches from the held-out taste tasks: T1 = 10 tasks naming the person, T2 = 10 naming only the meeting
or audience, one per person where possible (seeded). Prints the task lists for the agent prompts.

  make_batches.py
"""
import json
import random
from pathlib import Path

D = Path(__file__).resolve().parent
rows = [json.loads(x) for x in (D / "tasks-holdout.jsonl").read_text().splitlines() if x.strip()]
random.seed(7)
(D / "batches").mkdir(exist_ok=True)
for name, typ in (("T1", "taste-named"), ("T2", "taste-implicit")):
    pool = [r for r in rows if r["type"] == typ]
    pick, seen = [], set()
    for r in random.sample(pool, k=len(pool)):
        if r["bundle"] not in seen:
            pick.append(r)
            seen.add(r["bundle"])
        if len(pick) == 10:
            break
    (D / "batches" / f"{name}.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in pick))
    print(f"== {name} ({typ})")
    for i, r in enumerate(pick, 1):
        print(f"T{i} {r['q']}")
