"""Workspaces and prompts for a Haiku arm of the agent eval (BUILD-GUIDE §7.3), from a dreamed bank-index world.

usage: python3 eval/agent/make_haiku_arm.py <repo> <dreamed bank-index world: .../memory> <out dir>
"""
import json
import re
import shutil
import sys
from pathlib import Path

REPO, WORLD, OUT = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
MEM, GREP = OUT / "H-mem", OUT / "H-grep"
if OUT.exists():
    shutil.rmtree(OUT)
shutil.copytree(WORLD, MEM / "memory")
shutil.copytree(REPO / "skills/memory-dream", MEM / "skills/memory-dream", ignore=shutil.ignore_patterns("__pycache__"))
shutil.copytree(WORLD, GREP / "memory", ignore=shutil.ignore_patterns("_dream", "KINDS.md", "TYPES.md", "EDGES.md", "ALIASES.md",
                                                                      "CONFLICTS.md", "DIGEST.md"))
desc = re.search(r"^description: (.*)$", (REPO / "skills/memory-dream/SKILL.md").read_text(), flags=re.M).group(1)
TAIL = """Reply in exactly this format, nothing else:
## Q1
<answer in 1–4 sentences with the key numbers>
Sources: <note paths>
"""
(OUT / "prompts").mkdir()
for b in ("P1", "C-h1", "P2"):
    qs = [json.loads(x) for x in (REPO / "eval/agent/batches" / f"{b}.jsonl").read_text().splitlines() if x.strip()]
    ql = "".join(f"Q{i} {q['q']}\n" for i, q in enumerate(qs, 1))
    mem = (f"You are answering questions about a data-science team's past work. Work only inside {MEM} — do not read or\n"
           f"search anything outside it.\n"
           f"The team's memory is in {MEM}/memory/. You have this skill:\n"
           f"  memory-dream: {desc}\n"
           f"  memory.py = python3 {MEM}/skills/memory-dream/scripts/memory.py --root {MEM}/memory\n"
           f"  (Full instructions, if you need them: {MEM}/skills/memory-dream/SKILL.md)\n"
           f"This is a read-only task: do not write or edit notes and do not run `dream` or `log`.\n"
           f"Answer these 10 questions:\n{ql}{TAIL}")
    grep = (f"You are answering questions about a data-science team's past work. Work only inside {GREP} — do not read or\n"
            f"search anything outside it.\n"
            f"The team's notes are markdown files under {GREP}/memory/ (one folder per project, plus prefs/, reporting/,\n"
            f"glossary/, corrections/, howto/ and qa/; one note per question, experiment, finding, decision, or\n"
            f"dataset/feature/model description; the `# ` line states the point; frontmatter `from:` names notes it built\n"
            f"on and `supersedes:` names notes it overturns; log/ holds daily scratch lines). Find what you need with grep,\n"
            f"find, ls and cat via Bash, or with Read; you may cat whole folders.\n"
            f"This is a read-only task: do not write or edit anything.\n"
            f"Answer these 10 questions:\n{ql}{TAIL}")
    (OUT / "prompts" / f"H-mem-{b}.txt").write_text(mem)
    (OUT / "prompts" / f"H-grep-{b}.txt").write_text(grep)
print("workspaces:", MEM, GREP)
print("prompts:", sorted(p.name for p in (OUT / "prompts").iterdir()))
