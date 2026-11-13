# memory-dream v0.5 — the plan, third draft: the script does exact work, cheap agents read, one contract

2026-11-11 · rev 3. The first draft (commit e78eb8f) was grilled against the owner's ten points and against the
code that ships (rev 2). The owner then added six points, an independent reviewer attacked rev 2 with twenty
experiments, and four more measurements were made. This draft is what survived.

**Status, the same day.** The owner took every recommendation of §15 and asked first why the memory was graded
below grep. That question was answered before anything else was built (RESULTS phase L), and it built most of §11:
items 2, 4 and 5 are in `ask`, item 1 in the case that was measured. §11 and §14 carry what the measurements
changed. Step 0 is built (RESULTS phase M): `memory.py drop`, the tombstone, and an `ask` that survives a missing
file; §8 says where the build went past the draft. Of step 1, item 1 is built (RESULTS phase N): origins and
`memory.py absorb`; §9 says what it added to the draft. Item 3 is built (RESULTS phase O): pointers into code; §10
says what a probe on this repository's history changed. Item 4 is built (RESULTS phase P): packets and the dry
run; §4 says which limit of a packet binds. Item 5 is built (RESULTS phase Q): tags through `TAGS.md`, and the
walk's words on the lines of `EDGES.md`. Item 6 is built (RESULTS phase R): the skill's section on setting a
memory up, and a memory's own proof questions in `SETUP.md` that `check` asks again. Item 7 is built too: the
page's filters. Step 1 is done.

**Step 2, 2026-11-12** (RESULTS phase S). Built and measured: packets on Haiku 5.5, a bank grep cannot read exactly
(the worn bank), lineage read from prose, identity by reading (the curator), the arms run headless. The answer to
point 14 on that bank is in S6: the memory was the less accurate arm with either reader because an agent answers
from what the memory holds and the keeper had read 94% of the links; with every line that states lineage read a
second time on its own it holds 99.5%, and Haiku with the memory answers 96% of the questions exactly at
$0.017 a ten questions, where Haiku with grep answers 90% at $0.080 and Opus with grep 99% at $0.70. Not built:
the decomposing writer (item 11).

**The base too large to read whole, the same day** (RESULTS S7), with every arm's context held to 100,000 tokens
as the owner asked: the project folders poured into one of 1,224 notes. A keeper cannot be shown such a folder, so
the second reading shows it the notes near the lines it reads; the memory holds 99.2% of the links. Opus with grep
99%, Opus with the memory 97% (99% by the second count) at 0.57 of the price, Haiku with the memory 89% (92%) at a
46th, Haiku with grep 65%, or 80% at five questions a session. Not shown: a base whose notes seldom name each
other; identity in a folder that large.

The contract field by field is `CONTRACT-2.md`. Every number has a command, all without a model:
`python3 eval/contract_probe.py <bank-index world>` (drop, absorb, documents, sets), `python3 eval/agent/arms.py`
(the five arms), `python3 eval/pointer_probe.py [--built]`, `python3 eval/decompose_probe.py score …`. RESULTS phase K
has them.

## 1. What is asked

The owner, 2026-11-11, first message:

1. A contract open enough, and blocks separate enough, for plug-ins later.
2. Notes, entities, edges, tags, definitions: some mandatory, some optional.
3. Absorb the output of other knowledge bases in general.
4. Several uses: memory, a project, tracking, a knowledge graph, lineage.
5. Very simple. Easy to see how it works.
6. A skill an agent operates. It does the detective work on the materials and sets up writers, keepers and the
   starting vocabulary.
7. Drop a note and what came from it is dropped too.
8. Retrieval easier, faster, cheaper, simpler: the point of it all.
9. A page to look at, with search that needs no agent.
10. No over-engineering, few tests. The end-to-end result and the performance are what count.

Added the same day:

11. The reading uses the method of the owner's claims base, and caching.
12. Mostly Haiku 5.5, tuned to the 100K-token line below which it is cheapest. The agent that plans and investigates
    may be Opus; the heavy work is parallel and goes to Haiku.
13. Some memory of a codebase too: pointers.
14. The bar: much cheaper and faster than an Opus agent with grep and glob, at similar answer quality.
15. A note is whatever an agent wrote. The requirement on it is light: complete enough to be read alone. What agents
    write (notes, comments, handoffs) decomposes into notes.
16. Entities and edges are deduplicated, edges have a direction, entities have definitions, a definition can be part
    of a tag. Fuzzy matching is the wrong tool: dedup and merging are done by agents.

## 2. What the measurements say

### The bar of point 14, measured for the first time

The agent eval of phase G had Opus on both arms. On 2026-11-11 the same thirty questions were given to Haiku 5.5
agents with the same prompts, and every answer, the Opus ones included, was graded twice by the same judge.

| arm | correct / partial / wrong of 30 (two passes) | tool calls | tokens | $ per ten questions | seconds |
|---|---|---|---|---|---|
| Opus + grep (the bar) | 29/1/0 and 29/1/0 | 18.7 | 1,742k | 1.546 | 273 |
| Opus + memory | 22/7/1 and 24/6/0 | 5.7 | 498k | 1.068 | 204 |
| Haiku + grep | 25/5/0 and 26/4/0 | 8.7 | 485k | 0.0167 | 42 |
| Haiku + memory | 23/5/2 and 23/6/1 | 5.3 | 293k | 0.0129 | 34 |
| Haiku + memory, notes printed whole | 23/6/1 and 23/6/1 | 6.3 | 334k | 0.0140 | 38 |

What it says:

- **The model is the lever.** Haiku is 92 to 120 times cheaper and 6 to 8 times faster than Opus with grep. On one
  model the memory moves the cost by 0.7 to 0.8. "Much cheaper and faster" is met by point 12 alone.
- **The memory does not yet give "similar quality"; today it costs some.** On both models the grep arm answers
  better than the memory arm, and only memory arms give a wrong answer. Printing the notes whole changes nothing
  (23 correct either way), so the cause is not the length of the excerpts.
- **Why.** The agent answers from what `ask` prints and takes its silence for absence. Three cases, each on these
  thirty questions: the thing's own note is not headed (why recall@10 is the metric: wrong in all three memory arms,
  right in both grep arms; `ask` heads twelve notes that use the word and not the note that defines it); one name
  stands for two things (`holdout-2025q4` is 1.2M accounts in one project and 412,600 rows in a how-to: marked down
  in three arms, hedged in a fourth); the inputs of a thing come back incomplete (`sfc-hier-v3`: partial in four
  arms, and only Opus with grep named all four inputs).
- **The instrument is too coarse.** The judge changed 14 of 150 verdicts between its two passes, and graded the same
  Opus answers 23/7/0 on both arms ten days ago. Thirty questions and one judge cannot settle "similar" to better
  than three answers.

So the base has one job in v0.5: make a cheap reader as complete as an expensive one that explores. The own note
first, the whole list of inputs, one thing per name. That is what definitions, edges and dedup are for, and these
thirty questions already measure it.

### What else was measured

| asked | measured on v0.4 | this draft |
|---|---|---|
| 1 plug-ins | a graph another model wrote came in through the file socket in 0.4 s with no call. But a model command ignores that socket and would read the notes again | files in, files out; a reading that came with a note is used (§6) |
| 2 mandatory, optional | with no model and no index `ask` heads 0.939 of the gold notes, with them 0.941 | one record must exist, the note (§5) |
| 3 absorb | a copied-in memory keeps its lineage (42 of 42) and loses its areas (3 → 1) and 3 kinds; the absorbed cards became the home of 2 host things; 21 of the host's 326 gate answers change, 17 now head an absorbed note; `README.md`, `INDEX.md` and `.txt` files are skipped without a word; absorb and drop gives back the same graph | an origin is data, apart until judged (§9) |
| 4 several uses | the walk and several rules name one field's words in the code | they move to registry lines, the seed as fallback (§11) |
| 7 drop | derived records go (8 of 8 links, 1 of 1 thing). The supersession chain is cut and the replaced note shows as current (23 notes sit mid-chain). On a big memory `ask` crashes until the next dream | `drop` is a command that leaves a tombstone (§8) |
| 8 retrieval | asked for every note of a kind in a project, `ask` names 0.47 of the set; one call of ten questions takes 0.5 s | filters, the own note first, complete inputs (§11) |
| 13 pointers | a `file:line` pointer is right for 41% of definitions one version later and for none after five; its quoted text is found for 97% and 96%; its symbol for 100% and 100%, and for 70% after 29 versions | pointers by symbol or quote, checked free (§10) |
| 15 decomposing | Haiku 5.5 turned a 14,220-character handoff into 95 claims in one call: 87 kept by the gates, no invented quote, no wrong number, about $0.0055. The claim notes then answered 5 of 8 probe questions for 1,882 characters each; the untouched document answered 5 of 8 for 616. Two probed facts were never extracted; a gate refused a true one | a document is a note as it is; decomposing is a writer for what cannot be a note (§5) |
| 16 dedup | 3,216 names become 2,972, and 203 of those merges are made by a rule on surface forms that nobody judges; the name-alike proposer offered 87 pairs and 14 were the same thing; a free tagger gave 87 different tags to 87 notes | identity by reading; tags from a vocabulary (§7) |

## 3. How it works

A reader should be able to retell this section.

- **Notes** are text files that agents and people wrote. They are the truth and nothing rewrites them.
- **`ask`** answers a question by grep over the notes. A small graph then orders what grep found and adds what grep
  cannot see: which note replaced which, other names for the same thing, a thing's own note, what a thing is built
  from. One call takes every question; no model runs.
- **Keepers** are cheap agents that read each note once and return its **reading**: the entities it names and the
  edges it states between them, each with the words of the note it rests on. A reading is stored under the hash of
  the text it read, so nothing unchanged is read twice.
- **Registries** are small text files that say what the words mean: kinds of note, types of entity, types of edge,
  tags. `ALIASES.md` says which names are one entity; `CONFLICTS.md` says which note replaced which when the notes
  do not say it themselves.
- **`dream`** rebuilds the graph from notes, readings and those files. It calls no model and takes a second.

```
 what agents wrote ─▶ NOTES ──▶ keepers read, in packets ─▶ READINGS        truth     kept as written
                        │                                      │
                        │      KINDS · TYPES · EDGES · TAGS · ALIASES · CONFLICTS · SETUP    meaning   one line per decision
                        ▼                                      ▼
                    dream, no model ─▶ GRAPH ─▶ ask · the page · the digest · check          derived   rebuilt in a second
```

Four rules:

1. **A note is the only record that must exist.** A folder of notes is a base and `ask` answers from it.
2. **Every other record names the note it rests on** and is checked against that note's text.
3. **The graph is recomputed from the notes that exist now.** Nothing in it outlives a note.
4. **The script does only exact work; whatever needs judgement is read by an agent and written down as one line
   with its reason.** No threshold and no string distance decides anything.

Rule 4 is new and answers points 12 and 16 together. Hashing, finding a quote, counting, joining equal names,
checking a pointer and building the graph are exact and free. Whether two names are one thing, what a word means
here, whether a note replaces another: these are read by a cheap agent, and its answer is a line a person can edit.

## 4. Who does the work

| who | model | does | never |
|---|---|---|---|
| the main agent | whatever the session runs; Opus is fine | looks at the materials, asks the user, writes the setup and the starting vocabulary, runs the commands, spot-checks, answers | reads the corpus itself |
| keepers | Haiku 5.5 | read notes into readings | decide what a word means |
| resolvers and curators | Haiku 5.5 | say which names are one entity, map raw words onto terms, find notes that replace each other (§7) | merge anything without leaving a line |
| writers, when wanted | Haiku 5.5 | decompose material that cannot be a note into notes (§5) | touch a note that exists |
| the script | none | everything exact | judge |

How the heavy work is packed (points 11 and 12):

- **Packets.** `dream --packets` writes the work as files: the instructions and the vocabulary once, then as many
  notes as fit a budget. One worker answers one packet. Workers run in parallel (`-j`).
- **Under the line.** Haiku 5.5 costs $0.10 and $0.50 per million tokens while a prompt is at most 100K tokens, and
  five times that above. A packet is built to 60K tokens by the script's count of three characters a token, because
  the tokenizer counts about 30% more than the older one and the answer needs room. No call may cross the line.
- **A lean call, not a tool-using agent.** A Haiku subagent of the harness carries about 35K tokens before any
  work: the runs here sent prompts of up to 88,671 tokens, and one decomposing a 14K-character file ended at 94K.
  The headless command with no tools and no settings carries about 1K (the claims base measured 33,648 against
  948). Packets go through the command; subagents answer packets only where no command can run.
- **Two caches.** The answer is stored under the hash of what was read, so a changed base re-reads only what
  changed. The prompt's first part is identical for every packet of a dream and sits where the model caches it: read
  again at a tenth of the price.
- **The reading method** is the claims base's: cut at headings; each record carries the exact words it rests on;
  the script, not the model, decides what is kept. Its fuzzy step is not taken over: a quote is found exactly,
  spaces and case aside, or the record is refused.
- **Before spending**, `dream --dry-run` prints the packets and the estimate.

What it costs today, at Haiku 5.5's prices: a reading is $0.0016 a note, one call each with 4.9K tokens in, about
4K of them the same instructions every time, and 350 to 1,750 out ($2.72 for the bank's 1,677 notes); decomposing
a handoff was $0.0055; ten answered questions $0.013. What packets save on the reading is measured in step 2.

Built in phase P, with one number changed by a measurement. A packet is not sized by its prompt alone. A reading is
3.2 times its note on the bank, so a 60,000-token prompt of short notes would ask for 135,000 tokens back: the
answer's room fills first. A packet closes at 12,000 characters of notes or 60,000 tokens of prompt, whichever
comes first, which is about 25 of the bank's notes and a prompt of 6,000 tokens. (Phase S, with a model: two dozen
notes a call read thinner, a dozen read as much as a single call and place more lineage at 0.6 of the price, so the
limit is 6,000 characters now.) By the dry run the bank is 67
packets in place of 1,677 calls, a tenth of the input, and $0.39 against $0.72 before what a command adds to each
call; the answers are nine tenths of what is left. A packet's answer is one line a note, so a cut-off answer loses
one note. The lean command existed already (`tests/haiku_cmd.py`, and the one-line `MEMORY_LLM` of the runbook).

## 5. The contract: what must exist and what may

| record | written by | must carry | may carry |
|---|---|---|---|
| **note** | an agent or a person | a text file under an area | a `# ` line, a date · `from`, `supersedes`, `type` · new: `source`, `tags` · pointers into files |
| **entity** | a keeper | an id and its words as found in the note | a type |
| **edge** | a keeper | two entities of the same note, a word for the link, the quote | – |
| **tag** | whoever writes the note | a word that `TAGS.md` defines | – |
| **definition** | a writer | it is a note: the one named after the entity | – |
| **pointer** | whoever writes the note | `path#symbol`, or `path:line` with a few quoted words | – |
| **term** | the setup, a curator, a person | a name and a definition | other names, a family, what it is not |
| **decision** | a resolver, a curator, a person | one line in `ALIASES.md` or `CONFLICTS.md` | its reason and who made it |

- **A note is whatever an agent wrote** (point 15): a note, a handoff, a design record, a session summary, as it was
  written. The requirement is that it can be read alone: it says what it is about, when, and where its numbers come
  from. There is no size rule for what is taken in; the keeper reads a long note in windows.
- **Decomposing is a writer, not a duty.** It is for material that cannot be a note: a transcript, a log, code. It
  is safe (no invented quote in 95 claims) and cheap, and its notes are made from their source, so they go when the
  source goes. But a source is either a note or material for notes, never both: on the probe the claim notes found
  no more answers than the document and cost three times the characters.
- **A definition is a note** (points 2 and 16): the note named after the entity. `ask` puts it first when a
  question names the entity. A **tag carries its own definition** in `TAGS.md`, and a writer picks from that list:
  left free, a tagger made 87 tags for 87 notes.
- **Edges have a direction** and it belongs to the type: `uses` reads one way, and a word listed with `~` is the
  same type read the other way.
- **Readings stay where they are**, one file per hash in `_dream/notes/`, and that folder goes into git; the rest
  of `_dream/` stays ignored. Rev 2's readings file beside the notes is out: it weighs 3.4 times the notes and puts
  them into every plain grep.

## 6. The blocks and their sockets

| block | does | ships as | replaced by |
|---|---|---|---|
| **write** | work and material → notes | the agent following the skill; `absorb`; the decomposing writer | anything that writes `.md` files |
| **keep** | notes → readings | Haiku on packets through `MEMORY_LLM`; helper agents on the same packets | any command; any program that leaves an answer file for a packet or a note |
| **name** | raw words → terms; names → entities; which note replaced which | resolvers and curators on packets of cards; the registries | editing the files; any program that writes decision lines |
| **build** | notes + readings + meaning → graph | `dream`, no model | nothing: it is the contract |
| **use** | graph + notes → answers, a page, warnings | `ask`, `graph.html`, `DIGEST.md`, `check`, the stores | anything that reads `graph.json`, `index.db` or a store |

No loader, nothing to register. One rule is missing today and is added: **a reading that came with a note is
used, and that note is not sent to the keeper again.** With a model command set, v0.4 ignores answer files and
would re-read an absorbed base.

## 7. Identity, dedup and merging: by reading

What v0.4 does, on the bank: 3,216 names as written become 2,972, and 203 of those merges are made by a rule on
surface forms that nobody judges. A proposer of name-alike pairs (string ratio 0.85, or a shared surface form) offered 87
pairs to the review; 14 were one thing and 73 were siblings such as `aml-oot-2026h1 / cli-oot-2026h1`. The review
decides each pair on one line of context. Equal names join across projects without a question, which is how
`holdout-2025q4` became one entity for two datasets. Conflicts between notes are proposed from shared title words:
5 of 73 were real.

v0.5:

1. **The script joins only equal names inside one area, and what a decision line says.** The surface rule and the
   string ratio neither decide nor propose.
2. **Candidates come from what the notes say, never from how names look**: one name used in several areas or
   origins; a note that gives one entity another's name ("X, also called Y"), which the keeper returns as an edge
   with its quote; two entities of one type with the same typed neighbours; and a curator's read of an area's
   cards, the only way to find two unlike names for one thing.
3. **A card** per entity, built by the script: its own note's first line if it has one, three lines that mention
   it, its type, its typed neighbours, the areas it appears in.
4. **The resolver** reads a packet of cards and answers, for each group: the same · different · one is a part or
   a version of the other · cannot tell. It quotes the card line that decided, and it may open the notes when the
   cards are not enough. That is the agentic part: it looks, as a person would. "Cannot tell" keeps them apart and
   is asked again only when new mentions arrive.
5. **A decision is one line** with its reason: `- a = b | why: … | by: resolver 2026-11-11`, `not: a / b | why: …`,
   and for one name that is two things, the name qualified by its area. A person's line wins. No verdict per
   mention, no versions, no anchors: the lines are the whole record.
6. **Edges** follow: after entities are resolved, edges with the same ends and type are one edge with all their
   evidence. A curator maps every raw link word onto a type or leaves it, not only the words over a bar.
7. **Notes that replace or repeat each other** are found the same way: a curator reads the live claims of one kind
   in one area as a packet, in place of shared title words.
8. **Merging two bases is this pass** over the names both use, plus a curator's read of both vocabularies. Nothing
   joins across origins without a line.

A card is about 120 tokens, so every entity of the bank is two packets and a few cents. A verdict per item was cut
from the first draft as too heavy; at a fortieth of the price per token it is the simple choice.

Built in phase S, in part. The string ratio is out of the script (item 1, second half): on the bank it had offered 46
pairs, 5 of them one thing. Items 3 to 5 are the curator: a folder's things on one page, each with its written forms
and a line that mentions it; an answer that names the ones that are one thing, with a reason; a line of `ALIASES.md`
signed `by: curator`. The cards are a folder's, not a packet of the whole base, because the first run showed what a
reader of one folder must not do: two projects call two models "the response model", and each folder's curator
joined the name to its own. The script now refuses a join of a name that other folders use, of a thing whose note
is elsewhere, and any line that would hold two things with notes. Note identity (item 2's "a note that gives one
entity another's name") is read by the keeper itself, which is given the folder's notes by file name. Still as in
v0.4: the rule that joins an id to the one thing that writes it as a spelling (item 1, first half), raw link words
mapped only over the bar (item 6), conflicts proposed from shared title words (item 7), and nothing qualifies a
name by its folder (item 5, last clause). The curator does not move retrieval on the bank: 0.811, 0.814 and 0.809
on the gate's 719 name questions with the old lines, with none and with its own.

## 8. Dropping

1. **Only `memory.py drop <note | folder>` drops.** It reads the note first, prints what will go with it, and does
   nothing more unless told `--yes`.
2. It deletes the file and its reading, and leaves one tombstone in `CONFLICTS.md`:
   `dropped: <path> (date) > <what it had replaced>`.
3. The build reads a tombstone as a pass-through in a chain. Where X replaced the dropped note and the dropped note
   had replaced Y, X now replaces Y: on a fresh clone, for two neighbours dropped together, with no old graph.
4. Notes made from it (`source:` naming it by its exact path, and no other source left) go with it. Notes built
   on it (`from:`) stay and are shown as built on a dropped note.
5. **A file that is merely gone is not a drop.** A rename with an edit, another branch, a `git pull`: `dream` says
   which notes are gone and names the command, and writes and deletes nothing. Rev 2 inferred the drop from the
   missing file; the review showed a branch switch would then delete notes.

Following `from:` instead would take a median of 2 notes, 18 at the ninetieth percentile and up to 54 across
three projects for one dropped note. That stays the owner's call (§15).

Built in phase M as written, with four things the draft had left open. A folder is one line, and one more for each
note in it that a note outside still names. When the dropped note was the newest of its line, the note it had
replaced becomes the newest left and says that its replacement was dropped. A file that is gone is remembered in the
manifest with where it stood, so `drop` can still record it after a dream has run. And `drop` rebuilds the graph
itself, with no model, so nothing reads a half-dropped memory.

## 9. Absorbing another base

1. **An origin is a folder with an `ORIGIN.md` in it**: what it is, where it came from, when, and what it is trusted
   for. Its next folder level is the area, so its areas and kinds survive.
2. **It is data.** Its notes answer questions and never instruct: its preference and rule notes keep their kind
   and stay out of a task's preferences and out of the digest unless `ORIGIN.md` says `trust: preferences`. A note
   of the form `me-…` never crosses.
3. **Its readings come with it and are used as they are** (§6).
4. **Its entities stay apart from the host's until a resolver or a person joins them** (§7), and a host entity
   keeps its own note as its home.
5. **Its words are read through the host's registries**; its own registries and its own decided lineage are read
   inside the origin. Today they are skipped and a copied base loses its decided supersessions.
6. **What is checked, exactly:** an entity is kept if its words are in the note; an edge if its quote is in the
   note and both ends are named in the note. The script does not check that the quote states the edge. Refused
   records are kept in a file with the reason.
7. **Input:** `.md` files with a `# ` line. `absorb` gives a missing one from the file name and lists every file it
   did not take. A graph with no text becomes one note per entity whose lines state its edges, and needs no reading.
8. Absorbing again replaces the folder. Dropping it is dropping the folder (§8).

Built in phase N, with one rule the draft did not have. "Apart" was written for identity and for trust. Measured on
the bank, an absorbed base also changed 19 of 326 answers the host gave from its own notes, by ranking among them.
So `ask` now ranks the host's notes as if the origin were not there and lists the origin's notes after them, in a
block of their own, when the origin names what the question names: 0 of 326 host answers change, and a question
across the two still gets both. Item 5 is built for `ALIASES.md` and `CONFLICTS.md`; the origin's registry lines
are reported as words the host does not know, not written anywhere. The graph input of item 7 is a
`relations.jsonl` with entity cards, as in `eval/absorb/policy-kb`.

"In general" is not shown: the one sample is hand-made, in a shape its own project has since withdrawn. Step 1 runs
one real export of another system before that word is used.

## 10. Memory of a codebase: pointers

- Agents already write `memory.py:2440` and `memory.py#grep_lines`. The script takes these as pointers when the
  path is a file of the project, records the text it points at, and checks every pointer at each dream, free:
  intact · moved, with its new line · changed · gone.
- `ask` prints the pointer and its state under the note, so the next step is one read of the right lines. A note
  whose pointer changed is marked stale. It is not dropped: what was learned may still hold.
- By the numbers of §2 the skill says: point with `path#symbol`, or with `path:line` and a few quoted words; a bare
  line number is wrong within one edit.
- This is not a code index. A parser can add symbols and calls as entities and edges through the keep socket. The
  rule that a file is never an entity moves from the code to the `drop:` line of `TYPES.md`, so a base about code
  can keep files.

Built in phase O as written, and then corrected by a measurement the draft did not ask for. The lookup was scored
on 34 versions of this repository's script (`eval/pointer_probe.py --built`): as first built it put 12 of 209
symbols on the line of a call or of a local variable and called them intact. A definition is now looked for form by
form, a call is no form, and quoted words are not found inside a longer word. After that no pointer of any form
names a wrong line at any distance: twenty versions later a symbol is found for 94% of definitions, quoted words for
85%, a bare line for 80%, and the rest say that they changed. The file rule is its own line, `drop-names:`, beside
`drop:`, because `drop:` lists types and this lists names.

## 11. Retrieval, for a cheap reader

Each item names the case of §2 it answers. None adds a model to `ask`.

Phase L found the rule the items share: an agent answers from what one call shows and takes its silence for
absence, and it makes one call. So a call is complete, or it says in the question's own section that it is not.
What is built is marked.

1. **The entity's own note first** when a question names the entity (recall@10). *Built for the measured case:*
   when most of a call points at one small folder, the folder is printed whole. Open where no folder wins the call.
2. **Inputs complete**: "what does X depend on" prints the whole list from the edges and the lineage, not the best
   eight (`sfc-hier-v3`). *Built:* the `⇡` and `⇣` lines, the notes one step away apart from those reached through
   them. Haiku still answers that question with the four notes one step away.
3. **One name, one thing** (§7), so an answer does not mix two datasets (`holdout-2025q4`). Open: step 2.
4. **Silence is not absence.** A weak answer says it is weak, and the skill tells the agent to grep before it writes
   "not recorded". Haiku wrote that twice where grep found the note. *Built:* a section says "printed whole:
   nothing else is recorded there" or "the best matches, not all of them", with the command that maps the folder.
   The second line is what got a set question answered that two runs had answered "none".
5. **Sets by filter**: `ask --list [-p folder] [--kind K]` prints one line per note, capped, with "N more". The
   agent turns "list every open risk" into filters; the skill says so. `ask` does not guess a list from the wording:
   the two gate questions that say "all" or "each" ask for a reason and a number, not a list. *Built* for folder
   and kind, and for `--tag` since phase Q.
6. **Walk words on registry lines**, with `~` for the inward direction; a registry without them takes the seed's,
   so existing bases answer as before. What stays in the code is listed in the contract, not denied. *Built:* the
   `walk:` and `hops:` fields of `EDGES.md`; 0 differences from the tables they replace on 433 questions.
7. **The page**: filters for tag, type and origin beside the search that exists. *Built:* words in the search box
   (`tag:`, `type:`, `origin:`, `kind:`) and a picker for each.
8. **A note's kind from its name and folder before the keeper's reading.** *Built.* The reading had relabelled 268
   of the bank's 1,677 notes, and a map by kind left models out. New for the setup of §4: check each kind prefix
   against the readings, since a project's own code can be one (`inc-`).

Two things the measurements changed. Characters are not the cost: a request carries about 35,000 tokens of harness
whatever a tool returns, so the price is the number of requests, and a call may print a quarter more to save one.
And the line to watch is the 100K prompt: the map of a whole kind is 38,000 characters, and one run with it reached
92,000 tokens.

## 12. What was cut, and what would bring it back

| cut | why | back when |
|---|---|---|
| the plug-in loader, nine interfaces, splitting `memory.py` | files are the interface | a block no file can reach |
| contracts, anchors, excludes, a verdict per mention and version | decision lines with reasons do the work (§7) | lines stop being enough on a real base |
| the ledger, levels of evidence, the doctor | git, `check`, and the reason on every line | a base outside git |
| findings as records, a queue, twelve analyzers | upkeep, not retrieval | a base asks |
| mounts, bundles, seeded alignment | a folder is the bundle; the resolver aligns | a base too large or too private to copy |
| rev 2's readings file beside the notes; its `survey` command; the keeper reading tags and definitions; guessing a list question from its wording | each failed the review or a measurement (§2, §5, §11) | – |
| the surface rule and the name-alike ratio | they decide by how names look (§7) | never |
| a fixture per claim, a gate per block | point 10 | – |

## 13. The order of work

**Step 0, two defects of v0.4, no model.** `ask` must not crash on a big memory or a store when a note is gone.
A dropped note must not bring back the note it replaced (`drop` and the tombstone, §8). *Done: RESULTS phase M.*

**Step 1, no model.**

1. Origins: `ORIGIN.md`, one function for a note's area, trust, readings that come along, the reports (§9).
   *Done: RESULTS phase N.*
2. Retrieval for a cheap reader: the own note first, complete inputs, filters with a cap, the weak marker (§11).
   Done in phase L but for the own note where no folder wins the call, and the tag filter.
3. Pointers (§10). *Done: RESULTS phase O.*
4. Packets: `dream --packets`, the budget, the lean command, `--dry-run` (§4). Readings in git.
   *Done: RESULTS phase P.* One call a note stays the default until step 2 measures a packet's yield.
5. Tags from frontmatter and `TAGS.md`; walk words on registry lines. *Done: RESULTS phase Q.*
6. The skill's setup section: look with your own tools, ask at most three questions, write `SETUP.md` and the
   starting vocabulary, take the materials in, prove it with five questions. *Done: RESULTS phase R.* The five
   questions are lines of `SETUP.md` and `memory.py check` asks them again.
7. The page's filters. *Done: RESULTS phase R.*
8. The end-to-end run (§14).

**Step 2, Haiku.** Under $5 without the Opus arms.

9. Read the bank again in packets on Haiku 5.5: cost and yield against the readings on file. Two loose ends of
   the handoff need this re-read and go with it: note kinds named as entity types (item 6) and the pool of calls
   fed continuously (item 7). *Done for a 300-note sample and for the worn bank: RESULTS phase S (S1, S3).* The two
   loose ends are still loose. *And the reading is now two readings (S6):* the packet, then every line that states
   lineage once more on its own, because the packet reading left out one in ten of the things such a line names by
   a phrase.
10. Cards, the resolver and the curator (§7); the alias gate is re-based on their decision lines, kept in the
    repository like the readings. *The curator is built and measured (RESULTS S4); §7 says what is left.* The gate
    was not re-based: its score is the same with any set of lines.
11. The decomposing writer with the gates (§5), as a block that can be left out. *Not built:* K4 measured no gain
    from it on a document that can be read as it is, and step 2 went to the eval.
12. The agent eval, made able to answer point 14: at least 100 questions, two judge passes, the five arms. The Opus
    arms are the only dear part, about $1.50 per ten questions with grep. Phase L says what it must add to be worth
    its cost: answers that can be scored exactly where possible, three runs a row, and a base on which grep is not
    already exact (links no line states, one thing under two names, folders too large to read whole). On the bank
    as it is, grep answers 37 of 37 linkage questions on both models and no memory can do better. *Done for links
    no line states (RESULTS S6):* 98 questions scored exactly, no judge, three runs a Haiku row, the arms headless
    with the CLI's own cost, $20.67 of Opus. *Folders too large to read whole (RESULTS S7):* 72 of the questions on
    the bank in one folder, every arm with a 100,000-token window, $7.43 more of Opus, which the owner allowed.

**Later**, when a base needs it: anything in §12.

## 14. Proof: one run, one table

`tests/e2e.py`, no model, under two minutes, once on the small path and once with `MEMORY_WIDE=5`: set up a base,
absorb documents and the policy graph, dream, ask (a lookup, a filter, an entity's own note, inputs, a question
across origins), drop a note from the middle of a chain and drop an origin, check what is left, open the page. It
exists since phase M with the dream, the ask and the drop parts (19 lines a path, a few seconds); each item of
step 1 adds its lines.

| measure | v0.4 today | floor for v0.5 |
|---|---|---|
| gold notes headed on the bank, without and with the index | 0.939 / 0.941; after phase L 0.978 / 0.973 | 0.96, the gate's floor now |
| characters a question on the bank | 2,359 / 2,599; after phase L 2,954 / 3,138 | the gate's 3,000 / 3,200. The first floor here was 1% over v0.4; phase L spent a quarter more on purpose (§11) |
| ten questions in one call | 0.5 s | 0.5 s |
| the own note headed when a question names an entity that has one | not measured; fails for recall@10 | 0.95 |
| the inputs of an entity named in full | fails for `sfc-hier-v3` in every arm; after phase L the call prints all 17, and Haiku names the first four | 0.95 |
| a set by filter | 0.47 by question; after phase L Haiku answers 37 of 37 set questions exactly with the map | the whole set, by construction |
| after `drop` | the chain cut; a crash on a big memory; after phase M the chain holds, no crash, the reading gone, 5 of 5 notes built on it marked | the chain holds; no crash; nothing derived left |
| the host's answers changed by an absorb | 21 of 326 (19 on the script of phase M); after phase N 0, with the origin's notes in a block of their own for 6 | 0 until something is joined |
| an absorbed base's preference notes | lose their kind (0 of 2 kept); after phase N 2 of 2 kept, served to a host task only with `trust: preferences`, a `me-` note never | keep their kind (2 of 2) and are never served as the host's own |
| pointers checked | none; after phase O every pointer has a state, at each dream and each `ask`, and on 34 versions of one file none names a wrong line | every pointer has a state |
| dream, 1,677 notes with their readings | 0.85 s | 1 s |
| Haiku with the memory against Opus with grep (step 2) | 120 times cheaper, 8 times faster, 23 correct against 29; after phase L 107 times and 7.9 times, 25 against 29, and the same exact answers on 37 linkage questions at 35 to 46 times cheaper; on the worn bank after phase S 96% exact against 99%, 42 times cheaper and 2.3 times faster; in one folder under a 100,000-token window 89% against 99%, 46 times cheaper and 2.8 times faster, and Opus with the memory 97% for 0.57 of the price | as cheap; correct within the judge's own spread on 100 questions |
| lineage a note states only in prose, held (the worn bank) | none: v0.4 reads lineage from frontmatter only; after phase S 99.5% of `from` and of `supersedes`, 99% of the edges in the key, and the lineage alone answers 93 of 98 set questions | the gate's floors: 0.98, 0.98, 0.98, 91 |
| proposals that are the same thing (step 2) | 14 of 87 | half |

The 40 checks, the three retrieval gates and the stability eval stay. The only new test is this run.

## 15. What is needed from the owner

Answered on 2026-11-11: every recommendation below is taken (items 1 to 7). Item 8 is still open.

1. **What "downstream" means** (§8): made-from goes, built-on stays and says so. Say if built-on should go too.
2. **Readings in git** (`memory/_dream/notes/`), so a clone builds the same graph without paying a keeper.
3. **Identity by reading** (§7) removes two string rules that today's alias score rests on. The score is re-based in
   step 2 on a resolver's decisions. Confirm.
4. **Decomposing as an optional writer** (§5), not the default for what agents wrote: the measurement went against
   making it the default.
5. **The eval that can answer point 14** needs Opus arms on about 100 questions: roughly $15 to $25. Haiku's side is
   cents.
6. **Words and names**: entity and edge, as you wrote them (the README says thing and link; `graph.json` keeps
   `relations` for edges and `edges` for lineage, and schema 2 does not rename them); `SETUP.md`, `TAGS.md`,
   `ORIGIN.md`; `drop`, `absorb`.
7. **Go for step 0 and step 1.** They spend nothing.
8. Still open from the handoff: the branch and the licence.
