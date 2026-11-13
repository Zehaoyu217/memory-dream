# memory-dream — runbook

Everything runs with stock `python3` (3.9+, stdlib only). Paths are relative to the repo root.

## Install in a project

```bash
cp -R skills/memory-dream  <project>/.claude/skills/memory-dream        # or ~/.claude/skills/
cp skills/memory-dream/agents/memory-dreamer.md <project>/.claude/agents/   # file-mode dreamer
mkdir -p <project>/memory
```

`memory.py` finds the memory root by `--root`, then `$MEMORY_DIR`, then the nearest `memory/`
upward from the cwd, then `./memory`. It needs a shell, Python 3.9+ and grep; any agent that has those
can use it, with or without a model.

Beside Claude Code's own memory: `ask` also reads the project's auto-memory topic files
(`~/.claude/projects/<project>/memory/`, or `autoMemoryDirectory`; override with `MEMORY_CC_DIR`,
switch off with `MEMORY_SOURCES=notes`) and never writes there — `dream`, `log`, `drop` and `viz` refuse such a
root. To keep `memory/DIGEST.md` (written by every dream, ≤ 40 lines) in context every session, add one
line to CLAUDE.md: `@memory/DIGEST.md`.

## Daily use

```bash
M="python3 .claude/skills/memory-dream/scripts/memory.py"
$M ask "what came of exp-014?" "who owns cards.txn_daily?"   # answering: grep + memory, every question in one call
$M viz                            # memory/_dream/graph.html (dream refreshes it): Timeline, Map, Connections
$M log "backfill running" -p churn-2026
$M check                          # every warning C1–C18 in full
$M drop churn-2026/exp-014        # what would go with this note; add --yes to do it (a folder works the same way)
grep -rn velocity memory/ --exclude-dir=_dream                 # plain grep stays first-class
```

Viewer (`_dream/graph.html`, self-contained, white, one black at four strengths, one blue, plain words only; the Timeline opens first, then the Map and Connections tabs): three views — notes by area and time with
their lineage drawn (lanes as bands of colour, no lines), and the entity graph (one column per family, the notes'
current relations as curves; pan, zoom, drag, a fisheye under the mouse; `Connections` tab or `#view=graph`), and
the Map (`#view=map`: what a person wrote → what it became → who checked it, with verdicts; one graph with its hubs
named; what each kind of statement is worth); pick a note to read
it in its own box, see how it connects (direct links first, the rest folded), what the assistant took from it, the
entities and relations the dreamer read in it, pending conflicts; legends are toggles (two rows: nodes, edges);
fuzzy search over titles, text and entity names (`/`). Deep links: `graph.html#note=<path>`, `#entity=<id>`,
`#area=<name>`, `#q=<search>`, `#view=graph`, `#check`. "Worth checking" lists what may be wrong (notes that may
disagree, names that may be the same thing, odd or broken links, notes on their own), each with a "Copy question"
button whose text you paste to the assistant; a picked note and each extracted fact have the same.

## Typed links in `ask` (phase I)

For a thing the question names by id, `ask` follows the index's typed links when the question asks about inputs or
users (`uses`, `trained-on`, `part-of` cues: "what does X use", "inputs", "depends on", "built on", "what uses X"): two
steps — what it is built from, what those are built from, what its predecessor was built from — through typed relations
and `from:` lineage alike, each as a one-line pointer (header + `# ` line), at most 8 (`W["relation_lines"]`). Measured on
the real index (RESULTS I3): dependency questions 0.853 → 0.920 of gold notes for +4.6% characters. Knobs for
measurement: `MEMORY_RELATION_LINES=0` switches it off, `MEMORY_RELATION_MODE=cue|inputs|always`, `MEMORY_RELATION_HOPS=1|2`;
`MEMORY_DEBUG=1` prints the walk. The real index of the bank rebuilds with no model from `eval/real/bank-index/`
(`restore.py`, then `dream`).

## The domain: three registries, not the code

`memory/KINDS.md` (kinds of note), `memory/TYPES.md` (types of thing) and `memory/EDGES.md` (types of link) are
written by the first dream from seeds that cover data, analytics, software and finance work, and read before every
command. The extraction prompt is a fixed piece of guidance filled from them: the kinds list, the type lines (what each
is, its aliases, what it is not), the relation lines. A hand edit is permanent and costs nothing: the next dream
re-derives the graph from the cached readings, which keep the dreamer's raw words, so no note is re-read. Add a type by
adding a line; add a domain with `pack: research` or `pack: ops`; retire a type by merging it (add its word to another
type's `aka`) — a deleted line is reported (C13) and its readings fall back to `other/<word>`, so nothing is lost
either way. The review may also admit types: a word used for things that fit no type is counted, offered over the bar
(`promote:`), admitted within the `budget:` with a `family:`, and demoted after the `probation:` if it stays rare,
exactly as relation labels are.

## Entities and the relation vocabulary

- Relation types are a constrained open vocabulary: the 8 types in EDGES.md with their aliases
  (`~` = read in reverse), plus whatever label the dreamer gives a link that fits none — kept and
  shown as `other/<label>`, listed on the entity card, never on the map. A label is offered to the
  review only over the bar in EDGES.md (`promote: 5 uses, 5 notes, 2 areas`); the review may alias it
  onto a type, keep it a label, drop it (note-to-note links only), or answer `new: <definition>`, which
  the code admits only within `budget: 24` types, written as `- <type> (proposed <date>): …`. A proposed
  type still under the bar after `probation: 60 days` is demoted back to a label (0 calls). Hand-written
  lines are permanent; `pack: software` (or research, ops) adds a domain's types. Any edit relabels
  everything at the next merge, 0 calls.
- Conflicts: two live `…-vN` siblings in one area, two live notes with the same title, or two live notes of
  one kind (decision, model, finding) in one area, not linked by lineage, sharing an id-like title token or two
  rare title words, are queued (C10) and offered to the review, 20 per dream. Verdicts land in `memory/CONFLICTS.md`: `- a > b` (a supersedes b: lineage from then
  on, both notes untouched), `compatible: a / b`, `- a ? b` (unsure: listed for a person). Nothing is
  asked twice; a person can write any of these lines by hand.
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
- Kinds need no model either: frontmatter `type:` wins (Claude Code's user/feedback/project/reference
  count as preference/rule/note/note), then the area when it has a kind (`prefs/` preference, `glossary/` term,
  `corrections/` correction, `reporting/` and `howto/` rule), then a prefix in the first or second part of the
  filename (`exp- feat- ds- dec- fnd- q- metric-`), then `…-vN` is a model, and only then the dreamer's
  kind: the folder and the name a writer chose come before a reading. `modified:` serves as the date when
  `updated:` is absent.

## Another base, taken in (`absorb`, origins)

```bash
$M absorb ~/their-kb --as policy-kb            # what it would take, what it would not and why; changes nothing
$M absorb ~/their-kb --as policy-kb --yes      # copy the notes under memory/policy-kb/, write ORIGIN.md, bring readings, rebuild
$M ask -p policy-kb "who approves a tier 1 model?"   # ask that base alone
$M drop policy-kb --yes                        # take it out again
```

What it takes: every `.md` under the folder (a file with no `# ` line gets one from its name), the readings of a
memory-dream base (`_dream/notes/`), or a graph in `relations.jsonl` (`{from, relation, to, evidence: [note
paths]}`) with entity cards (notes with `id:` in their frontmatter). What it leaves is listed with the reason, and
so is every link it refuses: a link is kept when the note it cites names both ends. The full list stays in
`memory/_dream/absorb-<name>.json`.

What an origin is afterwards (CONTRACT §7): your answers are the same to the letter; its notes are listed after
yours under `in other bases`, when it names what the question names; `-p <name>` asks it alone. Its preferences
and rules reach a task only with `--trust preferences` (or `trust: answers, preferences` in its `ORIGIN.md`), a
`me-` note never. The report names every name both sides use: they are two things until you add one line to
`ALIASES.md`, `- auc = policy-kb:auc`. Words its readings use that the registries do not know show as
`other/<word>`; a line in `TYPES.md` or `EDGES.md` reads them (0 calls). A folder you copied in by hand becomes an
origin when you add an `ORIGIN.md` to it.

## Dream (index new or changed notes)

Command mode (default when a command is set):

```bash
export MEMORY_LLM='claude -p --model haiku --tools "" --setting-sources "" --strict-mcp-config --no-session-persistence'
$M dream -j 6
```

`--setting-sources ""` and `--strict-mcp-config` keep the dreamer from loading your CLAUDE.md,
hooks, plugins and MCP servers: each call is then ~4.4k input tokens and ~$0.0015 with Haiku.
`tests/haiku_cmd.py` is the same command with per-call cost logging (`$DREAM_COST_LOG`).

Many notes to read: packets.

```bash
$M dream --dry-run --packets      # how many notes, in how many packets, about how many tokens and dollars; nothing is called
$M dream --packets -j 6           # a packet a call: about a dozen short notes each
```

A packet holds notes up to 6,000 characters, or a prompt of 60,000 tokens, whichever comes first
(`MEMORY_PACKET="tokens,characters"`). An answer that skips a note or is cut off costs only that note,
which is asked once more. Measured on Haiku 5.5 (RESULTS phase S): a dozen notes a call reads as many
things a note as one call a note, places more of the links between a folder's notes, and costs 0.6 as
much; two dozen a call costs 0.4 and reads thinner (0.60 of the things). One call a note is still what
`dream` does when `--packets` is not given.

After the first reading, with a command, every line of a note that says what it builds on or replaces is
read once more beside its folder's notes (`second reading: … lines read once more`), 45 lines a call.
A folder of more than 200 notes (`MEMORY_FOLDER`) cannot be listed in a prompt: the keeper is then shown
the notes near the lines of a call, and the calls are smaller. A dream that was stopped by hand leaves
`_dream/lock`; the next one says so and waits until the file is deleted. Nothing read is lost: readings
are on file as they arrive, and the next dream reads only what is still unread.

No command: `dream` builds everything that needs no model — lineage, kinds, conflicts, digest,
viewer, index — and says how many notes have no entities yet; `check` says it in one C5 line.
Answering is unaffected. When you want entities and relations without a model command, run
`dream --packets`: it writes the unread notes as packets to `memory/_dream/pending/` and lists them
in `pending/TODO.md`; run `memory-dreamer` subagents on them, one packet each, in parallel; run
`dream --packets` again. A review prompt can appear on the second pass, so loop until it reports
0 pending (normally 2 rounds). `dream --prompts` does the same with one prompt a note.

A long dream on a laptop: keep the machine awake (`caffeinate -s -i $M dream -j 8` on macOS). A
machine that sleeps freezes the dream and breaks the calls in flight, and it looks like a service
that stopped answering. `MEMORY_TIMEOUT` (300 seconds) counts the time the machine is awake; a call
that outlives it is ended with everything it started and tried once more, and the notes it held are
left for the next dream (`C3`). A dream that was killed leaves `_dream/lock`: delete it. What it had
read is on file and is not read again.

Keep the readings in git: `memory/_dream/notes/` is what a keeper was paid for, and with it a clone
builds the same graph with no call. Ignore the rest of `_dream/` (`memory/_dream/*`, then
`!memory/_dream/notes/`). Two branches that read the same note leave the same file name: take either.

Other flags: `--review` forces the vocabulary review, `--all` re-indexes everything (after changing
the dreamer model). Indexing is optional for answering: `ask` works on raw notes (grep plus lineage);
the index adds aliases, typed relations and the viewer's entity views (measured on 1,677 notes: about
1 point more gold recall and 6 more on alias questions, for 5% more characters).

## Tests

```bash
python3 tests/acceptance.py                 # 40 checks (A1–A20, A24–A43) with the deterministic fake dreamer (~30 s)
python3 tests/e2e.py                        # one run on both read paths: dream, ask, a file gone, drop, absorb (a few seconds)
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

Every dream also writes `memory/DIGEST.md` (how to ask, your own `prefs/me-*`, the newest live decisions and
models, the open questions no finding or decision builds on; ≤ 40 lines) and remembers the script's hash, so an
upgraded `memory.py` rebuilds the graph once with 0 calls.

With a model command, notes are indexed project by project with one KNOWN list per project, and the prompt's static
part is handed to the command as a system prompt (`tests/haiku_cmd.py`), which Claude caches across calls: $0.0015
per note instead of $0.0022 on the 70-note sample, convergence unchanged (1.06× after the review).

What dream writes in `_dream/`: `store.db` (its caches: parsed note facts by path, extractions by content hash;
the files in `_dream/notes/` stay the source), `index.db` (the graph as SQLite: `ask` on a big memory reads only the
rows a question needs), and the viewer. Up to `MEMORY_WIDE` notes: `graph.json` + one `graph.html`. Past it: no
graph.json; `graph.html` is an overview of areas and `viz/<area>.html` one page per area, redrawn only when that
area changed (`viz/_sig.json`). A dream with nothing new stops after the scan.

```bash
python3 eval/scale/profile_dream.py <memory root>                       # where a full rebuild spends its time
python3 eval/scale/profile_incremental.py <memory root> <scratch> fraud-2026   # re-index one area with the fake dreamer
```

## A hosted store (ADR-001): PostgreSQL, Neo4j, or an export

The notes stay the truth and the local index keeps working; a store holds a copy of the graph (CONTRACT.md schema 1) for
dashboards, cross-repository queries and a graph explorer. `skills/memory-dream/scripts/stores.py` carries the backends;
`memory.py` itself stays standard-library only and imports it only when `MEMORY_STORE` is set.

```bash
pip install "psycopg[binary]"                                   # the PostgreSQL driver (the script needs nothing else)
export MEMORY_STORE=postgres MEMORY_STORE_URL=postgresql://user:pw@host:5432/memdream   # MEMORY_REPO=<id> for many memories
$M dream            # publishes the graph as a diff after the dream: "store postgres: +N −M rows in 0.4s"; a dream with
                    # nothing new still publishes when the store is behind
$M ask "…"          # reads notes, lineage, entities and names from the store (identical output: tests/store_parity.py)
$M check            # one line: store postgres: repo R · N notes · E entities · R relations · built … · schema 1 v0.4
$M export --to /tmp/graph-export   # no driver: CSV in neo4j-admin header format + import.sh + load.cypher + meta.json
```

- Publishing is a diff: rows are keyed and hashed, only new or changed rows travel, rows gone from the graph are deleted,
  in one transaction under a per-repository advisory lock; a schema or version mismatch republishes everything.
- If the store is down, `ask` says so on stderr and reads the local index; `dream` reports "publish failed" and the local
  index is complete. Nothing in answering depends on a database.
- Neo4j: `MEMORY_STORE=neo4j MEMORY_STORE_URL=neo4j://host:7687 MEMORY_STORE_USER=neo4j MEMORY_STORE_PASSWORD=…` with
  `pip install neo4j`. Nodes `Note` and `Entity` keyed by `repo|id`, lineage as `BUILT_ON`, `SUPERSEDES`, `REFS`,
  `MENTIONED_IN {lines}`, typed relations as `REL {type, evidence}`, `Name` nodes for folded spellings. This backend has
  not been run against a server in this repository's test environment, and neither have the export's `import.sh` and
  `load.cypher`: the export is checked only for its files and counts.
- Parity test: `MEMORY_STORE_URL=… python3 tests/store_parity.py postgres [--bank]` (needs the driver): identical `ask`
  output through the store and the local index, the graph read back equals graph.json, a second dream publishes nothing,
  an edit publishes one note, a deletion deletes it, a version mismatch republishes all.

## Troubleshooting

- `dream` says C3: the dreamer answer was unusable twice; the note stays grep-searchable and is
  retried on the next `dream`.
- `check` starts with `contract: schema 1 ok`: the graph conforms to `.specs/memory-dream/CONTRACT.md`. Anything
  else there is a bug in `memory.py`, not in your notes.
- `C11`: a note over 40 lines; split it or move detail into a new note (the dreamer reads only the first 16k
  characters of a note).
- `C13`: a type line was removed from EDGES.md or TYPES.md while readings still use its word; the things or links
  show as `other/<word>`. Merge the word into another type's `aka`, or restore the line.
- `C15`: a note's file is gone and nobody dropped it (a wrong `rm`, another branch, a rename with an edit). Nothing
  was written or deleted. Until it is settled the note it had replaced reads as current and notes built on it get
  `C2 … not found`. Either put the file back, or run the command the line names: `memory.py drop <path> --yes`
  records the drop from where the note stood at the last dream.
- `C14`: a note is built on a note that was dropped, or its replacement was dropped and it is the newest left of its
  line. Both are shown on the note's header in `ask`. Nothing to do unless the note should go too: drop it as well.
- Undo a drop: restore the file from git and delete its `dropped:` line in CONFLICTS.md. `drop` never touches git.
- `curator: 12 folders, 5 names joined, 3 refused`: a cheap model read each folder's things together
  and said which are one thing under two names. Every join is a line of `memory/ALIASES.md` with its
  reason (`| why: …`) and `| by: curator <date>`. Read the new lines; delete one that is wrong and add
  `not: a / b` so that it is not written again. `dream --review` runs the curator on a memory that was
  read before it existed.
- `proof: 4 of 5 questions of SETUP.md are answered by their note`, with the fifth named: a question
  the memory was set up to answer no longer leads to its note. Something changed since it did: a
  registry line, a folder, the note itself. Put the question to `ask` and read what comes first.
  The lines are `- the question? -> area/note.md` in `memory/SETUP.md`; change one only when the
  note that answers it changed.
- `? it builds on «…», in its own words` under a note in `ask`, and `not the whole chain` on a `⇡`
  line: the same thing as C18, shown to whoever is reading. The memory holds no link for those
  words, and says so instead of looking complete.
- `C18`: a note says in its own words that it builds on or replaces something ("Builds on the
  dispositions dataset"), and no note answers to the name. With a command, a dream reads every
  such line once more, alone and beside the folder's notes, and asks for each thing the line names
  (`second reading: 1462 lines read once more, +108 links (50 calls)`); a line is read twice and
  no more. What is still listed after that needs a person: add `from: [the-note]` or
  `supersedes: [the-note]` to the note's frontmatter, which always wins.
- `second reading: … N lines left for the next dream`: a dream reads at most 200 folders' worth of
  such lines; run `dream` again.
- `third reading: K of N words placed`: words of a note's lineage that the second reading kept as
  words, put once more beside the few notes they could mean, with their first lines. What is still
  listed after it (C18) needs a line of frontmatter.
- `C17`: a note's `tags:` line has a word that `memory/TAGS.md` does not list. Add its line
  (`- word: what it means`), or add the word to the `aka:` of the tag it is another spelling of. It
  filters either way (`ask --list --tag word`); the line is what gives it a definition.
- `C16`: a note points into a file (`src/app.py#load`, `src/app.py:8 "LIMIT = 10"`, `app.py:11`) and the file is
  gone, or the symbol or the words are no longer in it. `ask` shows the same on the note (`STALE: 1 of its pointers
  no longer hold`) and, for a pointer that only moved, the line it is on now. The note stays: what it says may
  still hold. Write a new note that supersedes it, or fix the pointer. Files are looked for from the repository
  around `memory/`; set `MEMORY_CODE=<folder>` when the code lives elsewhere.
- `C7 … labels below the review bar`: links outside the vocabulary, shown as `other/<label>`; nothing
  to do unless you want one as a type — add a line to EDGES.md (0 calls). `C7 vocabulary budget full`:
  raise `budget:` or remove a type. `C10 conflict pending`: two live notes may disagree; let `dream`
  with a model ask the review, or write `- a > b` / `compatible: a / b` into CONFLICTS.md yourself.
- `check` says C9: the note contains NUL bytes (a binary paste, a bad encoding). `ask` still greps it (`grep -a`),
  but keep notes plain text.
- `ask` prints `(weak match: 'x' found nowhere in memory …)`: an id, version or number you named occurs in no note
  (the notes shown are its nearest neighbours, such as the versions that do exist), or a word of the question occurs
  in no note and the best note covers at most half of the question's words. Rephrase, or grep.
- On a small memory (≤ 200 notes) `ask` prints the whole memory after the per-question pointers whenever that costs
  about the same as the surgical lines (within 1.2×): nothing is missed, and it is no dearer than `cat`.
- `memory.py: another dream is running` (exit 3): `_dream/lock` exists and is under two hours old; wait, or
  delete it if that dream died. A lock older than two hours is taken over.
- Delete `memory/_dream/` to rebuild from scratch; EDGES.md, ALIASES.md and CONFLICTS.md survive.
