#!/usr/bin/env python3
"""Taste eval: tasks an agent is handed for a person (a chart, a deck, a table), where that person's preferences and
the house rules should shape the result without being named. Haiku writes them per person; gold = note paths.

  make_tasks.py <memory root> <out.jsonl>
"""
import json
import re
import subprocess
import sys
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

root, out = Path(sys.argv[1]), Path(sys.argv[2])
CMD = ["claude", "-p", "--model", "haiku", "--tools", "", "--setting-sources", "", "--strict-mcp-config",
       "--no-session-persistence", "--output-format", "json"]
PROMPT = """You write evaluation tasks for a data-science team's shared memory. Below are every preference note
about {person}, and the titles of the team's house rules.

Write 4 tasks that a colleague might hand an AI agent where {person}'s preferences should shape the result:
- 2 tasks name {person}; 2 name only their meeting, report or audience as these notes describe it (e.g. "the weekly
  alert review", "the board pack"), not the person.
- Each task names the artifact to make (chart, table, deck, slide, model card, email, alert, notebook, ...) and its
  subject, like a real request: "Build the chart for Chloe's Q4 campaign readout: five campaigns, three segments."
- Never use the preferences' own wording or values: no colours, no chart-type bans, no numbers or thresholds from
  the notes. The task must not give the answer away.
For each task list the notes that should shape the result: {person}'s preference notes that apply, and the house
rules that apply. Use only paths listed below.

Reply with JSON only: {{"tasks": [{{"q": "...", "variant": "named" or "implicit", "notes": ["prefs/x.md", "reporting/y.md"]}}]}}

## {person}'s preference notes
{prefs}

## House rules (path: title)
{rules}
"""


def title(p):
    m = re.search(r"^# (.+)$", p.read_text(), re.M)
    return m.group(1) if m else p.stem


people = defaultdict(list)
for p in sorted((root / "prefs").glob("*.md")):
    people["-".join(p.stem.split("-")[:2])].append(p)
rules = "\n".join(f"{p.relative_to(root).as_posix()}: {title(p)}" for d in ("reporting", "howto")
                  for p in sorted((root / d).glob("*.md")))
known = {p.relative_to(root).as_posix() for d in ("prefs", "reporting", "howto") for p in (root / d).glob("*.md")}


def ask(item):
    slug, files = item
    person = " ".join(w.capitalize() for w in slug.split("-"))
    prefs = "\n\n".join(f"### {p.relative_to(root).as_posix()}\n{p.read_text()}" for p in files)
    r = subprocess.run(CMD, input=PROMPT.format(person=person, prefs=prefs, rules=rules), capture_output=True, text=True)
    try:
        res = json.loads(r.stdout)
        txt = res["result"]
        tasks = json.loads(txt[txt.index("{"):txt.rindex("}") + 1])["tasks"]
    except (ValueError, KeyError):
        return slug, [], 0.0
    return slug, tasks, res.get("total_cost_usd") or 0.0


rows, cost = [], 0.0
with ThreadPoolExecutor(6) as ex:
    for slug, tasks, c in ex.map(ask, sorted(people.items())):
        cost += c
        for t in tasks:
            notes = [n for n in t.get("notes", []) if n in known]
            if t.get("q") and notes:
                rows.append({"type": "taste-" + t.get("variant", "named"), "q": t["q"], "a": "", "notes": notes,
                             "bundle": f"prefs-{slug}"})
out.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
print(f"{len(rows)} tasks for {len(people)} people · ${cost:.3f}")
