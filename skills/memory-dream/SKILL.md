---
name: memory-dream
description: Project memory for work done with an agent, in any field (data, analytics, software, finance, research, operations). Plain notes in memory/<area>/, one per thing (a question, a result, a decision, a dataset, a model, a plan, a risk, a rule, a term, a person's preference). Before answering anything about past work or making something for someone, read the memory in one call; write a note for each new fact or decision; dream at the end to index and check.
---
# memory-dream

For any agent with a shell: Python 3.9+ and grep, no model required. The notes in `memory/<area>/<slug>.md` are the
truth; everything else is derived and disposable. `memory.py` = `python3 <this skill>/scripts/memory.py`
(root: `--root`, `$MEMORY_DIR`, or the nearest `memory/` upward).

## What an agent does with memory
1. **Read first, once.** Before answering about past work or making something for someone, put every question and
   task into ONE call: `memory.py ask "what came of exp-014?" "Make the Q4 chart for Chloe Martin's readout"`.
   Per question it prints `line: text` under `▸ path · kind · date · from … · SUPERSEDED → newer`; a small memory is
   printed whole, each question pointing at its notes. SUPERSEDED → a → b is history: the last named is current. For a
   task it adds the preferences and house rules that apply — follow them, or say why not. `(weak match …)` names a word
   found nowhere: rephrase. Name the area or an id when you know it; it scopes the search. At most one batched
   follow-up: `ask` with sharper words, plain `grep -rn … memory/`, or read a printed line.
2. **Write as you go.** One note per thing, in `memory/<project>/`, or for what spans projects in `prefs/`,
   `reporting/`, `glossary/`, `corrections/`, `howto/`, `qa/`, `people/`. The filename is the id; a prefix from
   `memory/KINDS.md` says what kind of note it is (`exp- fnd- dec- plan- risk- inc- ds- feat- q- …`; a thing's own note
   is named after the thing, `churn-xgb-v3`). The `# ` line is the claim; the first paragraph is what is true now.
   Frontmatter `from: [notes built on]`, `supersedes: [notes overturned]`, `updated: YYYY-MM-DD`: never rewrite an old
   conclusion, write a new note that supersedes it. Numbers carry their unit or metric, their basis (the data, the
   period, the sample), and the date; sources (tables, documents, queries, tickets) in backticks. ≤ 40 lines, plain
   markdown, nothing about the memory system. Taste is said once, in passing ("no pie charts", "round to one decimal
   for the board"): save it then — `prefs/<first>-<last>-<topic>.md` (your user's own: `prefs/me-<topic>.md`): the rule,
   where it applies, why. When it changes, a new note with `supersedes:`.
3. **Dream at the end.** `memory.py dream` (background is fine) refreshes `_dream/graph.html` — the map, what is worth
   checking, the review queue — the digest `memory/DIGEST.md` and the index. With `$MEMORY_LLM` set (e.g. `claude -p
   --model haiku --tools ""`) a cheap model also names the things each note mentions and the typed links between them;
   without a model nothing is missing for answering, and `memory.py dream --prompts` writes prompts for any helper agent
   (`memory-dreamer`) when you want the things too. `memory.py check` lists warnings. Scratch lines: `memory.py log "…" -p
   <project>`.

## The domain is three files you may edit, never the code
`memory/KINDS.md` (kinds of note: prefixes, areas, roles), `memory/TYPES.md` (types of thing: what each is and is not,
its aliases, its family) and `memory/EDGES.md` (types of link between things). All three are seeded for data,
analytics, software and finance work; `pack: research` or `pack: ops` adds a domain's lines. The model is only ever
asked to use what these files list; a word that fits nothing is kept as `other/<word>`, and becomes a type through the
review once it is common. A hand-written line is permanent and costs no model calls: the graph is re-derived from the
cached readings. Add types freely; to retire one, merge it (add it to another type's `aka`) rather than delete it, so
nothing already read is lost. `ALIASES.md` (`- canonical = other-id`, `not: a / b`) and `CONFLICTS.md` (`- a > b`
makes a supersede b without touching either note) are the other two files at the root that are yours.

## Beside Claude Code's own memory (when you are Claude Code)
CLAUDE.md holds standing instructions people wrote; auto memory holds what you learned about the user; these notes
hold the work itself, with lineage, and travel with the repository. `ask` also reads your auto-memory topic files in
the same call and never writes there. To keep the digest in context every session, add one line to CLAUDE.md:
`@memory/DIGEST.md`. Never the same thing in two places: if CLAUDE.md already says it, write no note.
