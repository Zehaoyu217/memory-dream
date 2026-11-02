#!/usr/bin/env python3
"""Store parity (ADR-001): through a hosted store, `ask` prints exactly what it prints from the local index, the graph
read back equals graph.json, and publishing is a diff. Needs the store's driver on this interpreter and MEMORY_STORE_URL.

  MEMORY_STORE_URL=postgresql://user:pw@host/db python3 tests/store_parity.py postgres [--bank] [--keep]

Steps on a copy of the fixture, indexed by the fake dreamer: dream publishes · ask ×6 identical both ways · the graph read
back equals graph.json · a second dream publishes nothing · an edited note publishes a few rows and ask stays identical ·
a deleted note leaves the store · a version mismatch republishes everything · a store that is down falls back to the local
index with one line on stderr · `export` writes the CSV bundle. --bank adds the 1,677-note bank: publish time and the
326-question retrieval numbers through the store against the local index.
"""
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MEM = ROOT / "skills/memory-dream/scripts/memory.py"
FAKE = f"{sys.executable} {ROOT / 'tests/fake_dreamer.py'}"
QS = ["what came of exp-014?", "who owns cards.txn_daily?", "what uses the txn table?", "what is the current churn model?",
      "Make the Q4 chart for Maya Ortiz's readout", "what is the meaning of zxqv?"]


def load_mem():
    spec = importlib.util.spec_from_file_location("memory", MEM)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def run(args, env, root, ok=True):
    r = subprocess.run([sys.executable, str(MEM), "--root", str(root), *args], capture_output=True, text=True, env=env)
    if ok and r.returncode != 0:
        raise SystemExit(f"memory.py {' '.join(args)}: exit {r.returncode}\n{r.stdout[-1500:]}\n{r.stderr[-1500:]}")
    return r.stdout, r.stderr


def first_diff(a, b):
    la, lb = a.splitlines(), b.splitlines()
    for i, (x, y) in enumerate(zip(la, lb)):
        if x != y:
            return f"line {i + 1}: local {x[:70]!r} · store {y[:70]!r}"
    return f"lengths {len(la)} vs {len(lb)} lines"


def same_graph(a, b):
    """CONTRACT §1 fields that the store must give back unchanged (edges without the review mark `by`)."""
    keys = ("path", "id", "project", "title", "line", "kind", "updated", "sha", "indexed", "superseded_by")
    na = [{k: n[k] for k in keys} for n in sorted(a["notes"], key=lambda n: n["path"])]
    nb = [{k: n[k] for k in keys} for n in sorted(b["notes"], key=lambda n: n["path"])]
    ea = [(e["src"], e["dst"], e["rel"]) for e in a["edges"]]
    eb = [(e["src"], e["dst"], e["rel"]) for e in b["edges"]]
    ent = lambda es: sorted(({**{k: e[k] for k in ("id", "type", "home", "headline", "aka", "names")},  # noqa: E731
                              "mentions": sorted((m["path"], tuple(m["lines"])) for m in e["mentions"])} for e in es), key=lambda e: e["id"])
    ra = sorted((r["s"], r["type"], r["o"], tuple(r["evidence"])) for r in a["relations"])
    rb = sorted((r["s"], r["type"], r["o"], tuple(r["evidence"])) for r in b["relations"])
    meta = lambda g: {k: g.get(k) for k in ("schema", "v", "built", "proposed", "review", "dedup", "vocab", "conflicts", "proposed_types", "tvocab")}  # noqa: E731
    ca, cb = sorted((c["code"], c["msg"]) for c in a["checks"]), sorted((c["code"], c["msg"]) for c in b["checks"])
    return na == nb and ea == eb and ent(a["entities"]) == ent(b["entities"]) and ra == rb and meta(a) == meta(b) and ca == cb


def tamper_version(name, url, repo):
    """Pretend the store was written by another memory.py version: the next publish must start over."""
    if name in ("postgres", "postgresql", "pg"):
        import psycopg
        from psycopg.types.json import Jsonb
        with psycopg.connect(url) as conn:
            conn.execute("UPDATE md_meta SET v=%s WHERE repo=%s AND k='v'", (Jsonb("0.0"), repo))
    else:
        raise SystemExit(f"tamper_version: no recipe for {name}")


def main(argv):
    name = next((a for a in argv[1:] if not a.startswith("--")), "postgres")
    url = os.environ.get("MEMORY_STORE_URL")
    if not url:
        raise SystemExit("MEMORY_STORE_URL is not set")
    work = Path(tempfile.mkdtemp(prefix="parity-"))
    root = work / "memory"
    shutil.copytree(ROOT / "tests/fixture/memory", root)
    base = {k: v for k, v in os.environ.items() if not k.startswith(("MEMORY_", "FAKE_"))}
    local = {**base, "MEMORY_LLM": FAKE}
    repo = f"parity-{os.getpid()}"
    store = {**local, "MEMORY_STORE": name, "MEMORY_STORE_URL": url, "MEMORY_REPO": repo}
    results = []

    def check(label, ok, detail=""):
        results.append(ok)
        print(("PASS " if ok else "FAIL ") + label + (f" · {detail}" if detail else ""))

    out, err = run(["dream"], store, root)
    check("dream publishes", f"store {name}: +" in out and "publish failed" not in err,
          out.strip().split(" · ")[-1] + (" · " + err.strip()[-300:] if "failed" in err else ""))
    a_local, _ = run(["ask", *QS], local, root)
    a_store, err = run(["ask", *QS], store, root)
    check("ask identical through the store", a_local == a_store and "unavailable" not in err,
          f"{len(a_store)} chars, 6 questions" if a_local == a_store else first_diff(a_local, a_store) + (err.strip()[-200:] if err.strip() else ""))
    out, _ = run(["check"], store, root)
    check("check names the store", f"store {name}: repo {repo}" in out, next((ln for ln in out.splitlines() if ln.startswith("store ")), "")[:120])
    os.environ.update({"MEMORY_STORE": name, "MEMORY_STORE_URL": url, "MEMORY_REPO": repo})
    mem = load_mem()
    g_local = json.loads((root / "_dream/graph.json").read_text())
    g_store = mem.stores_module().read_graph(name, root)
    check("graph round-trips", same_graph(g_local, g_store), f"{len(g_store['notes'])} notes, {len(g_store['entities'])} entities, {len(g_store['relations'])} relations, {len(g_store['edges'])} edges")
    out, _ = run(["dream"], store, root)
    check("second dream publishes nothing", "nothing changed" in out, out.strip().split(" · ")[-1])
    p = root / "churn-2026/txn-backfill.md"
    p.write_text(p.read_text() + "\nThe October partitions were re-checked on 2026-11-02; no gap.\n")
    out, _ = run(["dream"], store, root)
    check("an edit publishes a few rows", f"store {name}: +" in out and "nothing changed" not in out, out.strip().split(" · ")[-1])
    a_local, _ = run(["ask", *QS], local, root)
    a_store, _ = run(["ask", *QS], store, root)
    check("ask identical after the edit", a_local == a_store, "" if a_local == a_store else first_diff(a_local, a_store))
    (root / "churn-2026/q-tier-cutoffs.md").unlink()
    out, _ = run(["dream"], store, root)
    g_store = mem.stores_module().read_graph(name, root)
    check("a deleted note leaves the store", "−" in out and all(n["path"] != "churn-2026/q-tier-cutoffs.md" for n in g_store["notes"]), out.strip().split(" · ")[-1])
    tamper_version(name, url, repo)
    p.write_text(p.read_text() + "One more check, 2026-11-02.\n")
    out, _ = run(["dream"], store, root)
    check("a version mismatch republishes everything", "republished all" in out, out.strip().split(" · ")[-1])
    down = {**store, "MEMORY_STORE_URL": "postgresql://127.0.0.1:1/none?connect_timeout=1" if name.startswith("p") else "neo4j://127.0.0.1:1"}
    a_down, err = run(["ask", *QS], down, root)
    a_local, _ = run(["ask", *QS], local, root)
    check("a store that is down falls back to the local index", a_down == a_local and "unavailable" in err, err.strip()[:100])
    out, _ = run(["export", "--to", str(work / "export")], local, root)
    files = sorted(q.name for q in (work / "export").iterdir())
    check("export writes the CSV bundle", {"notes.csv", "entities.csv", "lineage.csv", "relations.csv", "import.sh", "load.cypher"} <= set(files), out.strip()[:110])

    if "--bank" in argv:
        bank = work / "bank"
        subprocess.run([sys.executable, ROOT / "eval/bank/assemble.py", ROOT / "eval/bank/generated", ROOT / "tests/fixture/memory", bank], check=True, capture_output=True)
        bank_store = {**base, "MEMORY_STORE": name, "MEMORY_STORE_URL": url, "MEMORY_REPO": repo + "-bank"}
        t = time.time()
        out, _ = run(["dream"], bank_store, bank)
        t_pub = time.time() - t
        check("bank: 1,677 notes published", f"store {name}: +" in out, f"{out.strip().split(' · ')[-1]} (dream + publish {t_pub:.1f}s)")
        qs = sorted((ROOT / "eval/questions").glob("bank-*.jsonl"))
        r_local = subprocess.run([sys.executable, ROOT / "eval/retrieval.py", bank, *qs], capture_output=True, text=True, env=base).stdout.splitlines()[0]
        r_store = subprocess.run([sys.executable, ROOT / "eval/retrieval.py", bank, *qs], capture_output=True, text=True, env=bank_store).stdout.splitlines()[0]
        jl, js = json.loads(r_local), json.loads(r_store)
        same = all(jl[k] == js[k] for k in ("questions", "note_recall", "num_recall", "precision", "full_note_hit", "chars_per_q"))
        check("bank: retrieval identical through the store", same, f"local {jl['note_recall']}/{jl['num_recall']} in {jl['secs_per_batch']}s per batch · store {js['note_recall']}/{js['num_recall']} in {js['secs_per_batch']}s")

    print(f"{sum(results)}/{len(results)} passed" + (f" · work dir kept: {work}" if "--keep" in argv else ""))
    if "--keep" not in argv:
        shutil.rmtree(work, ignore_errors=True)
    sys.exit(0 if all(results) else 1)


if __name__ == "__main__":
    main(sys.argv)
