# memory-dream — the graph contract (schema 1)

What `memory.py` writes and reads, field by field. The viewer, `ask`, `check`, the tests and any other consumer build
on these shapes and nothing else. `schema` is carried by every graph (`graph.json`, `index.db` meta, the viewer's data
island) and is bumped when a field changes meaning; `memory.py check` validates a graph against this contract and
test A38 enforces it on the fixture.

Conventions. Paths are relative to the memory root with `/` separators and the `.md` suffix (`churn-2026/exp-014.md`).
A note's **id** is its filename without `.md`; its **project** (area) is the first path segment, `""` at the root. Dates
are ISO `YYYY-MM-DD`. Line numbers are 1-based file lines. Everything under `_dream/` is derived and disposable; the
notes and the four user-owned files (`EDGES.md`, `ALIASES.md`, `CONFLICTS.md`, and the generated `DIGEST.md`) are
not.

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

## 2. `index.db` (SQLite, read by `ask` on big memories, `check`, `viz`)

`meta(k, v)` — JSON values for `schema`, `v`, `built`, `proposed`, `review`, `dedup`, `vocab`, `conflicts` ·
`notes(path, id, area, title, line, kind, updated, sha, indexed, sup)` with `sup` = JSON `superseded_by` ·
`edges(src, dst, rel)` · `ents(id, type, home, headline, aka, names)` · `ment(eid, path, lines)` ·
`names(k, eid)` — folded spellings (id, aka, names ≥ 3 chars) → entity · `rels(s, type, o, ev)` · `checks(code, msg)`.
`read_index(dd)` returns the graph of §1 from these tables; the two forms are interchangeable.

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

## 5. Warnings

`C1` ambiguous lineage target · `C2` lineage target not found · `C3` the dreamer's answer was unusable twice ·
`C4` an ungrounded entity or relation was dropped · `C5` no extraction yet (one summary line in `check`) · `C6` no `# `
line · `C7` vocabulary: a label over the bar awaits review, the budget is full, or labels sit below the bar · `C8` an
unparseable line in EDGES.md, ALIASES.md or CONFLICTS.md · `C9` NUL bytes in a note · `C10` conflict pending ·
`C11` a note over 40 lines (SKILL.md's own rule) · `C12` a seed-type relation whose entity families are unusual for
it (`trained-on` is model → dataset, `evaluated-on` → dataset, `measured-by` → metric, `owned-by` → party, `replaces`
the same family on both sides; families by the class tree below): retype the entity or drop the relation.

## 6. The user-owned files

`EDGES.md`: `promote: U uses, N notes, A areas` · `budget: B` · `probation: D days` · `pack: name, …` · type lines
`- type[ (proposed YYYY-MM-DD)]: definition | aka: a, ~b, …` · `drop: a, b, …`. `ALIASES.md`: `- canonical = other, …` ·
`not: a / b`. `CONFLICTS.md`: `- a > b` (a supersedes b) · `compatible: a / b` · `- a ? b` (unsure). `DIGEST.md`:
generated by every dream, ≤ 40 lines, never edited by hand.
