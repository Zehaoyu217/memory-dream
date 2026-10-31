---
name: memory-dream
description: Project memory for data-science work in memory/ (notes on projects, experiments, findings, decisions, datasets, features, models, people's preferences, reporting rules, terms, corrections). To answer questions about past work, make ONE call with all your questions — python3 <this skill>/scripts/memory.py ask "q1" "q2" … — it greps the notes with memory (aliases, lineage, superseded → current) and prints the lines that answer each. Write short notes as you work; run memory.py dream at session end.
---
# memory-dream v0.4

Notes in `memory/<area>/<slug>.md` are the truth; plain markdown, so grep and Read work on them as usual.
`memory/INDEX.md` and `memory/_dream/` are generated; `memory/EDGES.md` and `memory/ALIASES.md` are yours to edit.
`memory.py` = `python3 <this skill>/scripts/memory.py` (root: `--root`, `$MEMORY_DIR`, or the nearest `memory/` upward).

## Read — one call, then answer
- `memory.py ask "<q1>" "<q2>" …` — every question in ONE call. It is grep plus memory: it expands each question
  through aliases and note ids, greps the notes, ranks current notes first, follows `from:`/`supersedes:` lineage,
  and prints `line: text` under `▸ path · kind · date · from … · SUPERSEDED → newer` (small memories: whole notes).
- Answer from that output. A note marked SUPERSEDED is history: its successor is the current answer.
- Name the project or the id when you know it ("… in churn-2026", "exp-014"): it scopes the search.
- A fact missing? ONE batched follow-up: `memory.py ask` with sharper words or ids, `memory.py grep -i -e A -e B`
  (grep with the same headers), or Read at a printed line. Don't open INDEX.md or browse note by note.
- Browsing, not answering: `memory.py where <terms>`, `memory.py trace <note|entity> [--down]`, INDEX.md.

## Write
1. One note per thing (question, experiment, finding, decision, dataset/feature/model, preference, term, rule,
   correction), in `memory/<project or area>/`; the filename is its id.
2. The `# ` line is the point: the claim, or what the thing is. First paragraph = what is true now.
3. Frontmatter `from: [notes you built on]`, `supersedes: [notes you overturn]`. Never rewrite an old conclusion;
   write a new note (a corrected definition supersedes the old one).
4. Numbers carry metric, eval set, n, date. Sources (tables, notebooks, queries) in backticks.
5. ≤ 40 lines, plain markdown, nothing about the memory system. Scratch: `memory.py log "…" -p <project>`.

## End of session
`memory.py dream` (background is fine; command mode needs `$MEMORY_LLM`, e.g. `claude -p --model haiku --tools ""`).
If it reports pending prompts, run the `memory-dreamer` subagent, then `memory.py dream` again.
