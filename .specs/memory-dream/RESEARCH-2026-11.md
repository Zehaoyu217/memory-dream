# memory-dream — materials collected for the v0.5 plan (2026-11-11)

What was read before `PLAN.md` was written: two outside systems (SAG2, OpenViking), one of the owner's own (a
private claims base), and our own graph looked at with plain graph methods. Each claim about an outside system is marked
`[code]` (read in its source), `[docs]` (its own documentation or release notes) or `[inferred]`. Nothing from either
outside repository was run.

## 1. SAG2 (Zleap AI)

Identification, about 95% sure: "SAG2: Embedding-Free Multi-Hop Retrieval with BM25 and JEV" (arXiv:2610.22588,
2026-10-15), the successor of Zleap-AI/SAG ("SQL-Retrieval Augmented Generation", arXiv:2606.15971, now called SAG1).
It exists as reference code (`Zleap-AI/SAG-Benchmark`), the package `zleap-sag2` 0.4.0 (2026-11-03), the desktop app
and CLI `Zleap-AI/SAG-Wiki` v0.2.9 (2026-11-11) and an unmerged branch of `Zleap-AI/SAG`. All MIT. No other project
of that name was found in this field.

- It is not a knowledge graph or a memory system: no entities, relations, types, events or embeddings, only the
  original passages and a positional inverted index (SQLite by default). `[code]`
- Ingest makes no model call. `[code]`
- A question: BM25 top 100 → a hosted, closed "decision model" scores each passage as necessary evidence → the best
  ten donate rare terms and name phrases → BM25 per term, interleaved → judged again with context; two rounds; the
  top ten reordered for diversity. `[code]`
- The authors report recall@10 of 86.6 (MuSiQue), 97.4 (2Wiki) and 99.0 (HotpotQA) on 1,000-question subsets.
  Caveats: MuSiQue was used in development, baselines are cited rather than re-run, recall only, and no independent
  replication was found. `[docs]`
- Per question: about three requests, 331 judgments, 83 to 103 thousand input tokens, about $0.0043; no fallback if
  the judge fails. The accuracy rests on the closed judge: open rerankers in the same pipeline reach 72 to 74 on
  MuSiQue, and the same judgments spent on plain BM25 give 69.8. `[code][docs]`
- SAG-Wiki adds notes whose citations are anchored by file hash, byte range, lines and quoted text and re-verified
  locally (intact, moved, changed, missing). Its "Explore" graph is TF-IDF similarity only. It skips YAML
  frontmatter. `[code]`
- SAG1, the graph-like predecessor: one model-extracted event per chunk plus entities from a closed type list,
  bipartite, identity = the lower-cased name, no links between entities. The team's own review shipped in the
  package calls its disambiguation broken. `[code]`
- `zleap-sag2` needs Python 3.11 and eleven third-party packages; its source repository is private. `[docs]`

Not verified: nothing was run; the paper was read through a summary whose tables match the repository's result
files; the judge model's internals and pricing; no independent benchmark.

## 2. OpenViking (Volcengine, ByteDance)

`volcengine/OpenViking`, read at `main` 12b188a (2026-11-11); v0.5.4.1 released the same day; 74 releases since
2026-02-05; still marked Alpha.

- **Licence: AGPL-3.0** since 2026-03-30 (it was Apache-2.0), with a README clause against wholesale rewriting or
  porting. `[code][docs]`
- **A server is mandatory.** The embedded clients were removed in v0.4.14; it needs an embedding model and an LLM;
  the vector engine is bundled; about sixty runtime packages. `[code][docs]`
- **There is no graph engine, graph index or graph retrieval.** "Knowledge Graph" is an example skill for
  `ov compile`: a 224-line prompt driving a model map / shuffle / reduce pipeline that writes `entities/<id>.md`
  (`type, id, title, entity_type, description, aliases, sources`) and one `relations.jsonl`
  (`{from, relation, label, to, evidence[]}`), plus a standard-library validator and viewer script. Evidence is a
  source URI: no line, no quote. It landed 2026-08-20 and was taken out of the packaged skills on 2026-10-29. `[code][docs]`
- Typing, predicates, alias merging and de-duplication are instructions in the prompt; no registry, ontology or
  gate exists in code. `[code]`
- The original relations between contexts were deleted in v0.4.16 because nothing consumed them; memory-to-memory
  links are off by default and not read by retrieval. `[code][docs]`
- Directory-recursive retrieval was removed in v0.4.23 (2026-10-02): now one global vector search per question and
  an optional rerank; the retrieval-trace types are dead code. `[code][docs]`
- Memory extraction: one model call over the session and five prefetched memories, then model merges per type;
  identity is the file path; provenance is a run id and a per-commit diff file; no approval step. `[code]`
- Open user issues of 2026-11-09 report the graph compile stopping near 400 to 500 edges and marking partial graphs
  complete; single-user reports, unanswered. `[docs]`

Not verified: nothing was run; the reasons for removing recursive retrieval and un-packaging the graph skill are
unpublished; hosted-service features are unknown; its benchmark figures predate the retrieval rewrite.

## 3. The claims base (a separate, private project of the owner's)

Its mechanisms are described here in our own words; none of its code or text is reproduced. It holds documents as
**claims**, groups claims into **concepts** by recorded **membership**, and has neither a graph nor a taxonomy:
this project has those two halves and lacks its two. Neither SAG nor OpenViking figures in it.

- **A claim** is one self-contained sentence plus the verbatim span of the document it rests on. Its identity is a
  hash of its content. Whether it is grounded is decided by code, not by a model: the quote must be found in the
  document, its numbers must match, it may not add a negation, and it must cover enough of the sentence. A claim that
  fails is kept with the reason and never served. What is stored is the document's own text at the span, not the
  model's rendering. Whether a claim is current is computed, never stored.
- **A concept is a contract**: a name, a definition that says what belongs and then what does not, a handful of
  anchors (members that fix the boundary from inside) and a few excludes (near-misses that look related and do not
  belong).
- **Membership** is a recorded verdict of claim × concept × contract version: in or out, from an anchor, a judging
  model or a person, with a one-line reason. The judge decides against the definition as written; a passing mention
  is out; an ambiguous case is out. A person's verdict outranks the judge's and survives a new version of the
  contract. No similarity threshold decides anything: similarity only proposes candidates.
- **Split and merge** follow fixed rules. A split proposes groups from the members, gives each child its own anchors
  and the other groups' nearest members as excludes, and leaves applying it to a person. A merge takes the union of
  the anchors, redrafts the contract, judges membership afresh and retires the sources. Nothing is deleted.
- **A conflict is a record of a detection, not a verdict**, with the states open, resolved by supersession, resolved
  by conditions (the two hold under different conditions) and dismissed (by whom and why). Open is a valid end: two
  sources disagreeing is a fact to surface, not a contest to settle. Supersession is a different thing: the same
  source saying the same thing better.
- **Upkeep is a budgeted pass**: free steps always, paid steps within a budget, a dry run that prints the cost first.
  A separate doctor answers a fixed list of invariants pass, fail or could-not-check, with no model.
- **Decisions are append-only**, each with the evidence it rested on, so that it can be re-opened when the evidence
  changes.
- It deliberately has no typed links, no taxonomy, no confidence score and no automatic de-duplication of concepts.

**What the plan takes**: truth and meaning on separate planes; the contract with its "not" and its near-misses;
membership as recorded verdicts with a precedence; no threshold decides; grounded-or-rejected with reason codes; the
conflict record that is not a verdict; nothing deleted on split or merge; the budgeted upkeep pass and the doctor;
the append-only decision record. **What it does not take**: embeddings as the way to propose candidates (ours are
names and graph neighbours; embeddings stay a plug-in), and the refusal of typed links (our links are the graph).

## 4. Our own graph, looked at as a graph

`python3 eval/graph_probe.py <memory> --conflicts eval/real/bank-index/CONFLICTS.md` on the indexed bank: 1,677
notes, 3,733 lineage edges, 1,325 things, 3,119 links. Standard library, no model, a few seconds.

| question | answer on the bank |
|---|---|
| how much of the vocabulary is settled? | 14 link types carry 2,528 links (81%); 493 raw link words carry 591 (426 words used once). 31 thing types carry 1,239 things; 62 raw words carry 86. The commonest raw thing words are `log-tag` and `project-tag` |
| are there loops where none can be? | 27 in links: 6 pairs that each `replaces` the other, 16 `uses` loops (11 of them two things pointing at each other), 3 `owned-by`, 2 `measured-by`; none in `evaluated-on`, `part-of`, `trained-on`, `produces`. 6 loops of `from:` between notes, holding 13 notes |
| is one name used for several things? | 83 things are mentioned in 5 or more areas; 44 of them have no note of their own. `holdout-2025q4` is one thing mentioned by 95 notes in 17 areas whose own note belongs to one project. `auc`: 232 notes, 30 areas, no note of its own |
| how connected is it? | 121 components; one holds 1,187 of the 1,325 things; 108 things have no link. 295 bridges, 245 resting on one line of evidence |
| do link types overlap? | 126 pairs of things are joined by two link words at once: `trained-on` with `uses` ×5, `evaluated-on` with `uses` ×5, `evaluated-on` with `trained-on` ×4 |
| what does a kind of thing usually carry? | 88% of models are measured by a metric and 74% are evaluated on a dataset; 89% and 73% for experiments; 79% of features are used by a model. 22 roles are shared by 3+ things across 3+ areas (28 features with "used by a model, uses a dataset") |
| do things with the same neighbours name the same thing? | 17 pairs of one family share most of their typed neighbours; none is name-alike, and by inspection they are siblings (two features of one model), not duplicates |
| are partial graphs ever exactly equal? | after two rounds of Weisfeiler–Lehman colouring, 24 of 1,217 linked things (2%) have exactly the same surroundings as another |
| do shared things reveal a conflict? | of the 73 pairs a review judged, 5 were supersessions (7%). Keeping pairs whose notes share 40% of their things keeps 2 of the 5 and 6 of the 68 compatible ones (25%); at 20%, 3 and 26 (10%) |

What follows from it. The cheapest methods pay first: loops and declared link algebra are exact and free. Hubs that
span areas without a definition are where identity is most at risk, so that is where contracts go first. Exact
equivalence of partial graphs is too strict for real notes: combining equivalent parts means approximate, seeded
alignment, and matters between graphs rather than inside one. Things alike in structure are usually siblings: good
near-misses for each other's contracts, bad merge candidates. Shared things order a conflict queue; they do not
decide it.

## 5. Side by side

| | memory-dream v0.4 | SAG2 | OpenViking | the claims base |
|---|---|---|---|---|
| unit of truth | a note (one claim) | a passage of the original | a file under `viking://`; merged memory cards | a claim: a sentence and its verbatim span |
| evidence | note path and line; quote for links | file hash, byte range, lines, quote (in its app) | a source URI | the document's text at a span, checked by code |
| things and links | extracted once per note, raw words kept | none | written by a model from a prompt | none (concepts only) |
| vocabulary | registries with a bar, a budget, probation | none | free text in a prompt | none |
| identity | folded id, aliases, same/different on pairs | n/a | the file path | a contract, anchors, excludes, verdicts |
| conflicts | candidate pairs; `>`, compatible, `?` | none | inline records on compiled pages | a detection record with states |
| retrieval | grep first, lineage, graph walk | BM25, a closed judge, term expansion | one vector search, optional rerank | KNN and full text |
| needs | Python standard library, grep | a paid remote judge; 11 packages or a binary | a server, two models, ~60 packages | embeddings, a judge model |
| licence | MIT | MIT | AGPL-3.0 | private |

## 6. Sources

SAG2: arxiv.org/abs/2610.22588 · arxiv.org/abs/2606.15971 · github.com/Zleap-AI/SAG · github.com/Zleap-AI/SAG-Benchmark ·
github.com/Zleap-AI/SAG-Wiki · pypi.org/project/zleap-sag2. OpenViking: github.com/volcengine/OpenViking (source,
release notes, pull requests, issues, docs). Both were read on 2026-11-11 from shallow clones and package archives;
the investigators' full reports, with file paths for every `[code]` claim, are kept outside this repository.
