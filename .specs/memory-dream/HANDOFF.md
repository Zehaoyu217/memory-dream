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
daemon off. The work is on the same branch, on top of a4d53c0.

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
seed, on the order grep listed the files in, and for tasks on the other questions of the call. With those three fixed
the next CI run still read 0.819 on Linux against 0.818 here, which led to two more: a thing's headline note went to
whichever tied file was modified last (a clone keeps no modification times), and on a machine with no grep the
registries were answered as notes. RESULTS phase J has the measurements and the five fixes; `eval/stability.py`
measures the read path and A42 holds all five. Of the gated numbers two moved: alias, 0.821 here and on Linux now,
and characters per question, up by one.

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
| new | a note with no date of its own is dated by its file, so by the day of the clone (RESULTS J3; README Limits) |
| new | BSD grep took twice as long as the Python matcher on this Mac (49 s against 22 s for 1,149 questions): not looked into |

What comes next was first drafted as `PLAN.md` at commit e78eb8f (v0.5, eleven blocks, six milestones) with its
materials in `RESEARCH-2026-11.md`. That draft was grilled and rewritten the same day: see "The plan, second draft"
at the end of this file.

### Verified at the end of this session

| check | result |
|---|---|
| `python3 tests/acceptance.py` | 40/40 on Python 3.9.6 and on 3.13 |
| `python3 tests/retrieval_gate.py bank` | gold 0.939 · numbers 0.979 · stale 0.962 / 1.0 · absence 1.0 |
| `python3 tests/retrieval_gate.py software` | gold 1.00 · numbers 1.00 · stale 1.0 / 1.0 |
| `python3 tests/retrieval_gate.py bank-index` | gold 0.941 · numbers 0.978 · alias 0.821 |
| `python3 eval/stability.py <bank-index world>` | 0 differences in 1,149 questions, seven variants; the same with `MEMORY_WIDE=100` |
| `node tests/viz_check.js` | 15/15 |
| `python3 tests/bundle_refresh.py --check` | fresh |
| CI on d725562 (Linux, GNU grep, Python 3.9 and 3.13) | green on all six jobs; 40/40 twice; store parity 11/11; every gate line the same as this machine's, digit for digit, alias 0.821 included |

On this machine the old local worktree `.claude/worktrees/build-v0.4` is still at 904fe5e, 36 commits behind. It held
uncommitted outputs of a taste agent run from 2026-10-31 (`eval/taste/collect.py`, `harness.json`, four judge files,
`runs/`, `usage-T.jsonl`, and small fixes to `eval/a21/extract.py` and `eval/taste/summarize.py`). They are committed
on this branch now (RESULTS J5), so that worktree holds nothing that exists nowhere else and can be removed.

### The plan, grilled (2026-11-11, later the same day)

The owner answered the first draft with ten points and then six more (`PLAN.md` §1): an open contract, a base that
an agent sets up, a drop that reaches what came from a note, absorbing other knowledge bases, retrieval first,
nothing over-engineered; then the work on Haiku 5.5 under the 100K-token line with the claims base's reading
method, pointers into code, a note being whatever an agent wrote, dedup by agents and no fuzzy matching, and the
bar of an Opus agent with grep. The draft was grilled against those points and the code that ships (rev 2),
attacked by an independent reviewer, and rewritten again (rev 3). No shipped code changed.

| file | what it is now |
|---|---|
| `PLAN.md` | rev 3: what the measurements say, how it works, who does the work on which model, three steps |
| `CONTRACT-2.md` | the draft of schema 2 that goes with it |
| `eval/contract_probe.py`, `eval/absorb/policy-kb/` | drop, copy-in, absorb, documents, sets: under a minute, no model |
| `eval/agent/arms.py`, `runs/H-*.md`, `usage-H.jsonl`, `judge-H.json`, `make_haiku_arm.py`, `askfull.py` | five arms on thirty questions: Opus and Haiku, memory and grep, every answer graded twice |
| `eval/pointer_probe.py` | how long a pointer into code stays right, from git |
| `eval/decompose_probe.py`, `eval/real/handoff-claims/` | a handoff decomposed by Haiku 5.5 and gated in code |
| `RESULTS.md` phase K | all of the above |
| `README.md` Results and Limits | the re-grading of phase G's tie; a deleted note cuts its chain and crashes `ask` on a big memory; a list question gets part of its set; `ask`'s silence taken for absence |

Where it stands: waiting for the owner's answers in `PLAN.md` §15. Step 0 is two defects of v0.4 (the crash and
the cut chain) and step 1 needs no model.

Spent on models in this pass: nine Haiku 5.5 subagents for the arms, one for the decomposition, thirty judge calls
and one long independent review. No Opus arm was run.

The loose ends the first draft had folded in stay open here: items 6 (note kinds named as thing types) and 7 (the
pool of calls fed continuously) fit step 2, when the bank is read again anyway; the three "new" rows of the table
above (lines under a note depending on the other questions of the call, a note dated by its file, BSD grep slower
than the Python matcher) are small fixes of their own.

### Why the memory was graded below grep (2026-11-11, phase L)

The owner took every recommendation of `PLAN.md` §15 and asked one thing first: the memory should be the more
accurate arm at a fraction of the price, so why is it graded below grep? His guess was the retrieval and how it
decides when to stop, and questions too easy to need linkage. RESULTS phase L is the answer. In short:

- The one call the skill asks for showed all the evidence for 23 of the thirty questions. The seven it failed are
  one batch about a project no question names: `ask` printed 25,000 characters of look-alike projects, the folder is
  8,600, and the agent made that one call and answered.
- `ask` changed (133 lines): a small folder printed whole when a call points at it, the whole chain of a named note,
  `ask --list` as the map of a folder or a kind, a line that says when a section is not the whole folder, and a
  note's kind from its name before the dreamer's reading.
- Haiku with the memory now answers 30 of 30 linkage questions inside a project and 7 of 7 across the memory
  exactly, as Opus and Haiku with grep do, 35 and 46 times cheaper than Opus with grep; on the thirty it is graded
  25 where Haiku with grep gets 25 or 26 and Opus with grep 29.
- It ties grep and does not beat it. On the bank grep is exact, so nothing here can show a memory being more
  accurate. That needs a base grep cannot read whole.

| file | what it is now |
|---|---|
| `skills/memory-dream/scripts/memory.py`, `SKILL.md` | the changed `ask` and the lines that tell an agent how to read it |
| `eval/agent/why.py` | question by question: what one call showed against the reference, beside the verdicts |
| `eval/linkage.py`, `eval/questions/linkage-bank.jsonl`, `linkage-global.jsonl` | 30 + 7 questions whose answer is a set of notes, made from the lineage and scored exactly |
| `eval/agent/make_linkage_arm.py`, `persist.py`, `arms.py` | prompts for those sets; filing a subagent's run; every arm side by side, three tables |
| `eval/agent/runs/`, `usage-*.jsonl`, `judge-H.json`, `harness.json` | 36 new runs: the experiments of L2, the linkage and whole-memory arms, three rounds of the changed memory |
| `eval/agent/askarea.py` | the experiment that printed a folder whole before `ask` did |
| `eval/real/bank-index/KINDS.md` | `inc` off the incident line: it is that bank's code for a project |
| `tests/retrieval_gate.py`, `eval/retrieval.py`, `eval/stability.py` | the gold floor at 0.96; a folder printed whole counted for the questions that point at it |

How an arm is run, since no script can start a subagent: `make_haiku_arm.py` or `make_linkage_arm.py` writes a
workspace and one prompt file a batch; one subagent a batch on the model of the arm is told to read its prompt file
and reply in its format; `persist.py` takes the transcript and the harness's three numbers and files the run;
`arms.py` prints the tables. A subagent of the harness carries about 35,000 tokens of its own in every request.

Verified at the end: `tests/acceptance.py` 40 of 40; the three retrieval gates (bank 0.978 gold, 0.978 numbers,
2,954 characters; bank-index 0.973, 0.978, 3,138, alias 0.811; software 1.0, 1.0); `eval/stability.py` all zeros;
`tests/bundle_refresh.py --check` fresh; `persist.py` writes the 36 runs again to the same bytes.

Open, in the order I would take them:

1. Step 0 of the plan: done the same day, RESULTS phase M. `memory.py drop <note | folder> [--yes]` writes a
   `dropped:` line in CONFLICTS.md that the build reads as a pass-through; a file deleted by hand is reported (C15)
   and nothing is written for it; `ask` survives a missing file on both read paths. `tests/e2e.py` is new and in CI.
2. Step 1, item 1: done the same day, RESULTS phase N. A top folder with an `ORIGIN.md` is another base's notes;
   `memory.py absorb <folder> --as <name> [--trust preferences] [--yes]` takes one in with its readings or its
   `relations.jsonl`. It stays apart: 0 of the host's 326 answers change, its notes follow in a block of their own,
   its things are `<name>:<id>` until a line of ALIASES.md joins them. `eval/origin_probe.py` is new.
   Item 3, pointers into code, is done too (RESULTS phase O, 2026-11-12): `path#symbol`, `path:line "words"` and
   `path:line` are looked up at every dream and every `ask`, a note whose pointer no longer holds is marked STALE
   (C16), and `eval/pointer_probe.py --built` scores the lookup on this repository's history: no wrong line in any
   form, after it found 12 of 209 symbols on a wrong line in the first build. The rule that a file is never a thing
   is the `drop-names:` line of TYPES.md now.
   Item 4, packets, is done (RESULTS phase P, 2026-11-12): `dream --packets` reads about 25 short notes a call, or
   leaves the packets in `_dream/pending/` for helper agents; `dream --dry-run` prints the calls, tokens and a cost
   and writes nothing; an answer on file is taken whether a command is set or not; `_dream/notes/` belongs in git.
   By the dry run the bank is 67 packets in place of 1,677 calls. One call a note is still the default: no model
   has read a packet yet.
   Item 5 is done (RESULTS phase Q, 2026-11-12): `tags:` in a note's frontmatter read through `memory/TAGS.md`
   (definition and spellings a line; an unlisted word is C17), `ask --list --tag`, and the words that make `ask`
   follow a link type as `walk:` and `hops:` fields of EDGES.md in place of three tables in the code.
   The rest of step 1: the setup section of the skill, the page's filters; each adds its lines to `tests/e2e.py`.
3. Small things this phase found and left: the own note of a thing when no folder wins the call (C-h1 Q6 is served
   only because its folder is printed whole); a check of each kind prefix against the readings at setup (`inc-`);
   `(weak match: … found nowhere in memory)` says "memory" when the search was scoped to one folder; "built directly
   on" is not read as a lineage question, only "built on"; the map of a whole kind is 38,000 characters and wants a
   cap or a narrower default before a prompt crosses 100K tokens.
4. Step 2's evaluation, designed from RESULTS L9: a base on which grep is not already exact, answers scored exactly
   where they can be, three runs a row, and the Opus arm with the memory run again on the changed `ask`.

Spent on models in this pass: four Opus 5.5 subagents, the grep arms of the two linkage sets, about $3.40 at list
prices; about forty Haiku 5.5 subagents, under $1; the judge's two passes over thirteen runs of ten answers.
