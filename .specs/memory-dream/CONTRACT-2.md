# memory-dream — the contract, schema 2 (draft)

2026-11-11 · the draft that goes with `PLAN.md` rev 3, to be agreed before anything is built · `CONTRACT.md`
(schema 1) stays the contract of the code that ships.

Schema 2 adds to schema 1. A base that uses none of the additions is a valid schema 2 base.

## 1. Four rules

1. **A note is the only record that must exist.**
2. **Every other record names the note it rests on** and is checked against that note's text.
3. **The graph is recomputed from the notes that exist now.**
4. **The script does only exact work. What needs judgement is read by an agent and written down as one line with its
   reason.** No threshold and no string distance decides anything.

## 2. The files of a base

```
memory/
  SETUP.md                       what the base is for, what a note is here, who writes and who reads        meaning
  KINDS.md  TYPES.md  EDGES.md   the vocabulary: kinds of note, types of entity, types of edge              meaning
  TAGS.md                        the tags, each with its definition                                         meaning
  ALIASES.md  CONFLICTS.md       decisions: which names are one entity; which note replaced which           meaning
  <area>/<id>.md                 notes                                                                      truth
  <origin>/ORIGIN.md             marks a folder that came from elsewhere                                    meaning
  <origin>/<area>/<id>.md        its notes, in its own areas                                                truth
  _dream/notes/<hash>.json       what a keeper read in one note text; kept in git                           truth
  DIGEST.md  _dream/…            the digest, graph.json, index.db, graph.html, packets                      derived
```

New against schema 1: `SETUP.md`, `TAGS.md`, `ORIGIN.md`, and `_dream/notes/` going into git (the build guide tells
git to ignore all of `_dream/` today). Everything else under `_dream/` can be deleted at any time.

## 3. The records

`*` marks what a record must carry.

| record | lives in | written by | must carry | may carry |
|---|---|---|---|---|
| **note** | `<area>/<id>.md` | an agent or a person | the file* | a `# ` line, a date · `from`, `supersedes`, `type` · new: `source`, `tags` · pointers in its text |
| **reading** | `_dream/notes/<hash>.json` | a keeper | the hash* of the text it read | `kind`, `entities`, `relations`, `refs`, `path`, `model`, `indexed_at` |
| · entity | a reading | | `id`* · `as`* (words found in the note) | `type`, `label` |
| · edge | a reading's `relations` | | `s`*, `o`* (entities of the same reading) · `type`* · `quote`* (found in the note) | `label` |
| **tag** | the note's `tags:` | whoever writes the note | a word* that `TAGS.md` lists | – |
| **pointer** | the note's text | whoever writes the note | `path#symbol`*, or `path:line`* with quoted words | – |
| **term** | a registry line | the setup, a curator, a person | `- name: definition`* | `aka`, `family`, `not`, schema 1's fields · new: `walk` |
| **decision** | `ALIASES.md`, `CONFLICTS.md` | a resolver, a curator, a person, `drop` | the line* | `why:`, `by:` |
| **origin** | `<origin>/ORIGIN.md` | `absorb` | what it is, from where, when* | `trust: preferences` |

- **A note** is whatever was written, kept as written. It should be readable alone: what it is about, when, where
  its numbers come from. `check` says when a note has no `# ` line or no date of its own; nothing is refused.
- **`source:`** names what a note was made from, by exact path: a note of the base, or a file outside it. A note
  with a source has no standing of its own (§6). `from:` keeps its meaning: built on, and it stands by itself.
- **A definition** is not a record of its own. It is the note named after the entity, and `ask` heads it when a
  question names the entity.
- **A tag** is a word of `TAGS.md`, whose line carries the tag's definition and other spellings. A word that is not
  listed is kept on the note and reported, and is not a tag until someone adds its line.
- **An edge** is directed: `s` → `o`, read "s <type> o". A word listed with `~` under a type is that type read the
  other way. (`graph.json` stores edges as `relations` and uses the word `edges` for lineage between notes; schema 2
  does not rename them. The README calls an entity a thing and an edge a link.)
- **`walk:`** on an `EDGES.md` line lists the question words that make `ask` follow that type, `~word` for the
  inward direction. A registry without the field takes the seed's, so a base made before schema 2 answers as before.
- **A decision line**: `- a = b | why: … | by: …` · `not: a / b | why: …` · `not: <area>/a / <area>/a` for one name
  that is two entities · `- x > y` (x replaced y) · `compatible: x / y` · `dropped: <path> (date) > <what it had
  replaced>`. A line without `by:` is a person's and wins.
- **A pointer** is found by the script in the note's text when its path is a file of the project. Its anchor, the
  text it pointed at when first seen, is kept beside the reading (`_dream/notes/<hash>.pointers.json`).

## 4. What is checked, exactly

| record | kept when | not checked |
|---|---|---|
| a mention of an entity | one of its `as` words occurs in the note | that the words mean that entity |
| an edge | its quote occurs in the note, and both ends are entities named in the note | that the quote states the edge |
| a claim of a decomposing writer | its quote is in its section; every number of the claim is in the quote or the heading; it adds no negation; the quote covers half of its words | that nothing was left out |
| a pointer | its symbol, or its quoted words, are found in the file | – |
| a tag | `TAGS.md` lists it | that it fits the note |

A quote is found exactly, spaces and case aside. There is no fuzzy step. What is refused is written to
`_dream/refused.jsonl` with its reason, and counted by `check`.

## 5. The sockets

| socket | how | today |
|---|---|---|
| notes in | write `.md` files under an area; `absorb` for a folder | yes |
| readings in, by command | `MEMORY_LLM`: a packet on stdin, JSON on stdout | yes, one note a call |
| readings in, by files | `dream --packets` writes `_dream/pending/packet-<n>.md`: the instructions and vocabulary once, then notes up to the budget (60K tokens at three characters a token); the answer is `packet-<n>.json`, a reading per note hash | one note a file |
| readings in, with their notes | reading files that arrive with an absorbed base | new |
| decisions in | lines in the meaning files | yes |
| graph out | `_dream/graph.json`, `_dream/index.db`, a store, `export` | yes |

A reading that came with a note is used, and that note is not sent to a keeper unless asked for by name.

## 6. Dropping

1. Only `memory.py drop <note | folder>` drops. It prints what goes with the note and stops, unless given `--yes`.
2. It deletes the file and its reading and appends the tombstone line of §3.
3. The build reads a tombstone as a pass-through: who replaced the dropped note now replaces what it had replaced.
4. A note whose every `source:` is dropped is dropped with it. A note built on it stays, shown as built on a
   dropped note (`C14`).
5. A file that is gone without a drop is reported (`C15`) and nothing is written or deleted.
6. `ask` never fails on a note that is gone, on a small memory, a big one or a store.

Built in phase M, inside schema 1, and written into `CONTRACT.md` (§1 `dropped`, §4 `gone`, §5, §6). Two things came
out other than drafted here. The marks are not fields of a note: they are in the graph's `dropped` list
(`built_on_by`, `left_newest`) and in the manifest, so no store had to change. And a note whose replacement was
dropped with nothing after it becomes the newest left of its line, also `C14`.

## 7. Origins

1. A folder with an `ORIGIN.md` is an origin. Its next folder level is the area; kinds by area and the areas that
   span projects match on the last part of the name. A question is scoped to an origin only by `-p` or a full area
   name, never by a word that happens to be the folder's name.
2. A note's lineage target is looked for in its own folder, then in its origin, then in the host, and never guessed
   across origins.
3. An origin's entities are not joined with the host's by name. They are joined by a decision line. A host entity's
   home is a host note.
4. Its preference and rule notes keep their kind. They are served to a task and put in the digest only with
   `trust: preferences`, and a `me-` note never is.
5. Its `ALIASES.md` and `CONFLICTS.md` are read for its own notes. Its registry lines are offered to the host's as
   proposals.
6. `memory.py absorb <folder> --as <origin>`: without `--yes` it prints the notes it would take, every file it would
   not, the names both sides use with a line from each, and the words the registries do not know. Absorbing again
   replaces the folder.

Built in phase N, inside schema 1, and written into `CONTRACT.md` §7. Three things differ from this draft. An
origin's notes are in no digest, with or without `trust: preferences`. Its registry lines are not offered anywhere:
the report names the words the host's registries do not know, and a person adds a line. And one rule is new: `ask`
ranks the host's notes as if the origin were not there and lists the origin's after them, so that absorbing a base
changes no answer the host gave before.

## 8. Pointers

`path#symbol` · `path:line "quoted words"` · `path:line` (taken, and reported as weak). States: intact · moved (the
new line is printed) · changed · gone. A note with a changed or gone pointer is shown as stale (`C16`).

## 9. The graph

`schema: 2`. Added: on a note `tags`, `source`, `origin`, `pointers` `[{to, line, state}]`; at the top `dropped`
`[{path, date, replaced, built_on_by, left_newest}]` (already there in schema 1 since phase M). `project` stays the first folder for a host note and becomes
`<origin>/<area>` under an origin. New warnings: `C14`, `C15`, `C16`.

## 10. Words of one field that stay in the code

Schema 2 moves the walk's words and the "a file is not an entity" rule onto registry lines. These stay, and a base
in another field should know them: the question words for intent and the artefact words that mark a task
(`INTENT`, `SYN`, `ART`), the stop words of the conflict proposer, the kinds preferred for a headline (finding,
decision), the kinds the digest leads with (decision, model), the `…-vN is a model` rule as a fallback, and the
viewer's fixed lists of general areas and colours.

## 11. Left out on purpose

A verdict per mention; contract versions, anchors and excludes; a ledger beside git; findings as records; a base
read in place without copying; properties on entities; confidence scores; any matching by similarity.
