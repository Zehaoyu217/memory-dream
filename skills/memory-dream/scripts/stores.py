#!/usr/bin/env python3
"""memory-dream stores (ADR-001): the graph of CONTRACT.md (schema 1) in a hosted store, published by `dream` and read
by `ask` through the same seven calls that index.db answers. The notes stay the truth; a store holds a copy and can
be dropped: the next dream republishes it.

  MEMORY_STORE=postgres  MEMORY_STORE_URL=postgresql://user:pw@host:5432/db            needs: pip install "psycopg[binary]"
  MEMORY_STORE=neo4j     MEMORY_STORE_URL=neo4j://host:7687  MEMORY_STORE_USER=neo4j
                         MEMORY_STORE_PASSWORD=…  [MEMORY_STORE_DB=neo4j]               needs: pip install neo4j
  MEMORY_REPO=<id>       one store holds many memories; default: the name of the folder that holds memory/
  memory.py export --to DIR    CSV + Cypher + a neo4j-admin import script; no driver needed

Publishing is a diff: every row is keyed and carries a hash of its content; only new or changed rows travel, rows gone
from the graph are deleted, all in one transaction under a per-repository lock (PostgreSQL: an advisory lock; Neo4j:
the repository's Lock node). A schema or version mismatch (CONTRACT.md `schema`, memory.py `v`) deletes the
repository's rows first and republishes everything. The PostgreSQL backend is tested (tests/store_parity.py). The
Neo4j backend is written against the official 5.x driver and has NOT been run against a server in this repository's
test environment, and neither have the CSV export's import.sh and load.cypher: the export is checked only for its files
and counts.

The seven calls (what memory.py's DbView needs; SqliteRows in memory.py answers them from index.db):
  notes() -> (path, id, area, title, line, kind, updated, superseded_by)…   edges_from(p) / edges_to(p) -> (src, dst, rel)…
  rels_out(i) / rels_in(i) -> (s, type, o, evidence)…   entity(i) -> ({id, type, home, headline, aka, names}, [(path, lines)]) or None
  names(k) -> {entity id}
"""
import csv
import hashlib
import json
import os
import time
from collections import defaultdict
from pathlib import Path

LINEAGE = {"from": "BUILT_ON", "supersedes": "SUPERSEDES", "refs": "REFS"}  # lineage as graph relationship types
LINEAGE_BACK = {v: k for k, v in LINEAGE.items()}
META_KEYS = ("schema", "v", "built", "proposed", "review", "dedup", "vocab", "conflicts", "proposed_types", "tvocab", "checks")
NOTE_KEYS = ("path", "id", "project", "title", "line", "kind", "updated", "sha", "indexed", "superseded_by")
ENT_KEYS = ("id", "type", "home", "headline", "aka", "names")


def _h(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()[:16]


def repo_id(root):
    return os.environ.get("MEMORY_REPO") or Path(root).resolve().parent.name or "memory"


def url_of():
    u = os.environ.get("MEMORY_STORE_URL")
    if not u:
        raise RuntimeError("MEMORY_STORE_URL is not set")
    return u


def desired(g, fold):
    """The graph as keyed rows: what a store should hold for this repository. Edges keep their order (ord) so that
    a view reads them exactly as the local index does."""
    notes = {n["path"]: {k: n[k] for k in NOTE_KEYS} for n in g["notes"]}
    edges = {(e["src"], e["dst"], e["rel"]): i for i, e in enumerate(g["edges"])}
    ents = {e["id"]: {k: e[k] for k in ENT_KEYS} for e in g["entities"]}
    ment = {(e["id"], m["path"]): m["lines"] for e in g["entities"] for m in e["mentions"]}
    names = {(k, e["id"]) for e in g["entities"]
             for k in {fold(x) for x in [e["id"], *e["aka"], *(n["name"] for n in e["names"])] if len(x) >= 3}}
    rels = {(r["s"], r["type"], r["o"]): r["evidence"] for r in g["relations"]}
    meta = {k: g.get(k) for k in META_KEYS}
    return notes, edges, ents, ment, names, rels, meta


def diff(current, wanted):
    """current {key: hash} against wanted {key: hash} -> (keys gone, keys new or changed)."""
    return [k for k in current if k not in wanted], [k for k, h in wanted.items() if current.get(k) != h]


def summary(name, st, t0):
    quiet = not st["upserted"] and not st["deleted"]
    return (f"store {name}: " + ("republished all · " if st.get("full") else "")
            + f"+{st['upserted']} −{st['deleted']} rows" + (" (nothing changed)" if quiet else "") + f" in {time.time() - t0:.1f}s")


# ---------- PostgreSQL ----------

class Postgres:
    """Eight tables keyed by repo. JSONB for lists; `h` is the row's content hash; `ord` keeps edge order."""
    DDL = """
    CREATE TABLE IF NOT EXISTS md_meta  (repo TEXT, k TEXT, v JSONB, PRIMARY KEY (repo, k));
    CREATE TABLE IF NOT EXISTS md_notes (repo TEXT, path TEXT, id TEXT, area TEXT, title TEXT, line INT, kind TEXT,
                                         updated TEXT, sha TEXT, indexed BOOL, sup JSONB, h TEXT, PRIMARY KEY (repo, path));
    CREATE TABLE IF NOT EXISTS md_edges (repo TEXT, src TEXT, dst TEXT, rel TEXT, ord INT, h TEXT, PRIMARY KEY (repo, src, dst, rel));
    CREATE TABLE IF NOT EXISTS md_ents  (repo TEXT, id TEXT, type TEXT, home TEXT, headline TEXT, aka JSONB, names JSONB, h TEXT,
                                         PRIMARY KEY (repo, id));
    CREATE TABLE IF NOT EXISTS md_ment  (repo TEXT, eid TEXT, path TEXT, lines JSONB, h TEXT, PRIMARY KEY (repo, eid, path));
    CREATE TABLE IF NOT EXISTS md_names (repo TEXT, k TEXT, eid TEXT, PRIMARY KEY (repo, k, eid));
    CREATE TABLE IF NOT EXISTS md_rels  (repo TEXT, s TEXT, type TEXT, o TEXT, ev JSONB, h TEXT, PRIMARY KEY (repo, s, type, o));
    CREATE INDEX IF NOT EXISTS md_edges_dst ON md_edges (repo, dst);
    CREATE INDEX IF NOT EXISTS md_rels_o ON md_rels (repo, o);
    CREATE INDEX IF NOT EXISTS md_ment_path ON md_ment (repo, path);
    """
    TABLES = ("md_notes", "md_edges", "md_ents", "md_ment", "md_names", "md_rels", "md_meta")

    def __init__(self, url, repo):
        self.url, self.repo = url, repo

    def connect(self, **kw):
        import psycopg
        return psycopg.connect(self.url, **kw)

    def publish(self, g, fold):
        from psycopg.types.json import Jsonb as J
        notes, edges, ents, ment, names, rels, meta = desired(g, fold)
        t0, st, R = time.time(), {"upserted": 0, "deleted": 0, "full": False}, self.repo
        with self.connect() as conn:
            conn.execute(self.DDL)
            with conn.transaction():
                conn.execute("SELECT pg_advisory_xact_lock(hashtext(%s))", (R,))  # one publisher per repo at a time
                have = {k: v for k, v in conn.execute("SELECT k, v FROM md_meta WHERE repo=%s", (R,))}
                if have and (have.get("schema") != meta["schema"] or have.get("v") != meta["v"]):
                    st["full"] = True
                    for tb in self.TABLES:
                        conn.execute(f"DELETE FROM {tb} WHERE repo=%s", (R,))
                self.sync(conn, st, "md_notes", ("path",), ("id", "area", "title", "line", "kind", "updated", "sha", "indexed", "sup"),
                          {(p,): (_h(n), (n["id"], n["project"], n["title"], n["line"], n["kind"], n["updated"], n["sha"],
                                          bool(n["indexed"]), J(n["superseded_by"]))) for p, n in notes.items()})
                self.sync(conn, st, "md_edges", ("src", "dst", "rel"), ("ord",), {k: (str(i), (i,)) for k, i in edges.items()})
                self.sync(conn, st, "md_ents", ("id",), ("type", "home", "headline", "aka", "names"),
                          {(i,): (_h(e), (e["type"], e["home"], e["headline"], J(e["aka"]), J(e["names"]))) for i, e in ents.items()})
                self.sync(conn, st, "md_ment", ("eid", "path"), ("lines",), {k: (_h(v), (J(v),)) for k, v in ment.items()})
                self.sync(conn, st, "md_names", ("k", "eid"), (), {k: ("", ()) for k in names})
                self.sync(conn, st, "md_rels", ("s", "type", "o"), ("ev",), {k: (_h(v), (J(v),)) for k, v in rels.items()})
                conn.cursor().executemany("INSERT INTO md_meta (repo, k, v) VALUES (%s, %s, %s) ON CONFLICT (repo, k) DO UPDATE SET v = EXCLUDED.v",
                                 [(R, k, J(v)) for k, v in meta.items()])
        return summary("postgres", st, t0)

    def sync(self, conn, st, table, keys, cols, rows):
        """rows {key tuple: (hash, values)}: delete what is gone, upsert what is new or changed (by hash)."""
        hashed = bool(cols)  # tables of bare keys carry no hash column
        current = {}
        for row in conn.execute(f"SELECT {', '.join(keys)}{', h' if hashed else ''} FROM {table} WHERE repo=%s", (self.repo,)):
            current[tuple(row[:len(keys)])] = row[len(keys)] if hashed else ""
        gone, put = diff(current, {k: v[0] for k, v in rows.items()})
        if gone:
            conn.cursor().executemany(f"DELETE FROM {table} WHERE repo=%s AND " + " AND ".join(f"{k}=%s" for k in keys),
                             [(self.repo, *k) for k in gone])
        if put:
            allcols = ("repo", *keys, *cols) + (("h",) if hashed else ())
            upd = ", ".join(f"{c}=EXCLUDED.{c}" for c in (*cols, *(("h",) if hashed else ())))
            sql = (f"INSERT INTO {table} ({', '.join(allcols)}) VALUES ({', '.join(['%s'] * len(allcols))}) "
                   f"ON CONFLICT ({', '.join(('repo', *keys))}) " + (f"DO UPDATE SET {upd}" if upd else "DO NOTHING"))
            conn.cursor().executemany(sql, [(self.repo, *k, *rows[k][1], *((rows[k][0],) if hashed else ())) for k in put])
        st["deleted"] += len(gone)
        st["upserted"] += len(put)

    def rows(self):
        return PostgresRows(self, self.connect(autocommit=True))

    def status(self):
        R = self.repo
        with self.connect() as conn:
            if not conn.execute("SELECT to_regclass('md_meta')").fetchone()[0]:
                return f"store postgres: empty (no tables yet; run dream with MEMORY_STORE=postgres)"
            meta = {k: v for k, v in conn.execute("SELECT k, v FROM md_meta WHERE repo=%s", (R,))}
            if not meta:
                return f"store postgres: no rows for repo {R} yet (run dream)"
            n, e, r = (conn.execute(f"SELECT count(*) FROM {t} WHERE repo=%s", (R,)).fetchone()[0] for t in ("md_notes", "md_ents", "md_rels"))
        return f"store postgres: repo {R} · {n} notes · {e} entities · {r} relations · built {meta.get('built')} · schema {meta.get('schema')} v{meta.get('v')}"

    def read_graph(self):
        """The graph of CONTRACT.md §1 back from the tables (parity tests; a dashboard)."""
        R = self.repo
        with self.connect() as conn:
            meta = {k: v for k, v in conn.execute("SELECT k, v FROM md_meta WHERE repo=%s", (R,))}
            ment = defaultdict(list)
            for e, p, ls in conn.execute("SELECT eid, path, lines FROM md_ment WHERE repo=%s ORDER BY eid, path", (R,)):
                ment[e].append({"path": p, "lines": ls})
            notes = [dict(zip(NOTE_KEYS, r)) for r in conn.execute(
                "SELECT path, id, area, title, line, kind, updated, sha, indexed, sup FROM md_notes WHERE repo=%s ORDER BY path", (R,))]
            ents = [{**dict(zip(ENT_KEYS, r)), "mentions": ment[r[0]]} for r in conn.execute(
                "SELECT id, type, home, headline, aka, names FROM md_ents WHERE repo=%s ORDER BY id", (R,))]
            rels = [{"s": s, "type": t, "o": o, "evidence": ev} for s, t, o, ev in conn.execute(
                "SELECT s, type, o, ev FROM md_rels WHERE repo=%s ORDER BY s, type, o", (R,))]
            edges = [{"src": a, "dst": b, "rel": r} for a, b, r in conn.execute(
                "SELECT src, dst, rel FROM md_edges WHERE repo=%s ORDER BY ord", (R,))]
        return {**meta, "notes": notes, "entities": ents, "relations": rels, "edges": edges}


class PostgresRows:
    def __init__(self, store, conn):
        self.repo, self.db = store.repo, conn
        if not self.db.execute("SELECT 1 FROM md_meta WHERE repo=%s AND k='schema'", (self.repo,)).fetchone():
            raise RuntimeError(f"no rows for repo {self.repo}; run dream with MEMORY_STORE set to publish")

    def notes(self):
        return self.db.execute("SELECT path, id, area, title, line, kind, updated, sup FROM md_notes WHERE repo=%s ORDER BY path", (self.repo,))

    def edges_from(self, p):
        return self.db.execute("SELECT src, dst, rel FROM md_edges WHERE repo=%s AND src=%s ORDER BY ord", (self.repo, p)).fetchall()

    def edges_to(self, p):
        return self.db.execute("SELECT src, dst, rel FROM md_edges WHERE repo=%s AND dst=%s ORDER BY ord", (self.repo, p)).fetchall()

    def rels_out(self, i):
        return self.db.execute("SELECT s, type, o, ev FROM md_rels WHERE repo=%s AND s=%s ORDER BY type, o", (self.repo, i)).fetchall()

    def rels_in(self, i):
        return self.db.execute("SELECT s, type, o, ev FROM md_rels WHERE repo=%s AND o=%s ORDER BY type, s", (self.repo, i)).fetchall()

    def entity(self, i):
        row = self.db.execute("SELECT id, type, home, headline, aka, names FROM md_ents WHERE repo=%s AND id=%s", (self.repo, i)).fetchone()
        if not row:
            return None
        ms = self.db.execute("SELECT path, lines FROM md_ment WHERE repo=%s AND eid=%s ORDER BY path", (self.repo, i)).fetchall()
        return dict(zip(ENT_KEYS, row)), ms

    def names(self, k):
        return {i for (i,) in self.db.execute("SELECT eid FROM md_names WHERE repo=%s AND k=%s", (self.repo, k))}


# ---------- Neo4j (official 5.x driver; not run against a server in this repository's test environment) ----------

class Neo4j:
    """Notes and Entities as nodes keyed by `repo|id`; lineage as BUILT_ON, SUPERSEDES, REFS; MENTIONED_IN with lines;
    typed relations as REL {type, evidence} (one relationship type, the memory's type as a property, so any edition
    and version can hold it); Name nodes for folded spellings; one Meta and one Lock node per repo. Only
    single-property uniqueness constraints are used (Community edition has no composite node keys)."""
    SCHEMA = (
        "CREATE CONSTRAINT md_note_key IF NOT EXISTS FOR (n:Note) REQUIRE n.key IS UNIQUE",
        "CREATE CONSTRAINT md_ent_key IF NOT EXISTS FOR (e:Entity) REQUIRE e.key IS UNIQUE",
        "CREATE CONSTRAINT md_name_key IF NOT EXISTS FOR (m:Name) REQUIRE m.key IS UNIQUE",
        "CREATE CONSTRAINT md_lock_repo IF NOT EXISTS FOR (l:Lock) REQUIRE l.repo IS UNIQUE",
        "CREATE CONSTRAINT md_meta_repo IF NOT EXISTS FOR (m:Meta) REQUIRE m.repo IS UNIQUE",
        "CREATE INDEX md_note_repo IF NOT EXISTS FOR (n:Note) ON (n.repo)",
        "CREATE INDEX md_ent_repo IF NOT EXISTS FOR (e:Entity) ON (e.repo)",
    )

    def __init__(self, url, repo):
        self.url, self.repo = url, repo
        self.auth = (os.environ.get("MEMORY_STORE_USER", "neo4j"), os.environ.get("MEMORY_STORE_PASSWORD", ""))
        self.database = os.environ.get("MEMORY_STORE_DB", "neo4j")

    def driver(self):
        from neo4j import GraphDatabase
        return GraphDatabase.driver(self.url, auth=self.auth)

    def key(self, x):
        return f"{self.repo}|{x}"

    @staticmethod
    def batches(tx, q, rows, size=2000, **params):
        for i in range(0, len(rows), size):
            tx.run(q, rows=rows[i:i + size], **params).consume()

    def publish(self, g, fold):
        notes, edges, ents, ment, names, rels, meta = desired(g, fold)
        t0, st, R, K = time.time(), {"upserted": 0, "deleted": 0, "full": False}, self.repo, self.key
        with self.driver() as drv:
            with drv.session(database=self.database) as s:
                for q in self.SCHEMA:
                    s.run(q).consume()
                with s.begin_transaction() as tx:
                    tx.run("MERGE (l:Lock {repo: $r}) SET l.at = timestamp()", r=R).consume()  # the node lock serialises publishers
                    have = tx.run("MATCH (m:Meta {repo: $r}) RETURN m.schema AS schema, m.v AS v", r=R).single()
                    if have and (have["schema"] != meta["schema"] or have["v"] != meta["v"]):
                        st["full"] = True
                        tx.run("MATCH (n {repo: $r}) WHERE NOT n:Lock DETACH DELETE n", r=R).consume()
                    # notes
                    cur = {rec["path"]: rec["h"] for rec in tx.run("MATCH (n:Note {repo: $r}) RETURN n.path AS path, n.h AS h", r=R)}
                    gone, put = diff(cur, {p: _h(n) for p, n in notes.items()})
                    self.batches(tx, "UNWIND $rows AS k MATCH (n:Note {key: k}) DETACH DELETE n", [K(p) for p in gone])
                    self.batches(tx, "UNWIND $rows AS r MERGE (n:Note {key: r.key}) SET n.repo = $repo, n.path = r.path, n.id = r.id, "
                                     "n.area = r.area, n.title = r.title, n.line = r.line, n.kind = r.kind, n.updated = r.updated, "
                                     "n.sha = r.sha, n.indexed = r.indexed, n.superseded_by = r.sup, n.h = r.h",
                                 [{"key": K(p), "path": p, "id": n["id"], "area": n["project"], "title": n["title"], "line": n["line"],
                                   "kind": n["kind"], "updated": n["updated"], "sha": n["sha"], "indexed": bool(n["indexed"]),
                                   "sup": n["superseded_by"], "h": _h(n)} for p in put for n in [notes[p]]], repo=R)
                    st["deleted"] += len(gone); st["upserted"] += len(put)
                    # entities
                    cur = {rec["id"]: rec["h"] for rec in tx.run("MATCH (e:Entity {repo: $r}) RETURN e.id AS id, e.h AS h", r=R)}
                    gone, put = diff(cur, {i: _h(e) for i, e in ents.items()})
                    self.batches(tx, "UNWIND $rows AS k MATCH (e:Entity {key: k}) DETACH DELETE e", [K(i) for i in gone])
                    self.batches(tx, "UNWIND $rows AS r MERGE (e:Entity {key: r.key}) SET e.repo = $repo, e.id = r.id, e.type = r.type, "
                                     "e.home = r.home, e.headline = r.headline, e.aka = r.aka, e.names = r.names, e.h = r.h",
                                 [{"key": K(i), "id": i, "type": ents[i]["type"], "home": ents[i]["home"], "headline": ents[i]["headline"],
                                   "aka": ents[i]["aka"], "names": json.dumps(ents[i]["names"], ensure_ascii=False), "h": _h(ents[i])}
                                  for i in put], repo=R)
                    st["deleted"] += len(gone); st["upserted"] += len(put)
                    # lineage (ord kept on the relationship so a view reads edges in the index's order)
                    cur = {(rec["a"], rec["b"], rec["rel"]): rec["ord"] for rec in tx.run(
                        "MATCH (a:Note {repo: $r})-[x:BUILT_ON|SUPERSEDES|REFS]->(b:Note) RETURN a.path AS a, b.path AS b, type(x) AS rel, x.ord AS ord", r=R)}
                    want = {(a, b, LINEAGE[r]): i for (a, b, r), i in edges.items()}
                    gone, put = diff(cur, want)
                    for rel in LINEAGE.values():
                        self.batches(tx, f"UNWIND $rows AS r MATCH (a:Note {{key: r.a}})-[x:{rel}]->(b:Note {{key: r.b}}) DELETE x",
                                     [{"a": K(a), "b": K(b)} for a, b, rl in gone if rl == rel])
                        self.batches(tx, f"UNWIND $rows AS r MATCH (a:Note {{key: r.a}}), (b:Note {{key: r.b}}) MERGE (a)-[x:{rel}]->(b) SET x.ord = r.ord",
                                     [{"a": K(a), "b": K(b), "ord": want[(a, b, rl)]} for a, b, rl in put if rl == rel])
                    st["deleted"] += len(gone); st["upserted"] += len(put)
                    # mentions
                    cur = {(rec["e"], rec["p"]): rec["h"] for rec in tx.run(
                        "MATCH (e:Entity {repo: $r})-[x:MENTIONED_IN]->(n:Note) RETURN e.id AS e, n.path AS p, x.h AS h", r=R)}
                    gone, put = diff(cur, {k: _h(v) for k, v in ment.items()})
                    self.batches(tx, "UNWIND $rows AS r MATCH (e:Entity {key: r.e})-[x:MENTIONED_IN]->(n:Note {key: r.p}) DELETE x",
                                 [{"e": K(e), "p": K(p)} for e, p in gone])
                    self.batches(tx, "UNWIND $rows AS r MATCH (e:Entity {key: r.e}), (n:Note {key: r.p}) MERGE (e)-[x:MENTIONED_IN]->(n) "
                                     "SET x.lines = r.lines, x.h = r.h",
                                 [{"e": K(e), "p": K(p), "lines": ment[(e, p)], "h": _h(ment[(e, p)])} for e, p in put])
                    st["deleted"] += len(gone); st["upserted"] += len(put)
                    # names
                    cur = {(rec["k"], rec["e"]) for rec in tx.run("MATCH (m:Name {repo: $r})-[:OF]->(e:Entity) RETURN m.k AS k, e.id AS e", r=R)}
                    gone, put = sorted(cur - names), sorted(names - cur)
                    self.batches(tx, "UNWIND $rows AS r MATCH (m:Name {key: r.k})-[x:OF]->(e:Entity {key: r.e}) DELETE x",
                                 [{"k": K(k), "e": K(e)} for k, e in gone])
                    self.batches(tx, "UNWIND $rows AS r MERGE (m:Name {key: r.key}) SET m.repo = $repo, m.k = r.k "
                                     "WITH m, r MATCH (e:Entity {key: r.e}) MERGE (m)-[:OF]->(e)",
                                 [{"key": K(k), "k": k, "e": K(e)} for k, e in put], repo=R)
                    tx.run("MATCH (m:Name {repo: $r}) WHERE NOT (m)-[:OF]->() DELETE m", r=R).consume()
                    st["deleted"] += len(gone); st["upserted"] += len(put)
                    # typed relations
                    cur = {(rec["s"], rec["t"], rec["o"]): rec["h"] for rec in tx.run(
                        "MATCH (s:Entity {repo: $r})-[x:REL]->(o:Entity) RETURN s.id AS s, x.type AS t, o.id AS o, x.h AS h", r=R)}
                    gone, put = diff(cur, {k: _h(v) for k, v in rels.items()})
                    self.batches(tx, "UNWIND $rows AS r MATCH (s:Entity {key: r.s})-[x:REL {type: r.t}]->(o:Entity {key: r.o}) DELETE x",
                                 [{"s": K(s), "t": t, "o": K(o)} for s, t, o in gone])
                    self.batches(tx, "UNWIND $rows AS r MATCH (s:Entity {key: r.s}), (o:Entity {key: r.o}) MERGE (s)-[x:REL {type: r.t}]->(o) "
                                     "SET x.evidence = r.ev, x.h = r.h",
                                 [{"s": K(s), "t": t, "o": K(o), "ev": rels[(s, t, o)], "h": _h(rels[(s, t, o)])} for s, t, o in put])
                    st["deleted"] += len(gone); st["upserted"] += len(put)
                    tx.run("MERGE (m:Meta {repo: $r}) SET m.schema = $schema, m.v = $v, m.built = $built, m.json = $json",
                           r=R, schema=meta["schema"], v=meta["v"], built=meta["built"], json=json.dumps(meta, ensure_ascii=False)).consume()
                    tx.commit()
        return summary("neo4j", st, t0)

    def rows(self):
        return Neo4jRows(self)

    def status(self):
        with self.driver() as drv, drv.session(database=self.database) as s:
            m = s.run("MATCH (m:Meta {repo: $r}) RETURN m.schema AS schema, m.v AS v, m.built AS built", r=self.repo).single()
            if not m:
                return f"store neo4j: no rows for repo {self.repo} yet (run dream)"
            n = s.run("MATCH (n:Note {repo: $r}) RETURN count(n) AS c", r=self.repo).single()["c"]
            e = s.run("MATCH (e:Entity {repo: $r}) RETURN count(e) AS c", r=self.repo).single()["c"]
            r = s.run("MATCH (:Entity {repo: $r})-[x:REL]->() RETURN count(x) AS c", r=self.repo).single()["c"]
        return f"store neo4j: repo {self.repo} · {n} notes · {e} entities · {r} relations · built {m['built']} · schema {m['schema']} v{m['v']}"

    def read_graph(self):
        R = self.repo
        with self.driver() as drv, drv.session(database=self.database) as s:
            m = s.run("MATCH (m:Meta {repo: $r}) RETURN m.json AS j", r=R).single()
            meta = json.loads(m["j"]) if m else {}
            notes = [dict(zip(NOTE_KEYS, rec)) for rec in s.run(
                "MATCH (n:Note {repo: $r}) RETURN n.path, n.id, n.area, n.title, n.line, n.kind, n.updated, n.sha, n.indexed, "
                "coalesce(n.superseded_by, []) ORDER BY n.path", r=R).values()]
            ment = defaultdict(list)
            for e, p, ls in s.run("MATCH (e:Entity {repo: $r})-[x:MENTIONED_IN]->(n:Note) RETURN e.id, n.path, x.lines ORDER BY e.id, n.path", r=R).values():
                ment[e].append({"path": p, "lines": ls})
            ents = [{**dict(zip(ENT_KEYS, (i, t, h, hl, aka or [], json.loads(nm or "[]")))), "mentions": ment[i]} for i, t, h, hl, aka, nm in s.run(
                "MATCH (e:Entity {repo: $r}) RETURN e.id, e.type, e.home, e.headline, e.aka, e.names ORDER BY e.id", r=R).values()]
            rels = [{"s": a, "type": t, "o": b, "evidence": ev} for a, t, b, ev in s.run(
                "MATCH (a:Entity {repo: $r})-[x:REL]->(b:Entity) RETURN a.id, x.type, b.id, x.evidence ORDER BY a.id, x.type, b.id", r=R).values()]
            edges = [{"src": a, "dst": b, "rel": LINEAGE_BACK[t]} for a, b, t in s.run(
                "MATCH (a:Note {repo: $r})-[x:BUILT_ON|SUPERSEDES|REFS]->(b:Note) RETURN a.path, b.path, type(x) ORDER BY x.ord", r=R).values()]
        return {**meta, "notes": notes, "entities": ents, "relations": rels, "edges": edges}


class Neo4jRows:
    def __init__(self, store):
        self.store, self.repo = store, store.repo
        self.drv = store.driver()
        self.s = self.drv.session(database=store.database)
        if not self.s.run("MATCH (m:Meta {repo: $r}) RETURN 1", r=self.repo).single():
            raise RuntimeError(f"no rows for repo {self.repo}; run dream with MEMORY_STORE set to publish")

    def q(self, cypher, **p):
        return self.s.run(cypher, repo=self.repo, **p).values()

    def notes(self):
        for row in self.q("MATCH (n:Note {repo: $repo}) RETURN n.path, n.id, n.area, n.title, n.line, n.kind, n.updated, "
                          "coalesce(n.superseded_by, []) ORDER BY n.path"):
            yield tuple(row)

    def edges_from(self, p):
        return [(a, b, LINEAGE_BACK[t]) for a, b, t in self.q(
            "MATCH (a:Note {key: $k})-[x:BUILT_ON|SUPERSEDES|REFS]->(b:Note) RETURN a.path, b.path, type(x) ORDER BY x.ord", k=self.store.key(p))]

    def edges_to(self, p):
        return [(a, b, LINEAGE_BACK[t]) for a, b, t in self.q(
            "MATCH (a:Note)-[x:BUILT_ON|SUPERSEDES|REFS]->(b:Note {key: $k}) RETURN a.path, b.path, type(x) ORDER BY x.ord", k=self.store.key(p))]

    def rels_out(self, i):
        return [tuple(r) for r in self.q("MATCH (s:Entity {key: $k})-[x:REL]->(o:Entity) RETURN s.id, x.type, o.id, x.evidence ORDER BY x.type, o.id", k=self.store.key(i))]

    def rels_in(self, i):
        return [tuple(r) for r in self.q("MATCH (s:Entity)-[x:REL]->(o:Entity {key: $k}) RETURN s.id, x.type, o.id, x.evidence ORDER BY x.type, s.id", k=self.store.key(i))]

    def entity(self, i):
        rows = self.q("MATCH (e:Entity {key: $k}) RETURN e.id, e.type, e.home, e.headline, coalesce(e.aka, []), e.names", k=self.store.key(i))
        if not rows:
            return None
        eid, t, h, hl, aka, nm = rows[0]
        ms = [(p, ls) for p, ls in self.q("MATCH (e:Entity {key: $k})-[x:MENTIONED_IN]->(n:Note) RETURN n.path, x.lines ORDER BY n.path", k=self.store.key(i))]
        return {"id": eid, "type": t, "home": h, "headline": hl, "aka": aka, "names": json.loads(nm or "[]")}, ms

    def names(self, k):
        return {i for (i,) in self.q("MATCH (m:Name {key: $k})-[:OF]->(e:Entity) RETURN e.id", k=self.store.key(k))}


# ---------- CSV + Cypher export (any graph database; verified without a server) ----------

def export_csv(root, g, out, fold):
    """notes.csv, entities.csv, names.csv, lineage.csv, mentions.csv, names_of.csv, relations.csv in neo4j-admin header
    format, plus import.sh (neo4j-admin database import), load.cypher (LOAD CSV) and meta.json. -> one summary line."""
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    notes, edges, ents, ment, names, rels, meta = desired(g, fold)

    def w(name, header, rows):
        with open(out / name, "w", newline="", encoding="utf-8") as f:
            cw = csv.writer(f)
            cw.writerow(header)
            cw.writerows(rows)
        return len(rows)

    def arr(xs):
        return ";".join(str(x).replace(";", ",") for x in xs)  # neo4j-admin array delimiter

    n_notes = w("notes.csv", ["path:ID(Note)", "id", "area", "title", "line:int", "kind", "updated", "sha", "indexed:boolean", "superseded_by:string[]"],
                [[p, n["id"], n["project"], n["title"], n["line"], n["kind"], n["updated"], n["sha"], str(bool(n["indexed"])).lower(),
                  arr(n["superseded_by"])] for p, n in sorted(notes.items())])
    n_ents = w("entities.csv", ["id:ID(Entity)", "type", "home", "headline", "aka:string[]", "names"],
               [[i, e["type"], e["home"] or "", e["headline"] or "", arr(e["aka"]), json.dumps(e["names"], ensure_ascii=False)]
                for i, e in sorted(ents.items())])
    n_names = w("names.csv", ["k:ID(Name)"], [[k] for k in sorted({k for k, _ in names})])
    n_edges = w("lineage.csv", [":START_ID(Note)", ":END_ID(Note)", ":TYPE", "ord:int"],
                [[a, b, LINEAGE[r], i] for (a, b, r), i in sorted(edges.items(), key=lambda kv: kv[1])])
    n_ment = w("mentions.csv", [":START_ID(Entity)", ":END_ID(Note)", "lines:int[]", ":TYPE"],
               [[e, p, arr(ls), "MENTIONED_IN"] for (e, p), ls in sorted(ment.items())])
    w("names_of.csv", [":START_ID(Name)", ":END_ID(Entity)", ":TYPE"], [[k, e, "OF"] for k, e in sorted(names)])
    n_rels = w("relations.csv", [":START_ID(Entity)", ":END_ID(Entity)", "type", "evidence:string[]", ":TYPE"],
               [[s, o, t, arr(ev), "REL"] for (s, t, o), ev in sorted(rels.items())])
    (out / "meta.json").write_text(json.dumps(meta, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    (out / "import.sh").write_text("""#!/bin/sh
# Neo4j 5: bulk import into a new database (run on the database host, from this directory). Usage: sh import.sh [dbname]
set -e
DB=${1:-memdream}
neo4j-admin database import full --overwrite-destination --array-delimiter=';' \\
  --nodes=Note=notes.csv --nodes=Entity=entities.csv --nodes=Name=names.csv \\
  --relationships=lineage.csv --relationships=mentions.csv --relationships=names_of.csv --relationships=relations.csv "$DB"
""", encoding="utf-8")
    (out / "load.cypher").write_text("""// LOAD CSV alternative for a running Neo4j: copy the CSV files into the server's import directory first.
CREATE CONSTRAINT note_path IF NOT EXISTS FOR (n:Note) REQUIRE n.path IS UNIQUE;
CREATE CONSTRAINT entity_id IF NOT EXISTS FOR (e:Entity) REQUIRE e.id IS UNIQUE;
CREATE CONSTRAINT name_k IF NOT EXISTS FOR (m:Name) REQUIRE m.k IS UNIQUE;
LOAD CSV WITH HEADERS FROM 'file:///notes.csv' AS r
  MERGE (n:Note {path: r.`path:ID(Note)`})
  SET n.id = r.id, n.area = r.area, n.title = r.title, n.line = toInteger(r.`line:int`), n.kind = r.kind, n.updated = r.updated,
      n.sha = r.sha, n.indexed = (r.`indexed:boolean` = 'true'),
      n.superseded_by = CASE r.`superseded_by:string[]` WHEN '' THEN [] ELSE split(r.`superseded_by:string[]`, ';') END;
LOAD CSV WITH HEADERS FROM 'file:///entities.csv' AS r
  MERGE (e:Entity {id: r.`id:ID(Entity)`})
  SET e.type = r.type, e.home = r.home, e.headline = r.headline, e.names = r.names,
      e.aka = CASE r.`aka:string[]` WHEN '' THEN [] ELSE split(r.`aka:string[]`, ';') END;
LOAD CSV WITH HEADERS FROM 'file:///lineage.csv' AS r
  MATCH (a:Note {path: r.`:START_ID(Note)`}), (b:Note {path: r.`:END_ID(Note)`})
  FOREACH (_ IN CASE WHEN r.`:TYPE` = 'BUILT_ON' THEN [1] ELSE [] END | MERGE (a)-[x:BUILT_ON]->(b) SET x.ord = toInteger(r.`ord:int`))
  FOREACH (_ IN CASE WHEN r.`:TYPE` = 'SUPERSEDES' THEN [1] ELSE [] END | MERGE (a)-[x:SUPERSEDES]->(b) SET x.ord = toInteger(r.`ord:int`))
  FOREACH (_ IN CASE WHEN r.`:TYPE` = 'REFS' THEN [1] ELSE [] END | MERGE (a)-[x:REFS]->(b) SET x.ord = toInteger(r.`ord:int`));
LOAD CSV WITH HEADERS FROM 'file:///mentions.csv' AS r
  MATCH (e:Entity {id: r.`:START_ID(Entity)`}), (n:Note {path: r.`:END_ID(Note)`})
  MERGE (e)-[x:MENTIONED_IN]->(n) SET x.lines = [l IN split(r.`lines:int[]`, ';') | toInteger(l)];
LOAD CSV WITH HEADERS FROM 'file:///relations.csv' AS r
  MATCH (s:Entity {id: r.`:START_ID(Entity)`}), (o:Entity {id: r.`:END_ID(Entity)`})
  MERGE (s)-[x:REL {type: r.type}]->(o) SET x.evidence = split(r.`evidence:string[]`, ';');
LOAD CSV WITH HEADERS FROM 'file:///names_of.csv' AS r
  MATCH (e:Entity {id: r.`:END_ID(Entity)`}) MERGE (m:Name {k: r.`:START_ID(Name)`}) MERGE (m)-[:OF]->(e);
// Examples: the live end of a chain   MATCH (n:Note {path: $p})<-[:SUPERSEDES*1..4]-(m) WHERE NOT (m)<-[:SUPERSEDES]-() RETURN m.path
//           what uses a thing          MATCH (x:Entity)-[r:REL {type: 'uses'}]->(e:Entity {id: $id}) RETURN x.id, r.evidence
""", encoding="utf-8")
    (out / "README.md").write_text(f"""# memory-dream graph export

The graph of CONTRACT.md (schema {meta.get('schema')}, built {meta.get('built')}) as CSV in neo4j-admin header format:
notes.csv ({n_notes} Note nodes), entities.csv ({n_ents} Entity nodes), names.csv ({n_names} Name nodes, folded spellings),
lineage.csv ({n_edges} BUILT_ON / SUPERSEDES / REFS relationships, `ord` keeps the index's order), mentions.csv ({n_ment}
MENTIONED_IN with line numbers), names_of.csv (Name OF Entity), relations.csv ({n_rels} REL with `type` and `evidence`),
meta.json (vocabulary, conflicts, checks, dedup counters).

- `sh import.sh [db]` bulk-imports into a new Neo4j 5 database with neo4j-admin (fast; the database must not exist or
  `--overwrite-destination` replaces it).
- `load.cypher` does the same with LOAD CSV against a running server (copy the CSV files into its import directory).
- Any other graph or relational database can read the same files: ids are the memory's own (note paths, entity ids).

The export is a copy. The notes in the repository stay the truth; re-export after a dream to refresh it.
""", encoding="utf-8")
    return (f"export: {n_notes} notes, {n_ents} entities, {n_names} names, {n_edges} lineage links, {n_ment} mentions, {n_rels} relations → "
            f"{out} (import.sh for neo4j-admin, load.cypher for LOAD CSV)")


# ---------- what memory.py calls ----------

def backend(name, root):
    repo = repo_id(root)
    if name in ("postgres", "postgresql", "pg"):
        return Postgres(url_of(), repo)
    if name in ("neo4j", "bolt"):
        return Neo4j(url_of(), repo)
    raise RuntimeError(f"unknown MEMORY_STORE {name!r}: postgres or neo4j, or unset for the local index")


def publish(name, root, g, fold):
    return backend(name, root).publish(g, fold)


def rows(name, root):
    return backend(name, root).rows()


def status(name, root):
    return backend(name, root).status()


def read_graph(name, root):
    return backend(name, root).read_graph()
