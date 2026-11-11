# memory-dream: handoff, 2026-11-02

Branch `production-readiness`, four commits on `worktree-build-v0.4` (102cbc0). Not merged; no pull request. This file
is the state of the work at the end of the session that made those commits, for whoever picks it up.

## In one paragraph

The repository does what its README claims, and the README now says what the evidence supports. The session
re-evaluated the claims against the code (2026-11-01), closed the gaps that needed no agent runs, added a store seam so
the graph can live in PostgreSQL (or Neo4j, untested), and measured how the graph serves retrieval on a real index. One
hop of typed links adds nothing; two hops for input questions lift dependency answers from 0.853 to 0.920 of gold notes
for 4.6% more characters, kept as the default. The real index is now in the repository, so every with-index number
rebuilds with no model call. CI is written and has never run.

## Verified at the end of the session

| check | command | result |
|---|---|---|
| acceptance | `python3 tests/acceptance.py` | 38/38, about 27 s, no model |
| retrieval, bank, no index | `python3 tests/retrieval_gate.py bank` | gold 0.939 · numbers 0.979 · stale 0.962 / 1.0 · absence 1.0 |
| retrieval, bank, real index | `python3 tests/retrieval_gate.py bank-index` | gold 0.941 · numbers 0.978 · alias 0.821 · about 60 s, 0 calls |
| retrieval, software fixture | `python3 tests/retrieval_gate.py software` | gold 1.00 · numbers 1.00 · stale 1.0 / 1.0 |
| PostgreSQL store | `MEMORY_STORE_URL=… python3 tests/store_parity.py postgres [--bank]` | 11/11 after the last code change; 13/13 with `--bank` at 8666ffc; needs `psycopg[binary]` |
| viewer, headless | `node tests/viz_check.js <graph.html>` | 15/15, needs Playwright |
| build bundle | `python3 tests/bundle_refresh.py --check` | fresh |

`.github/workflows/ci.yml` runs all of them (the store test without `--bank`). It was pushed at the end of the session
and no run has been read. Python 3.9 is checked for syntax and for a few 3.10-only library calls, not run.

## Commits

| commit | content |
|---|---|
| 8666ffc | README from the latest run on shipped code, Limits, conflict precision and the unmeasured digest disclosed; software kinds and types in the seeds, the payments-api fixture and 30 questions; the `MEMORY_STORE` seam (`stores.py`: PostgreSQL, Neo4j, CSV export; `memory.py export`); ADR-001; LICENSE; CI; `tests/retrieval_gate.py`; `bundle_refresh.py --check`; doc drift fixed |
| 5a28021 | the typed-link walk in `ask` behind knobs; `retrieval.py --by-type`; `eval/ab_env.py` |
| c8973d6 | phase I: the bank indexed with Haiku ($2.72), kept as readings in `eval/real/bank-index/` with `restore.py`; the walk measured and kept; RESULTS phase I |
| this one | this handoff; README dedup counts from the kept index; the export's verification stated correctly |

## The re-evaluation of 2026-11-01, gap by gap

| gap found | status |
|---|---|
| headline cost and time came from a run before the retrieval rewrite | fixed: README leads with RESULTS phase G on shipped code; older cells are labelled as older |
| evidence small and synthetic, not said | said in Limits; still synthetic |
| with-index numbers needed model calls to reproduce | fixed: readings in the repository, 0-call rebuild, gated in CI |
| nothing exercised a coding project | partly fixed: software kinds and types seeded; payments-api fixture (30 notes, 30 questions). A helper agent wrote it and iterated until the gate passed, so it is a smoke test of the software path, not a benchmark |
| the conflict detector's 6% precision not said | said |
| the digest recommended without evidence | said to be unmeasured; still unmeasured |
| no limits section | added |
| no licence | MIT added, holder taken from the git author name; the owner should confirm |
| no CI | added; never run |
| no tags or releases | open |
| the only branch is `worktree-build-v0.4` | open |
| twelve vs thirteen checks, three costs per note, unsourced dedup counts, an old 168k timing, old tab names and test counts, a docstring pointing at the first spec, incomplete install steps | fixed |
| `memory.py check \| head` ends in a BrokenPipeError traceback | open |

## Hosting and the store (ADR-001, proposed, not signed off)

- Git stays the truth; a store holds a copy of the graph and can be dropped. `memory.py` stays standard-library only and
  imports `stores.py` only when `MEMORY_STORE` is set.
- PostgreSQL: tested. A dream publishes a diff keyed by content hash under an advisory lock (1,677 notes: 5,355 rows in
  0.3 s). `ask` through the store prints byte-identical output, and retrieval on the bank is identical (0.939 / 0.979).
  A store that is down falls back to the local index with one line on stderr. A version mismatch republishes everything.
- Neo4j: written against the 5.x driver, never run. The container had a Docker client with no daemon, and the network
  proxy refused the Neo4j download.
- Export (`memory.py export --to DIR`): CSV in neo4j-admin header format, `import.sh`, `load.cypher`, `meta.json`.
  Checked only for its files and counts; never imported into Neo4j. Earlier reports in the session called the export
  the verified path into a graph database. That overstated it, and the docs now say so.
- The service was not built, by the owner's decision on 2026-11-02. A skeleton existed in the session's scratch space
  and is not preserved.
- Only the publish is incremental. A dream still rebuilds the whole graph in memory (4.8 GB peak at 168,141 notes).

## The graph in retrieval (RESULTS phase I)

On a fresh real index, 326 questions:

| | no index | index, walk off | index, walk on (default) |
|---|---|---|---|
| gold notes headed | 0.937 | 0.933 | 0.941 |
| complete answers | 272 | 270 | 274 |
| dependency questions, gold | 0.853 | 0.853 | 0.920 |
| alias questions, gold | 0.771 | 0.821 | 0.821 |
| characters per question | 2,368 | 2,484 | 2,598 |

The walk runs only when the question asks about inputs or users. It follows `uses`, `trained-on`, `part-of` and `from:`
two steps (inputs of inputs and the predecessor's inputs; the users for "what uses X") and adds at most 8 one-line
pointers. It costs about 9,300 characters per extra complete answer, more than earlier additions paid, and was kept
because it spends only on the questions it serves. `MEMORY_RELATION_LINES=0` switches it off; `MEMORY_RELATION_HOPS` and
`MEMORY_RELATION_MODE` are the other knobs, and `eval/ab_env.py` measures any of them.

Two real indexes of the same notes differed by about a point of gold recall, so a difference under a point between two
settings is noise.

## Open, in the order I would take them

1. Read the first CI run and fix what fails. The likely spots are the Python 3.9 job, the viewer job's Playwright
   install and the store job's PostgreSQL service container.
2. Merge: review `production-readiness` and merge it into the default branch; consider renaming that branch to `main`
   and tagging a release.
3. Confirm or change the licence.
4. Re-run the agent eval of RESULTS phase G on the shipped code with the walk on: the 1,677-note cell first, then the
   30-note and 168,141-note cells and a "memory + digest" cell. This needs model spend; the README marks the cells it
   would replace.
5. Run the Neo4j backend and the export's import against a Neo4j 5 server; record the result in ADR-001 item 5.
6. Four of the eight thing types the review admitted on the bank are note kinds (experiment, decision, finding,
   question): the dreamer names notes as things. Add note kinds to the `drop:` line of the TYPES seed, rebuild the
   bank-index world and re-run its gate.
7. Indexing throughput: a wave of `-j` calls waits for its slowest call, so the pool was about a third busy at `-j 8`.
   Feeding the pool continuously within a project would keep the cached prefix and remove the barrier.
8. `memory.py check | head` should exit quietly on a closed pipe.
9. BUILD-GUIDE §8 "Results to expect" still shows round-4 numbers; refresh it, then the bundle.
10. The bank-index registries carry types on probation dated 2026-11-02. From 2027-01-01 a dream may demote some of
    them (0 calls), which can move the gated numbers a little; the floors have margin.

## Environment notes

- The session ran in an ephemeral cloud container: Python 3.13, Node 22, the Claude Code CLI 2.1.316, GNU grep.
  PostgreSQL 16 was installed with apt for the parity test and went with the container, as did the driver's venv.
- `tests/haiku_cmd.py` worked through the CLI: about $0.0016 per call with the cached prefix; `-j 16` indexed about 48
  notes a minute.
- Measurement knobs: `MEMORY_RELATION_LINES`, `MEMORY_RELATION_HOPS`, `MEMORY_RELATION_MODE`, `MEMORY_NO_INDEX=1`,
  `MEMORY_WIDE=100` (big-memory routing on a small memory), `MEMORY_DEBUG=1` (the ranking and the walk on stderr).

## Picking it up

```bash
git fetch origin production-readiness && git switch production-readiness
python3 tests/acceptance.py
python3 tests/retrieval_gate.py bank && python3 tests/retrieval_gate.py software && python3 tests/retrieval_gate.py bank-index

# the PostgreSQL store, given a server and the driver
pip install "psycopg[binary]==3.2.9"
MEMORY_STORE_URL=postgresql://user:pw@host:5432/db python3 tests/store_parity.py postgres --bank

# any knob, A/B on the real index with no model call
python3 eval/bank/assemble.py eval/bank/generated tests/fixture/memory /tmp/w/memory
python3 eval/real/bank-index/restore.py /tmp/w/memory
python3 skills/memory-dream/scripts/memory.py --root /tmp/w/memory dream
python3 eval/ab_env.py /tmp/w/memory eval/questions/bank-*.jsonl --var "off:MEMORY_RELATION_LINES=0" --var "default:" \
  --index-world /tmp/w/memory
```

## Picked up on 2026-11-11

Everything above is the 2026-11-02 session's record, left as written. A second session took the work over on another
machine: macOS, Python 3.9.6 and 3.13, BSD grep, Node 22 with Playwright; no PostgreSQL, Docker installed with its
daemon off. The work is on the same branch, one commit on a4d53c0.

### What the pick-up found

| check | on this machine, before any change |
|---|---|
| acceptance | 38/38 on Python 3.9.6 in 14 s: the first run on 3.9 outside CI |
| retrieval, bank, no index | as above: gold 0.939 · numbers 0.979 · stale 0.962 / 1.0 · absence 1.0 |
| retrieval, software fixture | as above |
| retrieval, bank, real index | gold 0.941 · numbers 0.978 · alias **0.818**, where the table above has 0.821; 0.816 on the next run |
| viewer, headless | 15/15 (`NODE_PATH="$(npm root -g)"` finds a global Playwright) |
| CI | had run four times; the last run, on a4d53c0, green on all six jobs. The one red run (5a28021) was the bundle check |
| PostgreSQL store | not run here: no server. CI ran it green |

The alias figure was the thread to pull. `ask` did not print the same answer every time: it depended on Python's hash
seed, on the order grep listed the files in, and for tasks on the other questions of the call. RESULTS phase J has the
measurement and the three fixes; `eval/stability.py` measures it and A42 holds it. No gated number moved.

### The open list, as it stands

| item above | now |
|---|---|
| 1. read the first CI run | done: green at a4d53c0 |
| 2. merge, rename the default branch, tag | open: the owner's call. Still no pull request |
| 3. the licence | open: the owner's call |
| 4. agent eval on the shipped code | open: needs model spend |
| 5. Neo4j backend and the export's import | open: no Neo4j here either |
| 6. note kinds named as thing types | open. It re-bases every with-index number and the README's dedup counts, so it wants its own commit |
| 7. indexing throughput | open: proving it needs model calls |
| 8. `check \| head` | done: exit 0, nothing on stderr (A43) |
| 9. BUILD-GUIDE §8 | done; the bundle's own stale exit conditions too (`35/35 passed`, "~1,900 lines") |
| 10. probation dates | unchanged |
| new | the lines printed under a note still depend on the other questions of the call (RESULTS J3) |

### Verified at the end of this session

| check | result |
|---|---|
| `python3 tests/acceptance.py` | 40/40 on Python 3.9.6 and on 3.13 |
| `python3 tests/retrieval_gate.py bank` | gold 0.939 · numbers 0.979 · stale 0.962 / 1.0 · absence 1.0 |
| `python3 tests/retrieval_gate.py software` | gold 1.00 · numbers 1.00 · stale 1.0 / 1.0 |
| `python3 tests/retrieval_gate.py bank-index` | gold 0.941 · numbers 0.978 · alias 0.818 |
| `python3 eval/stability.py <bank-index world>` | 0 differences in 1,149 questions; the same with `MEMORY_WIDE=100` |
| `node tests/viz_check.js` | 15/15 |
| `python3 tests/bundle_refresh.py --check` | fresh |

On this machine the old local worktree `.claude/worktrees/build-v0.4` is still at 904fe5e, 36 commits behind, and holds
uncommitted outputs of a taste agent run from 2026-10-31 (`eval/taste/collect.py`, `harness.json`, four judge files,
`runs/`, `usage-T.jsonl`, and small fixes to `eval/a21/extract.py` and `eval/taste/summarize.py`). None of it is in
any commit. It was left untouched.
