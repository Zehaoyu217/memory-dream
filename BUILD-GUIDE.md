# memory-dream — build guide

How to rebuild the memory-dream skill from scratch, install it, and reproduce every measurement behind it.
Everything here is in this repository (`Zehaoyu217/memory-dream`, branch `worktree-build-v0.4`); file paths are
relative to its root. Results quoted are from `.specs/memory-dream/RESULTS.md`.

---

## 0. What you are building

A project memory for coding and data-science agents:

- **Notes are the truth.** Plain markdown in `memory/<area>/<slug>.md`, one note per thing (question, experiment,
  finding, decision, dataset, feature, model, preference, rule, term, correction). Agents read them with grep and Read.
- **`memory.py ask "q1" "q2" …` answers every question in one call**: grep plus a thin layer of lineage
  (`from:` / `supersedes:`), names (aliases from the index), current-first ranking and surgical line output.
- **`memory.py dream`** (end of session) has a cheap model, Haiku, index new notes into entities and typed relations,
  dedups them, keeps a closed relation vocabulary, and writes the viewer (`_dream/graph.html`).
- One stdlib Python file (`skills/memory-dream/scripts/memory.py`, ~1,900 lines), one HTML template, one SKILL.md.

What it measures against a grep-only Opus agent (same questions, Haiku judge):

| memory size | accuracy (memory vs grep) | cost | time |
|---|---|---|---|
| 30 notes | 26/3/1 vs 25/5/0 | 0.93× | 0.75× |
| 1,677 notes | 27/3/0 vs 26/4/0 | 0.47× | 0.35× |
| 168,141 notes | 24/6/0 vs 24/6/0 | 0.41× | 0.42× |

Saving a note costs about $0.0015–0.002 of Haiku at any size. A dream with nothing new takes 3 s at 168k notes.

---

## 1. Prerequisites

| need | for | notes |
|---|---|---|
| a shell | any agent: Claude Code, Claude through the API with a shell tool, other LLM agents, people | the skill is instructions plus one script |
| Python ≥ 3.9 | everything | stdlib only (sqlite3, json, re, subprocess) |
| `grep` | `ask` | BSD or GNU; Python fallback if missing |
| Claude Code CLI (`claude`) | the Haiku dreamer, agent evals, Haiku judges | `claude -p --model haiku …` headless |
| node + playwright + chromium | optional: rendering checks of the viewer | `npm i -g playwright && npx playwright install chromium` |

---

## 2. Install it in a project (5 minutes)

```bash
git clone https://github.com/Zehaoyu217/memory-dream.git && cd memory-dream && git checkout worktree-build-v0.4
python3 tests/acceptance.py                         # 21/21 should pass

# the skill and the dreamer subagent, user-wide
mkdir -p ~/.claude/skills ~/.claude/agents
cp -R skills/memory-dream ~/.claude/skills/
cp skills/memory-dream/agents/memory-dreamer.md ~/.claude/agents/

# in your project
cd /path/to/project && mkdir -p memory && echo "memory/_dream/" >> .gitignore
export MEMORY_LLM='claude -p --model haiku --tools "" --setting-sources "" --strict-mcp-config --no-session-persistence'
python3 ~/.claude/skills/memory-dream/scripts/memory.py dream      # seeds EDGES.md, ALIASES.md, DIGEST.md, _dream/
echo '@memory/DIGEST.md' >> CLAUDE.md                              # Claude Code: the digest in context every session
```

Beside Claude Code's own memory (CLAUDE.md, auto memory under `~/.claude/projects/<project>/memory/`): `ask` reads the
auto-memory topic files in the same call and never writes there; `dream`, `log` and `viz` refuse such a root. Any other
agent with a shell uses the same three steps SKILL.md gives: read once, write as you go, dream at the end.

Daily use (what SKILL.md tells the agent):

```bash
M="python3 ~/.claude/skills/memory-dream/scripts/memory.py"
$M ask "what came of exp-014?" "Make the Q4 campaign chart for Chloe Martin's readout"   # one call, all questions/tasks
$M log "velocity v2 leaks past the observation date" -p churn-2026                      # scratch line
$M dream            # end of session: index new notes (Haiku), dedup, viewer
$M check            # warnings in full;  $M viz → _dream/graph.html
```

Without `MEMORY_LLM`, `dream` builds everything that needs no model (lineage, kinds, conflicts, digest, viewer,
index) and stays quiet about entities. To add them without a model command: `dream --prompts` writes prompts to
`memory/_dream/pending/` and lists them in `TODO.md`; run the `memory-dreamer` subagent (Haiku) on them, then
`dream --prompts` again.

---

## 3. The design in one page

1. **Thin layer on grep.** Agents are good at grep and Read; the tool enhances them, never replaces them. Every
   change is benchmarked against a grep-only agent on the same questions.
2. **One call.** Round 1 lost to grep (2.3× cost) because of round trips: every request re-sends ~37k tokens of
   context. `ask` takes every question at once and prints only the lines that answer.
3. **Lineage is written by the author, not inferred.** `from:` (built on) and `supersedes:` (overturns) in
   frontmatter; a superseded note is shown as history with its successor.
4. **The index is optional for answering** (measured: neutral for accuracy) and earns its keep for aliases,
   dedup, the viewer and management. It must stay cheap and conservative: loose names hurt retrieval.
5. **Constrained open relation vocabulary.** Eight types; any other link keeps its label (`other/<label>`), and a
   label becomes a type only over an evidence bar, through the review, within a budget, on probation.
6. **Scale by routing, not by heavier machinery.** Past 10,000 notes, `ask` greps only where a question points,
   reads an SQLite index row by row, and the viewer splits into an overview plus one page per area.

---

## 4. Repository layout

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

## 5. Build it step by step

Build in this order; each step is testable on the fixture before the next.

### 5.1 Notes and SKILL.md

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

### 5.2 Scan and manifest (`scan`)

Walk `memory/` with `os.walk` (skip `_dream/`, dot dirs, `EDGES.md`, `ALIASES.md`, `README.md`, `INDEX.md`).
Keep `{path: {sha256, mtime_ns, size}}` in `_dream/manifest.json`; re-hash only files whose mtime or size changed.
A path that disappeared while the same hash appeared at exactly one new path is a move (`former` keeps old paths so
old references still resolve).

### 5.3 Note facts (`parse_note`, `note_facts`)

From each note's text: frontmatter (`from`, `supersedes`, `type`, `updated`), the `# ` title and its line, `[[links]]`
outside code, and every slug-like token in the body (`[a-z][a-z0-9]*(-[a-z0-9]+)+`). Cached per path and content
hash in `_dream/store.db` so a dream re-reads only changed notes.

### 5.4 The graph, note half (`notes_part`)

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
  (binary-looking), C10 conflict pending.

### 5.5 The graph, vocabulary half (`build`, `merge_entities`)

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
Conflicts: live notes of one kind (decision, model, finding) in one area, unlinked, sharing an id-like title token or
two rare words, are queued (C10, 20 per review); verdicts persist in `memory/CONFLICTS.md` (`- a > b` becomes lineage,
`compatible: a / b`, `- a ? b`); notes are never edited.

The seed vocabulary (8 types): `uses`, `produces`, `part-of`, `trained-on`, `evaluated-on`, `measured-by`,
`replaces`, `owned-by` (full alias lists in `EDGES_SEED`). Evidence: 81% of 5,196 extracted links fit them and 365 of
366 questions need lineage, a single note, or one of the 8 (`eval/type_coverage.py`, `eval/question_relations.py`);
with Haiku on 70 notes the two-tier prompt gives 81% typed, 19% labels, 0 invented types (RESULTS "Phase C").

Review candidates: new entities of the same type that share a rare surface form or have similar folded ids
(difflib ≥ 0.85); pairs with two different home notes are never queued.

### 5.6 The dreamer (`dream`)

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
- **Command mode** (`MEMORY_LLM` set): waves of `-j` parallel calls, one retry for unusable answers.
  **No model**: nothing is written for a helper and `check` summarises C5 in one line; **`--prompts`** writes the
  prompts to `_dream/pending/` for the `memory-dreamer` subagent and ingests its answers on the next dream.
- **Review** (`REVIEW`, one call when due): labels over the bar (`alias T`, `alias ~T`, `new: <definition>`,
  `label`, `drop`), entity pairs (`same` / `different`), conflicts (`a supersedes b`, `compatible`, `unsure`). At most
  40 labels, 30 pairs and 20 conflicts per dream; the code, not the prompt, enforces bar, budget and offered pairs.
- **Cache**: one JSON per content hash in `_dream/notes/<sha12>.json` (the source), mirrored in `store.db`; kept
  30 days after last use so reverted edits cost nothing.
- **Outputs**: `index.db` (always), `memory/DIGEST.md` (≤ 40 lines: how to ask, `prefs/me-*`, the ten newest live
  decisions and models; import it from CLAUDE.md with `@memory/DIGEST.md`), plus `graph.json` + `graph.html` up to
  `MEMORY_WIDE` (10,000) notes, or an overview `graph.html` and `viz/<area>.html` pages past it. A dream with nothing
  new (same hashes, vocabulary and script hash, no review due, every extraction file and the digest present) stops
  after the scan; a changed `memory.py` rebuilds the graph once with 0 calls.

### 5.7 Answering (`ask`)

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
   successor. Up to 8 notes ≥ 20% of the best. When the question walks lineage or names two or more ids, up to 4
   relatives of the picked notes (parents, successors, children for "what came of") follow as a header plus their
   `# ` line (gold recall 0.895 → 0.920 for +11% characters). Weights in the `W` table.
8. **Print**: under `▸ path · kind · date · from … · SUPERSEDED → newer`, the best 2–4 lines per note; whole notes
   when everything picked fits the budget (900 chars per question + 1,500). On a memory of ≤ 200 notes, when the
   whole memory would cost ≤ 1.2× the surgical output, print it all: per-question `▸ path` pointers, then every note
   by area — complete, and no dearer than `cat`. A question with a word found nowhere, whose best note covers at most
   half its words, gets a `(weak match: 'x' found nowhere …)` line.
9. **Taste** (task intent only, `taste`): scored inside the general areas so project notes cannot crowd them out; a
   person named in the task, or named inside one of the three best-matching house notes (their meeting's roster,
   their report), brings all their notes; house rules about the artifact asked for (chart, table, deck …) come along;
   `prefs/me-*` always. Up to twelve notes, printed as their `# ` line.
10. **Claude Code's auto memory** (`cc_search`, read-only): the project's auto-memory topic files are grepped once for
    every question; at most three files and two lines each, under `▸ claude-code: <file> · <type> · <date>`.
    `MEMORY.md` is skipped (Claude Code loads it itself). Resolution: `$MEMORY_CC_DIR`, `autoMemoryDirectory` in
    `.claude/settings.local.json` or `~/.claude/settings.json`, else `<config>/projects/<git root sanitised>/memory`.

### 5.8 Big memories

| piece | what | why |
|---|---|---|
| `_dream/store.db` | note facts by path, extractions by hash | a dream re-reads only what changed (was 75 s of file reads at 168k) |
| `_dream/index.db` | the graph as SQLite (notes, edges, ents, ment, names, rels, checks) | `ask` (`DbView`) loads note rows and reads the rest per question (was a 381 MB JSON parse per call) |
| patch on read | notes changed since the dream are re-read from text (lineage now, entities at the next dream) | no 90 s rebuild inside `ask` |
| viewer split | overview (120 best-linked areas, filterable table, health) + `viz/<area>.html`, redrawn when the area's notes, lineage, entity ids or relations change (`viz/_sig.json`) | one 372 MB page → 2.4 MB + ~110 KB per area |
| `notes_part` reuse | after a review only the vocabulary half is rebuilt | halves the dream when a review applies |

### 5.9 Viewer (`assets/viz.html`)

Self-contained HTML (no network), grayscale theme with light and dark modes, one accent (the ink) for what is picked.
Data lives in `<script type="application/json" id="data-graph">` (notes with their full text, entities with
mentions, relations with evidence, lineage edges, checks, review queue, conflicts); `memory.py` fills it
(`render_viz`); every top-level element has an id; parts talk through `dp:` events. Two views:

- **Global — notes by area and time.** One row per area (projects first, general areas in italics), x = date, each
  note a shape by kind (circle experiment, square decision, diamond finding, triangle model, hexagon dataset or
  feature) in a grey by kind; superseded notes hollow and dashed; lineage drawn as curves (built on; dashed =
  supersedes; faint = refers to). Hovering a note lights its links; picking one dims everything outside two lineage
  hops and draws its own links in (a 420 ms stroke animation, off under `prefers-reduced-motion`). Clicking an area
  label opens the area's summary.
- **Picked — what the agent sees.** For a note: the exact `▸ path · kind · date · from … · SUPERSEDED → …` header and
  the numbered lines `memory.py ask` prints, then its lineage as a five-column tree (built on ×2 · built on · the note ·
  built upon by · ×2, clickable), the entities the dreamer read in it (chips → the entity view), the relations it
  states with the quoted line (`label?` for links outside the vocabulary), pending conflicts and warnings. For an
  entity: how it is written, headline and home note, typed relations, labels, every note that mentions it. For an
  area: counts by kind, superseded → current chains, conflicts, warnings, notes newest first.
- **Fuzzy search** (fzf-style subsequence scoring with word-start and run bonuses; exact substrings win) over title,
  id, text and entity names; the best 20 listed with matched letters marked, every match kept in the lanes while the
  rest fade; `/` focuses, arrows and Enter pick, Esc clears.
- **Health** (collapsed): warnings by code, superseded → current, unlinked notes, the review queue (pairs, labels
  over the bar, conflicts). Deep links: `#note=`, `#entity=`, `#area=`, `#q=`, `#health`.
- **Modes**: whole memory; `area` (one page per area past `MEMORY_WIDE`, with "← all areas"); `overview` (one card per
  area with a kind bar, linking to its page). Measured: the 1,677-note bank renders in 0.9 s from a 1.6 MB page with
  1,524 notes and 3,680 links drawn, 0 console errors.

---

## 6. Tests

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
re-asked). Results are written to `tests/acceptance.json`.

---

## 7. Reproduce the evaluations

### 7.1 The 56× bank (1,677 notes) and its questions

The bank was written by Haiku subagents, one bundle per project or general area, each bundle = notes + questions
with gold notes and reference answers (lookup, lineage, dependency, current, why, numeric, correction, term …).

```bash
python3 eval/bank/split.py <bundles dir> eval/bank/generated eval/questions     # bundles → notes + questions
python3 eval/bank/assemble.py eval/bank/generated tests/fixture/memory <W>/memory # bank + churn-2026
MEMORY_LLM="python3 tests/haiku_cmd.py" DREAM_COST_LOG=<W>/cost.jsonl \
  python3 skills/memory-dream/scripts/memory.py --root <W>/memory dream -j 10      # index: ~$3.3, ~25 min
```

### 7.2 Offline retrieval (no LLM)

```bash
python3 eval/retrieval.py <W>/memory eval/questions/bank-*.jsonl        # gold-note recall, number recall, chars
python3 eval/retrieval.py <W>/memory eval/questions/bank-*.jsonl --must # superseded gold notes count as history
MEMORY_WIDE=100 python3 eval/retrieval.py <W>/memory eval/questions/bank-*.jsonl   # force big-memory routing
python3 eval/adversarial.py <W>/memory eval/questions/bank-*.jsonl --index-world <real-indexed world> --show
```
Expect 0.895 / 0.972 at 1,677 notes (0.899 with `--must`; 0.891 / 0.963 routed). `adversarial.py` measures the sets
where grep should lose: stale-vs-current (successor above the old note 0.95, old marked 1.00), scattered evidence
(all gold 0.66 at 1.9k chars vs 0.99 at 12.6k for `cat` of the folder), alias traps (0.93 with or without the index
vs 0.43 for an exact-phrase grep). `MEMORY_NO_INDEX=1` switches `ask`'s use of the index off, for such comparisons.

### 7.3 Agent eval (Opus subagents, memory vs grep)

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

### 7.4 What a note costs

`tests/haiku_cmd.py` logs `total_cost_usd` and tokens per call when `DREAM_COST_LOG` is set (never quote prices
from memory). `python3 eval/prompt_breakdown.py <memory>` splits a prompt into template, EDGES, KNOWN and note.

### 7.5 100× (168,141 notes)

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

### 7.6 Taste (preferences applied to tasks)

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

## 8. Results to expect

| measure | 30 notes | 1,677 | 168,141 |
|---|---|---|---|
| retrieval: gold notes / numbers | — | 0.882 / 0.970 | 0.854 / 0.950 |
| `ask`, 10 questions | < 1 s | 0.5 s | 2.3 s |
| agent cost vs grep | 0.93× | 0.47× | 0.41× |
| $ per new note (Haiku) | 0.0013 (60-note world) | 0.0020 | 0.0015–0.0019 |
| dream, nothing new | — | 0.7 s | 3 s |
| dream, 30 new notes (with Haiku) | — | — | 82 s, 4.8 GB |
| viewer | 1 page | 2.9 MB | 2.4 MB overview + ~110 KB per area |

Taste retrieval (fresh tasks, recall of the gold notes): the person's preferences 0.93 when the task names them,
0.57 when it names only their meeting or audience; house rules 0.42 (before the taste layer: 0.76 / 0.35 / 0.25).

---

## 9. Pitfalls met on the way (and what fixed them)

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

## 10. Known limits and next steps

- **Taste is mostly not written down.** It arrives as corrections in conversation; the memory only knows what an
  agent saved (SKILL.md now says to save it at once). The write side has not been measured with agents.
- **Implicit audiences** (a task names the meeting, not the person) still miss ~40% of the person's preferences:
  the link from meeting to person exists only inside the notes' text.
- **A dream holds the whole graph in memory** (4.8 GB at 168k notes) and `_dream/` takes ~2.2 GB on disk at that size.
- **Synthetic data.** Notes and questions were written by Haiku; real notes from people over months are untested.
