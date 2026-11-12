"""Batches and prompts for the linkage questions, on workspaces made by make_haiku_arm.py. Answers carry a "Notes:"
line and are scored exactly by eval/linkage.py score.

usage: python3 eval/agent/make_linkage_arm.py <repo> <arm dir> [--global] [<name>=<workspace folder> ...]

  default    eval/questions/linkage-bank.jsonl in tens → batches L1, L2, L3
  --global   eval/questions/linkage-global.jsonl in one batch G1, and the memory prompt carries the skill's own
             "Read first, once" paragraph, as a harness does once the skill is in use
Each <name>=<workspace> gets prompts L<name>-<batch>.txt for the memory in that workspace; the grep prompts
(Lgrep-<batch>.txt) are always written, for the workspace H-grep.
"""
import json
import re
import sys
from pathlib import Path

REPO, ARM = Path(sys.argv[1]), Path(sys.argv[2])
rest = sys.argv[3:]
GLOBAL = "--global" in rest
VARIANTS = dict(a.split("=") for a in rest if "=" in a) or {"mem": "H-mem"}
qs = [json.loads(x) for x in (REPO / "eval/questions" / ("linkage-global.jsonl" if GLOBAL else "linkage-bank.jsonl")).read_text().splitlines() if x.strip()]
skill = (REPO / "skills/memory-dream/SKILL.md").read_text()
desc = re.search(r"^description: (.*)$", skill, flags=re.M).group(1)
step1 = re.search(r"^1\. \*\*Read first, once\.\*\*.*?(?=^2\. )", skill, flags=re.M | re.S).group(0).rstrip() \
    if GLOBAL or "--skill" in rest else ""  # --skill: the same paragraph for the batches of ten
TAIL = """Reply in exactly this format, nothing else:
## Q1
<answer in 1–3 sentences>
Notes: <the paths of the notes that answer the question, comma-separated, like fraud-2025/exp-104.md>
"""
(ARM / "prompts").mkdir(exist_ok=True)
size = len(qs) if GLOBAL else 10
for k in range(0, len(qs), size):
    b = "G1" if GLOBAL else f"L{k // 10 + 1}"
    batch = qs[k:k + size]
    (REPO / "eval/agent/batches" / f"{b}.jsonl").write_text("".join(json.dumps(q) + "\n" for q in batch))
    ql = "".join(f"Q{i} {q['q']}\n" for i, q in enumerate(batch, 1))
    for name, folder in VARIANTS.items():
        W = ARM / folder
        (ARM / "prompts" / f"L{name}-{b}.txt").write_text(
            f"You are answering questions about a data-science team's past work. Work only inside {W} — do not read or\n"
            f"search anything outside it.\n"
            f"The team's memory is in {W}/memory/. You have this skill:\n"
            f"  memory-dream: {desc}\n"
            f"  memory.py = python3 {W}/skills/memory-dream/scripts/memory.py --root {W}/memory\n"
            + (f"  How to read it, from the skill:\n{step1}\n" if step1 else "")
            + f"  (Full instructions, if you need them: {W}/skills/memory-dream/SKILL.md)\n"
            f"This is a read-only task: do not write or edit notes and do not run `dream` or `log`.\n"
            f"Answer these {len(batch)} questions:\n{ql}{TAIL}")
    G = ARM / "H-grep"
    (ARM / "prompts" / f"Lgrep-{b}.txt").write_text(
        f"You are answering questions about a data-science team's past work. Work only inside {G} — do not read or\n"
        f"search anything outside it.\n"
        f"The team's notes are markdown files under {G}/memory/ (one folder per project, plus prefs/, reporting/,\n"
        f"glossary/, corrections/, howto/ and qa/; one note per question, experiment, finding, decision, or\n"
        f"dataset/feature/model description; the `# ` line states the point; frontmatter `from:` names notes it built\n"
        f"on and `supersedes:` names notes it overturns; log/ holds daily scratch lines). Find what you need with grep,\n"
        f"find, ls and cat via Bash, or with Read; you may cat whole folders.\n"
        f"This is a read-only task: do not write or edit anything.\n"
        f"Answer these {len(batch)} questions:\n{ql}{TAIL}")
print(sorted(p.name for p in (ARM / "prompts").glob("L*")))
