# ADR-001: Hosting memory-dream as a service; git stays the truth; the store is a configuration choice

**Status:** Proposed (needs the owner's sign-off)
**Date:** 2026-11-01, updated 2026-11-02
**Deciders:** the repository owner

## Context

memory-dream is files in a repository: notes are the truth, `ask` is one grep over them ordered by lineage, and the
index (entities, typed relations, conflicts, checks) is derived, disposable and rebuilt by `dream`. The question is
what changes when it has to run for many people as a hosted service, and whether that service should keep the index
in a graph database.

Measured facts that shape the answer (RESULTS.md and the re-evaluation of 2026-11-01):

- The graph is already a property graph with a versioned contract (CONTRACT.md, schema 1): Note and Entity nodes,
  lineage edges `from`, `supersedes`, `refs`, mentions with line numbers, typed relations with evidence, conflicts.
- Everything stored goes through one seam: one writer of eight SQLite tables (36 lines) and one row reader that
  `ask` uses through seven calls (64 lines). No other SQL exists in the script.
- What the graph contributes to answering today: alias expansion of the question's names, lineage headers and
  SUPERSEDED chains, one summary line of an entity's typed relations, a boost for notes that mention a named
  entity, and routing to areas on big memories. It does not follow typed relations to pull in the notes of related
  things. Its measured worth for answers is +0.8 points of gold-note recall and +6.4 on alias questions; answering
  works without it.
- Sizes: 1,677 notes give 3,678 lineage edges, about 900 entities and 2,700 relations; 168,141 notes give 124,000
  entities and a 384 MB index. Queries are one or two hops by design, plus supersession chains of at most four.
- The viewer is one self-contained page fed by an embedded JSON island; the dream holds the whole graph in memory
  (4.8 GB at 168,141 notes); one lock file serialises dreams on one machine.

Constraints: the skill must stay standard-library Python so any agent with a shell can use it; notes must stay
readable and editable as files; nothing in the read path may call a model.

## Decision

1. **Git stays the truth.** The service mirrors repositories: it checks out each one on push, runs the existing CLI
   (`dream`, `viz`, `ask`), and serves answers, the viewer and the warnings. Notes are never written by the service.
2. **The store is a configuration choice behind the existing seam.** `memory.py` publishes the graph to a store named
   by `MEMORY_STORE` after every dream and reads rows from it in `ask` when one is named; SQLite files remain the
   default and need nothing. `stores.py` carries the backends (PostgreSQL first, Neo4j second) and a CSV + Cypher
   export for any graph database. Publishing is a diff keyed by content hash, under a per-repository lock, and a
   schema mismatch republishes everything.
3. **PostgreSQL is the default hosted store; a graph database is opt-in.** The data and the queries do not need a
   graph engine; a graph database is chosen when a people-facing explorer or ad-hoc Cypher is the point.
4. **A service, if ever built, is a separate package** with its own dependencies; the skill's rule stands. The owner
   decided on 2026-11-02 not to build it now; the store seam is what ships.

## Options Considered

### Option A: files only, as today
| Dimension | Assessment |
|---|---|
| Complexity | Low |
| Cost | None |
| Scalability | one machine, one writer; 168k notes measured |
| Team familiarity | High |

**Pros:** no infrastructure; the memory travels with the repository; works offline and in cloud sessions.
**Cons:** no shared view across machines; no concurrency; no API; the viewer is per checkout.

### Option B: git mirror + PostgreSQL (chosen default)
| Dimension | Assessment |
|---|---|
| Complexity | Medium |
| Cost | one managed database |
| Scalability | rows are small; the largest measured world is 384 MB; recursive CTEs cover chains |
| Team familiarity | High |

**Pros:** one database for the index, jobs, keys, metrics and full-text search if ever wanted; mature operations;
the diff publish keeps it current in seconds.
**Cons:** no visual graph explorer out of the box; typed relations are rows, not edges, for ad-hoc exploration.

### Option C: git mirror + graph database (Neo4j, Memgraph, Neptune) — opt-in
| Dimension | Assessment |
|---|---|
| Complexity | Medium to High |
| Cost | a graph service or cluster |
| Scalability | ample for these sizes |
| Team familiarity | Medium |

**Pros:** supersession chains and "what depends on X" as path queries; Bloom-style exploration; the published shape is
already a property graph.
**Cons:** a second system beside whatever holds jobs and keys; the read path gains nothing for answers unless retrieval
is also rewritten; Enterprise-only features (composite node keys) must be avoided for portability.

### Option D: the database is the truth (notes live in the database)
Rejected. It discards append-only history in git, offline use, the delete-and-rebuild guarantee and portability, and
it needs an editor, auth and an audit trail before it is as safe as a file in a pull request.

## Trade-off Analysis

The index migration is small because the seam is small and the data is already graph-shaped; it is deliberately
reversible. The service is the real project: concurrency, tenancy, cost caps on model calls and an API for the
viewer are new code regardless of the store. The read path is grep over files; moving retrieval into any store means
reimplementing ranking and proving parity with the eval harness, which is a separate decision with its own
measurement, not a side effect of hosting.

## Consequences

- Easier: one dashboard for many repositories; one place to see what may be wrong; ad-hoc queries over the index;
  explorers that query instead of loading a page.
- Harder: two places where the index can be stale (the checkout and the store), handled by publishing in the same
  job as the dream; secrets and keys to manage; model cost to cap per repository.
- To revisit: whether retrieval should use typed relations (follow `uses`, `owned-by` to the notes of related
  things); it needs a real index of the bank to measure, about $4 of Haiku calls.

## Action Items
1. [x] `stores.py`: PostgreSQL backend with diff publish, advisory lock, schema check (tested, `tests/store_parity.py`);
       Neo4j backend written against the 5.x driver (not run against a server here); CSV + Cypher export; `memory.py export`.
2. [x] `MEMORY_STORE` wiring in `memory.py`: publish after every dream (and when a dream has nothing new but the store is
       behind), read rows in `ask`, a status line in `check`; the SQLite path is unchanged and remains the default.
3. [x] Parity test: identical `ask` output and an identical graph through the SQLite view and the PostgreSQL store; a
       second dream publishes nothing; an edit, a deletion and a version mismatch behave as specified.
4. [ ] The service itself (mirror worker, queue per repository, API, viewer as a client): not built, by the owner's
       decision on 2026-11-02; a skeleton exists outside the repository if it is ever wanted.
5. [ ] Run the Neo4j backend against a server and record the result here.
6. [x] Measured on a real index ($2.72; RESULTS phase I): one hop lands on notes `from:` lineage already heads; two hops for
       input questions take dependency questions from 0.853 to 0.920 of gold notes for +4.6% characters, kept as the default.
       The readings are in `eval/real/bank-index/` and rebuild the index with no model call.
