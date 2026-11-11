#!/usr/bin/env python3
"""Five arms on the same thirty questions: Opus and Haiku, with the memory and with grep only. No model: it reads
what is in this folder.

  python3 eval/agent/arms.py

The Opus arms are the runs of phase G (2026-11-01). The Haiku arms were run on 2026-11-11 with the same prompts on
the bank-index world: eval/agent/make_haiku_arm.py builds the workspaces and prompts; each prompt went to one
Haiku 5.5 subagent, told to read it from its file (one extra tool call a run, taken out below); `full` used
eval/agent/askfull.py, an experiment that prints the first six notes of each question whole. Every answer was graded
twice that day by the judge of eval/judge.py (judge-H.json), the Opus answers included, so all arms share one judge.
Dollars use each model's own prices; every Haiku request stayed under 100K tokens, the largest was 88,671.
Quoted in PLAN.md (rev 3) and RESULTS.md phase K.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
BATCHES = ("P1", "C-h1", "P2")
RATE = {  # $ per million tokens: fresh input, cache read, cache write (5 minutes), output
    "Opus 5.5": (4.00, 0.20, 5.00, 20.00),
    "Haiku 5.5": (0.10, 0.01, 0.125, 0.50),  # the prices for a prompt of 100K tokens or fewer; five times these above
}
ARMS = (("G-grep", "Opus 5.5", "Opus + grep"), ("G-mem", "Opus 5.5", "Opus + memory"), ("H-grep", "Haiku 5.5", "Haiku + grep"),
        ("H-mem", "Haiku 5.5", "Haiku + memory"), ("H-full", "Haiku 5.5", "Haiku + memory, notes whole"))


def main():
    usage = {}
    for f in ("usage-G.jsonl", "usage-H.jsonl"):
        for ln in (HERE / f).read_text().splitlines():
            if ln.strip():
                u = json.loads(ln)
                usage[u["run"]] = u
    harness = json.loads((HERE / "harness.json").read_text())
    judge = json.loads((HERE / "judge-H.json").read_text())
    print("arm · correct/partial/wrong of 30, first and second pass of the judge · tool calls · requests · tokens · $ · seconds (each a batch of ten)")
    rows = {}
    for arm, model, label in ARMS:
        runs = [f"{arm}-{b}" for b in BATCHES]
        both = []
        for p in ("pass1", "pass2"):
            if all(r in judge[p] for r in runs):
                both.append("/".join(str(sum(judge[p][r][k] for r in runs)) for k in ("correct", "partial", "wrong")))
        fi, cr, cw, out = RATE[model]
        cost = sum(usage[r]["input"] * fi + usage[r]["cache_read"] * cr + usage[r]["cache_write"] * cw + usage[r]["output"] * out for r in runs) / 1e6 / 3
        tools = sum(usage[r]["tool_calls"] - (1 if arm.startswith("H-") else 0) for r in runs) / 3
        sec = sum(harness[r]["ms"] for r in runs) / 3000
        rows[label] = (cost, sec, both)
        print(f"{label:<28} · {' and '.join(both):<19} · {tools:4.1f} · {sum(usage[r]['requests'] for r in runs) / 3:4.1f} · "
              f"{sum(usage[r]['total'] for r in runs) / 3000:6,.0f}k · ${cost:.4f} · {sec:3.0f}")
    base = rows["Opus + grep"]
    for label, (cost, sec, _) in rows.items():
        if label != "Opus + grep":
            r = base[0] / cost
            print(f"{label} against Opus + grep: {r:.0f} times cheaper, {base[1] / sec:.1f} times faster" if r >= 10 else
                  f"{label} against Opus + grep: {1 / r:.2f} of the cost, {base[1] / sec:.1f} times faster")
    flips = sum(judge["pass1"][r]["verdicts"][q]["v"] != judge["pass2"][r]["verdicts"].get(q, {}).get("v")
                for r in judge["pass1"] for q in judge["pass1"][r]["verdicts"])
    total = sum(len(judge["pass1"][r]["verdicts"]) for r in judge["pass1"])
    print(f"the judge against itself: {flips} of {total} verdicts differ between its two passes")
    was = {}
    for arm in ("G-mem", "G-grep"):
        t = [0, 0, 0]
        for b in BATCHES:
            d = json.loads((HERE / f"judge-{arm}-{b}.json").read_text())
            d = d if "correct" in d else list(d.values())[0]
            t = [t[0] + d["correct"], t[1] + d["partial"], t[2] + d["wrong"]]
        was[arm] = "/".join(map(str, t))
    print(f"the same Opus answers as graded on 2026-11-01: memory {was['G-mem']}, grep {was['G-grep']}")


if __name__ == "__main__":
    main()
