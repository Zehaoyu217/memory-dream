# Vocabulary: one rule for every list

Read this when you set a memory up, edit one of its lists, or need to know why a word was offered, kept or refused.

Six files at the root of `memory/` hold what the notes may be called. Four are vocabularies, run by one rule; two
record decisions about particular things. All six are yours to edit, and editing them costs no model calls.

| file | holds | a line | a keeper's own word, when nothing fits |
|---|---|---|---|
| `KINDS.md` | kinds of note: a decision, a finding, a dataset's card | `- kind: what it is \| prefix: \| area: \| family: \| role: \| aka:` | `other: <word>`: the note counts as `note`, the word is kept |
| `TYPES.md` | types of thing: a model, a dataset, a person | `- type: what it is \| aka: \| family: \| not:` | kept as `other/<word>` |
| `EDGES.md` | types of link, read "X <type> Y" | `- type: what it means \| aka: a, ~b \| walk: \| hops: \| shape:` | kept as `other/<label>` |
| `TAGS.md` | themes that notes in different folders share | `- tag: what it means \| aka: \| family:` | `other: <word>`, kept as a word |
| `ALIASES.md` | which names are one thing | `- a = b \| why: … \| by: …` and `not: a / b` | |
| `CONFLICTS.md` | which of two live notes is current | `- a > b`, `compatible: a / b`, `- a ? b` | |

## The rule
1. **Constrained open.** A keeper (the cheap model that reads notes) is shown every list in its prompt and uses it.
   What fits nothing is never forced onto a line and never lost: the keeper's own word stays in its reading.
2. **Counted, for nothing.** Every merge (each `dream`, no model) counts each word outside a list: its uses, the
   notes and the areas they are in, and three examples.
3. **The bar and the budget.** A word is offered once it is over `promote:` and its list has room under `budget:`.
   A full list offers nothing and says so (C7).
4. **One review for every list.** One call answers each offered word by what it means and how the examples use it,
   never by how it is spelled: `alias X` (another word for X), `new: <what it means, and how it differs from the
   closest line>`, `label` (keep it a plain word) or `drop` (not a word of this list).
5. **Code admits the answer.** alias: the word joins X's `aka:`. new: a line marked `(proposed <date>)`, if the
   budget has room. label: `keep: word ×uses (date)`, and the word is not offered again until its uses double.
   drop: the word goes on the `drop:` line. An answer about a word that was not offered is ignored.
6. **Applied at every merge, read once.** A reading is kept as the keeper gave it and resolved through the lists
   as they stand at each merge: a new alias or line relabels every note at once, and no note is read again.
7. **The next reading sees it.** Each keeper's prompt is built from the files at the start of a run.
8. **Probation.** A `(proposed …)` line still under the bar after `probation:` days goes back to being a word (0
   calls). Take the mark off to keep a line for good.
9. **A person's line is permanent.** Write, merge or retire lines by hand; the next merge applies them. To retire
   a line, add it to another line's `aka:` rather than delete it, so nothing already read is lost.

Every list takes the same settings: `promote: U uses, N notes, A areas`, `budget: N`, `probation: D days`,
`pack: name` (a domain's seed lines), `drop: a, b`, and the `keep:` line that the review writes.

| list | promote | budget | probation | seeded with |
|---|---|---|---|---|
| KINDS | 5 uses, 5 notes, 2 areas | 40 | 60 days | 23 kinds; `pack: research, ops` |
| TYPES | 5 uses, 5 notes, 2 areas | 40 | 60 days | 27 types; `pack: research, ops` |
| EDGES | 5 uses, 5 notes, 2 areas | 24 | 60 days | 8 types; `pack: software, research, ops` |
| TAGS | 3 uses, 3 notes, 1 area | 30 | 60 days | none: a tag belongs to one base |

A tag's bar is lower because a theme is shared by fewer notes, and it may live in one area.

## Which list a word belongs in
- What a note **is** goes in KINDS. Keep kinds few, a dozen to two dozen: a kind decides what heads the digest, what
  is compared for disagreement, and what answers a question.
- What a **thing** is goes in TYPES: the things people will look up by name.
- How two things **relate** goes in EDGES, with the question words that follow the link (`walk:`). A link nobody
  will ask along stays a label.
- What notes **are about** across folders goes in TAGS: a regulation, a risk theme, a recurring process. A tag never
  repeats what the folder (the project), the kind (a decision) or the things (a model's name) already say.
- None of these: a project or area is a folder; a status or a date is frontmatter (`updated:`, `supersedes:`); a
  person is a thing of type `person`, and their taste is a note in `prefs/`; a number, a file or a date is never a
  thing (`drop:`).

Use as few as serve. Start from what you saw (SKILL.md, setting up, step 4) and leave out any line you are unsure of:
the loop adds what proves common, and a proposed line nobody uses goes back after its probation.

## Who is the same: identity by evidence
Names of things are joined in five ways: the same id once folded (case, spaces, `_`, `.` and `-` do not count), the
surface rule (an id that exactly one other thing writes as one of its names), the curator (one call per folder whose
things changed: which of them are one thing under two names), the review (pairs that some note writes in the same
words), and a person (a line of ALIASES.md).

The curator and the review read the same card for each thing: its type, how the notes write it, how many notes name
it, what its own note says it is, what the notes link it to, and a line that mentions it. A pair also shows what the
two are both linked to. One thing under two names is the same kind of thing, described alike and linked to the same
things by the same relations. A shared word in two names is not evidence.

The script holds these, whatever an answer says:
- two versions (v2, v3) are two things;
- `not: a / b` stands until a person removes it;
- two things that each have a note of their own are two things;
- a folder's curator joins only names that are used in that folder alone;
- two things a note links to each other are two things: no rule joins them, the curator's or the review's join is
  refused, and a person's join is reported (C19).

To undo a wrong join, delete its line in ALIASES.md and write `not: a / b`. The same goes for words in a list:
whether `fit-on` means `trained-on` is the review's `alias` answer, decided from the definitions and the examples.

## What to watch
`memory.py check` lists the warnings. C7: a list is full (raise its budget or merge lines). C12: a link does not fit
its type's shape. C13: a type was removed by hand, and its things keep the word. C17: a tag written in notes that
TAGS.md does not list; it is counted and offered like any other word. C19: a line of ALIASES.md joins two names that
a note links. `dream --review` asks the review now. Without a model command its prompt waits in
`_dream/pending/review.prompt.md`, and the answer (`review.json` beside it) is taken at the next dream.
