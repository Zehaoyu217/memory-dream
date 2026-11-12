#!/usr/bin/env python3
"""Every arm of the agent eval side by side: Opus and Haiku, with the memory and with grep only. No model: it reads
what is in this folder.

  python3 eval/agent/arms.py

Three question sets.
  thirty   batches P1, C-h1, P2 of phase G: one answer in a few sentences, graded by the judge of eval/judge.py. Every
           answer here was graded twice on 2026-11-11 (judge-H.json), the Opus answers of phase G included.
  linkage  batches L1, L2, L3 (eval/questions/linkage-bank.jsonl): the answer is a set of notes inside one project,
           reached through several links; scored exactly by eval/linkage.py.
  whole    batch G1 (eval/questions/linkage-global.jsonl): the answer is a set of notes across many projects.

The Opus arms on the thirty are the runs of phase G. Everything else was run on 2026-11-11 on the bank-index world,
one subagent a batch, each told to read its prompt from a file (one tool call a run, taken out below).
make_haiku_arm.py and make_linkage_arm.py write the workspaces and prompts, persist.py files what the subagents
answered and what they used. Dollars use each model's own prices. A
Haiku 5.5 request whose prompt is over 100K tokens costs five times as much: one run had two (Haiku with grep on the
whole-memory questions), they are priced so, and the line says it. Quoted in RESULTS.md phases K and L.

The memory of phase L was run three times, each on the script as it stood, every question set again each time:
  r1  a small folder printed whole when a call points at it, the whole chain of a named note, the map (`ask --list`)
  r2  and a note's kind taken from its name and folder before the dreamer's reading
  r3  and a section that says when it holds the best matches of a folder and not all of it; the chain line names the
      notes one step away apart from those reached through them (the script as committed)
One run a batch is all any row has: on the thirty the three rounds are as much a measure of run-to-run spread as of
the changes between them.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
RATE = {  # $ per million tokens: fresh input, cache read, cache write (5 minutes), output
    "Opus 5.5": (4.00, 0.20, 5.00, 20.00),
    "Haiku 5.5": (0.10, 0.01, 0.125, 0.50),  # the prices for a prompt of 100K tokens or fewer; five times these above
}
B3 = ("P1", "C-h1", "P2")
THIRTY = (  # label, model, runs
    ("Opus + grep", "Opus 5.5", [f"G-grep-{b}" for b in B3]),
    ("Opus + memory, v0.4", "Opus 5.5", [f"G-mem-{b}" for b in B3]),
    ("Haiku + grep", "Haiku 5.5", [f"H-grep-{b}" for b in B3]),
    ("Haiku + memory, v0.4", "Haiku 5.5", [f"H-mem-{b}" for b in B3]),
    ("  … its notes printed whole", "Haiku 5.5", [f"H-full-{b}" for b in B3]),
    ("  … told not to stop", "Haiku 5.5", [f"H-persist-{b}" for b in B3]),
    ("  … its folder printed whole", "Haiku 5.5", ["H-mem-P1", "H-area-C-h1", "H-mem-P2"]),
    *((f"Haiku + memory, phase L r{i}", "Haiku 5.5", [f"H-r{i}-{b}" for b in B3]) for i in (1, 2, 3)),
)
LINKAGE = (
    ("Opus + grep", "Opus 5.5", [f"LO-grep-L{i}" for i in (1, 2, 3)]),
    ("Haiku + grep", "Haiku 5.5", [f"LH-grep-L{i}" for i in (1, 2, 3)]),
    ("Haiku + memory, v0.4", "Haiku 5.5", [f"LH-mem-L{i}" for i in (1, 2, 3)]),
    *((f"Haiku + memory, phase L r{j}", "Haiku 5.5", [f"LH-r{j}-L{i}" for i in (1, 2, 3)]) for j in (1, 2, 3)),
)
WHOLE = (
    ("Opus + grep", "Opus 5.5", ["GO-grep-G1"]),
    ("Haiku + grep", "Haiku 5.5", ["GH-grep-G1"]),
    *((f"Haiku + memory, phase L r{j}", "Haiku 5.5", [f"GH-r{j}-G1"]) for j in (1, 2, 3)),
)


def load():
    usage = {}
    for f in sorted(HERE.glob("usage-*.jsonl")):
        for ln in f.read_text().splitlines():
            if ln.strip():
                u = json.loads(ln)
                usage[u["run"]] = u
    return usage, json.loads((HERE / "harness.json").read_text()), json.loads((HERE / "judge-H.json").read_text())


def spend(usage, harness, model, runs):
    """→ (tool calls, requests, thousands of tokens, dollars, seconds, requests over 100K tokens), each per run but the last."""
    fi, cr, cw, out = RATE[model]
    n = len(runs)
    price = lambda u: u["input"] * fi + u["cache_read"] * cr + u["cache_write"] * cw + u["output"] * out  # noqa: E731
    # a Haiku 5.5 request whose prompt is over 100K tokens is billed at five times the price: four more times its tokens
    late = [usage[r]["over_100k"] for r in runs if model == "Haiku 5.5" and "over_100k" in usage[r]]
    return (sum(usage[r]["tool_calls"] - (0 if r.startswith("G-") else 1) for r in runs) / n,
            sum(usage[r]["requests"] for r in runs) / n, sum(usage[r]["total"] for r in runs) / n / 1000,
            (sum(price(usage[r]) for r in runs) + 4 * sum(price(o) for o in late)) / 1e6 / n,
            sum(harness[r]["ms"] for r in runs) / n / 1000, sum(o["requests"] for o in late))


def main():
    usage, harness, judge = load()
    import importlib.util
    spec = importlib.util.spec_from_file_location("linkage", HERE.parent / "linkage.py")
    linkage = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(linkage)

    print("THIRTY QUESTIONS · correct/partial/wrong of 30, two passes of the judge · per batch of ten: tool calls · requests · tokens · $ · seconds")
    base = None
    for label, model, runs in THIRTY:
        both = ["/".join(str(sum(judge[p][r][k] for r in runs)) for k in ("correct", "partial", "wrong")) for p in ("pass1", "pass2")
                if all(r in judge[p] for r in runs)]
        t, q, k, d, s, late = spend(usage, harness, model, runs)
        base = base or (d, s)
        print(f"{label:<30} · {' and '.join(both):<19} · {t:4.1f} · {q:4.1f} · {k:6,.0f}k · ${d:.4f} · {s:3.0f}"
              + (f"   ({base[0] / d:.0f}x cheaper, {base[1] / s:.1f}x faster than Opus + grep)" if base[0] / d >= 10 else "")
              + (f" · {late} requests over 100K tokens, at five times the price" if late else ""))
    flips = sum(judge["pass1"][r]["verdicts"][q]["v"] != judge["pass2"][r]["verdicts"].get(q, {}).get("v")
                for r in judge["pass1"] for q in judge["pass1"][r]["verdicts"])
    print(f"the judge against itself: {flips} of {sum(len(judge['pass1'][r]['verdicts']) for r in judge['pass1'])} verdicts differ between its two passes")

    for title, arms, per in (("LINKAGE INSIDE A PROJECT · of 30", LINKAGE, "batch of ten"), ("ACROSS THE WHOLE MEMORY · of 7", WHOLE, "batch of seven")):
        print(f"\n{title}: answered exactly · whole set named · recall · precision · per {per}: tool calls · requests · tokens · $ · seconds")
        base = None
        for label, model, runs in arms:
            if not all((HERE / "runs" / f"{r}.md").exists() and r in usage for r in runs):
                continue
            ex = full = n = 0
            rec, pre = [], []
            for r in runs:
                qs = [json.loads(x) for x in (HERE / "batches" / f"{r.rsplit('-', 1)[1]}.jsonl").read_text().splitlines() if x.strip()]
                e, f, rc, pr, _ = linkage.tally(qs, (HERE / "runs" / f"{r}.md").read_text())
                ex, full, n = ex + e, full + f, n + len(qs)
                rec.append(rc)
                pre.append(pr)
            t, q, k, d, s, late = spend(usage, harness, model, runs)
            base = base or (d, s)
            print(f"{label:<26} · {ex:2d} · {full:2d} · {sum(rec) / len(rec):.2f} · {sum(pre) / len(pre):.2f} · {t:4.1f} · {q:4.1f} · {k:6,.0f}k · ${d:.4f} · {s:3.0f}"
                  + (f"   ({base[0] / d:.0f}x cheaper, {base[1] / s:.1f}x faster than Opus + grep)" if base[0] / d >= 10 else "")
                  + (f" · {late} requests over 100K tokens, at five times the price" if late else ""))


if __name__ == "__main__":
    main()
