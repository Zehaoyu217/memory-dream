#!/usr/bin/env python3
"""Question batches for the agent eval (seeded): C-orig, C-h1, C-h2 (churn-2026), P1 (projects), P2 (general)."""
import json
import random
from collections import defaultdict
from pathlib import Path

Q = Path(__file__).resolve().parent.parent / "questions"
OUT = Path(__file__).resolve().parent / "batches"
OUT.mkdir(exist_ok=True)
rnd = random.Random(20261030)


def load(name):
    return [json.loads(x) for x in (Q / name).read_text().splitlines() if x.strip()]


def interleave(items):
    by = defaultdict(list)
    for it in items:
        by[it.get("type")].append(it)
    out = []
    while any(by.values()):
        for t in sorted(by):
            if by[t]:
                out.append(by[t].pop(0))
    return out


def save(name, items):
    (OUT / f"{name}.jsonl").write_text("".join(json.dumps(i, ensure_ascii=False) + "\n" for i in items))
    print(f"== {name}", len(items), sorted({i.get("type") for i in items}))
    for k, i in enumerate(items, 1):
        print(f"Q{k} {i['q']}")


save("C-orig", load("churn-orig.jsonl"))
ch = interleave(load("churn-haiku.jsonl"))
save("C-h1", ch[:10])
save("C-h2", ch[10:20])
projects = sorted(p for p in Q.glob("bank-*.jsonl") if not p.name.startswith("bank-general-"))
pool = [q for p in projects for q in load(p.name)]
types = ["lookup", "lineage", "dependency", "current", "numeric", "why"]
picked, used = [], set()
for k in range(10):
    t = types[k % len(types)]
    cands = [q for q in pool if q.get("type") == t and q["bundle"] not in used]
    q = rnd.choice(cands)
    picked.append(q)
    used.add(q["bundle"])
save("P1", picked)
gen = [q for p in sorted(Q.glob("bank-general-*.jsonl")) for q in load(p.name)]
want = {"preference": 2, "reporting": 2, "term": 1, "correction": 3, "howto": 1, "qa": 1}
p2 = []
for t, n in want.items():
    cands = [q for q in gen if q.get("type") == t]
    p2 += rnd.sample(cands, min(n, len(cands)))
save("P2", p2)
