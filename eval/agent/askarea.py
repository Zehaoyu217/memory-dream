#!/usr/bin/env python3
"""An experiment, not shipped code: `ask` that first finds where the questions live.

Copied into a workspace beside memory.py. It runs the same `memory.py ask`, then looks at the call as a whole: when
at least half of the questions (and at least two) have a note of one project folder among their first three notes,
and that folder is small, the folder is printed whole once at the end, and under each question its notes are listed
as pointers. Everything else is printed as memory.py prints it.

  askarea.py --root <memory> ask "q1" "q2" ...        ASKAREA_MAX (default 16000) characters a folder may have
"""
import collections
import os
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
GENERAL = {"prefs", "reporting", "glossary", "corrections", "howto", "qa", "people", "log"}
args = sys.argv[1:]
root = Path(args[args.index("--root") + 1]) if "--root" in args else None
out = subprocess.run([sys.executable, str(HERE / "memory.py"), *args], capture_output=True, text=True)
sys.stderr.write(out.stderr)
if "ask" not in args or root is None:
    sys.stdout.write(out.stdout)
    sys.exit(out.returncode)
parts = re.split(r"^(## .*)$", out.stdout, flags=re.M)
secs = [(parts[i], parts[i + 1]) for i in range(1, len(parts) - 1, 2)]
votes = collections.Counter()
for _, body in secs:
    heads = re.findall(r"^▸ (\S+\.md)", body, flags=re.M)[:3]
    for a in {h.split("/")[0] for h in heads if "/" in h} - GENERAL:
        votes[a] += 1
limit = int(os.environ.get("ASKAREA_MAX", "16000"))
whole = [a for a, n in sorted(votes.items()) if n >= max(2, (len(secs) + 1) // 2)
         and sum(p.stat().st_size for p in (root / a).glob("*.md")) <= limit]
if not whole:
    sys.stdout.write(out.stdout)
    sys.exit(0)
res = [parts[0].rstrip("\n")] if parts[0].strip() else []
for head, body in secs:
    res.append(head)
    lines = body.strip("\n").split("\n")
    # a question that points at a folder printed whole keeps the lines of the general areas only (rules, terms,
    # corrections); notes of other projects stay as one-line pointers
    here = any(h.split("/")[0] in whole for h in re.findall(r"^▸ (\S+\.md)", body, flags=re.M)[:3])
    skip = False
    for ln in lines:
        m = re.match(r"▸ (\S+\.md)", ln)
        if m:
            area = m.group(1).split("/")[0]
            skip = area in whole or (here and area not in GENERAL)
            res.append(ln.split(" · ")[0] + ("  (whole, below)" if area in whole else "  (another project)") if skip else ln)
        elif not (skip and re.match(r"\s+\d+: ", ln)):
            skip = False
            res.append(ln)
for a in whole:
    notes = sorted((root / a).glob("*.md"))
    res.append(f"## {a}/ — the whole folder, {len(notes)} notes: nothing else is recorded in this project")
    for p in notes:
        text = p.read_text().split("\n")
        fm = text[1:next((i for i in range(1, len(text)) if text[i].strip() == "---"), 0)] if text and text[0].strip() == "---" else []
        meta = " · ".join(x.strip() for x in fm if re.match(r"(from|supersedes|updated):", x.strip()))
        res.append(f"▸ {a}/{p.name}" + (f" · {meta}" if meta else ""))
        start = len(fm) + 2 if fm or (text and text[0].strip() == "---") else 0
        res += [f"  {t.strip()}" for t in text[start:] if t.strip()]
sys.stdout.write("\n".join(res) + "\n")
