# memory-dream — the graph contract (schema 1)

What `memory.py` writes and reads, field by field. The viewer, `ask`, `check`, the tests and any other consumer build
on these shapes and nothing else. `schema` is carried by every graph (`graph.json`, `index.db` meta, the viewer's data
island) and is bumped when a field changes meaning; `memory.py check` validates a graph against this contract and
test A38 enforces it on the fixture.

Conventions. Paths are relative to the memory root with `/` separators and the `.md` suffix (`churn-2026/exp-014.md`).
A note's **id** is its filename without `.md`; its **project** (area) is the first path segment, `""` at the root, and
under an origin (§7) the origin and the next segment (`policy-kb/entities`). Dates
are ISO `YYYY-MM-DD`. Line numbers are 1-based file lines. Everything under `_dream/` is derived and disposable; the
notes and the user-owned files (`KINDS.md`, `TYPES.md`, `EDGES.md`, `TAGS.md`, `ALIASES.md`, `CONFLICTS.md`,
`SETUP.md`, and the generated `DIGEST.md`) are not. None of these files is a note.

## 1. The graph

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
| `vocab` | object | `{types, budget, promote: [uses, notes, areas], probation, labels, below, demote: [type]}` — the relation vocabulary (EDGES.md) |
| `proposed_types` | list of label | type words (things typed outside TYPES.md) over the `promote` bar of TYPES.md, offered to the review |
| `tvocab` | object | the same shape as `vocab`, for TYPES.md |
| `dedup` | object | counters from entity merging (`mentions`, `ids_as_written`, `after_folding`, …) |
| `checks` | list of `{code, msg}` | warnings, sorted by code; codes `C1`–`C18` (§5) |
| `dropped` | list, optional | what `drop` recorded: `{path, date, replaced, built_on_by, left_newest}` (below) |
| `pointers` | object, optional | `{note path: [pointer]}`: what the notes point at in the project's files (below) |
| `unplaced` | list, optional | lineage a reading states that no note answers to (C18): `{note, field, i, what, quote, asked}`, `field` being `built_on` or `replaces` and `i` its place in the reading's list; `asked` once the line it stands on has been through the second reading |
| `tags` | object, optional | `{tag: [note paths]}`, from the `tags:` line of each note's frontmatter read through `TAGS.md` (§6): a listed tag under its name whatever spelling the note used, a word that is not listed under its own folded spelling (C17). In `manifest.json` too |

**pointer** — `{to, path, line, quote, symbol, text, state, now, of, form}`. A note's text points into a file as
`path#symbol`, `path:line "quoted words"` or `path:line`; `to` is the path as written and `path` the file it is,
from the project's root (the repository around the memory, or `$MEMORY_CODE`): a name with no folder is the one file
of that name. Only what is a file of the project at a dream is a pointer; a ratio or a host and its port is not.
`state`: `intact` · `moved` (`now` is the line) · `changed` (the file is there; the symbol is not defined in it, or
the words are on no line) · `gone` (the file is not).
- A symbol is looked for as a definition, form by form, and the first form found anywhere in the file decides: a
  keyword before the name (`def`, `class`, `function`, `fn`, `func`, `struct`, `const` and their kin), a block that
  opens (`render() {`), an assignment at the start of a line, a key at the start of a line. A call is no form.
  `form` is the one it was first found by, and a weaker one is not taken later. `Class.method` finds the class, then
  the method after it. `of`: how many lines define the name; `now` is the first.
- Quoted words are looked for on a line, runs of spaces aside, case kept, and never inside a longer word. No longer
  on their line and on several others, a line that begins with them comes before one that mentions them, then the
  nearest; `of` is how many lines hold them.
- A bare line is held by the whole text of the line it named when a dream first saw it (`text`), and by nothing else.

The list is in `manifest.json` too, with `psig`, a signature of the files named: a dream with nothing else new still
runs when one of them changed. `ask` looks every pointer of the notes it prints up again.

**dropped** — one entry per `dropped:` line of `CONFLICTS.md`, and one per dropped note inside a dropped folder that
a note still names. `path`: the note, or the folder with a closing `/`; never a note that exists. `replaced`: what
the line says the note had replaced. `built_on_by`: notes whose `from:` names it (they stay; C14). `left_newest`:
notes it had replaced that no note replaces now (C14). Who had replaced a dropped note replaces what it had replaced:
those are ordinary `supersedes` edges with `by: "drop"`. The same list is in `manifest.json`, where `ask` reads it on
a memory too large for `graph.json`.

**note** — `{path, id, project, title, line, kind, updated, superseded_by, sha, indexed}`
- `title`: the text of the first `# ` line outside code fences (`""` when none → C6); `line`: its file line (0 when none).
- `kind`: lowercase; frontmatter `type:` wins (Claude Code's `user|feedback|project|reference` map to
  `preference|rule|note|note`), else the kind of its area when the area has one (the `area:` fields, seeded
  `prefs`→preference, `glossary`→term, `corrections`→correction, `reporting`/`howto`→rule, `log`→log; under an origin
  the area's last part), else the kind whose prefix is the first or second part of the filename (`exp-014`,
  `aml-find-kyc-lift`; the prefixes are the `prefix:` fields of `KINDS.md`, seeded `exp- feat- ds- dec- fnd- find-
  finding- q- metric- model- pref- rule- term- plan- req- risk- inc- rpt- report- svc- mod- lib- sys- adr- design- bug-
  fix- rel- release-`), else `model` for a name ending `…-vN`, else the dreamer's kind unless it is `note` (and only a
  kind `KINDS.md` lists), else `note`. The folder and the name its writer gave a note come before a dreamer's reading
  of it (RESULTS phase L; until 2026-11-11 the dreamer's kind came second), and a folder that has a kind before a
  first word (phase N: `howto/model-card-required-fields` is a rule, not a model).
- `updated`: frontmatter `updated:` or `modified:` (first 10 chars), else a `log/YYYY-MM-DD` filename, else mtime.
- `superseded_by`: paths of notes whose `supersedes:` names this note, plus `- a > b` lines of `CONFLICTS.md`; every
  entry has a matching `supersedes` edge.
- `sha`: first 12 hex of the note's SHA-256; `indexed`: an extraction exists for this sha.

**edge** — `{src, dst, rel}` with `rel ∈ {from, supersedes, refs}`; `by: "review"` marks a supersession recorded in
`CONFLICTS.md`, `by: "drop"` one passed on by a tombstone, `by: "reading"` lineage that the note states only in its
prose and a keeper read with the words that state it (the `built_on` and `replaces` of its reading, §4). What such
an item names is looked up as a note (a path, or a file name, in the note's own folder first), then through the
things' names (the home note of the thing, or for a thing with no note of its own name the one note of the folder
that names it on its `# ` line), then as the one note that the item's own words name by path or id and that no
other item of the note took; an item that names no note is listed (`unplaced`, C18), not kept. A line of frontmatter
that already says it leaves it out, and for a replacement so does `compatible: a / b` in `CONFLICTS.md` or the
reverse replacement. A replacement is not taken from a note older than the one it names ("Superseded by X", read the
wrong way round), nor from a note of another kind when a note of the replaced note's own kind says it too (a
decision that reports "v3 replaces v2"); two notes that each claim to replace the other are believed neither. A
`refs` edge between the same two notes gives way to it. The counts are in `dedup` (`lineage_read`, `…_unplaced`,
`…_older`, `…_other_kind`, `…_both_ways`). `from` and `supersedes` come from frontmatter (resolution:
relative path, exact path, unique filename, same-project filename → C1 if ambiguous, then moved paths; a target that
`drop` recorded → C14 for `from`, and for `supersedes` an edge to each note the dropped one had replaced; otherwise
unresolved → C2). `refs`: `[[links]]`, the dreamer's refs, and body slugs that name a note in the same project or a
unique note anywhere.

**entity** — `{id, type, home, aka, names, headline, mentions}`
- `id`: canonical (the `ALIASES.md` lead, else the most-used spelling); `type`: lowercase, a type of `TYPES.md` (the
  dreamer's type or alias read through the file), **or** `other/<word>` when the dreamer's word fits no type (the word is
  folded), or `other`; a thing whose word is on the `drop:` line of `TYPES.md` is not an entity; `aka`: other spellings
  merged into it; `names`: `[{name, n}]` surface forms
  with counts; `home`: the note whose id is this entity's id, or null; `headline`: the best live note mentioning it
  (title-line mention, then finding/decision, then the latest date, then the first by path: never the file's
  modification time, which a clone does not keep), or null; `mentions`: `[{path, lines}]` sorted by path.
- Kept only with a home note, ≥ 2 mentioning notes, or an `ALIASES.md` line. A name on the `drop-names:` line of
  `TYPES.md` is never an entity, whatever its type (the seed's line: files and notebooks).

**relation** — `{s, type, o, evidence}`; `s`, `o` are entity ids; `type` is a vocabulary type from `EDGES.md` (incl.
packs and `(proposed …)` types) **or** `other/<label>` with the label folded (lowercase, `-` joined); `evidence`:
`["path:line", …]`, the note and line stating it. `drop:` types never appear.

**label** (in `proposed`) — `{type, uses, notes, areas, examples}`: the label, instance count, distinct notes, distinct
areas, up to 3 `"s — o: quote"` examples.

**conflict** — `{a, b, shared, unsure}`: two live notes of one kind in one area, not linked by lineage, `shared` = the
id-like or rare title tokens they share (or `version` for `…-vN` siblings, `same title` for equal titles); `unsure`:
the reviewer answered unsure (`- a ? b`), so it waits for a person and is not asked again.

## 2. `index.db` (SQLite, read by `ask` on big memories, `check`, `viz`)

`meta(k, v)` — JSON values for `schema`, `v`, `built`, `proposed`, `review`, `dedup`, `vocab`, `conflicts` ·
`notes(path, id, area, title, line, kind, updated, sha, indexed, sup)` with `sup` = JSON `superseded_by` ·
`edges(src, dst, rel)` · `ents(id, type, home, headline, aka, names)` · `ment(eid, path, lines)` ·
`names(k, eid)` — folded spellings (id, aka, names ≥ 3 chars) → entity · `rels(s, type, o, ev)` · `checks(code, msg)`.
`read_index(dd)` returns the graph of §1 from these tables; the two forms are interchangeable.

A hosted store (`stores.py`, ADR-001; `MEMORY_STORE=postgres|neo4j`) holds the same tables keyed by a repository id
(`md_notes`, `md_edges` with the index's edge order, `md_ents`, `md_ment`, `md_names`, `md_rels`, `md_meta`; in Neo4j the
equivalent nodes and relationships), published as a diff after every dream; its `read_graph()` returns the graph of §1,
and `ask` reads it through the same seven row calls as `index.db` (`tests/store_parity.py` checks both).

## 3. The viewer's data island (`<script type="application/json" id="data-graph">`)

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

## 4. Caches and the manifest (`_dream/`)

- `notes/<sha12>.json` — one extraction per note content: `{kind, entities: [{id, type, label, as, lines}], relations:
  [{s, type, label, o, quote, line}], refs, built_on: [{what, quote, line[, asked]}], replaces: [the same], dropped:
  {entities, relations}, path, sha, model, indexed_at}`. `built_on` and `replaces` are what the note says of itself,
  the document, kept only with words found in the note; a reading made before they existed has neither. `what` is
  a note's file name, a thing's id, or, when a keeper could name neither, the note's own words for it. `asked`: the
  line the item stands on has been read a second time, alone and beside the folder's notes, and this item is one
  member of what that reading found there: `quote` is the member's own words in the line, `what` the file name of
  the note the keeper named for it (`folder/name` for a note of another folder), or the words again when it named
  none. The items a first reading had on that line are gone from the list. `looked`: the item's words were put
  to a third reading with the few notes they could mean; `said`: the words or name it had before that reading named
  a note. `recheck: [{field, line[, asked]}]`: lines that write what an item names whose copied words were not in
  the note, so the item was not kept; the second reading reads them. `type` and
  `label` are the dreamer's raw words; the registries read them at merge time. Entities keep only surface forms (`as`)
  that occur in the note; relations only with their quote found (the rest counted in `dropped` → C4). Kept `KEEP_DAYS`
  after last use. This is the one folder of `_dream/` worth keeping in git: a clone then builds the same graph
  without paying a keeper again (ignore `_dream/*`, keep `!_dream/notes/`).
- `store.db` — `facts(path, sha, rec)` parsed note facts (`fm`, `title`, `line`, `links`, `ids`, `nul`, `lines`);
  `x(sha, mt, rec)` the extraction, valid while its file's mtime matches.
- `manifest.json` — `v`, `code` (hash of memory.py), `files {path: {sha, mtime, size}}`, `former {path: [old paths]}`,
  `vsig` (hash of EDGES + ALIASES + CONFLICTS + KINDS + TYPES), `registry` (the type names of EDGES.md and TYPES.md at
  the last dream, for C13), `seen`, `queue`, `failed`, `attempts`, `refs`, `dreamed`, `unindexed`, `due`, `dropped`
  (the graph's list, §1), `tags` and `unplaced` (§1), `curated {folder: signature of the things it held when the curator last read
  it}`, `gone {path: {seen, replaced, replaced_by, built_on_by}}` (notes that left without a `drop`,
  with where they stood at the dream that noticed: C15, and what `drop` needs to record them later), `pointers` and
  `psig` (§1). A dream with nothing changed in any of these, nor in a file a note points at, stops after the scan.
- `pending/` — what a helper agent is asked, each answered by a file of the same name ending in `.json`; `TODO.md`
  lists them. `dream --prompts` writes `<sha12>.prompt.md`, one note each; `dream --packets` writes
  `packet-<8 hex>.prompt.md`, many notes each under `NOTE <sha12> <path>:` lines and named by the notes it holds, so
  the same unread notes make the same packets. A packet's answer is one JSON object a note, each with
  `"note": "<sha12>"` beside the fields of a reading: one a line, or an array, or one object keyed by the id. An
  answer that is cut off loses the note it was cut in and nothing else; a note asked for and not answered is asked
  once more, then recorded as failed (C3). `review.prompt.md` is written with either flag. An answer file is taken
  whether a command is set or not. `lock` — pid of a running dream.

## 5. Warnings

`C1` ambiguous lineage target · `C2` lineage target not found · `C3` the dreamer's answer was unusable twice ·
`C4` an ungrounded entity or relation was dropped · `C5` no extraction yet (one summary line in `check`) · `C6` no `# `
line · `C7` vocabulary: a label over the bar awaits review, the budget is full, or labels sit below the bar · `C8` an
unparseable line in EDGES.md, ALIASES.md or CONFLICTS.md · `C9` NUL bytes in a note · `C10` conflict pending ·
`C11` a note over 40 lines (SKILL.md's own rule) · `C12` a relation whose entity families are unusual for its type
(the `shape:` field of its EDGES.md line; seeded `trained-on` model → dataset, `evaluated-on` → dataset, `measured-by` →
metric, `owned-by` → party, `replaces` the same family on both sides; families by the class tree below): retype the
entity or drop the relation · `C13` a type removed by hand from EDGES.md or TYPES.md while cached readings still use
its word: the readings show as `other/<word>`; merge the type into another (add the word to that type's `aka`) or
restore the line. `C7` covers type words of TYPES.md as it covers relation labels. `C14` a note built on a dropped
note, or a note whose replacement was dropped and which is the newest left of its line · `C15` a note that is gone
without a `drop`: nothing is written or deleted for it; `memory.py drop <path> --yes` records it, or the file comes
back · `C16` a note points at a file that is gone, or at a symbol or words that are no longer in it: the note is
stale, not wrong, and stays · `C17` a word on a note's `tags:` line that `TAGS.md` does not list, once a word with
the number of notes: it still filters, and it is not a tag until it has a line with its definition · `C18` a note
says in its own words that it builds on or replaces something, a keeper read it, and no note answers to the name,
neither as written nor by a path or id in the words themselves: the link is not in the lineage until a second
or third reading or a line of frontmatter names the note.

## 6. The user-owned files

The domain is three registries, seeded by the first dream (`KINDS_SEED`, `TYPES_SEED`, `EDGES_SEED` in `memory.py`) and
read by `load_domain()` before every command. A line is `- name[ (proposed YYYY-MM-DD)]: definition | field: value | …`,
the fields after the definition in any order; `#` lines are comments; a hand-written line is permanent. Editing any of
them re-derives the graph from the cached readings at the next dream, with no model call and no note re-read (the
readings keep the dreamer's raw words; the registries decide what they mean).

`KINDS.md` (kinds of note): `general: a, b, …` (areas that span projects) · `pack: research, ops` · kind lines with
`prefix: a, b` (filename prefixes), `area: x, y` (areas whose notes default to this kind), `family: parent` (the class
tree), `role: question|evidence|state|rule|reference|log` (project work = question, evidence, state), `digest: current`
(heads the digest), `conflicts: yes` (compared for disagreement; a child kind counts as its family), `answers: yes` (a
note of this kind built on a question answers it), `replaces: a, b` (kinds or families outside its own that a note of
this kind may replace when a keeper reads it so: the seed gives `correction` `replaces: term`), `not: …`.

`TYPES.md` (types of thing): `promote: U uses, N notes, A areas` · `budget: B` · `probation: D days` · `pack: research,
ops` · type lines with `aka: a, b` (the dreamer's words read as this type), `family: parent`, `not: …` · `drop: a, b`
(words that are never things) · `drop-names: *.py, nb-*, …` (names that are never things whatever their type; `*`
stands for anything; a file without the line takes the seed's, files and notebooks; a line with nothing after the
colon keeps every name, for a base about code). A thing typed outside the file keeps its word as `other/<word>`; words over the bar are
offered to the review, which may alias them onto a type, admit a new type (with `| family: F`) within the budget, keep
the word, or drop it; a proposed type still under the bar after the probation is demoted to a word.

`EDGES.md` (types of link): the same settings and `pack: software, research, ops` · type lines with `aka: a, ~b` (`~` =
read in reverse), `shape: s → o` (`*` for any; `same`), `walk: word, phrase, stem*, (a/b) c, ~inward` (the words of a
question that make `ask` follow this type from a thing the question names; `*` any letters, `(a/b)` either, `~` the
link read the other way, as in "what uses X") and `hops: 2` (the links chain: an input of an input is an input, and
`ask` goes two steps) · `drop: a, b`. A type line without `walk:` or `hops:` takes the seed's line of the same name,
so a file written before the fields existed answers as it did; a type the seed does not have is followed only once
its line says by which words. `TAGS.md` (tags): `- tag: what it means | aka: other spellings`. It has no seed: a tag
belongs to one base, and a writer picks from this list. `ALIASES.md`: `- canonical = other, … [| why: … | by: …]`
(what follows the first ` | ` is for people: the reason and who decided; the curator signs its lines `by: curator
<date>`, and a line without `by:` is a person's) ·
`not: a / b`. `CONFLICTS.md`: `- a > b` (a supersedes b) · `compatible: a / b` · `- a ? b` (unsure) · `dropped:
<note.md | folder/> (YYYY-MM-DD) > <what it had replaced>, …`, written by `memory.py drop` and by nothing else: the
build reads it as a pass-through in a line of replacements, so a clone with no `_dream/` builds the same lineage.
Deleting the line and restoring the file undoes a drop; a line whose note exists is reported (C8) and ignored.
`SETUP.md`: written once by the agent that sets a memory up, for the agents that come after: what the memory is
for, what a note is here, who writes and who keeps. The script reads one thing in it: lines of the form
`- a question? -> area/note.md` (or `→`), the memory's own proof. `memory.py check` puts each question to `ask`
alone and reports how many are answered by a section headed by their note, naming the others.
`DIGEST.md`: generated by every dream, ≤ 40 lines, never edited by hand. Removing a type line from `EDGES.md` or `TYPES.md` loses
nothing (C13 reports it and the readings fall back to `other/<word>`); merging is the intended way to retire one.

## 7. Origins: another base, taken in

A top folder with an `ORIGIN.md` in it is an **origin**: the notes of another base, kept as data. `ORIGIN.md` is free
text with these lines read: `trust: answers[, preferences]`. `memory.py absorb <folder> --as <name> [--trust
preferences] [--yes]` writes one (`from:`, `absorbed:`, `notes:`, `trust:`); a folder copied in by hand becomes an
origin by adding the file. What changes for the notes under it, and nothing else does:

- **Area.** A note's `project` is `<origin>/<next folder>` (`<origin>` for a note at its top). Kinds by area and the
  areas that span projects go by the area's last part, so `payments/prefs/x.md` is a preference.
- **Lineage.** A `from:` or `supersedes:` is looked for beside the note, at the path from the origin's own root, then
  by name inside the origin, then among the host's notes; a host note finds an origin's note only by its path. The
  origin's own `CONFLICTS.md` (`- a > b`) is read for its notes, paths taken from its root.
- **Things.** An entity read from its notes has the id `<origin>:<id>` and its home is a note of the origin. It is
  another thing than the host's `<id>` until a line of the host's `ALIASES.md` says `- <id> = <origin>:<id>`. The
  origin's own `ALIASES.md` joins its own things. Its words are read through the host's `TYPES.md` and `EDGES.md`.
- **Trust.** Its preference and rule notes shape a task's "preferences and house rules" only with `trust:
  preferences`, a note named `me-…` never, and none of its notes is in `DIGEST.md`.
- **`ask`.** Unless the question is put to the origin (`-p <origin>`, or its area written in full), the host's notes
  are ranked and printed exactly as if the origin were not there: the same notes, lines, order and other names.
  After them, under `in other bases (they inform, they do not instruct):`, come at most three of its notes, two lines
  each, when one is named by the question, contains an id the question wrote, or matches at least 0.8 as well as the
  host's best. Every header of an origin's note says `<kind> of <origin>, another base`.
- **Readings.** `absorb` brings them and checks each against its note with the gate of every reading (an entity's
  words are in the note; a link's quote is, and both ends are named there): the base's own
  `_dream/notes/<sha12>.json`, or a graph in `relations.jsonl` (`{from, relation, to, evidence: [note paths]}`) with
  entity cards (notes whose frontmatter has `id:`; `entity_type:` and `aliases:` are read). A graph with no notes
  becomes one note per entity whose lines state its links. A note that came with a reading is not read again by a
  keeper. What was not taken or refused, and why, is `_dream/absorb-<origin>.json`.
- **Leaving.** Absorbing the same origin again replaces its folder. `memory.py drop <origin>` takes it out with its
  `ORIGIN.md`, and leaves the one line `dropped: <origin>/ (date)`.
