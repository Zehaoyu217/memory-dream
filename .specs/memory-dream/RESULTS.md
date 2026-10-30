# memory-dream v0.4 — results

2026-10-30 · built from the "Memory" email spec (`build-spec.md`) · macOS, Python 3.9.6, Claude Code 2.1.314.

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
