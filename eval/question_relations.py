#!/usr/bin/env python3
"""Which link does each question need? Haiku labels every question in the bank (batched, no tools).

  question_relations.py eval/questions/*.jsonl
Labels: lineage (built on / came of / why / supersedes between notes), one of the 8 relation types,
none (the answer sits in one note's text), or other:<name>.
"""
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

LABELS = "lineage, uses, produces, part-of, trained-on, evaluated-on, measured-by, replaces, owned-by, none"
PROMPT = f"""You audit questions asked of a data-science team's notes. For each question, name the one kind of
link between things that answering it needs:
- lineage: how notes build on each other (what came of an experiment, what led to a decision, why something
  changed, what superseded what)
- uses | produces | part-of | trained-on | evaluated-on | measured-by | replaces | owned-by: a typed link between
  things (X uses table Y, model trained on Y, owned by team Y, metric Y, ...)
- none: the answer is stated inside a single note (a definition, a number, a preference, a rule)
- other:<short name>: a typed link between things that none of the above covers
Reply with JSON only: {{"<id>": "<label>", ...}}

"""


def ask(batch):
    body = "".join(f"{i}: {q['q']}\n" for i, q in batch)
    cmd = ["claude", "-p", "--model", "haiku", "--tools", "", "--setting-sources", "", "--strict-mcp-config",
           "--no-session-persistence"]
    out = subprocess.run(cmd, input=PROMPT + body, capture_output=True, text=True).stdout
    try:
        return json.loads(out[out.find("{"):out.rfind("}") + 1])
    except ValueError:
        return {}


items = [(f"{Path(f).stem}#{k}", json.loads(x)) for f in sys.argv[1:]
         for k, x in enumerate(Path(f).read_text().splitlines()) if x.strip()]
labels = {}
for i in range(0, len(items), 70):
    labels.update(ask(items[i:i + 70]))
c = Counter(str(v).split(":")[0].strip() for v in labels.values())
other = Counter(str(v) for v in labels.values() if str(v).startswith("other"))
by = {i: q for i, q in items}
print(json.dumps({"questions": len(items), "labelled": len(labels), "counts": c.most_common(),
                  "other": other.most_common(20)}, indent=1))
for i, v in labels.items():
    if str(v).startswith("other"):
        print(f"  {v:28} {by.get(i, {}).get('q', '')[:110]}")
Path("eval/question_relations.json").write_text(json.dumps(labels, indent=1))
