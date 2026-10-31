# memory-dream

Project memory for data-science agents: notes in `memory/` are the truth; `memory.py ask` answers by
grep plus a thin layer of lineage and names; an optional cheap model ("the dreamer") adds entities and
typed relations for aliases and the viewer (`memory.py viz`). Stdlib Python, markdown + JSON.

- `skills/memory-dream/` — the skill: `SKILL.md`, `scripts/memory.py`, `agents/memory-dreamer.md`
- `.specs/memory-dream/` — `build-spec.md` (v0.4), `RUNBOOK.md`, `RESULTS.md`
- `tests/` — churn-2026 fixture, fake dreamer, `acceptance.py` (A1–A20), `real_model.py` (Haiku)
- `eval/` — real-model outputs and the A21 subagent eval (answers, grades, usage)

```bash
python3 tests/acceptance.py
python3 skills/memory-dream/scripts/memory.py --root tests/fixture/memory ask "what came of exp-014?" "who owns cards.txn_daily?"
python3 skills/memory-dream/scripts/memory.py --root tests/fixture/memory viz --out /tmp/graph.html
```

For any agent with a shell (Python 3.9+, grep; a model is optional). Beside Claude Code's own memory: `ask` also
reads the project's auto-memory topic files and never writes there; one line in CLAUDE.md, `@memory/DIGEST.md`,
keeps the ≤ 40-line digest that every `dream` writes in context. Relation types are a constrained open vocabulary
(links outside it keep their label; promotion is gated by evidence, a budget and probation); live notes that may
disagree are queued for a reviewing subagent, whose verdicts persist in `memory/CONFLICTS.md`. Review and measured
phases: `.specs/memory-dream/REVIEW.md`, `RESULTS.md`.

Answering is grep plus memory: `ask` expands questions through the graph (aliases, ids, lineage),
greps the notes once, and prints the answering lines current-first. Against a grep-only agent it is
as accurate, 0.93× the cost at 30 notes and 0.39–0.47× at 1,677 (`.specs/memory-dream/RESULTS.md`); on the
1,677-note bank it heads 92% of the gold notes at ~2.2k characters per question, and a quarter of the tool calls
of a grep agent. No model is needed; a cheap one adds entities for the viewer.
`eval/bank/generated/` holds the 56× Haiku-written test bank; `eval/questions/` its 366 questions.
