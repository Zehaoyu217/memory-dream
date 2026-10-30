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
python3 skills/memory-dream/scripts/memory.py --root tests/fixture/memory where cards.txn_daily
```
