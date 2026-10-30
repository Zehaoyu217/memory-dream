# memory-dream — runbook

Everything runs with stock `python3` (3.9+, stdlib only). Paths are relative to the repo root.

## Install in a project

```bash
cp -R skills/memory-dream  <project>/.claude/skills/memory-dream        # or ~/.claude/skills/
cp skills/memory-dream/agents/memory-dreamer.md <project>/.claude/agents/   # file-mode dreamer
mkdir -p <project>/memory
```

`memory.py` finds the memory root by `--root`, then `$MEMORY_DIR`, then the nearest `memory/`
upward from the cwd, then `./memory`.

## Daily use

```bash
M="python3 .claude/skills/memory-dream/scripts/memory.py"
$M where cards.txn_daily          # entities, headline, relations, notes with path:line
$M where -p churn-2026            # project overview
$M trace churn-xgb-v3             # lineage: what it built on (--down: what built on it)
$M trace cards.txn_daily --down   # entity relations: what depends on it (-e when a note shares the name)
$M log "backfill running" -p churn-2026
$M check                          # every warning C1–C8 in full
```

## Dream (index new or changed notes)

Command mode (default when a command is set):

```bash
export MEMORY_LLM='claude -p --model haiku --tools "" --setting-sources "" --strict-mcp-config --no-session-persistence'
$M dream -j 6
```

`--setting-sources ""` and `--strict-mcp-config` keep the dreamer from loading your CLAUDE.md,
hooks, plugins and MCP servers: each call is then ~4.4k input tokens and ~$0.0015 with Haiku.
`tests/haiku_cmd.py` is the same command with per-call cost logging (`$DREAM_COST_LOG`).

File mode (no command): `dream` writes prompts to `memory/_dream/pending/` and lists them in
`pending/TODO.md`; run the `memory-dreamer` subagent; run `dream` again. A review prompt can
appear on the second pass, so loop until `dream` reports 0 pending (normally 2 rounds).

Other flags: `--review` forces the vocabulary review, `--gists` writes entity gists (entities in
≥ 3 notes), `--all` re-indexes everything (after changing the dreamer model).

## Tests

```bash
python3 tests/acceptance.py                 # A1–A20 with the deterministic fake dreamer (~10 s)
python3 tests/acceptance.py A6 A15          # a subset
python3 tests/real_model.py a3  /tmp/w-a3   # A3/A18 with real Haiku in command mode (~60 s, ~$0.05)
python3 tests/real_model.py a10-prep /tmp/w-a10   # A10: file mode; then run memory-dreamer on
python3 tests/real_model.py a10-next /tmp/w-a10   #   /tmp/w-a10/memory and call a10-next per round
```

- `tests/fixture/memory/` — the churn-2026 world (25 notes + 5 logs). Regenerate with
  `python3 tests/make_fixture.py tests/fixture/memory`.
- `tests/fake_dreamer.py` — oracle answers for the fixture; knobs `FAKE_LOG`, `FAKE_INJECT`,
  `FAKE_REVIEW`, `FAKE_SAVE`, `FAKE_GIST_BAD`.
- `tests/truth.py` — the fixture's true entities, used for A18 convergence.

## A21 agent eval

1. Index a copy of the fixture with Haiku (`real_model.py a3 <w>`).
2. Make worlds: `mem-N` = that memory + `skills/memory-dream/`; `grep-N` = the bare notes.
3. Run a fresh Opus subagent per world with the prompt in `eval/a21/prompts.md` (memory runs get
   SKILL.md only; baseline runs get a one-paragraph description of the note format).
4. Save each answer as `eval/a21/runs/<world>.md`, grade with
   `python3 eval/a21/grade.py eval/a21/runs/*.md`, and record tokens and tool calls reported by
   the harness for each subagent.

## Troubleshooting

- `dream` says C3: the dreamer answer was unusable twice; the note stays grep-searchable and is
  retried on the next `dream`.
- Many `C7 type x? ×1`: single-use proposed relation types; they stay live (marked `?`) and go to
  review once a type has ≥ 2 uses. Edit EDGES.md to alias or drop them by hand (0 calls).
- Delete `memory/_dream/` to rebuild from scratch; EDGES.md and ALIASES.md survive.
