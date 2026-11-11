# memory-dream v0.5 — the plan: a general memory and knowledge graph, built in blocks

2026-11-11 · written to be argued with before anything is built · materials behind it: `RESEARCH-2026-11.md` (SAG2,
OpenViking, the owner's claims base, and what plain graph methods find in our own graph today) · starting state: `HANDOFF.md`,
`RESULTS.md` phases A–J.

## 1. What is asked

Grow the project memory into a general memory and knowledge graph, slowly, without losing what makes it work:

- **Writers** (agents, people) leave notes. A note is a claim with its evidence.
- **Keepers** (cheap model passes) distil from the notes the things they name, the links between them, tags, and what
  each thing is and is not.
- A **taxonomy** of thing types, link types and tags that is not fixed: it grows from the words the notes use and is
  tidied behind the scenes by merging, mapping, declaring how terms relate, and de-duplicating.
- A **contract loose enough** that a graph built by this skill for another project, memory or body of knowledge can
  be merged in.
- **Graph methods and plain engineering** to find conflicts, loose ends, and equivalent parts that can be combined.
- **Governance**: every assertion rests on evidence, and every change of meaning leaves a record.
- All of it **light**, and each stage a **block** that can be swapped for another solution or upgraded alone.

## 2. The picture

```
 writers ──▶ NOTES (claims) ──▶ keeper reads ──▶ READINGS (raw words + quotes)     TRUTH    never edited; keyed by content
                                                     │
        REGISTRIES  kinds · thing types · link types · tags                        MEANING  small text files; changed by
        CONTRACTS   what a thing is / is not, its anchors and near-misses                   the keeper, by rules, by people;
        VERDICTS    which mention belongs to which thing                                    every change has a ledger line
        DECISIONS   the ledger: who, what, on what evidence, how to undo
                                                     │   merge: no model call
                                                     ▼
 other graphs ──▶ mount / merge ──▶  GRAPH  things · links · lineage · findings     DERIVED  disposable; rebuilt from the
                                       │            │                                        two planes above
                    ask · digest · viewer · stores  └─▶ analysis ─▶ QUEUE ─▶ keeper / person ─▶ DECISIONS
```

Three planes, taken from the claims base's rule that truth and meaning never share a record: what a note says (truth) is read
once and kept in the keeper's own words; what those words mean (meaning) lives in small files that can change any
day; the graph (derived) is recomputed from the two with no model call. v0.4 already works this way for types of
things and links. The plan extends the same split to tags, to the identity of things, and to more than one graph.
It is also what makes a merge cheap: another graph's readings come along with their notes, and only the meaning
plane has to be reconciled.

## 3. Where we start

v0.4 has a first version of most blocks.

| stage | what exists today | measured |
|---|---|---|
| write | one note per thing; the `# ` line is the claim; `from`, `supersedes`, `updated`; kinds from the filename prefix (SKILL.md) | an agent session saved as 8 notes, 3 supersessions, none rewritten |
| keep: read | one cheap-model reading per note content, cached by hash: kind, things (id, type word, the note's own word, surface forms), links (type word, label, quote); what the note does not contain is dropped (C4) | $0.0016 a note; 94 ungrounded items dropped on the bank |
| keep: vocabulary | three registries (`KINDS.md`, `TYPES.md`, `EDGES.md`): a definition, aliases, a family and a `not:` per term; other words kept as `other/<word>`; a bar, a budget, probation; the review maps or drops | 14 link types carry 81% of the links; 493 raw link words carry the rest and 62 raw type words 6% of the things |
| keep: identity | folded ids, a surface rule, `ALIASES.md` (`=`, `not:`), same/different answers on name-alike pairs | 3,216 ids as written → 1,325 things |
| graph | notes, lineage, things, links with `path:line` evidence; schema 1; JSON and SQLite; rebuilt with no call | 1,677 notes in 0.9 s |
| checks | 13 warnings, mostly per note; conflict pairs from shared title words; `CONFLICTS.md` (`>`, `compatible`, `?`) | 5 of the 73 conflict pairs a review judged were real (7%) |
| use | `ask` (grep first, lineage, aliases, typed links, preferences), the digest, the viewer | gold 0.939 to 0.941; 0.61× the cost of an agent with grep alone |
| stores | SQLite index; PostgreSQL (tested); Neo4j (written, never run); CSV export | parity 11/11 |
| proof | 40 checks, three retrieval gates, the stability eval, CI on two Pythons, the same numbers on macOS and Linux | green |

Missing for what is asked: tags; a definition per thing and a record of which mention belongs to which thing; more
than one graph; any analysis of the graph as a graph; a ledger of decisions; a way to plug a block in.

## 4. What the materials say

Details and sources are in `RESEARCH-2026-11.md`. Nothing from either outside repository was run.

**Both outside systems moved away from a maintained graph this autumn.**

- **SAG2** (Zleap AI, MIT; paper of 2026-10-15, package `zleap-sag2` 0.4.0) is not a knowledge graph. It is the
  successor of the event-and-entity engine now called SAG1, and it removed the graph: no entities, no relations, no
  embeddings, only the original passages and a word index, built with no model call. At question time it takes the
  best 100 passages by BM25, has a hosted, closed model judge each as "necessary evidence", lets the best ten donate
  rare terms for a second search, and judges again. Its predecessor's identity rule was the lower-cased name, and
  the team's own review calls its disambiguation broken.
- **OpenViking** (Volcengine, AGPL-3.0 since 2026-03-30, a running server required) has no graph engine. Its
  "knowledge graph" is an example skill, a prompt that has a model write `entities/<id>.md` files and one
  `relations.jsonl`, with evidence only at the level of a source file. It was taken out of the packaged skills on
  2026-10-29. Its earlier links between contexts were deleted because nothing read them, and its directory-walking
  retrieval was replaced by one vector search on 2026-10-02. Types, predicates and de-duplication are instructions
  in a prompt: there is no registry and no gate.

So neither is a graph to plug in, and both confirm the two bets this project already made: search the original
text first, and keep meaning in something small that can be checked.

| | as the keeper's extractor | as a retriever | as a store | as a source of notes | weight |
|---|---|---|---|---|---|
| SAG2 | no: it extracts nothing | an optional arm to compare against, out of process; a paid closed judge, and the text leaves the machine | no | narrowly: its app's notes carry citations anchored by hash, lines and quote | a 32 MB binary or eleven packages |
| OpenViking | no | low value: vector recall through its server | a one-way publish target where it already runs | feasible and lossy: its memories are merged cards with no quotes | a server, two models, about sixty packages, AGPL |

The best fit runs the other way: OpenViking's users are building `entities/` + `relations.jsonl` graphs by hand
with no merger and no validator, which is what this project is. Reading and writing that shape (B10) makes
memory-dream the checking layer for a graph someone else's model wrote.

**Taken as ideas, into the blocks.** From SAG2: a second search round keyed by rare terms mined from the best notes
of the first (B9); "necessary evidence" as the judge's question (B4, B9); evidence anchored by hash and position
with a state — intact, moved, changed, missing (B2, B8); an alias used only when the literal word finds nothing
(B9). From OpenViking: the `entities/` + `relations.jsonl` exchange shape, with the line and the quote added (B10);
a stable key apart from a display label (B3); the judge chooses only among the candidates it is offered, and groups
are cliques, never transitive closure (B4); an account of what every input became — delivered, failed, unreferenced
(B8); conflict records kept beside the text they concern (B7).

**Deliberately not copied.** A remote closed judge on every question; dropping the graph; a closed type list that
drops what does not fit; identity by lower-cased name; whole files or graphs rewritten by a model; free-text types
with no gate; entity cards that are edited in place; any AGPL code.

## 5. Principles every block keeps

1. **Notes are the truth.** Nothing rewrites a note. Everything derived can be thrown away and rebuilt.
2. **Raw words in, meaning late.** A reading keeps the keeper's own words; the registries decide what they mean when
   the graph is merged. So a change of taxonomy, and a merge of two graphs, re-reads nothing.
3. **Similarity proposes, the keeper judges, a person overrules.** No threshold decides what a thing is (the claims base's rule).
4. **Grounded or not served.** Every thing, link, tag and definition points at a line of a note; what does not is
   kept with the reason and never shown.
5. **A detection is not a verdict.** A conflict is a record that two things cannot both hold; `open` is a valid end.
6. **Light.** The core is the standard library and files. No block needs a server, a vector store or a model to keep
   answering; anything heavier is a plug-in someone chose.
7. **Never worse than grep, and measured.** A block lands with a number, a way to reproduce it and a gate in CI.
8. **The same answer everywhere** (phase J): no result may depend on a machine, a run or the company a question keeps.
9. **A merged graph is data.** Never code, never instructions: its notes are quoted with their origin, and plug-ins
   load only from the skill's own directory.

## 6. The loose contract (schema 2): the records that cross block boundaries

A block is replaceable when the records on either side of it are fixed and small. Every record carries `schema`,
keeps fields it does not know, and never needs another record to be parsed.

| record | plane | what it is | new in schema 2 (all optional) |
|---|---|---|---|
| **note** | truth | a markdown file; the `# ` line is the claim; `from`, `supersedes`, `updated` | `source:` where the claim comes from · `by:` who wrote it · `tags:` the writer's own · `holds:` the conditions it is true under |
| **reading** | truth | the keeper's extraction of one note content: `kind`, `entities`, `relations`, `refs`, in raw words with surface forms, lines and quotes | `tags` · `defs` (what the note says a thing is, and is not, with the quote) · a reason on each dropped item |
| **registry line** | meaning | `- name[ (proposed date)]: definition \| field: value …` in `KINDS.md`, `TYPES.md`, `EDGES.md` | `TAGS.md` · `broader:` · `not:` naming terms · `same: graph:term` · for links `one`, `acyclic`, `symmetric` |
| **contract** | meaning | — | `- id: what it is \| not: the nearest things it is not \| aka: … \| anchors: path:line … \| excludes: path:line …` in `THINGS.md` or the thing's own note |
| **verdict** | meaning | today only pairs: `a = b`, `not: a / b` in `ALIASES.md` | mention × thing × contract version → `in` or `out`, from `anchor`, `keeper`, `person` or `rule`, with a reason |
| **decision** | meaning | outcomes in `ALIASES.md` and `CONFLICTS.md` | one dated line per change of meaning in `DECISIONS.md`: who, what, the evidence, how to undo |
| **finding** | derived | `checks` (`C1`–`C13`), `conflicts` | `{code, subjects, evidence, detector, suggestion, state}`; its state changes are decisions |
| **graph** | derived | schema 1 (CONTRACT.md) | `origin` on every record · `tags` · `contract` and `status` on things · `support` on links · `findings` |
| **bundle** | exchange | — | notes, readings, registries, contracts and decisions of one graph; never the derived graph, never code |

Why this is loose enough to merge: ids are local names, not global ones; a reading never contains a decision; two
graphs need to share only the note and reading formats; their registries may differ and are reconciled by `aka`,
`broader`, `not` and `same` lines, each a decision that can be undone.

## 7. The blocks

Each block: what it does, what exists, what to build, what could be swapped in, and the measurement that says it is
done. "Swap in" names alternatives a plug-in may provide; the default is always the standard-library one.

### B0 · Seams and the plug

- **Today.** Three seams prove the pattern: `MEMORY_LLM` (any command that takes a prompt on stdin), `MEMORY_STORE`
  with `stores.py` (seven row calls, loaded only when named), and the matcher with its Python stand-in. Everything
  else is direct calls inside one 3,200-line file.
- **Build.** (1) Name the interfaces the core calls through: `extract`, `ground`, `resolve`, `build`, `analyze`,
  `match`, `rank`, `render`, `store`. (2) `MEMORY_PLUGINS=a,b` loads `scripts/plugins/<name>.py` from the skill's own
  directory, each registering a replacement or an addition. (3) Every record that crosses a seam is one of §6.
  (4) Split `memory.py` into one file per block only where (1) to (3) leave it hard to read; the install stays `cp -R`.
- **Done when.** With no plug-in named, `ask` prints byte-identical answers on the 1,149 questions and `graph.json`
  is byte-identical on the bank; 40/40; the gates are unchanged; a 20-line demo plug-in replaces the matcher and
  passes A42's no-grep line.

### B1 · Notes as claims (writers)

- **Today.** SKILL.md's note: one thing, one claim, what is true now, what it was built on, what it replaces.
- **Build.** The optional fields of §6 (`source`, `by`, `tags`, `holds`): two claims that differ only because they
  hold under different conditions are not a conflict, and `holds:` is where a writer says so. The same contract for
  knowledge that is not project work (a paper, a policy, a meeting). Importers are plug-ins that write notes under a
  prefix and never touch existing ones. A note with no date of its own is a finding, not a silent guess from the
  file's modification time (RESULTS J3).
- **Swap in.** Any source of notes: see §4 for what SAG2 and OpenViking could feed; the claims base's claims (a
  sentence plus the verbatim span it rests on) map one to one.
- **Done when.** The write-path run of phase E repeated under the new text: no note rewritten, sources present
  where the session stated them; a note with none of the new fields behaves exactly as today.

### B2 · Readings (the keeper, one note at a time)

- **Today.** The `EXTRACT` prompt, `ground()`, the cache by content hash.
- **Build.** Reading schema 2, old readings still valid: `tags` (words the note uses or the registry lists), `defs`
  (only where the note itself says what a thing is or is not, with the quote), and a reason on every dropped item
  (`absent`, `no-quote`, `numbers` when a quote's numbers differ from the note's, `negation` when the reading adds or
  loses a "not") — kept, never served. What is stored as evidence is the note's text at that line, not the model's
  rendering of it. And the handoff's item 7: the pool of calls is fed continuously within a project instead of in
  waves that wait for their slowest call (a third busy at eight in parallel today).
- **Contract.** Note text, the registries' current lines and the known ids in; one reading out. A reading never
  contains a decision of the meaning plane.
- **Swap in.** Any model command; file mode for a helper agent; the rule-based keeper the tests use; an extractor
  from §4, as long as it emits a reading.
- **Done when.** On the 70-note sample, then the bank (about $3): tags and definitions 100% grounded; at most
  $0.0025 a note; the things a fixture defines in words get those definitions; gates and the stability eval hold
  with old and new readings mixed.

### B3 · Registries: the dynamic taxonomy

- **Today.** Three registries with a bar (5 uses, 5 notes, 2 areas), a budget and a 60-day probation; an edit
  re-derives the graph with no call. The words below the bar are the raw material: 493 link words (426 used once)
  and 62 type words. The two commonest raw type words on the bank are `log-tag` and `project-tag`: the keeper is
  already reaching for tags that have nowhere to go.
- **Build.**
  1. One engine for four files: add `TAGS.md` (tags on notes and things, with an optional `facet:`).
  2. How terms relate, declared on the line: `aka` (the same), `broader:` (a kind of; any depth, kept free of
     loops), `not:` naming terms (cannot both hold), `same: <graph>:<term>` (another graph's word for it). For link
     types the algebra the checks need: `one: yes` (a thing has at most one), `acyclic: yes`, `symmetric: yes`,
     beside today's `~` reverse and `shape:`.
  3. Operations, each one changed line plus one ledger line, each undoable because readings keep the raw word:
     merge, split (one word into two terms by a rule on its neighbours), rename, admit, retire, map.
  4. Proposals from counts, no model: two words used for the same things → `aka`; a word whose things are a subset
     of another's → `broader`; two link words always found on the same pair → `aka` or an implication; what the
     things of a family usually carry → a learned `shape:`. The keeper's review confirms; a person can overrule.
- **Done when.** Merging a term and undoing it restores `graph.json` byte for byte with no call; replayed from the
  bank's raw readings, the counting proposer is scored against the review's decisions on file (6 link types admitted
  of 7 offered, 8 thing types, 14 pairs of things merged and 73 kept apart), then floored; the registries pass the
  loop check; the handoff's item 6 (note kinds named as thing types) is closed by a `not:` line.

### B4 · Things: contracts and membership

- **Today.** A thing is an id. No statement of what it is; no way to say "this mention is another thing of the
  same name". On the bank `holdout-2025q4` is one thing mentioned by 17 projects.
- **Build** (from the claims base, where it is the core).
  1. A **contract** for each thing that needs one: what it is, then the nearest things it is not, its other names,
     its anchors (mentions that are certainly it) and its excludes (near-misses). The keeper drafts it from the
     definitions the notes state (B2) and from the mentions; it is `(proposed <date>)` until a person accepts it or
     it passes the bar.
  2. **Membership verdicts**: mention × thing × contract version → `in` or `out`, with a one-line reason naming the
     deciding feature. The effective verdict is a person's or an anchor's first, then the newest contract version.
     Ambiguous is `out`.
  3. Who gets a contract: not every thing. The ones the graph marks: mentioned across many areas with no note of
     their own (44 on the bank), name-alike pairs, hubs that glue unrelated areas, and anything two merged graphs
     bring under one id.
  4. Operations under the claims base's rules. Split: groups proposed from the mentions' surroundings; each child gets its
     anchors and the other groups' nearest mentions as excludes; a person applies it. Merge: union of anchors,
     excludes minus anchors, the contract redrafted, membership judged afresh, the sources retired. Nothing is
     ever deleted.
- **Swap in.** Candidate generators (names today; shared neighbours; embeddings as a plug-in); the judge (any model
  command, or a person).
- **Done when.** On a labelled sample of the `holdout-2025q4` mentions the per-project things are separated with no
  wrong fusion; a fixture with planted homonyms (one id, two things) and synonyms (two ids, one thing) is resolved
  exactly; the 44 homeless hubs each have a proposed contract; the alias gate (0.821) and bank gold (0.941) hold;
  verdicts survive a re-reading of an unchanged note.

### B5 · The graph, schema 2

- **Build.** Additive fields only (§6): `origin`, `tags`, `contract`, `status`, `support`, `findings`. A schema 1
  reader keeps working.
- **Done when.** `check` validates schema 2; the viewer check and the store parity test pass unchanged.

### B6 · Stitching graphs

- **Today.** One memory. But `ask` already reads a second, foreign memory in the same call and never writes to it
  (Claude Code's own), and the 100× world is 137 renamed copies of every project.
- **Build.**
  1. **Mount.** `MOUNTS.md`: `- fraud: ../fraud/memory` reads another memory in place, read-only, its paths
     prefixed, its notes shown with their origin in every answer.
  2. **Merge.** `memory.py merge <bundle> --as <prefix>` copies notes with their readings (keyed by content: no
     note is read again), then folds the meaning plane: registry lines that agree become one; the same word with
     another definition is a finding and stays apart as `prefix:word` until mapped; contracts and decisions come
     along under the prefix.
  3. **Alignment.** The same id in two graphs is only a candidate. Seeds are ids that are rare and defined alike;
     the match grows through shared typed neighbours (a thing whose neighbours are already matched); every pair is
     judged against both contracts (B4) and recorded as a `same:` line.
- **Done when.** The bank split into two memories and merged back gives the unsplit bank's `graph.json` byte for
  byte with no call; `ask` over a mount prints what `ask` prints over the merged copy; with ids renamed in one half,
  alignment recall and precision are measured, then floored; a bundle carrying a script or an instruction-like note
  changes nothing but the notes.

### B7 · Analysis: the graph looks at itself

- **Today.** Checks per note; nothing reads the graph as a graph.
- **Build.** Analyzers: small pure functions from the graph to findings, registered by name, each free or paid per
  item. The first set is §8, in the order our own graph says they pay. A **finding** records a detection, not a
  verdict: its states are `open`, `resolved` (how) and `dismissed` (by whom, why), and `open` is a valid end. One
  **queue**, ordered by what a finding touches (the mentions behind it, the links through it): it is the viewer's
  "worth checking" and `memory.py check`.
- **Swap in.** More analyzers as plug-ins (communities, centrality, embeddings); a graph library for whoever wants
  one, never in the core.
- **Done when.** Every loop the probe finds on the bank (27 in links, 6 in lineage) is a finding with a proposed
  fix; a fixture with planted defects (a lineage loop, a fork, two owners under `one: yes`, a two-way `replaces`, a
  missing expected link, two same-shape partial graphs under other names) is found exactly; the top 20 of the bank's
  queue are judged by a person and the precision is recorded, then floored.

### B8 · Governance: evidence, decisions, upkeep

- **Today.** Nothing ungrounded enters; links keep `path:line`; outcomes sit in `ALIASES.md` and `CONFLICTS.md`;
  types on probation carry a date; the model's "unsure" waits for a person.
- **Build.**
  1. The **ledger** `DECISIONS.md`, append-only. `check` fails any registry line, alias, contract or verdict that
     has no ledger line (seed lines excepted).
  2. **Levels of evidence** on everything served: stated (a quote in a live note), supported (how many notes and
     areas), history only (every source superseded), decided (a ledger line), inferred (a rule or an analyzer,
     always marked as such).
  3. **Who may decide what** (§9).
  4. **Upkeep as a budgeted pass.** Free steps always: scan, merge, analyzers, counting proposals. Paid steps in
     queue order within a budget; `--dry-run` prints the calls and the estimate before anything is spent.
  5. **Doctor.** Invariants answered PASS, FAIL or COULD-NOT-CHECK: every quote is in its note at its line; every
     verdict's contract version exists; no mention is both anchor and exclude; the registries have no loop; the
     graph rebuilds identically from the two planes.
- **Done when.** The bank's existing decisions replayed into a ledger pass `check`; the dry-run estimate is within
  20% of a real pass; the doctor fails on each planted violation and on nothing else.

### B9 · Use: ask, digest, viewer

- **Build.** Only what the new records make cheap: scope by tag; a thing's "is / is not" printed beside its name;
  the origin of a mounted note; a finding said with the answer it touches ("two current answers", "defined two
  ways"). The viewer gains the queue and the taxonomy. Two loose ends from phase J close here: the lines printed
  under a note stop depending on the other questions of the call (the character counts are re-based once), and the
  matchers are timed against each other (on a Mac the Python one took 22 s where BSD grep took 49).
- **Swap in.** The matcher (grep, the Python stand-in, ripgrep, SQLite full text); a retriever in front whose hits
  are re-ranked like grep's (§4).
- **Done when.** The three gates and the stability eval hold; "never worse than grep" is re-measured in the agent
  eval once the spend is approved.

### B10 · Stores and exchange

- **Build.** Schema 2 through the seven row calls; the bundle as the exchange format; the taxonomy exported as plain
  CSV (term, definition, broader, aka, not) for any other tool.
- **Done when.** Store parity passes on schema 2; a bundle imported into an empty memory rebuilds the same graph.

### B11 · Proof

- **Build.** One fixture per new claim, model-free wherever possible: planted homonyms and synonyms (B4), the
  split-and-merged bank (B6), planted defects (B7), the replayed review (B3). Each block's "done when" becomes a
  gate in CI.

## 8. The graph toolbox, measured on our own graph first

`python3 eval/graph_probe.py <memory> --conflicts eval/real/bank-index/CONFLICTS.md`: standard library, no model, a
few seconds on the indexed bank (1,325 things, 3,119 links, 3,733 lineage edges).

| method | what it finds | on the bank today | what happens next |
|---|---|---|---|
| strongly connected groups, per link type and in lineage | loops where none can be | 27 in links: 6 pairs that each `replaces` the other, 16 `uses` loops, 3 `owned-by`, 2 `measured-by`; 6 loops of `from:` holding 13 notes | a finding with the evidence lines side by side; most are a link read backwards |
| the link algebra declared on a registry line (`one`, `acyclic`, `symmetric`, `not`) | a thing with two owners where one is allowed; a thing of two types that exclude each other | 22 of 155 subjects have two or more owners, legal until `one: yes` is declared | a conflict finding, or the evidence that the type is not `one` |
| spread and homelessness of hubs | one name for several things; shared things nobody defined | 83 things in 5+ areas, 44 with no note of their own; `holdout-2025q4` in 17 projects | a contract drafted, a split proposed (B4) |
| bridges | links that alone hold parts together | 295, of which 245 rest on one line of evidence | ranked low unless the bridge joins two projects |
| parallel links on one pair | a link type that implies another; smells | 126 pairs: `trained-on` with `uses` ×5, `evaluated-on` with `trained-on` ×4 | a `broader:` proposal; a "trained and evaluated on the same data" finding |
| roles by family | what a kind of thing usually carries, and who lacks it | 88% of models are measured by a metric (20 are not); 74% are evaluated on a dataset (44 are not) | a learned `shape:`; gap findings |
| shared typed neighbours | siblings, not duplicates | 17 pairs, none of them name-alike | each other's excludes in contracts; a shared tag or parent |
| things two live notes share | where two claims are about the same things | on the 73 judged pairs, precision 7% → 25% keeping 2 of the 5 real ones | orders the conflict queue; not a detector |
| exact shape hashing (Weisfeiler–Lehman) | identical partial graphs | 2% of linked things: of no use inside one real graph | only to check a merge left shapes intact |
| seeded neighbourhood alignment | the same things under other names in another graph | not run: needs two graphs (B6's split bank) | candidate pairs with their shared neighbours as evidence, to the judge |
| reach from superseded notes | things and links that rest only on history | exists in part ("current" links) | the "history only" level; a re-check queue |
| communities (label propagation) | clusters that are not areas | not run | tag proposals; mis-filed notes |

Two findings shaped the plan. Exact equivalence of partial graphs is rare in real notes, so "equivalent parts that
can be combined" has to be approximate and seeded, and it belongs to stitching (B6). And things that look alike
structurally are usually siblings, which makes them the best near-misses for each other's contracts (B4) rather than
candidates to merge.

## 9. Who decides what

| a person, or the writing agent | the keeper (a cheap model) | the script |
|---|---|---|
| what a note claims, its sources, the conditions it holds under | what a note mentions, with quotes; its tags; the definitions it states | grounding; kinds; dates; what is kept |
| the final word on any verdict, contract, merge of hubs, or mapping between two graphs | drafts contracts; `in` or `out` with a reason; maps a word onto a term; supersedes, compatible or unsure | candidates, counts and proposals; every analyzer; the queue's order; levels of evidence; that the ledger is complete |
| accepting a contract or a term early; dismissing a finding (the why is mandatory) | — | admitting a term over the bar; demoting it after probation |

The right column stays rules anyone can read. The middle column always leaves a quote and a reason behind. Only the
left column is judgement, and it is never overruled by the other two.

## 10. The order of work

Each milestone ships alone, keeps every gate green and adds a phase to RESULTS.

| | milestone | blocks | spends on a model | why here |
|---|---|---|---|---|
| M0 | a clean base | — | no | done except the owner's part (§12) |
| M1 | seams, the ledger and the finding record | B0, the two formats of B8 and B7 | no | everything later writes these two records; no behaviour changes |
| M2 | the graph looks at itself | B7 first analyzers, B5 fields | no | free, pays at once (33 loops, 44 homeless hubs, the gaps), and its queue tells the keeper where to spend |
| M3 | the taxonomy engine and tags | B3, tags of B2 | a few review calls | one engine for four registries; undoable operations; counting proposals |
| M4 | contracts and membership | B4, definitions of B2 | yes: contracts and verdicts for the marked things only | the first block that needs the keeper for something new |
| M5 | stitching | B6, the bundle of B10 | no, except judging aligned pairs | needs identity (M4) to be safe; a read-only mount can ship with M2 |
| M6 | blocks from outside, and the agent eval on the shipped code | plug-ins of §4, B9 | yes | only after the seams exist |

## 11. What we will not do

- No global ontology and no reasoner: terms relate by four plain statements (`aka`, `broader`, `not`, `same`), read
  by counting and graph walks.
- No vector store, embedding model or server in the core. Any of them may be a plug-in.
- No merge of two things across graphs on their names alone, and no merge of hubs without a person.
- No rewriting of notes, by any block.
- No code and no instructions accepted from a merged graph.
- No number without the command that reproduces it.

## 12. What is needed from the owner

1. **The branch.** `production-readiness` holds everything and is green. Merge it, make `main` the default branch,
   delete `worktree-build-v0.4`, tag `v0.4.1`. This is yours: the working session may not merge or push to `main`.
2. **The licence.** MIT with the holder taken from the git author name: confirm or change.
3. **The names.** "writer" and "keeper" for the two roles; the command stays `dream`; the files `TAGS.md`,
   `THINGS.md`, `MOUNTS.md`, `DECISIONS.md`.
4. **The first milestone.** M1 then M2 need no spend and no decision beyond this plan. Say go, or reorder.
5. **Spend.** M3 to M6 call a model: $3 to $4 to re-read the bank with the wider reading (it cost $2.69 with
   today's), a few cents per reviewed batch, and the agent eval re-run that the handoff still lists.
6. **The claims base.** This plan borrows its mechanisms, in our own words, and none of its code or text. Say if
   it should also become a source of notes one day (its claims already have the shape of a note with its quote).
