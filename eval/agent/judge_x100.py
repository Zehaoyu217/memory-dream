#!/usr/bin/env python3
"""A24 (100x world): merge run timings into harness.json, grade the six runs with the Haiku judge, print verdicts."""
import json
import subprocess
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

D = Path(__file__).resolve().parent
h = json.loads((D / "harness.json").read_text())
h.update({
    "X-mem-P1": {"tokens": 62104, "tool_uses": 5, "ms": 59845},
    "X-mem-C-orig": {"tokens": 63466, "tool_uses": 4, "ms": 77418},
    "X-mem-P2": {"tokens": 57384, "tool_uses": 6, "ms": 91286},
    "X-grep-C-orig": {"tokens": 64829, "tool_uses": 14, "ms": 121732},
    "X-grep-P2": {"tokens": 72611, "tool_uses": 28, "ms": 201098},
    "X-grep-P1": {"tokens": 85903, "tool_uses": 37, "ms": 218485},
})
if "X-*" not in h["_note"]:
    h["_note"] += "; X-* = 100x world (168,141 notes)"
(D / "harness.json").write_text(json.dumps(h, indent=1))
(D / "harness-x100.json").unlink(missing_ok=True)


def judge(job):
    b, a = job
    out = subprocess.run(["python3", str(D.parent / "judge.py"), str(D / "batches" / f"{b}.jsonl"), str(D / "runs" / f"X-{a}-{b}.md")],
                         capture_output=True, text=True, cwd=D.parents[1]).stdout
    (D / f"judge-X-{a}-{b}.json").write_text(out)
    return job, out


with ThreadPoolExecutor(6) as ex:
    for (b, a), out in ex.map(judge, [(b, a) for b in ("P1", "P2", "C-orig") for a in ("mem", "grep")]):
        for path, r in json.loads(out).items():
            c = Counter(v["v"] for v in r["verdicts"].values())
            print(f"X-{a}-{b}".ljust(16), dict(c), [(q, v["v"], v["why"][:80]) for q, v in r["verdicts"].items() if v["v"] != "correct"])
