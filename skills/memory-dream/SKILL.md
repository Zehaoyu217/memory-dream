---
name: memory-dream
description: Project memory for data-science work in memory/. Write short notes as you work, find them with memory.py where, follow lineage and dependencies with memory.py trace, and run memory.py dream at session end so a cheap model indexes new notes. Use whenever a session touches a project, dataset, feature, model, experiment, finding or decision, or when asked to remember or recall.
---
# memory-dream v0.4

Notes in `memory/<project>/<slug>.md` are the truth. `memory/INDEX.md` and `memory/_dream/` are generated; never edit them. `memory/EDGES.md` (relation types) and `memory/ALIASES.md` (entity merges) are yours to edit.
`memory.py` = `python3 <this skill>/scripts/memory.py` (root: `--root`, `$MEMORY_DIR`, or the nearest `memory/` upward).

## Read
- Start: the head of `memory/INDEX.md`, or `memory.py where -p <project>`.
- `memory.py where <terms>`: entities with headline and relations, notes and `path:lines` pointers; superseded notes show their successor. Read what it points to, nothing more.
- `memory.py trace <note>` (what it built on) · `--down` (what built on it). On an entity, `trace <entity> --down` = what depends on it (`-e` if a note has the same name).
- Summaries and relations are hints from a cheap model; the note is the source.

## Write
1. One note per thing (question, experiment, finding, decision, or a dataset/feature/model/metric description), in `memory/<project>/`; the filename is its id.
2. The `# ` line is the point: the claim, or what the thing is. First paragraph = what is true now.
3. Frontmatter `from: [notes you built on]`, `supersedes: [notes you overturn]`. Never rewrite an old conclusion; write a new note.
4. Numbers carry metric, eval set, n, date. Sources (tables, notebooks, queries) in backticks.
5. ≤ 40 lines, plain markdown, nothing about the memory system.
Mid-session scratch: `memory.py log "…" -p <project>`.

## End of session
`memory.py dream` (background is fine; command mode needs `$MEMORY_LLM`, e.g. `claude -p --model haiku --tools ""`). If it reports pending prompts, run the `memory-dreamer` subagent, then `memory.py dream` again. `memory.py check` lists warnings.
