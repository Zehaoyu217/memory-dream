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
- One stdlib Python file (`skills/memory-dream/scripts/memory.py`, ~3100 lines), one HTML template, one SKILL.md; stores.py for optional hosted stores.

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
python3 tests/acceptance.py                         # 40/40 should pass

# the skill and the dreamer subagent, user-wide
mkdir -p ~/.claude/skills ~/.claude/agents
cp -R skills/memory-dream ~/.claude/skills/
cp skills/memory-dream/agents/memory-dreamer.md ~/.claude/agents/

# in your project
cd /path/to/project && mkdir -p memory && printf 'memory/_dream/*\n!memory/_dream/notes/\n' >> .gitignore  # the readings stay in git
export MEMORY_LLM='claude -p --model haiku --tools "" --setting-sources "" --strict-mcp-config --no-session-persistence'
python3 ~/.claude/skills/memory-dream/scripts/memory.py dream      # seeds KINDS.md, TYPES.md, EDGES.md, ALIASES.md, DIGEST.md, _dream/
echo '@memory/DIGEST.md' >> CLAUDE.md                              # Claude Code: the digest in context every session
```

Beside Claude Code's own memory (CLAUDE.md, auto memory under `~/.claude/projects/<project>/memory/`): `ask` reads the
auto-memory topic files in the same call and never writes there; `dream`, `log`, `drop` and `viz` refuse such a root. Any other
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
index) and stays quiet about entities. To add them without a model command: `dream --packets` writes the unread
notes as packets to `memory/_dream/pending/` and lists them in `TODO.md`; run `memory-dreamer` subagents (Haiku) on
them, one packet each, then `dream --packets` again. `dream --dry-run --packets` first says how many packets and
about how much; with a command set, `dream --packets` sends each packet as one call.

---

## 3. The design in one page

1. **Thin layer on grep.** Agents are good at grep and Read; the tool enhances them, never replaces them. Every
   change is benchmarked against a grep-only agent on the same questions.
2. **One call.** Round 1 lost to grep (2.3× cost) because of round trips: every request re-sends ~37k tokens of
   context. `ask` takes every question at once and prints only the lines that answer.
3. **Lineage is the author's when it is written, and read when it is only said.** `from:` (built on) and
   `supersedes:` (overturns) in frontmatter come first and always win; a superseded note is shown as history with
   its successor. Where a note says it only in its own sentences ("Builds on exp-303 and the isotonic score map"),
   a cheap keeper reads it, each item with the note's own words, and the script places it by exact rules (a path or
   an id; a note replaces one of its own family; not a newer note; not two that claim each other). What cannot be
   placed is listed (C18) and printed by `ask` beside the note, never dropped in silence.
4. **An agent is as right as what the memory holds.** It makes one call and answers from it, so on a base whose
   links are only in prose the readings are what make a chain whole: as first read the memory held 94% of the
   links and its lineage alone answered 83 of 98 set questions, and Opus with it scored 82 (RESULTS S6). Measure
   the lineage alone (`eval/linkage.py lineage`) before touching retrieval. On a base that writes its lineage in
   frontmatter the index stays optional for answering, as measured before (RESULTS F4, F9: 0.8 points of gold
   recall and 6.4 on alias questions for 5% more characters), and earns its keep for aliases, the viewer and
   management. It must stay cheap and conservative: loose names hurt retrieval.
5. **The domain is three registries, not code.** `KINDS.md` (kinds of note), `TYPES.md` (types of thing) and
   `EDGES.md` (types of link) are seeded for data, analytics, software and finance and read before every command; the
   extraction prompt is fixed guidance filled from them. Both vocabularies are constrained open: a word that fits no
   type is kept as `other/<word>`, and becomes a type only over an evidence bar, through the review, within a budget,
   on probation. A registry edit never re-reads a note (the cached readings keep the raw words; the registries decide
   what they mean at merge time), and a type is retired by merging, not deleting (a deleted line is reported, C13).
6. **Scale by routing, not by heavier machinery.** Past 10,000 notes, `ask` greps only where a question points,
   reads an SQLite index row by row, and the viewer splits into an overview plus one page per area. A folder too
   large to list in a prompt is shown to a keeper by what is near the lines it reads (RESULTS S7).
7. **Cheap readers, exact scripts.** Every model step is one prompt that returns JSON with the note's own words; the
   script decides what is kept. Nothing is joined or placed by how alike two strings look: a name is one thing
   because a keeper read both and said so (the curator), and a phrase is a note because a keeper chose it from the
   notes the script showed.

**What a dream does, and what it costs.** Measured for the bank of 1,677 notes on Haiku 5.5, once with its forty
project folders and once with them poured into one (RESULTS S5 to S8). `dream --dry-run --packets` gives the
estimate for a memory before anything is called.

| stage | who | what it does | for the 1,677 notes |
|---|---|---|---|
| plan | script | finds the notes that are new or changed; checks pointers into code and tags | no call |
| first reading (`index`, `PACKET`) | Haiku, a dozen notes a call | the things each note names, the links it states, and what it says it builds on or replaces, each with a quote | about 145 calls, $1.28 to $1.57, 17 to 22 minutes at six calls at once |
| grounding (`ground`) | script | drops what its quote does not show; sends a lineage line it could not ground to the second reading | no call |
| second reading (`PLACE`, `run_place`) | Haiku, up to 45 lineage lines of a folder a call | every member of every line that states lineage, each with the note meant; in a folder too large to list, beside the notes near the line | 50 to 77 calls, $0.18 to $0.28, about 3 minutes |
| third reading (`CHOOSE`, `run_choose`) | Haiku, 8 items a call | the words two readings could not place, beside the six notes they could mean, with their first lines | 16 or 17 calls, $0.02 to $0.05 |
| build (`build`, `lineage_as_read`) | script | places what was read by exact rules, merges names, decides what is current, the 18 checks | no call, about a second |
| curator (`CURATE`) | Haiku, a folder a call | which names are one thing, each join signed with its reason; the script refuses a join that breaks its rules | 7 to 49 calls |
| review (`REVIEW`) | Haiku, one call | labels mapped onto link types, and which of two conflicting live notes stands | 1 call; with the curator $0.03 to $0.12 |
| write | script | `graph.json`, the page, `DIGEST.md`, the readings in `_dream/notes/` | no call |

$1.59 for the bank with folders and $1.92 in one folder, about a dollar a thousand notes, paid once: a note is read
again only when its text changes, and the readings kept in git let a clone rebuild the same graph with no call. With
no model command nothing is read: `ask`, the checks, the digest and the page all work, and lineage is what the
frontmatter says. How an agent sets a memory up and has it read is the skill's section "Setting a memory up".

---

## 4. Repository layout

```
skills/memory-dream/
  SKILL.md                     what the agent reads: read, write, end of session, the vocabulary, setting up
  guides/                      optional: vocabulary.md (the one rule), scenarios.md (where the lists start),
                               knowledge-graph.md (the graph page for any data)
  scripts/memory.py            ask · dream · viz · check · log  (stdlib, ~3,200 lines)
  scripts/graph_page.py        the knowledge-graph page for any graph (JSON, or two CSV tables), through memory.py
  scripts/stores.py           optional hosted stores (PostgreSQL, Neo4j) and the CSV export; imported only when MEMORY_STORE is set
  assets/viz.html              viewer template (html-lite habits; normal, overview and area modes)
  assets/knowledge-graph.html  the page to show a memory, with d3.v7.9.0.min.js and its LICENSE-d3 (§5.10)
  agents/memory-dreamer.md     Haiku subagent for file mode
.specs/memory-dream/           build-spec.md (v0.4 spec), RUNBOOK.md, RESULTS.md (rounds 1–4)
tests/
  fixture/memory/              churn-2026: 25 notes + 5 log days (hand-written ground truth)
  acceptance.py                46 checks: A1–A20 (spec), A24 (big memories), A25–A43 (phases A–J), A44–A49 (one
                               vocabulary rule, identity by evidence), fake dreamer, ~30 s
  retrieval_gate.py            CI floors for the model-free retrieval numbers: bank (326 questions) and software fixture
  store_parity.py              a hosted store (MEMORY_STORE=postgres) gives identical ask output and the same graph
  fixture-software/memory/     a software project (payments-api: services, modules, ADRs, bugs, releases, an incident)
  fake_dreamer.py              deterministic dreamer (regex extraction) for tests and profiling
  haiku_cmd.py                 MEMORY_LLM wrapper around `claude -p --model haiku`, logs cost per call
  real_model.py, truth.py      Haiku runs against the fixture's ground truth
eval/
  bank/generated/              56× test bank: 1,648 Haiku-written notes in 47 areas
  questions/                   366 questions with gold notes and reference answers
  retrieval.py                 offline: did ask print the gold notes and the answer's numbers?
  stability.py                 offline: the same answer under any hash seed, file order and company? (phase J)
  graph_probe.py               offline: what plain graph methods find in a dreamed graph (loops, hubs, roles; PLAN.md §8)
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

Walk `memory/` with `os.walk` (skip `_dream/`, dot dirs, `KINDS.md`, `TYPES.md`, `EDGES.md`, `ALIASES.md`, `CONFLICTS.md`, `DIGEST.md`, `README.md`, `INDEX.md`).
Keep `{path: {sha256, mtime_ns, size}}` in `_dream/manifest.json`; re-hash only files whose mtime or size changed.
A path that disappeared while the same hash appeared at exactly one new path is a move (`former` keeps old paths so
old references still resolve).

### 5.3 Note facts (`parse_note`, `note_facts`)

From each note's text: frontmatter (`from`, `supersedes`, `type`, `updated`), the `# ` title and its line, `[[links]]`
outside code, every slug-like token in the body (`[a-z][a-z0-9]*(-[a-z0-9]+)+`), and its pointers into files
(`POINTER`: `path#symbol`, `path:line "quoted words"`, `path:line`). Cached per path and content hash in
`_dream/store.db` so a dream re-reads only changed notes.

Pointers (`pointer_states`, CONTRACT §1): at every dream each one is looked up in the project's files (`code_root`:
the repository around the memory): a symbol as a definition, quoted words on a line, a bare line by the text it
named when first seen. States intact, moved (with the line it is on now), changed, gone; C16 for the last two. A
name that was never a file of the project is not a pointer. `ask` looks the pointers of the notes it prints up
again, so the line it shows is today's, and marks a note STALE when one no longer holds. This is not a code index:
nothing is parsed, and files are not things unless `TYPES.md` says so.

A definition (`define_line`, the four patterns of `DEFINES`) is looked for form by form, and the first form found
anywhere in the file decides: a keyword before the name, a block that opens, an assignment at the start of a line, a
key at the start of a line. A call is no form, and the form a symbol was first found by is kept with the pointer so
that a weaker one is not taken later. Quoted words (`words_rx`) are never found inside a longer word; on several
lines and no longer on their own, a line that begins with them comes first, then the nearest. Do not fold these into
one pattern that takes the first match: `eval/pointer_probe.py --built` scores the lookup on this repository's
history, and that version put 12 of 209 symbols on the line of a call or of a local variable.

### 5.4 The graph, note half (`notes_part`)

- One record per note: path, id (filename), project (top folder), title, line, kind (`kind_of`: frontmatter `type`
  with Claude Code's user/feedback/project/reference mapped to preference/rule/note/note, else the area when it has a
  kind (the `area:` fields: `prefs/ glossary/ corrections/ reporting/ howto/ log/`), else the kind whose prefix is the
  first or second part of the filename (the `prefix:` fields of `KINDS.md`: `exp- feat- ds- dec- fnd- find- q- metric-
  plan- req- risk- inc- rpt-` in the seed), else `…-vN` = model, else the dreamer's kind unless it is the fallback
  "note", else `note`: the folder and the name a writer chose come before the dreamer's reading), updated (frontmatter `updated`
  or `modified`, log filename date, or mtime), superseded_by. `general_areas` judges an area on its kinded notes only.
- Edges: `from` and `supersedes` resolved by relative path, then exact path, then unique filename, then same-project
  filename (warning C1 if ambiguous), then moved paths; unresolved → C2. Plus `refs`: `[[links]]`, the dreamer's refs,
  and any body slug that names a note in the same project.
- Tombstones (`parse_dropped`): a line `dropped: <note.md | folder/> (date) > <what it had replaced>` in
  `CONFLICTS.md`, written only by `memory.py drop`. A reference that finds no note and names a tombstone is not C2:
  a `from:` marks the note as built on a dropped note (C14), a `supersedes:` becomes an edge to each note the dropped
  one had replaced, followed through further tombstones (`by: "drop"`). So a line of replacements holds when a note
  in its middle leaves, on any clone, with no old graph. The graph's `dropped` list carries what was recorded.
- `drop <note | folder> [--yes]`: prints what goes with the target and stops; with `--yes` deletes the files and their
  readings, appends the tombstones, and runs the dream's plan, graph and write stages with no model. Notes whose every
  `source:` is dropped go too. A file that is gone without a drop is never treated as one: the dream keeps where it
  stood in the manifest (`gone`) and reports C15 with the command.
- Origins (`ORIGINS`, `area_of`, `origin_of`; CONTRACT §7): a top folder with an `ORIGIN.md` is another base's notes.
  One function gives a note's area everywhere (`<origin>/<next folder>` under an origin, the first folder otherwise),
  so its kinds by area survive. A lineage target is looked for inside the origin before the host and never guessed
  across; an entity read from its notes is `<origin>:<id>` until a line of `ALIASES.md` joins it; its preferences are
  served only with `trust: preferences`; none of its notes is in the digest. In `ask` the host's notes are ranked as
  if the origin were not there (their own document frequencies, their own things' names) and at most three of its
  notes follow in a block of their own. `absorb <folder> --as <name> [--yes]` copies a folder in as one, brings its
  readings through `ground()`, turns a `relations.jsonl` with entity cards into readings, and reports what it refused.
- Warnings: C1 ambiguous, C2 not found, C3 indexing failed, C4 dropped ungrounded entity/relation, C5 unindexed,
  C6 no `# ` line, C7 review pending (labels, budget), C8 bad EDGES/ALIASES/CONFLICTS line, C9 NUL bytes in a note
  (binary-looking), C10 conflict pending, C11 a note over 40 lines, C14 built on a dropped note or left the newest of
  its line by a drop, C15 gone without a drop, C16 a pointer into a file that no longer holds, C17 a tag that
  TAGS.md does not list, C18 lineage a note states in prose that no note answers to, C19 a note links two names that a
  line of ALIASES.md joins. `check` also runs the memory's own proof (`proof`): each `- question? -> note` line of
  `memory/SETUP.md` is put to `ask` alone, and the line counts when a section of the answer is headed by that note.

### 5.5 The graph, vocabulary half (`build`, `merge_entities`)

Entities, from every note's extraction:
1. Key = `fold(id)`: lowercase, runs of space `_` `.` `-` → `-` (`cards.txn_daily` = `cards-txn-daily`).
2. Union-find: every ALIASES.md line merges its ids (forced); `not: a / b` lines and version pairs (ids differing
   only in digits) are never merged, and no rule merges two ids that a reading links to each other (`read_links`:
   two things a note links are two things; a person's line that joins them is reported, C19).
3. Surface rule: if exactly one other entity writes this id as a surface form (and ≤ 3 users), merge.
4. Keep an entity only if it has a home note (a note whose filename is its id), is mentioned in ≥ 2 notes, or is
   named in ALIASES.md; drop a name that the `drop-names:` line of `TYPES.md` matches, as written or folded (the
   seed's line: `*.py, *.sql, *.ipynb, *.csv, *.parquet, *.json, *.md, *notebook*, nb-*, *-script`; `name_drop`).
5. Canonical id: ALIASES.md lead, else the most used raw id; type by majority vote over the occurrences' types read
   through `TYPES.md` (`canon_occ`: the dreamer's type or label that is a type or alias → that type; a word that fits
   none → `other/<word>`, counted for the review; a word on the `drop:` line removes the occurrence); headline = best
   current note (a title-line mention, then a finding or decision, then the latest date, then the first by path; the
   file's modification time is never asked, since a clone does not keep it).

Relations, two tiers: the dreamer gives each relation a `type` (an EDGES type or alias, or `other`) and a `label` (the
note's own verb). Listed types and their aliases (`~` = read in reverse) are kept with evidence `path:line`; a link
whose type and label fit nothing is kept as `other/<label>` (shown on the entity card, not on the map); `drop:` names
only note-to-note links. A label is offered to the review once it clears `promote: 5 uses, 5 notes, 2 areas`
(EDGES.md); the review answers `alias T`, `alias ~T`, `label`, `drop` or `new: <definition>`, and the code admits
`new` only under `budget: 24` types, writing `- <type> (proposed <date>): …`; a proposed type still under the bar
after `probation: 60 days` is demoted to a label (0 calls). `pack: software | research | ops` adds domain types.
Type words go through the same gate (`vocab_gate`, shared): `TYPES.md` has its own `promote`, `budget: 40` and
`probation`; the review's `etypes` answers alias a word onto a type, admit `new: <definition> | family: <F>`, keep the
word, or drop it; `tvocab` and `proposed_types` in the graph mirror `vocab` and `proposed`. A type line removed by hand
from either file while readings still use its word is reported (C13); the readings show as `other/<word>`.
Kind words and tag words go through the same gate and the same review, and one function admits every answer
(`apply_terms`): a keeper's `other: <word>` for a note no kind fits is kept in its reading as `kind_word` (the note
counts as `note` until KINDS.md has the kind or an alias, `aka:`, and then counts as that kind with no re-read; a kind
given a family takes its family's role); tags come from notes' `tags:` lines and from the keepers' `tags` (at most
three a note, given from the TAGS section of their prompt), both resolved through TAGS.md at every merge. The TAGS
section, its rule and the reply's `tags` key (last) are in the prompt only once TAGS.md lists a tag (`tag_fill`):
asked first in the reply, tags cost a third of the links on the fixture (RESULTS phase T). `KINDS.md`
takes `promote` (5/5/2), `budget: 40` and `probation`, and `TAGS.md` `promote: 3 uses, 3 notes, 1 area`, `budget: 30`
and `probation`; the review answers `kinds` and `tags` as it answers `etypes`; `kvocab`/`proposed_kinds` and
`gvocab`/`proposed_tags` mirror `vocab`/`proposed`. In every file a `label` answer is remembered on a `keep:` line
(`word ×uses (date)`) and the word is offered again only once its uses double, so a word the review kept is not asked
about on every run. The rule as an agent reads it: `skills/memory-dream/guides/vocabulary.md`.
Conflicts: two live `…-vN` siblings in one area, two live notes with the same title, or live notes of one kind
(decision, model, finding) in one area, unlinked, sharing an id-like title token or two rare words, are queued (C10,
20 per review); verdicts persist in `memory/CONFLICTS.md` (`- a > b` becomes lineage, `compatible: a / b`, `- a ? b`);
notes are never edited.

The seed vocabulary (8 types): `uses`, `produces`, `part-of`, `trained-on`, `evaluated-on`, `measured-by`,
`replaces`, `owned-by` (full alias lists and `shape:` fields in `EDGES_SEED`; a file written before shapes existed keeps
the seed's shapes). The seed thing types (27, `TYPES_SEED`): person, team, organisation, term, metric, tool, document;
dataset, segment, feature, model, pipeline, dashboard; service, module, environment, release; instrument, portfolio,
account, counterparty, policy, scenario, desk; flag, test, issue — each with aliases, a family where it has one, and `not:` on the most
confusable. The seed kinds (23, `KINDS_SEED`): question, experiment, finding, incident, decision, plan, requirement,
risk, dataset, feature, model, metric, report, component, design, bug, release, term, preference, rule, correction,
log, note, with prefixes, areas,
families, roles and the `digest`, `conflicts` and `answers` flags. Evidence: 81% of 5,196 extracted links fit them and 365 of
366 questions need lineage, a single note, or one of the 8 (`eval/type_coverage.py`, `eval/question_relations.py`);
with Haiku on 70 notes the two-tier prompt gives 81% typed, 19% labels, 0 invented types (RESULTS "Phase C").

Review candidates (`candidates`): new entities of the same type that some note writes with the same words; pairs with
two different home notes, or that a note links to each other, are never queued. Each side of a pair is shown by its
card, the curator's (`thing_cards`, below), and the pair by what the two are both linked to (`shared_links`). Nothing is proposed from how two names look. Do not bring a string
distance back: on the bank the ratio that used to do it (0.85) offered 46 pairs, 5 of them one thing (all plurals)
and 41 siblings such as aml-oot-2026h1 / cli-oot-2026h1.

The curator (`CURATE`, `Dream.cards`, `Dream.run_curate`): identity by reading. For each folder whose things changed
since it was last read, one prompt lists them, one card each (`thing_cards`): its type, its written forms, the number
of notes, what its own note says it is (`is:`, that note's title), what the notes link it to (`links:`, the three best
attested, → from it and ← to it) and a line that mentions it, from another note than its own; the answer names the
ones that are one thing under two names, each with a reason. Identity is read from what a thing is and what it is
linked to, never from a name alone. A join is a
line of `ALIASES.md`, `- a = b | why: … | by: curator <date>`. The script holds six rules whatever the answer says:
both are on the folder's list; never two versions; never against a `not:` line; never two things a note links; the name joined to another is used
in this folder alone, and a thing whose note is in another folder is not renamed here; no line may come to join two
things that each have a note. The folder's signature after the joins is kept in the manifest (`curated`), so the
same things are not read twice; at most 60 folders a dream. With a command it runs before the review, `-j` folders
at a time; without one the prompts are `curate-<folder>.prompt.md` in `_dream/pending/`, written with `--prompts` or
`--packets` and answered like the others.

### 5.6 The dreamer (`dream`)

Structure: `dream` takes `_dream/lock` (a second dream exits 3; a lock older than 2 h is taken over) and runs a
`Dream` object in stages — `plan` (scan, caches, what to index), `index` (command or file mode), `graph`, `demote`
(probation over), `run_review` (labels over the bar, entity pairs, conflicts), `write` (viewer, index.db, digest,
pending list, manifest), `report`. The tuned numbers of `rank`/`route` live in the `W` table beside the retrieval
constants, each with the measurement that set it.

- **Extraction prompt** (`EXTRACT`): fixed guidance filled from the registries — JSON with kind (one of KINDS),
  entities `{id, type, label, as[]}` (a TYPES type or alias, or `other` with the note's own word as label), relations
  `{s, type, label, o, quote}`, refs. It gets the KINDS list, the TYPES lines, the EDGES lines and KNOWN: up to 80
  entities of the note's project plus 20 most-mentioned shared ones
  (`Known`, one sort per wave), so ids are reused and the prompt stops growing (~2.2k tokens plus the CLI's own ~4.8k).
- **Grounding** (`ground`): an entity survives only if one of its `as` strings occurs in the note; a relation only if
  its quote occurs. Dropped ones are counted (C4). The same holds for `built_on` and `replaces`, the two lists in
  which a keeper says what the note itself builds on and what it replaces: an item is kept with the words that say so.
- **Lineage as read** (`lineage_as_read`, in `build`): each kept item becomes a `from` or `supersedes` edge marked
  `by: "reading"`, once what it names is placed: as a note by path or file name (the note's own folder first), else as
  the home note of the thing of that name after the merge. Frontmatter and `CONFLICTS.md` win. Replacements are
  collected first and then judged together: none from a note older than the one it names, none from a note of
  another kind when a note of the replaced note's own kind claims it too, none when two notes claim each other.
  These three were set on the whole worn bank (RESULTS S5), where a plainer rule, one kind only, held 68% of the
  replacements and these hold 91%; do not go back to judging each claim as it comes, in note order. So that a keeper can
  name the note a phrase means ("the dispositions dataset"), both prompts carry `FOLDER`: the notes of the folder as
  `file name: first line` (`folder_lines`, at most 80 a folder), part of the prefix that every call of a folder shares.
  One more exact step comes last (`named`): an item no note answers to, whose own words name one note by its path
  or id that no other item of the note took, is that note ("Replaces glossary/brier.", written down by a keeper as
  the thing `glossary-brier`: 13 on the worn bank, all right). Only a word written like a path or an id is looked
  up, never a plain word of the sentence. And a replacement is taken from a note of the replaced note's own family
  only, unless the replacing kind's line in KINDS.md names the other under `replaces:` (the seed: a correction
  replaces a term). "pbs-gmm-v3 replaces the kmeans and gmm-v2 tables", in a decision, had made the decision the
  replacement of the model, and the note in force wrong (RESULTS S8); on the worn bank the rule refused 20 claims
  and no true replacement. A version may end in a letter: `bsm-app-gbm-v10a` is a model, as `…-v10` is.
- **Grounding does not lose a line** (`ground`, `recheck`): an item whose copied words are not in the note is not
  kept, as before, but the lines that write what it names are put to the second reading. A keeper had copied
  "Builds on aml-xgb-v3, …" for a line that says v2, and the four members of that line were lost without a trace.
- **The second reading** (`PLACE`, `Dream.run_place`): the first reading finds the lines of a note that say what it
  builds on or replaces among everything else it does for a dozen notes, and of the things such a line names by a
  phrase it left one in ten out without a trace (RESULTS S6). With a command, every such line is put to the keeper
  once more, by folder, 45 lines a call, with the folder's notes by file name and one thing asked: every member of
  the line, each with its own words and the note meant. The answer takes the first reading's place on that line:
  one item a member, the member's words as its quote, marked `asked` so that a line is read twice and no more; a
  member no note is named for stays, with its words, and is listed (C18). Nothing is lost by silence: an answer
  with no member for a line leaves the line as it was, and an item whose name is written in the line stays. On the
  worn bank, 1,462 lines in 50 calls for $0.18: `from` links held 94.3% → 99.5%, replacements 91.2% → 99.5%, the
  questions its lineage answers exactly 83 → 93 of 98. Do not fold this into the first reading's prompt: the rule
  is already there ("a sentence that names three gives three items") and was not kept. What works is the line
  alone, with nothing else to do.
- **A folder too large to list** (`FOLDER_SHOWN`, 200 notes; `$MEMORY_FOLDER`): a prompt cannot carry its notes by
  name, and the first 200 by alphabet are no help. The second reading then shows the keeper the notes *near* the
  lines of a call (`PLACE_NEAR`): those within four steps of a line's note by a name written in a note, either way
  (`NEAR_STEPS`), and apart from them, under ELSEWHERE, the eight notes of the folder whose first line and file
  name share the rarest words with the line (`NEAR_WORDS`). Lines of notes that name each other go into the same
  call, and a call takes lines only while the notes to show for them fit in 120 (`NEAR_SHOWN`), so none is cut
  for coming late in the alphabet. The script chooses what is shown and says how near it is; the keeper decides,
  and no note is placed by its words. Three things were measured on the flat bank (`eval/hard/make_flat.py`, 1,224
  notes in one folder; RESULTS S7) and should not be undone. Without a model, the note a phrase means is among
  those shown for 99.5% of 750 phrases, 33 notes at the median; four steps alone hold 95.5%, the words alone under
  90%, and a third rule on shared name tokens added nothing. The two kinds must be shown apart: as one list, a
  look-alike from another project ("the logistic regression baseline", of which every project has one) made the
  keeper answer that two notes could be meant, for 30 phrases whose note was near. And a shorter list does not
  mend that: 70 notes a call in place of 200 left as many phrases unnamed and took five times the calls. The
  first reading does less in such a folder: its `FOLDER` list holds only the notes its own notes name by file
  name (`folder_lines(text=…)`), so it places ids, and a thing it cannot name it gives as an item with the note's
  words, which is what puts the line before the second reading.
- **The third reading** (`CHOOSE`, `Dream.run_choose`): words that two readings could not place are put once more,
  each with the few notes of its folder (six) whose file name, first line and next two lines share its rarest
  words, shown with those lines; the keeper says which note is meant or that none is, and an answer counts only
  when it names one of the notes shown. Asked once (`looked`). Three phrases had cost four of the six questions the
  flat memory's lineage got wrong: their note was on the second reading's list beside a look-alike, and by a title
  alone the keeper would not choose ("the bg/nbd versus gbm accuracy test": exp-501, against exp-503 on the same
  models). On the worn bank it placed 17 of 28 such words in 17 calls.
- **What `ask` does with an item that is still not placed** (`loose_ends`): it prints the note's own words under
  the note (`? it builds on «…», in its own words`), says `not the whole chain` on a `⇡` line that runs through such
  a note, and carries the words on the note's line of the map. Do not drop these lines to save characters. `ask` is
  a layer on grep, and an agent with grep reads that sentence; an `ask` that shows the derived lineage and is silent
  about the link it could not derive knows less than grep, and the agent takes the silence for "nothing more".
  These lines are only as good as what the memory knows it lacks: on the worn bank they changed nothing while two
  thirds of the missing links were members a keeper had left out without a trace (RESULTS S6), which is why the
  second reading asks for every member and keeps the ones it cannot name.
- **Command mode** (`MEMORY_LLM` set): waves of `-j` parallel calls, one retry for unusable answers. A call runs in a
  process group of its own (`run_command`): past `MEMORY_TIMEOUT` seconds (300) the whole group is killed, the pipes
  are closed from this side and only the shell is waited for. Do not go back to `subprocess.run(timeout=…)`: it kills
  the shell alone and reads on, so a hung grandchild keeps the dream waiting for good (`tests/hang_cmd.py` and a line
  of `tests/e2e.py` hold this). Notes are ordered by
  project then date, one KNOWN per project (big memories: refreshed at most every 10 waves) so every call of a project
  shares one byte-identical prefix; its length goes to the command in `MEMORY_STATIC_PREFIX`, and `tests/haiku_cmd.py`
  puts that prefix in the system prompt, which `claude -p` caches (−32% per note on the sample, convergence 1.06×).
  Note text is capped at 16k characters. **No model**: nothing is written for a helper and `check` summarises C5 in
  one line; **`--prompts`** writes the prompts to `_dream/pending/` for the `memory-dreamer` subagent and ingests its
  answers on the next dream.
- **Packets** (`--packets`; `PACKET`, `pack`, `packet_prompt`, `parse_packet`, `index_packets`): the same reading
  asked for many notes in one call. The rules are cut from `EXTRACT`, so the two prompts cannot drift; each note
  follows under `NOTE <sha12> <path>:` and is answered by one line of JSON that names it. A packet closes at
  `PACKET_TEXT` = 6,000 characters of notes (a dozen short ones) or `PACKET_TOKENS` = 60,000 tokens of prompt, at
  three characters a token, whichever comes first (`$MEMORY_PACKET="tokens,characters"`). The size is a measured
  trade (RESULTS phase S): two dozen notes a call read thinner (0.60 of the things of a single call), a dozen read as
  much and place more lineage, since the keeper sees the folder's notes together. With a command, `-j`
  packets run at a time, KNOWN is refreshed between waves, and a note whose line is missing is packed once more;
  without one the packets are files, named by the notes they hold. Every answer is grounded against its own note,
  as a single call's is. Answer files are taken first in both modes (`take_answers`): a reading on file is never
  asked for again. The stand-in dreamer builds the same graph from packets as from single calls.
- **Dry run** (`--dry-run`, with or without `--packets`): prints the notes to read, the calls or packets, the tokens
  in and out and a cost at `$MEMORY_PRICE="in,out"` ($0.10 and $0.50 a million, Haiku 5.5 under 100,000 tokens),
  and says when a prompt would cross that line. It counts the prompts as sent and a reading at 3.2 times its note:
  what a command adds to every call is not in it. It makes no folder, takes no lock and writes no cache.
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
   successor. Up to 8 notes ≥ 20% of the best. For every question, up to 4 relatives of the picked notes (parents, successors,
   children for "what came of") follow as a header plus their `# ` line (gold recall 0.895 → 0.920 for +11%
   characters when triggered by lineage words; for every question +1 point and +7 complete answers for +3%, F9). Weights in the `W` table.
   Scores are exact sums (`math.fsum`) and every sort ends on the path, so notes that score the same come in path
   order on every run and every machine, whatever the hash seed or the order grep lists the files in (phase J, A42).
8. **Print**: under `▸ path · kind · date · from … · SUPERSEDED → newer`, the best 2–4 lines per note; whole notes
   when everything picked fits the budget (900 chars per question + 1,500). On a memory of ≤ 200 notes, when the
   whole memory would cost ≤ 1.2× the surgical output, print it all: per-question `▸ path` pointers, then every note
   by area — complete, and no dearer than `cat`. An id, version or number the question names that no note mentions,
   or a plain word found nowhere when the best note covers at most half the question's words, gets a
   `(weak match: 'x' found nowhere …)` line; the rule reads the question's own words, never the index's aliases.
   A question about a set across the whole memory (`SET_WIDE`: "across every project", "whole memory", "other
   projects", with no folder named) gets a line that says its matches are not the set and names the map to grep,
   by the kind it asks for (`SET_KIND`: "which model notes" → `ask --list --kind model --all`). The map of every
   note of a big memory is larger than a reader's context, and a session under a 100,000-token window that read it
   was compacted and got 2 of 8 (RESULTS S7, S8). A project's map (`--list -p`) prints what rests on the folder from
   outside, and what it rests on, under its header and before its notes, so that a read cut short keeps the line
   that answers "which notes outside X rest on X".
9. **Taste** (task intent only, `taste`): scored inside the general areas so project notes cannot crowd them out; a
   person named in the task, or named inside one of the three best-matching house notes (their meeting's roster,
   their report; on a line the task's own words matched, never one that only another question of the call matched),
   brings all their notes; house rules about the artifact asked for (chart, table, deck …) come along;
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

### 5.8b The graph contract

`.specs/memory-dream/CONTRACT.md` is the authority on every shape `memory.py` writes and reads: the graph (`graph.json`,
`index.db`), the viewer's data island, the extraction cache, `store.db`, the manifest, the warning codes C1–C19 and the
grammar of EDGES.md, ALIASES.md, CONFLICTS.md and DIGEST.md. Every graph carries `schema: 1`; `validate()` checks a
graph against the contract, `memory.py check` prints the result first, and A38 enforces it on the fixture (graph,
`index.db` round trip, island). Build the viewer against the contract, never against the code.

### 5.9 Viewer (`assets/viz.html`)

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
(`render_viz`); every top-level element has an id; parts talk through `dp:` events. Three views, the Timeline first
when the page opens (tab order Timeline · Map · Connections; `#view=map` and `#view=graph` open the others):

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
- **Filters** ride in the search box as words: `tag:risk`, `type:model` (notes that mention a thing of that type or
  of its family), `origin:policy-kb`, `kind:decision`, alone or with search words, so a `#q=` link carries them.
  Beside the box a picker for each of tag, type of thing and base lists what this memory has and writes the word
  into the box; a picker with nothing to list is not shown. The page gets `tags`, `tag_defs` and `origins` in its
  data (`write_viz`); an area page of a big memory gets its own notes' tags.
- **Health** (collapsed): warnings by code, superseded → current, unlinked notes, the review queue (pairs, labels
  over the bar, conflicts). Deep links: `#note=`, `#entity=`, `#area=`, `#q=`, `#health`.
- **Modes**: whole memory; `area` (one page per area past `MEMORY_WIDE`, with "← all areas"); `overview` (one card per
  area with a kind bar, linking to its page). Measured: the 1,677-note bank renders in 0.9 s from a 2.6 MB page with
  1,524 notes and 3,680 links drawn; its graph view lays out 400 entities and 1,355 current relations in 1.3 s;
  0 console errors on the bank and the fixture, headless (Playwright: `tests/viz_check.js`).

### 5.10 The knowledge-graph page (`assets/knowledge-graph.html`)

The viewer is for working in a memory; this page is for showing one. It holds the things that have a link and the
links alone, and nothing in it knows a domain, so the same page serves any memory and any graph given as nodes and
links (`scripts/graph_page.py`). `write_kg` fills it after every dream that read links, and `viz` rewrites
it; the page and d3 7.9.0 (ISC) sit in `assets/`, and it opens offline.

1. **Islands.** A thing lives on the project holding at least 60% of the notes that name it among projects; a thing
   no project names, on the shared folder naming it most; a thing several projects share, in the middle. When the
   folders do not part the things (one island holds over half of them, or fewer than three hold three: a memory kept
   in one folder), the islands are the communities of the links instead (Louvain, deterministic), each named for its
   most linked thing. Islands are packed as circles (`d3.packSiblings`, the middle first, each island after those it
   shares most links with), then settle into an ellipse the shape of the screen (pull to the centre weaker across
   than down); things lay out inside their island with a short-range push, so they fill it instead of lining its rim.
   Those are d3's forces (links, a many-body push within 34, a pull to the island's heart, its rim, a collide) ticked
   by hand one island at a time over a grid of typed arrays: things on two islands never meet, and a grid finds the
   neighbours within 34 at a small part of a quadtree's cost. The layout runs in slices along the entrance sweep
   (120 ms at once, then before each frame 22 ms, or one and a half times what the last frame cost to draw where
   drawing is slow, as without a GPU), so the page answers at once and an island blooms when it has settled; a
   dragged thing settles its own island again, not the graph.
2. **Things, links, tags.** Only a thing's id and a link's two ends are required (read by the names other tools give
   them too: key, name, title, from/to, src/dst, start/end, a Cytoscape `data` wrapper); everything else is optional
   and undeclared: a row may have fields others lack, a nested object is spread into its fields, and n/a, none or
   unknown count as no value. A thing: an id, a label, an island (`group`), and tags. A link: source to target, a
   type (named both ways: common ones built in, a memory's from EDGES.md, another graph's from `link_types`), a
   direction (`->`; `<-`, turned round; `o-o`, none: one link however it is written, drawn in the accent, no flow
   along it, its own ↔ group in the panel), the line that says so, and tags. A tag: a column, in each row a value or
   several, of four sorts told by its values (`"sort"` settles it): a category repeats, each value a path whose
   levels are split by `/` (`dataset/table/daily`); a time is an ISO date, a category of year/month/day read as
   dates and in their order; a number (a thing's `size` sizes its dot, a link's `weight` its line and how hard it
   pulls, or another number by `"use"`); a text is long or mostly its own (a definition, a citation), kept whole,
   shown and searched with its owner, never coloured. Weight, time and provenance are tags like any other. A
   memory's things carry their type under its family (TYPES.md `family:`, so `segment` is `dataset/segment`), the
   projects whose notes name them, those notes' TAGS.md tags, Last noted (a time) and About (the key line of the
   note that best says what each is); its links carry the stating note's kind, Stated (a time) and Replaced, and a
   relation whose EDGES.md backward name is itself has no direction. Any other graph's tags are every column of its
   nodes and links but the fields above, with `columns`, `link_columns` and `link_types` entries for the vocabulary
   (`scripts/graph_page.py`, JSON or two CSV tables).
   The page colours by one column, chosen in the legend: the seven top-level values with the most things (each with
   2% of them) a colour each, the same hue for the same family in every memory, the rest one grey, "Everything
   else". The legend is a tree: › opens a value into the level under it (and "Other …" for those that stop at it),
   Everything else into the values without a colour and the things with none; pointing at any row lights its
   things, clicking hides them. Search finds the values too, every level, and lights them until Esc, and finds a
   thing by the words of its text tags; the panel shows its text tags and lists its categories, each a way to light
   its kind. With 56 types in a long tail (`model/uplift`,
   `question/open`, …) the colours fall on 7 of their 15 families and 23% of 20,000 things are grey (each still one
   row to open, light, hide or find); taken flat, 7 types got colours and 60% were grey.
3. **Motion with a reason.** It blooms in on a clockwise sweep with the camera easing out; while nothing is chosen,
   pulses run along links between islands; a chosen thing flies into view on the smooth zoom path (van Wijk and
   Nuij), its links flowing blue for what it uses and orange for what uses it, beside a panel of each link and the
   line of the note that says it; the legend lights a group, a panel row makes its thing beat, an island click flies
   to it, the tour visits the most linked things. Names never cover one another. `prefers-reduced-motion` stills it.
4. **Six looks, one page, kept side by side.** Paper; a star map at night (deep sky and twinkling stars, a nebula
   and a turning orbit under each island, glowing things, faint gold lines between islands, glass panels with gold
   corners); a gala, a purple show at night (stage-lit purple sky with a small moon, four-point sparkles, a pink
   wheel and a counter-turning ring of gold beads round each island, candy colours by legend order, a theatrical
   italic serif); and moonlit, a light look after a lilac-and-plum outfit with roses (a pale lilac stage under a
   great moon, sparkles in white, lilac and gold, ribbons drifting across, a moonlight pool ringed with turning gold
   pearls under each island, glossy pearl things in plum, violet, rose and periwinkle, a plum zig-zag hem on the
   panel, plum diamonds turning round a picked thing); and fanfare, a show after a violet-and-gold stage outfit (a
   violet stage with no black, gold, pink and cyan spotlights sweeping from above, a checkered floor running back to
   the horizon, bunting along the top, each island a round stage ringed with chasing marquee bulbs, candy-bright
   lotto balls, white cards with speech-bubble rows, a ✦ after the title); and noir, black and white after a
   black-and-white outfit with purple tulle (a black stage, one warm spotlight, a black-and-white checkered floor,
   white and silver things, warm-white marquee bulbs, the four card suits turning round a picked thing, purple only
   as an accent). The gala, moonlit, fanfare and noir fling confetti out of a thing when it is picked (noir's a
   quarter card suits). Each look is tokens on `<html data-theme>` (names on the page read `--page-ink`, names on a
   card `--ink`) plus a few canvas branches; a switch in the header picks one and the canvas fades across;
   `viz --theme star|gala|moon|fanfare|noir` opens in another. Measured on the 1,677-note bank:
   1,082 things, 2,740 links, 49 islands, 1.4 MB; 60 frames a second in every look on a laptop's GPU; 0 page errors
   and no stray black in any look, headless (`tests/kg_check.js`).
5. **Scale.** `demo/knowledge-graph/make_big.py` makes a graph shaped like a big memory (projects of every size, a
   shared middle with hubs, ten families). At 20,000 things and 45,000 links (9.6 MB) the page answers in 0.44 s
   (its longest task 0.28 s), every island has settled by 1.8 s and bloomed by 3.2 s, and it holds 60 frames a second
   in every look on a laptop's GPU: at rest, zooming, zoomed deep among the names, dragging, with the most linked
   thing (431 links) chosen. 31,700 and 60,000 links settle by 1.7 and 2.0 s; without groups, Louvain finds 80
   islands in 1 s of Python. One d3 simulation of every thing took 23 s with the page frozen; the 1,082-thing bank
   now opens in 133 ms instead of 768. Without a GPU (a remote desktop) the canvas is drawn on the CPU: past 6,000
   links they are laid plainly instead of adding light (the same on a dark page), and wherever WebGL names a software
   renderer they stay hairlines, as a line over one device pixel wide stalls a CPU canvas for most of a second;
   there it runs at about 40 frames a second at a pixel ratio of 1. CI builds the 20,000-thing graph and checks that
   it answers, settles, finds, drags and errs nowhere (`tests/kg_scale.js`).

---

## 6. Tests

```bash
python3 tests/acceptance.py            # 46 checks, A1–A20, A24, A25–A49, with the fake dreamer, about 30 s
python3 tests/e2e.py                   # one run on both read paths: dream, ask, a file gone by hand, drop a note, the end of a line, a folder, absorb a base
python3 tests/retrieval_gate.py bank   # the model-free numbers with floors (README Results); `software` for the second fixture
python3 tests/kg_tags.py               # the knowledge graph's tag columns through graph_page.py: CSV, JSON, parents, --colour
MEMORY_STORE_URL=postgresql://… python3 tests/store_parity.py postgres --bank   # needs psycopg: the PostgreSQL store (ADR-001)
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
python3 eval/stability.py <W>/memory   # the same answer under 3 hash seeds, 2 file orders, no grep, alone and in company: all zeros
```
Expect 0.937 / 0.980 at 1,677 notes on the fake-indexed world (0.895 / 0.972 before the lineage one-liners;
0.946 / 0.978 on a real Haiku index, 0.938 / 0.979 with `MEMORY_NO_INDEX=1`). `adversarial.py` measures the sets
where grep should lose: stale-vs-current (successor above the old note 0.97, old marked 1.00), scattered
evidence (all gold 0.78 at 2.2k chars on the fake index, 0.79 at 2.3k on the real one, vs 0.99 at 12.6k for `cat`
of the folder), absence (70 questions about things the memory does not hold: ask says "(no match" or marks
the unknown id or word, 70 of 70), alias traps (needs a real index for its surface
forms: 0.93 with or without the index vs 0.43 for an exact-phrase grep on the 70-note world's 14 forms; the full
bank's 280 forms: 0.89 with the index, 0.83 without, 0.52 grep). `MEMORY_NO_INDEX=1` switches `ask`'s use of the index off, for such comparisons.

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

On the shipped code unless a cell says otherwise (README "Results" has the same numbers with their sources).

| measure | 30 notes | 1,677 | 168,141 |
|---|---|---|---|
| retrieval: gold notes / numbers | 1.00 / 1.00 (the software fixture, 30 questions) | 0.939 / 0.979 with no index, 0.941 / 0.978 with the index (326 questions; both gated in CI) | 0.854 / 0.950 (round 4, earlier code, not re-run) |
| `ask`, 10 questions | < 1 s | 0.5 s | 2.3 s (round 4) |
| agent cost vs grep | 0.93× (round 2, earlier code) | 0.61× cost units (phase G, real index, n = 3 batches per arm: tool calls 0.30×, tokens 0.29×, time 0.75×, accuracy tied 23/7/0); 0.47× in round 2 on earlier code | 0.41× (round 4, earlier code) |
| $ per new note (Haiku) | 0.0013 (60-note world) | 0.0016 (phase I: the whole bank for $2.69; 0.0020 before the cached prefix) | 0.0015–0.0019 |
| dream, nothing new | — | 0.7 s | 3 s |
| dream, 30 new notes (with Haiku) | — | — | 82 s, 4.8 GB |
| viewer | 1 page | 3.0 MB | 2.4 MB overview + ~110 KB per area |
| the same answer on another run or machine | yes (A42) | yes: 1,149 questions, 0 differ (phase J, `eval/stability.py`) | not re-run |

Taste retrieval (the holdout tasks, `eval/taste/score.py`, recall of the gold notes, no index): the person's
preferences 0.95 when the task names them, 0.84 when it names only their meeting or audience; house rules 0.50
(phase J). At the taste layer's first cut these were 0.93 / 0.57 / 0.42, and before it 0.76 / 0.35 / 0.25.

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
| the same question printed other notes on another run or machine | float sums added in a set's order; ties left to the order grep listed the files in; a task reading lines its neighbours matched; a headline tie going to the newer file; the no-grep matcher returning the registries | exact sums (`math.fsum`), every sort ends on the path, a task reads its own lines, headline ties go to the path, the matcher skips the registries (A42, `eval/stability.py`) |
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
