#!/usr/bin/env python3
"""Per-condition averages for A21 from usage.jsonl (transcript tallies) + harness.json + grades.json.

Cost units weight tokens by Opus price ratios: fresh input 1, cache read 0.1, cache write 1.25, output 5.
"""
import json
from pathlib import Path

D = Path(__file__).parent
rows = [json.loads(x) for x in (D / "usage.jsonl").read_text().splitlines()]
harness = json.loads((D / "harness.json").read_text())
grades = json.loads((D / "grades.json").read_text())


def units(r):
    return r["input"] + 0.1 * r["cache_read"] + 1.25 * r["cache_write"] + 5 * r["output"]


out = {}
for cond in ("mem", "grep"):
    rs = [r for r in rows if r["run"].startswith(cond)]
    n = len(rs)
    g = [v for f, qs in grades.items() if Path(f).stem.startswith(cond) for v in qs.values()]
    out[cond] = {
        "runs": n,
        "correct": f"{sum(x['grade'] == 'correct' for x in g)}/{len(g)}",
        "tool_calls_per_run": round(sum(r["tool_calls"] for r in rs) / n, 1),
        "api_requests_per_run": round(sum(r["requests"] for r in rs) / n, 1),
        "processed_tokens_per_run": round(sum(r["total"] for r in rs) / n),
        "output_tokens_per_run": round(sum(r["output"] for r in rs) / n),
        "harness_tokens_per_run": round(sum(harness[r["run"]]["tokens"] for r in rs) / n),
        "secs_per_run": round(sum(harness[r["run"]]["ms"] for r in rs) / n / 1000),
        "cost_units_per_run": round(sum(units(r) for r in rs) / n),
    }
    out[cond]["per_question"] = {k: round(out[cond][k + "_per_run"] / 10, 1)
                                 for k in ("tool_calls", "processed_tokens", "harness_tokens", "cost_units")}
out["ratio_mem_over_grep"] = {k: round(out["mem"][k] / out["grep"][k], 2)
                              for k in ("tool_calls_per_run", "processed_tokens_per_run", "harness_tokens_per_run",
                                        "cost_units_per_run", "secs_per_run")}
(D / "summary.json").write_text(json.dumps(out, indent=1))
print(json.dumps(out, indent=1))
