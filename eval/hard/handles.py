#!/usr/bin/env python3
"""A short phrase for every note of the bank: how a colleague refers to it in passing. One cheap model, once.

  python3 eval/hard/handles.py <dreamed tidy bank> eval/hard/handles.json [-j 6]

One call a folder through `claude -p --model haiku` (no tools, no settings): the notes of the folder as `path | title`,
and for each a phrase of 2 to 6 words that names what it is about and never its id. A phrase is kept only when it
does not contain the note's id and no other note of the folder got the same one; a note without a kept phrase is
simply named by its id in the worn bank. The file is kept in the repository so that make_hard.py needs no model.
"""
import collections
import json
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

PROMPT = """Below are the notes of one project folder, one per line: path | title.
For each note write the short phrase a colleague would use to refer to it in passing, in the middle of a sentence,
when they do not remember its id: 2 to 6 words, lowercase, starting with "the". It says what the note is about (the
dataset, the feature, the model version, the experiment, the decision, the finding, the question), and is specific
enough to tell it from every other note below. It never contains the note's id, its file name or a code such as
exp-404 or v3-final.
Reply with JSON only, one key per note: {"<path>": "<phrase>", ...}

"""
CMD = ["claude", "-p", "--model", "haiku", "--tools", "", "--setting-sources", "", "--strict-mcp-config",
       "--no-session-persistence", "--output-format", "json", "--effort", "low"]


def ask(lines):
    r = subprocess.run(CMD, input=PROMPT + "\n".join(lines) + "\n", capture_output=True, text=True, timeout=600)
    try:
        d = json.loads(r.stdout)
        text = d.get("result", "")
        return json.loads(text[text.index("{"):text.rindex("}") + 1]), d.get("total_cost_usd") or 0
    except (ValueError, KeyError):
        return {}, 0


def main(argv):
    src, out = Path(argv[1]), Path(argv[2])
    j = int(argv[argv.index("-j") + 1]) if "-j" in argv else 6
    g = json.loads((src / "_dream" / "graph.json").read_text())
    by = collections.defaultdict(list)
    for n in g["notes"]:
        if n["project"] != "log" and n["title"]:
            by[n["project"]].append(n)
    areas = sorted(by)
    with ThreadPoolExecutor(j) as ex:
        got = list(ex.map(lambda a: ask([f"{n['path']} | {n['title']}" for n in by[a]]), areas))
    handles, cost, refused = {}, 0, collections.Counter()
    for a, (ans, c) in zip(areas, got):
        cost += c
        seen = collections.Counter(str(v).strip().lower() for v in ans.values())
        for n in by[a]:
            h = str(ans.get(n["path"], "")).strip().rstrip(".").lower()
            words = h.split()
            if not h:
                refused["no answer"] += 1
            elif not (2 <= len(words) <= 7 and words[0] == "the"):
                refused["not a phrase of 2 to 6 words starting with the"] += 1
            elif n["id"].lower() in h or re.search(r"\b[a-z]+-\d|\bv\d+\b|\d{3,}", h) and any(t in h for t in n["id"].lower().split("-") if re.search(r"\d", t)):
                refused["contains the id or a code of it"] += 1
            elif seen[h] > 1:
                refused["not unique in its folder"] += 1
            else:
                handles[n["path"]] = h
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(dict(sorted(handles.items())), indent=0, ensure_ascii=False) + "\n")
    total = sum(len(v) for v in by.values())
    print(f"{len(handles)} of {total} notes have a phrase ({len(areas)} calls, ${cost:.3f}); refused: {dict(refused)}")


if __name__ == "__main__":
    main(sys.argv)
