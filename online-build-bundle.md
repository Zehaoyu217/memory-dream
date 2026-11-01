# memory-dream — online build bundle

One markdown file that hands the whole skill to other agents: every phase, every spec, every exit condition.
Lines that read `<--->` mark where it may be split into separate files; each part stands on its own and starts
with its title. To split it, cut at every such line and name each piece after its first heading, for example
`csplit -z -f part- online-build-bundle.md '/^<--->$/' '{*}'` gives `part-00` … `part-08` (parts 1–9); keep
the pieces in one folder. Nothing in the text refers to a file name — cross-references use part numbers,
appendix letters and section numbers, so the pieces may be renamed freely. The body (parts 1–4) is written by hand; the appendices (parts 5–9) are verbatim copies of the
repository's own spec files, refreshed by `python3 tests/bundle_refresh.py` so they cannot drift. A phase brief
points at them as "Appendix B" (the graph contract), "Appendix C §n" (the build guide), "Appendix D" (prompts and
tuned tables), "Appendix A" (the skill text) and "Appendix E" (evaluation record formats).

| part | holds |
|---|---|
| 1 | this header, the two modes, the ground rules, the shared contracts (layout, note format, CLI, warnings, the graph contract, vocabulary and conflicts), the phase brief |
| 2 | phases P0–P5: bootstrap, the contract surface, scan and store, the graph's two halves, the dreamer |
| 3 | phases P6–P8: answering, big memories, the viewer's two plots |
| 4 | phases P9–P11, the handoff packet, the definition of done, known traps |
| 5 | Appendix A — `SKILL.md` and the dreamer agent, verbatim |
| 6 | Appendix B — the graph contract (`CONTRACT.md`), verbatim |
| 7 | Appendix C — the build guide §3–§10, verbatim: design, layout, every module's algorithm, tests, eval recipes, expected numbers, pitfalls, limits |
| 8 | Appendix D — the dreamer's prompts, the seed vocabulary and packs, the user-owned file headers, every tuned table |
| 9 | Appendix E — evaluation record formats |

Repository: `https://github.com/Zehaoyu217/memory-dream`, branch `worktree-build-v0.4`. All paths are relative to
its root. The reference implementation is `skills/memory-dream/` (the oracle for Mode B); measured evidence lives in
`.specs/memory-dream/RESULTS.md` and `REVIEW.md` (not needed to build; cited where a number is quoted).

---

_Part 1 of 9 · online-build-bundle.md_

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
  CONFLICTS.md                verdicts on pairs of live notes: `- a > b`, `compatible: a / b`, `- a ? b`
  DIGEST.md                   written by every dream, ≤ 40 lines; CLAUDE.md imports it with `@memory/DIGEST.md`
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
memory.py [--root DIR] dream [--cmd CMD] [-j 4] [--review] [--all] [--prompts]
memory.py [--root DIR] ask "q1" "q2" … [-f FILE] [-p PROJECT] [--budget N]
memory.py [--root DIR] viz [--out FILE]
memory.py [--root DIR] check
memory.py [--root DIR] log "text" [-p PROJECT]
```

Root lookup: `--root`, then `$MEMORY_DIR`, then the nearest `memory/` upward from the cwd, then `./memory`.
Environment variables: `MEMORY_LLM` (model command, prompt on stdin; unset means file mode), `MEMORY_WIDE`
(10000), `MEMORY_TIMEOUT` (300), `MEMORY_DEBUG` (prints the ranking to stderr), `DREAM_COST_LOG`, `MEMORY_CC_DIR`
(Claude Code's auto-memory directory to read; default resolved from settings and `<config>/projects/`),
`MEMORY_SOURCES=notes` (read no Claude Code memory). `dream`, `log` and `viz` without `--out` refuse a root that is
Claude Code's own memory (holds `MEMORY.md`, or lies under `<config>/projects/*/memory`): exit 2.

Kinds without a model (`kind_of`): frontmatter `type:` (Claude Code's user/feedback/project/reference →
preference/rule/note/note), else the dreamer's kind unless "note", else the filename prefix (`exp- feat- ds- dec- fnd-
find- q- metric-`; `…-vN` = model), else the area (`prefs/ glossary/ corrections/ reporting/ howto/ log/`), else
`note`. `modified:` is the date when `updated:` is absent.

Constants: `KEEP_DAYS = 30`, `MIN_UNKNOWN_USES = 3`. Review caps: 40 types and 30 entity pairs per dream.
KNOWN = up to 80 entities from the note's project plus the 20 most-mentioned shared ones. Lookalike cutoff:
difflib ≥ 0.85, same type.

### 2.4 Warnings (`check`)

C1 ambiguous reference · C2 reference not found · C3 indexing failed (answer unusable twice) · C4 dropped an
ungrounded entity or relation · C5 note not indexed · C6 no `# ` line · C7 review pending (unknown types) ·
C8 unparseable line in EDGES.md, ALIASES.md or CONFLICTS.md · C9 NUL bytes in a note (binary-looking; `ask` greps it
with `-a`) · C10 conflict pending (two live notes of one kind in one area may disagree) · C11 a note over 40 lines.

### 2.4b The graph contract

Appendix B (`.specs/memory-dream/CONTRACT.md`, schema 1) is the authority on every shape: the graph (`graph.json`, `index.db`
meta and tables), the viewer's data island (graph + per-note `text`, `families` — the class tree — `mode`, and the
overview/area fields), the
extraction cache, `store.db`, the manifest, the warning codes and the user-owned files' grammar. Every graph carries
`schema`; `validate(g, types)` returns the violations; `memory.py check` prints `contract: schema 1 ok` first, then a
`lineage:` line (from/supersedes links per live project note, and the notes that link to nothing); A38
enforces it. Build P6–P8 against the contract, and bump `SCHEMA` when a field changes meaning.

### 2.5 Vocabulary (constrained open) and conflicts

Eight seed relation types: `uses produces part-of trained-on evaluated-on measured-by replaces owned-by`, each with
`aka:` aliases (`~` = read in reverse); `drop:` names only note-to-note links. Every extracted relation carries a
`type` (a type, an alias, or `other`) and a `label` (the note's own verb); a link that fits no type is kept as
`other/<label>`. EDGES.md settings: `promote: 5 uses, 5 notes, 2 areas` (a label is offered to the review only over
this bar), `budget: 24` (types), `probation: 60 days` (a `(proposed <date>)` type still under the bar is demoted to a
label), `pack: software | research | ops` (`PACKS`). The review answers `alias T`, `alias ~T`, `new: <definition>`,
`label` or `drop` for labels, `same` / `different` for entity pairs, and `<a> supersedes <b>` / `compatible` / `unsure`
for conflicts; the code admits `new` only within the budget and records conflict verdicts in `CONFLICTS.md`. Copy
`EDGES_SEED`, `PACKS`, `EXTRACT` and `REVIEW` exactly from `skills/memory-dream/scripts/memory.py` (in Mode B, from
`reference/`): these texts are tuned and measured, so they count as contract, not code.

ALIASES.md lines: `- canonical = other-id …` (merge these) and `not: a / b` (never merge these). CONFLICTS.md lines:
`- a > b` (a supersedes b, applied as lineage), `compatible: a / b`, `- a ? b` (unsure, for a person); paths relative
to the memory root.

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

<--->

_Part 2 of 9 · online-build-bundle.md — phases P0–P5_

## 4. Phases

### P0 — Bootstrap and baseline

- **Owner:** orchestrator or any agent. **Model calls:** none.
- **Do:** clone and check out `worktree-build-v0.4`, check `python3 --version` ≥ 3.9 and `grep` on PATH, and run
  the reference suite once to record the baseline. In Mode B, create the branch `rebuild/<date>` and move the
  reference: `git mv skills/memory-dream reference/skills/memory-dream`, then `mkdir -p skills/memory-dream/{scripts,assets,agents}`.
- **Exit conditions:**
  - [ ] `python3 tests/acceptance.py` on the untouched branch prints `35/35 passed`. Record the time; it is
        about 25 s.
  - [ ] Mode B: `test ! -e skills/memory-dream/scripts/memory.py && test -e reference/skills/memory-dream/scripts/memory.py`
  - [ ] Note whether `claude` (the Claude Code CLI) is on PATH. It is needed only for P9b and P10.

### P1 — Contract surface: SKILL.md, the dreamer agent, the CLI skeleton

- **References:** Appendix C §5.1; build-spec §3, §7, §12; reference `SKILL.md` and `agents/memory-dreamer.md`.
- **Do:**
  - Write `SKILL.md` for **any agent with a shell** (Claude Code, Claude through the API, other LLM agents, people),
    in plain dense language: frontmatter `name: memory-dream` and a description that tells the agent to make ONE
    `ask` call holding all its questions and tasks. Body: requirements (a shell, Python 3.9+, grep, no model needed),
    what the notes are, then "What an agent does with memory" in three numbered steps — read first, once (one call;
    SUPERSEDED is history; a task brings preferences; `(weak match …)`; one batched follow-up at most); write as you
    go (the rules in §2.2, prefixes give kinds, taste notes `prefs/<first>-<last>-<topic>.md` or `prefs/me-<topic>.md`);
    dream at the end (viewer, digest, index; a model is optional) — then one paragraph for Claude Code (CLAUDE.md
    holds instructions, auto memory holds learnings, these notes hold the work; `ask` reads auto memory and never
    writes it; `@memory/DIGEST.md`; never the same thing twice), then EDGES/ALIASES hand edits. ≤ 45 lines; keep the
    word count: achievement per word is a metric (RESULTS.md, "Phase B").
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

- **References:** Appendix C §5.2–5.3 and §5.8 (store.db); build-spec §5.3.
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

- **References:** Appendix C §5.4; build-spec §5.1 and §8.
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

- **References:** Appendix C §5.5; build-spec §4.6–4.7; RUNBOOK "Entities and the relation vocabulary".
- **Do:**
  - Fold ids: lowercase, and turn runs of space `_` `.` `-` into `-`.
  - Run union-find: ALIASES lines force merges; `not:` pairs and version pairs (ids that differ only in digits)
    never merge.
  - Apply the surface rule: when exactly one other entity writes this id as a surface form, and it has ≤ 3 users,
    merge them.
  - Keep an entity when it has a home note, is mentioned in ≥ 2 notes, or is named in ALIASES. Drop file-like ids.
  - Canonical id: the ALIASES lead, else the most-used raw id. Type by majority vote. The headline is the title of
    the best current note.
  - Map relations through EDGES (type first, then the label; aliases, `~` reverse, drop). A link that fits nothing
    is kept as `other/<label>` with evidence `path:line`; labels are counted by uses, notes and areas; those over the
    `promote` bar are offered to the review unless the budget is full (then C7 names them); the rest are summarised
    in one C7 line. Types marked `(proposed <date>)` still under the bar after the probation are listed for demotion.
  - Review candidates for entities: same type, a shared rare surface form, or difflib ≥ 0.85. Never queue a pair with
    two different home notes.
  - Conflict candidates: two live `…-vN` siblings in one area (`shared: ["version"]`), two live notes with the same
    title (`["same title"]`), or live notes of one kind (decision, model, finding) in one area, not linked, sharing an
    id-like title token or two rare title words; pairs decided in CONFLICTS.md are not offered again; `- a > b`
    lines become `supersedes` edges in the note half.
  - Hand edits to EDGES.md, ALIASES.md and CONFLICTS.md relabel at the next merge with 0 calls. Emit C8 for
    unparseable lines.
- **Exit conditions** (with the fake dreamer from P5, or with extraction JSONs loaded directly):
  - [ ] `python3 tests/acceptance.py A11 A13 A14 A15 A16 A17 A18 A20` all pass.
  - [ ] `python3 tests/acceptance.py A19` passes: 1,000 notes, merge < 1 s, review candidates < 2 s.
  - [ ] `python3 tests/acceptance.py A34 A35 A36 A37` passes once P5's review exists (promotion gate and packs,
        probation, budget, conflicts).

### P5 — The dreamer: prompts, grounding, modes, review, cache

Shape: a `Dream` class whose stages are methods — `plan`, `index`, `graph`, `demote`, `run_review`, `write`,
`report` — run under `_dream/lock` (a second dream exits 3; a lock older than 2 h is taken over). Tuned numbers of
the read path live in one `W` table with their provenance.

- **References:** Appendix C §5.6; build-spec §4.1–4.4 and §4.8; RESULTS "Deviations" item 1 (TODO.md).
- **Do:**
  - Fill `EXTRACT` with the EDGES list, KNOWN (one sort per wave, `Known`), the path and the text.
  - Parse answers that are wrapped in prose or code fences. Retry an unusable answer once; after that, emit C3 and
    retry at the next dream.
  - Ground the output: keep an entity only if one of its `as` strings occurs in the note, and a relation only if
    its quote occurs. Count what is dropped as C4.
  - Command mode (`--cmd` or `$MEMORY_LLM`): run waves of `-j` parallel calls with the prompt on stdin. Order the
    notes by project then date, refresh KNOWN only when the project changes (big memories: at most every 10 waves),
    so every call of a project shares one byte-identical prefix (template, EDGES, KNOWN); pass its length in
    `MEMORY_STATIC_PREFIX` so a cache-aware command (`tests/haiku_cmd.py`: `--append-system-prompt` for the prefix,
    the note as the message) lets the model cache it. Cap note text at 16k characters: every call stays small.
  - No model: write nothing for a helper (the memory is complete for answering; `check` summarises C5 in one line
    and the summary says "N without entities (no model; …)"). With `--prompts`: write `_dream/pending/<id>.prompt.md`
    and `pending/TODO.md` (and the review prompt when due), then ingest the `.json` answers on the next `dream`.
  - Review: send one `REVIEW` call when it is due, or when `--review` is passed. Append the answers to EDGES.md and
    ALIASES.md.
  - Cache: `_dream/notes/<sha12>.json` (the source), mirrored into store.db, kept `KEEP_DAYS` after last use.
    `--all` re-indexes everything.
  - Stop after the scan when nothing is new (same hashes, vocabulary and script hash; digest and index present).
    Write `index.db` and `memory/DIGEST.md` every time (digest: a comment line, the count, how to ask with the
    script's real path, `prefs/me-*` titles, the ten newest live decisions and models outside the general areas,
    up to eight open questions — question notes no finding or decision builds on; ≤ 40 lines). Store the script's hash in the manifest so an upgraded script rebuilds the graph once, 0 calls.
    The summary line reads `dream: N notes · K indexed (C calls) · … · P pending`.
- **Exit conditions:**
  - [ ] `python3 tests/acceptance.py A3 A5 A6 A7 A8 A9 A10 A12` all pass.
  - [ ] Re-run A4, which now passes with 0 calls.
  - [ ] Run `dream` twice in a row on the indexed fixture. The second prints `0 indexed (0 calls)` and
        `nothing new`.

<--->

_Part 3 of 9 · online-build-bundle.md — phases P6–P8_

### P6 — Answering: `ask`

- **References:** Appendix C §5.7 (steps 1–9); RESULTS round 2 ("What changed") and round 4 (taste).
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
    (successor of a superseded note, children for "what came of", parents two hops back for why); finally a
    superseded note never outranks its live successor (the successor's score is at least the old note's). Return
    ≤ 8 notes that score ≥ 20% of the best. Short `(above)` / `(more)` headers keep the SUPERSEDED mark. For every
    question, up to 4 relatives of the picked notes (parents, successors; children for "what came of") follow as
    a header plus their `# ` line (in the complete print they are part of the memory, not pointers).
  - Print `▸ path · kind · date · from … · SUPERSEDED → newer` and the best 2–4 lines under it. Print whole
    notes when everything fits the budget (900 chars per question + 1,500).
  - Taste block, for task intent only: up to twelve notes from the general areas. A named person brings all of
    their notes; a person named inside a matched house note (the roster of the deck, the meeting) counts as named
    (two hops); the house rules for the artifact asked for come along, plus `prefs/me-*`.
  - Small memories (≤ 200 notes): when the whole memory would cost ≤ 1.2× the surgical output, print per-question
    `▸ path` pointers and then every note by area — complete, no dearer than `cat`.
  - Weak match: an id, version or number the question names that no note mentions is always flagged; a plain word
    found nowhere, when the best note covers ≤ half the question's words, is flagged too. The rule reads the
    question's own words (never the aliases the index added; a hyphenated phrase is judged by its words) and prints
    `(weak match: 'x' found nowhere in memory …)` under the question. Absence set: 70 of 70; real questions 2 of 326.
  - A project named in plain words scopes the search (match folder names on the question's unstemmed words;
    general areas are never scopes by word).
  - Claude Code's auto memory, read-only (`cc_search`): one grep over the resolved directory's topic files
    (never `MEMORY.md`), at most three files and two lines each per question, printed under
    `▸ claude-code: <file> · <type> · <date>` after the notes. Nothing is ever written there.
  - `ask` must work with no index at all (grep plus lineage).
- **Exit conditions:**
  - [ ] `memory.py --root tests/fixture/memory ask "what came of exp-014?" "who owns cards.txn_daily?"` gives one
        output with a block per question. The exp-014 block reaches churn-xgb-v3 and shows v2 as SUPERSEDED.
  - [ ] A2's ask check passes (ask answers from lineage + grep with no model).
  - [ ] `python3 tests/acceptance.py A25 A26 A28 A29 A31` passes (whole-memory print, folder scope, weak match,
        two-hop taste, Claude Code's memory read and never written); A27 (C9), A30 (kinds), A32 (digest) and A33
        (frontmatter convention) belong to P3 and P5 and pass once those are done.
  - [ ] **Retrieval gate** (needs the P10 tier-1 world, no LLM): `python3 eval/retrieval.py <W>/memory eval/questions/bank-*.jsonl`
        gives gold-note recall ≥ 0.88, number recall ≥ 0.95, precision ≥ 0.55 at ≤ 2.6k chars per question. The
        reference measured 0.937 / 0.980 / 0.616 / 2,361 (fake index; 0.946 / 0.978 / 0.597 / 2,487 on a real one).

### P7 — Big memories: index.db, routing, patching, viewer split

- **References:** Appendix C §5.8; RESULTS round 4 ("What broke at 100×, and the fix").
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

### P8 — Viewer (`assets/viz.html`, `render_viz`): the two plots

- **References:** Appendix C §5.9 (the whole page); RESULTS H3–H4; `tests/viz_check.js` (the runnable checks).
  This phase builds the two plots only — the **Timeline** (notes by topic and date with their lineage) and
  **Connections** (the things the notes talk about and their current links). Everything else on the page (search,
  the Selected panel, the markdown rendering, Worth checking) is optional here and described in Appendix C §5.9.
- **The frame both plots share.** One self-contained HTML file, no external requests; the data in
  `<script type="application/json" id="data-graph">` (CONTRACT §3: `notes` with `path, kind, updated,
  superseded_by, title`, `edges` with `src, dst, rel ∈ from|supersedes|refs`, `entities` with `id, type, mentions`,
  `relations` with `s, type, o, evidence`, and `families` `{kinds, types}` — the class tree). Plain words only on
  the surface: a `human(id)` that splits on `- _ .`, upper-cases tokens of ≤ 3 letters and known acronyms, keeps
  `v3` and `2025Q4`, capitalises the rest (`gbm-model-exp233` → "GBM Model Exp233"); kinds and link types read
  "Finding", "evaluated on"; dates read "30 Oct 2026"; raw ids live only in `title` tooltips. Tokens on `:root`,
  nothing else names a colour: a white page; one black at four strengths for text — `.95 .80 .70 .60` — and four
  for rules — `.95 .44 .34 .16` (`rgba(0,0,0,a)`, so ink sits right on any tint); one blue `#7297c5` with its text
  twin `#446ea6` and a 16% wash, used only for what is selected and the lit path; status colours for status only
  (positive `#398025` on `#e9f4e6`, negative `#c2170a` on `#fbeeed`, warning `#b2570d` on `#fdf3ad`, shown as a
  tint under a 3px rule of that colour); and the families in series order — finding/metric navy `#092c61`, model
  blue `#7297c5`, rule/party magenta `#a6428c`, dataset teal `#159788`, decision/system orange `#e0731a`, feature
  purple `#7537ad`, term ochre `#bd8c00`, question and other greys `#8d8f91` / `#a2a4a6` (the 5th and 8th nearly
  merge under deuteranopia, so shapes carry identity as well). Square corners (`* { border-radius: 0 }`), no shadow
  at rest (an overlay such as the search results may carry `0 4px 24px rgba(0,0,0,.12)`), spacing on 8, system
  faces only (`"Helvetica Neue", Helvetica, Arial` for everything; `Georgia` for the page title and a picked note's
  title; no web fonts, no icon set, no brand mark or wording of any kind). Every module opens with a 3px ink rule;
  view tabs are plain words over a hairline with a 2px blue line under the open one; buttons and chips are square
  1px ink outlines; lists use hairline rows. Shapes carry identity too: square decision/party, diamond finding/feature, triangle model, hexagon
  dataset, circle metric/term/question, wide rectangle tool. A child kind takes its family's shape with a lighter
  fill. Two legend rows (nodes, then lines), each entry a button that toggles an `off` class on what it names; an
  edge hides when either end is hidden. `prefers-reduced-motion` turns the animations off.

- **P8a Timeline — do:**
  1. Rows: one per area (project areas first, general ones last and in italics), `ROW = 42` px; columns: x from the
     date, `LEFT = 170`, 34 px per month, width `max(720, …)`; a month grid (lines at 7% ink, January at 16%) with
     uppercase labels every `ceil(months/18)`, and each year drawn once as a faint watermark (4.5% ink, 64 px,
     `aria-hidden`) behind the first rows. No line between rows: lanes are bands of colour, white and light grey
     by turns for the project areas, a blue wash for the general ones, each zone headed by an uppercase label
     (Projects, General) when both exist; the picked note's or area's lane takes a 12% blue wash; the lane-label
     column repeats the band colour so it reads as part of the lane when the lanes scroll.
  2. Place each note at its date; when two notes of a row land within 11 px, nudge the later one into the next of 4
     sub-lanes (8 px apart). Draw order: grid, row lines, edges, nodes, labels — the labels in a last layer with a
     panel-coloured rect behind each, translated by `scrollLeft` on scroll so they stay put (sticky).
  3. Mentions (`refs`) start hidden — their legend entry is off until the reader turns it on — so a lane is not a
     thicket of lines; within a lane a link is an arc above the notes (quadratic, height `min(0.55·ROW, 6 +
     0.22·|dx|)`), never a line along the lane. Between lanes, edges are cubic curves from the older note (`dst`)
     to the newer (`src`), control points `±min(70, max(14,
     |Δx|/2))`; `from` solid, `supersedes` dashed in the accent, `refs` faint; past 4,000 edges skip `refs`.
  4. A superseded note is drawn hollow and dashed. Hover lights a note's own curves (`hot`). A pick adds `picked`
     (the shape scales 1.75× through CSS `transform` with `transform-box: fill-box`, no ring), marks its linked notes
     `hot` (1.3×), lights its curves (accent, `stroke-dasharray 6 4`, `marker-end` arrowhead at the newer end, a
     `stroke-dashoffset` keyframe flowing toward it), dims everything beyond two lineage hops, and scrolls the pane
     to centre it. Search hits get `hit`; an area pick keeps its row.
  5. Clicking a row label opens the area; clicking a node picks the note (`dp:pick`).
- **P8a exit conditions:**
  - [ ] `viz` writes `_dream/graph.html`; `grep -c 'https\?://'` finds no script or stylesheet URLs.
  - [ ] `node tests/viz_check.js <page>`: one `.node` per non-log note, `.edge` paths, two `.legend` rows with ≥ 3
        toggles; `#note=<path>` gives one `.node.picked`, ≥ 1 `.edge.hot` with a `marker-end`, and `.dim` on the
        rest; a legend toggle hides that kind's nodes and the curves touching them; 0 page errors.
  - [ ] The 1,677-note bank draws 1,524 notes and 3,680 curves in under 3 s (reference 0.9 s).

- **P8b Connections — do:**
  1. Nodes: entities with at least one *current* relation (one of its evidence notes is live) or ≥ 2 mentions,
     sorted by mentions + degree, the first 400; "Include older versions" admits relations stated only in
     superseded notes. When a picked entity is outside the set, rebuild as its neighbourhood (two hops, ≤ 150) with
     a "Show all" button back. Node radius `4 + min(6, √mentions)`; an entity that a `replaces` relation points at
     is drawn hollow and dashed. Arrows: `uses`, `part-of`, `owned-by` solid; `replaces` dashed in the accent;
     `trained-on`, `evaluated-on`, `measured-by` dotted; `other/…` faint; `marker-end` arrowhead, `vector-effect:
     non-scaling-stroke`.
  2. Layout, deterministic, in columns: one zone per family. Order the families so linked ones sit side by side
     (cost = Σ over cross-family links of their column distance; try every order of up to eight families with
     Heap's algorithm, else keep size order; the larger end on the left). Inside a zone sort by degree, then
     mentions; `lanes = min(4, ceil(n/48))`; the most connected go to the right-hand lane (the one that carries
     names at rest), the rest leftward; zone width `28 + (lanes−1)·40 + 150`, zones 56 apart; row spacing
     `SP = clamp(16, 36, (paneH−16)/(paneW−16) · W / tallest lane)` so the figure fills the pane's height; each lane
     centred vertically; then six barycentre sweeps (sort a lane by the mean y of each thing's neighbours, replace).
     Zones are rects from far above to far below the figure (white / light grey by turns), with a 28 px strip of
     HTML labels above the pane positioned by the camera (`left = x·k + cam.x`, `width = w·k`, uppercase, ellipsis).
     Curves: cubic between columns (`c = max(24, 0.4·|dx|)` in the travel direction), a quadratic bowing out to the
     left between two things of the same lane; the end shortened by the target's radius + 2.
  3. A camera, not a scrollbar: all layers under one `<g transform="translate(x y) scale(k)">`; `fitAll()` picks
     `k` to fit the pane (clamped 0.12–2) and centres; `zoomAt(f, sx, sy)` zooms around a screen point (`k` clamped
     0.1–6); wheel `f = exp(−Δy·0.0012)`; drag on the background pans; drag on a node moves it (`moveNode` rewrites
     its transform, its label and its arrows' endpoints); two pointers pinch; a pointerup without 3 px of movement is
     a click (pick a node); +/−/⌂ buttons; the fit leaves the 28 px name strip clear. Labels keep their size by
     `font-size = 10.5/k`; the label layer gets `far` when `k·SP < 10` (rows closer than 10 px), which hides every
     name except those with `keep` (the picked thing and its neighbours, a hovered thing's, the fisheye's).
  4. Fisheye: on pointermove (rAF-throttled) each shown node gets `scale(s)` on its shape with
     `s = 1 + 0.95·exp(−d²/(2·60²))`, `d` the screen distance to the cursor; names get `keep` for `s > 1.35`;
     cleared on leave (names kept by the pick stay).
  5. Legends hide a family's zone and name along with its things; "Include older versions" rebuilds with the
     relations stated only in superseded notes.
  6. Pick focus: dim beyond two hops (one hop for hubs with > 30 neighbours); the pick's curves and neighbours
     `hot`, their names `keep`; the pick's zone and its name in the strip `picked` (blue wash, blue text); centre
     the camera on it (zoom 1.1) when zoomed out below 0.8, or when it is off screen. Hover lights a node's curves
     and names its neighbours. Legend rows: families (+ "Older version"); relation types (+ "Other links").
- **P8b exit conditions:** (`node tests/viz_check.js <page>` runs all of them)
  - [ ] `#view=graph`: `.gnode` count = shown entities, `.gedge` count = shown relations, two legend rows, a legend
        toggle hides a family's nodes.
  - [ ] One `.gzone` and one strip name per family, every thing's x inside its family's zone; picking a thing marks
        exactly one zone and one strip name `picked` and keeps some names; zooming to `k = 0.15` sets `far` on the
        label layer and zooming to `1.5` clears it.
  - [ ] A background drag changes `cam.x`/`cam.y` by the drag; a wheel step changes `cam.k`; dragging a node moves
        `state.pos[id]`; moving the mouse over a node sets inline `transform: scale(…)` on nearby shapes
        (reference: 51 within ~150 px on the bank); 0 page errors.
  - [ ] The bank's 400 nodes and 1,355 arrows lay out in under 3 s (reference 1.3 s).
- **P8c Map (v2) — do** (the tab that opens first; `#view=time` and `#view=graph` open the other two; the same things read for trust, after a public ontology viewer's
  idea — a person asserts → what it becomes → who reads it; verdicts; one connected graph; a legend that says what each
  statement is worth — in our own theme):
  1. The flow, three columns with arrows, each row a status swatch + a line + a small badge: *The notes* (written,
     current, read by the assistant; logs aside) → *What they become* (stated links = lineage edges other than
     mentions, badge STATED; facts = relations with at least one live evidence note, badge QUOTES ITS LINE; older
     facts = the rest; things named, with how many have a home note) → *Who checks it* (conflict pairs, badge
     REVIEWER; C12 + C1/C2 counts, badge RULES; open questions = question notes with no `from` edge pointing at
     them, badge OPEN; "You" → Worth checking). Swatches: ink written/stated, blue extracted, grey older, red
     disputed, amber open, green pass. On `dp:pick` rewrite it for the note (its lineage counts, its facts with
     line numbers, its things, its conflicts, its checks, open/answered if a question) or the thing (facts in
     current notes, older facts, its spellings, odd links naming it).
  2. The graph: the 400 most linked things by current relations; a deterministic force layout (seed 11; repulsion
     `K = 24`, zero beyond `7K`, capped 32; springs rest 42, stiffness 0.06; pull 0.012 toward the family's place
     on a ring of `0.5R` and 0.015 toward the centre; 200 iterations, 140 past 250 nodes; step cap `3 + 28·cooling`);
     radius `2.5 + min(10, 1.7·√degree)`; fill = family colour with an ink outline when the thing has a home note,
     else `rgba(0,0,0,.55)`; the 12 highest-degree things named at rest (`hub`), names sized by the layer
     (`font-size = 11/k`, never in CSS), kept for the picked thing and its neighbours (≤ 40) and under the hover;
     a caption line with the count and the top five relation types; a legend line under the frame.
  3. Two tables, each a label header over a 1px ink rule and hairline rows: "What the memory holds" with six counts
     (written, stated, extracted, older, disputed, open) and one sentence each; "What a statement is worth" with
     the action for each kind.
- **P8c exit conditions:** (`node tests/viz_check.js <page>` runs them)
  - [ ] `setView('map')`: `.mnode` = the map state's nodes (> 0), `.medge` = its edges, ≥ 1 `.mlabel.hub` whose
        computed font size × `cam.k` is 10–12 px, three `.mflow .col`, ≥ 10 table rows with six counts.
  - [ ] Picking a thing marks one `.mnode.picked`, lights its `.medge.hot`, dims others, and the flow's first
        column heading reads "The thing".
- **Reference numbers** (bank, 1,677 notes, real Haiku index): page 2.6 MB; Timeline 0.9 s; Connections 400 of 900
  things, 1,355 current arrows, 1.3 s; both plots 0 console errors in headless Chromium.

<--->

_Part 4 of 9 · online-build-bundle.md — phases P9–P11, handoff, done, traps_

### P9 — Integration

- **P9a, deterministic (required):**
  - [ ] `python3 tests/acceptance.py` prints `35/35 passed` in under 60 s, and `memory.py check` on the fixture
        starts with `contract: schema 1 ok`.
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
Appendix C §7; only the gates are repeated here.

| tier | build | gate (exit condition) | cost |
|---|---|---|---|
| 1. 56× world | `eval/bank/assemble.py eval/bank/generated tests/fixture/memory <W>/memory`, then a Haiku `dream -j 10` with `tests/haiku_cmd.py` | 1,677 notes indexed, 0 C3; cost per note ≤ $0.003 | measured $3.73 at $0.0022 per note before the cache-aware wrapper, $0.0013 per note with it; ~25 min at `-j 10` |
| 1-free | the same world, indexed with `MEMORY_LLM="python3 $PWD/tests/fake_dreamer.py" memory.py --root <W>/memory dream -j 10` | `1677 indexed`, `0 pending`. Enough for the P6 and P7 retrieval gates. Measured on the reference: 0.937 / 0.980, routed 0.932 / 0.971 (the real Haiku index: 0.946 / 0.978, routed 0.940 / 0.968) | $0, ~20 s |
| 2. offline retrieval | `eval/retrieval.py`, both normal and `MEMORY_WIDE=100`; `--must` for history-free gold | ≥ 0.88 gold / ≥ 0.95 numbers / precision ≥ 0.55 / ≤ 2.6k chars per question (reference 0.937 / 0.980 / 0.616 / 2,361 on the fake index; 0.946 / 0.978 / 0.597 / 2,487 on a real one) | $0 |
| 2b. adversarial sets | `eval/adversarial.py <W>/memory eval/questions/bank-*.jsonl [--index-world <real-indexed world>]` | stale: successor above the old note ≥ 0.90 and old marked 1.00 (ref 0.971 / 1.00 on both); scattered evidence all-gold ≥ 0.60 at ≤ 2.4k chars (ref 0.782 / 2,231 fake, 0.794 / 2,339 real); absence (70 questions about things not in memory): ask flags ≥ 0.95 as "(no match" or "(weak match …" (ref 1.00 on both indexes); alias (needs `--index-world` on a real Haiku index; the fake index records almost no surface forms): with the index ≥ without it > grep, and ≥ 0.80 on the full bank (ref 0.893 / 0.829 / grep 0.521 on 280 forms; 0.929 on the 70-note world's 14 forms) | $0 |
| 3. agent eval | `eval/agent/make_batches.py`, then Opus subagents per batch on the memory arm and the grep arm (prompt in Appendix C §7.3; the grep arm may `cat` whole folders — the strongest baseline; both read the questions from one file and report tool calls per question), then `a21/extract.py` where transcripts exist, `judge.py`, `agent/summarize.py` | memory accuracy ≥ grep accuracy minus 1 correct per 10 questions, **and** memory tool calls ≤ 0.35× grep (reference: 0.23× in round 2; phase G on the real Haiku index, 3 batches per arm: 23/7/0 against 23/7/0, tool calls 0.30×, tokens processed 0.29×, cost units 0.61×, wall time 0.75×); report cost units only when transcripts give them (`eval/a21/extract.py` reads the subagent transcripts) | Opus tokens; 2 arms × ≥ 3 batches |
| 3b. write path | one Opus subagent gets SKILL.md, a copy of the fixture and a short fictional session transcript (facts with numbers, a decision, an ownership change, a correction that should supersede an existing note, two spoken preferences, one non-fact); it writes notes and must not run `dream`. Then `dream` with no model, `check`, and `ask` for each fact | every fact findable by `ask`; the correction carries `supersedes:`; preferences land in `prefs/<first>-<last>-<topic>.md`; no note over 40 lines; the non-fact not saved; 0 C1/C2/C6 warnings | one Opus run |
| 4. 100× | `eval/scale/make_world.py <W>/memory <X>/memory --copies 137`, `bootstrap.py`, `time_ask.py`, `profile_incremental.py` | `ask` on 10 questions < 5 s (ref 2.3 s); a dream with nothing new < 10 s (ref 3 s); retrieval ≥ 0.83 / ≥ 0.93 | ~20 GB disk, ~5 GB RAM; Haiku about $0.06 for 30 notes |
| 5. taste | `eval/taste/score.py <W>/memory eval/taste/tasks.jsonl` (fixed tasks), optionally the T1/T2 agent runs and `taste/judge.py` | named-person preference recall ≥ 0.85 (ref 0.93); house rules ≥ 0.35 (ref 0.42) | $0 for the scorer |

Every tier reports its numbers in the same rows as Appendix C §8, so they can be compared side by side.

### P11 — Package, install check and docs

- **Do:** follow Appendix C §2 to install the skill and agent into a scratch `HOME`, with
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

<!-- appendices: generated by tests/bundle_refresh.py — everything below is copied from the repository; edit the sources, not this -->

<--->

## Appendix A — the contract surface, verbatim: `skills/memory-dream/SKILL.md` and the dreamer agent

_Part 5 · copied at commit 6ee2bae. Mode B workers write these files; Mode R workers check them. The skill text is what every agent reads, so its wording is part of the contract (achievement per word)._

```markdown
---
name: memory-dream
description: Project memory for data-science and coding work. Plain notes in memory/<area>/, one per thing (question, experiment, finding, decision, dataset, feature, model, a person's preference, rule, term, correction). Before answering anything about past work, and before making something for someone (chart, table, deck, email, notebook, query), make ONE call with all your questions and tasks — python3 <this skill>/scripts/memory.py ask "q1" "q2" … — it greps the notes with memory (aliases, lineage, superseded → current, who wants what) and prints the lines that answer. Write a short note per new fact as you work; run memory.py dream at the end.
---
# memory-dream

For any agent with a shell: Python 3.9+ and grep, no model required. The notes in `memory/<area>/<slug>.md` are the
truth; everything else is derived and disposable. `memory.py` = `python3 <this skill>/scripts/memory.py`
(root: `--root`, `$MEMORY_DIR`, or the nearest `memory/` upward).

## What an agent does with memory
1. **Read first, once.** Before answering about past work or making something for someone, put every question and
   task into ONE call: `memory.py ask "what came of exp-014?" "Make the Q4 chart for Chloe Martin's readout"`.
   Per question it prints `line: text` under `▸ path · kind · date · from … · SUPERSEDED → newer`; a small memory is
   printed whole, each question pointing at its notes. SUPERSEDED → a → b is history: the last named is current. For a task it
   adds the preferences and house rules that apply — follow them, or say why not. `(weak match …)` names a word found
   nowhere: rephrase. Name the project or an id when you know it; it scopes the search. At most one batched
   follow-up: `ask` with sharper words, plain `grep -rn … memory/`, or read a printed line.
2. **Write as you go.** One note per thing, in `memory/<project>/`, or for what spans projects in `prefs/`,
   `reporting/`, `glossary/`, `corrections/`, `howto/`, `qa/`, `people/`. The filename is the id (a model's note is
   named after the model; prefixes `exp- feat- ds- dec- fnd- q-` say what it is). The `# ` line is the claim; the
   first paragraph is what is true now. Frontmatter `from: [notes built on]`, `supersedes: [notes overturned]`:
   never rewrite an old conclusion, write a new note that supersedes it. Numbers carry metric, eval set, n, date;
   sources (tables, notebooks, queries) in backticks. ≤ 40 lines, plain markdown, nothing about the memory system.
   Taste is said once, in passing ("no pie charts", "round to 1 decimal for the board", "too AI-looking"): save it
   then — `prefs/<first>-<last>-<topic>.md` (your user's own: `prefs/me-<topic>.md`): the rule, where it applies
   (artifact, meeting, audience), why. When it changes, a new note with `supersedes:`.
3. **Dream at the end.** `memory.py dream` (background is fine) refreshes `_dream/graph.html` — the map, health,
   review queue — the digest `memory/DIGEST.md` and the index. With `$MEMORY_LLM` set (e.g. `claude -p --model haiku
   --tools ""`) a cheap model also names entities and typed relations; without a model nothing is missing for
   answering, and `memory.py dream --prompts` writes prompts for any helper agent (`memory-dreamer`) when you want
   entities too. `memory.py check` lists warnings. Scratch lines: `memory.py log "…" -p <project>`.

## Beside Claude Code's own memory (when you are Claude Code)
CLAUDE.md holds standing instructions people wrote; auto memory holds what you learned about the user; these notes
hold the work itself, with lineage, and travel with the repository. `ask` also reads your auto-memory topic files in
the same call and never writes there. To keep the digest in context every session, add one line to CLAUDE.md:
`@memory/DIGEST.md`. Never the same thing in two places: if CLAUDE.md already says it, write no note.

Three files at the memory root are yours to edit, and a hand edit costs no model calls: `EDGES.md` (relation types —
a link outside them keeps its own label, shown as other/<label>; `promote`, `budget` and `probation` lines gate when a
label becomes a type), `ALIASES.md` (`- canonical = other-id` merges entity ids, `not: a / b` keeps them apart) and
`CONFLICTS.md` (two live notes that disagreed: `- a > b` makes a supersede b without touching either note).
```

`skills/memory-dream/agents/memory-dreamer.md` (the helper agent for the no-API-key path):

```markdown
---
name: memory-dreamer
description: Answers memory-dream prompts in memory/_dream/pending/. Use when memory.py dream reports pending prompts.
model: haiku
tools: Read, Write, Glob
---
memory/_dream/pending/TODO.md lists the pending prompt files, one path per line.
For each listed *.prompt.md that has no matching .json: read it, follow it,
and write only the JSON answer to the same path with .json in place of .prompt.md.
Touch nothing else.
```

<--->

## Appendix B — the graph contract, verbatim: `.specs/memory-dream/CONTRACT.md`

_Part 6 · copied at commit 6ee2bae. Schema 1; `memory.py check` validates against it (A38)._

## memory-dream — the graph contract (schema 1)

What `memory.py` writes and reads, field by field. The viewer, `ask`, `check`, the tests and any other consumer build
on these shapes and nothing else. `schema` is carried by every graph (`graph.json`, `index.db` meta, the viewer's data
island) and is bumped when a field changes meaning; `memory.py check` validates a graph against this contract and
test A38 enforces it on the fixture.

Conventions. Paths are relative to the memory root with `/` separators and the `.md` suffix (`churn-2026/exp-014.md`).
A note's **id** is its filename without `.md`; its **project** (area) is the first path segment, `""` at the root. Dates
are ISO `YYYY-MM-DD`. Line numbers are 1-based file lines. Everything under `_dream/` is derived and disposable; the
notes and the four user-owned files (`EDGES.md`, `ALIASES.md`, `CONFLICTS.md`, and the generated `DIGEST.md`) are
not.

### 1. The graph

Produced by `build()`, written as `_dream/graph.json` (≤ `MEMORY_WIDE` notes) and as `_dream/index.db` (always).

| key | type | meaning and invariants |
|---|---|---|
| `schema` | int | this contract's version, `1` |
| `v` | str | `memory.py` output version (`"0.4"`) |
| `built` | str | `YYYY-MM-DDTHH:MM` |
| `notes` | list of note | sorted by path |
| `entities` | list of entity | sorted by folded id |
| `relations` | list of relation | sorted by (folded s, type, folded o) |
| `edges` | list of edge | lineage between notes; unique per (src, dst, rel) |
| `proposed` | list of label | labels over the `promote` bar, offered to the review (empty when the budget is full) |
| `review` | list of `{a, b}` | entity pairs for the review (canonical ids) |
| `conflicts` | list of conflict | live-note pairs that may disagree |
| `vocab` | object | `{types, budget, promote: [uses, notes, areas], probation, labels, below, demote: [type]}` |
| `dedup` | object | counters from entity merging (`mentions`, `ids_as_written`, `after_folding`, …) |
| `checks` | list of `{code, msg}` | warnings, sorted by code; codes `C1`–`C12` (§5) |

**note** — `{path, id, project, title, line, kind, updated, superseded_by, sha, indexed}`
- `title`: the text of the first `# ` line outside code fences (`""` when none → C6); `line`: its file line (0 when none).
- `kind`: lowercase; frontmatter `type:` wins (Claude Code's `user|feedback|project|reference` map to
  `preference|rule|note|note`), else the dreamer's kind unless it is `note`, else the filename prefix (first two id
  segments: `exp- feat- ds- dec- fnd- find- finding- q- metric- model- pref- rule- term-`; `…-vN` → `model`), else the
  area (`prefs`→preference, `glossary`→term, `corrections`→correction, `reporting`/`howto`→rule, `log`→log), else `note`.
- `updated`: frontmatter `updated:` or `modified:` (first 10 chars), else a `log/YYYY-MM-DD` filename, else mtime.
- `superseded_by`: paths of notes whose `supersedes:` names this note, plus `- a > b` lines of `CONFLICTS.md`; every
  entry has a matching `supersedes` edge.
- `sha`: first 12 hex of the note's SHA-256; `indexed`: an extraction exists for this sha.

**edge** — `{src, dst, rel}` with `rel ∈ {from, supersedes, refs}`; `by: "review"` marks a supersession recorded in
`CONFLICTS.md`. `from` and `supersedes` come from frontmatter (resolution: relative path, exact path, unique filename,
same-project filename → C1 if ambiguous, then moved paths; unresolved → C2). `refs`: `[[links]]`, the dreamer's refs,
and body slugs that name a note in the same project or a unique note anywhere.

**entity** — `{id, type, home, aka, names, headline, mentions}`
- `id`: canonical (the `ALIASES.md` lead, else the most-used spelling); `type`: lowercase (`dataset feature model metric
  segment person team term tool other`); `aka`: other spellings merged into it; `names`: `[{name, n}]` surface forms
  with counts; `home`: the note whose id is this entity's id, or null; `headline`: the best live note mentioning it
  (title-line mention, then finding/decision, then newest), or null; `mentions`: `[{path, lines}]` sorted by path.
- Kept only with a home note, ≥ 2 mentioning notes, or an `ALIASES.md` line; file-like ids are dropped.

**relation** — `{s, type, o, evidence}`; `s`, `o` are entity ids; `type` is a vocabulary type from `EDGES.md` (incl.
packs and `(proposed …)` types) **or** `other/<label>` with the label folded (lowercase, `-` joined); `evidence`:
`["path:line", …]`, the note and line stating it. `drop:` types never appear.

**label** (in `proposed`) — `{type, uses, notes, areas, examples}`: the label, instance count, distinct notes, distinct
areas, up to 3 `"s — o: quote"` examples.

**conflict** — `{a, b, shared, unsure}`: two live notes of one kind in one area, not linked by lineage, `shared` = the
id-like or rare title tokens they share (or `version` for `…-vN` siblings, `same title` for equal titles); `unsure`:
the reviewer answered unsure (`- a ? b`), so it waits for a person and is not asked again.

### 2. `index.db` (SQLite, read by `ask` on big memories, `check`, `viz`)

`meta(k, v)` — JSON values for `schema`, `v`, `built`, `proposed`, `review`, `dedup`, `vocab`, `conflicts` ·
`notes(path, id, area, title, line, kind, updated, sha, indexed, sup)` with `sup` = JSON `superseded_by` ·
`edges(src, dst, rel)` · `ents(id, type, home, headline, aka, names)` · `ment(eid, path, lines)` ·
`names(k, eid)` — folded spellings (id, aka, names ≥ 3 chars) → entity · `rels(s, type, o, ev)` · `checks(code, msg)`.
`read_index(dd)` returns the graph of §1 from these tables; the two forms are interchangeable.

### 3. The viewer's data island (`<script type="application/json" id="data-graph">`)

The graph of §1 with: each note carrying `text` (its non-blank lines from the `# ` line, ≤ 60); `families`
`{kinds: {child kind: parent}, types: {child type: parent}}` — the class tree (two levels; `experiment` under
`finding`, `correction` and `preference` under `rule`, `metric` under `term`; `table` and `segment` under `dataset`,
`column` under `feature`, `person` and `team` under `party`, `tool`, `job`, `pipeline`, `service` under `system`;
anything absent is its own family), which the viewer uses for colours, shapes and legends and the checks for C12
and conflict kinds; and a `mode`:
- absent — the whole memory;
- `"area"` — one area's page: `area` (name), `home` (the overview's relative URL), notes of other areas that lineage
  touches present as stubs with `text: []`, `entities` limited to those mentioned in the area, `relations` to those
  with evidence in it;
- `"overview"` — big memories: `pages` (relative directory of area pages), `totals` `{notes, entities, relations,
  edges, areas, checks: {code: n}}`, `areas` `[{id, n, general, kinds: {kind: n}, updated, superseded, warnings,
  edges}]`, `area_links` `[{a, b, w}]`, `checks` (first 300), `chains` `[{path, title, by}]`, `orphans` `[{path, title,
  kind}]`, `review`, `proposed`, `conflicts`; `notes`, `entities`, `relations`, `edges` empty.
The viewer derives everything else client-side (per-note entities from `mentions`, per-note relations from `evidence`,
the `ask` header from edges and `superseded_by`, following `superseded_by` chains to the live end as `ask` does; a
relation is "current" when one of its evidence notes is live).

### 4. Caches and the manifest (`_dream/`)

- `notes/<sha12>.json` — one extraction per note content: `{kind, entities: [{id, type, as, lines}], relations:
  [{s, type, label, o, quote, line}], refs, dropped: {entities, relations}, path, sha, model, indexed_at}`. Entities
  keep only surface forms (`as`) that occur in the note; relations only with their quote found (the rest counted in
  `dropped` → C4). Kept `KEEP_DAYS` after last use.
- `store.db` — `facts(path, sha, rec)` parsed note facts (`fm`, `title`, `line`, `links`, `ids`, `nul`, `lines`);
  `x(sha, mt, rec)` the extraction, valid while its file's mtime matches.
- `manifest.json` — `v`, `code` (hash of memory.py), `files {path: {sha, mtime, size}}`, `former {path: [old paths]}`,
  `vsig` (hash of EDGES + ALIASES + CONFLICTS), `seen`, `queue`, `failed`, `attempts`, `refs`, `dreamed`, `unindexed`,
  `due`. A dream with nothing changed in any of these stops after the scan.
- `pending/` — `<sha12>.prompt.md` and `review.prompt.md` written by `dream --prompts`, answered as `.json` by a helper
  agent; `TODO.md` lists them. `lock` — pid of a running dream.

### 5. Warnings

`C1` ambiguous lineage target · `C2` lineage target not found · `C3` the dreamer's answer was unusable twice ·
`C4` an ungrounded entity or relation was dropped · `C5` no extraction yet (one summary line in `check`) · `C6` no `# `
line · `C7` vocabulary: a label over the bar awaits review, the budget is full, or labels sit below the bar · `C8` an
unparseable line in EDGES.md, ALIASES.md or CONFLICTS.md · `C9` NUL bytes in a note · `C10` conflict pending ·
`C11` a note over 40 lines (SKILL.md's own rule) · `C12` a seed-type relation whose entity families are unusual for
it (`trained-on` is model → dataset, `evaluated-on` → dataset, `measured-by` → metric, `owned-by` → party, `replaces`
the same family on both sides; families by the class tree below): retype the entity or drop the relation.

### 6. The user-owned files

`EDGES.md`: `promote: U uses, N notes, A areas` · `budget: B` · `probation: D days` · `pack: name, …` · type lines
`- type[ (proposed YYYY-MM-DD)]: definition | aka: a, ~b, …` · `drop: a, b, …`. `ALIASES.md`: `- canonical = other, …` ·
`not: a / b`. `CONFLICTS.md`: `- a > b` (a supersedes b) · `compatible: a / b` · `- a ? b` (unsure). `DIGEST.md`:
generated by every dream, ≤ 40 lines, never edited by hand.


<--->

## Appendix C — the build guide, verbatim: `BUILD-GUIDE.md` §3–§10

_Part 7 · copied at commit 6ee2bae. The design in one page, the repository layout, every module's algorithm (§5: notes and SKILL.md, scan, note facts, the graph's two halves, the dreamer, answering, big memories, the contract, the viewer), the tests, how to reproduce the evaluations, the numbers to expect, the pitfalls and the known limits. Phase briefs point here as "Appendix C §n"._

### 3. The design in one page

1. **Thin layer on grep.** Agents are good at grep and Read; the tool enhances them, never replaces them. Every
   change is benchmarked against a grep-only agent on the same questions.
2. **One call.** Round 1 lost to grep (2.3× cost) because of round trips: every request re-sends ~37k tokens of
   context. `ask` takes every question at once and prints only the lines that answer.
3. **Lineage is written by the author, not inferred.** `from:` (built on) and `supersedes:` (overturns) in
   frontmatter; a superseded note is shown as history with its successor.
4. **The index is optional for answering** and earns its keep for aliases, dedup, the viewer and management.
   Measured on a real Haiku index of 1,677 notes (RESULTS F4, F9): with it `ask` gains 0.8 points of gold recall
   and 6.4 on alias questions for 5% more characters; without it nothing is missing. It must stay cheap and
   conservative: loose names hurt retrieval.
5. **Constrained open relation vocabulary.** Eight types; any other link keeps its label (`other/<label>`), and a
   label becomes a type only over an evidence bar, through the review, within a budget, on probation.
6. **Scale by routing, not by heavier machinery.** Past 10,000 notes, `ask` greps only where a question points,
   reads an SQLite index row by row, and the viewer splits into an overview plus one page per area.

---

### 4. Repository layout

```
skills/memory-dream/
  SKILL.md                     what the agent reads (41 lines): read, write, end of session
  scripts/memory.py            ask · dream · viz · check · log  (stdlib, ~1,900 lines)
  assets/viz.html              viewer template (html-lite habits; normal, overview and area modes)
  agents/memory-dreamer.md     Haiku subagent for file mode
.specs/memory-dream/           build-spec.md (v0.4 spec), RUNBOOK.md, RESULTS.md (rounds 1–4)
tests/
  fixture/memory/              churn-2026: 25 notes + 5 log days (hand-written ground truth)
  acceptance.py                A1–A20 (spec) + A24 (big memories), fake dreamer, < 1 min
  fake_dreamer.py              deterministic dreamer (regex extraction) for tests and profiling
  haiku_cmd.py                 MEMORY_LLM wrapper around `claude -p --model haiku`, logs cost per call
  real_model.py, truth.py      Haiku runs against the fixture's ground truth
eval/
  bank/generated/              56× test bank: 1,648 Haiku-written notes in 47 areas
  questions/                   366 questions with gold notes and reference answers
  retrieval.py                 offline: did ask print the gold notes and the answer's numbers?
  judge.py                     Haiku judge: correct / partial / wrong vs reference answers
  agent/                       Opus agent eval (batches, runs, usage, judge, summarize)
  scale/                       100× world, timing, tracing, profiling
  taste/                       taste tasks, scorer, agent eval, judge
```

---

### 5. Build it step by step

Build in this order; each step is testable on the fixture before the next.

#### 5.1 Notes and SKILL.md

Note format (the only thing a person or agent writes):

```markdown
---
from: [exp-014, leak-hypothesis]      # notes this builds on (ids = filenames)
supersedes: [churn-xgb-v2]            # notes this overturns
updated: 2026-10-30
---
# churn-xgb-v3 replaces v2: AUC 0.76, recall@10 0.43 on holdout-2025q4 (no leakage)
First paragraph = what is true now. Numbers carry metric, eval set, n, date. Sources in backticks.
```

Write rules in SKILL.md: one note per thing; filename = id; the `# ` line is the point; never rewrite an old
conclusion (write a new note that supersedes it); ≤ 40 lines. General knowledge lives in `prefs/`, `reporting/`,
`glossary/`, `corrections/`, `howto/`, `qa/`, `people/`; a person's preference is `prefs/<first>-<last>-<topic>.md`,
your own `prefs/me-<topic>.md`, saved as soon as it is said.

#### 5.2 Scan and manifest (`scan`)

Walk `memory/` with `os.walk` (skip `_dream/`, dot dirs, `EDGES.md`, `ALIASES.md`, `README.md`, `INDEX.md`).
Keep `{path: {sha256, mtime_ns, size}}` in `_dream/manifest.json`; re-hash only files whose mtime or size changed.
A path that disappeared while the same hash appeared at exactly one new path is a move (`former` keeps old paths so
old references still resolve).

#### 5.3 Note facts (`parse_note`, `note_facts`)

From each note's text: frontmatter (`from`, `supersedes`, `type`, `updated`), the `# ` title and its line, `[[links]]`
outside code, and every slug-like token in the body (`[a-z][a-z0-9]*(-[a-z0-9]+)+`). Cached per path and content
hash in `_dream/store.db` so a dream re-reads only changed notes.

#### 5.4 The graph, note half (`notes_part`)

- One record per note: path, id (filename), project (top folder), title, line, kind (`kind_of`: frontmatter `type`
  with Claude Code's user/feedback/project/reference mapped to preference/rule/note/note, else the dreamer's kind unless
  it is the fallback "note", else the filename prefix `exp- feat- ds- dec- fnd- find- q- metric-` or `…-vN` = model,
  else the area `prefs/ glossary/ corrections/ reporting/ howto/ log/`, else `note`), updated (frontmatter `updated`
  or `modified`, log filename date, or mtime), superseded_by. `general_areas` judges an area on its kinded notes only.
- Edges: `from` and `supersedes` resolved by relative path, then exact path, then unique filename, then same-project
  filename (warning C1 if ambiguous), then moved paths; unresolved → C2. Plus `refs`: `[[links]]`, the dreamer's refs,
  and any body slug that names a note in the same project.
- Warnings: C1 ambiguous, C2 not found, C3 indexing failed, C4 dropped ungrounded entity/relation, C5 unindexed,
  C6 no `# ` line, C7 review pending (labels, budget), C8 bad EDGES/ALIASES/CONFLICTS line, C9 NUL bytes in a note
  (binary-looking), C10 conflict pending, C11 a note over 40 lines.

#### 5.5 The graph, vocabulary half (`build`, `merge_entities`)

Entities, from every note's extraction:
1. Key = `fold(id)`: lowercase, runs of space `_` `.` `-` → `-` (`cards.txn_daily` = `cards-txn-daily`).
2. Union-find: every ALIASES.md line merges its ids (forced); `not: a / b` lines and version pairs (ids differing
   only in digits) are never merged.
3. Surface rule: if exactly one other entity writes this id as a surface form (and ≤ 3 users), merge.
4. Keep an entity only if it has a home note (a note whose filename is its id), is mentioned in ≥ 2 notes, or is
   named in ALIASES.md; drop file-like ids (`.py .sql .ipynb .csv`, notebooks).
5. Canonical id: ALIASES.md lead, else the most used raw id; type by majority vote; headline = best current note.

Relations, two tiers: the dreamer gives each relation a `type` (an EDGES type or alias, or `other`) and a `label` (the
note's own verb). Listed types and their aliases (`~` = read in reverse) are kept with evidence `path:line`; a link
whose type and label fit nothing is kept as `other/<label>` (shown on the entity card, not on the map); `drop:` names
only note-to-note links. A label is offered to the review once it clears `promote: 5 uses, 5 notes, 2 areas`
(EDGES.md); the review answers `alias T`, `alias ~T`, `label`, `drop` or `new: <definition>`, and the code admits
`new` only under `budget: 24` types, writing `- <type> (proposed <date>): …`; a proposed type still under the bar
after `probation: 60 days` is demoted to a label (0 calls). `pack: software | research | ops` adds domain types.
Conflicts: two live `…-vN` siblings in one area, two live notes with the same title, or live notes of one kind
(decision, model, finding) in one area, unlinked, sharing an id-like title token or two rare words, are queued (C10,
20 per review); verdicts persist in `memory/CONFLICTS.md` (`- a > b` becomes lineage, `compatible: a / b`, `- a ? b`);
notes are never edited.

The seed vocabulary (8 types): `uses`, `produces`, `part-of`, `trained-on`, `evaluated-on`, `measured-by`,
`replaces`, `owned-by` (full alias lists in `EDGES_SEED`). Evidence: 81% of 5,196 extracted links fit them and 365 of
366 questions need lineage, a single note, or one of the 8 (`eval/type_coverage.py`, `eval/question_relations.py`);
with Haiku on 70 notes the two-tier prompt gives 81% typed, 19% labels, 0 invented types (RESULTS "Phase C").

Review candidates: new entities of the same type that share a rare surface form or have similar folded ids
(difflib ≥ 0.85); pairs with two different home notes are never queued.

#### 5.6 The dreamer (`dream`)

Structure: `dream` takes `_dream/lock` (a second dream exits 3; a lock older than 2 h is taken over) and runs a
`Dream` object in stages — `plan` (scan, caches, what to index), `index` (command or file mode), `graph`, `demote`
(probation over), `run_review` (labels over the bar, entity pairs, conflicts), `write` (viewer, index.db, digest,
pending list, manifest), `report`. The tuned numbers of `rank`/`route` live in the `W` table beside the retrieval
constants, each with the measurement that set it.

- **Extraction prompt** (`EXTRACT`): JSON with kind, entities `{id, type, as[]}`, relations `{s, type, o, quote}`,
  refs. It gets the EDGES list and KNOWN: up to 80 entities of the note's project plus 20 most-mentioned shared ones
  (`Known`, one sort per wave), so ids are reused and the prompt stops growing (~2.2k tokens plus the CLI's own ~4.8k).
- **Grounding** (`ground`): an entity survives only if one of its `as` strings occurs in the note; a relation only if
  its quote occurs. Dropped ones are counted (C4).
- **Command mode** (`MEMORY_LLM` set): waves of `-j` parallel calls, one retry for unusable answers; notes ordered by
  project then date, one KNOWN per project (big memories: refreshed at most every 10 waves) so every call of a project
  shares one byte-identical prefix; its length goes to the command in `MEMORY_STATIC_PREFIX`, and `tests/haiku_cmd.py`
  puts that prefix in the system prompt, which `claude -p` caches (−32% per note on the sample, convergence 1.06×).
  Note text is capped at 16k characters. **No model**: nothing is written for a helper and `check` summarises C5 in
  one line; **`--prompts`** writes the prompts to `_dream/pending/` for the `memory-dreamer` subagent and ingests its
  answers on the next dream.
- **Review** (`REVIEW`, one call when due): labels over the bar (`alias T`, `alias ~T`, `new: <definition>`,
  `label`, `drop`), entity pairs (`same` / `different`), conflicts (`a supersedes b`, `compatible`, `unsure`). At most
  40 labels, 30 pairs and 20 conflicts per dream; the code, not the prompt, enforces bar, budget and offered pairs.
- **Cache**: one JSON per content hash in `_dream/notes/<sha12>.json` (the source), mirrored in `store.db`; kept
  30 days after last use so reverted edits cost nothing.
- **Outputs**: `index.db` (always), `memory/DIGEST.md` (≤ 40 lines: how to ask, `prefs/me-*`, the ten newest live
  decisions and models, up to eight open questions; import it from CLAUDE.md with `@memory/DIGEST.md`), plus `graph.json` + `graph.html` up to
  `MEMORY_WIDE` (10,000) notes, or an overview `graph.html` and `viz/<area>.html` pages past it. A dream with nothing
  new (same hashes, vocabulary and script hash, no review due, every extraction file and the digest present) stops
  after the scan; a changed `memory.py` rebuilds the graph once with 0 calls.

#### 5.7 Answering (`ask`)

Per question:
1. **Terms** (`qterms`): ids and numbers kept whole (weight 3 / 1.5), words stemmed to prefixes, word pairs
   (1.5), a few synonyms (own → owner, depend → uses …). Stop words removed.
2. **Intent**: current, down ("what came of"), up ("based on"), why, dep ("depends on"), task ("make / build /
   draft …", "how should I present …").
3. **Names from the index, conservatively**: only ids the question names (≤ 2 entities per name) and 2–3-word
   entity names spelled out in the question are expanded to their aliases.
4. **Scope**: a folder name in the question (`"in churn-2026"`) or `-p` limits the search to that area.
5. **Routing** (only past `MEMORY_WIDE` notes): the named area; else areas whose note ids and titles match
   (idf-weighted, ≤ 8, a hint when many tie), the areas the index says mention the question's ids, named notes'
   areas, and the general areas; one grep over everything only for ids nothing else places.
6. **One `grep -rniIF` per group of questions sharing areas**; hits kept only where a pattern starts a word.
7. **Rank** (`rank`): idf per pattern (title lines count double, path matches count), named notes first, entity
   mentions boosted (inside the scope or routed areas only), then lineage: successors of superseded notes ("current"),
   children for "what came of", parents two hops for why/based-on; a superseded note never outranks its live
   successor. Up to 8 notes ≥ 20% of the best. For every question, up to 4 relatives of the picked notes (parents, successors,
   children for "what came of") follow as a header plus their `# ` line (gold recall 0.895 → 0.920 for +11%
   characters when triggered by lineage words; for every question +1 point and +7 complete answers for +3%, F9). Weights in the `W` table.
8. **Print**: under `▸ path · kind · date · from … · SUPERSEDED → newer`, the best 2–4 lines per note; whole notes
   when everything picked fits the budget (900 chars per question + 1,500). On a memory of ≤ 200 notes, when the
   whole memory would cost ≤ 1.2× the surgical output, print it all: per-question `▸ path` pointers, then every note
   by area — complete, and no dearer than `cat`. An id, version or number the question names that no note mentions,
   or a plain word found nowhere when the best note covers at most half the question's words, gets a
   `(weak match: 'x' found nowhere …)` line; the rule reads the question's own words, never the index's aliases.
9. **Taste** (task intent only, `taste`): scored inside the general areas so project notes cannot crowd them out; a
   person named in the task, or named inside one of the three best-matching house notes (their meeting's roster,
   their report), brings all their notes; house rules about the artifact asked for (chart, table, deck …) come along;
   `prefs/me-*` always. Up to twelve notes, printed as their `# ` line.
10. **Claude Code's auto memory** (`cc_search`, read-only): the project's auto-memory topic files are grepped once for
    every question; at most three files and two lines each, under `▸ claude-code: <file> · <type> · <date>`.
    `MEMORY.md` is skipped (Claude Code loads it itself). Resolution: `$MEMORY_CC_DIR`, `autoMemoryDirectory` in
    `.claude/settings.local.json` or `~/.claude/settings.json`, else `<config>/projects/<git root sanitised>/memory`.

#### 5.8 Big memories

| piece | what | why |
|---|---|---|
| `_dream/store.db` | note facts by path, extractions by hash | a dream re-reads only what changed (was 75 s of file reads at 168k) |
| `_dream/index.db` | the graph as SQLite (notes, edges, ents, ment, names, rels, checks) | `ask` (`DbView`) loads note rows and reads the rest per question (was a 381 MB JSON parse per call) |
| patch on read | notes changed since the dream are re-read from text (lineage now, entities at the next dream) | no 90 s rebuild inside `ask` |
| viewer split | overview (120 best-linked areas, filterable table, health) + `viz/<area>.html`, redrawn when the area's notes, lineage, entity ids or relations change (`viz/_sig.json`) | one 372 MB page → 2.4 MB + ~110 KB per area |
| `notes_part` reuse | after a review only the vocabulary half is rebuilt | halves the dream when a review applies |

#### 5.8b The graph contract

`.specs/memory-dream/CONTRACT.md` is the authority on every shape `memory.py` writes and reads: the graph (`graph.json`,
`index.db`), the viewer's data island, the extraction cache, `store.db`, the manifest, the warning codes C1–C12 and the
grammar of EDGES.md, ALIASES.md, CONFLICTS.md and DIGEST.md. Every graph carries `schema: 1`; `validate()` checks a
graph against the contract, `memory.py check` prints the result first, and A38 enforces it on the fixture (graph,
`index.db` round trip, island). Build the viewer against the contract, never against the code.

#### 5.9 Viewer (`assets/viz.html`)

Self-contained HTML (no network), written for a person who knows nothing about how the memory works: plain words
everywhere (no file names, ids or codes on the surface — `gbm-model-exp233` reads "GBM Model Exp233",
`evaluated-on` reads "evaluated on", dates are spelt out; raw forms stay in tooltips),
a white page, one black at four strengths for text (.95 .80 .70 .60) and four for rules (.95 .44 .34 .16), one
blue (`#7297C5`, text twin `#446EA6`, a 16% wash) for what is selected and the lit path, eight series colours for
the families (navy, blue, magenta, teal, orange, purple, red, ochre; shapes carry identity as well), status colours
for status only, spacing on 8, a 3px ink rule opening every module, square corners, no shadow at rest, system faces
only (a serif for the page title and the picked note's title). The values are measured from a bank's public site;
nothing of its fonts, icons, marks, wording or markup is used. What is picked pops (no ring) and its lines light up
in the blue with arrowheads and a slow flow toward the newer note. The Selected panel keeps a trail:
Back and Forward through everything looked at (Alt+← / Alt+→).
Data lives in `<script type="application/json" id="data-graph">` (notes with their full text, entities with
mentions, relations with evidence, lineage edges, checks, review queue, conflicts); `memory.py` fills it
(`render_viz`); every top-level element has an id; parts talk through `dp:` events. Three views, the Map first
when the page opens (tab order Map · Timeline · Connections; `#view=time` and `#view=graph` open the others):

- **Time — notes by area and date.** One row per area (projects first, general areas in italics), x = date, each
  note a shape by kind (square decision, diamond finding, triangle model, hexagon dataset or feature, circle
  question; a child kind such as experiment takes its family's shape with a lighter fill) in its family's colour;
  superseded notes hollow and dashed; lineage drawn as curves (built on; dashed = supersedes; faint = refers to).
  Lane labels stay put when the lanes scroll. Hovering a note lights its links; picking one dims everything outside
  two lineage hops and draws its own links in (a 420 ms stroke animation, off under `prefers-reduced-motion`).
  Clicking an area label opens the area's summary.
- **Graph — entities and their relations.** The `Graph` tab: nodes are entities shaped and coloured by family
  (hexagon dataset, triangle model, diamond feature, circle metric or term, square party, rounded square system),
  sized by mentions, dashed when a newer version replaces them; arrows are the relations the notes state, current
  by default (at least one evidence note live; "include history" adds the rest), solid for uses/part-of/owned-by,
  dashed for replaces, dotted for trained/evaluated/measured, faint for labels outside the vocabulary. The layout
  is columns, deterministic: one zone per family (white and light grey by turns, the picked family's on a blue
  wash, each named in a strip above the pane), in the order that puts linked families side by side (every order of
  up to eight families is tried); inside a zone the most connected things stand in the right-hand lane, named,
  the rest in up to three lanes to its left (48 per lane); six sweeps then level each thing with the mean height of
  its neighbours so the curves run short and flat, and the row spacing stretches (16–36 units) to fill the pane's
  height so names read at the fitted zoom. The 400 best-connected entities are shown, and picking any other builds
  its neighbourhood (two hops, ≤ 150). The canvas is a camera: drag the background to pan, wheel or pinch to zoom
  around the cursor, +/−/⌂ buttons, drag a node to place it (its curves follow); names keep their size on screen
  and go when rows are closer than 10 px, except the picked, lit, hovered or magnified ones. A fisheye follows the
  mouse: the node under it grows almost double and those around it a little, fading with distance. Picking dims
  everything beyond two hops (one hop for hubs with > 30 neighbours), washes its zone, names its neighbours and
  centres it when zoomed out or off screen; hovering lights a node's curves and names its neighbours. `#view=graph`
  opens it.
- **Map (v2) — a person writes, what it becomes, who checks it.** The `Map` tab (`#view=map`) is the second
  reading of the same things, built for trust rather than structure, after a public ontology viewer whose idea is
  borrowed (not its look): **the flow** — three columns under "1 · a person writes": *The notes* (how many, how
  many current, how many the assistant read), *What they become* (stated links a note itself declares — built on,
  replaces — tagged STATED; facts the assistant read out of current notes, tagged QUOTES ITS LINE; older facts
  that rest only on replaced notes; things named, and how many have a note of their own), *Who checks it* (pairs
  that may disagree, tagged REVIEWER; links flagged by the house rules, tagged RULES; open questions — question
  notes nothing was built on — tagged OPEN; and "You", linking to Worth checking). Each row carries a status swatch
  in the functional colours: ink for written and stated, blue for extracted, grey for older, red for disputed,
  amber for open, green when a check passes. Picking a note rewrites the flow for that note (its stated links,
  its facts with their line numbers, the things it names, whether a current note clashes with it, whether it
  passes the rules, whether it is an open or answered question); picking a thing rewrites it for the thing (facts
  in current notes, older facts, the ways it is written, odd links). **The graph** — one framed picture captioned
  with its real counts ("400 things of your memory, one graph · uses, measured by, …"): a deterministic force
  layout with a gentle pull toward each family's place on a ring, nodes sized by their links (`2.5 + 1.7√degree`,
  capped), things with a note of their own filled in their family's colour with an ink outline, things only
  mentioned as small ink dots; only the twelve most linked are named at rest, names keep their size on screen,
  hovering names a thing and its neighbours, picking lights its links and dims the rest; drag, wheel and pinch as
  in Connections. **The two tables** below — "What the memory holds" (written, stated, extracted, older, disputed,
  open, each with its count and one sentence) and "What a statement is worth" (what to do with each kind: believe
  the note; follow the author's link; open the quoted line and press Wrong? if it does not say that; read both
  clashing notes; write the note that answers the question).
- **Selected — the note, and what the agent sees.** For a note: its text rendered as markdown in its own box, the
  main thing on the panel (headings, lists, quotes, fenced code, pipe tables, inline code/bold/italic/links; note
  ids and entity ids become links in plain words; built as DOM nodes, never HTML), then "How this note connects"
  shown progressively — the direct links first (Built on, Replaces, Replaced by, Current version, Led to; six per
  row then "and N more"), mentions folded; the five-column family tree is drawn under the big figure, full width,
  not in the panel. The things the note mentions are marked in the text itself, not listed: after rendering, the
  text nodes are merged and every surface form the index knows for each mentioned thing (its id, its plain words,
  the aliases seen; longest first, whole words, any case; code, links and chips already placed are skipped) becomes
  a square chip with the family's colour in its corner, which opens the thing; a token that is both a thing and a
  note is the thing. Anything the index says is mentioned but the text did not yield (typically a mention in the
  title) is named once in an "Also about" line under the text, so nothing is missed. The one action, "Something
  wrong?", sits at the right of the box in ink. Then what the assistant took from it (five facts, then "Show N
  more"), what it may disagree with, and what is worth a look. There is no technical block: the raw `▸ path · kind
  · date` header and the numbered lines that `ask` prints stay off the page. For an entity: how it is written, headline and
  home note, typed relations, labels, every note that mentions it. For an area: counts by kind, superseded → current
  chains, conflicts, warnings, notes newest first.
- **Legends** are two rows of toggles, nodes then edges: each entry (a kind or family; a lineage kind or a relation
  type) shows or hides what it names; hidden entries are struck through. Edges whose end is hidden hide too.
- **Worth checking** (a section, not a hidden panel): what may be wrong, in plain words, each with a "Copy question"
  button that puts a ready question for the assistant on the clipboard — notes that may disagree (the conflict
  queue), names that may be the same thing (the entity review queue), links that look odd (C12), links that lead
  nowhere (C1, C2), notes on their own (no lineage in or out, project areas only, daily logs excluded), other
  things to look at (C3, C6, C8, C9, C11). Six items per list, then "Show all N" — no inner scrollbars. A picked
  note has the same button ("Something wrong here?") and every extracted fact has a "Wrong?" button whose question
  quotes the line. The header counts the items. Older versions and what replaced them sit folded under it.
- **Fuzzy search** (fzf-style subsequence scoring with word-start and run bonuses; exact substrings win) over title,
  id, text and entity names; the best 20 listed with matched letters marked, every match kept in the lanes while the
  rest fade (in the graph view, the entities those notes mention light up); `/` focuses, arrows and Enter pick, Esc
  clears.
- **Health** (collapsed): warnings by code, superseded → current, unlinked notes, the review queue (pairs, labels
  over the bar, conflicts). Deep links: `#note=`, `#entity=`, `#area=`, `#q=`, `#health`.
- **Modes**: whole memory; `area` (one page per area past `MEMORY_WIDE`, with "← all areas"); `overview` (one card per
  area with a kind bar, linking to its page). Measured: the 1,677-note bank renders in 0.9 s from a 2.6 MB page with
  1,524 notes and 3,680 links drawn; its graph view lays out 400 entities and 1,355 current relations in 1.3 s;
  0 console errors on the bank and the fixture, headless (Playwright: `tests/viz_check.js`).

---

### 6. Tests

```bash
python3 tests/acceptance.py            # A1–A20, A24, A25–A37 with the fake dreamer, about 25 s
python3 tests/acceptance.py A6 A24     # some
python3 tests/real_model.py            # Haiku on the fixture vs tests/truth.py (costs a few cents)
```

The fixture (`tests/fixture/memory`, from `tests/make_fixture.py`) is a churn project with a planted leak story:
exp-014 → churn-xgb-v2 (AUC 0.81) → leak hypothesis → exp-017 → churn-xgb-v3 (0.76) supersedes v2. Highlights:
A3 incremental (a second dream costs 0 calls), A6 entity headlines move to the newest note and broken links warn
(C2), A8 grounding (fabricated surface forms and absent quotes dropped), A12 an unknown relation type is held back
until the review maps it (0 extraction calls), A14 vocabulary edits by hand (0 calls), A15 dedup (case fold and the
surface rule for free, versions never asked, one review line in ALIASES.md), A19 1,000-note speed, A20 entity keep
rules, A24 big-memory routing, patching and per-area page redraws, A25 whole-memory print on small memories, A26 a
plain-word project name scopes the search, A27 NUL-byte notes (C9, still grepped), A28 the weak-match marker, A29
two-hop taste (the task names the deck, the roster names the person), A30 kinds and general areas with no model, A31
Claude Code's auto memory read and never written, A32 the digest, A33 Claude Code's frontmatter convention, A34 the
promotion gate and packs, A35 probation and demotion, A36 the budget, A37 conflicts (queued, decided, recorded, never
re-asked), A38 the graph contract (validation, `index.db` round trip, the viewer's island, C11, version and same-title
conflict candidates, open questions in the digest). Results are written to `tests/acceptance.json`.

---

### 7. Reproduce the evaluations

#### 7.1 The 56× bank (1,677 notes) and its questions

The bank was written by Haiku subagents, one bundle per project or general area, each bundle = notes + questions
with gold notes and reference answers (lookup, lineage, dependency, current, why, numeric, correction, term …).

```bash
python3 eval/bank/split.py <bundles dir> eval/bank/generated eval/questions     # bundles → notes + questions
python3 eval/bank/assemble.py eval/bank/generated tests/fixture/memory <W>/memory # bank + churn-2026
MEMORY_LLM="python3 tests/haiku_cmd.py" DREAM_COST_LOG=<W>/cost.jsonl \
  python3 skills/memory-dream/scripts/memory.py --root <W>/memory dream -j 10      # index: ~$3.3, ~25 min
```

#### 7.2 Offline retrieval (no LLM)

```bash
python3 eval/retrieval.py <W>/memory eval/questions/bank-*.jsonl        # gold-note recall, number recall, chars
python3 eval/retrieval.py <W>/memory eval/questions/bank-*.jsonl --must # superseded gold notes count as history
MEMORY_WIDE=100 python3 eval/retrieval.py <W>/memory eval/questions/bank-*.jsonl   # force big-memory routing
python3 eval/adversarial.py <W>/memory eval/questions/bank-*.jsonl --index-world <real-indexed world> --show
```
Expect 0.937 / 0.980 at 1,677 notes on the fake-indexed world (0.895 / 0.972 before the lineage one-liners;
0.946 / 0.978 on a real Haiku index, 0.938 / 0.979 with `MEMORY_NO_INDEX=1`). `adversarial.py` measures the sets
where grep should lose: stale-vs-current (successor above the old note 0.97, old marked 1.00), scattered
evidence (all gold 0.78 at 2.2k chars on the fake index, 0.79 at 2.3k on the real one, vs 0.99 at 12.6k for `cat`
of the folder), absence (70 questions about things the memory does not hold: ask says "(no match" or marks
the unknown id or word, 70 of 70), alias traps (needs a real index for its surface
forms: 0.93 with or without the index vs 0.43 for an exact-phrase grep on the 70-note world's 14 forms; the full
bank's 280 forms: 0.89 with the index, 0.83 without, 0.52 grep). `MEMORY_NO_INDEX=1` switches `ask`'s use of the index off, for such comparisons.

#### 7.3 Agent eval (Opus subagents, memory vs grep)

Workspaces: `<A>/X-mem` = memory (with `_dream/`) + `skills/memory-dream`; `<A>/X-grep` = notes only. Batches:
`python3 eval/agent/make_batches.py` → `eval/agent/batches/{P1,P2,C-orig,…}.jsonl` (10 questions each).

Memory-arm prompt (grep arm identical except the middle paragraph):

```
You are answering questions about a data-science team's past work. Work only inside <A>/X-mem — do not read or
search anything outside it.
The team's memory is in <A>/X-mem/memory/. You have this skill:
  memory-dream: <the description line of SKILL.md, with the script path written out and --root <A>/X-mem/memory>
  (Full instructions, if you need them: <A>/X-mem/skills/memory-dream/SKILL.md)
This is a read-only task: do not write or edit notes and do not run `dream` or `log`.
Answer these 10 questions:
Q1 …
Reply in exactly this format, nothing else:
## Q1
<answer in 1–4 sentences with the key numbers>
Sources: <note paths>
```
Grep arm middle paragraph: "The team's notes are markdown files under <A>/X-grep/memory/ (one folder per project,
plus prefs/, reporting/, glossary/, corrections/, howto/ and qa/; … the `# ` line states the point; frontmatter
`from:` … `supersedes:` …). Find what you need with grep, find, ls and cat via Bash, or with Read."

Then:
```bash
python3 eval/a21/extract.py eval/agent/runs NAME=<subagent transcript.jsonl> … > eval/agent/usage-X.jsonl
python3 eval/judge.py eval/agent/batches/P1.jsonl eval/agent/runs/X-mem-P1.md > eval/agent/judge-X-mem-P1.json
python3 eval/agent/summarize.py     # accuracy, tool calls, tokens, cost units (Opus price ratios), seconds
```
Cost units weight tokens as fresh input 1, cache read 0.1, cache write 1.25, output 5.

#### 7.4 What a note costs

`tests/haiku_cmd.py` logs `total_cost_usd` and tokens per call when `DREAM_COST_LOG` is set (never quote prices
from memory). `python3 eval/prompt_breakdown.py <memory>` splits a prompt into template, EDGES, KNOWN and note.

#### 7.5 100× (168,141 notes)

```bash
python3 eval/scale/make_world.py <W>/memory <X>/memory --copies 137   # sibling copies, already indexed
python3 eval/scale/bootstrap.py <X>/memory                            # first dream (~100 s, fills store.db)
python3 eval/scale/time_ask.py <W>/memory <X>/memory                  # seconds and chars per batch
python3 eval/scale/trace_ask.py <X>/memory P2                         # where one ask spends its time
python3 eval/scale/profile_dream.py <X>/memory                        # a full rebuild, profiled
python3 eval/scale/profile_incremental.py <X>/memory <scratch> fraud-2026   # re-index one area, fake dreamer
```
Copies get project-local ids renamed (`exp-014` → `exp-xab-014`) and every number shifted, so they read like
sibling projects with different facts; general areas stay 1×.

#### 7.6 Taste (preferences applied to tasks)

```bash
python3 eval/taste/make_tasks.py <W>/memory eval/taste/tasks.jsonl    # Haiku: 4 tasks per person, gold notes
python3 eval/taste/score.py <W>/memory eval/taste/tasks.jsonl --misses # person-preference and house-rule recall
python3 eval/taste/make_batches.py                                     # T1 named, T2 implicit (agent eval)
python3 eval/taste/judge.py <W>/memory eval/taste/batches/T1.jsonl eval/taste/runs/T-mem-T1.md > eval/taste/judge-T-mem-T1.json
python3 eval/taste/summarize.py
```
Agents get the tasks and list the choices the notes support ("do not produce the artifacts"); the judge counts
which applicable notes each plan follows by content, and which it contradicts.

---

### 8. Results to expect

| measure | 30 notes | 1,677 | 168,141 |
|---|---|---|---|
| retrieval: gold notes / numbers | — | 0.882 / 0.970 | 0.854 / 0.950 |
| `ask`, 10 questions | < 1 s | 0.5 s | 2.3 s |
| agent cost vs grep | 0.93× | 0.47× (phase G, real index, n = 3 batches per arm: tool calls 0.30×, tokens 0.29×, cost units 0.61×, time 0.75×, accuracy tied 23/7/0) | 0.41× |
| $ per new note (Haiku) | 0.0013 (60-note world) | 0.0020 | 0.0015–0.0019 |
| dream, nothing new | — | 0.7 s | 3 s |
| dream, 30 new notes (with Haiku) | — | — | 82 s, 4.8 GB |
| viewer | 1 page | 2.9 MB | 2.4 MB overview + ~110 KB per area |

Taste retrieval (fresh tasks, recall of the gold notes): the person's preferences 0.93 when the task names them,
0.57 when it names only their meeting or audience; house rules 0.42 (before the taste layer: 0.76 / 0.35 / 0.25).

---

### 9. Pitfalls met on the way (and what fixed them)

| symptom | cause | fix |
|---|---|---|
| index-first agent cost 2.3× grep | round trips re-send ~37k tokens each | one `ask` call for every question |
| graph answers not "surgical" | whole notes and entity cards | print the answering lines under a lineage header |
| big bank retrieval worse with the index | loose Haiku names expanded every question | expand only ids named and 2–3-word names spelled out |
| 508 relation types | open vocabulary | closed 8 types, review may only alias or drop |
| review mapping everything | permissive prompt | "when unsure, drop / different" |
| `ask` 52–135 s at 168k | one grep over everything (37 s, 502k lines) | route to areas past 10,000 notes |
| copies crowded out the gold note | entity boosts ignored the named project | boosts stay inside scope or routed areas |
| dream 202 s / 8.2 GB | re-read everything, wrote 380 MB JSON + 372 MB HTML | store.db, index.db, per-area pages, stop when nothing is new |
| a review redrew 5,624 pages | page fingerprint included the vocabulary and hub spellings | fingerprint area notes, lineage, entity ids, relations |
| KNOWN prompt prep took days at 168k | a full entity sort per note | one sort per wave (`Known`) |
| taste missed unless the person was named | grep on task words; project notes outranked preferences | taste block scored inside the general areas, whole person, artifact rules |
| dreamer could not list files | no Glob tool in that CLI | `pending/TODO.md` lists the prompts |
| viewer checks failed | dangling playwright symlink | `npm i -g playwright && npx playwright install chromium` |

---

### 10. Known limits and next steps

- **Taste is mostly not written down.** It arrives as corrections in conversation; the memory only knows what an
  agent saved (SKILL.md now says to save it at once). The write side has not been measured with agents.
- **Implicit audiences** (a task names the meeting, not the person) still miss ~40% of the person's preferences:
  the link from meeting to person exists only inside the notes' text.
- **A dream holds the whole graph in memory** (4.8 GB at 168k notes) and `_dream/` takes ~2.2 GB on disk at that size.
- **Synthetic data.** Notes and questions were written by Haiku; real notes from people over months are untested.


<--->

## Appendix D — prompts, seeds and tuned tables, verbatim from `memory.py`

_Part 8 · extracted at commit 6ee2bae by importing the script. The dreamer's two prompts, the seed vocabulary (`EDGES.md`), the packs for other domains, the headers of the user-owned files, and every tuned number with its name. A rebuild reproduces these exactly; the measurements in RESULTS.md set them._

### D.1 `EXTRACT` — the per-note prompt (the static part is cached; `EDGES:` and `KNOWN:` follow, then `NOTE`)

```
Index this memory note for retrieval. Reply with JSON only:
{"kind": "question|experiment|finding|decision|dataset|feature|model|metric|term|preference|rule|log|note",
 "entities": [{"id": "...", "type": "dataset|feature|model|metric|segment|person|team|term|tool",
               "as": ["text copied verbatim from the note"]}],
 "relations": [{"s": "entity id", "type": "an EDGES type or alias, or other", "label": "the note's own verb, 1-3 words",
                "o": "entity id", "quote": "short text copied verbatim from the note that states it"}],
 "refs": ["ids or paths of other notes the text explicitly points to"]}
Entities are things someone would look up across notes: tables, features, models, metrics, segments,
people, teams, defined terms. Not columns, files, notebooks, numbers, or note ids (those go in refs).
If an entity is in KNOWN, reuse its id. Otherwise id = its most specific name, lowercase, spaces to
hyphens; a table keeps its dots (cards.txn_daily).
Relations: only ones the note states, read "s <type> o". Use an EDGES type or one of its aliases
(aliases marked ~ read in reverse) and always give the label. If no type fits a real link between two
things, type is other: the label is kept and shown, and becomes a type once it is common.
EDGES:
{edges}
KNOWN:
{known}
NOTE {path}:
{text}
```

### D.2 `REVIEW` — the one-call review (entity pairs, labels over the bar, conflicts)

```
You keep the vocabulary of a data-science memory.
RELATION TYPES, read "X <type> Y" ({n} of {budget} slots used):
{edges}
LABELS the indexer used that fit no type, each over the bar of {u} uses in {nn} notes across {a} areas
(uses, notes, areas; up to 3 examples "X — Y: quote"):
{proposals}
ENTITY PAIRS that may name the same thing (id, type, surface forms, one context line each):
{pairs}
LIVE NOTES of one kind in one area that may disagree (path · "title" «first line»; neither supersedes the other):
{conflicts}
Reply with JSON only:
{"types": {"<label>": "alias T" | "alias ~T" | "new: <one line: what the link means and how it differs from the closest type>" | "label" | "drop"},
 "entities": {"<a> / <b>": "same" | "different"},
 "conflicts": {"<a> / <b>": "<a> supersedes <b>" | "<b> supersedes <a>" | "compatible" | "unsure"}}
Map a label onto T when it names the same link as T, as a synonym ("alias T") or read in reverse
("alias ~T"). Answer "new: …" only for a link between two things that no listed type expresses and that
the notes will keep using; name the closest type and the difference. Answer "label" to keep it as a plain
label. Drop only what links notes rather than things (answers, led-to, basis-for) or is a conversation
(asked-by, raised-by). When unsure between alias and new, alias; when unsure between new and drop, label.
If unsure whether two entities are the same thing, answer different. Versions (v2, v3) are different.
Two notes: the newer one supersedes the older when it decides or states the same thing differently (a new
cutoff, a newer model as the current one); they are compatible when they are about different things or
one builds on the other; otherwise unsure. Never invent paths: copy them from the pair.
```

### D.3 `EDGES_SEED` — `memory/EDGES.md` as first written (software pack)

```markdown
# EDGES — relation types between entities, read "X <type> Y". Constrained open: the dreamer uses these types and
# their aliases (~ = read in reverse); any other link it finds keeps its own label and is shown as other/<label>.
# A label becomes a type only over the bar below, through the review, within the budget; a type marked
# (proposed <date>) is demoted back to a label if it is still under the bar after the probation. Edit freely: a
# hand-written line is permanent and relabels everything at the next merge (0 calls). Optional: pack: software, research, ops.
# Note-to-note links (from:, supersedes:, refs) are lineage, not relations.
promote: 5 uses, 5 notes, 2 areas
budget: 24
probation: 60 days
- uses: X needs Y as an input (model uses feature; feature uses table) | aka: depends-on, consumes, built-on, built-from, derived-from, based-on, sourced-from, requires, reads, reads-from, joined-to, ~feeds, ~input-to, ~used-by, ~used-for, ~used-in
- produces: X creates or writes Y (job produces table; model produces scores) | aka: writes, writes-to, creates, outputs, generates, ~generated-by, ~produced-by, ~output-of
- part-of: X is a component of Y (column part-of table; feature part-of feature-set) | aka: member-of, column-of, subset-of, stored-in, ~contains, ~has, ~includes
- trained-on: model X was fit on dataset Y | aka: fit-on, fitted-on, trained-with
- evaluated-on: X was measured on dataset or segment Y | aka: tested-on, validated-on, measured-on, scored-on, backtested-on
- measured-by: X is judged by metric Y | aka: reports, reports-metric, has-metric, measures, measured-in, scored-by, optimizes, optimises, targets, ~metric-of
- replaces: X is the newer version of Y | aka: supersedes, retires, ~replaced-by, ~superseded-by
- owned-by: X is maintained or decided by person or team Y | aka: maintained-by, managed-by, run-by, approved-by, decided-by, set-by, signed-off-by, agreed-by, ~owns, ~maintains
drop: related-to, associated-with, about, mentions, relates-to, answers, answered-by, basis-for, evidence-for, led-to, leads-to, motivates, motivated-by, informs, follows, confirms, explains, supports, overturned-by
```

### D.4 `PACKS` — seed types for other domains (`pack: research|ops` in EDGES.md)

```json
{
 "software": "- calls: X invokes Y (service calls API; function calls function) | aka: invokes, requests, queries, ~called-by, ~serves\n- implements: X realises Y (module implements interface; service implements spec) | aka: realises, realizes, satisfies, ~implemented-by, ~specified-by\n- deployed-to: X runs in Y (service deployed-to cluster) | aka: runs-on, runs-in, hosted-on, ~hosts\n- configures: X sets Y's behaviour (flag configures service; file configures job) | aka: sets, parameterises, parameterizes, ~configured-by\n- tested-by: X is checked by Y (module tested-by suite) | aka: covered-by, verified-by, ~tests, ~covers, ~verifies\n- blocked-by: X waits on Y (release blocked-by bug) | aka: waits-on, ~blocks",
 "research": "- cites: X refers to Y as a source (paper cites paper; note cites report) | aka: references, quotes, ~cited-by\n- extends: X builds on Y's method or result (model extends baseline) | aka: generalises, generalizes, refines, ~extended-by\n- contradicts: X's result disagrees with Y's | aka: disagrees-with, refutes, ~contradicted-by\n- reproduces: X repeats Y's result | aka: replicates, ~reproduced-by",
 "ops": "- alerts-on: X raises an alert on Y (monitor alerts-on metric) | aka: monitors, watches, pages-on, ~monitored-by\n- runs-after: X is scheduled after Y (job runs-after job) | aka: scheduled-after, ~runs-before, ~precedes\n- escalates-to: X hands off to Y (queue escalates-to team) | aka: hands-off-to, ~escalated-from\n- rolled-back-to: X reverted to Y (release rolled-back-to version) | aka: reverted-to, ~rolled-back-from"
}
```

### D.5 Headers of `ALIASES.md` and `CONFLICTS.md`

```markdown
# ALIASES — entity ids that name the same thing; the first id on a line is canonical. Edit freely.
```

```markdown
# CONFLICTS — decisions about pairs of live notes that looked contradictory. `- a > b`: a supersedes b (lineage from then on; the notes are untouched). `compatible: a / b`: both stand. `- a ? b`: the reviewer was unsure; a person decides. Edit freely.
```

### D.6 Tuned tables and constants (`W` is `rank`/`route`; the rest are named where they are used)

```json
{
 "PREFIX_KIND": {
  "exp": "experiment",
  "feat": "feature",
  "ds": "dataset",
  "dec": "decision",
  "fnd": "finding",
  "find": "finding",
  "finding": "finding",
  "q": "question",
  "metric": "metric",
  "model": "model",
  "pref": "preference",
  "rule": "rule",
  "term": "term"
 },
 "AREA_KIND": {
  "prefs": "preference",
  "glossary": "term",
  "corrections": "correction",
  "reporting": "rule",
  "howto": "rule",
  "log": "log"
 },
 "CC_KIND": {
  "user": "preference",
  "feedback": "rule",
  "project": "note",
  "reference": "note"
 },
 "KIND_PARENT": {
  "experiment": "finding",
  "correction": "rule",
  "preference": "rule",
  "metric": "term"
 },
 "TYPE_PARENT": {
  "table": "dataset",
  "segment": "dataset",
  "column": "feature",
  "person": "party",
  "team": "party",
  "tool": "system",
  "job": "system",
  "pipeline": "system",
  "service": "system"
 },
 "SHAPES": {
  "trained-on": [
   "model",
   "dataset"
  ],
  "evaluated-on": [
   null,
   "dataset"
  ],
  "measured-by": [
   null,
   "metric"
  ],
  "owned-by": [
   null,
   "party"
  ],
  "replaces": [
   "same",
   "same"
  ]
 },
 "CONFLICT_KINDS": [
  "decision",
  "finding",
  "model"
 ],
 "CONFLICT_STOP": [
  "current",
  "decision",
  "finding",
  "from",
  "holdout",
  "model",
  "note",
  "rule",
  "that",
  "this",
  "threshold",
  "using",
  "what",
  "when",
  "with"
 ],
 "GENERAL": [
  "corrections",
  "glossary",
  "howto",
  "log",
  "people",
  "prefs",
  "qa",
  "reporting"
 ],
 "W": {
  "entity_named": 0.25,
  "successor_current": 1.1,
  "successor": 0.85,
  "superseded_current": 0.85,
  "why_parent": 0.6,
  "down_intent": 0.7,
  "down_named": 0.5,
  "up_hop": 0.6,
  "seeds": 6,
  "picks": 8,
  "pick_floor": 0.2,
  "lines_top": 4,
  "lines_rest": 2,
  "route_common": 50,
  "route_near": 0.9,
  "route_areas": 8,
  "route_floor": 0.6,
  "lineage_lines": 4
 },
 "PROMOTE": [
  5,
  5,
  2
 ],
 "BUDGET": 24,
 "PROBATION_DAYS": 60,
 "COMPLETE_MAX_NOTES": 200,
 "COMPLETE_RATIO": 1.2,
 "WEAK_SHARE": 0.5,
 "TASTE_MAX": 12,
 "TASTE_FLOOR": 0.15,
 "NOTE_CAP": 16000,
 "NOTE_MAX_LINES": 40,
 "WIDE": 10000,
 "CONFLICT_MAX": 20,
 "DIGEST_MAX_LINES": 40,
 "DIGEST_HEADS": 10,
 "SCHEMA": 1,
 "V": "0.4"
}
```

<--->

## Appendix E — evaluation record formats

_Part 9 · the shapes `eval/` reads and writes, so a rebuilt eval can be compared line for line with the reference._

- **Question** (`eval/questions/*.jsonl`, one JSON object per line): `type` (lookup · lineage · dependency · current ·
  numeric · why · preference · reporting · term · correction · howto · qa), `q` (the question), `a` (the reference
  answer the judge grades against), `notes` (gold note paths; with `--must` the superseded ones count as history),
  `bundle` (the area or question file it came from), optional `nums` (numbers the answer must contain).
- **Taste task** (`eval/taste/tasks.jsonl`): `type` (taste-named · taste-implicit), `q` (the task), `a` (empty),
  `notes` (the preference and rule notes that should come along).
- **Batch** (`eval/agent/batches/<name>.jsonl`): ten question lines, made by `eval/agent/make_batches.py` (seeded).
- **Agent answer file** (`eval/agent/runs/<cell>-<arm>-<batch>.md`): sections `## Q1` … `## Q10`, each an answer,
  a `Sources:` line and `Tool calls for this question: n`; last lines `Total tool calls in this task: n` and
  `Minutes spent: n`.
- **Judge** (`eval/judge.py <batch> <answers.md>` → `eval/agent/judge-<cell>-<arm>-<batch>.json`):
  `{"<answers.md>": {"correct": n, "partial": n, "wrong": n, "verdicts": {"Q1": {"v": "correct|partial|wrong", "why": "…"}}}}`.
- **Usage** (`eval/a21/extract.py <out_dir> name=<transcript.jsonl>` → one line in `eval/agent/usage-<cell>.jsonl`):
  `{"run", "tool_calls", "requests", "input", "cache_read", "cache_write", "output", "total"}`; cost units weight
  fresh input 1, cache read 0.1, cache write 1.25, output 5.
- **Harness** (`eval/agent/harness.json`): `{"<run>": {"tokens", "tool_uses", "ms"}}` from the subagent notifications.
- **Summary** (`eval/agent/summarize.py` → `summary.json`): per cell `runs, questions, correct, partial, wrong,
  tool_calls, requests, processed_tokens, cost_units, secs`, and `<size>-mem/grep` ratios.
- **Retrieval** (`eval/retrieval.py <memory> <questions…> [--must]`): one JSON line `{"questions", "note_recall",
  "num_recall", "precision", "full_note_hit", "chars_per_batch", "chars_per_q", "secs_per_batch"}` after the
  `  miss …` lines. **Adversarial** (`eval/adversarial.py <memory> <questions…> [--index-world <root>]`): JSON with
  `stale`, `scatter`, `absence` and, with an index world, `alias`.
- **Dreamer cost log** (`DREAM_COST_LOG=<file>` with `tests/haiku_cmd.py`): one JSON line per call `{"kind":
  "extract|review", "cost", "ms", "in", "fresh", "cached", "cache_write", "out", "static", "error"}`.
