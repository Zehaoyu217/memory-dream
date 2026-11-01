---
name: memory-dream
description: Project memory for data-science and coding work. Plain notes in memory/<area>/, one per thing (question, experiment, finding, decision, dataset, feature, model, a person's preference, rule, term, correction). Before answering anything about past work, and before making something for someone (chart, table, deck, email, notebook, query), make ONE call with all your questions and tasks — python3 <this skill>/scripts/memory.py ask "q1" "q2" … — it greps the notes with memory (aliases, lineage, superseded → current, who wants what) and prints the lines that answer. Write a short note per new fact as you work; run memory.py dream at the end.
---
# memory-dream

For any agent with a shell: Python 3.9+ and grep, no model required. The notes in `memory/<area>/<slug>.md` are the
truth; everything else is derived and disposable. `memory.py` = `python3 <this skill>/scripts/memory.py`
(root: `--root`, `$MEMORY_DIR`, or the nearest `memory/` upward).

## What an agent does with memory
1. **Read first, once.** Before answering about past work or making something for someone, put every question and
   task into ONE call: `memory.py ask "what came of exp-014?" "Make the Q4 chart for Chloe Martin's readout"`.
   Per question it prints `line: text` under `▸ path · kind · date · from … · SUPERSEDED → newer`; a small memory is
   printed whole, each question pointing at its notes. SUPERSEDED → a → b is history: the last named is current. For a task it
   adds the preferences and house rules that apply — follow them, or say why not. `(weak match …)` names a word found
   nowhere: rephrase. Name the project or an id when you know it; it scopes the search. At most one batched
   follow-up: `ask` with sharper words, plain `grep -rn … memory/`, or read a printed line.
2. **Write as you go.** One note per thing, in `memory/<project>/`, or for what spans projects in `prefs/`,
   `reporting/`, `glossary/`, `corrections/`, `howto/`, `qa/`, `people/`. The filename is the id (a model's note is
   named after the model; prefixes `exp- feat- ds- dec- fnd- q-` say what it is). The `# ` line is the claim; the
   first paragraph is what is true now. Frontmatter `from: [notes built on]`, `supersedes: [notes overturned]`:
   never rewrite an old conclusion, write a new note that supersedes it. Numbers carry metric, eval set, n, date;
   sources (tables, notebooks, queries) in backticks. ≤ 40 lines, plain markdown, nothing about the memory system.
   Taste is said once, in passing ("no pie charts", "round to 1 decimal for the board", "too AI-looking"): save it
   then — `prefs/<first>-<last>-<topic>.md` (your user's own: `prefs/me-<topic>.md`): the rule, where it applies
   (artifact, meeting, audience), why. When it changes, a new note with `supersedes:`.
3. **Dream at the end.** `memory.py dream` (background is fine) refreshes `_dream/graph.html` — the map, health,
   review queue — the digest `memory/DIGEST.md` and the index. With `$MEMORY_LLM` set (e.g. `claude -p --model haiku
   --tools ""`) a cheap model also names entities and typed relations; without a model nothing is missing for
   answering, and `memory.py dream --prompts` writes prompts for any helper agent (`memory-dreamer`) when you want
   entities too. `memory.py check` lists warnings. Scratch lines: `memory.py log "…" -p <project>`.

## Beside Claude Code's own memory (when you are Claude Code)
CLAUDE.md holds standing instructions people wrote; auto memory holds what you learned about the user; these notes
hold the work itself, with lineage, and travel with the repository. `ask` also reads your auto-memory topic files in
the same call and never writes there. To keep the digest in context every session, add one line to CLAUDE.md:
`@memory/DIGEST.md`. Never the same thing in two places: if CLAUDE.md already says it, write no note.

Three files at the memory root are yours to edit, and a hand edit costs no model calls: `EDGES.md` (relation types —
a link outside them keeps its own label, shown as other/<label>; `promote`, `budget` and `probation` lines gate when a
label becomes a type), `ALIASES.md` (`- canonical = other-id` merges entity ids, `not: a / b` keeps them apart) and
`CONFLICTS.md` (two live notes that disagreed: `- a > b` makes a supersede b without touching either note).
