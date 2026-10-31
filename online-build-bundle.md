# memory-dream — online build bundle

A handoff file for agents. It splits rebuilding the memory-dream skill into phases. Each phase lists an owner,
its inputs, the work, what it hands off, and **exit conditions**: commands that must pass before the next phase
starts. An orchestrator agent reads this file once, then sends each phase to a worker agent with the
**phase brief** (§3) filled in.

Repository: `https://github.com/Zehaoyu217/memory-dream`, branch `worktree-build-v0.4`. All paths are relative to
its root. Detailed references, for when a phase needs more than this file gives:

| file | holds |
|---|---|
| `BUILD-GUIDE.md` | design, algorithm per module, eval recipes, expected numbers, pitfalls |
| `.specs/memory-dream/build-spec.md` | the v0.4 spec (§13 = acceptance table A1–A21) |
| `.specs/memory-dream/RUNBOOK.md` | operator commands |
| `.specs/memory-dream/RESULTS.md` | measured results, rounds 1–4, deviations from the spec |
| `skills/memory-dream/` | the reference implementation (the oracle for Mode B) |

---

## 0. Pick a mode

| mode | goal | what the agents do | cost |
|---|---|---|---|
| **R — reproduce** | confirm the shipped skill works and its numbers hold | run P0, P9, P10 (whichever eval tiers you choose) and P11 against the code as it is | P0+P9: $0, ~1 min. P10: see its tiers |
| **B — rebuild** | write the skill again, clean-room, and confirm it matches | run P0 → P11 in order. The reference code is kept aside as an oracle and is never copied | ~1,900 lines of Python + 600 lines of HTML; the tests cost $0 |

Mode B setup (P0 does this): on a new branch, move the reference to `reference/skills/memory-dream/`, which agents
may **read for behaviour, not copy**. Leave `tests/` and `eval/` where they are: they are the contract.
`tests/acceptance.py` loads `skills/memory-dream/scripts/memory.py` (hard-coded), and `eval/retrieval.py` takes
`$MEM_PY`.

---

## 1. Ground rules (apply to every phase)

1. **Stdlib only.** Python ≥ 3.9 (`sqlite3`, `json`, `re`, `subprocess`, `difflib`, `hashlib`, `argparse`). No pip.
2. **Notes are the truth.** Everything under `memory/_dream/` can be thrown away and rebuilt. `EDGES.md` and
   `ALIASES.md` belong to the user: append to them, never rewrite them.
3. **A thin layer on grep.** The tool helps an agent's grep and Read; it never replaces them. Any change to
   retrieval is measured against a grep-only agent on the same questions.
4. **Deterministic tests use the fake dreamer** (`tests/fake_dreamer.py`). Real model calls happen only in P9b
   and P10, and only when the orchestrator allows it.
5. **Never quote prices from memory.** Costs come from `DREAM_COST_LOG` (`tests/haiku_cmd.py`) or from harness
   usage.
6. **Do not edit the contract files** (`tests/acceptance.py`, `tests/fixture/`, `tests/fake_dreamer.py`,
   `tests/truth.py`, `eval/questions/`, `eval/bank/generated/`) to make a test pass. If a test looks wrong,
   stop and report it in the handoff packet.
7. Commit at the end of each phase with the message `P<n>: <summary>`. Push only when the orchestrator says so.

---

## 2. Shared contracts (every phase builds against these)

### 2.1 Layout

```
skills/memory-dream/
  SKILL.md                    ≤ ~45 lines, frontmatter name + description (one-call ask policy)
  scripts/memory.py           one file: dream · ask · viz · check · log
  assets/viz.html             self-contained viewer template (no CDN)
  agents/memory-dreamer.md    Haiku subagent for file mode (Read, Write, Glob; reads pending/TODO.md)
memory/                       (in a user project)
  <area>/<slug>.md            notes; filename = id; area = project or a general area
  log/YYYY-MM-DD.md           scratch lines (memory.py log)
  EDGES.md  ALIASES.md        user-owned vocabularies (seeded by the first dream)
  _dream/                     generated: manifest.json, store.db, index.db, notes/<sha12>.json,
                              graph.json + graph.html (≤ MEMORY_WIDE notes) or graph.html overview +
                              viz/<area>.html + viz/_sig.json (> MEMORY_WIDE), pending/ (file mode)
```

General areas: `prefs reporting glossary corrections howto qa people log`.

### 2.2 Note format

```markdown
---
from: [exp-014, leak-hypothesis]
supersedes: [churn-xgb-v2]
type: model            # optional; else the dreamer's kind
updated: 2026-10-30    # optional; else the log filename date, else mtime
---
# churn-xgb-v3 replaces v2: AUC 0.76, recall@10 0.43 on holdout-2025q4 (no leakage)
First paragraph = what is true now. Numbers carry metric, eval set, n, date. Sources in `backticks`.
```

Kinds: `question experiment finding decision dataset feature model metric term preference rule log note`.

### 2.3 CLI

```
memory.py [--root DIR] dream [--cmd CMD] [-j 4] [--review] [--all]
memory.py [--root DIR] ask "q1" "q2" … [-f FILE] [-p PROJECT] [--budget N]
memory.py [--root DIR] viz [--out FILE]
memory.py [--root DIR] check
memory.py [--root DIR] log "text" [-p PROJECT]
```

Root lookup: `--root`, then `$MEMORY_DIR`, then the nearest `memory/` upward from the cwd, then `./memory`.
Environment variables: `MEMORY_LLM` (model command, prompt on stdin; unset means file mode), `MEMORY_WIDE`
(10000), `MEMORY_TIMEOUT` (300), `MEMORY_DEBUG` (prints the ranking to stderr), `DREAM_COST_LOG`.

Constants: `KEEP_DAYS = 30`, `MIN_UNKNOWN_USES = 3`. Review caps: 40 types and 30 entity pairs per dream.
KNOWN = up to 80 entities from the note's project plus the 20 most-mentioned shared ones. Lookalike cutoff:
difflib ≥ 0.85, same type.

### 2.4 Warnings (`check`)

C1 ambiguous reference · C2 reference not found · C3 indexing failed (answer unusable twice) · C4 dropped an
ungrounded entity or relation · C5 note not indexed · C6 no `# ` line · C7 review pending (unknown types) ·
C8 unparseable line in EDGES.md or ALIASES.md.

### 2.5 Vocabulary

Eight closed relation types: `uses produces part-of trained-on evaluated-on measured-by replaces owned-by`.
Each has `aka:` aliases (`~` = read in reverse), plus a `drop:` list and `mode: closed`. Copy `EDGES_SEED`,
`EXTRACT` and `REVIEW` exactly from `skills/memory-dream/scripts/memory.py` lines 41–97 (in Mode B, from
`reference/`). These prompt texts are tuned and measured, so they count as contract, not code. The review may
answer only `alias T`, `alias ~T` or `drop` for a type, and `same` or `different` for a pair.

ALIASES.md lines: `- canonical = other-id …` (merge these) and `not: a / b` (never merge these).

---

## 3. Phase brief (the orchestrator fills this in for each worker)

```
You are building phase P<n> of memory-dream. Read online-build-bundle.md §1, §2 and §4.P<n>, and the
references listed there. Mode: <R|B>. Branch: <branch>. Model calls allowed: <none | Haiku up to $X>.
Previous handoff packets: <paste them>.
Do the work, run every exit condition, and reply with the handoff packet (§5). Do not start the next phase.
```

Phase order and what can run in parallel:

```
P0 ─► P1 ─► P2 ─► P3 ─► P4 ─► P5 ─► P6 ─► P7 ─► P9 ─► P10 ─► P11
                                   └──► P8 (viewer; needs P5's graph output) ──┘
```

P6 and P8 can run in parallel once P5 is done. P10's tiers are independent of each other.

---

## 4. Phases

### P0 — Bootstrap and baseline

- **Owner:** orchestrator or any agent. **Model calls:** none.
- **Do:** clone and check out `worktree-build-v0.4`, check `python3 --version` ≥ 3.9 and `grep` on PATH, and run
  the reference suite once to record the baseline. In Mode B, create the branch `rebuild/<date>` and move the
  reference: `git mv skills/memory-dream reference/skills/memory-dream`, then `mkdir -p skills/memory-dream/{scripts,assets,agents}`.
- **Exit conditions:**
  - [ ] `python3 tests/acceptance.py` on the untouched branch prints `21/21 passed`. Record the time; it is
        about 20 s.
  - [ ] Mode B: `test ! -e skills/memory-dream/scripts/memory.py && test -e reference/skills/memory-dream/scripts/memory.py`
  - [ ] Note whether `claude` (the Claude Code CLI) is on PATH. It is needed only for P9b and P10.

### P1 — Contract surface: SKILL.md, the dreamer agent, the CLI skeleton

- **References:** BUILD-GUIDE §5.1; build-spec §3, §7, §12; reference `SKILL.md` and `agents/memory-dreamer.md`.
- **Do:**
  - Write `SKILL.md`: frontmatter `name: memory-dream` and a description that tells the agent to make ONE
    `ask` call holding all its questions and tasks. Body sections: Read (one call, then answer; SUPERSEDED means
    history; scope with the project or id; ask with the task to get preferences), Write (the rules in §2.2, taste
    notes `prefs/<first>-<last>-<topic>.md` or `prefs/me-<topic>.md`), End of session (`dream`, `check`, EDGES and
    ALIASES edits).
  - Write `agents/memory-dreamer.md`: `model: haiku`. It reads `memory/_dream/pending/TODO.md`, answers every
    listed `*.prompt.md` that has no `.json` yet, and touches nothing else.
  - Write the `memory.py` skeleton: argparse with the five subcommands, root lookup (§2.3), the `log` command
    (appends `- HH:MM [project] text` to `log/YYYY-MM-DD.md`), and the constants and prompt texts from §2.5.
- **Exit conditions:**
  - [ ] `python3 skills/memory-dream/scripts/memory.py --help` lists dream, ask, viz, check and log.
  - [ ] `wc -l skills/memory-dream/SKILL.md` ≤ 45, and its frontmatter has `name` and `description`.
  - [ ] `memory.py --root /tmp/t/memory log "x" -p p1` creates today's log file. `MEMORY_DIR` and upward lookup
        both resolve, checked by hand from a subdirectory.

### P2 — Scan, manifest, note facts, store.db

- **References:** BUILD-GUIDE §5.2–5.3 and §5.8 (store.db); build-spec §5.3.
- **Do:** walk `memory/` with `os.walk`, skipping `_dream/`, dot directories and the files in `SKIP`. Keep the
  manifest `{path: {sha256, mtime_ns, size}}` and re-hash a file only when its mtime or size changed. Detect moves:
  a path that vanished while the same hash appeared at exactly one new path. Keep `former` paths. Parse each note
  for frontmatter, title and title line, `[[links]]` outside code, and body slugs
  (`(?<![\w/-])([a-z][a-z0-9]*(?:-[a-z0-9]+)+)(?![\w-])`). Cache the facts by path and hash in
  `_dream/store.db`.
- **Exit conditions:**
  - [ ] A first scan of `tests/fixture/memory` (copied to a scratch directory) finds 30 notes (25 notes and 5 log
        days).
  - [ ] A second scan re-reads 0 files. Shown with a debug counter or timing.
  - [ ] Moving 5 notes and renaming 2 with unchanged contents is reported as 7 moves.
  - [ ] Deleting `_dream/` and scanning again gives the same facts.

### P3 — Graph, note half: lineage, refs, warnings

- **References:** BUILD-GUIDE §5.4; build-spec §5.1 and §8.
- **Do:** build one record per note (path, id, project, title, line, kind, updated, superseded_by). Resolve
  `from` and `supersedes` in this order: relative path, exact path, unique filename, same-project filename (C1 when
  ambiguous), then moved paths. When nothing resolves, emit C2. Refs come from `[[links]]`, the dreamer's refs,
  and body slugs that name a note in the same project. Emit C1, C2, C5 and C6. `dream` with no model writes
  EDGES.md and ALIASES.md the first time it runs, plus `_dream/` outputs (C5 for every note).
- **Exit conditions:**
  - [ ] `python3 tests/acceptance.py A1 A2` passes. A2 reports 26 lineage edges and C5 = 30.
  - [ ] `python3 tests/acceptance.py A4` passes (moves, 0 calls, `from: exp-014` resolves). Needs P5's cache to
        report "0 calls". If P5 is not done yet, check the lineage half by hand and re-run A4 at P5 exit.

### P4 — Graph, vocabulary half: entities, relations, dedup

- **References:** BUILD-GUIDE §5.5; build-spec §4.6–4.7; RUNBOOK "Entities and the relation vocabulary".
- **Do:**
  - Fold ids: lowercase, and turn runs of space `_` `.` `-` into `-`.
  - Run union-find: ALIASES lines force merges; `not:` pairs and version pairs (ids that differ only in digits)
    never merge.
  - Apply the surface rule: when exactly one other entity writes this id as a surface form, and it has ≤ 3 users,
    merge them.
  - Keep an entity when it has a home note, is mentioned in ≥ 2 notes, or is named in ALIASES. Drop file-like ids.
  - Canonical id: the ALIASES lead, else the most-used raw id. Type by majority vote. The headline is the title of
    the best current note.
  - Map relations through EDGES (aliases, `~` reverse, drop). Anything unknown is counted and held back (C7) and
    goes to review once it has ≥ 3 uses. Evidence for each relation is `path:line`.
  - Review candidates: same type, a shared rare surface form, or difflib ≥ 0.85. Never queue a pair with two
    different home notes.
  - Hand edits to EDGES.md and ALIASES.md relabel at the next merge with 0 calls. Emit C8 for unparseable lines.
- **Exit conditions** (with the fake dreamer from P5, or with extraction JSONs loaded directly):
  - [ ] `python3 tests/acceptance.py A11 A13 A14 A15 A16 A17 A18 A20` all pass.
  - [ ] `python3 tests/acceptance.py A19` passes: 1,000 notes, merge < 1 s, review candidates < 2 s.

### P5 — The dreamer: prompts, grounding, modes, review, cache

- **References:** BUILD-GUIDE §5.6; build-spec §4.1–4.4 and §4.8; RESULTS "Deviations" item 1 (TODO.md).
- **Do:**
  - Fill `EXTRACT` with the EDGES list, KNOWN (one sort per wave, `Known`), the path and the text.
  - Parse answers that are wrapped in prose or code fences. Retry an unusable answer once; after that, emit C3 and
    retry at the next dream.
  - Ground the output: keep an entity only if one of its `as` strings occurs in the note, and a relation only if
    its quote occurs. Count what is dropped as C4.
  - Command mode (`--cmd` or `$MEMORY_LLM`): run waves of `-j` parallel calls with the prompt on stdin.
  - File mode: write `_dream/pending/<id>.prompt.md` and `pending/TODO.md`, then ingest the `.json` answers on the
    next `dream`.
  - Review: send one `REVIEW` call when it is due, or when `--review` is passed. Append the answers to EDGES.md and
    ALIASES.md.
  - Cache: `_dream/notes/<sha12>.json` (the source), mirrored into store.db, kept `KEEP_DAYS` after last use.
    `--all` re-indexes everything.
  - Stop after the scan when nothing is new. Write `index.db` every time. The summary line reads
    `dream: N notes · K indexed (C calls) · … · P pending`.
- **Exit conditions:**
  - [ ] `python3 tests/acceptance.py A3 A5 A6 A7 A8 A9 A10 A12` all pass.
  - [ ] Re-run A4, which now passes with 0 calls.
  - [ ] Run `dream` twice in a row on the indexed fixture. The second prints `0 indexed (0 calls)` and
        `nothing new`.

### P6 — Answering: `ask`

- **References:** BUILD-GUIDE §5.7 (steps 1–9); RESULTS round 2 ("What changed") and round 4 (taste).
- **Do:**
  - Build terms: ids and numbers whole (weight 3 / 1.5), stemmed words, word pairs (1.5), small synonym table
    `SYN`, stop words removed.
  - Detect intent (current, down, up, why, dep, task).
  - Expand names conservatively: only ids the question names (≤ 2 entities per name) and 2–3-word entity names
    spelled out in full.
  - Scope by a folder name in the question or by `-p`.
  - Run one `grep -rniIF` per group of questions that share areas, with a Python fallback when grep is missing.
    Keep a hit only where a pattern starts a word.
  - Rank by idf (title lines count ×2), then named notes, then entity boosts inside the scope only, then lineage
    (successor of a superseded note, children for "what came of", parents two hops back for why). Return ≤ 8
    notes that score ≥ 20% of the best.
  - Print `▸ path · kind · date · from … · SUPERSEDED → newer` and the best 2–4 lines under it. Print whole
    notes when everything fits the budget (900 chars per question + 1,500).
  - Taste block, for task intent only: six notes from the general areas. A named person brings all of their
    notes, plus the house rules for the artifact asked for, plus `prefs/me-*`.
  - `ask` must work with no index at all (grep plus lineage).
- **Exit conditions:**
  - [ ] `memory.py --root tests/fixture/memory ask "what came of exp-014?" "who owns cards.txn_daily?"` gives one
        output with a block per question. The exp-014 block reaches churn-xgb-v3 and shows v2 as SUPERSEDED.
  - [ ] A2's ask check passes (ask answers from lineage + grep with no model).
  - [ ] **Retrieval gate** (needs the P10 tier-1 world, no LLM): `python3 eval/retrieval.py <W>/memory eval/questions/bank-*.jsonl`
        gives gold-note recall ≥ 0.86 and number recall ≥ 0.95. The reference measured 0.882 / 0.970.

### P7 — Big memories: index.db, routing, patching, viewer split

- **References:** BUILD-GUIDE §5.8; RESULTS round 4 ("What broke at 100×, and the fix").
- **Do:**
  - Write `index.db` (notes, edges, ents, ment, names, rels, checks). `ask` reads it through a `DbView` that loads
    note rows and reads everything else per question.
  - Patch on read: notes that changed since the dream are re-read from their text, with lineage updated now and
    entities at the next dream.
  - Past `MEMORY_WIDE` notes, `ask` routes each question to the area it names. Otherwise it uses areas that match
    the note ids and titles (idf-weighted, ≤ 8), areas the index links to the question's ids, the areas of named
    notes, and the general areas. A global grep is allowed only for ids nothing else places.
  - Past `MEMORY_WIDE`: no graph.json. graph.html becomes an overview, plus `viz/<area>.html` pages redrawn only
    when `viz/_sig.json` changes (area notes, lineage, entity ids, relations; not the vocabulary spellings).
  - After a review, rebuild only the vocabulary half (`notes_part` reuse).
- **Exit conditions:**
  - [ ] `python3 tests/acceptance.py A24` passes: scoped ask, a general question routes to prefs, patch without
        rebuild, 4 area pages, one edit redraws only `['prefs']`.
  - [ ] `MEMORY_WIDE=100 python3 eval/retrieval.py <W>/memory eval/questions/bank-*.jsonl` gives ≥ 0.86 / ≥ 0.95.
        The reference measured 0.877 / 0.960.

### P8 — Viewer (`assets/viz.html`, `render_viz`)

- **References:** BUILD-GUIDE §5.9; RESULTS round 2 "Viewer".
- **Do:** write one self-contained HTML file with no external requests. Data lives in
  `<script type="application/json" id="data-graph">` and components talk through `dp:` events. Tabs: Map,
  Overview, Explore and Health. Deep links: `#note=<path>`, `#entity=<id>`, `#health`. Three modes: normal,
  `overview`, `area`. Theme tokens with dark mode, a 16px phone gutter and no horizontal scroll.
- **Exit conditions:**
  - [ ] `memory.py --root <indexed fixture> viz --out /tmp/g.html` writes the file, and
        `grep -c 'https\?://' /tmp/g.html` finds no script or stylesheet URLs.
  - [ ] Headless Chromium (Playwright; skip if not installed) loads `/tmp/g.html#note=churn-2026/exp-014.md` and
        `#health` with no console errors.
  - [ ] A24's big-memory page checks pass. These are shared with P7.

### P9 — Integration

- **P9a, deterministic (required):**
  - [ ] `python3 tests/acceptance.py` prints `21/21 passed` in under 60 s.
  - [ ] Mode B: `wc -l skills/memory-dream/scripts/memory.py` is within ±30% of the reference's ~1,900 lines. Report
        the number; it does not gate.
  - [ ] Mode B: `diff <(sed -n '/^EDGES_SEED/,/^"""$/p' reference/…/memory.py) <(… new …)` is empty, and the same
        holds for `EXTRACT` and `REVIEW`.
- **P9b, real model (optional; needs `claude` and a budget of about $0.10):**
  - [ ] `python3 tests/real_model.py a3 <scratch>/w-a3`: every note is indexed once, and a second dream makes 0
        calls.
  - [ ] File mode: `python3 tests/real_model.py a10-prep <scratch>/w-a10`, then run the `memory-dreamer`
        subagent, then `a10-next`, repeating until `dream` reports 0 pending (normally 2 rounds).
  - [ ] The per-note cost in `DREAM_COST_LOG` is ≤ $0.003. The reference measured $0.0013–0.0020.

### P10 — Evaluations (each tier is optional and runs on its own)

The orchestrator picks tiers by budget. `<W>` = 1,677-note world, `<X>` = 100× world. The commands are in
BUILD-GUIDE §7; only the gates are repeated here.

| tier | build | gate (exit condition) | cost |
|---|---|---|---|
| 1. 56× world | `eval/bank/assemble.py eval/bank/generated tests/fixture/memory <W>/memory`, then a Haiku `dream -j 10` with `tests/haiku_cmd.py` | 1,677 notes indexed, 0 C3; cost per note ≤ $0.003 | ~$3.3, ~25 min |
| 1-free | the same world, indexed with `MEMORY_LLM="python3 $PWD/tests/fake_dreamer.py" memory.py --root <W>/memory dream -j 10` | `1677 indexed`, `0 pending`. Enough for the P6 and P7 retrieval gates. Measured on the reference: 0.888 / 0.969, routed 0.885 / 0.958 | $0, ~20 s |
| 2. offline retrieval | `eval/retrieval.py`, both normal and `MEMORY_WIDE=100` | ≥ 0.86 gold / ≥ 0.95 numbers | $0 |
| 3. agent eval | `eval/agent/make_batches.py`, then Opus subagents per batch on the memory arm and the grep arm (prompt in BUILD-GUIDE §7.3), then `a21/extract.py`, `judge.py`, `agent/summarize.py` | memory accuracy ≥ grep accuracy minus 1 correct per 10 questions, **and** memory cost ≤ 0.6× grep at 1,677 notes (reference: 0.47×) | Opus tokens; 2 arms × 3 batches |
| 4. 100× | `eval/scale/make_world.py <W>/memory <X>/memory --copies 137`, `bootstrap.py`, `time_ask.py`, `profile_incremental.py` | `ask` on 10 questions < 5 s (ref 2.3 s); a dream with nothing new < 10 s (ref 3 s); retrieval ≥ 0.83 / ≥ 0.93 | ~20 GB disk, ~5 GB RAM; Haiku about $0.06 for 30 notes |
| 5. taste | `eval/taste/score.py <W>/memory eval/taste/tasks.jsonl` (fixed tasks), optionally the T1/T2 agent runs and `taste/judge.py` | named-person preference recall ≥ 0.85 (ref 0.93); house rules ≥ 0.35 (ref 0.42) | $0 for the scorer |

Every tier reports its numbers in the same rows as BUILD-GUIDE §8, so they can be compared side by side.

### P11 — Package, install check and docs

- **Do:** follow BUILD-GUIDE §2 to install the skill and agent into a scratch `HOME`, with
  `cp -R skills/memory-dream ~/.claude/skills/` and the agent file into `~/.claude/agents/`. Make a fresh project
  with an empty `memory/`, then run `dream`, write two notes, `ask`, and `check`. Update `README.md` and
  `RESULTS.md` (a new round section) with what P9 and P10 measured. In Mode B, delete `reference/` in the last
  commit.
- **Exit conditions:**
  - [ ] The installed copy works from a directory outside the repository (upward root lookup).
  - [ ] `git status` is clean, and every phase commit is present (`git log --oneline | grep -c '^.\{8\} P[0-9]'`).
  - [ ] The final handoff packet lists every exit condition from P0 to P11 with pass, fail or skipped. A skipped
        condition needs its reason.

---

## 5. Handoff packet (each worker replies with exactly this)

```markdown
## P<n> handoff — <pass | fail | blocked>
- commit: <sha> on <branch>
- exit conditions:
  - [x] <condition> — <evidence: command + the line of output that shows it>
  - [ ] <condition> — <why it failed or was skipped>
- measured: <numbers, with units and source (DREAM_COST_LOG, harness usage, timing)>
- deviations from the bundle or the reference: <what and why, or "none">
- open problems for the next phase: <list, or "none">
- files touched: <paths>
```

The orchestrator moves to the next phase only on `pass`. On `fail`, it sends the packet back to the same worker,
or to a fresh worker given the packet, at most twice. After that, it stops and reports to the user. On `blocked`
(for example, a contract file looks wrong or the budget is exhausted), it reports to the user straight away.

---

## 6. Definition of done

- Mode R: P0 and P9a pass, the chosen P10 tiers meet their gates, and P11's packet is written.
- Mode B: everything above holds, plus every P1–P8 exit condition passes, the prompt texts match, and
  `reference/` is removed.
- In both modes: nothing under `tests/` or `eval/questions/` was changed. If a measured number misses its gate, it
  is reported rather than hidden (ground rule 6).

---

## 7. Known traps (read before P5–P7)

| trap | fix the reference uses |
|---|---|
| the dreamer subagent cannot list files (no Glob in some CLIs) | `pending/TODO.md` lists the prompts |
| loose Haiku names hurt retrieval | expand only ids the question names and 2–3-word names spelled out |
| an open relation vocabulary grew to 508 types | closed 8 types; the review may only alias or drop, and is told "when unsure, drop" |
| multi-call answering cost 2.3× grep | one `ask` call for every question; print lines, not whole notes |
| one global grep took 52–135 s at 168k notes | route to areas past `MEMORY_WIDE` |
| entity boosts let copies crowd out the gold note | boosts apply only inside the scope or the routed areas |
| a full dream took 202 s and 8.2 GB, with 380 MB of JSON | store.db + index.db, area pages, stop when nothing is new |
| a review redrew every area page | the page fingerprint excludes vocabulary spellings |
| building the KNOWN prompt took days at 168k | one entity sort per wave |
| the dreamer loaded the user's CLAUDE.md, hooks and MCP | `claude -p --model haiku --tools "" --setting-sources "" --strict-mcp-config --no-session-persistence` |
