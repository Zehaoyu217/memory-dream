#!/usr/bin/env python3
"""Copy subagent runs into this folder: the answers (machine paths taken out), the usage, the harness's own numbers,
and for runs on the thirty questions two passes of the judge. No model but the judge.

  python3 eval/agent/persist.py <arm dir> <transcripts dir> <run>=<transcript id>,<tokens>,<tool uses>,<ms> …

<arm dir> is where make_haiku_arm.py and make_linkage_arm.py wrote the workspaces and prompts. A run is one subagent
on one batch, told to read its prompt from a file and named <arm>-<batch>: `H-…` for the thirty questions (batches
P1, C-h1, P2; graded by eval/judge.py), anything else for the linkage sets (batches L1 to L3 and G1; scored exactly
by arms.py). The transcript is the subagent's JSONL as the harness wrote it, `<transcript id>.output`; tokens, tool
uses and ms are the three numbers the harness reports when the subagent ends.

A run already graded is not graded again: take its name out of judge-H.json to grade new answers. A request whose
prompt is over 100K tokens is recorded apart (`over_100k`), since Haiku 5.5 bills it at five times the price and
arms.py prices it so. Every run of RESULTS phase L was filed with this.
"""
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent


def over_line(rows):
    """The requests whose prompt (fresh, cached and cache-written input) is over 100K tokens, summed."""
    over, seen = {"requests": 0, "input": 0, "cache_read": 0, "cache_write": 0, "output": 0}, set()
    for r in rows:
        m = r.get("message")
        if not isinstance(m, dict) or m.get("role") != "assistant" or not m.get("usage") or m.get("id") in seen:
            continue
        seen.add(m.get("id"))
        x = m["usage"]
        if x.get("input_tokens", 0) + x.get("cache_read_input_tokens", 0) + x.get("cache_creation_input_tokens", 0) > 100_000:
            over["requests"] += 1
            over["input"] += x.get("input_tokens", 0)
            over["cache_read"] += x.get("cache_read_input_tokens", 0)
            over["cache_write"] += x.get("cache_creation_input_tokens", 0)
            over["output"] += x.get("output_tokens", 0)
    return over


def main(arm, tasks, args):
    spec = importlib.util.spec_from_file_location("extract", REPO / "eval/a21/extract.py")
    ex = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ex)
    runs = {}
    for a in args:
        name, rest = a.split("=")
        tid, tok, tools, ms = rest.split(",")
        runs[name] = (tid, int(tok), int(tools), int(ms))
    harness = json.loads((HERE / "harness.json").read_text())
    usage = {"H": {}, "L": {}}
    for name, (tid, tok, tools, ms) in runs.items():
        rows = [json.loads(ln) for ln in open(tasks / f"{tid}.output") if ln.strip()]
        models = {r["message"].get("model") for r in rows if isinstance(r.get("message"), dict) and r["message"].get("usage")}
        assert len(models) == 1, (name, models)  # one model a run, or the prices are wrong
        text = re.sub(re.escape(str(arm)) + r"/[^/\s,]+/", "", ex.report_text(rows))  # the workspace's path is not an answer
        (HERE / "runs" / f"{name}.md").write_text(text)
        over = over_line(rows)
        usage["H" if name.startswith("H-") else "L"][name] = {"run": name, **ex.usage(rows), **({"over_100k": over} if over["requests"] else {})}
        harness[name] = {"tokens": tok, "tool_uses": tools, "ms": ms}
    for k, f in (("H", "usage-H.jsonl"), ("L", "usage-L.jsonl")):
        old = [json.loads(ln) for ln in (HERE / f).read_text().splitlines() if ln.strip()] if (HERE / f).exists() else []
        rows = [usage[k].pop(u["run"], u) for u in old] + list(usage[k].values())  # a run filed again takes its old place
        (HERE / f).write_text("\n".join(json.dumps(u) for u in rows) + "\n")
    (HERE / "harness.json").write_text(json.dumps(harness, indent=1) + "\n")
    judge = json.loads((HERE / "judge-H.json").read_text())
    for p in ("pass1", "pass2"):
        for n in (n for n in runs if n.startswith("H-") and n not in judge[p]):
            b = n.split("-", 2)[2]
            out = subprocess.run([sys.executable, str(REPO / "eval/judge.py"), str(HERE / "batches" / f"{b}.jsonl"), str(HERE / "runs" / f"{n}.md")],
                                 capture_output=True, text=True).stdout
            judge[p][n] = list(json.loads(out).values())[0]
            print(p, n, judge[p][n]["correct"], judge[p][n]["partial"], judge[p][n]["wrong"])
    (HERE / "judge-H.json").write_text(json.dumps(judge, indent=1, ensure_ascii=False) + "\n")
    left = [f.name for f in (HERE / "runs").glob("*.md") if re.search(r"/(Users|home)/", f.read_text())]
    print("runs filed:", len(runs), "| run files that name a machine path:", left)
    return 1 if left else 0


if __name__ == "__main__":
    if len(sys.argv) < 4:
        raise SystemExit(__doc__)
    sys.exit(main(Path(sys.argv[1]).resolve(), Path(sys.argv[2]), sys.argv[3:]))
