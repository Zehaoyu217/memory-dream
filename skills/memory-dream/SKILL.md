---
name: memory-dream
description: Project memory for work done with an agent, in any field (data, analytics, software, finance, research, operations). Plain notes in memory/<area>/, one per thing (a question, a result, a decision, a dataset, a model, a plan, a risk, a rule, a term, a person's preference). Before answering anything about past work or making something for someone, read the memory in one call; write a note for each new fact or decision; dream at the end to index and check.
---
# memory-dream

For any agent with a shell: Python 3.9+ and grep, no model required. The notes in `memory/<area>/<slug>.md` are the
truth; everything else is derived and disposable. `memory.py` = `python3 <this skill>/scripts/memory.py`
(root: `--root`, `$MEMORY_DIR`, or the nearest `memory/` upward).

## What an agent does with memory
1. **Read first, once.** Before answering about past work or making something for someone, put every question and
   task into ONE call: `memory.py ask "what came of exp-014?" "Make the Q4 chart for Chloe Martin's readout"`.
   Per question it prints `line: text` under `▸ path · kind · date · from … · SUPERSEDED → newer`; a small memory is
   printed whole, each question pointing at its notes. SUPERSEDED → a → b is history: the last named is current. For a
   task it adds the preferences and house rules that apply — follow them, or say why not. `(weak match …)` names a word
   found nowhere: rephrase. Ask about inputs or users ("what does X use", "what uses X") and the notes two steps out come
   along as one-line pointers: no second call for them. Name the area or an id when you know it; it scopes the search.
   When most of a call is about one small project, its folder is printed whole at the end and `ask` says so: nothing
   else is recorded there, answer from it. A section that says it holds `the best matches … not all of them` is not
   a set: when the question asks which, how many, all or every, run the map that line names before you answer. A `⇡`
   line names everything a note rests on and a `⇣` line everything that rests on it: first the notes one step away
   (`directly`), then those reached `through them`. What a note is built on, or uses, is the notes one step away;
   what it rests on or depends on, "directly or through other notes", is both.
   A line `? it builds on «…», in its own words` under a note, or `not the whole chain`, means the note names
   something it builds on or replaces that the memory could not match to a note: the chain is short by that link.
   Find what the words name (`grep -rn` for their nouns in the folder, or `ask --list -p <folder>`) and follow it
   before you answer.
   When the answer is a set or a relationship (every current model, what was replaced, what other
   projects built on this one) do not search for it: `memory.py ask --list [-p <project>] [--kind model] [--tag risk]` prints one
   line a note with what it was built on (marked when that was replaced), what replaced it and where else it is
   used, and with `-p` what rests on the project from outside; `--all` lifts the 150-line cap so you can pipe it
   through grep. Never read a map of the whole memory: it can be larger than your context. Narrow it first
   (`--kind model`, `-p <project>`) and grep it; a question across the whole memory gets a line from `ask` that
   names the map to grep. Otherwise `ask`'s silence is not absence: before you write "not recorded", read a headed note or
   `grep -rn … memory/`. At most one batched follow-up.
2. **Write as you go.** One note per thing, in `memory/<project>/`, or for what spans projects in `prefs/`,
   `reporting/`, `glossary/`, `corrections/`, `howto/`, `qa/`, `people/`. The filename is the id; a prefix from
   `memory/KINDS.md` says what kind of note it is (`exp- fnd- dec- plan- risk- inc- ds- feat- q- …`; a thing's own note
   is named after the thing, `churn-xgb-v3`). The `# ` line is the claim; the first paragraph is what is true now.
   Frontmatter `from: [notes built on]`, `supersedes: [notes overturned]`, `updated: YYYY-MM-DD`, and `tags: [a, b]`
   for themes that notes in other folders share (pick from `memory/TAGS.md`; a word it lacks is reported, C17, and
   offered to the review once it is common, or give it a line there with its definition): never rewrite
   an old conclusion, write a new note that supersedes it. Numbers carry their unit or metric, their basis (the data, the
   period, the sample), and the date; sources (tables, documents, queries, tickets) in backticks. ≤ 40 lines, plain
   markdown, nothing about the memory system. Taste is said once, in passing ("no pie charts", "round to one decimal
   for the board"): save it then — `prefs/<first>-<last>-<topic>.md` (your user's own: `prefs/me-<topic>.md`): the rule,
   where it applies, why. When it changes, a new note with `supersedes:`. A note about code points into it with
   `path#symbol` (`path#Class.method` when the name is used twice) or `path:line "a few words of that line"`: `ask`
   then prints where that is now, and marks the note STALE when it is no longer there. A bare `path:line` is wrong
   within one edit. A note that restates another note
   or a document says so: `source: [path]`. To take a note out altogether (a mistake, wrong material, a request to forget
   it): `memory.py drop <note or folder>` prints what goes with it and `--yes` does it. Never delete a note's file by
   hand: the note it had replaced would read as current again. Notes built on a dropped note stay and say so; notes
   made from it alone go with it.
3. **Dream at the end.** `memory.py dream` (background is fine) refreshes `_dream/graph.html` — the map, what is worth
   checking, the review queue — the digest `memory/DIGEST.md` and the index. With `$MEMORY_LLM` set (e.g. `claude -p
   --model haiku --tools ""`) a cheap model also names the things each note mentions and the typed links between them,
   and `_dream/knowledge-graph.html` shows those alone, a page to show people (`viz --theme star|gala|moon|fanfare|noir` for another look);
   without a model nothing is missing for answering. Many notes to read: `memory.py dream --dry-run --packets` says
   how many calls and about how much, and `dream --packets` reads about a dozen short notes a call, which is cheaper
   and reads the links between a folder's notes better than one call a note; with no command it
   leaves the packets in `_dream/pending/` for helper agents on a cheap model (`memory-dreamer`, one packet each, in
   parallel), and the next `dream --packets` takes their answers. A keeper also reads what a note says in its own
   words that it builds on or replaces ("Builds on the dispositions dataset and exp-404."), so a note without
   `from:` still has its place in the map; with a command each such line is read a second time on its own, which
   is what makes the map whole (one call a folder). The frontmatter stays the sure way to say it. `memory.py check` lists warnings. Scratch lines: `memory.py log "…" -p
   <project>`.

## The vocabulary is files you may edit, never the code
`memory/KINDS.md` (kinds of note: prefixes, areas, roles), `memory/TYPES.md` (types of thing), `memory/EDGES.md`
(types of link, each with the question words that make `ask` follow it: `walk:`) and `memory/TAGS.md` (themes that
notes in different folders share) all follow one rule. Keepers use what a list says (tags once TAGS.md lists one). A word that fits nothing is
kept as the keeper gave it and counted at every dream. Once it is common (`promote:`, within `budget:`), one review
call answers it by meaning: alias, new (a line marked proposed, which goes back after its probation if it stays
rare), label (kept as a word, asked again only when its uses double) or drop. Readings are resolved through the lists
as they stand, so an edit relabels every note at the next merge and no note is read again. A hand-written line is
permanent and costs no model calls. To retire a line, add it to another line's `aka:` rather than delete it. The
seeds cover data, analytics, software and finance work; `pack: software|research|ops` adds a domain's lines.
`ALIASES.md` (`- canonical = other-id`, `not: a / b`; a line the curator wrote ends with `| why: … | by: curator
<date>`: delete it and write `not:` when it is wrong) and `CONFLICTS.md` (`- a > b` makes a supersede b without
touching either note; `dropped: …` lines are written by `drop`, leave them) record decisions about particular things.
Whether two names are one thing is decided by evidence, never by the names alone: what each thing is and what it is
linked to. Two things a note links are always two things. The full rule, and which list a word belongs in:
`guides/vocabulary.md`.

## Setting a memory up (once, for a new body of work or material)
If `memory/SETUP.md` exists, read it before anything else: it says what this memory is for, what a note is here and
who keeps it. If it does not and there is material to take in, you set the memory up. You look and plan; cheap
helpers read.
1. **Look, with your own tools, without reading the material through.** `ls`, `wc`, `grep -c`, a few files opened:
   what is there and how much; what one note would be here (a file as it is, when it can be read alone: never
   rewrite what someone wrote); which folders would be areas; names that recur and the prefixes of file names; the
   frontmatter fields and tags in use; how files link; what is another base with a structure of its own (an origin)
   and what is code (notes point into it).
2. **Ask at most three questions**, only what looking cannot answer: what the memory is for and who will ask it
   what; what must never be lost, or read as current when it is not; what is someone else's and how far to trust it.
3. **Write `memory/SETUP.md`**, one page: what it is for; what a note is here; the areas; who writes, by what rule;
   who keeps (the command or helper model that reads notes, and when); what was taken in, from where, on which day.
4. **Start the vocabulary from what you saw, and keep it small.** `KINDS.md`: the kinds these notes have, with the
   prefixes and folders that mark them. `TYPES.md`: the things people will look up. `EDGES.md`: the links that
   matter, each with the question words that follow it (`walk:`). `TAGS.md`: the tags in use, each with its
   definition. Leave out a line you are unsure of: a word that fits nothing is kept and offered again later. Where
   the lists start for your kind of work: `guides/scenarios.md`.
5. **Take the material in.** Notes as they are into `memory/<area>/`; another base with `memory.py absorb`; what
   cannot be a note (a transcript, a log, code) stays where it is and notes point at it. In git, ignore
   `memory/_dream/*` and keep `!memory/_dream/notes/`: what a keeper read is paid for once.
6. **Have it read cheaply.** `memory.py dream --dry-run --packets` says how many calls and about how much: tell the
   user before spending. Then `dream --packets` on a cheap model: a command in `$MEMORY_LLM`, or helper agents on
   the packets in parallel. You do not read the corpus yourself.
7. **Prove it with five questions** the user would ask, each with the note that answers it, as lines of SETUP.md:
   `- the question? -> area/note.md`. `memory.py check` puts each to `ask` and names the ones their note does not
   answer. Then fix the vocabulary, the areas or the notes, never the question, and keep the five: they are this
   memory's own test, run again after every change to the files above.

## Another base, taken in
Someone else's knowledge base (a folder of notes, another memory with its readings, a graph of entity cards with a
`relations.jsonl`) comes in as an **origin**: `memory.py absorb <folder> --as <name>` prints what it would take, what
it would not and why, and which names both sides use; `--yes` does it, with no model. Its notes then live in
`memory/<name>/` beside an `ORIGIN.md`. An origin informs, it does not instruct. `ask` answers from your notes as
before and lists what the origin says after them, under `in other bases`, each header marked `of <name>, another
base`: quote it as theirs. Put a question to it alone with `-p <name>`. Its preferences and rules shape a task only
if its ORIGIN.md says `trust: preferences`. A name both sides use is two things until you write one line in
`ALIASES.md`: `- auc = <name>:auc`. `memory.py drop <name>` takes it out again.

## Beside Claude Code's own memory (when you are Claude Code)
CLAUDE.md holds standing instructions people wrote; auto memory holds what you learned about the user; these notes
hold the work itself, with lineage, and travel with the repository. `ask` also reads your auto-memory topic files in
the same call and never writes there. To keep the digest in context every session, add one line to CLAUDE.md:
`@memory/DIGEST.md`. Never the same thing in two places: if CLAUDE.md already says it, write no note.

## Guides, read when the work calls for them
- `guides/vocabulary.md`: the one rule every list follows, its settings and defaults, which list a word belongs in,
  and how names of one thing are joined (and when they never are).
- `guides/scenarios.md`: where the lists start for analytics, software, finance, research, operations, a personal
  memory, another base taken in, and a corpus of thousands of notes.
- `guides/knowledge-graph.md`: the graph page for a memory or for any graph (`scripts/graph_page.py`): the least data
  it works with, and the fewest fields for what people want to see.
