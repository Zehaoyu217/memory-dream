# memory-dream v0.4 — results

2026-10-30 (round 4: 2026-10-31) · built from the "Memory" email spec (`build-spec.md`) · macOS, Python 3.9.6, Claude Code 2.1.314.

# Phase H (2026-11-01) — a class tree, chains to the live end, shapes, and the graph view

## H1 — the class tree (two levels, no inference)

`KIND_PARENT` (experiment → finding, correction and preference → rule, metric → term) and `TYPE_PARENT` (table and
segment → dataset, column → feature, person and team → party, tool/job/pipeline/service → system), read through
`family()`. Three consumers, all 0 calls:

| consumer | before | after |
|---|---|---|
| conflict candidates (`CONFLICT_KINDS` by family: an experiment is a finding) | 64 on the bank | 53 — the group a token's rarity is judged in is bigger, so fewer pairs qualify; the 4 supersessions the review confirmed are all still produced (checked with the review's lineage undone) |
| shape check C12 (`SHAPES`: trained-on model → dataset, evaluated-on → dataset, measured-by → metric, owned-by → party, replaces same family) | — | 35 of 1,071 seed-type relations on the real index: evaluated-on 21, measured-by 10, trained-on 3, replaces 1; nearly all a `term` where a dataset or metric belongs — a retype for the review or a person |
| the viewer | colours by kind | colours and shapes by family, child kinds lighter; the entity graph's families; legends by family (`families` in the island, CONTRACT §3) |

Not added, as agreed: inference (transitive or inverse edges, OWL-style), beyond the explicit walks `ask` makes.

## H2 — supersession chains to the live end

215 superseded notes on the bank; 23 (11%) had a successor that was itself superseded, so the header's
`SUPERSEDED → v2` sent the agent on a second hop. `successors()` follows the first successor's chain (≤ 4 hops,
cycle-safe); the header reads `SUPERSEDED → v2 → v3`; `rank` lifts the whole chain for "current" questions and the
never-below rule now lifts the live end rather than a dead middle. A40 covers a three-note chain. Retrieval on the
real index 0.944 / 0.978 / 275 complete / 2,485 chars (one gold note moved; complete answers unchanged); stale set
unchanged (successor headed 1.00, above the old note 0.971, old marked 1.00).

## H3 — the viewer: an entity graph beside the time lanes, legends that toggle, markdown notes

- **Graph view** (`#view=graph`): entities as nodes shaped and coloured by family, sized by mentions, dashed when a
  newer version replaces them; the relations the notes state as arrows, current by default (an evidence note is
  live), with "include history". A deterministic force layout fitted to the pane; the 400 best-connected of the
  bank's 900 entities with relations (1,355 current arrows) lay out in 1.3 s; picking an entity outside builds its
  neighbourhood (two hops, ≤ 150); picking dims beyond two hops (one for hubs); hover lights a node's arrows.
- **Legends** in two rows (nodes, then edges), every entry a toggle: kinds and families, superseded, lineage kinds,
  relation types. Hiding a family hides its arrows; hidden entries are struck through.
- **Notes rendered as markdown** (headings, lists, quotes, fenced code, pipe tables, inline marks; note and entity
  ids become links; DOM nodes, never HTML), with the raw `ask` view collapsed below it; the header replica follows
  chains like `ask`. Lane labels stay put when the lanes scroll.
- Verified headless on both worlds (Playwright): 0 errors; a legend toggle hides 93 of 400 nodes and all built-on
  curves as expected; markdown lists and links render; the agent block is collapsed.

## H4 — the page for a person who knows nothing about any of this

Rewritten for its real reader: someone who wants to look at their own memory, see where it may be wrong, and say so
with no effort. Plain words everywhere — `gbm-model-exp233` reads "GBM Model Exp233", `evaluated-on` reads
"evaluated on", a date reads "30 Oct 2026", areas read "Churn 2026"; known ids inside authored titles are rendered
the same way; raw forms survive only in tooltips and one folded "What the assistant reads (technical)" block. Views
are "Timeline" and "Connections"; lines are "Built on", "Replaces", "Mentions"; a picked note shows "How this note
connects" (Built on, Replaces, Replaced by, Current version, Led to, Mentions, Mentioned by), "Mentioned in this
note", "What the assistant took from it". **Worth checking** is a section on the page, not a hidden panel: notes
that may disagree, names that may be the same thing, links that look odd, links that lead nowhere, notes on their
own, other things to look at — each item in a sentence, with a "Copy question" button that puts a ready question
for the assistant on the clipboard (the note titles and paths inside it, so the assistant can act); a picked note
has "Something wrong here? Copy a question", every extracted fact a "Wrong?" button quoting its line. On the bank:
106 items (53 pairs that may disagree, 35 odd links, 1 broken link, 4 notes on their own, 13 other). Theme: navy ink
and one blue, square corners, a seven-hue family palette validated in both modes by the dataviz validator (CVD
separation, lightness band, chroma floor, contrast; shapes carry identity as well); selection pops (1.7×, no ring)
and its lines light up with arrowheads flowing toward the newer note. Headless checks pass on both worlds; the
viewer is 938 lines, still one file, no dependencies.

Then, on the owner's review: white only (the dark theme went); the Connections view became a camera — drag to
pan, wheel or pinch to zoom around the cursor, drag a node to place it, a fisheye under the mouse (the node it
touches grows almost double, those around it less with distance), and bubbles below zoom 0.85 where nodes that
share a screen-sized cell fold into one count (on the bank at the fitted zoom, 48 bubbles hold 162 of 400 nodes;
zoomed out, 54 hold 379; zoomed in, none); the Selected panel keeps a Back/Forward trail; the note's text sits in
its own box as the main thing; "How this note connects" shows direct links first with mentions and the family
tree folded; "Worth checking" lists six items then "Show all", with no inner scrollbars. All verified headless:
pan moves the camera, a wheel step zooms 1.14 → 1.64, a drag moves a node, 51 nodes magnify near the cursor,
Back returns to the previous note; 0 errors. 1,075 lines, one file, no dependencies.

**H5 — measured tokens (1 Nov).** The owner shared their html-harness (a component catalogue measured from a bank's
public site: 190 design tokens, 178 components, the diagram skin) and asked for its look with one rule — nothing
that could cause legal trouble. What crossed over is values and conventions only: the ink ladder (one black at .95
/.80/.70/.60 for text, .95/.44/.34/.16 for rules) instead of navy hexes; one blue `#7297C5` (text twin `#446EA6`,
selection wash at 16%) used for what is selected and the lit path; the eight series colours in their order (navy,
blue, magenta, teal, orange, purple, red, ochre) for the families, grey for context; status colours for status only
(amber tint under a 3px rule for "may be wrong"); spacing on 8; a 3px ink rule opening every module; tabs as plain
words over a hairline with a 2px blue line under the open one; square outline buttons and chips; hairline rows in
every list; a serif voice for the page title and the picked note's title (Georgia, a system face); the year as a
faint watermark behind the timeline. Nothing of the bank's crossed: no font files, no icons, no mark, no wording,
no component markup (the magnifier in the search box is two CSS pseudo-elements). The harness's own diagram
references are MIT (vendored from a third party) and were read for conventions, not copied. Both headless checks
and the 37 acceptance tests pass unchanged; the page is still one file with no requests.

**H6 — zones, not bubbles; a calmer timeline (1 Nov).** The owner's review of H5: the bubbles were not cool, the
timeline had too many horizontal lines, zones should carry colour (the light grey, the blue, black), no accent bars
on top or left of a container, shorter buttons, no footnote under a button, and the family tree under the big chart
rather than folded in the panel. Done: the Connections view is now columns — one zone per family, white and light
grey by turns, the picked family's on a 12% blue wash, named in a strip above the pane; the families are ordered so
linked ones sit side by side (every order of up to eight is tried), the most connected things stand in each zone's
right-hand lane with their names, the rest in lanes to the left, and six barycentre sweeps level each thing with its
neighbours so the curves run short; the row spacing stretches to fill the pane, so names read at the fitted zoom and
go only when rows are closer than 10 px (the picked, lit, hovered and magnified ones stay). The clustering code is
gone (about 60 lines). The timeline lost its row lines and month lines: lanes are bands (white and light grey by
turns; general topics on a blue wash; the picked lane washed deeper), only January keeps a hairline, months are
ticks under their label, within-lane links are arcs above the notes, and mentions start hidden with their legend
entry off. Containers carry no bar: the note sits on the light grey field, warnings on the amber tint, the header
closes with a hairline. Buttons are 24 px and two words ("Something wrong?", "Wrong?", "Copy question"); what a
button does, and that it worked, is a flat ink popover on hover, focus or after a click. The family tree is drawn
full width under the figure whenever a picked note has one. The headless check now covers zones, the washed lane
and zone, the kept names and the reading-distance rule; 13 checks pass on both worlds, 0 page errors.

**H7 — mentions in the text, one action in ink (1 Nov).** The owner's next review: the action belongs at the right of
the box, in black; the things a note mentions should be marked in the text rather than listed below it, and none may be
missed; the technical block ("What the assistant reads") goes; the timeline's picked note should look as it does in
Connections (a blue outline, not an enlarged shape with a boxy edge). Done. Marking works on the rendered note: the
text nodes are merged first (the renderer emits one per word, which is why multi-word names failed on the first try),
then every surface form the index knows for each mentioned thing — id, plain words, aliases — is matched longest
first, whole words, any case, skipping code, links and chips already placed; a token that is both a thing and a note
now renders as the thing (it used to become a note link, so model and feature ids were never marked). Whatever the
text does not yield, typically a mention only in the title, is named once in an "Also about" line under the text.
Measured on 84 sampled bank notes (332 mentions): 0 missed; on the fixture (25 notes, 86 mentions): 0 missed. The
headless check now asserts every mention marked and no technical block on the picked note.

**H8 — the Map (v2) (1 Nov).** The owner showed a public ontology viewer's poster — a person asserts → what it
becomes → who reads it, verdict badges (certificate, opinion), one connected graph with only the hubs named, and a
legend that says what each kind of statement is worth — and asked for a v2 of the graph in that spirit, in our own
theme. Added as a third tab beside Timeline and Connections, so the two readings can be compared. Our epistemic
ladder, from the data the page already carries: written (notes a person wrote) · stated (lineage a note declares
itself) · extracted (facts the assistant read out of current notes, each quoting its line) · older (facts that rest
only on replaced notes) · disputed (conflict pairs) · open (question notes nothing was built on). The flow shows
these as three columns with status swatches and small badges and rewrites itself for a picked note or thing; the
graph is one framed force layout, nodes sized by their links, things with a note of their own in their family's
colour, the rest as ink dots, twelve hubs named at rest and the picked thing's neighbourhood named on pick; two
tables below give the counts and what to do with each kind. On the bank: 1,521 notes (logs aside), 2,428 stated
links, 2,354 current facts, 318 older, 53 disputed pairs, 60 open questions; 400 of 861 linked things drawn with
1,355 links. Fixing the Map's name sizes uncovered that Connections' names were also stuck at world size (a CSS
font-size overrode the per-zoom size on the layer); both now keep their size on screen. 15 headless checks pass
on both worlds.

# Phase G (2026-11-01) — agents on the real index, and two designs read for free money

## G1 — the agent eval at n = 3 batches per arm (Opus, real Haiku index)

Six Opus subagents, three batches of ten questions each (P1 projects, C-h1 churn-2026, P2 general: preferences,
reporting rules, corrections, a term, a how-to, a QA note), one arm per workspace: **memory** = the bank with its
real Haiku index and the skill (`ask` only; read-only), **grep** = the same notes with nothing else, told it may
`cat` whole folders. Prompts as in BUILD-GUIDE §7.3; answers graded by the Haiku judge against the question
bank's reference answers; usage from the transcripts (`eval/a21/extract.py`), wall time from the harness.

| arm | correct / partial / wrong (30) | tool calls per batch | API requests | tokens processed | cost units | seconds |
|---|---|---|---|---|---|---|
| memory (`ask` on the real index) | 23 / 7 / 0 | **5.7** | 6.0 | **498k** | **285,723** | **204** |
| grep (bare notes, folders allowed) | 23 / 7 / 0 | 18.7 | 19.7 | 1,742k | 465,811 | 273 |
| memory / grep | tie | **0.30** | 0.30 | **0.29** | **0.61** | **0.75** |

Per batch (correct/partial/wrong · tool calls): P1 memory 8/2/0 · 8 against grep 8/2/0 · 26; C-h1 memory 5/5/0 · 5
against 7/3/0 · 9; P2 memory 10/0/0 · 4 against 8/2/0 · 21. No wrong answer in either arm; every partial is a
detail missing or an unverified extra, on both sides. Cost units weight fresh input 1, cache read 0.1, cache write
1.25, output 5: the memory arm reads 0.29× the tokens but writes answers of the same length, and output is what
costs, so 0.61× is the floor this question format allows. The tier-3 gate of the bundle holds: accuracy within
one correct answer per ten (a tie), tool calls ≤ 0.35× (0.30×). One observation: on the densest batch (churn-2026,
60 notes plus daily log entries) the memory agent answered mostly from `ask`'s lines and read few whole notes, which
is where its five partials come from; the grep agent read whole notes and had three.

## G2 — Helix Foundry, HelixDB's memory skill, MOOSEDev: what they do, what was worth borrowing

Read for this pass (cloned, not run): **Helix Foundry** (`HelixDB/helix-foundry`, Apache-2.0) — an agent drafts an
ontology over a company's databases, Slack, Notion and documents, a person reviews it, and it loads into HelixDB as
one graph; every value stays traceable to the row or quote it came from, reads are versioned by load (`as_of`), the
agent's Read and Ask contracts are JSON schemas (`contract/ontology_agent/`) whose results carry `stats: what the
request spent`, and a price catalog of models with as-of dates feeds its cost estimates. A hosted product with a
database, a Go backend and a web app: a different problem (integrating a company's data) and a different cost
class; nothing in it is free to borrow, though its "every answer cites the row" is what `▸ path · line:` already
does for notes. **HelixDB's `helix-memory-system` skill** is a design guide for agent memory on a hybrid graph +
vector + BM25 store: `Memory` nodes with `isLatest` / `validFrom` / `validTo` / `deletedAt`, `UPDATES` / `EXTENDS` /
`DERIVES` edges, a maintained profile, and two rules it states as law — "never collapse a memory system to
vector-only" and "exact names, ids, rare tokens need BM25; embeddings blur them". Our plain files already carry each
of these: `supersedes:` is `UPDATES`, `from:` is `DERIVES`/`EXTENDS`, the SUPERSEDED mark is `isLatest`, `prefs/`
plus the digest is the profile, and grep is the exact-token channel the skill says must exist.

**MOOSEDev** (`Trivyn/moosedev`, Apache-2.0 on a closed engine; the NeSy 2026 paper "Ontology-Grounded Project
Memory for Coding Agents", read through search summaries because arxiv.org is outside this session's network) is
the closest relative: typed records (decision, requirement, constraint, alternative, consequence, pattern,
anti-pattern, lesson) in two small OWL ontologies with SHACL shapes, the graph committed to git as N-Quads,
supersede-with-rationale (the new record links `supersedes` to the old and `hasRationale` to a rationale node; the
old is flipped to `superseded`, never deleted), current-only retrieval by default with history one hop away,
provenance of who and when, MCP tools and SPARQL. Its benchmark (`bench/RESULTS.md`) is the useful part: on
reversal pairs (a decision later reversed) the structured graph answers with the current state 100% of the time,
BM25 over the same text 46% when context is pushed to the agent (8% in the worst pair) and 91% when the agent pulls
its own search; the paper's set-completeness and negation questions score 0.98–1.00 against 6–27% for a vector-
memory product; a dense channel beside BM25 recovered nothing BM25 missed at k = 10 and only re-ranked the head
(−19% agent tokens); and a grading lesson — stale-keyword detection is unreliable because a correct current answer
narrates the old state to deny it. Against this: our stale set already measures their "currency" — successor
headed 1.00, above the old note 0.97, old marked 1.00 — by lineage alone, with no database; our stale metric is
structural (which note heads, is it marked), not keyword-based, so their lesson is already built in; their dense-
channel result supports keeping retrieval at grep plus structure; their rationale node is our rule that a
superseding note's first line says what changed and why (the note is the rationale); their typed kinds are our
note kinds. Two of their ideas were cheap and missing here:

| borrowed | what | measured |
|---|---|---|
| a **negation (absence) set** in `adversarial.py` | 70 questions about things the memory does not hold: 30 versions never written (`…-v9`), 30 made-up ids with real prefixes, 10 nonsense terms beside a real word. A good answer says "(no match" or carries the `(weak match …` marker naming the unknown token | before: 64 of 70 flagged (4 version bumps headed the nearest version unmarked; 2 nonsense terms were vetoed by an entity hit on their real word). After the rule below: **70 of 70** on the real and the fake index; grep's "every matching line" is quiet on 60 of 70 |
| a **lineage connectivity line** in `check` (their bootstrap target: edges ≳ nodes) | `lineage: 2,426 from/supersedes links over 1,073 live project notes (2.3 per note) · 13 link to nothing: …` — the notes "why" and "what came of" cannot reach | bank: 13 of 1,073 (8 questions, 2 datasets); fixture: 4 of 23. 0 calls, 9 lines |

The weak-match rule changed in three ways for the absence set, each measured on the 326 real questions so the
marker stays rare there: an id, version or number the question names that no note mentions is always said, even
when its neighbours match ("feat-cb-handoff-rule-v9" heads the v2 and v1 notes, marked); the rule reads the
question's own words only, never the aliases the index added (those produced 22 false markers on real questions
in the first attempt: dreamer-coined names like `precision-at-0.90`); a hyphenated phrase is judged by its words
("call-routing" counts as found when both words are). The entity veto went: a generic word that is an entity id
("holdout") no longer hides a nonsense neighbour. Real questions marked: 2 of 326 on the real index, 1 of 326 on the
fake, both truthful ("company" and "segmentation" occur in no note); retrieval unchanged at 0.946 / 0.978 / 275
complete / 2,487 chars; suite 35/35.

Not borrowed, on purpose: an ontology language, shapes and a daemon (`CONTRACT.md` plus `check` validate what we
need, and "a thin layer on grep" is the design); separate alternative/consequence records (a decision note carries
them); an author field (notes carry a date; who wrote them is git's job); `as_of` point-in-time reads (about ten
lines — filter notes by date and recompute supersession as of then — but no question in the bank asks it; listed
under next steps).

# Phase F (2026-10-31) — five improvements, each measured, the best kept

The review of phases A–E named the weak spot (scattered evidence: 66% of multi-note questions get every gold note,
against 99% for `cat` of the folder) and five cheap moves. Each was built, measured, and kept only where it won.

## F1 — lineage one-liners (kept, at 4 lines)

When a question walks lineage (what came of, why, based on, depends on) or names two or more ids, the picked notes'
parents, successors and — for "what came of" — children come along as a header plus their `# ` line.

| 326 bank questions | gold notes | numbers | precision (headed notes that are gold or one lineage hop from gold) | complete answers | chars per question | scattered evidence, all gold (248) |
|---|---|---|---|---|---|---|
| none | 0.895 | 0.972 | 0.710 | 242 | 2,002 | 0.661 |
| **4 lines (kept)** | **0.920** | 0.975 | 0.649 | **259** | 2,226 (+11%) | **0.730** |
| 8 lines | 0.930 | 0.976 | 0.612 | 264 | 2,352 (+17%) | 0.750 |

Per 10k characters read, complete answers go 3.71 → 3.57 → 3.44: the one-liners buy recall at a small cost in
density. Four was kept because it takes most of the gain (+7 points on scattered evidence, +17 complete answers) for
half the extra characters of eight, and the stale set even improves (successor first 0.952 → 0.962). Precision drops
because a relative of a picked note is not always a relative of a gold note; it is still a pointer the agent can use.

## F2 — the model-free path is quiet (kept)

Without a model, `dream` used to write one prompt file per unindexed note and `check` one C5 line per note.

| bank, 1,677 notes, no model | before | after |
|---|---|---|
| `dream` | 1,678 prompt files written, "run the memory-dreamer" | 0 files; "1677 without entities (no model; `dream --prompts` writes prompts for a helper agent)"; 0.4 s |
| `check` | 1,700+ lines | 29 lines; C5 is one line that says answering is unaffected and how to add entities |
| the helper-agent flow | automatic | `dream --prompts` (1,679 files: notes, review, TODO), then the agent, then `dream` |

A10 covers both paths. SKILL.md says it in one clause: "without a model nothing is missing for answering".

## F3 — a precision line in `retrieval.py` (kept)

A headed note counts as relevant when it is gold or one lineage hop from gold. Baseline 0.710; with F1 0.649. It is
the missing half of achievement per word and will gate future changes alongside recall and characters.

## F5 — `taste()` simplifications (none kept; measured and reverted)

| variant | named prefs | implicit prefs | house rules | chars per task |
|---|---|---|---|---|
| as is | 1.00 | 0.87 | 0.46 | 4,021 (F1 adds ~6% on tasks) |
| without the "first word of a family" rule | 1.00 | 0.89 | **0.39** | 4,027 |
| without the context-family rule | 1.00 | **0.81** | 0.47 | 4,011 |
| without the artifact rule | 1.00 | 0.87 | 0.42 | 3,955 |
| without the first two | 1.00 | 0.87 | 0.39 | 4,017 |
| candidate pool by kind (preference, rule) instead of general areas | 1.00 | 0.87 | 0.44 | 3,979 |

The "first-name" rule turned out to be a family-word rule: "chart" in a task brings the whole `chart-style-*` family
of house rules, which is where 7 points of rule recall live. Every heuristic in `taste()` earns its keep; the code
is unchanged except that its comment now says what each rule is worth.

## F4 — is the index worth anything to answers? (one real run: kept)

Phases D and E could only ask this on a fake index or a 70-note sample. The whole 1,677-note bank was indexed with
Haiku (`tests/haiku_cmd.py`, before the cache-aware wrapper of F8): 1,677 extraction calls, $3.734 ($0.0022 per
note, median 5,950 tokens in and 1,963 out, 0 errors), then one review call ($0.009) over 30 entity pairs, 5 labels
and 20 conflicts. The run merged 5 aliases, mapped 1 label onto a type, admitted 4 new types on probation (`lifts`,
`predicts`, `compared-against`, `wants`; vocabulary 12 of 24) and decided 19 of the 20 conflicts (CONFLICTS.md now
holds 3 supersessions, 36 compatible pairs, 1 left to a person). Graph: 923 entities, 2,672 relations — 82% typed,
18% kept as `other/<label>` over 418 labels, 427 of them below the review bar; 39 conflict candidates pending
(C10), 12 ungrounded claims dropped (C4), 1 unresolved reference (C2). Then `ask` with and without the index on the
same world (`MEMORY_NO_INDEX=1` switches off alias expansion and the entity boosts; lineage stays):

| 326 bank questions, real index | gold notes | numbers | precision | complete answers | chars per question | complete per 10k chars |
|---|---|---|---|---|---|---|
| index on | **0.935** | **0.977** | 0.605 | **271** | 2,486 | 3.34 |
| index off | 0.921 | 0.975 | **0.650** | 258 | 2,226 | 3.56 |
| routed (`MEMORY_WIDE=100`), on | **0.936** | **0.972** | 0.621 | **271** | 2,273 | 3.66 |
| routed, off | 0.917 | 0.966 | **0.658** | 254 | 2,073 | 3.76 |

| adversarial sets, real index | index on | index off | grep |
|---|---|---|---|
| alias questions (280 surface forms Haiku recorded), gold note headed | **0.839** | 0.800 | 0.521 |
| stale trap (104): successor above the old note · old marked when shown | 0.952 · 1.00 | — | — |
| scattered evidence (248), all gold | 0.786 at 2,348 chars | — | 0.99 at 12.6k (`cat` folder) |
| taste tasks: named prefs · implicit prefs · house rules | 1.00 · 0.85 · 0.44 at 4,457 chars | — | — |

The index is not neutral on a real index: +1.4 points of gold recall (+1.9 routed), +13 complete answers, +3.9 on the
alias set, for 12% more characters and 4.5 points of precision. 25 questions are missed only with the index on and
37 only with it off, so the two paths fail on different questions rather than the index adding noise everywhere.
Per 10k characters the index is slightly less dense (3.34 against 3.56 complete answers), so the question is whether
its extra characters are productive: they cost 6,500 characters per extra complete answer — twice the average
cost of `ask`'s own picks, but half the cost of a folder `cat` (12,800) and a twelfth of grep lines (77,000), the
agent's two ways of finding the same notes without the index. Decision: **keep `ask`'s use of the index**; the
~60 lines of entity boosting stay, and the F5 cut of the review is closed. The scattered-evidence set also moves,
0.730 on the fake index → 0.786 here: real entities link the notes that share a subject.

**The sweep that followed (free money).** With a real index to measure against, the three constants of the boost
were swept (`MEM_PY` points the eval at a variant of the script; all on the same world):

| entity boost: named · phrase · ×findings/decisions | gold | numbers | precision | complete | chars/q | alias | scattered | stale: successor above |
|---|---|---|---|---|---|---|---|---|
| 0.35 · 0.15 · 1.5 (as shipped) | 0.935 | 0.977 | 0.605 | 271 | 2,486 | 0.839 | 0.786 | 0.952 |
| 0.50 · 0.15 · 1.5 | 0.920 | 0.973 | 0.597 | 267 | 2,486 | 0.839 | 0.786 | 0.952 |
| 0.35 · 0.15 · 2.0 | 0.918 | 0.973 | 0.599 | 266 | 2,479 | 0.832 | 0.782 | 0.952 |
| 0.35 · 0.00 · 1.5 (no phrase tier) | 0.935 | 0.977 | 0.602 | 271 | 2,488 | 0.839 | 0.786 | 0.952 |
| 0.35 · 0.15 · 1.0 (no kind multiplier) | 0.939 | 0.975 | 0.609 | 274 | 2,461 | 0.843 | 0.798 | 0.962 |
| 0.20 · 0.00 · 1.5 | 0.938 | 0.974 | 0.611 | 272 | 2,461 | 0.846 | 0.790 | 0.971 |
| 0.30 · 0.00 · 1.0 | 0.938 | 0.975 | 0.609 | 273 | 2,450 | 0.843 | 0.794 | 0.962 |
| **0.25 · — · — (kept)** | **0.939** | 0.973 | **0.609** | **273** | **2,448** | 0.839 | **0.794** | **0.971** |
| 0.20 · — · — | 0.939 | 0.975 | 0.613 | 273 | 2,432 | 0.836 | 0.794 | 0.971 |
| 0.15 · — · — | 0.940 | 0.974 | 0.616 | 273 | 2,417 | 0.832 | 0.794 | 0.971 |

Stronger boosts lose (0.50, or ×2.0 for findings and decisions: −1.5 to −1.7 points); the phrase tier is worth
exactly nothing (the row with it off is the shipped row); the finding/decision multiplier costs 3 complete answers.
From 0.15 to 0.30 with neither, every column ties within one or two questions, so the boost is now **one weight,
0.25**: phrase-matched entities still add their aliases as patterns (that is where the alias set is won) but no
longer score, and kinds no longer scale the boost. Two constants and a branch gone. Final numbers against no index:
gold 0.939 vs 0.921 (+1.8; routed 0.938 vs 0.917), complete answers 273 vs 258, characters 2,448 vs 2,226 (+10%),
alias 0.839 vs 0.800, 19 questions missed only with the index against 30 only without. On the fake-indexed bank
the change is noise (0.920 → 0.919 gold, 259 → 258 complete, 2,226 → 2,220 chars; taste 1.00 / 0.87 / 0.45 at
3,948 chars per task); the suite stays 35/35. F9 below moves both sides of this comparison (lineage one-liners for
every question); its last table has the final figures.

## F6 — the graph contract (`.specs/memory-dream/CONTRACT.md`)

The shapes `memory.py` writes and reads are now written down field by field with their invariants: the graph
(`graph.json`, `index.db`), the viewer's data island, the extraction cache, `store.db`, the manifest, the warning codes
and the grammar of the four user-owned files. Every graph carries `schema: 1`; `memory.py check` prints
`contract: schema 1 ok` or the violations; test A38 validates the fixture's graph, round-trips `index.db` to the same
notes, edges and relations, and parses the viewer's island. The viewer was rebuilt on this contract and derives
everything else client-side.

## F7 — another pass for free money (model-free, measured on the bank)

| idea | result | kept |
|---|---|---|
| two live `…-vN` siblings, or two live notes with the same title, as conflict candidates (a missing `supersedes:` is almost certain) | 0 such pairs on the bank (its versions all carry `supersedes:`); the fixture test queues `churn-xgb-v3 / churn-xgb-v4` and a restated decision | yes: high precision by construction, 0 noise where lineage is kept |
| open questions in the digest: question notes no finding or decision builds on | 51 on the bank; the digest stays 25 lines | yes |
| C11: a note over 40 lines (SKILL.md's own rule, never checked) | 0 on the bank and the fixture; fires on a 42-line note | yes |
| cross-project body slugs as `refs` when the stem is unique anywhere | +67 links; gold 0.920 → 0.916, numbers 0.975 → 0.976, precision unchanged, scattered evidence 0.730 → 0.726 | no: nil for answers, so the simpler same-project rule stays |
| a recency tie-break for "current" questions (phase E) | no change on 40 questions | no |
| a table of contents of the named project (phase A) | +2.9k characters per scoped question | no |

## F8 — the dreamer: cache the prefix, keep every call small

`claude -p` caches its system prompt across calls, not the message; so the prompt's static part (template, EDGES,
KNOWN) now goes into the system prompt (`--append-system-prompt` in `tests/haiku_cmd.py`, told its length through
`MEMORY_STATIC_PREFIX`), notes are indexed project by project with one KNOWN per project (big memories: refreshed at
most every 10 waves), and note text is capped at 16k characters so no call grows large.

| 70-note sample, Haiku | before | cache-aware |
|---|---|---|
| cost per note | $0.0022 | **$0.0015 (−32%)** |
| input tokens per call (median) | 5,350, none cached | 5,314: **3,331 read from cache**, 1,518 written, 2 fresh |
| output tokens per call (median) | 2,232 | 1,618 (−28%) |
| seconds per call | 11.5 | 8.9 |
| graph | 56 entities, 132 relations (23 labels), 0 C4 | 74 entities, 122 relations (15 labels), 1 C4 |
| fixture A3/A18 with real Haiku (30 notes) | round 1: $0.0452, convergence 1.05× | **$0.0374**, convergence 1.12× after one pass, **1.06× after the review** (target ≤ 1.2×); the one split left is `cards.txn_daily / txn-table`, as in round 1 |

The entity count on the sample moved (74 against 56); the fixture's convergence check says dedup still holds, so the
difference is in what Haiku chose to extract, not in merging. Review calls are one per dream and need no caching.

Then `--effort low`, now the wrapper's default (`DREAM_EFFORT=default` restores the CLI's setting):

| 70-note sample | cache-aware | cache + effort low |
|---|---|---|
| cost per note | $0.0015 | **$0.0013** (−41% against the starting $0.0022) |
| output tokens per call | 1,618 | 1,588 · cached input 3,848 of 5,302 |
| graph | 74 entities, 122 relations (15 labels), 1 C4 | 67 entities, 124 relations (10 labels), 2 C4 |
| fixture A3/A18 (30 notes) | $0.0374; 16 of 20 true entities found, 1.06× after the review | **$0.0289**; 15 of 20 found, **1.00×** (no split at all), 2 C4 |

Low effort finds one true entity fewer on the fixture and drops two ungrounded claims; it merges cleaner. Kept as the
default because grounding already protects the graph from what less thinking costs.

## F9 — what only a real index could show: two hijacks, one trigger, and the detector's precision

The fake dreamer records no surface forms and no wrong aliases, so three things were invisible until the bank had
a real index. Each was found by reading the misses of F4's alias set (45 of 280) and the Haiku verdicts.

**Alias hijacks.** Haiku records generic words as names: "Model" is a name of `inc-gbm-v3`, "v4" of
`lbl-fraud-gbm-v4`, and `exp-102` an alias of the entity `lightgbm`. Any question containing "model" then named
`inc-gbm-v3` outright (+top+1), and "LightGBM v3" pulled seven projects' `exp-102` notes. A second bug hid the
good names: `low` kept the question's punctuation, so a 2–3-word name at the end of a question ("…about Intent model
v2?") never matched. Three rules now: punctuation is stripped before name matching; a single token selects an entity
only when it is that entity's id ("churn") or an id-like recorded name of 4+ characters ("exp-102" — never "model"
or "v2"); and a hit entity's plain single-word names are not added as patterns (its id and multi-word names are).

**Lineage one-liners for every question.** The alias fix cost 7 "current X model" answers, and the trace showed
why: the hijacked `inc-gbm-v3` patterns counted as two ids named, which switched the lineage one-liners on, which
showed the superseded predecessor the gold list counts as history. The accident was doing useful work, so the
trigger (lineage words or two ids) was measured against one id and against no trigger at all:

| real index, 326 questions | gold | numbers | precision | complete | complete (`--must`) | chars/q | alias (280) | scattered (248) | stale: successor above |
|---|---|---|---|---|---|---|---|---|---|
| after F4's sweep | 0.939 | 0.973 | 0.609 | 273 | 277 | 2,448 | 0.839 | 0.794 | 0.971 |
| + the three alias rules | 0.936 | 0.976 | 0.611 | 268 | 275 | 2,417 | **0.889** | 0.766 | 0.962 |
| … without the punctuation rule | 0.935 | 0.976 | 0.612 | 267 | — | 2,413 | 0.821 | 0.762 | 0.962 |
| … plain-word names allowed as patterns | 0.936 | 0.976 | 0.610 | 268 | — | 2,419 | 0.886 | 0.766 | 0.962 |
| + one-liners from one id named | 0.938 | 0.976 | 0.597 | 270 | 277 | 2,466 | 0.893 | 0.774 | 0.962 |
| **+ one-liners for every question (kept)** | **0.946** | **0.978** | 0.597 | **275** | **280** | 2,487 | **0.893** | **0.794** | **0.971** |

Per 10k characters the kept row and the row before it tie (3.39 against 3.40 complete answers); the extra
one-liners cost 3,900 characters per extra complete answer, cheaper than the index's own 6,500. The condition and
the `ids_named` count are gone from `rank`; in the complete print the relatives are listed with the memory, not as
pointers (A25). On the fake-indexed bank the same change moves gold recall 0.919 → 0.937 and complete answers
258 → 272 for +6% characters, scattered evidence 0.726 → 0.782, the stale trap 0.962 → 0.971; taste on the real
index 1.00 / 0.89 / 0.48 at 4,225 characters (from 1.00 / 0.85 / 0.44 at 4,457). Suite 35/35.

What the index is worth, final (same world, `MEMORY_NO_INDEX=1` for the right-hand column):

| real index | with the index | without |
|---|---|---|
| gold · numbers · precision | 0.946 · 0.978 · 0.597 | 0.938 · 0.979 · 0.616 |
| complete answers · chars per question | 275 · 2,487 | 271 · 2,373 |
| routed (`MEMORY_WIDE=100`): gold · complete · chars | 0.940 · 273 · 2,255 | 0.938 · 271 · 2,196 |
| alias questions, gold headed (grep the form: 0.521) | 0.893 | 0.829 |

The index's own share is now +0.8 points of gold recall, +4 complete answers and +6.4 points on the alias set for
+4.8% characters: smaller than F4 measured, because the one-liners now do for every question part of what the
entity boosts did for some. Still positive, still kept; the alias set is what it is for.

**The conflict detector's precision.** Two more `dream --review` calls on the real index ($0.0053 and $0.0043,
20 and 18 pairs, 17 and 18 decided) cleared the backlog: 78 verdicts in CONFLICTS.md, 4 supersessions, 4 left to
a person, 70 compatible. Of the 67 candidates the detector produces on this world today, 4 are supersessions
(6%): by rule, an id-like token 2 of 19, two rare title words 2 of 48, plus the 4 unsure. The four are real missing
`supersedes:` lines — `dec-ed-promote-v3` over `dec-ed-gbm-for-watchlist`, `clv-ml-v2` over `clv-bgnbd-v1`,
`mrisk-find-watchlist-065` over `exp-506`, `dec-rs-promote-v3` over `dec-rs-placement-cutoff` — and `ask` now
marks the old notes as history. A tighter rule (three shared tokens, or two with an id-like one) keeps 3 of the 4
and 1 of the 4 unsure in 15 candidates (20%). Not taken: with a model the review costs $0.00026 a pair and recall
is worth more than precision; without one, the C10 list is long (67 pairs on 1,677 notes) and already ordered
most-shared-first, so a person or a subagent meets the likely ones first. The version and same-title rules of F7
fired 0 times here (every version carries `supersedes:`).

# Phase E (2026-10-31) — an evaluation that measures the claim

`REVIEW.md` F12 and phase E. New tooling: `eval/retrieval.py --must` (gold notes that are superseded count as history),
`eval/adversarial.py` (the sets where grep should lose, measured offline against simulated grep strategies),
`MEMORY_NO_INDEX=1` (what the index is worth to `ask`). Everything below is on the 1,677-note bank unless said.

## E1 — gold lists name history

| 326 bank questions | gold recall | complete answers |
|---|---|---|
| as written (superseded notes required) | 0.895 | 242 of 326 |
| `--must` (heading the successor answers the question) | **0.899** | **252 of 326** |

## E2 — where the design should win, offline

| set | what it tests | `ask` | grep, every matching line | `cat` the named folder |
|---|---|---|---|---|
| **stale vs current** (104 questions whose gold has an old → new pair) | the live successor heads the answer and the old note is marked | successor headed 0.981; **successor above the old note 0.952** (0.702 before this phase); old note marked SUPERSEDED whenever shown **1.00** (0.865) | both printed, unmarked: the agent must open frontmatter | both printed, unmarked |
| **scattered evidence** (248 questions with 2+ gold notes) | every gold note headed, and characters read | all gold **0.661** at **1,874** chars/question | 0.871 at 82,235 | 0.991 at 12,625 (214 scoped questions) |
| **alias traps** (14 surface forms on the real-indexed 70-note world: "what do we know about card-not-present?") | the entity's home or headline note found | 0.929 with the index, **0.929 without it**; ~1,950 chars | 0.429 for the exact phrase | — |

Per 10k characters read, complete answers on the scattered set: `ask` 3.5, `cat` the folder 0.78, grep lines 0.11.
Reading: `ask` loses on scattered evidence (66% vs 99%) and pays that for 6.7× fewer characters; it wins the stale trap
outright, which grep cannot even see; and the alias questions are answered by word matching, not by the index — one
more datum for "the index serves the viewer and management, not answers".

Change adopted from E2: **a superseded note never outranks its live successor** (`rank`: the successor's score is
at least the old note's). Stale set 0.702 → 0.952 above, full gate 0.898 → 0.895 gold (9 regressed, 7 fixed, all
history notes dropping out of the top 8), numbers 0.972 unchanged, history-free 0.899, routed 0.889 → 0.891. And a
short `(above)` header keeps the SUPERSEDED mark, so history is marked wherever it appears.

## E3 — agents: one memory run against the strongest grep arm (Opus subagents, P1 batch, Haiku judge)

The grep arm was told it may `cat` whole folders; the memory arm got the skill's description, the script path and
SKILL.md. Replies: `eval/agent/runs/E-mem-P1.md`, `E-grep-P1.md`; verdicts `eval/agent/judge-E-P1.json`.

| | memory arm | grep arm (folder `cat` allowed) | ratio |
|---|---|---|---|
| answers, 10 questions (correct / partial / wrong) | 7 / 3 / 0 | 8 / 2 / 0 | tie within noise (the judge's "partials" are detail-level on both sides) |
| tool calls | **7** (questions file, one `ask` for all ten, four checking reads) | 31 | **0.23** |
| harness tokens for the run | 113.7k | 120.4k | 0.94 |
| wall time | 275 s | 285 s | 0.96 |
| minimum reading | the `ask` output: 25,092 chars (~4.2k words) for ten questions, plus SKILL.md (650 words) | unknown (31 reads) | — |

Reading: with the skill as it now is, the memory arm needs a quarter of the tool calls for the same accuracy; the
token and time gap of round 2 (0.47× cost, 0.35× time) did not show in this single pair. Three reasons are candidates
and none is measured here: one run per arm (round 2 had three), the harness token figure is not round 2's cost units
(cache reads weighted 0.1), and the grep arm was allowed `cat` of folders, which round 2's was not. What this pair does
establish: correctness is not lost against the strongest grep strategy, and tool calls — the thing that scales context
re-sends — drop 4×. A proper rerun needs transcripts: n ≥ 3 per arm, single-question agents, cost units.

## E4 — the write path: an agent saves a session under SKILL.md (one Opus run on the 30-note fixture)

Input: SKILL.md, a copy of the churn-2026 fixture, and a six-line fictional session — an experiment result with
numbers, two preferences said in passing, a correction of a metric definition, a decision, an ownership change, and
one unresolved incident ("nothing concluded yet"). The agent used 24 tool calls in 12 minutes and did not run `dream`.

| what was said | what the agent wrote | lineage |
|---|---|---|
| exp-021: AUC 0.77, recall@10 0.45 on holdout-2025q4, n=1.2M, 2026-11-03 | `churn-2026/exp-021.md` (7 lines) | `from: [exp-019-recall]` |
| decision: promote the retrained model as churn-xgb-v3.1 from 2026-11-10; cuts stay | `dec-promote-v3.1.md` (8) | `from: [exp-021, dec-risk-tiers]` |
| the new model itself (implied) | `churn-xgb-v3.1.md` (10) | `from: [exp-021, dec-promote-v3.1]`, **`supersedes: [churn-xgb-v3]`** |
| correction: recall@10 is per month, not per quarter | `metric-recall-at-10-monthly.md` (9) | **`supersedes: [metric-recall-at-10]`** |
| cards.churn_labels now owned by retention-data | `ds-churn-labels-owner.md` (10) | **`supersedes: [ds-churn-labels]`** |
| "recall@10 per risk tier" · "no red/green, colour-blind reviewers" | `prefs/maya-ortiz-recall-by-tier.md`, `prefs/maya-ortiz-no-red-green.md` (7–8) | the rule, where it applies, why, who said it, when |
| the nightly job failed twice, under investigation | one line in `log/2026-10-31.md` | — |

No existing note was edited; no note is over 10 lines. `dream` with no model: 38 notes, 0 C1/C2/C6; one C10 —
`dec-promote-v3.1` / `dec-retrain-cadence` share the token `churn-xgb-v3`, a false candidate the review would mark
compatible. `ask`, five questions in one call (7.5k characters): **5 of 5 facts found** — AUC 0.77 for exp-021; the
owner of cards.churn_labels, with the old dataset note marked SUPERSEDED; recall@10 per month, with the old definition
marked SUPERSEDED; the current production model v3.1, with v3 marked SUPERSEDED; and for "Make the recall@10 chart for
Maya Ortiz's retention readout" both preference notes head the answer in full.

Caveats: one run, one model, a transcript written by the evaluator; the agent wrote one note the transcript only
implied (the model note churn-xgb-v3.1), which SKILL.md allows (a model's note is named after the model). The write
rules measured here for the first time hold: one note per thing, lineage by `supersedes:` instead of edits,
preferences saved at once as `prefs/<first>-<last>-<topic>.md`.

# Phase D (2026-10-31) — simplify what the measurements allow

`REVIEW.md` F9, F10, F13 and §5. Suite 34/34; bank retrieval byte-identical before and after (0.898 / 0.972 / 2,004
characters; routed 0.889 / 0.962; taste 1.00 / 0.87 / 0.46).

| change | before | after |
|---|---|---|
| `dream()` | one 306-line function of closures | a `Dream` class in 15 stage methods (plan → index → graph → demote → review → write → report), none over 68 lines |
| tuned numbers in `rank`/`route` | 13 literals in the code | one `W` table with the measurement behind each; 46 retrieval literals remain outside it (15 distinct), from 58 (22) before phase A |
| concurrent dreams | raced on manifest.json and store.db | `_dream/lock`: a second dream exits 3 with a message; a lock older than 2 h is taken over (measured: fresh lock refused, stale lock taken, no lock left behind) |
| question words | ASCII only: "vélocité" produced no term | `\w`: "qu'est-ce que la vélocité?" finds the note |
| legacy | INDEX.md unlink | removed (INDEX.md stays skipped if present) |
| `memory.py` | 1,897 lines (review), 2,391 after phases A–C | 2,446 lines: the features of A–C (kinds, Claude Code's memory, the digest, two-tier vocabulary, conflicts, the lock) cost ~550 lines; the review's 1,400-line target is not reachable with them in |

Measured and kept, not cut: `ask`'s entity boosts. On the one world with a real index (70 notes, 56 entities, 12 bank
questions) gold recall is 0.842 with or without them, number recall 0.991 with against 0.970 without, +8% characters
— a small positive, so the ~60 lines stay (F5 said measure, then cut or keep). Not done: F11 (patch below 10,000
notes); the in-memory rebuild is exact and takes 0.6 s at 1,677 notes, while a patch would have to recompute headlines,
mentions and evidence to match it.

# Phase C (2026-10-31) — a constrained open vocabulary, and conflicts for a subagent to settle

`REVIEW.md` §10 and the conflict queue of §6 phase C. Suite 30 → 34 tests (A34–A37; A11/A12/A14/A20 rewritten),
34/34 in 21 s. Real-model checks used Haiku through `tests/haiku_cmd.py` with costs logged.

## The vocabulary, two tiers (measured with Haiku on 70 bank notes: fraud-2026, collections-uplift, 10 prefs)

| measure | closed (round 3) | constrained open |
|---|---|---|
| extracted relations | — | 257; Haiku wrote a label distinct from the type for 241 (94%), `type: other` for 40 (16%), **0 invented types** (sprawl ends at the source), 0 grounding drops |
| relations in the graph | 81% typed, 13% hidden in the cache, 5.5% dropped | 132: **107 typed (81%), 25 shown as other/<label> (19%) over 23 labels** — 4 of them the old drop list discarded (`is-a`, `excludes`, `excluded-from`, `removed-from`), the rest were invisible |
| the label tail | flat (1.5 uses per name on the 56× bank) | flat again: the largest label has 2 uses in 70 notes; nothing reaches the 5 / 5 / 2 bar |
| review with the bar lowered to 2 / 2 / 1 | — | `lifts` ×2 offered; Haiku answered `new: X lifts Y means feature X improves the measured performance of model Y; differs from measured-by …`; admitted as `- lifts (proposed 2026-10-31)`; $0.0011 |
| cost per indexed note | $0.0013 (60 notes, round 3), $0.0020 (inside the 1,677 bank) | **$0.0022** (median 5,350 in / 2,232 out tokens, 11.5 s): the label field and the longer relation instruction cost about $0.0009 per note on a small memory |

Gates in code, tested with the fake dreamer: under the bar a label is never offered (A34); `new:` writes a line marked
`(proposed <date>)` and relabels at 0 extraction calls (A34); a proposed type still under the bar after the probation
is demoted back to a label, 0 calls (A35); a full budget offers nothing, C7 names the waiting labels, raising the
budget admits them (A36); `pack: software` adds 6 types (A34). EDGES.md carries the knobs: `promote: 5 uses, 5 notes,
2 areas`, `budget: 24`, `probation: 60 days`. The `drop:` list shrank to note-to-note links (answers, led-to,
basis-for, …); claims and comparisons (`beats`, `improves`, `causes`) are kept as labels. Deviation from §10: when the
budget is full the code refuses promotion and says so, rather than asking the review to name a type to demote.

## Conflicts between live notes (measured on the 1,677-note bank, one real Haiku review)

| step | result |
|---|---|
| detector v1: five kinds, one shared rare title word | 282 candidate pairs across 41 areas |
| Haiku review of the first 20 (one call, $0.0040, 17 s) | 2 "a supersedes b" — both genuine by reading (`dec-ed-promote-v3` replaces `dec-ed-gbm-for-watchlist`; `clv-ml-v2` replaces the `clv-bgnbd-v1` baseline); 18 "compatible" — all clearly different things. Reviewer precision ≈ 20/20; detector precision 2/20 |
| detector v2: decision, model, finding only; an id-like shared token or two rare words | **282 → 38 candidates**, both true positives kept; the 157 rule/preference pairs (distinct by nature) gone |
| after the 20 verdicts | 24 pending on the bank (about two review calls, ~$0.01, to clear); every verdict persists in `CONFLICTS.md`; the 2 supersessions act as lineage: `ask` heads the current note and marks the old one SUPERSEDED (gold recall 0.897 → 0.898) |

Fake-dreamer test A37: three pairs queued (C10); the review decides one supersession (applied as lineage, both notes
byte-identical, `ask` shows SUPERSEDED), one compatible (never asked again), one unsure (`- a ? b`, listed for a person,
not asked again). Without a model the pairs are simply listed; nothing is decided.

Read path unchanged: 326 bank questions 0.898 / 0.972 at 2,004 characters per question; taste 1.00 / 0.87 / 0.46.
The viewer lists other/<label> links on the entity card (not drawn on the map) and conflicts in the Health queue;
rendered with 0 console errors. SKILL.md: 606 → 650 words (43 lines) for the labels and `CONFLICTS.md` — the only
words an agent must read once; achievement per word on the read path is unchanged at 3.7 complete answers per 10k
characters.

Found on the way: after the review wrote CONFLICTS.md, `dream` rebuilt the graph from its cached note half, so a new
supersession appeared only at the next dream (and `ask` did not see a hand edit of CONFLICTS.md between dreams). Fixed:
the review clears the cached half, and CONFLICTS.md is part of the freshness signature with EDGES.md and ALIASES.md.

# Phase B (2026-10-31) — free byproduct, any agent, beside Claude Code's memory

`REVIEW.md` F6 and §8 R1–R5, plus SKILL.md rewritten for any agent with a shell. 0 model calls anywhere. Suite 26 → 30
tests (A30–A33), 30/30 in 24 s.

| measure | before | after |
|---|---|---|
| notes with a kind, no model (bank, 1,677 notes) | 0 of 1,500 non-log notes (`type:` absent, kind "note") | **1,595 of 1,677 (95%)** from filename prefixes and areas; the graph shows experiment 291, feature 200, finding 176, dataset 163, decision 148, model 135, rule 96, question 84 |
| general areas detected, no model | all 48 areas (the kind rule saw no work kinds anywhere) | **7 of 48**: corrections, glossary, howto, log, prefs, qa, reporting |
| taste, 52 tasks: named / implicit prefs / house rules / chars per task | 1.00 / 0.83 / 0.42 / 3,826 | 1.00 / **0.87** / **0.46** / 3,795 (the taste pool is now the general areas only) |
| bank retrieval: gold / numbers / chars per question | 0.897 / 0.972 / 1,988 | 0.897 / 0.972 / 2,005; routed 0.888 / 0.962 |
| `memory/DIGEST.md` | — | bank: 15 lines, 1,596 chars (10 live heads across 5 projects); fixture: 9 lines, 894 chars |
| viewer after a dream with no model | rendered, kinds all "note" | renders Map, Explore, Health with the seven kinds, 0 console errors |
| `ask` with Claude Code's auto memory present (mock, 3 questions) | — | 0.10 s with or without it; topic file shown as `▸ claude-code: feedback_testing.md · feedback · 2026-10-25`, MEMORY.md skipped, directory byte-identical afterwards |
| `dream`, `log`, `viz` pointed at Claude Code's directory | wrote EDGES.md, ALIASES.md, `_dream/` into it | refused with exit 2 and a one-line reason |
| SKILL.md | 605 words, Claude-Code-flavoured | 606 words, addressed to any agent with a shell: three steps (read once, write as you go, dream at the end), a paragraph for Claude Code |
| a changed `memory.py` | the graph kept old kinds until a note changed | the manifest carries the script's hash: one rebuild, 0 calls (bank: 0.33 s) |

Achievement per word — the skill's efficiency, to be tracked from here on (characters are what is measured; ~6.7
characters per word of this kind of text):

| read path, 326 bank questions | complete-gold answers | characters per question | complete answers per 10k characters read | instruction read once |
|---|---|---|---|---|
| `ask` | 242 | 2,005 | **3.7** | SKILL.md 606 words |
| `cat` the named project folder (simulated best grep agent, 230 scoped questions) | 323 of 326 | 12,638 | 0.78 | a paragraph on the note format |
| one grep, every matching line | 262 | 63,001 | 0.13 | the same |

Tasks: the person's preferences 0.94 and house rules 0.46 of the gold notes at 3,795 characters per task. The
agent-level version of the same ratio (correct answers per 10k characters the agent read, including SKILL.md and
tool output) is phase E's job; RESULTS round 2 gives the ingredients (memory arm 27 of 30 correct at 311k tokens
processed, grep arm 26 at 1,465k).

What changed:
1. **Kinds without a model** (F6): `kind_of` — frontmatter `type:` (Claude Code's user/feedback/project/reference map
   to preference/rule/note/note), else the dreamer's kind unless it is the fallback "note", else the filename prefix
   (`exp- feat- ds- dec- fnd- find- q- metric-`, `…-vN` is a model), else the area (`prefs/ glossary/ corrections/
   reporting/ howto/ log/`). `general_areas` judges an area on its kinded notes only, so an unindexed memory no longer
   counts every area as general; this is what lifted taste.
2. **Claude Code's memory, read in the same call** (R1): `claude_code_memory` resolves `$MEMORY_CC_DIR`, else
   `autoMemoryDirectory` from `.claude/settings.local.json` or `~/.claude/settings.json` (the checked-in project
   settings are not trusted, as Claude Code itself does), else `<config>/projects/<git root, non-alphanumerics → ->/memory`;
   off with `MEMORY_SOURCES=notes` or `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`, and absent in cloud sessions. One extra grep
   over the topic files (never MEMORY.md, which Claude Code already loads), at most three files and two lines each per
   question, under their own mark.
3. **Never write there** (R2): `dream`, `log` and `viz` without `--out` refuse a root holding MEMORY.md or lying under
   `<config>/projects/*/memory`.
4. **The digest** (R3): `write_digest` after every dream — a comment line (free in Claude Code's context), the count,
   how to ask with the script's real path, the user's own preferences (`prefs/me-*`), the ten newest live decisions and
   models outside the general areas; ≤ 40 lines; `DIGEST.md` is skipped by the scan and required by the nothing-new
   short cut.
5. **Frontmatter compatibility** (R4): `modified:` is the date when `updated:` is absent.
6. **SKILL.md for any agent** (R5): requirements first (a shell, Python 3.9+, grep, no model), what the notes are,
   then the three things an agent does with memory in dense plain language, then one paragraph for Claude Code (which
   layer owns what, the digest import, never the same thing twice). The description keeps the one-call policy.

# Phase A (2026-10-31) — the read path never loses

Changes to `ask` from `REVIEW.md` F1–F4 and F7, all with 0 model calls. Suite 21 → 26 tests (A25–A29), 26/26 in 19 s.
Bank numbers use the 1,677-note world indexed by the fake dreamer (RESULTS round 4 shows the real index within noise).

| measure | before | after |
|---|---|---|
| fixture (30 notes), the 10 A21 questions in one call | 11,325 chars, 24 of 30 notes headed | 12,922 chars, **30 of 30**: per-question pointers, then the whole memory by area (raw notes: 9,345 chars) |
| fixture, 1 / 3 / 5 questions | 2,269 / 3,762 / 6,950 chars, surgical | unchanged: the whole memory is printed only when it costs ≤ 1.2× the surgical output |
| bank, 326 questions: gold notes / numbers / chars per question | 0.888 / 0.969 / 1,984 | **0.897 / 0.972** / 1,988 (15 questions fixed, 8 regressed) |
| bank, routed (`MEMORY_WIDE=100`) | 0.885 / 0.958 | 0.888 / 0.962 |
| taste, 52 tasks: named prefs / implicit prefs / house rules / chars per task | 1.00 / 0.72 / 0.39 / 3,083 | 1.00 / **0.83** / 0.42 / 3,826 |
| "what is the current model in pricing?" (single-word project) | not scoped; two churn notes printed | scoped to `pricing/` |
| a note containing a NUL byte | invisible to `ask` (`grep -I`), no warning | found (`grep -a`), warning C9 |
| "what is the meaning of zxqv?" | an unrelated note headed like a hit | `(weak match: 'zxqv' found nowhere in memory …)` |

What changed:
1. **Complete mode** (F1). On a memory of ≤ 200 notes, `ask` renders the surgical answer and the whole memory (each
   question as `▸ path` pointers, then every note by area with its lineage header) and prints the whole memory when
   it costs ≤ 1.2× the surgical output. At 10 questions that is +14% characters for 30 instead of 24 notes, with
   lineage; it is 38% more than a bare `cat` of the notes, which has neither pointers nor SUPERSEDED marks.
2. **Folder scope on the question's own words** (F2): the stemmer had turned `pricing` into `pric`, so a plain-word
   project name never scoped. A first version scoped on every folder name and lost two bank questions ("… use in
   reporting?"): general areas are not scopes by word; `-p` still names them.
3. **`grep -a` and C9** (F3): a NUL byte made `grep -I` skip the note silently.
4. **Weak match** (F4): a question word found nowhere in the memory, the best note covering at most half of the
   question's words, no id, number or word pair matched, nothing named. A first version flagged "who owns
   cards.txn_daily?" because the word `owns` occurs nowhere; the strong-match veto fixed it. On the bank 5 questions
   were flagged before change 6, 4 of them genuine misses; 3 remain.
5. **Taste** (F7): a person named inside one of the three best-matching house notes (the deck's roster, the meeting)
   counts as named and brings their preferences (0.72 → 0.83 on implicit tasks); up to 12 notes with floor 0.15
   instead of 6 and 0.25 (+0.03 house rules, +24% characters).
6. **Hyphenated phrases also search as their words** ("call-routing" → call, routing; digits excluded): +0.9 pt gold
   notes, +0.3 pt numbers, +0.2% characters; a scoped folder's own words are not patterns.

Seen on the way, left for phase B: without an index every note's kind is "note", so the kind-based rule for general
areas (fewer than 80% work kinds) marks *every* area general, and the taste pool spans the whole memory. Prefix kinds
(F6) fix it. Not adopted after measuring: a recency tie-break for "current" questions (no change on 40 questions) and
a table of contents of the named project for scoped questions (+2.9k characters per question, covers 228 of 230).

# Round 4 — 100× (168,141 notes): what scales, what broke, what changed

## The world (`eval/scale/make_world.py`)
137 versions of each of the 41 projects: the originals plus 136 sibling copies whose project-local ids get
a code (fraud-2026 → fraud-xaa-2026, exp-014 → exp-xaa-014) and whose numbers all move (60 days → 62 days,
0.023 → 0.025). Shared tables and terms stay shared; general areas and the log stay 1× (one person, one set
of preferences). 168,141 notes, 124,294 entities. Copies carry their extraction through the same rewrite, so
they count as indexed. This is harder than real growth: siblings share titles and wording, so every
general word hits 137 projects.

## Saving a note costs the same (30 real Haiku calls, fraud-2026 re-indexed inside the 100× world)
| | 1,677 notes | 168,141 notes |
|---|---|---|
| KNOWN entities in the prompt, tokens (median / max) | 1,447 / 1,861 | 1,597 / 1,945 |
| tokens per note, in / out | 7.0k / 2.3k | 7.3k / 2.0k |
| **$ per note** | **0.0020** | **0.00187** |
| review call | $0.0026–0.0066 | $0.0040 (40 types) |

KNOWN is capped (80 project + 20 shared entities), so the prompt stops growing. A full re-index at 100×
would be ~$310 and ~37 h at -j 10; only a prompt or model change needs one.

## Answering at 100× (Opus agents, 3 batches × 10 questions, Haiku judge; per batch)
| | memory agent | grep agent | memory ÷ grep | (1,677 notes: memory ÷ grep) |
|---|---|---|---|---|
| answers (30 questions) | 24 / 6 / 0 | 24 / 6 / 0 | tie | 27/3/0 vs 26/4/0 |
| tool calls | 4.0 | 25.3 | 0.16 | 0.19 |
| tokens processed | 262k | 1,491k | 0.18 | 0.21 |
| cost units (Opus price ratios) | 116k | 286k | **0.41** | 0.47 |
| time | 76 s | 180 s | **0.42** | 0.35 |

Neither side's cost grew from 1,677 notes (memory 131k → 116k units, grep 279k → 286k): the questions name
a project or an id (P1), are general (P2), or come with the working project (C-orig: "you are working in
churn-2026"), and the grep agent narrowed to that folder too. Without a project, "what is the current
churn model?" has 137 right answers at 100×; `ask` says so ("N areas match about equally: name the project").

## Offline retrieval (326 bank questions, `eval/retrieval.py`)
| | gold notes | answer numbers | s per batch of 10 |
|---|---|---|---|
| 1,677 notes, grep everything | 0.882 (round 3: 0.878) | 0.970 | 0.5 |
| 1,677 notes, routed (`MEMORY_WIDE=100`) | 0.877 | 0.960 | 0.1 |
| 168,141 notes, routed | 0.852 | 0.949 | 5.8 |

## What broke at 100×, and the fix
1. **`ask` took 52–135 s per call.** One grep over 168k files took 37 s and printed 502k lines; turning each
   path back into a note path took 9 s more. Now, above `MEMORY_WIDE` (10,000) notes, each question greps
   only where it points: the project it names; else areas whose note ids and titles match (idf-weighted),
   the areas the index says mention its ids, and the general areas. One grep over everything is left only
   for ids the index does not know and nothing else places. → 5–8 s per call, 3.9 s of it loading graph.json.
   Up to 10,000 notes nothing changes.
2. **Scope leak (all sizes).** Entity boosts ignored the named project, so at 100× copies crowded the gold
   notes out. Boosts now stay inside the project or routed areas (1× gold-note recall 0.878 → 0.882).
3. **A widely shared id (holdout-2025q1) cancelled a precise one (fraud25-gbm-v2)** when choosing areas: now
   each id counts on its own.
4. **An edit before the next dream made `ask` rebuild the graph** (~90 s at 100×). Big memories now patch the
   last graph for changed notes: title, kind, date, `from:`/`supersedes:` (entities wait for the dream). A24.
5. **KNOWN sorted all 124k entities for every prompt.** Now one sort per wave (`Known`); a full re-index
   would otherwise have spent days sorting.

## Dream, ask and the viewer at 100×, fixed (`eval/scale/profile_dream.py`, `profile_incremental.py`)
| at 168,141 notes | before | now |
|---|---|---|
| dream, nothing new | 120 s, 8.2 GB | **3 s, 0.4 GB** (stops after the scan) |
| dream, 30 new notes (real Haiku; ~40 s of it are the calls) | 202 s, 8.2 GB | **82 s, 4.8 GB**; 137 area pages redrawn |
| $ per new note | 0.00187 | 0.00145 (same prompt; more of it cached) |
| `ask`, batch of 10 questions | 5–8 s (52–135 s before routing) | **2.3 s** on average (1.8–5 s) |
| offline retrieval, gold notes / numbers | 0.852 / 0.949 | 0.854 / 0.950 |
| viewer | one 372 MB page | 2.4 MB overview + one ~110 KB page per area |
| at 1,677 notes: dream / retrieval | 2 s / 0.882, 0.970 | 0.7 s / 0.882, 0.970 (unchanged) |

What changed:
1. **The dream's caches live in `_dream/store.db`** (SQLite, stdlib): parsed note facts by path and extractions by
   content hash. A dream re-reads only notes whose hash changed, instead of 168k notes and 168k cache files (75 s).
   The files in `_dream/notes/` stay the source: a row is used only while its file's mtime matches, so deleting an
   extraction file still forces a re-index.
2. **The graph is written to `_dream/index.db`**; `ask` on a big memory (`DbView`) loads every note row and reads
   entities, lineage and relations only for what a question touches. It gives the same answers as the in-memory
   graph (1,677 notes forced through it: 0.877 / 0.960 both ways).
3. **No graph.json past 10,000 notes**; `graph.html` is an overview of areas (map of the 120 best-linked, a filterable
   table of all, health with counts and the first 300 of each list) and `viz/<area>.html` one viewer per area,
   redrawn only when its notes, lineage, entity ids or relations change (`viz/_sig.json`). A first version fingerprinted
   entities by their spellings too: one new spelling of a hub entity redrew 3,568 pages; now 137.
4. **A dream with nothing new stops after the scan** (same hashes, same vocabulary, no review due, every extraction file
   present).
5. **After a vocabulary review only the entity half of the graph is rebuilt** (`notes_part` is reused); `fold` is
   memoized; dedup counts are taken only when `check` needs them; KNOWN is rebuilt every 10th wave on big memories.

Seen on the way: at 100× rare relation types pass the review threshold (3 uses) 137 times over, so 237 types queued
and the review, 40 per dream, took 4 dreams to clear; each of those dreams changed the vocabulary and redrew most pages.

Still heavy: a dream holds the whole graph in memory (4.8 GB peak at 168k notes); `_dream/` takes ~2.2 GB on disk at
100× (extraction files 670 MB, store.db 464 MB, index.db 384 MB, area pages 703 MB) against 657 MB of notes; the first
dream after this change fills store.db and draws every page (~100 s).

# Round 3 — refined: drop what didn't help, curate entities and the relation vocabulary

## What was dropped, and the evidence

In the 9 round-2 memory-agent runs (33 tool calls), agents used `memory.py ask` 9 times (once per
run), shell `cat` 20 times and shell `grep` 17 times. They used `where`, `trace`,
`memory.py grep`, INDEX.md and SKILL.md 0 times. So all of these went:

| dropped | why |
|---|---|
| `where`, `trace` | replaced by `ask` for answering, and by the viewer for browsing |
| `memory.py grep` | agents use native grep |
| INDEX.md | never read; `dream` now writes `_dream/graph.html` |
| gists (`--gists`), dreamer summaries | used by nothing |
| open relation vocabulary, and the review's "new type" answer | grew EDGES.md from 7 to 185 types |
| 300-entity KNOWN list | about 9k-token prompts; now this project's entities ≤ 80 plus shared ≤ 20 |

`memory.py`: 1,610 → 1,292 lines. Verbs: `ask`, `dream`, `viz`, `check`, `log`. A1–A20 were
rewritten for the refined design and all 20 pass. A20 now tests vocabulary and identity in place of
gists.

## How entities and the relation vocabulary are kept

- **Relations: a closed vocabulary of 8 types** in EDGES.md: uses, produces, part-of, trained-on,
  evaluated-on, measured-by, replaces, owned-by.
  - Each type has aliases (`~` = read in reverse), and there is a `drop:` list. Both were grown from
    the 508 type names Haiku actually wrote on the 56× bank.
  - The dreamer may use only these. Anything else is held back at merge and counted (C7).
  - A type used 3 or more times goes to the review, which may only answer `alias T`, `alias ~T` or
    `drop`. New types come from a human editing EDGES.md.
  - The review prompt names what to drop: claims (lifts, beats, improves), note-to-note links
    (answers, led-to, basis-for) and conversations (asked-by), and "when unsure, drop".
- **Entities: kept only when they mean something across notes.**
  - An entity is kept when it has a home note (a note whose slug is its id, e.g. the model's own
    note), is mentioned in 2 or more notes, or is named in ALIASES.md.
  - Files, notebooks, columns and note ids are not entities; grep finds them.
  - Ids fold `.`, `_`, `-`, spaces and case (`cards.txn_daily` = `cards-txn-daily`).
- **Dedup:** folding and the surface-form rule are free. Versions never merge. Two entities with
  different home notes are never queued for review. Other look-alikes are asked once, and the
  answer lands in ALIASES.md (`- a = b` or `not: a / b`).
- **Lineage stays separate:** `from:`, `supersedes:`, and note ids written in a body link notes with
  no model and no vocabulary.

## Effect on the 56× bank (same Haiku extractions; re-merged with 0 extraction calls)

| | before | after |
|---|---|---|
| relation types | 508 written, 185 in EDGES.md | 8 |
| relations in the graph | 4,559 | 3,166 |
| entities | 2,276 | 1,545 (941 tied to their home note) |
| entities that link nothing (one note, no home) | 873 | 0 |
| files and notebooks as entities | 51 | ~7 (name heuristics) |
| unknown types awaiting review | 323 | 0, after one review call ($0.0066): 3 mapped, the rest dropped |
| entity pairs awaiting review | 147 | 28 |

Retrieval is unchanged within noise. `ask` gold-note recall:
- small bank: 0.927 → 0.915
- 56×, indexed: 0.879 → 0.878
- 56×, no index: 0.892 → 0.892

Answer-number recall stays at 0.97. The agent-level results of round 2 still stand: the read path
(`ask`) is the same.

## What indexing costs (Haiku through `claude -p`, refined prompt, measured on 60 notes)

| per note | before refinement (56× bank) | refined, default effort | refined, `--effort low` |
|---|---|---|---|
| cost | $0.0035 | **$0.00133** | $0.00113 |
| input tokens, median | 14.8k | 5.9k | 6.0k |
| output tokens, median (incl. thinking) | 2,525 | 1,398 | 1,021 |
| seconds per call, median | 10.4 | 6.5 | 4.6 |
| `ask` gold-note / number recall, 46 questions | — | 0.866 / 0.958 | 0.866 / 0.958 |
| grounding drops (C4) | — | 1 | 7 |

- **Whole 56× bank:** about $2.2 and about 20 minutes at `-j 10`, against $5.95 and 45 minutes
  before. Low effort is about $1.9; retrieval is unchanged, but it makes more unsupported claims,
  which grounding drops.
- **Steady state:** only new or edited notes cost a call. Moves, renames, deletes and edits to
  EDGES.md or ALIASES.md cost 0.
- **Dedup** (folding, surface rule, home notes, versions, union-find) uses no model: 0.12 s for
  1,000 notes.
- **Review:** at most 1 call per `dream`, only when something is queued: $0.0007–$0.0066.
- **File mode instead:** one `memory-dreamer` subagent answered 30 prompts in 186 s (131k tokens).
- **Where input tokens go:** much of each call's input is Claude Code's own prompt. A direct API
  call would be smaller (not measured).

## What one memory costs to save and to keep (measured inside the full 1,677-note bank)

| operation | model calls | cost | time |
|---|---|---|---|
| agent writes a note | none (part of its own turn) | ~150 output tokens of the session's model (notes average ~100 tokens) | — |
| `dream` indexes a new or edited note | 1 Haiku call | **$0.0020** (7.0k in / 2.3k out); $0.0013 in a small memory | 9.9 s, parallel |
| move, rename, delete a note | 0 | $0 | — |
| edit EDGES.md or ALIASES.md | 0 | $0 | — |
| dedup merge, graph, viewer | 0 | $0 | ~0.1 s per 1,000 notes |
| vocabulary review (only when something is queued) | ≤ 1 per `dream` | $0.0026 (28 pairs + 1 type) to $0.0066 (30 pairs + 34 types) | 8–34 s |
| re-index everything (`--all`) | 1 per note | ~$3.3 for 1,677 notes | ~25 min at `-j 10` |

At 20 new notes a day that is about $0.04 a day: about $1 a month for indexing and review. The
known-entity list that prevents duplicate ids is about 1.4k of the ~7k input tokens, roughly 8% of
the per-note cost.

## What dedup did on the 56× bank (`memory.py check`, `eval/dedup_report.py`)

| stage | count | change |
|---|---|---|
| entity mentions extracted | 10,005 | |
| ids as written | 2,397 | |
| after spelling folding | 2,382 | 15 merged |
| after ALIASES.md lines from the review | 2,369 | 13 merged |
| after the surface-form rule | 2,267 | 102 merged |
| kept | 1,545 | 941 with a home note, 604 in 2+ notes |
| dropped by the keep rules | 722 | 684 one-note, 38 file-like |

The review also wrote 46 `not:` lines.

Merge quality, by hand:
- **Spelling folds:** 8 of 8 sampled are right.
- **Surface rule:** about 10 of 15 sampled are right. Others are lossy: `psi = feature-psi = score-psi`,
  `churn-rate = churn`, `recovery-rate = net-recovery`.
- **Review merges:** about 9 of 12 are right. One is wrong: `control-group = randomised-control`, a
  distinction the corrections notes depend on.

The free surface rule and the Haiku reviewer both merge more eagerly than "when unsure, keep apart"
allows. Neither affects answers much (`ask` greps text), but the merges show up as aliases and in
the viewer.

## Is the 8-type vocabulary enough? (`eval/type_coverage.py`, `eval/question_relations.py`)

- **What Haiku writes when free to invent** (5,196 relation instances on the 56× bank, old open
  prompt):
  - 81.2% fit the 8 types (74.6% directly, 6.6% through an alias);
  - 5.5% are deliberately dropped (claims, note-to-note links);
  - 13.3% are unknown, spread over 449 names. The largest covers only 16 instances (0.3%: `prefers`).
- **What the 366 questions need** (labelled by Haiku):
  - lineage: 133 (36%);
  - the answer sits in a single note: 127 (35%);
  - one of the 8 types: 105 (29%), of which uses 50 and evaluated-on 38;
  - other: 1.
- **Answers don't hinge on it:** `ask` without any index is as accurate.
- **Not proven:** one domain, and notes, questions and labels all came from Haiku.
- **So extending must be free:** the dreamer now names links outside the vocabulary in 1–3 words.
  They are kept aside in the cache, not shown. A type added to EDGES.md later picks them up at the
  next merge. Demo (`eval/add_type_demo.py`): adding `prefers` and `predicts` brought in 8 and 4
  relations with 0 model calls. A listed type now wins over the drop line.

# Round 2 — a thin layer on grep, tested at 1× and 56×

## Verdict

Every target holds at both sizes. Fresh Opus subagents using the memory are at least as accurate
as a grep-only baseline. They cost less: 0.93× at 30 notes and 0.39–0.47× at 1,677 notes. And they
are faster: 0.75× at 30 notes and 0.35–0.44× at 1,677. Each cell is three runs of 10 questions,
judged by Haiku against reference answers.

| cell | correct / partial / wrong | tool calls | API requests | tokens processed | cost vs grep | time |
|---|---|---|---|---|---|---|
| small (30 notes) — memory | 26 / 3 / 1 | 1.3 | 2.3 | 104k | **0.93×** | 40 s |
| small — grep | 25 / 5 / 0 | 2.7 | 3.0 | 129k | 1× | 53 s |
| 56× (1,677 notes) — memory, Haiku index | **27** / 3 / 0 | 4.7 | 5.7 | 311k | **0.47×** | 61 s |
| 56× — memory, no LLM index | 26 / 4 / 0 | 5.0 | 6.0 | 324k | **0.39×** | 75 s |
| 56× — grep | 26 / 4 / 0 | 25.3 | 23.3 | 1,465k | 1× | 172 s |

Cost compares "cost units" per run: tokens weighted by Opus price ratios (fresh input 1, cache read
0.1, cache write 1.25, output 5). Data: `eval/agent/summary.json`; answers in `eval/agent/runs/`;
verdicts in `eval/agent/judge-*.json`.

## Why round 1 cost 2.3×

It was round trips, not note size. Every API request re-sends the subagent's context: at least 37k
tokens of system prompt, tools and history. Round 1's SKILL.md told agents to look up, then read
each pointer, one question at a time. That loop took 16–20 requests where grep took 3.

At 30 notes the whole corpus is about 3k tokens. INDEX.md alone was 70% of the corpus, so it
compressed nothing, and one `cat` of everything was the cheapest possible plan.
(`eval/a21/calls.py` lists every call of every run.)

## What changed: grep plus memory, not a replacement for grep

- `memory.py ask "q1" "q2" …` takes every question in one call:
  - The graph expands each question into grep patterns: note ids, entity aliases, and the project
    named in the question, which then scopes the search.
  - One real `grep -F` pass finds the lines.
  - Notes are scored by idf-weighted pattern hits; a hit on the title or in the slug counts double.
  - Then the graph orders them. Named notes come first. Superseded notes lift their successors.
    "What came of X" walks down the `from:` links; "what led to X", "why" and "depends on" walk two
    hops up. For "why" questions about a replaced note, the walk goes up from its successor.
  - Output is `line: text` under `▸ path · kind · date · from … · SUPERSEDED → newer`, i.e.
    surgical lines from the original files. When everything relevant fits the budget (small
    memories), it prints whole notes instead.
- `memory.py grep <grep args>`: plain grep over the notes, with the same headers per note.
- Lineage without a model: a slug-like note id written in a note's body counts as a `refs` link
  within its project. Log notes take their date from the `log/YYYY-MM-DD` filename.
- SKILL.md policy: one `ask` call with every question, answer, and at most one batched follow-up.
  The skill description, which agents see without loading the skill, names the command, so the
  skill body never has to be read just to answer.

## The 56× bank (written by 12 Haiku subagents)

- **Projects:** 40, each with 30 notes in real chains: question → experiments → findings →
  decisions → new versions, with at least 2 supersessions per project.
- **General memory:** 300 notes across `prefs/` (people's taste and working preferences),
  `reporting/` (conventions), `glossary/` (terms), `corrections/` (wrong definitions or
  understandings, each superseding what it corrects), `howto/` (analysis practice) and `qa/`
  (saved question-and-answer notes).
- **Size:** 1,499 notes plus 149 log days. Adding the churn-2026 fixture gives 1,677 files and
  653 KB, about 190k tokens.
- **Questions:** 326, each with gold notes, written by the same authors. Plus 30 more churn-2026
  questions from a 13th agent.
- **Validation** (`eval/bank/split.py`): 0 notes over 40 lines, 0 without a title, 1 of 2,190
  `from:` links unresolved, 0 of 209 `supersedes:` links unresolved.

## Offline retrieval (no LLM): did the answer's evidence come back?

| bank | questions | gold-note recall | answer-number recall | chars per question |
|---|---|---|---|---|
| small, Haiku index | 40 | 0.93 | 0.97 | 1,200 |
| 56×, no index | 326 | 0.89 | 0.97 | 1,975 |
| 56×, Haiku index | 326 | 0.88 | 0.97 | 2,210 |

`python3 eval/retrieval.py <memory root> <questions…>`. Weakest types are "current" (26 of 40
miss at least one gold note or number) and "dependency" (21 of 40); some of those are strict gold
lists (the gold names the superseded version too).

## Is the Haiku index worth it? For retrieval, no; for management, yes

- **Cost:** indexing 1,677 notes took 1,677 calls plus 1 review call, $5.95 and about 45 minutes
  at `-j 10`. The KNOWN entity list makes each prompt about 9k tokens.
- **Retrieval value:** neutral. The index's loose entity names made `ask` worse (gold-note recall
  0.86 vs 0.88), so `ask` now uses the index conservatively:
  - aliases expand only through short names;
  - entities are matched by name, not by long descriptions;
  - the boost is smaller for phrase matches.

  With that, indexed and unindexed are within noise offline and at agent level (27 vs 26 correct).
  The indexed agent runs used the ranking from just before the last why/current tweak, which is
  worth +0.8 pt offline.
- **Where it pays:** entity aliases and typed relations ("what uses `cards.txn_daily`" across 27
  projects), the viewer, and review.
- **Problem found:** with Haiku as reviewer, all 178 proposed relation types with 2 or more uses
  were answered "new". EDGES.md grew from 7 types to 185, and 470 vocabulary items still await
  review (C7). The review needs a stricter prompt or a cap.

## Viewer (for visualization and management)

`memory.py viz` writes `memory/_dream/graph.html`, self-contained with no CDN and built to the
html-harness habits (10/10 under `map.py`). It has three tabs:
- **Overview:** every project and area with note counts by kind, last update, superseded and
  warning counts.
- **Explore:** search plus a radial neighbourhood for a note (built on, built upon by, supersedes,
  entities) or an entity (depends on, used by, mentioned in), and a detail panel with the note text
  and links.
- **Health:** warnings by code, all 211 superseded → current chains, unlinked notes, and the review
  queue.

Deep links: `#note=<path>`, `#entity=<id>`, `#health`. It renders with 0 errors and 0 AA contrast
failures in light and dark mode. Screenshots are in `eval/viz/`.

## Caveats

- The judge is Haiku, with n = 30 questions per cell, so a one-question difference is noise.
  Several "partial" verdicts say "substantively correct".
- Each run answers 10 questions in one session, which lets grep spread its reads across questions.
  One fresh agent per question would favour the one-call design more; that was not measured.
- The questions were written by Haiku. Churn-2026 questions written for the small bank are
  ambiguous in the big one ("the current churn model" could be churn-2025's).
- `memory.py` is 1,610 lines against the spec's ~600.

## Next refinements

1. Make the dreamer optional for answering and keep it for aliases, relations and the viewer.
   Cap the KNOWN list per project, which should roughly halve indexing cost.
2. Gate the vocabulary review: accept a new type only with a definition distinct from every
   existing type, and cap new types per review.
3. Run single-question agents, and use a stronger judge.
4. Improve "current" and "dependency" retrieval: follow the successor's relations, not only its
   lineage.
5. Test the write path: agents writing notes under the SKILL rules.

# Round 1 — the spec as written

## Verdict

The tool works to spec: **A1–A20 pass** with a deterministic fake dreamer. A3, A10 and A18 also pass
with real Haiku, both in command mode and through a `memory-dreamer` subagent. **A21 is mixed.**
Fresh Opus subagents using the memory answered 30/30 questions correctly, against 28/30 for a grep
baseline. But on this 30-note fixture the memory runs cost about 2.3× more than the baseline, so A21's
"the index must cost less than the baseline" **fails at fixture scale**. Whole corpus: 9.4 KB.
INDEX.md alone: 7.5 KB. At that size grep agents simply `cat` every note in one call.

## Acceptance (spec §13)

| id | result | evidence |
|---|---|---|
| A1 | pass | empty `memory/` → INDEX.md, graph.json, EDGES seed, ALIASES header; exit 0 |
| A2 | pass | no model: 26 lineage edges exactly as written, both supersessions, `trace` on notes, `where` from titles + grep; C5 = 30 |
| A3 | pass (fake + **real Haiku**) | Haiku: 30 notes → 30 calls, $0.0452, 60 s at `-j 6`; second `dream` 0 calls |
| A4 | pass | 5 moved + 2 renamed: 0 calls, "7 moved", no C2, `from: exp-014` resolves to the renamed note; graph identical modulo paths |
| A5 | pass | edited note drops out of entities/relations immediately, listed under `unindexed`; next `dream` = exactly 1 call |
| A6 | pass | deleted dec-risk-tiers (named by 2 `from:`): nothing derived from it remains, `offers.tier_matrix` gone, 2 headlines moved, C2 ×2, 0 calls |
| A7 | pass | revert → cached extraction reused, 0 calls |
| A8 | pass | fabricated `as`, absent quote, ungrounded number → all dropped, C4 = 3, summary → title |
| A9 | pass | prose- and fence-wrapped answers parsed; invalid JSON → 1 retry → C3 |
| A10 | pass (fake + **real subagent**) | Haiku subagent answered 30/30 prompts, 0 failures, C4 = 0; forced review round answered and applied (`snapshot-of` → new type) |
| A11 | pass | uses / trained-on / evaluated-on / owned-by with valid `path:line` evidence; `trace cards.txn_daily --down` lists v2, v3, utilization, churn-xgb-v2/v3 |
| A12 | pass | `fitted-on?` ×2 live; review → `alias trained-on` appended to EDGES.md; relabelled with 0 extraction calls |
| A13 | pass | "the txn table feeds the velocity features" → `feat-velocity-v2 uses cards.txn_daily` (txn-backfill.md:6) |
| A14 | pass | hand-folding trained-on into uses relabels everything, 0 calls |
| A15 | pass | `Cards.TXN_daily` and `txn-table` merge free; v2/v3 (both "velocity features") never asked; risk-tier pair asked once → ALIASES.md; next `dream` asks nothing |
| A16 | pass | `- cards.txn_daily = ds-txn` moves relations and pointers, 0 calls |
| A17 | pass | `where feat-velocity-v2` headline = post-period-leak; after deleting it → feat-velocity-v3 (§5.1 order), 0 calls |
| A18 | pass (**real Haiku**) | command mode 21 ids / 20 true entities = **1.05×**; subagent file mode 20 / 19 = **1.05×** (target ≤ 1.2×); review merged nothing further |
| A19 | pass | 1,000 notes / 1,900 entities / 2,900 relations: merge 0.12 s, `where` 0.06 s (0.17 s after an edit forces a re-merge), review candidates for 200 new ids 0.35 s |
| A20 | pass | 14 gists (entities in ≥ 3 notes), ungrounded numbers dropped, `key` filtered to real notes, rerun 0 calls, deleting a cited note hides the gist |
| A21 | **mixed** | accuracy ✓ (30/30 vs 28/30); cost ✗ at 30 notes (see below) |

Rerun: `python3 tests/acceptance.py` (≈ 10 s); real-model steps in RUNBOOK.md.

## Real dreamer runs

| | command mode (`claude -p --model haiku --tools ""`, isolated) | file mode (`memory-dreamer` subagent, Haiku) |
|---|---|---|
| work | 30 calls + 1 review call | round 1: 30 prompts in one agent (92 tool calls, 131k tokens, 186 s); round 2: review (5 tool calls, 41k tokens) |
| cost | $0.0452 extraction + $0.0009 review (≈ 4.4k in / 2k out per call incl. thinking) | not priced by the harness; token count above |
| grounding drops (C4) | 2 (a `churn-2026` entity not in the note, one quote) | 0 |
| entities / relations | 58 / 69 | 39 / 37 |
| proposed types | 14 single-use (C7 ×14); 2 with ≥ 2 uses → review → `has-metric`, `implemented-by` as new | 1 (`snapshot-of`) → new |
| A18 | 1.05× (split: `recall@10` / `recall-at-k`) | 1.05× (split: `cards-txn-daily` / `txn-table`) |

One agent answering every prompt keeps ids consistent across notes without the KNOWN list doing
anything. It also extracts fewer junk entities. Command mode calls are independent and cheaper per
note, but noisier.

## A21 — fresh Opus subagents, 10 questions, n = 3

Each run: one fresh Opus subagent answering all 10 questions. Memory runs got the Haiku-indexed
memory plus SKILL.md. Grep runs got the same 30 notes and a one-paragraph description of the note
format. Answers: `eval/a21/runs/`. Grading against key facts: `eval/a21/grade.py`. Numbers:
`eval/a21/summary.json`.

| per run (mean of 3) | memory | grep baseline | ratio |
|---|---|---|---|
| questions fully correct | **10.0** (30/30) | 9.3 (28/30) | |
| tool calls | 19.3 | 2.3 | 8.4× |
| API requests | 18.3 | 3.0 | |
| tokens, harness-reported | 67.2k | 51.8k | 1.3× |
| tokens processed, all requests (≈ 96% cache reads) | 960k | 130k | 7.4× |
| cost units (Opus price weights) | 222k | 97k | **2.3×** |
| wall time | 141 s | 66 s | 2.1× |

Per question: memory ≈ 1.9 tool calls and 22k cost units; grep ≈ 0.2 tool calls and 9.7k.

The two grep partials: grep-2's Q2 omits the velocity-v3 rebuild. grep-1 says "the v3 rebuild",
which the regex misses, so it is arguably correct. All six runs had the same headline facts. They
also flagged the same gaps in the notes (no v3 tenure split, the unexplained 0.74→0.76 gap, the
October backfill).

Why the index lost:
- The grep agents ran `cat` over every note once and answered all 10 questions from that.
- The memory agents followed SKILL.md literally, one question at a time: read the INDEX head, `where`
  or `trace`, then read the notes it pointed to. That loop meant 16–24 turns, and every turn re-reads
  a ~50k context.
- Design caveat: one session per run lets the baseline spread its single read over all 10 questions.
  Ten one-question agents per run would hurt grep more. A corpus big enough that `cat` stops being an
  option (hundreds of notes) is where the index should win. **Neither variant was run.**

## Deviations from the spec

1. **`memory-dreamer` cannot list files.** This Claude Code build has no Glob tool, and Read does not
   list directories. The spec'd agent (Read, Write, Glob) wrote nothing on its first try. Fix:
   `dream` now writes `_dream/pending/TODO.md` with every unanswered prompt path, and the agent text
   says to read it. Glob stays in `tools:` for builds that have it.
2. **`memory.py` is 1,261 lines** against "≤ ~600". Everything in §4–§8 is implemented in one stdlib
   file: grounding, both vocabularies, review, gists, file and command mode, move detection,
   freshness. It is not compacted.
3. **`check_skills.py` is not on this machine** (or in the email), so R9/R10/R12/R15 are unverified.
   What was checked by hand: SKILL.md is 25 lines with `name` and `description` frontmatter; the
   subagent lives in `agents/`; nothing hook-dependent.
4. Small choices the spec leaves open:
   - command mode runs calls in waves of `-j` and refreshes KNOWN between waves (no extra calls)
   - `trace -e` forces an entity walk when a note has the same name
   - C4 counts dropped items, not notes
   - a C3 note is retried at the next `dream`
   - `where` prefers a body line over a frontmatter line as the pointer

## What to change next

- **SKILL.md read loop.** For small memories, tell the main agent to read the INDEX body and `cat`
  the project's notes in one call. Or give `where` an option that prints the pointed lines inline, so
  "read what it points to" is not one call per note.
- **Extraction noise.** 37 of command-mode Haiku's 58 entities are columns, notebooks, code files,
  project or note ids. Tell the prompt "not columns, files or notebooks". Or drop entities whose id
  equals a note stem (`exp-014`, `ds-txn-2025q4`).
- **Proposed-type sprawl.** Single-use types never reach the review (gate ≥ 2) and sit in C7
  forever. Consider sending them after N days, or listing them in the review prompt as a batch.
- **Headline signal.** "Named on the title line" dominates. With Haiku's loose surface forms ("30-day
  velocity"), exp-014, not post-period-leak, became the headline of `feat-velocity-v2`.
- **Re-run A21 at scale** (≈ 300 notes, several projects) before judging the index on cost.
