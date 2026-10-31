# memory-dream

Project memory for data-science agents: notes in `memory/` are the truth; a cheap model ("the dreamer")
indexes them into a pointer graph of entities, relations and lineage; `memory.py where | trace` answers
from it. Stdlib Python, markdown + JSON.

- `skills/memory-dream/` — the skill: `SKILL.md`, `scripts/memory.py`, `agents/memory-dreamer.md`
- `.specs/memory-dream/` — `build-spec.md` (v0.4), `RUNBOOK.md`, `RESULTS.md`
- `tests/` — churn-2026 fixture, fake dreamer, `acceptance.py` (A1–A20), `real_model.py` (Haiku)
- `eval/` — real-model outputs and the A21 subagent eval (answers, grades, usage)

```bash
python3 tests/acceptance.py
python3 skills/memory-dream/scripts/memory.py --root tests/fixture/memory ask "what came of exp-014?" "who owns cards.txn_daily?"
python3 skills/memory-dream/scripts/memory.py --root tests/fixture/memory viz --out /tmp/graph.html
```

Answering is grep plus memory: `ask` expands questions through the graph (aliases, ids, lineage),
greps the notes once, and prints the answering lines current-first. Against a grep-only agent it is
as accurate, 0.93× the cost at 30 notes and 0.39–0.47× at 1,677 (`.specs/memory-dream/RESULTS.md`).
`eval/bank/generated/` holds the 56× Haiku-written test bank; `eval/questions/` its 366 questions.
