#!/usr/bin/env python3
"""Score `ask` on taste tasks: did the person's preference notes (prefs/) and the house rules (reporting/, howto/)
named as gold come back for the task? Batches of 10, one ask call each, like an agent.

  score.py <memory root> <tasks.jsonl> [--show] [--misses]
"""
import importlib.util
import json
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("retrieval", HERE.parent / "retrieval.py")
ret = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ret)
root, tasks = Path(sys.argv[1]).resolve(), [json.loads(x) for x in Path(sys.argv[2]).read_text().splitlines() if x.strip()]
got = defaultdict(lambda: [0, 0])  # (variant, kind) → [hit, gold]
chars, misses = 0, []
for i in range(0, len(tasks), 10):
    batch = tasks[i:i + 10]
    out = ret.run_ask(root, [t["q"] for t in batch])
    chars += len(out)
    if "--show" in sys.argv:
        print(out)
    for t, (_, sec) in zip(batch, ret.sections(out)):
        heads = {ln.split(" · ")[0][2:].split(" (")[0].strip() for ln in sec.split("\n") if ln.startswith("▸ ")}
        for n in t["notes"]:
            kind = "prefs" if n.startswith("prefs/") else "rules"
            hit = n in heads
            for v in (t["type"], "all"):
                got[(v, kind)][0] += hit
                got[(v, kind)][1] += 1
            if not hit and kind == "prefs":
                misses.append((t["q"][:100], n))
res = {f"{v} {k}": f"{h}/{n} = {h / n:.2f}" for (v, k), (h, n) in sorted(got.items())}
res["chars per task"] = round(chars / len(tasks))
print(json.dumps(res, indent=1))
if "--misses" in sys.argv:
    for q, n in misses:
        print(f"  miss {n} | {q}")
