# memory-dream — build spec v0.4

Place at `.specs/memory-dream/build-spec.md` · 2026-10-30 · supersedes v0.3
Build target: `skills/memory-dream/` (SKILL.md, `scripts/memory.py`, optional `agents/memory-dreamer.md`).

(Transcribed from the "Memory" email of 2026-10-30; hard line wraps rejoined.)

## Changes from v0.3

- **The graph is a union of per-note subgraphs** (§5.3). The dreamer turns each note into a small subgraph: its entities, the relations it states between them (each entity's edges out), and a summary. The graph is the union of those subgraphs after renaming entity ids and relation types to canonical names. Dedup is that renaming and nothing else.
- **Change and removal** (§5.3). The union is recomputed from the notes that exist now; extractions are only a cache keyed by note hash. An edited note's old extraction is never read again; a deleted note contributes nothing from the next answer on, at no call.
- **Relation types** (§4.6): `memory/EDGES.md`, a short vocabulary the dreamer reads. It may propose new types; they work at once, marked, until a review maps each to an alias, a reversed alias, a new type, or drop.
- **Entity dedup** (§4.7): prevented by the KNOWN list in the prompt, done for free by two merge rules, never merging versions, with leftover lookalikes judged once each in the same review call (§4.8). Decisions live in `memory/ALIASES.md`.
- **Entity = pointers + headline** (§5.1). Each entity shows the title of its best live note as its headline conclusion, at no call; gists stay optional.
- **Lineage stays fixed**: `from`, `supersedes`, `refs` sit outside both vocabularies. `trace` also walks entity relations (`trace cards.txn_daily --down`).
- Checks C7 (vocabulary pending) and C8 (unparseable vocabulary lines).

## 0. Thesis

| role | writes | reads | cost |
|---|---|---|---|
| main agent (day) | notes: `memory/<project>/<slug>.md` | INDEX.md, `where`, `trace`, then the notes they point to | ~30-line SKILL.md; 1–3 calls per lookup |
| dreamer (night) | JSON answers only (stdout, or files in `_dream/pending/`) | one note + the entity list + EDGES.md | one cheap call per new or changed note; at most one review call per `dream` |
| `memory.py` | `_dream/`, INDEX.md, appends to EDGES.md and ALIASES.md | notes, answers | stdlib, no model |

Notes are the truth. The dreamer builds a routing table: which files, which lines, which entities, how they relate. A dreamer mistake costs recall, never correctness, because the main agent reads the source before using anything.

Each note becomes a small subgraph and the graph is their union after renaming, so connecting notes costs nothing beyond dedup, and dedup is mostly free (§4.7).

The one thing a dreamer cannot recover is lineage: "this decision came from that finding" is known at write time and often unstated. So it is the main agent's single duty: `from:`.

## 1. Stance

- Bare minimum: markdown + JSON, stdlib Python. No DB, no embeddings; hooks optional.
- The main agent writes like an analyst keeping lab notes: no entity tagging, no taxonomy, no format errors.
- The dreamer gets no tools and never touches notes. A "rewrite" is a derived summary, never an in-place edit.
- Ground, don't trust: an entity survives only if its text is in the note, a relation only if its quote is, a summary only if every number in it is.
- Derived is never state: the graph is a function of the current notes, EDGES.md and ALIASES.md. The cache saves calls; it holds no truth.
- Two edge families. Lineage is fixed: the backbone retrieval depends on. Relations are open: a vocabulary that grows by proposal and shrinks by aliasing.
- Dedup by renaming, never rewriting: raw names stay in the cache; EDGES.md and ALIASES.md rename at merge time, so any correction costs zero calls.
- Never merge versions: ids that differ only in digits (`churn-xgb-v2`, `churn-xgb-v3`) are different things unless ALIASES.md says otherwise.
- When unsure, keep apart: a duplicate costs a longer list; a wrong merge loses meaning.
- Built for smarter models: the contract is notes + `from:` + one JSON shape + two vocabulary files. Nothing to migrate.

## 2. Layout

```
memory/
  INDEX.md              generated entry point
  EDGES.md              relation types: curated, the review appends, seeded if missing
  ALIASES.md            entity merges and judged-different pairs: curated, the review appends
  <project>/<slug>.md   notes (main agent) — the truth; folders are free
  log/YYYY-MM-DD.md     optional append-only scratch; indexed like any note
  _dream/               derived; safe to delete
    manifest.json       path → sha, former paths (move detection)
    notes/<sha12>.json  one grounded extraction per note version
    entities/<id>.json  optional gists
    pending/            file mode: <sha12>.prompt.md → <sha12>.json; review.prompt.md → review.json
    graph.json          merged pointer graph
```

Root: `--root` → `$MEMORY_DIR` → nearest `memory/` upward from cwd → `./memory`. Git: commit notes, `log/`, INDEX.md, EDGES.md, ALIASES.md; committing `_dream/` too saves re-indexing on a fresh clone.

## 3. Notes

Note = any `*.md` under `memory/` except `INDEX.md`, `EDGES.md`, `ALIASES.md`, `README.md` and `_dream/`. id = filename stem; the path disambiguates. Line numbers are 1-based file lines, frontmatter included, so they work directly as Read offsets.

Frontmatter is optional; two keys matter:

```
---
from: [exp-014]               # notes this built on: the lineage pointer
supersedes: [leak-hypothesis] # notes whose conclusion this overturns
---
```

Values: stems, relative paths or `[[stem]]`. Resolution: path → stem in the same folder → unique stem anywhere → former paths in the manifest → unresolved (C2). Everything else is optional: a declared `type` overrides the dreamer's guess; body `[[links]]` outside code become `refs` edges.

### 3.1 Five rules

1. **One note per thing**: a question, experiment, finding, decision, or a description of a dataset, feature, model or metric. Put it in `memory/<project>/`; the filename is its id.
2. **The `# ` line is the point**: the claim, or what the thing is ("Post-period aggregation leaks target: AUC 0.81→0.74 without it"). First paragraph = what is true now.
3. **`from:` the notes you built on; `supersedes:` the notes you overturn.** Never rewrite an old conclusion; write a new note.
4. **Numbers carry metric, eval set, n, date.** Name sources (tables, notebooks, queries) in backticks.
5. **≤ 40 lines, plain markdown**, nothing about the memory system.

Mid-session scratch: one line in `log/YYYY-MM-DD.md` (`- HH:MM [project] text`), via `memory.py log`.

```
---
from: [exp-014]
---
# Post-period aggregation leaks target: AUC 0.81→0.74 without it
holdout-2025q4, n=1.2M, 2026-10-29. The velocity features built on `cards.txn_daily`
aggregate past the observation date. Rebuild without post-period columns (v3).

Evidence: `nb/eda_velocity.ipynb`, cells 12–18.
```

## 4. Dream

### 4.1 When

`memory.py dream`: at session end (main agent, background is fine), on a schedule, or by hand; same command everywhere. Only notes with a new hash cost a call:

$$\mathrm{index}(n) \iff \mathrm{sha}(n) \notin \texttt{\_dream/notes/}$$

### 4.2 Calling the model

- **Command mode** (default): `$MEMORY_LLM` or `--cmd`, e.g. `claude -p --model haiku --tools ""` (the empty `--tools` disables every tool; older CLIs: `--disallowedTools`). Prompt on stdin, answer on stdout; the model has no tools. `-j N` runs calls in parallel.
- **File mode** (no command): the tool writes prompts to `_dream/pending/`; any agent answers by writing the `.json` beside each (e.g. the `memory-dreamer` subagent, §11); the next `dream` ingests them.

### 4.3 Prompt (embedded in memory.py)

```
Index this memory note for retrieval. Reply with JSON only:
{"kind": "question|experiment|finding|decision|dataset|feature|model|metric|concept|log|note",
 "summary": "the main point in at most 25 words; copy numbers exactly",
 "entities": [{"id": "...", "type": "dataset|feature|model|metric|segment|person|concept|tool|project|other",
               "as": ["text copied verbatim from the note"]}],
 "relations": [{"s": "entity id", "type": "relation type", "o": "entity id",
                "quote": "short text copied verbatim from the note that states it",
                "def": "only for a type not in EDGES: a one-line definition"}],
 "refs": ["ids or paths of other notes the text explicitly points to"]}
Entities are named things someone would look up later: tables, columns, features, models,
metrics, segments, people, methods, tools. Not generic words.
If an entity is in KNOWN, reuse its id. Otherwise id = its most specific name, lowercase,
spaces to hyphens.
Relations: only ones the note states, read "s <type> o". Use an EDGES type or one of its
aliases (aliases marked ~ read in reverse). If none fits, name a new type and give "def".
EDGES:
{the type lines of EDGES.md}
KNOWN:
{one "id (type): surface; surface" line per canonical entity, same project first, then by note count, max 300}
NOTE {path}:
{text}
```

Sample answer for the §3.1 note:

```json
{"kind": "finding",
 "summary": "Post-period aggregation in velocity features leaks the target; AUC 0.81→0.74 without it on holdout-2025q4.",
 "entities": [{"id": "feat-velocity-v2", "type": "feature", "as": ["velocity features"]},
              {"id": "cards.txn_daily", "type": "dataset", "as": ["cards.txn_daily"]},
              {"id": "auc", "type": "metric", "as": ["AUC"]}],
 "relations": [{"s": "feat-velocity-v2", "type": "built-on", "o": "cards.txn_daily",
                "quote": "velocity features built on `cards.txn_daily`"}],
 "refs": ["exp-014"]}
```

`built-on` is an alias of `uses` in the seed (§4.6), so this lands as `feat-velocity-v2 uses cards.txn_daily`, evidence `churn-2026/post-period-leak.md:5`.

### 4.4 Ingest (tool, deterministic)

1. Parse the first `{` … last `}` of the answer; on failure retry once, then mark the note failed (C3).
2. **Entities**: keep iff one of its `as` strings occurs in the note (case-insensitive); lines = every line containing a kept string.
3. **Relations**: keep iff `s` and `o` are kept entities of this note and `quote` occurs in the note (case-insensitive, whitespace runs collapsed); line = where the quote starts. Store the type as written, with `def` if given.
4. **Summary**: keep iff all its numbers occur in the note; else use the `# ` title.
5. **refs**: store as written; they resolve at merge (§5.3).
6. Write `_dream/notes/<sha12>.json`: kept fields + `path, sha, model, indexed_at, dropped`. Ids and types stay as written; renaming happens only at merge.

With $n$ the note text and $\mathrm{nums}(x)$ all matches of `\d+(?:\.\d+)?` in $x$:

$$e \text{ kept} \iff \exists\, a \in \mathrm{as}(e):\ a \text{ occurs in } n$$

$$(s, t, o, q) \text{ kept} \iff s, o \in E_{\text{kept}}(n) \;\wedge\; q \text{ occurs in } n$$

$$\text{summary kept} \iff \mathrm{nums}(\text{summary}) \subseteq \mathrm{nums}(n)$$

### 4.5 Entity gists (optional, `dream --gists`)

For entities in ≥ 3 notes whose mention set changed: one call with the mention lines (± 1 line, newest 30, each tagged with note id and date) → `{"gist": "at most 40 words", "key": ["note ids"]}`. Numbers grounded as in §4.4; `key` must come from the given notes. Stored in `_dream/entities/<id>.json` with the mention-set hash; a gist is shown only while that hash still matches. The free headline (§5.1) usually makes gists unnecessary.

### 4.6 Relation types — `memory/EDGES.md`

One relation type per line, read "X <type> Y". The tool writes this seed when the file is missing; edit it freely.

```
# EDGES — relation types, read "X <type> Y". Edit freely; relations relabel on the next merge.
- uses: X needs Y as an input (model uses feature; feature uses table) | aka: depends-on, consumes, built-on, ~feeds
- produces: X creates or writes Y (notebook produces table; job produces scores) | aka: writes, creates, ~generated-by
- part-of: X is a component of Y (column part-of table; feature part-of feature-set) | aka: ~contains, ~has
- trained-on: model X was fit on dataset Y | aka: fit-on
- evaluated-on: X was measured on dataset or segment Y | aka: tested-on, validated-on
- replaces: X is the newer version of Y | aka: supersedes, ~replaced-by
- owned-by: X is maintained by person or team Y | aka: maintained-by, ~owns
drop: related-to, associated-with, about
```

Grammar: `- <type>: <definition>` with optional ` | aka: a, b, ~c`; `~` marks an alias read in reverse; one `drop:` line; anything else that is not blank or a `#` line is ignored (C8). Types and aliases are folded (lowercase; space and `_` → `-`) before matching.

Renaming, at every merge, for a stored relation $(s, t, o)$ and canonical types $\mathcal{T}$:

$$\alpha_R(s, t, o) = \begin{cases} (s,\ T,\ o) & t = T \text{ or } t \in \mathrm{aka}(T),\ T \in \mathcal{T} \\ (o,\ T,\ s) & {\sim}t \in \mathrm{aka}(T) \\ \varnothing & t \in \mathrm{drop} \\ (s,\ t?,\ o) & \text{otherwise: proposed, live, marked} \end{cases}$$

Proposed types go to the review (§4.8) once they have ≥ 2 uses; until then they work, marked `?`. The types half of C7 is a set difference over what exists now:

$$\mathrm{C7}_{\text{types}} = \mathrm{types}\big(\{x_{\mathrm{sha}(n)}\}_{n \in \mathcal{N}_{\text{now}}}\big) \setminus \big(\mathcal{T} \cup \mathrm{aka}(\mathcal{T}) \cup \mathrm{drop}\big)$$

### 4.7 Entity dedup — `memory/ALIASES.md`

The same thing can come back under different ids from different notes. Dedup is a renaming applied at every merge, cheapest steps first:

1. **Prevent** (free): the extraction prompt lists KNOWN canonical ids with their surface forms, so the dreamer reuses them.
2. **Merge by rule** (free, no call):
   - ids equal after folding are one entity (`Cards.TXN_daily` = `cards.txn_daily`);
   - when exactly one other entity uses an entity's id as a surface form, they are one entity (`txn-table`, written `cards.txn_daily` in its note, joins `cards.txn_daily`).
3. **Review leftovers** (one batched call, §4.8): pairs of the same type that share a surface form, or whose folded ids have `difflib` ratio ≥ 0.85; computed only for ids new since the last `dream`; at most 30 per call. Each pair is asked once; the answer goes into ALIASES.md.
4. **Apply** (every merge): rule merges plus every ALIASES.md line, as one union-find. Relation endpoints rename with their entities; identical relations combine their evidence; self-loops drop.

Never merged by a rule or a review: ids that differ only in digits (versions), and pairs on a `not:` line. A surface form shared by more than 3 entities is too generic to count as evidence. Canonical id of a group: the first id of its ALIASES.md line, else the id the notes write most often (surface forms count when they fold to it; ties: alphabetical).

$$a \ne b \;\wedge\; \mathrm{strip}_{0\text{-}9}(a) = \mathrm{strip}_{0\text{-}9}(b) \;\Longrightarrow\; a \not\equiv b \quad \text{unless an ALIASES.md line joins them}$$

```
# ALIASES — entity ids that name the same thing; the first id on a line is canonical. Edit freely.
- cards.txn_daily = txn-table, txn-daily-tbl
- risk-tier-cuts = risk-tier-cutoffs
not: feat-velocity-v2 / velocity-features
```

Grammar: `- <canonical> = <id>, <id>`; `not: <a> / <b>`; anything else that is not blank or a `#` line is ignored (C8). Ids fold before matching. A line whose ids no longer occur is harmless.

### 4.8 Review — one cheap call for both vocabularies

`dream` makes at most one review call: when a proposed relation type has ≥ 2 uses or an entity pair awaits review. `--review` forces it.

```
You keep the vocabulary of a data-science memory.
RELATION TYPES, read "X <type> Y":
{type lines of EDGES.md}
PROPOSED TYPES (definition; uses; up to 3 examples "X — Y: quote"):
{proposals, or "none"}
ENTITY PAIRS that may name the same thing (id, type, surface forms, one context line each):
{pairs, or "none"}
Reply with JSON only:
{"types": {"<proposed>": "alias T" | "alias ~T" | "new" | "drop"},
 "entities": {"<a> / <b>": "same" | "different"}}
If unsure between alias and new, answer new. If unsure whether two entities are the same
thing, answer different. Versions (v2, v3) are different things.
{only when EDGES.md has more than 20 types: also list existing types that mean the same as
another, under "types", as "A": "alias B".}
```

Apply (tool); the next merge renames, nothing is re-indexed:

- `alias T` or `alias ~T` → append to T's aka in EDGES.md (unknown T → treated as `new`); `new` → append `- t: <def>`; `drop` → append to the `drop:` line; an existing type answered `alias B` → its line and aliases fold into B's aka.
- `same` → add the pair to ALIASES.md, onto the line that already holds either id, else a new line led by the id with more mentions; `different` → append `not: a / b`.
- Anything else is ignored and asked again next time. The summary line prints what changed; git shows the diff.

## 5. Merged outputs

### 5.1 graph.json

```json
{"v": "0.4", "built": "2026-10-30T17:10",
 "notes": [{"path": "churn-2026/post-period-leak.md", "id": "post-period-leak", "project": "churn-2026",
            "title": "Post-period aggregation leaks target: AUC 0.81→0.74 without it",
            "summary": "…", "kind": "finding", "superseded_by": [], "updated": "2026-10-30",
            "sha": "9f2c41ab07de", "indexed": true}],
 "entities": [{"id": "feat-velocity-v2", "type": "feature", "aka": ["velocity-features-v2"],
               "names": [{"name": "feat-velocity-v2", "n": 4}, {"name": "velocity features", "n": 3}],
               "headline": "churn-2026/post-period-leak.md",
               "mentions": [{"path": "churn-2026/post-period-leak.md", "lines": [5]},
                            {"path": "churn-2026/exp-014.md", "lines": [3, 4, 5]}],
               "gist": null}],
 "relations": [{"s": "feat-velocity-v2", "type": "uses", "o": "cards.txn_daily", "canon": true,
                "evidence": ["churn-2026/post-period-leak.md:5", "churn-2026/feat-velocity-v2.md:6"]}],
 "edges": [{"src": "churn-2026/post-period-leak.md", "dst": "churn-2026/exp-014.md", "rel": "from"}],
 "proposed": [{"type": "fitted-on", "def": "model X was fit on dataset Y", "uses": 2}],
 "review": [{"a": "risk-tier-cuts", "b": "risk-tier-cutoffs"}]}
```

- `edges` = lineage between notes, by path: `from`, `supersedes` (writer); `refs` (dreamer, or body `[[links]]`).
- `relations` = typed entity→entity, renamed and combined across notes; `evidence` = where each is stated; `canon: false` = proposed type.
- An entity is pointers plus a headline: `mentions` (note and lines), `names` (surface forms with counts), its relations' `evidence`, `aka` (ids merged into it), `headline` (below). `gist` only with `--gists`.
- `updated` = frontmatter `updated` if present, else file mtime. Entity type = most frequent across notes. Co-mentions are computed at query time.
- DuckDB: `select unnest(relations, recursive := true) from read_json('memory/_dream/graph.json')`. Field names avoid SQL keywords, and map-like data is stored as lists of records (never as keys), so the schema stays stable and nothing needs quoting.

Headline = the entity's best live note (mentions it, not superseded), compared lexicographically; recomputed at every merge, so it follows edits and deletions, at no call:

$$\mathrm{headline}(E) = \operatorname*{arg\,max}_{n \,\in\, \mathrm{live}(E)} \Big(\mathbb{1}[E \text{ is named on the title line of } n],\ \mathbb{1}[\mathrm{kind}(n) \in \{\text{finding}, \text{decision}\}],\ t_n\Big)$$

### 5.2 INDEX.md

```
# memory · 2026-10-30 17:10 · 84 notes · 132 entities · 210 relations (2 proposed) · 3 pending · 2 warnings
## projects
- churn-2026 · 31 notes · 10-30
- collections-uplift · 12 notes · 10-27
## recent (7d)
- churn-2026/post-period-leak.md · finding · 10-30 — Post-period aggregation leaks target: AUC 0.81→0.74 without it · from exp-014
## entities (top 20 by notes, with headline)
- feat-velocity-v2 · feature · 7 notes — Post-period aggregation leaks target: AUC 0.81→0.74 without it
## churn-2026
- post-period-leak.md · finding · 10-30 — Post-period aggregation leaks target: AUC 0.81→0.74 without it · from exp-014
- feat-velocity-v2.md · feature · 10-12 — 30-day transaction velocity per account (superseded → feat-velocity-v3)
```

Head (≈ 40 lines) = orientation. Body = every note, newest first per project, one line each.

### 5.3 Change and removal

Everything derived is recomputed from what exists now:

$$\mathcal{G} = \bigcup_{n \,\in\, \mathcal{N}_{\text{now}}} \alpha\big(x_{\mathrm{sha}(n)}\big)$$

where $x_h$ is the cached extraction for content hash $h$ (the note's subgraph) and $\alpha$ renames entity ids (§4.7) and relation types (§4.6); identical relations combine their evidence. Nothing is deleted from the graph; it stops being derived. An entity has no existence of its own: it exists while some current note's extraction mentions it, and the KNOWN list in prompts follows. `from:`, `supersedes:` and `refs` targets resolve at merge, so removing a target drops those edges without a call.

| event | what changes | model calls |
|---|---|---|
| note edited | its old summary, entities, relations, refs and line pointers drop from the next answer; it shows as unindexed (grep fallback) until the next `dream` | 1, at the next `dream` |
| note deleted | everything derived from it drops from the next answer; entities only it mentioned disappear; headlines move to the next best note; notes whose `from:` named it get C2 | 0 |
| note moved or renamed, content unchanged | pointers follow the new path; old ids resolve via former paths | 0 |
| edit reverted within 30 days | the cached extraction is reused | 0 |
| EDGES.md or ALIASES.md edited | relations and entities rename at the next merge | 0 |
| an entity's mention set changed | its gist (if any) hides until the next `--gists` run | 1, if gists are on |

Freshness: every verb stats the notes first; if anything differs from the manifest it re-hashes only the changed files and re-merges in memory before answering, so `where` and `trace` never point at a deleted note or a stale line. Only `dream` calls the model or writes files. `dream` deletes cache entries unreferenced for 30 days.

## 6. Retrieval

```
$ memory.py where cards.txn_daily
cards.txn_daily · dataset · 9 notes · aka txn-table · as "cards.txn_daily", "txn table"
  headline churn-2026/ds-txn-2025q4.md:4  Q4-2025 snapshot of cards.txn_daily, one row per account-day
  ← uses feat-velocity-v2, feat-velocity-v3, feat-utilization-v1   churn-2026/feat-velocity-v3.md:6 (+4)
  ← trained-on churn-xgb-v3   churn-2026/churn-xgb-v3.md:8
  → owned-by data-eng-cards   churn-2026/ds-txn-2025q4.md:3
  churn-2026/post-period-leak.md:5  finding 10-30  Post-period aggregation leaks target: AUC 0.81→0.74 without it · from exp-014
  … +7
unindexed
  log/2026-10-30.md:4  txn table backfill running
```

- `where <terms…> [-p P]`: matches ids, aliases, surface forms, titles, summaries, paths (fuzzy fallback via `difflib`). Entities first (≤ 8), each with its headline, relations (`→ t Y` = this entity t Y; `← t Y` = Y t this entity; proposed types end in `?`; one evidence pointer each) and notes (≤ 8, newest first); then other matching notes; then grep hits in unindexed notes. Superseded notes show their successor.
- `trace <note or entity> [--up/--down] [--rel t,…] [--depth N]`: a note walks lineage (`from`, `refs`; `supersedes` targets print as leaves). An entity walks relations: `--up` follows its own relations outward (what it needs), `--down` follows relations pointing at it (what depends on it); `--rel` filters types. Default `--up`, depth 3; repeats print `(seen)`; each step shows one evidence pointer.

```
$ memory.py trace churn-xgb-v3
churn-2026/churn-xgb-v3.md · model · 10-30
├─ from feat-velocity-v3.md · feature · 10-30
│  └─ from dec-velocity-v3.md · decision · 10-30
│     └─ from post-period-leak.md · finding · 10-30
└─ supersedes churn-xgb-v2.md · model · 10-02

$ memory.py trace cards.txn_daily --down
cards.txn_daily · dataset
├─ ← uses feat-velocity-v3 · feature · churn-2026/feat-velocity-v3.md:6
│  └─ ← uses churn-xgb-v3 · model · churn-2026/churn-xgb-v3.md:7
├─ ← uses feat-utilization-v1 · feature · churn-2026/feat-utilization-v1.md:5
└─ ← trained-on churn-xgb-v3 · model (seen)
```

## 7. Tool — `scripts/memory.py`

Stdlib only (`argparse, re, json, hashlib, pathlib, subprocess, concurrent.futures, difflib, datetime`). One file, ≤ ~600 lines; the prompts, the EDGES seed and the ALIASES header live in it.

| verb | does |
|---|---|
| `dream [--cmd C] [-j N] [--gists] [--review] [--all]` | rescan, detect moves, index new hashes, ingest pending answers, review vocabularies when due (≤ 1 call), merge → graph.json + INDEX.md, delete stale cache; prints one summary line |
| `where <terms…> [-p P]` | pointers, headlines and relations (§6) |
| `trace <note or entity> [--up/--down] [--rel t,…] [--depth N]` | lineage or relation walk (§6) |
| `check` | the warnings in full (§8) |
| `log "text" [-p P]` | append `- HH:MM [P] text` to today's log |

Summary line: `dream: 84 notes · 5 indexed (5 calls) · review: 12 pairs, 1 type (1 call) · +3 aliases · 2 moved · 1 deleted · 3 pending · C2×1 C4×2 C7×1`

`--all` re-indexes everything: after changing the dreamer model, or once to converge entity ids when the KNOWN list is complete. Every verb rescans first (§5.3).

## 8. Checks (all warnings)

| code | when | effect |
|---|---|---|
| C1 | two notes share an id and a `from:` is ambiguous | resolves to the same-project note |
| C2 | a `from:` or `supersedes:` target is not found (deleted, typo, or renamed and edited in one step) | that lineage edge is missing |
| C3 | a dreamer answer is unusable after one retry | note stays unindexed; `where` greps it |
| C4 | grounding dropped entities, relations or a summary | dreamer quality signal; counts only |
| C5 | notes pending (no extraction yet) | `where` greps them |
| C6 | note without a `# ` line | INDEX shows the path |
| C7 | vocabulary pending: proposed relation types (with uses) and entity pairs awaiting review | proposed types live as `type?`; review runs when due (§4.8) |
| C8 | a line in EDGES.md or ALIASES.md the tool can't parse | that line is ignored |

That is the whole validation layer; no note can fail. C7 is the vocabulary checker: the set difference of §4.6 for types, the candidates of §4.7 for entities.

## 9. Guarantees

- Only the main agent writes notes; the tool writes only `_dream/`, INDEX.md, `log/` (via `log`), and appends to EDGES.md and ALIASES.md.
- Edit or delete a note → everything derived from it is gone from the next answer; deletion costs no call, an edit one.
- Move or rename a note without editing it → zero calls; old ids keep resolving.
- Change EDGES.md or ALIASES.md in any way → zero calls; everything renames at the next merge.
- Versions never merge unless ALIASES.md says so; each entity pair is reviewed at most once.
- Lineage never depends on the vocabularies or the dreamer.
- Delete `_dream/` → `dream` rebuilds (re-indexing costs calls; the vocabularies survive).
- Reorganize folders, drop frontmatter, write any markdown style → pointers get weaker; nothing breaks.
- No model → lineage, titles, INDEX and grep fallback still work.
- Everything is readable without the tool: notes, INDEX.md, EDGES.md, ALIASES.md, graph.json.

## 10. Not built

| not built | why | seam if ever needed |
|---|---|---|
| dreamer rewriting notes | notes are the truth; a cheap model drops nuance and numbers silently | derived summaries already exist |
| contradiction detection | supersession is declared; contradictions are the reader's job | — |
| writer-declared relations | the main agent's only duty stays `from:` | frontmatter keys named like EDGES types |
| type constraints (e.g. trained-on: model → dataset) | no schema | a column in EDGES.md if mistyped relations ever hurt |
| embeddings | `where` over ids, aliases, surface forms, titles, summaries first | embed summaries keyed by sha, and entity names as review candidates, with a local model |
| DB, UI, required hooks | markdown + JSON only | DuckDB reads graph.json as-is |

## 11. Deliverables

```
skills/memory-dream/
  SKILL.md                  ≤ 40 lines (§12)
  scripts/memory.py         §7; prompts, EDGES seed and ALIASES header embedded
  agents/memory-dreamer.md  optional: file-mode subagent; copy to .claude/agents/
.specs/memory-dream/
  build-spec.md · RUNBOOK.md · RESULTS.md
```

Must pass `check_skills.py` (R9, R10, R12, R15; the subagent lives in `agents/`, not loose at the root); works with and without hooks.

`agents/memory-dreamer.md` (any agent that can read and write files can play this role):

```markdown
---
name: memory-dreamer
description: Answers memory-dream prompts in memory/_dream/pending/. Use when memory.py dream reports pending prompts.
model: haiku
tools: Read, Write, Glob
---
For each memory/_dream/pending/*.prompt.md that has no matching .json: read it, follow it,
and write only the JSON answer to the same path with .json in place of .prompt.md.
Touch nothing else.
```

## 12. SKILL.md (draft)

```markdown
---
name: memory-dream
description: Project memory for data-science work in memory/. Write short notes as you work, find them with memory.py where, follow lineage and dependencies with memory.py trace, and run memory.py dream at session end so a cheap model indexes new notes. Use whenever a session touches a project, dataset, feature, model, experiment, finding or decision, or when asked to remember or recall.
---
# memory-dream v0.4

Notes in `memory/<project>/<slug>.md` are the truth. `memory/INDEX.md` and `memory/_dream/` are generated; never edit them. `memory/EDGES.md` (relation types) and `memory/ALIASES.md` (entity merges) are yours to edit. `memory.py` = `python skills/memory-dream/scripts/memory.py`.

## Read
- Start: the head of `memory/INDEX.md`, or `memory.py where -p <project>`.
- `memory.py where <terms>`: entities with headline and relations, notes and `path:lines` pointers; superseded notes show their successor. Read what it points to, nothing more.
- `memory.py trace <note>` (what it built on) · `--down` (what built on it). On an entity, `trace <entity> --down` = what depends on it.
- Summaries and relations are hints from a cheap model; the note is the source.

## Write
1. One note per thing (question, experiment, finding, decision, or a dataset/feature/model/metric description), in `memory/<project>/`; the filename is its id.
2. The `# ` line is the point: the claim, or what the thing is. First paragraph = what is true now.
3. Frontmatter `from: [notes you built on]`, `supersedes: [notes you overturn]`. Never rewrite an old conclusion; write a new note.
4. Numbers carry metric, eval set, n, date. Sources (tables, notebooks, queries) in backticks.
5. ≤ 40 lines, plain markdown, nothing about the memory system.
Mid-session scratch: `memory.py log "…" -p <project>`.

## End of session
`memory.py dream` (background is fine). If it reports pending prompts, run the `memory-dreamer` subagent, then `memory.py dream` again.
```

## 13. Acceptance

Fixture: a churn-2026 world of ~30 notes (question → experiment → finding → decision chains, dataset/feature/model notes, two supersessions, a week of log files) written to the five rules.

| id | setup | pass |
|---|---|---|
| A1 | empty `memory/` | `dream` writes INDEX.md, graph.json, the EDGES.md seed and the ALIASES.md header; 0 notes; exit 0 |
| A2 | fixture, no model | lineage edges and supersessions correct; `trace` works on notes; `where` answers from titles + grep; C5 = 30 |
| A3 | fixture, Haiku in command mode | every note indexed once; a second `dream` makes 0 calls |
| A4 | move 5 notes, rename 2, contents unchanged | 0 calls; `from:` pointers to old ids still resolve; graph identical except paths |
| A5 | edit one note | before `dream`: its old pointers and relations are absent and it is listed unindexed; after: exactly 1 call |
| A6 | delete a note that two others name in `from:` | without `dream`: nothing derived from it appears in `where`/`trace`; entities only it mentioned are gone; headlines that pointed at it move on; C2 ×2; 0 calls |
| A7 | revert an edit | 0 calls |
| A8 | injected answers: a fabricated `as` string; a relation whose quote is absent; a summary with a number absent from the note | all three dropped (summary → title); C4 = 3 |
| A9 | answers wrapped in prose or code fences; one invalid JSON | first two parsed; invalid → one retry → C3 |
| A10 | file mode: no command; run memory-dreamer; `dream` again | all pending ingested, review included; 0 failures |
| A11 | relations on the fixture | `uses`, `trained-on`, `evaluated-on`, `owned-by` edges with evidence pointers; `trace cards.txn_daily --down` lists the dependent features and models |
| A12 | two notes yield type `fitted-on` | C7 shows `fitted-on?` ×2 and the edges are live; the review answers `alias trained-on`; it is appended to EDGES.md; the next merge relabels with 0 extraction calls |
| A13 | a note says "the txn table feeds the velocity features" | stored as `… uses cards.txn_daily` via `~feeds` |
| A14 | hand-edit EDGES.md: fold `trained-on` into `uses` | 0 calls; every `trained-on` relation now reads `uses` |
| A15 | entity rules: ids `cards.txn_daily` and `Cards.TXN_daily`; an entity `txn-table` written `cards.txn_daily` in its note; `feat-velocity-v2` and `feat-velocity-v3` both written "velocity features"; `risk-tier-cuts` and `risk-tier-cutoffs` | the first two merge and `txn-table` joins them, 0 calls; v2 and v3 are never merged or asked; the risk-tier pair is asked once, the answer lands in ALIASES.md, the next `dream` asks nothing |
| A16 | hand-edit ALIASES.md: `- cards.txn_daily = ds-txn` | 0 calls; relations and pointers of `ds-txn` now sit on `cards.txn_daily` |
| A17 | headline | `where feat-velocity-v2` shows post-period-leak (its own feature note is superseded); deleting post-period-leak moves the headline to the next note by §5.1, 0 calls |
| A18 | entity convergence | report distinct ids for the fixture's ~12 true entities after one pass and after one review (target ≤ 1.2×) |
| A19 | 1,000 synthetic notes, 2,000 entities | merge with renaming < 1 s; `where` < 0.5 s including the rescan; review candidates for 200 new ids < 2 s |
| A20 | `--gists` | gists only for entities in ≥ 3 notes, numbers grounded; rerun without changes → 0 calls; deleting a cited note hides the gist |
| A21 | POC: fresh Opus main agent with SKILL.md only, 10 fixture questions ("what do we know about feat-velocity-v2?", "what came of exp-014?", "what depends on `cards.txn_daily`?") vs a grep-only baseline; n = 3 | correct answers; report tool calls and tokens per question; the index must cost less than the baseline |

## 14. Open choices

| choice | proposed | alternative |
|---|---|---|
| model call | command mode, no tools | file mode only |
| when to dream | main agent at session end | nightly schedule only |
| gists | off (`--gists`); the headline is free | on |
| KNOWN list in the prompt | 300 ids, same project first | all |
| review gate | a proposed type with ≥ 2 uses, or any entity pair | every `dream` |
| review model | the dreamer (cheap) | main agent |
| entity lookalike cutoff | `difflib` ≥ 0.85, same type | 0.9, or any type |
| merge review of existing types | when EDGES.md exceeds 20 types | never |
| seed types | the 7 in §4.6 | start empty |
| `log/` | kept, indexed like notes | drop |
| commit `_dream/` | yes, skips re-indexing on clone | no |
