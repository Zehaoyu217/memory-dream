#!/usr/bin/env python3
"""Grade A21 answers against the key facts. Usage: grade.py answers.md [more.md ...] → JSON per file.

An answer file has sections "## Q1" … "## Q10". A question is correct when every fact matches
(any alternative regex, case-insensitive), partial when at least half do.
"""
import json
import re
import sys
from pathlib import Path

QS = json.loads((Path(__file__).parent / "questions.json").read_text())


def sections(text):
    parts = re.split(r"^##\s*(Q\d+)\b.*$", text, flags=re.M)
    return {parts[i]: parts[i + 1] for i in range(1, len(parts) - 1, 2)}


def grade(text):
    sec, out = sections(text), {}
    for q in QS:
        a = sec.get(q["id"], "")
        hits = [any(re.search(p, a, re.I) for p in alts) for alts in q["facts"]]
        n = sum(hits)
        out[q["id"]] = {"facts": f"{n}/{len(hits)}",
                        "grade": "correct" if n == len(hits) else "partial" if n * 2 >= len(hits) else "wrong",
                        "missing": [alts[0] for alts, h in zip(q["facts"], hits) if not h]}
    return out


if __name__ == "__main__":
    res = {f: grade(Path(f).read_text()) for f in sys.argv[1:]}
    print(json.dumps(res, indent=1))
