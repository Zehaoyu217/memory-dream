---
name: memory-dream
description: Project memory for data-science work in memory/ (notes on projects, experiments, findings, decisions, datasets, features, models, people's preferences, reporting rules, terms, corrections). Before making something for someone (chart, table, deck, email, notebook, query), and to answer questions about past work, make ONE call with the tasks and questions — python3 <this skill>/scripts/memory.py ask "q1" "q2" … — it greps the notes with memory (aliases, lineage, superseded → current) and prints the lines that answer each. Write short notes as you work; run memory.py dream at session end.
---
# memory-dream v0.4

Notes in `memory/<area>/<slug>.md` are the truth: plain markdown, so grep and Read work on them as usual.
`memory/_dream/` is generated: graph.html (the viewer; past 10,000 notes an overview, with a page per area in viz/),
index.db and store.db (what ask and dream read), graph.json (small memories). `memory/EDGES.md` and `memory/ALIASES.md` are yours.
`memory.py` = `python3 <this skill>/scripts/memory.py` (root: `--root`, `$MEMORY_DIR`, or the nearest `memory/` upward).

## Read — one call, then answer
- `memory.py ask "<q1>" "<q2>" …` — every question in ONE call: it expands each question through note ids and aliases,
  greps the notes, ranks current notes first, follows `from:`/`supersedes:` lineage, and prints `line: text` under
  `▸ path · kind · date · from … · SUPERSEDED → newer` (a small memory: the whole of it, each question pointing at its notes).
- Answer from that output. A note marked SUPERSEDED is history: its successor is the current answer.
  A `(weak match …)` line names a word found nowhere: rephrase, or grep.
- Name the project or the id when you know it ("… in churn-2026", "exp-014"): it scopes the search.
- About to make something? Ask with the task itself, naming who it is for and the artifact ("Make the Q4 campaign
  chart for Chloe Martin's readout"): it adds the preferences and house rules that apply. Follow them, or say why not.
- A fact missing? ONE batched follow-up: `ask` with sharper words or ids, plain `grep -rn … memory/`, or Read at a printed line.

## Write
1. One note per thing (question, experiment, finding, decision, dataset/feature/model, preference, term, rule,
   correction), in `memory/<project>/`, or for what spans projects in `prefs/`, `reporting/`, `glossary/`,
   `corrections/`, `howto/`, `qa/` or `people/`; the filename is its id (a model's note is named after the model).
2. The `# ` line is the point: the claim, or what the thing is. First paragraph = what is true now.
3. Frontmatter `from: [notes you built on]`, `supersedes: [notes you overturn]`. Never rewrite an old conclusion;
   write a new note (a corrected definition supersedes the old one).
4. Numbers carry metric, eval set, n, date. Sources (tables, notebooks, queries) in backticks.
5. ≤ 40 lines, plain markdown, nothing about the memory system. Scratch: `memory.py log "…" -p <project>`.
6. Taste is said once, in passing ("no pie charts", "round to 1 decimal for the board", "too AI-looking"): when someone
   states a preference or corrects your style, save it then — `prefs/<first>-<last>-<topic>.md` (your user's own:
   `prefs/me-<topic>.md`); the `# ` line is the rule, then where it applies (artifact, meeting, audience) and why.
   When it changes, write a new note with `supersedes:`.

## End of session
`memory.py dream` (background is fine; command mode needs `$MEMORY_LLM`, e.g. `claude -p --model haiku --tools ""`;
without it, run the `memory-dreamer` subagent on the prompts it lists, then `dream` again). It indexes new notes into
entities and typed relations and refreshes `_dream/graph.html`. `memory.py check` lists warnings.
Vocabulary: relation types are closed (EDGES.md); unknown types are held back until the review maps or drops them.
Merge entities by hand with a line in ALIASES.md (`- canonical = other-id`), or keep two apart with `not: a / b`.
