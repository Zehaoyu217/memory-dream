#!/usr/bin/env python3
"""A25 taste agent eval: pull the four runs' reports and usage from their transcripts, record wall time, judge them.

  collect.py <subagents dir> <memory root>
"""
import datetime as dt
import json
import subprocess
import sys
from pathlib import Path

D = Path(__file__).resolve().parent
S, root = Path(sys.argv[1]), sys.argv[2]
RUNS = {"T-mem-T1": "a8a59ca249783247a", "T-grep-T1": "a1290c962669f57c2",
        "T-mem-T2": "a93b9d3c4af488834", "T-grep-T2": "a9d94a296b9262d7d",
        # plain tasks ("write a short spec"), nothing said about notes or preferences
        "P-mem-T1": "a173498adf5639653", "P-grep-T1": "ade328da84d966dce", "P-none-T1": "a313f318afbe7cb21"}
args = [f"{k}={S / f'agent-{v}.jsonl'}" for k, v in RUNS.items()]
usage = subprocess.run(["python3", str(D.parent / "a21/extract.py"), str(D / "runs"), *args], capture_output=True, text=True).stdout
(D / "usage-T.jsonl").write_text(usage)
harness = {}
for k, v in RUNS.items():
    ts = [json.loads(ln).get("timestamp") for ln in open(S / f"agent-{v}.jsonl")]
    ts = [dt.datetime.fromisoformat(t.replace("Z", "+00:00")) for t in ts if t]
    harness[k] = {"ms": int((max(ts) - min(ts)).total_seconds() * 1000)}
(D / "harness.json").write_text(json.dumps(harness, indent=1))
for k in RUNS:
    b = k.split("-")[2]
    out = subprocess.run(["python3", str(D / "judge.py"), root, str(D / "batches" / f"{b}.jsonl"), str(D / "runs" / f"{k}.md")],
                         capture_output=True, text=True)
    (D / f"judge-{k}.json").write_text(out.stdout or out.stderr)
print(usage)
