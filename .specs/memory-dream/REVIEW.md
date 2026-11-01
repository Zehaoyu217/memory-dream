# memory-dream v0.4 — review

2026-10-31. Reviewed: `skills/memory-dream/` (memory.py 1,897 lines, SKILL.md, viz.html, the dreamer agent), the
acceptance tests, RESULTS.md rounds 1–4, and the eval data in `eval/`. Everything below marked **measured** was run
in this session on the committed code; nothing here used a real model. No agent runs were made, so agent-level
claims are quoted from RESULTS.md.

The brief: the skill should stay simple and robust, always beat a smart agent that uses grep/glob over a
hand-written memory (faster, cheaper, more accurate, better), produce maintenance and the viewer as a free byproduct,
and let subagents resolve conflicts.

---

## 1. Verdict

| criterion | verdict | evidence |
|---|---|---|
| faster and cheaper than a grep agent | **yes from a few hundred notes up; a wash below.** 0.47× cost / 0.35× time at 1,677 notes, 0.41× / 0.42× at 168k; 0.93× / 0.75× at 30 notes | RESULTS rounds 2 and 4 (Opus agents, n = 30 questions per cell) |
| more accurate | **a tie, not a win.** 27/3/0 vs 26/4/0 at 1,677; 24/6/0 vs 24/6/0 at 168k. Offline, `ask` heads 89% of gold notes at 1.9k chars per question; an agent that `cat`s the named project folder heads 99.7% at 12.6k chars | measured, §3 |
| better quality | yes in form (surgical lines under lineage headers, SUPERSEDED marks, preferences attached to tasks); not measured beyond accuracy | RESULTS; eval runs |
| simple | **architecture yes, implementation no.** Notes are the truth, `ask` is grep plus lineage, the dreamer is optional: three ideas. But memory.py is 1,897 lines against the spec's ~600; `dream()` is 242 lines; retrieval carries 58 tuned numeric constants | measured, §5 |
| robust | **good.** 14 malformed-input probes passed; failing, hanging and garbage-returning model commands are handled. Four real defects found (§4: F2, F3, F4, F10) | measured, §4 |
| maintenance and viewer free | **mostly.** The viewer and health checks render with no model at all (verified in Chromium); dedup, move detection and vocabulary edits cost 0 calls; the review is ≤ 1 call per dream; indexing is $0.0013–0.0020 per new note. Not free: entity names, types and typed relations need Haiku, and without it every note's kind is "note" (0 of 1,677 bank notes carry `type:`) | measured + RESULTS |
| subagents resolve conflicts | **partly.** Vocabulary and entity-pair reviews are already delegated (file mode → `memory-dreamer`). Conflicts between notes (two live notes that disagree) are neither detected nor queued | code reading |
| works alongside Claude Code's own memory (CLAUDE.md, auto memory) | **done in phase B** (was: `ask` worked read-only, `dream` would wrongly write there). Design in §8; results in RESULTS.md "Phase B" | measured, §8 |

Overall: the design is right and the evidence behind it is unusually honest. The read path is close to its ceiling
on the test bank. The gaps are (a) the small-memory case, where `ask` prints more than the whole memory,
(b) a handful of robustness defects, (c) implementation weight, and (d) the missing conflict queue. None of them
needs new machinery; all of them fit the existing shape.

---

## 2. Can it "always win, no matter how smart the agent"?

Both sides read the same notes, so the accuracy ceiling is the same. What the skill can own is the number of
turns (each turn re-sends ~37k tokens of context, RESULTS round 1) and the number of tokens read. A smart grep agent
has three good strategies, and the skill must beat each:

| the agent's best move | when | what it costs the agent (measured, 326 bank questions, 1,677 notes) | `ask` |
|---|---|---|---|
| `cat` everything | tiny memories | 9,410 chars for the 30-note fixture, 100% recall, one call | 11,325 chars for 10 questions (budget 10,500) — **`ask` loses here** |
| `cat` the named project folder | the question names a project (230 of 326 do) | 12,638 chars per question, gold notes 0.997, one call per project | 1,902 chars per question, gold notes 0.89, one call for everything |
| grep, then read the top files | unscoped questions | one grep printing every matching line: 63,001 chars per question for 0.90; grep then `cat` the top 8 files: 2,900 chars for 0.61; ids only then `cat` ≤ 8 files: 2,382 chars for 0.48 | 1,978 chars for 0.89 |

So the structural win is real and large wherever the memory is too big to `cat`: 6× fewer characters than
folder-`cat` and one turn instead of one per project, at a cost of about 10% of gold notes not being headed
(the answer's numbers are still present 97% of the time). The one place `ask` loses outright is the tiny memory, and
that is fixable for free (F1). "More accurate than an agent with unlimited budget" is not achievable by any read
tool; "never less accurate at equal budget, and far cheaper at equal accuracy" is, and is nearly where the skill is.

What the "current" misses are (measured, 40 current-type questions, 29 gold notes missed): 15 are superseded notes
the gold list still names (history), 8 are live notes whose successor or lineage neighbour was printed, 6 are
genuine misses. A recency tie-break for "current" questions, tried in a scratch copy, changed nothing. The eval
overstates the gap; ranking tweaks are not where the gains are.

---

## 3. Measurements made for this review

All on the committed code, Python 3.13, GNU grep. Worlds built from `eval/bank/assemble.py` (1,677 notes) and the
churn-2026 fixture (30 notes). The entity index, where used, came from `tests/fake_dreamer.py` (0 cost); RESULTS
shows the real Haiku index is within noise of it for retrieval (0.878–0.882 vs 0.888).

| measurement | result |
|---|---|
| `tests/acceptance.py` | 21/21 pass, 23 s |
| offline retrieval, 326 questions, no index / fake index | gold 0.892 / 0.888 · numbers 0.969 / 0.969 · 1,978 / 1,984 chars per question |
| misses by type (no index) | current 26 · dependency 21 · why 17 · numeric 16 · lookup 13 · lineage 10 · correction 2 |
| grep-only strategies | see §2 table |
| fixture, 10 A21 questions | `ask` 11,325 chars; whole memory, compact (paths, titles, body lines) 9,410 chars; 1 question 2,269; 3 → 3,678; 5 → 6,778 |
| table-of-contents fallback (titles of the named project's unprinted notes) | +2,924 chars per scoped question; would cover 228 of 230 scoped questions' gold notes — too expensive as a default |
| taste, 52 tasks (`eval/taste/score.py`) | named person's prefs 1.00 · implicit (meeting or audience named) 0.72 · house rules 0.39 · 3,083 chars per task |
| taste, cap 6 → 12 notes, floor 0.25 → 0.15 (scratch copy) | 1.00 · 0.77 · 0.42 · 3,857 chars |
| taste, cap 12 + two-hop person (a person named in a matched reporting note brings their prefs) | 1.00 · **0.85** · 0.41 · 3,849 chars; retrieval unchanged |
| gold rules per task | mean 4.2 (reporting/ + howto/); a digest of all 100 rule titles is 8.6k chars |
| viewer, headless Chromium, with and without the dreamer | renders Map/Overview/Explore/Health and the `#note=`, `#entity=`, `#health` deep links with 0 console errors; 81 KB / 73 KB |
| `ask` after one edited note, 1,677 notes (in-memory rebuild below `MEMORY_WIDE`) | 0.18 s → 0.58 s; projected ~4 s at 10,000 notes |
| kinds without a model | 0 of 1,677 notes carry `type:`; filename prefixes exp/feat/ds/dec/fnd/find/q cover 1,059 of 1,500 bank notes (71%) |
| deterministic identifiers (backticked or dotted names) as free entities | fixture: 4 of the 20 true entities; bank: 158 ids, 48 in ≥ 2 notes — too thin to replace the dreamer on this data |
| conflict candidates, crude heuristic (same project, both live, both `dec-`, no lineage between them, a shared title token) | 36 pairs across 26 projects; precision not measured |
| complexity | 64 top-level defs; longest `dream` 242, `ask` 137, `merge_entities` 103, `write_viz_big` 85, `rank` 80; 58 tuned numeric literals (22 distinct) in retrieval, 14 in merge, 19 in dream, 12 in viz; 49 regex literals; 5 env knobs |

Robustness probes that passed (no crash, sensible output): YAML-list frontmatter (`from:\n  - a`), bare
`supersedes: x`, CRLF line endings, unclosed frontmatter, nested folders (`project/sub/note.md`), a UTF-8 title with
symbols, latin-1 bytes in a note, an empty file, two notes that supersede each other, a question of regex
metacharacters and quotes, `-p` naming a missing project, an empty `memory/`, a model command that exits 1 (C3 after
one retry, 0.2 s), one that hangs (`MEMORY_TIMEOUT` honoured, C3), one that returns wrongly typed JSON (ingested
as an empty extraction), and `ask` with no `_dream/` at all (0.15 s).

---

## 4. Findings

Severity: **H** changes an answer or hides a note · **M** costs money, time or trust · **L** cosmetic or rare.

| # | sev | finding | evidence | fix |
|---|---|---|---|---|
| F1 | H | On small memories `ask` prints more than the whole memory and still misses notes. The best grep agent `cat`s everything in one call and is complete | 11,325 vs 9,410 chars for 10 questions on 30 notes | when the compact dump of every note fits the budget (900 per question + 1,500), print the whole memory grouped by area with SUPERSEDED marks; the surgical path only above that. Complete and cheaper, by construction |
| F2 | H | Project scoping fails for single-word folder names the stemmer shortens: `pricing` → `pric`, `collections` → `collection`, `prefs` → `pref`. The question "in pricing" is not scoped | measured: `pats={'pric': 1.0, …}`, scope empty, two unrelated churn notes printed | match folder names against the raw lowercase tokens before stemming |
| F3 | H | A note containing a NUL byte is skipped by `grep -I` as binary and never surfaces; `check` says nothing | measured: `zebra-nul` → "no match" | `check` warning C9 "binary-looking note", or grep with `-a` |
| F4 | M | Confident false positives: a question with no real match still prints a note, headed like a hit | "what is the meaning of zxqv?" → stem `mean` → `finding-new-accounts.md` printed | when no id, title or path hit exists and the best score is below an idf floor, print `(weak match)` on the header or "no match" |
| F5 | M | The entity index is neutral for answering (0.888 vs 0.892 gold recall; identical miss pattern) yet `ask` carries ~60 lines of entity boosting, multi-word name matching and `entity_line` | measured; RESULTS round 2 says the same | keep alias expansion for ids the question names; measure dropping the rest. If neutral, delete it. The index then serves the viewer and management only, which is what the evidence supports. **Measured on a real Haiku index of the whole bank (RESULTS F4, F9): the boosts stay at one weight (the phrase tier and the finding/decision multiplier measured nil); with lineage one-liners on for every question the index is worth +0.8 points gold recall and +6.4 on alias questions for +4.8% characters — kept** |
| F6 | M | Without the dreamer every note is kind "note": the viewer's lanes, the health counts and any kind-aware rule are empty for free users | 0/1,677 `type:`; prefixes cover 71% | filename prefix → kind (`exp-` experiment, `feat-` feature, `ds-` dataset, `dec-` decision, `fnd-`/`find-` finding, `q-` question, `prefs/` preference, `glossary/` term, `corrections/` correction, `howto/`/`reporting/` rule); frontmatter and the dreamer override. 0 calls |
| F7 | M | Implicit audiences miss 28% of the person's preferences; house rules 61% | 0.72 and 0.39 | two-hop person rule: 0.72 → 0.85 at +25% chars (measured). House rules are capped by the 6-note print cap against 4.2 gold rules per task plus prefs; raising the cap to 12 gives +3 pts for +25% chars. Rules keyed by measure type (rates, percents, CIs) cannot be found from task words; an always-on digest costs 8.6k chars and is not worth it. Accept ~0.4 and let the one batched follow-up grep `reporting/` |
| F8 | M | No note-level conflict detection or resolution queue | code; 36 crude candidates on the bank | §6, phase C. Precision on the real index (RESULTS F9): 4 true of 67 candidates, kept loose because a Haiku review of 20 pairs costs $0.005 |
| F9 | M | Implementation weight: `dream()` 242 lines mixing scan, planning, two call modes, review, cache upkeep and output; 58 tuned constants in retrieval with no table or provenance; legacy bits (INDEX.md cleanup, `SKIP` naming INDEX.md) | measured | split `dream` into stages; one `WEIGHTS` table with the measurement that justifies each value; delete legacy. Target ≤ 1,400 lines with 21/21 still passing |
| F10 | L | No lock: two concurrent `dream`s race on manifest.json and store.db | code | an `_dream/lock` file with pid and age; the second dream exits with a message |
| F11 | L | Below `MEMORY_WIDE`, `ask` after an edit rebuilds the whole graph in memory on every call until the next dream (0.58 s at 1,677, ~4 s at 10k); above it, it patches | measured | patch everywhere; the rebuild path then exists only inside `dream` |
| F12 | M | The evaluation does not measure the claim. Gold lists name superseded history (15 of 29 "current" misses); the grep baseline agent did not use its best strategy (folder-`cat`); runs are 10 questions per session, which favours grep; all notes, questions and judgements are Haiku-written; n = 30 per cell; the write path is unmeasured | RESULTS caveats; §2 | §6, phase E |
| F13 | L | Question terms are ASCII-only (`WORD`): non-English or accented words produce no patterns | code | `\w` with `re.UNICODE` |
| F14 | L | `scan` trusts mtime + size: an edit that keeps both (same-size write with preserved mtime) is missed until the next change | code | rare; document, or hash when mtime is older than the manifest's dream time |
| F15 | — | Prompt injection through a note is well contained: entities must occur in the text, relations must quote it; the review can only alias or drop types | code | keep; note it in the spec as a property worth protecting |

Not a finding but worth stating: the cycle `a supersedes b, b supersedes a` marks both SUPERSEDED with no loop,
which is the right degenerate behaviour; `check` could name it.

---

## 5. Simplicity, concretely

What is essential (keep): scan + manifest, `parse_note`/`note_facts`, `notes_part` (lineage), `ask`'s terms →
one grep → rank → print, the SUPERSEDED header, the taste block, the closed vocabulary, grounding, the review,
`write_viz`, `check`, `log`.

What earns its keep only at scale (keep, but isolate): store.db, index.db + `DbView`, routing, patching, per-area
pages. Together about 450 lines that only matter past 10,000 notes.

What the evidence says is neutral (measure, then cut or keep): entity boosts in `rank`, `multi_names`,
`entity_line` under "dep" questions, the `Known` wave refresh (a cost optimisation that matters only at 100×).

What is legacy (cut): the INDEX.md unlink, INDEX.md in `SKIP`, the `old_index` comment trail.

A reasonable shape: `memory.py` as one file still, but with five visible sections of ≤ 300 lines each and a
`WEIGHTS` table at the top of retrieval whose every entry cites the measurement that set it. The spec's 600 lines
is not reachable without dropping the big-memory layer; 1,300–1,400 is.

---

## 6. Recommended direction

Keep the architecture. Make `ask` unlosable at both ends, make the no-model path first-class, add the conflict
queue in the shape the review queue already has, then simplify, then sharpen the eval so it measures the claim.

**Phase A — never lose (ask).** F1 whole-memory print when it costs ≤ 1.2× the surgical output; F2 folder scoping
on the question's own words; F3 C9 for binary notes; F4 weak-match marker; F7 two-hop person rule and cap 12; and
hyphenated phrases searched as their words. **Done 2026-10-31** (RESULTS.md, "Phase A"): 26/26 tests; bank retrieval
0.888 / 0.969 → 0.897 / 0.972 at the same characters; implicit-audience prefs 0.72 → 0.83; the fixture's 10 questions
head 30 of 30 notes instead of 24. 0 model calls.

**Phase B — free byproduct, and Claude Code's memory alongside.** F6 prefix kinds; `dream` with no model documented
and tested as producing the full viewer and health page (it already does); SKILL.md states that the dreamer is
optional and what it adds (aliases, entity map, typed relations). Skip deterministic entity extraction: measured
coverage is too thin unless notes follow the backtick rule strictly. Then the five interop rules of §8: `ask` reads
Claude Code's auto-memory topic files in the same call (R1); `dream` and `log` refuse to write into Claude Code's
directories (R2); `dream` writes a ≤ 40-line `memory/DIGEST.md` the user can import from CLAUDE.md (R3); `modified:`
and Claude Code's `type:` values parse (R4); SKILL.md says which layer owns what (R5). Tests A30–A33. 0 model calls.
**Done 2026-10-31** (RESULTS.md, "Phase B"): 95% of bank notes kinded with no model, general areas 48 → 7, taste
implicit 0.83 → 0.87 and rules 0.42 → 0.46, digest 15 lines on the bank, Claude Code's directory read and never
written, SKILL.md rewritten for any agent with a shell at the same 606 words.

**Phase C — subagent maintenance queue.** Generalise `_dream/pending/` into the one place subagents work:
extraction prompts (exists), the vocabulary review (exists), and **conflict prompts** (new). Detection is
deterministic and free: same project, both live, same kind, no lineage path between them, a shared rare title
token or entity; dated. A subagent (or the dreamer in command mode) reads both notes and answers one of
`a supersedes b`, `b supersedes a`, `compatible`, `unsure`. Decisions persist in a user-owned
`memory/CONFLICTS.md` (`compatible: a / b`, `supersedes: a > b`) exactly as ALIASES.md does, so each pair costs at
most one call ever; `ask` honours a recorded supersession as lineage; `check` reports C10 "conflict pending"; the
Health tab lists them. Never edit a note automatically: the main agent or a person adds `supersedes:` to the note,
which is the truth. Before shipping, measure precision of the detector on the bank with Haiku (36 crude candidates
today; the heuristic needs kinds, which phase B supplies). Measured in phase F (RESULTS F9): 4 true of 67
candidates, 6%; kept loose since a Haiku review of 20 pairs costs $0.005 and found four missing `supersedes:` lines.

**Phase D — simplify.** F9, F10, F11, F13: split `dream`, the `WEIGHTS` table, patch everywhere, a lock file,
Unicode terms, delete legacy. Gate: 21/21 (plus the new tests) and retrieval within ±0.005 of today.
**Done 2026-10-31** (RESULTS.md, "Phase D"): `Dream` class in 15 methods, the `W` table, the lock, Unicode terms,
legacy removed; retrieval byte-identical. Not done, on evidence: F11 (the exact rebuild is 0.6 s at 1,677 notes) and
the F5 cut (the entity boosts measured +2 pts of number recall on the real-indexed world). The file is 2,446 lines:
phases A–C added about 550 lines of features, so the 1,400-line target of §5 is withdrawn.

**Phase E — an eval that measures the claim.** Gold notes split into `must` and `may` (history); adversarial sets
where grep should lose (stale-vs-current traps, alias traps, implicit audiences, scattered evidence); a grep
baseline agent that is told it may `cat` folders; single-question agents as well as 10-question sessions; a
stronger judge; a write-path eval (agents writing notes under SKILL.md, then dreamed and asked).
**Offline part done 2026-10-31** (RESULTS.md, "Phase E"): `--must` (242 → 252 complete answers), `adversarial.py`
(stale trap: successor first 0.70 → 0.95 after a one-line ranking rule, old note marked 1.00; scattered evidence
0.66 at 1/6.7 of the folder-`cat` characters; alias questions 0.93 with or without the index vs 0.43 for grep).
**Phase F (RESULTS.md "Phase F")**: the five improvements of the re-review, each measured (lineage one-liners kept at
4; quiet model-free path; precision metric; `taste()` left as is after five variants lost; the index question
answered with a real index of the whole bank: the boosts stay at one weight, +0.8 / +6.4 points for +4.8% characters once
lineage one-liners run for every question — F9, where the real index also exposed two alias hijacks and the
conflict detector's 6% precision), then the graph contract (`CONTRACT.md`, `schema: 1`, `check` validates, A38), a second
free-money pass (version and same-title conflict candidates, open questions in the digest, C11; cross-project refs
measured nil and dropped), a cache-aware dreamer (−32% per note, convergence 1.06×) and the rebuilt viewer.

Agent runs (RESULTS E3, E4): one memory/grep pair on ten questions, the grep arm allowed to `cat` folders — 7/3/0
against 8/2/0 correct/partial/wrong, tool calls 7 against 31, tokens and time about equal in this single pair —
**then phase G (RESULTS G1): three batches per arm on the real Haiku index, 23/7/0 against 23/7/0, tool calls 0.30×,
tokens processed 0.29×, cost units 0.61×, wall time 0.75×**; one
write-path run — eight notes from a six-line session, lineage right (three supersessions, two preferences in
`prefs/`), every fact findable by `ask` with history marked. Not done: single-question agents, a stronger judge,
n > 1 with cost units — they need a dedicated run with transcripts.

**Phase C, part 2 — a constrained open relation vocabulary** (§10): two tiers (coarse type, open label), promotion
gated by evidence and a budget, probation and automatic demotion, seed packs for other domains. Tests A12/A14/A20
rewritten, A34–A36 added. **Both parts done 2026-10-31** (RESULTS.md, "Phase C"): with Haiku on 70 notes, 81% of
relations typed and 19% kept as labels that were invisible before, 0 invented types; the conflict detector tightened
from 282 to 38 candidates on the bank after a real review showed 2 true conflicts in 20 and 157 rule/preference pairs
that can never be supersessions; the reviewer's own verdicts were right in all 20. Deviations: a full budget refuses
promotion and says so instead of asking for a type to demote; conflicts cover decisions, models and findings only.

What not to do: embeddings or any heavier retrieval; more model in the read path; an *unconstrained* open relation
vocabulary; automatic edits to notes.

---

## 8. Working alongside Claude Code's own memory

### What Claude Code does (v2.1.316; docs read 2026-10-31, confirmed against the installed binary)

Two mechanisms, both loaded at the start of every session:

- **CLAUDE.md files**, written by people: managed policy → `~/.claude/CLAUDE.md` → `./CLAUDE.md` or `./.claude/CLAUDE.md`
  → `./CLAUDE.local.md`; ancestors of the cwd load at launch, subdirectory files on demand; `.claude/rules/*.md` load
  unconditionally or scoped by `paths:` frontmatter; `@path` imports (depth 4, relative to the importing file; an import
  outside the working directory needs a one-time approval); HTML comments are stripped before injection; the guidance
  is under 200 lines per file.
- **Auto memory**, written by Claude: `~/.claude/projects/<project>/memory/`, where `<project>` is the git root path with
  every non-alphanumeric character replaced by `-` (`/home/user/memory-dream` → `-home-user-memory-dream`), or the
  `autoMemoryDirectory` setting, or `CLAUDE_CODE_PROJECT_DIR_NAME` with `CLAUDE_CONFIG_DIR`. `MEMORY.md` is the index:
  its first 200 lines or 25 KB load every session; one topic file per memory with `type: user | feedback | project |
  reference` and a `modified:` ISO timestamp, read on demand. Machine-local, not shared across machines, off by
  default in self-hosted and cloud sessions; `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` turns it off. Claude Code also runs
  its own background consolidation, called auto-dream (`autoDreamEnabled`), over its own files.

What `memory.py` does today when pointed at an auto-memory directory (measured on a mock with four typed memories):
`ask` works read-only — it heads MEMORY.md and the topic files, Claude Code's `type:` values pass through as kinds,
`modified:` is ignored so dates fall back to mtime. `dream` wrote `EDGES.md`, `ALIASES.md` and `_dream/` into the
directory, which must never happen to Claude Code's files.

### Where each layer is strong

| | CLAUDE.md and rules | auto memory | memory-dream notes |
|---|---|---|---|
| writer | people | Claude | agents and people |
| holds | standing instructions | learnings about the user and the work (user, feedback, project, reference) | the work itself: experiments, findings, decisions, datasets, features, models, taste, terms, corrections — with lineage and numbers |
| lives | the repo (and `~/.claude`) | this machine only | the repo (`memory/`): travels with git, present in cloud sessions |
| loaded | whole, every session | index every session, topics on demand | on demand, through one `ask` |
| scale | ≤ 200 lines per file by design | a 200-line index | thousands of notes, grep plus lineage |

The best of both: personal learnings stay local in Claude Code's memory; the team's knowledge lives in the repo with
lineage; one `ask` reads both; the always-loaded layer is Claude Code's own loader, not a second one.

### Five rules

- **R1 — one read over both.** `ask` also greps Claude Code's auto-memory *topic files* — not `MEMORY.md` and not
  CLAUDE.md or rules, which are already in the agent's context — ranks them in their own pool and prints at most three
  per question under an origin mark, e.g. `▸ claude-code: feedback_testing.md · feedback · 2026-10-25`. The taste block
  includes `user` and `feedback` memories when a task is asked. Source resolution follows Claude Code's own order:
  `autoMemoryDirectory` from `.claude/settings.local.json`, `.claude/settings.json`, `~/.claude/settings.json`, else
  `${CLAUDE_CONFIG_DIR:-~/.claude}/projects/<sanitised git root>/memory`. Skipped when the directory does not exist
  (cloud sessions), when `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`, or with `MEMORY_SOURCES=notes`. One extra grep; 0 calls.
- **R2 — never write there.** `dream` and `log` refuse a root that contains `MEMORY.md` or lies under
  `<config>/projects/*/memory`, with a one-line message; `ask`, `check` and `viz --out` stay allowed read-only. Nothing
  from Claude Code's memory is ever copied into `memory/` or the digest, so private memories stay where Claude put them,
  and Claude Code's auto-dream and memory-dream's `dream` never touch each other's files.
- **R3 — an always-loaded digest, through Claude Code's loader.** `dream` writes `memory/DIGEST.md` (deterministic,
  0 calls, ≤ 40 lines): how to ask (2 lines), the user's own preferences (`prefs/me-*` titles), the newest live
  decisions and models (≤ 10), and, off by default, the areas with counts. The user wires it with one line in
  CLAUDE.md — `@memory/DIGEST.md`, a relative import, so no approval dialog — or a symlink in `.claude/rules/`. The
  generation notice is an HTML comment, which costs no context. Measured size: 20 lines / 2.3k chars (~580 tokens per
  turn) at 1,677 notes and 47 areas with the areas list, 9 lines / 784 chars at 30 notes. The benefit is unmeasured:
  round 1 found an index *file* worthless at 30 notes, but context is different from a file to read. Before
  recommending it by default, run the agent eval cell "memory + digest" against "memory" and count tool calls and
  correctness. Claude Code's own rule — skip anything CLAUDE.md already says — then also keeps auto memory from
  duplicating what the digest states.
- **R4 — frontmatter compatibility.** `modified:` (ISO 8601) is the date when `updated:` is absent; Claude Code's
  types map to kinds: user → preference, feedback → rule, project → note, reference → howto. A note written in either
  convention parses.
- **R5 — which layer owns what** (a SKILL.md paragraph). Standing instructions to Claude → CLAUDE.md (people) or auto
  memory (Claude), exactly as Claude Code already does. A fact about the work with a number, a date, a source or a
  predecessor → a note. A person's taste about artifacts → `prefs/`, so `ask` attaches it to tasks and it carries
  lineage. Never the same thing in two layers: if CLAUDE.md says it, no note.

Conflicts across layers belong to the phase C queue: a note against an auto-memory topic file or a CLAUDE.md line
that share a rare token, both live, go to the subagent; the decision lands in `memory/CONFLICTS.md` naming the other
file's path; `ask` prints the decided one first and names the other; an edit to a Claude Code file is proposed in the
output, never applied. One naming collision to document: `memory.py dream` is unrelated to Claude Code's auto-dream.

Costs: R1 one grep per `ask` (milliseconds); R3 about 600 tokens per turn only if wired; R2, R4, R5 nothing.
Tests: A25 digest (content, cap, nothing from Claude Code's memory in it), A26 read-only source (hits shown with
their origin; `dream` refuses; the directory is byte-identical afterwards), A27 `modified:` and type mapping.

---

## 10. Relation vocabulary: constrained open

### What the two extremes did (RESULTS rounds 2–3)

Open: on the 56× bank Haiku wrote 508 distinct type names; the Haiku reviewer answered "new" to all 178 proposals
with ≥ 2 uses; EDGES.md grew from 7 to 185 types and 470 items waited for review. Closed: 8 types cover 81.2% of
5,196 relation instances (74.6% directly, 6.6% through aliases); 5.5% are dropped on purpose (claims, note-to-note
links); 13.3% are unknown, spread over 449 names — a flat tail of about 1.5 uses per name, the largest (`prefers`)
16 uses, 0.3%. Unknowns are cached but invisible until a person adds a type to EDGES.md, which picks them up at 0
calls. And relations do not change answers: `ask` measures the same with and without the index, so the vocabulary is
a question for the viewer and for management, not for accuracy.

The coverage problem with closed: the 13.3%, and everything from another domain (software, research, operations),
stays invisible until a person edits; the review can never add. The sprawl problem with open: synonyms multiply,
nothing converges, the viewer becomes unreadable. Both problems come from making *the vocabulary* carry the whole
load. Split it.

### Design: two tiers, gates in code

1. **Two tiers.** Every relation carries a coarse `type` — one of EDGES.md, or `other` — and a fine `label`: the
   note's own verb in 1–3 words, folded. The dreamer picks the closest type and always writes the label. Nothing
   grounded is dropped: `other/<label>` relations are kept, counted, listed on the entity card and shown on the map
   behind a toggle (off by default). Coverage is 100% of grounded relations from the first dream, in any domain.
2. **Promotion gated by evidence.** A label may become a type, or an alias of one, only once it has ≥ 5 uses in ≥ 5
   notes across ≥ 2 areas (constants in `WEIGHTS`). The review sees only labels over the bar and answers, per label:
   `alias T`, `alias ~T`, `new: <one line: what it means and how it differs from the closest type T>`, or `drop`.
   The code accepts `new` only when the bar is met, the definition names a closest type, and the budget has room;
   otherwise the label simply stays a label. The prompt cannot create sprawl because the prompt does not decide.
3. **A budget.** EDGES.md holds at most 24 types (8 seed + 16 promoted). When it is full, a promotion needs the review
   to name a type to merge or demote; the code refuses otherwise.
4. **Probation.** A promoted type is written as `- <type> (proposed 2026-10-31): <def> | aka: …`. If after 60 days
   its use is still under the bar, it is demoted to a label automatically: 0 calls, the relations reappear as
   `other/<label>`, nothing is lost. Lines without the mark — written by a person — are permanent. Any hand edit wins,
   as today.
5. **A smaller `drop:` list.** Only what is not a relation between two entities stays dropped: note-to-note links
   (`answers`, `led-to`, `basis-for`) that lineage already covers. Claims and comparisons (`beats`, `improves`,
   `causes`) are kept as `other/<label>`.
6. **Seed packs** for coverage on day one elsewhere: optional `pack: software` (calls, implements, deployed-to,
   configures, tested-by, blocked-by, …), `pack: research`, `pack: ops` lines in EDGES.md expand to types and aliases.
   A pack is nothing but lines; the default stays data-science.

### Expected effect and cost

From the round-3 numbers: about 19% of grounded relations that are now hidden or dropped become visible as
`other/<label>`. With the bar at 5 / 5 / 2 the flat tail promotes almost nothing on the 56× bank — probably `prefers`
and `predicts`, the two the add-type demo chose by hand — so EDGES.md stays near 8: the budget is a backstop, not the
daily mechanism. In a new domain the labels appear at once and the first promotions follow once the evidence exists.
Cost: one extra field per relation in the extraction (a few output tokens per note), the same single review call,
0 calls for relabelling and demotion. Code: `EXTRACT` (+`label`), `ground`/`build` (keep `other`), `REVIEW` (+`new:`
with a definition), `edit_edges` (add, mark, demote), the viewer (toggle), tests A12/A14/A20 rewritten, A34 promotion
gate, A35 probation and demotion, A36 budget. Risks: the `other` tail is noisy in the viewer, so it is hidden by
default; the thresholds are guesses until measured on real notes, which is why they live in `WEIGHTS` with a note.

---

## 11. Two other designs, read for what was free to borrow (phase G)

Helix Foundry (HelixDB) builds a company-wide ontology over connected data with an agent and a human reviewer and
loads it into a graph database — a different problem and cost class; its "every value traces to its row" is what
`▸ path · line:` does for notes. HelixDB's memory-system skill and MOOSEDev (Trivyn; the NeSy 2026 paper on
ontology-grounded project memory) are closer: typed records with lifecycle state, supersession kept as history,
current-only retrieval with history one hop away, exact-token search as a required channel. Each of those is
already here in plain files (`supersedes:`, `from:`, the SUPERSEDED mark, grep). What was missing and cheap:
MOOSEDev's **negation** category — now the absence set in `adversarial.py`, 70 of 70 flagged after a three-part
change to the weak-match rule that keeps it at 2 of 326 real questions — and its **connectivity** target, now the
`lineage:` line of `check`. Their currency benchmark (structured 100% vs BM25 46% with pushed context) is the
same guarantee our stale set measures by lineage (successor above the old note 0.97, old marked 1.00), and their
finding that a dense channel re-ranks but recovers nothing BM25 misses supports keeping retrieval at grep plus
structure. Not taken: an ontology language and a daemon, separate alternative/consequence records, an author field,
`as_of` reads. RESULTS G2 has the detail.

## 9. Appendix — probe scripts

All probes were run from the scratch directory and left no files in the repository. The three grep-strategy
and taste experiments used `eval/retrieval.py` and `eval/taste/score.py` unchanged, pointed at a scratch copy of
`memory.py` through `MEM_PY`. The scratch patches were: for F7, in `taste()`, the top three matched general-area
notes are scanned for a `first-last` name that has a `prefs/` family, which is then treated as named; and the
print cap `ranked[:6]` with floor `0.25` became `ranked[:12]` with floor `0.15`. The recency experiment added, for
"current" intent, a 1.05× bonus for the newest live note among seeds within 60% of the top score — it changed no
answer.
