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
$M ask "what came of exp-014?" "who owns cards.txn_daily?"   # answering: grep + memory, every question in one call
$M viz                            # memory/_dream/graph.html (dream refreshes it): overview, explorer, health
$M log "backfill running" -p churn-2026
$M check                          # every warning C1–C9 in full
grep -rn velocity memory/ --exclude-dir=_dream                 # plain grep stays first-class
```

Viewer deep links: `graph.html#note=<path>`, `#entity=<id>`, `#health`.

## Entities and the relation vocabulary

- Relation types are closed: the 8 in EDGES.md, plus their aliases (`~` = read in reverse) and a
  `drop:` list. The dreamer may use only those. Anything else is held back at merge and counted
  (C7), and a type used 3 or more times goes to the review. The review may only map it onto a
  listed type or drop it; new types come from you editing EDGES.md. Editing EDGES.md costs 0 calls,
  since everything relabels at the next merge.
- An entity is kept when it has a home note (a note whose slug is its id, e.g. the model's own
  note), is mentioned in 2 or more notes, or is named in ALIASES.md. Files, notebooks, columns and
  note ids are not entities; grep finds them.
- Identity: `.`, `_`, `-`, spaces and case don't distinguish ids (`cards.txn_daily` =
  `cards-txn-daily`).
- A free rule merges an id that exactly one other entity writes as a surface form. Ids that differ
  only in digits (versions) never merge.
- Two entities with different home notes are never queued for review. Other look-alikes are asked
  once, and the answer lands in ALIASES.md as `- a = b` or `not: a / b`.
- Lineage between notes (`from:`, `supersedes:`, and note ids written in a body) is not a relation:
  it needs no model and no vocabulary.

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

Other flags: `--review` forces the vocabulary review, `--all` re-indexes everything (after changing
the dreamer model). Indexing is optional for answering: `ask` works on raw notes (grep plus lineage);
the index adds aliases, typed relations and the viewer's entity views.

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

## Round 2: 50× bank, retrieval and agent eval

```bash
python3 eval/bank/split.py <bundles dir> eval/bank/generated eval/questions   # Haiku-written bundles → notes + questions
python3 eval/bank/assemble.py eval/bank/generated tests/fixture/memory <out>/memory   # big bank = generated + churn-2026
python3 eval/retrieval.py <memory root> eval/questions/bank-*.jsonl             # offline: gold-note and number recall of `ask`
python3 eval/agent/make_batches.py                                               # C-orig, C-h1, C-h2, P1, P2 (seeded)
python3 eval/a21/extract.py eval/agent/runs NAME=<subagent transcript> …         # report + usage per run
python3 eval/judge.py eval/agent/batches/<B>.jsonl eval/agent/runs/<run>.md      # Haiku judge vs reference answers
python3 eval/agent/summarize.py                                                  # per cell: accuracy, calls, tokens, cost, time
```

Agent prompts: memory runs get the skill's name and description (as a session lists skills) and the
path to SKILL.md; grep runs get a one-paragraph description of the note folders. Both get the same 10
questions and the same reply format. `MEMORY_DEBUG=1 memory.py ask …` prints the ranking to stderr.

## Round 4: 100× (168,141 notes)

```bash
python3 eval/scale/make_world.py <indexed 1,677-note memory> <out>/memory --copies 137   # sibling copies, already indexed
python3 eval/scale/bootstrap.py <out>/memory          # first dream, timed (review history taken as done)
python3 eval/scale/time_ask.py <memory root> …         # one ask per batch: seconds, characters printed
python3 eval/scale/trace_ask.py <memory root> P2       # where one ask spends its time: load, routing, each grep
python3 eval/retrieval.py <memory root> eval/questions/bank-*.jsonl
MEMORY_WIDE=100 python3 eval/retrieval.py …            # force big-memory routing on a small memory
python3 eval/agent/judge_x100.py                        # grade the six A24 runs (after extract.py)
```

Above `MEMORY_WIDE` notes (default 10,000), `ask` greps only where each question points: the project it
names; otherwise areas whose note ids and titles match, areas the index says mention its ids, and the
general areas (prefs, reporting, glossary, corrections, howto, qa, people, log, or any area whose notes
are mostly not project work). Changed notes are patched into the last graph instead of a rebuild.

What dream writes in `_dream/`: `store.db` (its caches: parsed note facts by path, extractions by content hash;
the files in `_dream/notes/` stay the source), `index.db` (the graph as SQLite: `ask` on a big memory reads only the
rows a question needs), and the viewer. Up to `MEMORY_WIDE` notes: `graph.json` + one `graph.html`. Past it: no
graph.json; `graph.html` is an overview of areas and `viz/<area>.html` one page per area, redrawn only when that
area changed (`viz/_sig.json`). A dream with nothing new stops after the scan.

```bash
python3 eval/scale/profile_dream.py <memory root>                       # where a full rebuild spends its time
python3 eval/scale/profile_incremental.py <memory root> <scratch> fraud-2026   # re-index one area with the fake dreamer
```

## Troubleshooting

- `dream` says C3: the dreamer answer was unusable twice; the note stays grep-searchable and is
  retried on the next `dream`.
- Many `C7 type x? ×1`: single-use proposed relation types; they stay live (marked `?`) and go to
  review once a type has ≥ 2 uses. Edit EDGES.md to alias or drop them by hand (0 calls).
- `check` says C9: the note contains NUL bytes (a binary paste, a bad encoding). `ask` still greps it (`grep -a`),
  but keep notes plain text.
- `ask` prints `(weak match: 'x' found nowhere in memory …)`: a word of the question occurs in no note and the best
  note covers at most half of the question's words; the notes shown are a guess. Rephrase, or grep.
- On a small memory (≤ 200 notes) `ask` prints the whole memory after the per-question pointers whenever that costs
  about the same as the surgical lines (within 1.2×): nothing is missed, and it is no dearer than `cat`.
- Delete `memory/_dream/` to rebuild from scratch; EDGES.md and ALIASES.md survive.
