# memory-dream v0.4 — results

2026-10-30 · built from the "Memory" email spec (`build-spec.md`) · macOS, Python 3.9.6, Claude Code 2.1.314.

# Round 3 — refined: drop what didn't help, curate entities and the relation vocabulary

## What was dropped, and the evidence

In the 9 round-2 memory-agent runs (33 tool calls), agents used `memory.py ask` 9 times (once per
run), shell `cat` 20 times and shell `grep` 17 times. They used `where`, `trace`,
`memory.py grep`, INDEX.md and SKILL.md 0 times. So all of these went:

| dropped | why |
|---|---|
| `where`, `trace` | replaced by `ask` for answering, and by the viewer for browsing |
| `memory.py grep` | agents use native grep |
| INDEX.md | never read; `dream` now writes `_dream/graph.html` |
| gists (`--gists`), dreamer summaries | used by nothing |
| open relation vocabulary, and the review's "new type" answer | grew EDGES.md from 7 to 185 types |
| 300-entity KNOWN list | about 9k-token prompts; now this project's entities ≤ 80 plus shared ≤ 20 |

`memory.py`: 1,610 → 1,292 lines. Verbs: `ask`, `dream`, `viz`, `check`, `log`. A1–A20 were
rewritten for the refined design and all 20 pass. A20 now tests vocabulary and identity in place of
gists.

## How entities and the relation vocabulary are kept

- **Relations: a closed vocabulary of 8 types** in EDGES.md: uses, produces, part-of, trained-on,
  evaluated-on, measured-by, replaces, owned-by.
  - Each type has aliases (`~` = read in reverse), and there is a `drop:` list. Both were grown from
    the 508 type names Haiku actually wrote on the 56× bank.
  - The dreamer may use only these. Anything else is held back at merge and counted (C7).
  - A type used 3 or more times goes to the review, which may only answer `alias T`, `alias ~T` or
    `drop`. New types come from a human editing EDGES.md.
  - The review prompt names what to drop: claims (lifts, beats, improves), note-to-note links
    (answers, led-to, basis-for) and conversations (asked-by), and "when unsure, drop".
- **Entities: kept only when they mean something across notes.**
  - An entity is kept when it has a home note (a note whose slug is its id, e.g. the model's own
    note), is mentioned in 2 or more notes, or is named in ALIASES.md.
  - Files, notebooks, columns and note ids are not entities; grep finds them.
  - Ids fold `.`, `_`, `-`, spaces and case (`cards.txn_daily` = `cards-txn-daily`).
- **Dedup:** folding and the surface-form rule are free. Versions never merge. Two entities with
  different home notes are never queued for review. Other look-alikes are asked once, and the
  answer lands in ALIASES.md (`- a = b` or `not: a / b`).
- **Lineage stays separate:** `from:`, `supersedes:`, and note ids written in a body link notes with
  no model and no vocabulary.

## Effect on the 56× bank (same Haiku extractions; re-merged with 0 extraction calls)

| | before | after |
|---|---|---|
| relation types | 508 written, 185 in EDGES.md | 8 |
| relations in the graph | 4,559 | 3,166 |
| entities | 2,276 | 1,545 (941 tied to their home note) |
| entities that link nothing (one note, no home) | 873 | 0 |
| files and notebooks as entities | 51 | ~7 (name heuristics) |
| unknown types awaiting review | 323 | 0, after one review call ($0.0066): 3 mapped, the rest dropped |
| entity pairs awaiting review | 147 | 28 |

Retrieval is unchanged within noise. `ask` gold-note recall:
- small bank: 0.927 → 0.915
- 56×, indexed: 0.879 → 0.878
- 56×, no index: 0.892 → 0.892

Answer-number recall stays at 0.97. The agent-level results of round 2 still stand: the read path
(`ask`) is the same.

## What indexing costs (Haiku through `claude -p`, refined prompt, measured on 60 notes)

| per note | before refinement (56× bank) | refined, default effort | refined, `--effort low` |
|---|---|---|---|
| cost | $0.0035 | **$0.00133** | $0.00113 |
| input tokens, median | 14.8k | 5.9k | 6.0k |
| output tokens, median (incl. thinking) | 2,525 | 1,398 | 1,021 |
| seconds per call, median | 10.4 | 6.5 | 4.6 |
| `ask` gold-note / number recall, 46 questions | — | 0.866 / 0.958 | 0.866 / 0.958 |
| grounding drops (C4) | — | 1 | 7 |

- **Whole 56× bank:** about $2.2 and about 20 minutes at `-j 10`, against $5.95 and 45 minutes
  before. Low effort is about $1.9; retrieval is unchanged, but it makes more unsupported claims,
  which grounding drops.
- **Steady state:** only new or edited notes cost a call. Moves, renames, deletes and edits to
  EDGES.md or ALIASES.md cost 0.
- **Dedup** (folding, surface rule, home notes, versions, union-find) uses no model: 0.12 s for
  1,000 notes.
- **Review:** at most 1 call per `dream`, only when something is queued: $0.0007–$0.0066.
- **File mode instead:** one `memory-dreamer` subagent answered 30 prompts in 186 s (131k tokens).
- **Where input tokens go:** much of each call's input is Claude Code's own prompt. A direct API
  call would be smaller (not measured).

## What one memory costs to save and to keep (measured inside the full 1,677-note bank)

| operation | model calls | cost | time |
|---|---|---|---|
| agent writes a note | none (part of its own turn) | ~150 output tokens of the session's model (notes average ~100 tokens) | — |
| `dream` indexes a new or edited note | 1 Haiku call | **$0.0020** (7.0k in / 2.3k out); $0.0013 in a small memory | 9.9 s, parallel |
| move, rename, delete a note | 0 | $0 | — |
| edit EDGES.md or ALIASES.md | 0 | $0 | — |
| dedup merge, graph, viewer | 0 | $0 | ~0.1 s per 1,000 notes |
| vocabulary review (only when something is queued) | ≤ 1 per `dream` | $0.0026 (28 pairs + 1 type) to $0.0066 (30 pairs + 34 types) | 8–34 s |
| re-index everything (`--all`) | 1 per note | ~$3.3 for 1,677 notes | ~25 min at `-j 10` |

At 20 new notes a day that is about $0.04 a day: about $1 a month for indexing and review. The
known-entity list that prevents duplicate ids is about 1.4k of the ~7k input tokens, roughly 8% of
the per-note cost.

## What dedup did on the 56× bank (`memory.py check`, `eval/dedup_report.py`)

| stage | count | change |
|---|---|---|
| entity mentions extracted | 10,005 | |
| ids as written | 2,397 | |
| after spelling folding | 2,382 | 15 merged |
| after ALIASES.md lines from the review | 2,369 | 13 merged |
| after the surface-form rule | 2,267 | 102 merged |
| kept | 1,545 | 941 with a home note, 604 in 2+ notes |
| dropped by the keep rules | 722 | 684 one-note, 38 file-like |

The review also wrote 46 `not:` lines.

Merge quality, by hand:
- **Spelling folds:** 8 of 8 sampled are right.
- **Surface rule:** about 10 of 15 sampled are right. Others are lossy: `psi = feature-psi = score-psi`,
  `churn-rate = churn`, `recovery-rate = net-recovery`.
- **Review merges:** about 9 of 12 are right. One is wrong: `control-group = randomised-control`, a
  distinction the corrections notes depend on.

The free surface rule and the Haiku reviewer both merge more eagerly than "when unsure, keep apart"
allows. Neither affects answers much (`ask` greps text), but the merges show up as aliases and in
the viewer.

## Is the 8-type vocabulary enough? (`eval/type_coverage.py`, `eval/question_relations.py`)

- **What Haiku writes when free to invent** (5,196 relation instances on the 56× bank, old open
  prompt):
  - 81.2% fit the 8 types (74.6% directly, 6.6% through an alias);
  - 5.5% are deliberately dropped (claims, note-to-note links);
  - 13.3% are unknown, spread over 449 names. The largest covers only 16 instances (0.3%: `prefers`).
- **What the 366 questions need** (labelled by Haiku):
  - lineage: 133 (36%);
  - the answer sits in a single note: 127 (35%);
  - one of the 8 types: 105 (29%), of which uses 50 and evaluated-on 38;
  - other: 1.
- **Answers don't hinge on it:** `ask` without any index is as accurate.
- **Not proven:** one domain, and notes, questions and labels all came from Haiku.
- **So extending must be free:** the dreamer now names links outside the vocabulary in 1–3 words.
  They are kept aside in the cache, not shown. A type added to EDGES.md later picks them up at the
  next merge. Demo (`eval/add_type_demo.py`): adding `prefers` and `predicts` brought in 8 and 4
  relations with 0 model calls. A listed type now wins over the drop line.

# Round 2 — a thin layer on grep, tested at 1× and 56×

## Verdict

Every target holds at both sizes. Fresh Opus subagents using the memory are at least as accurate
as a grep-only baseline. They cost less: 0.93× at 30 notes and 0.39–0.47× at 1,677 notes. And they
are faster: 0.75× at 30 notes and 0.35–0.44× at 1,677. Each cell is three runs of 10 questions,
judged by Haiku against reference answers.

| cell | correct / partial / wrong | tool calls | API requests | tokens processed | cost vs grep | time |
|---|---|---|---|---|---|---|
| small (30 notes) — memory | 26 / 3 / 1 | 1.3 | 2.3 | 104k | **0.93×** | 40 s |
| small — grep | 25 / 5 / 0 | 2.7 | 3.0 | 129k | 1× | 53 s |
| 56× (1,677 notes) — memory, Haiku index | **27** / 3 / 0 | 4.7 | 5.7 | 311k | **0.47×** | 61 s |
| 56× — memory, no LLM index | 26 / 4 / 0 | 5.0 | 6.0 | 324k | **0.39×** | 75 s |
| 56× — grep | 26 / 4 / 0 | 25.3 | 23.3 | 1,465k | 1× | 172 s |

Cost compares "cost units" per run: tokens weighted by Opus price ratios (fresh input 1, cache read
0.1, cache write 1.25, output 5). Data: `eval/agent/summary.json`; answers in `eval/agent/runs/`;
verdicts in `eval/agent/judge-*.json`.

## Why round 1 cost 2.3×

It was round trips, not note size. Every API request re-sends the subagent's context: at least 37k
tokens of system prompt, tools and history. Round 1's SKILL.md told agents to look up, then read
each pointer, one question at a time. That loop took 16–20 requests where grep took 3.

At 30 notes the whole corpus is about 3k tokens. INDEX.md alone was 70% of the corpus, so it
compressed nothing, and one `cat` of everything was the cheapest possible plan.
(`eval/a21/calls.py` lists every call of every run.)

## What changed: grep plus memory, not a replacement for grep

- `memory.py ask "q1" "q2" …` takes every question in one call:
  - The graph expands each question into grep patterns: note ids, entity aliases, and the project
    named in the question, which then scopes the search.
  - One real `grep -F` pass finds the lines.
  - Notes are scored by idf-weighted pattern hits; a hit on the title or in the slug counts double.
  - Then the graph orders them. Named notes come first. Superseded notes lift their successors.
    "What came of X" walks down the `from:` links; "what led to X", "why" and "depends on" walk two
    hops up. For "why" questions about a replaced note, the walk goes up from its successor.
  - Output is `line: text` under `▸ path · kind · date · from … · SUPERSEDED → newer`, i.e.
    surgical lines from the original files. When everything relevant fits the budget (small
    memories), it prints whole notes instead.
- `memory.py grep <grep args>`: plain grep over the notes, with the same headers per note.
- Lineage without a model: a slug-like note id written in a note's body counts as a `refs` link
  within its project. Log notes take their date from the `log/YYYY-MM-DD` filename.
- SKILL.md policy: one `ask` call with every question, answer, and at most one batched follow-up.
  The skill description, which agents see without loading the skill, names the command, so the
  skill body never has to be read just to answer.

## The 56× bank (written by 12 Haiku subagents)

- **Projects:** 40, each with 30 notes in real chains: question → experiments → findings →
  decisions → new versions, with at least 2 supersessions per project.
- **General memory:** 300 notes across `prefs/` (people's taste and working preferences),
  `reporting/` (conventions), `glossary/` (terms), `corrections/` (wrong definitions or
  understandings, each superseding what it corrects), `howto/` (analysis practice) and `qa/`
  (saved question-and-answer notes).
- **Size:** 1,499 notes plus 149 log days. Adding the churn-2026 fixture gives 1,677 files and
  653 KB, about 190k tokens.
- **Questions:** 326, each with gold notes, written by the same authors. Plus 30 more churn-2026
  questions from a 13th agent.
- **Validation** (`eval/bank/split.py`): 0 notes over 40 lines, 0 without a title, 1 of 2,190
  `from:` links unresolved, 0 of 209 `supersedes:` links unresolved.

## Offline retrieval (no LLM): did the answer's evidence come back?

| bank | questions | gold-note recall | answer-number recall | chars per question |
|---|---|---|---|---|
| small, Haiku index | 40 | 0.93 | 0.97 | 1,200 |
| 56×, no index | 326 | 0.89 | 0.97 | 1,975 |
| 56×, Haiku index | 326 | 0.88 | 0.97 | 2,210 |

`python3 eval/retrieval.py <memory root> <questions…>`. Weakest types are "current" (26 of 40
miss at least one gold note or number) and "dependency" (21 of 40); some of those are strict gold
lists (the gold names the superseded version too).

## Is the Haiku index worth it? For retrieval, no; for management, yes

- **Cost:** indexing 1,677 notes took 1,677 calls plus 1 review call, $5.95 and about 45 minutes
  at `-j 10`. The KNOWN entity list makes each prompt about 9k tokens.
- **Retrieval value:** neutral. The index's loose entity names made `ask` worse (gold-note recall
  0.86 vs 0.88), so `ask` now uses the index conservatively:
  - aliases expand only through short names;
  - entities are matched by name, not by long descriptions;
  - the boost is smaller for phrase matches.

  With that, indexed and unindexed are within noise offline and at agent level (27 vs 26 correct).
  The indexed agent runs used the ranking from just before the last why/current tweak, which is
  worth +0.8 pt offline.
- **Where it pays:** entity aliases and typed relations ("what uses `cards.txn_daily`" across 27
  projects), the viewer, and review.
- **Problem found:** with Haiku as reviewer, all 178 proposed relation types with 2 or more uses
  were answered "new". EDGES.md grew from 7 types to 185, and 470 vocabulary items still await
  review (C7). The review needs a stricter prompt or a cap.

## Viewer (for visualization and management)

`memory.py viz` writes `memory/_dream/graph.html`, self-contained with no CDN and built to the
html-harness habits (10/10 under `map.py`). It has three tabs:
- **Overview:** every project and area with note counts by kind, last update, superseded and
  warning counts.
- **Explore:** search plus a radial neighbourhood for a note (built on, built upon by, supersedes,
  entities) or an entity (depends on, used by, mentioned in), and a detail panel with the note text
  and links.
- **Health:** warnings by code, all 211 superseded → current chains, unlinked notes, and the review
  queue.

Deep links: `#note=<path>`, `#entity=<id>`, `#health`. It renders with 0 errors and 0 AA contrast
failures in light and dark mode. Screenshots are in `eval/viz/`.

## Caveats

- The judge is Haiku, with n = 30 questions per cell, so a one-question difference is noise.
  Several "partial" verdicts say "substantively correct".
- Each run answers 10 questions in one session, which lets grep spread its reads across questions.
  One fresh agent per question would favour the one-call design more; that was not measured.
- The questions were written by Haiku. Churn-2026 questions written for the small bank are
  ambiguous in the big one ("the current churn model" could be churn-2025's).
- `memory.py` is 1,610 lines against the spec's ~600.

## Next refinements

1. Make the dreamer optional for answering and keep it for aliases, relations and the viewer.
   Cap the KNOWN list per project, which should roughly halve indexing cost.
2. Gate the vocabulary review: accept a new type only with a definition distinct from every
   existing type, and cap new types per review.
3. Run single-question agents, and use a stronger judge.
4. Improve "current" and "dependency" retrieval: follow the successor's relations, not only its
   lineage.
5. Test the write path: agents writing notes under the SKILL rules.

# Round 1 — the spec as written

## Verdict

The tool works to spec: **A1–A20 pass** with a deterministic fake dreamer. A3, A10 and A18 also pass
with real Haiku, both in command mode and through a `memory-dreamer` subagent. **A21 is mixed.**
Fresh Opus subagents using the memory answered 30/30 questions correctly, against 28/30 for a grep
baseline. But on this 30-note fixture the memory runs cost about 2.3× more than the baseline, so A21's
"the index must cost less than the baseline" **fails at fixture scale**. Whole corpus: 9.4 KB.
INDEX.md alone: 7.5 KB. At that size grep agents simply `cat` every note in one call.

## Acceptance (spec §13)

| id | result | evidence |
|---|---|---|
| A1 | pass | empty `memory/` → INDEX.md, graph.json, EDGES seed, ALIASES header; exit 0 |
| A2 | pass | no model: 26 lineage edges exactly as written, both supersessions, `trace` on notes, `where` from titles + grep; C5 = 30 |
| A3 | pass (fake + **real Haiku**) | Haiku: 30 notes → 30 calls, $0.0452, 60 s at `-j 6`; second `dream` 0 calls |
| A4 | pass | 5 moved + 2 renamed: 0 calls, "7 moved", no C2, `from: exp-014` resolves to the renamed note; graph identical modulo paths |
| A5 | pass | edited note drops out of entities/relations immediately, listed under `unindexed`; next `dream` = exactly 1 call |
| A6 | pass | deleted dec-risk-tiers (named by 2 `from:`): nothing derived from it remains, `offers.tier_matrix` gone, 2 headlines moved, C2 ×2, 0 calls |
| A7 | pass | revert → cached extraction reused, 0 calls |
| A8 | pass | fabricated `as`, absent quote, ungrounded number → all dropped, C4 = 3, summary → title |
| A9 | pass | prose- and fence-wrapped answers parsed; invalid JSON → 1 retry → C3 |
| A10 | pass (fake + **real subagent**) | Haiku subagent answered 30/30 prompts, 0 failures, C4 = 0; forced review round answered and applied (`snapshot-of` → new type) |
| A11 | pass | uses / trained-on / evaluated-on / owned-by with valid `path:line` evidence; `trace cards.txn_daily --down` lists v2, v3, utilization, churn-xgb-v2/v3 |
| A12 | pass | `fitted-on?` ×2 live; review → `alias trained-on` appended to EDGES.md; relabelled with 0 extraction calls |
| A13 | pass | "the txn table feeds the velocity features" → `feat-velocity-v2 uses cards.txn_daily` (txn-backfill.md:6) |
| A14 | pass | hand-folding trained-on into uses relabels everything, 0 calls |
| A15 | pass | `Cards.TXN_daily` and `txn-table` merge free; v2/v3 (both "velocity features") never asked; risk-tier pair asked once → ALIASES.md; next `dream` asks nothing |
| A16 | pass | `- cards.txn_daily = ds-txn` moves relations and pointers, 0 calls |
| A17 | pass | `where feat-velocity-v2` headline = post-period-leak; after deleting it → feat-velocity-v3 (§5.1 order), 0 calls |
| A18 | pass (**real Haiku**) | command mode 21 ids / 20 true entities = **1.05×**; subagent file mode 20 / 19 = **1.05×** (target ≤ 1.2×); review merged nothing further |
| A19 | pass | 1,000 notes / 1,900 entities / 2,900 relations: merge 0.12 s, `where` 0.06 s (0.17 s after an edit forces a re-merge), review candidates for 200 new ids 0.35 s |
| A20 | pass | 14 gists (entities in ≥ 3 notes), ungrounded numbers dropped, `key` filtered to real notes, rerun 0 calls, deleting a cited note hides the gist |
| A21 | **mixed** | accuracy ✓ (30/30 vs 28/30); cost ✗ at 30 notes (see below) |

Rerun: `python3 tests/acceptance.py` (≈ 10 s); real-model steps in RUNBOOK.md.

## Real dreamer runs

| | command mode (`claude -p --model haiku --tools ""`, isolated) | file mode (`memory-dreamer` subagent, Haiku) |
|---|---|---|
| work | 30 calls + 1 review call | round 1: 30 prompts in one agent (92 tool calls, 131k tokens, 186 s); round 2: review (5 tool calls, 41k tokens) |
| cost | $0.0452 extraction + $0.0009 review (≈ 4.4k in / 2k out per call incl. thinking) | not priced by the harness; token count above |
| grounding drops (C4) | 2 (a `churn-2026` entity not in the note, one quote) | 0 |
| entities / relations | 58 / 69 | 39 / 37 |
| proposed types | 14 single-use (C7 ×14); 2 with ≥ 2 uses → review → `has-metric`, `implemented-by` as new | 1 (`snapshot-of`) → new |
| A18 | 1.05× (split: `recall@10` / `recall-at-k`) | 1.05× (split: `cards-txn-daily` / `txn-table`) |

One agent answering every prompt keeps ids consistent across notes without the KNOWN list doing
anything. It also extracts fewer junk entities. Command mode calls are independent and cheaper per
note, but noisier.

## A21 — fresh Opus subagents, 10 questions, n = 3

Each run: one fresh Opus subagent answering all 10 questions. Memory runs got the Haiku-indexed
memory plus SKILL.md. Grep runs got the same 30 notes and a one-paragraph description of the note
format. Answers: `eval/a21/runs/`. Grading against key facts: `eval/a21/grade.py`. Numbers:
`eval/a21/summary.json`.

| per run (mean of 3) | memory | grep baseline | ratio |
|---|---|---|---|
| questions fully correct | **10.0** (30/30) | 9.3 (28/30) | |
| tool calls | 19.3 | 2.3 | 8.4× |
| API requests | 18.3 | 3.0 | |
| tokens, harness-reported | 67.2k | 51.8k | 1.3× |
| tokens processed, all requests (≈ 96% cache reads) | 960k | 130k | 7.4× |
| cost units (Opus price weights) | 222k | 97k | **2.3×** |
| wall time | 141 s | 66 s | 2.1× |

Per question: memory ≈ 1.9 tool calls and 22k cost units; grep ≈ 0.2 tool calls and 9.7k.

The two grep partials: grep-2's Q2 omits the velocity-v3 rebuild. grep-1 says "the v3 rebuild",
which the regex misses, so it is arguably correct. All six runs had the same headline facts. They
also flagged the same gaps in the notes (no v3 tenure split, the unexplained 0.74→0.76 gap, the
October backfill).

Why the index lost:
- The grep agents ran `cat` over every note once and answered all 10 questions from that.
- The memory agents followed SKILL.md literally, one question at a time: read the INDEX head, `where`
  or `trace`, then read the notes it pointed to. That loop meant 16–24 turns, and every turn re-reads
  a ~50k context.
- Design caveat: one session per run lets the baseline spread its single read over all 10 questions.
  Ten one-question agents per run would hurt grep more. A corpus big enough that `cat` stops being an
  option (hundreds of notes) is where the index should win. **Neither variant was run.**

## Deviations from the spec

1. **`memory-dreamer` cannot list files.** This Claude Code build has no Glob tool, and Read does not
   list directories. The spec'd agent (Read, Write, Glob) wrote nothing on its first try. Fix:
   `dream` now writes `_dream/pending/TODO.md` with every unanswered prompt path, and the agent text
   says to read it. Glob stays in `tools:` for builds that have it.
2. **`memory.py` is 1,261 lines** against "≤ ~600". Everything in §4–§8 is implemented in one stdlib
   file: grounding, both vocabularies, review, gists, file and command mode, move detection,
   freshness. It is not compacted.
3. **`check_skills.py` is not on this machine** (or in the email), so R9/R10/R12/R15 are unverified.
   What was checked by hand: SKILL.md is 25 lines with `name` and `description` frontmatter; the
   subagent lives in `agents/`; nothing hook-dependent.
4. Small choices the spec leaves open:
   - command mode runs calls in waves of `-j` and refreshes KNOWN between waves (no extra calls)
   - `trace -e` forces an entity walk when a note has the same name
   - C4 counts dropped items, not notes
   - a C3 note is retried at the next `dream`
   - `where` prefers a body line over a frontmatter line as the pointer

## What to change next

- **SKILL.md read loop.** For small memories, tell the main agent to read the INDEX body and `cat`
  the project's notes in one call. Or give `where` an option that prints the pointed lines inline, so
  "read what it points to" is not one call per note.
- **Extraction noise.** 37 of command-mode Haiku's 58 entities are columns, notebooks, code files,
  project or note ids. Tell the prompt "not columns, files or notebooks". Or drop entities whose id
  equals a note stem (`exp-014`, `ds-txn-2025q4`).
- **Proposed-type sprawl.** Single-use types never reach the review (gate ≥ 2) and sit in C7
  forever. Consider sending them after N days, or listing them in the review prompt as a batch.
- **Headline signal.** "Named on the title line" dominates. With Haiku's loose surface forms ("30-day
  velocity"), exp-014, not post-period-leak, became the headline of `feat-velocity-v2`.
- **Re-run A21 at scale** (≈ 300 notes, several projects) before judging the index on cost.
