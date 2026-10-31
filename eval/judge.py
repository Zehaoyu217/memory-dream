#!/usr/bin/env python3
"""Grade agent answers against reference answers with a Haiku judge (headless Claude Code, no tools).

  judge.py <questions.jsonl> <answers.md> [more answers.md ...]  → JSON per file: verdict per question
answers.md has sections "## Q1" … in the order of questions.jsonl. One judge call per answer file.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

PROMPT = """You grade answers about a data-science team's project memory. For each item compare the CANDIDATE
answer with the REFERENCE answer. Verdicts:
- "correct": states the reference's key facts (numbers, ids, the current version or definition); extra
  correct detail is fine.
- "partial": some key facts right, some missing, nothing wrong that contradicts the reference.
- "wrong": misses the main point, gives a superseded/old value as current, or contradicts the reference.
Reply with JSON only: {"Q1": {"v": "correct|partial|wrong", "why": "<= 15 words"}, ...}

"""


def sections(text):
    parts = re.split(r"^##\s*(Q\d+)\b.*$", text, flags=re.M)
    return {parts[i]: parts[i + 1].strip() for i in range(1, len(parts) - 1, 2)}


def judge(items, answers):
    body = "".join(f"### Q{i}\nQUESTION: {q['q']}\nREFERENCE: {q['a']}\nCANDIDATE: {answers.get(f'Q{i}', '(no answer)')[:1500]}\n\n"
                   for i, q in enumerate(items, 1))
    cmd = ["claude", "-p", "--model", "haiku", "--tools", "", "--setting-sources", "", "--strict-mcp-config",
           "--no-session-persistence"]
    for _ in range(2):
        r = subprocess.run(cmd, input=PROMPT + body, capture_output=True, text=True)
        out = r.stdout
        i, j = out.find("{"), out.rfind("}")
        try:
            return json.loads(out[i:j + 1])
        except ValueError:
            continue
    return {}


if __name__ == "__main__":
    items = [json.loads(x) for x in Path(sys.argv[1]).read_text().splitlines() if x.strip()]
    res = {}
    for f in sys.argv[2:]:
        v = judge(items, sections(Path(f).read_text()))
        res[f] = {"verdicts": v, "correct": sum(1 for x in v.values() if x.get("v") == "correct"),
                  "partial": sum(1 for x in v.values() if x.get("v") == "partial"),
                  "wrong": sum(1 for x in v.values() if x.get("v") == "wrong")}
    print(json.dumps(res, indent=1, ensure_ascii=False))
