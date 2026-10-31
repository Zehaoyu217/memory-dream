#!/usr/bin/env python3
"""Judge taste plans: for each task, which of the applicable notes (the person's preferences, the house rules) does the
agent's plan follow, and which does it contradict? Haiku, one call per run file.

  judge.py <memory root> <batch.jsonl> <run.md> [more run.md ...]   → JSON per run file
"""
import json
import re
import subprocess
import sys
from pathlib import Path

CMD = ["claude", "-p", "--model", "haiku", "--tools", "", "--setting-sources", "", "--strict-mcp-config",
       "--no-session-persistence", "--output-format", "json"]
PROMPT = """You check whether an agent's plan for a task follows a team's notes. For each task you get the NOTES that
apply (a person's preference or a house rule, each with its path) and the agent's PLAN (a list of choices).
A note is "followed" when the plan contains a choice that carries out what the note says (by content; citing the note
is not needed and citing it is not enough). A note is "contradicted" when a choice goes against it.
Reply with JSON only: {"T1": {"followed": ["<path>", ...], "contradicted": ["<path>", ...]}, ...}

"""


def sections(text):
    parts = re.split(r"^##\s*(T\d+)\b.*$", text, flags=re.M)
    return {parts[i]: parts[i + 1].strip() for i in range(1, len(parts) - 1, 2)}


def note(root, path):
    t = (root / path).read_text().split("\n")
    i = next((k for k, ln in enumerate(t) if ln.startswith("# ")), 0)
    return " ".join(ln.strip() for ln in t[i:i + 6] if ln.strip())[:600]


root, batch = Path(sys.argv[1]), [json.loads(x) for x in Path(sys.argv[2]).read_text().splitlines() if x.strip()]
out = {}
for run in sys.argv[3:]:
    plans = sections(Path(run).read_text())
    body = ""
    for i, t in enumerate(batch, 1):
        notes = "\n".join(f"- {n} [{'person preference' if n.startswith('prefs/') else 'house rule'}]: {note(root, n)}"
                          for n in t["notes"])
        body += f"## T{i}\nTASK: {t['q']}\nNOTES:\n{notes}\nPLAN:\n{plans.get(f'T{i}', '(none)')}\n\n"
    r = subprocess.run(CMD, input=PROMPT + body, capture_output=True, text=True)
    res = json.loads(r.stdout)
    txt = res["result"]
    verdict = json.loads(txt[txt.index("{"):txt.rindex("}") + 1])
    out[run] = {"verdicts": verdict, "cost": res.get("total_cost_usd")}
print(json.dumps(out, indent=1))
