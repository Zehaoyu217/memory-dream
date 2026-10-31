#!/usr/bin/env python3
"""Acceptance tests A1–A20 (spec §13), A24 (big memories) and A25–A29 (REVIEW.md phase A: whole-memory print, folder
scope, C9, weak match, two-hop taste) on the churn-2026 fixture, with the deterministic fake dreamer.

  python3 tests/acceptance.py            # all
  python3 tests/acceptance.py A6 A15     # some
Real-model runs (A3, A10, A18 with Haiku) and the A21 agent eval are in tests/real_model.py and eval/.
"""
import importlib.util
import json
import os
import random
import re
import shutil
import subprocess
import sys
import tempfile
import time
import traceback
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
MEM = HERE.parent / "skills/memory-dream/scripts/memory.py"
FIX = HERE / "fixture/memory"
FAKE = f"{sys.executable} {HERE / 'fake_dreamer.py'}"
_spec = importlib.util.spec_from_file_location("memory", MEM)
mem = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mem)
sys.path.insert(0, str(HERE))
import fake_dreamer as fake  # noqa: E402
from truth import convergence  # noqa: E402

P = "churn-2026/"


class World:
    def __init__(self, fixture=True):
        self.dir = Path(tempfile.mkdtemp(prefix="memdream-"))
        self.root = self.dir / "memory"
        if fixture:
            shutil.copytree(FIX, self.root)
        else:
            self.root.mkdir()
        self.log = self.dir / "calls.log"
        self.env = {k: v for k, v in os.environ.items() if not k.startswith(("MEMORY_", "FAKE_"))}
        self.env["FAKE_LOG"] = str(self.log)

    def run(self, *args, model=True, env=None):
        e = dict(self.env, **(env or {}))
        if model:
            e["MEMORY_LLM"] = FAKE
        r = subprocess.run([sys.executable, str(MEM), "--root", str(self.root), *args],
                           capture_output=True, text=True, env=e)
        assert r.returncode == 0, f"{args}: exit {r.returncode}\n{r.stderr}"
        return r.stdout

    def calls(self, kind=None):
        rows = [ln.split() for ln in self.log.read_text().splitlines()] if self.log.exists() else []
        return [r for r in rows if kind is None or r[0] == kind]

    def graph(self):
        """What where/trace see right now (fresh rescan, in memory)."""
        return mem.load(self.root)[0]

    def text(self, rel):
        return (self.root / rel).read_text()

    def inject(self, answers):
        p = self.dir / "inject.json"
        p.write_text(json.dumps({k: v if isinstance(v, str) else json.dumps(v) for k, v in answers.items()}))
        self.env["FAKE_INJECT"] = str(p)

    def oracle(self, stem):
        rel = P + stem + ".md"
        return fake.extraction(rel, self.text(rel))


def ents(g):
    return {e["id"]: e for e in g["entities"]}


def rels(g):
    return {(r["s"], r["type"], r["o"]): r for r in g["relations"]}


def codes(g):
    return Counter(c["code"] for c in g["checks"])


def note(g, rel):
    return next(n for n in g["notes"] if n["path"] == rel)


# ---------- tests ----------

def A1():
    w = World(fixture=False)
    out = w.run("dream")
    for f in ("EDGES.md", "ALIASES.md", "_dream/graph.json", "_dream/graph.html"):
        assert (w.root / f).exists(), f
    assert not (w.root / "INDEX.md").exists()
    assert w.text("EDGES.md") == mem.EDGES_SEED and w.text("ALIASES.md") == mem.ALIASES_HEAD
    assert "0 notes" in out
    return out.strip()


def A2():
    w = World()
    out = w.run("dream", model=False)
    g = w.graph()
    assert codes(g)["C5"] == 30, codes(g)
    want = set()
    for p in w.root.rglob("*.md"):
        rel = p.relative_to(w.root).as_posix()
        if rel.split("/")[0] in ("_dream",) or p.name in mem.SKIP:
            continue
        fm = mem.parse_note(p.read_text())[0]
        want |= {(rel, P + v + ".md", k) for k in ("from", "supersedes") for v in mem.fm_list(fm.get(k))}
    got = {(e["src"], e["dst"], e["rel"]) for e in g["edges"] if e["rel"] != "refs"}
    assert got == want, (got ^ want)
    sup = {n["id"]: [Path(x).stem for x in n["superseded_by"]] for n in g["notes"] if n["superseded_by"]}
    assert sup == {"feat-velocity-v2": ["feat-velocity-v3"], "churn-xgb-v2": ["churn-xgb-v3"]}, sup
    a = w.run("ask", "what came of exp-014?", "why was the velocity feature rebuilt?", model=False)
    for s_ in ("churn-2026/exp-014.md", "churn-2026/churn-xgb-v2.md", "SUPERSEDED → churn-xgb-v3", "post-period-leak.md"):
        assert s_ in a, s_
    return f"{out.splitlines()[0]} · {len(got)} lineage edges · C5={codes(g)['C5']} · ask answers from lineage + grep"


def A3():
    w = World()
    o1 = w.run("dream")
    x = w.calls("extract")
    assert len(x) == 30 and len({r[1] for r in x}) == 30, len(x)
    n = len(w.calls())
    o2 = w.run("dream")
    assert len(w.calls()) == n and "0 indexed (0 calls)" in o2, o2
    g = w.graph()
    assert all(n["indexed"] for n in g["notes"]) and not codes(g)["C4"], codes(g)
    return f"{o1.strip()} || {o2.strip()}"


def A4():
    w = World()
    w.run("dream")
    g0, n = w.graph(), len(w.calls())
    moves = {P + s + ".md": P + "archive/" + s + ".md" for s in
             ("exp-011-baseline", "q-tier-cutoffs", "exp-015-tenure", "finding-new-accounts", "leak-hypothesis")}
    moves.update({P + "exp-014.md": P + "exp-014-xgb-velocity.md", P + "dec-risk-tiers.md": P + "dec-risk-tier-cuts.md"})
    for a, b in moves.items():
        (w.root / b).parent.mkdir(parents=True, exist_ok=True)
        os.rename(w.root / a, w.root / b)
    g1 = w.graph()
    out = w.run("dream")
    assert len(w.calls()) == n, "calls after move"
    assert "7 moved" in out and not codes(g1)["C2"], (out, codes(g1))
    back = {b: a for a, b in moves.items()}

    def norm(g):
        s_ = json.dumps({k: g[k] for k in ("notes", "entities", "relations", "edges", "proposed", "review")}, sort_keys=True)
        for b, a in sorted(back.items(), key=lambda z: -len(z[0])):
            s_ = s_.replace(b, a)
        g = json.loads(s_)
        for nn in g["notes"]:
            nn["id"] = Path(nn["path"]).stem
        g["notes"].sort(key=lambda z: z["path"])
        g["entities"] = sorted(({**e, "mentions": sorted(e["mentions"], key=lambda m: m["path"])} for e in g["entities"]),
                               key=lambda e: e["id"])
        for r in g["relations"]:
            r["evidence"].sort()
        g["edges"].sort(key=lambda e: (e["src"], e["dst"], e["rel"]))
        return g
    assert norm(g0) == norm(w.graph()), "graph differs beyond paths"
    edges = {(e["src"], e["dst"], e["rel"]) for e in w.graph()["edges"]}
    assert (P + "archive/leak-hypothesis.md", P + "exp-014-xgb-velocity.md", "from") in edges
    return f"{out.strip()} · from: exp-014 resolves to the renamed note · graph identical modulo paths"


def A5():
    w = World()
    w.run("dream")
    n = len(w.calls("extract"))
    rel = P + "churn-xgb-v3.md"
    (w.root / rel).write_text(w.text(rel) + "Retrain due 2026-11-30.\n")
    g = w.graph()
    assert not note(g, rel)["indexed"]
    assert not any(m["path"] == rel for e in g["entities"] for m in e["mentions"])
    assert not any(ev.startswith(rel + ":") for r in g["relations"] for ev in r["evidence"])
    a = w.run("ask", "when is the churn-xgb-v3 retrain due?")
    assert rel in a and "2026-11-30" in a, a
    w.run("dream")
    assert len(w.calls("extract")) == n + 1
    return "edited note dropped from the graph until dream, still found by ask (grep); exactly 1 call"


def A6():
    w = World()
    w.run("dream")
    g0, n = w.graph(), len(w.calls())
    rel = P + "dec-risk-tiers.md"
    pointed = [e["id"] for e in g0["entities"] if e["headline"] == rel]
    assert pointed
    os.remove(w.root / rel)
    g = w.graph()
    blob = json.dumps({k: g[k] for k in ("notes", "entities", "relations", "edges")})
    assert rel not in blob
    moved = {k: ents(g)[k]["headline"] for k in pointed if k in ents(g)}
    assert moved and all(h and h != rel for h in moved.values()), moved
    c2 = [c["msg"] for c in g["checks"] if c["code"] == "C2"]
    assert len(c2) == 2, c2
    assert "dec-risk-tiers" not in w.run("ask", "what are the risk tier cutoffs?")
    assert len(w.calls()) == n
    d = w.run("dream")
    assert len(w.calls()) == n and "1 deleted" in d
    return f"headlines moved {moved} · C2×{len(c2)} · 0 calls"


def A7():
    w = World()
    w.run("dream")
    rel = P + "exp-014.md"
    orig = w.text(rel)
    (w.root / rel).write_text(orig + "Re-run planned.\n")
    w.run("dream")
    n = len(w.calls("extract"))
    (w.root / rel).write_text(orig)
    out = w.run("dream")
    assert len(w.calls("extract")) == n, "revert cost a call"
    return out.strip()


def A8():
    w = World()
    a = w.oracle("exp-019-recall")
    a["entities"].append({"id": "churn-dashboard", "type": "tool", "as": ["the churn dashboard"]})
    b = w.oracle("churn-xgb-v3")
    b["relations"].append({"s": "churn-xgb-v3", "type": "uses", "o": "holdout-2025q4", "quote": "tuned weekly on holdout-2025q4"})
    w.inject({"exp-019-recall": a, "churn-xgb-v3": b})
    w.run("dream")
    g = w.graph()
    assert codes(g)["C4"] == 2, [c for c in g["checks"] if c["code"] == "C4"]
    assert "churn-dashboard" not in ents(g)
    assert ("churn-xgb-v3", "uses", "holdout-2025q4") not in rels(g)
    return "fabricated surface and absent quote both dropped · C4=2"


def A9():
    w = World()
    a, b = w.oracle("exp-019-recall"), w.oracle("exp-017-leak-check")
    w.inject({"exp-019-recall": "Sure! Here is the JSON:\n" + json.dumps(a) + "\nHope that helps.",
              "exp-017-leak-check": "```json\n" + json.dumps(b, indent=2) + "\n```",
              "leak-hypothesis": "{\"kind\": \"question\", \"summary\": oops"})
    w.run("dream")
    g = w.graph()
    assert note(g, P + "exp-019-recall.md")["indexed"] and note(g, P + "exp-017-leak-check.md")["indexed"]
    assert not note(g, P + "leak-hypothesis.md")["indexed"]
    c3 = [c["msg"] for c in g["checks"] if c["code"] == "C3"]
    tries = [r for r in w.calls("extract") if r[1] == P + "leak-hypothesis.md"]
    assert len(c3) == 1 and len(tries) == 2, (c3, tries)
    return "prose- and fence-wrapped answers parsed; invalid JSON retried once → C3"


def answer_pending(w):
    """Play the memory-dreamer subagent with the fake: answer every prompt without a .json."""
    pend, n = w.root / "_dream" / "pending", 0
    for pp in sorted(pend.glob("*.prompt.md")):
        pj = pend / (pp.name[:-len(".prompt.md")] + ".json")
        if not pj.exists():
            r = subprocess.run(FAKE.split(), input=pp.read_text(), capture_output=True, text=True, env=w.env)
            pj.write_text(r.stdout)
            n += 1
    return n


def A10():
    w = World()
    outs = [w.run("dream", model=False)]
    rounds = 0
    while list((w.root / "_dream" / "pending").glob("*.prompt.md")) and rounds < 4:
        answer_pending(w)
        outs.append(w.run("dream", model=False))
        rounds += 1
    g = w.graph()
    assert all(n["indexed"] for n in g["notes"]) and not codes(g)["C3"], codes(g)
    assert "fitted-on" in w.text("EDGES.md") and "risk-tier" in w.text("ALIASES.md"), "review not applied"
    assert not list((w.root / "_dream" / "pending").iterdir())
    return f"{rounds} dreamer rounds · " + " | ".join(o.splitlines()[0] for o in outs)


def A11():
    w = World()
    w.run("dream")
    g = w.graph()
    types = Counter(r["type"] for r in g["relations"])
    for t in ("uses", "trained-on", "evaluated-on", "owned-by"):
        assert types[t], t
    assert set(types) <= set(mem.parse_edges(mem.EDGES_SEED)[0]), types
    for r in g["relations"]:
        for ev in r["evidence"]:
            rel, line = ev.rsplit(":", 1)
            assert 1 <= int(line) <= len(w.text(rel).split("\n")), ev
    users = {r["s"] for r in g["relations"] if r["o"] == "cards.txn_daily"}
    users |= {r["s"] for r in g["relations"] if r["o"] in users}
    for x in ("feat-velocity-v2", "feat-velocity-v3", "feat-utilization-v1", "churn-xgb-v2", "churn-xgb-v3"):
        assert x in users, x
    return f"relation types {dict(types)} · two hops up from cards.txn_daily reach the features and models"


def A12():
    w = World()
    p = w.dir / "review.json"
    p.write_text(json.dumps({"types": {"learned-from": "maybe later"}}))
    w.run("dream", env={"FAKE_REVIEW": str(p)})
    g = w.graph()
    c7 = [c["msg"] for c in g["checks"] if c["code"] == "C7"]
    assert any("unknown relation type learned-from ×3" in m for m in c7), c7
    assert not any(r["type"] == "learned-from" for r in g["relations"]), "closed vocabulary shows unknown types"
    n = len(w.calls("extract"))
    w.run("dream")
    assert "learned-from" in next(ln for ln in w.text("EDGES.md").split("\n") if ln.startswith("- trained-on"))
    assert sum(1 for ln in w.text("EDGES.md").split("\n") if ln.startswith("- ")) == 8, "review added a type"
    g = w.graph()
    assert ("churn-xgb-v2", "trained-on", "cards.churn_labels") in rels(g)
    assert len(w.calls("extract")) == n
    return "learned-from ×3 held back (closed), review mapped it onto trained-on, relabelled with 0 extraction calls, still 8 types"


def A13():
    w = World()
    w.run("dream")
    r = rels(w.graph()).get(("feat-velocity-v2", "uses", "cards.txn_daily"))
    assert r and P + "txn-backfill.md:6" in r["evidence"], r
    return f"feat-velocity-v2 uses cards.txn_daily, evidence {r['evidence']}"


def A14():
    w = World()
    w.run("dream")
    n = len(w.calls())
    lines = w.text("EDGES.md").split("\n")
    tr = next(ln for ln in lines if ln.startswith("- trained-on"))
    aka = tr.split("aka:", 1)[1].strip()
    lines = [ln + ", trained-on, " + aka if ln.startswith("- uses:") else ln for ln in lines if ln != tr]
    (w.root / "EDGES.md").write_text("\n".join(lines))
    g = w.graph()
    assert not any(r["type"] == "trained-on" for r in g["relations"])
    assert ("churn-xgb-v3", "uses", "cards.churn_labels") in rels(g)
    w.run("dream")
    assert len(w.calls()) == n
    return "trained-on folded into uses by hand: every trained-on relation reads uses, 0 calls"


def A15():
    w = World()
    a = w.oracle("q-churn-drivers")
    for e in a["entities"]:
        if e["id"] == "cards.txn_daily":
            e["id"] = "Cards.TXN_daily"
    w.inject({"q-churn-drivers": a})
    w.env["FAKE_SAVE"] = str(w.dir / "prompts")
    w.run("dream")
    g = w.graph()
    E = ents(g)
    assert {"Cards.TXN_daily", "txn-table"} <= set(E["cards.txn_daily"]["aka"]), E["cards.txn_daily"]["aka"]
    assert "feat-velocity-v2" in E and "feat-velocity-v3" in E
    v2v3 = {n["name"] for n in E["feat-velocity-v2"]["names"]} & {n["name"] for n in E["feat-velocity-v3"]["names"]}
    assert "velocity features" in v2v3
    reviews = sorted((w.dir / "prompts").glob("*-review.txt"))
    assert len(reviews) == 1
    rv = reviews[0].read_text()
    assert "- risk-tier-cutoffs / risk-tier-cuts:" in rv or "- risk-tier-cuts / risk-tier-cutoffs:" in rv, rv
    assert "feat-velocity-v2 / feat-velocity-v3" not in rv and "txn" not in rv.split("ENTITY PAIRS", 1)[1]
    assert "risk-tier" in w.text("ALIASES.md")
    w.run("dream")
    assert len(list((w.dir / "prompts").glob("*-review.txt"))) == 1, "asked again"
    return "case fold + surface rule merged for free; v2/v3 never asked; risk-tier asked once → ALIASES.md"


def A16():
    w = World()
    a = w.oracle("ds-txn-2025q4")
    a["entities"] = [e for e in a["entities"] if e["id"] != "cards.txn_daily"] + \
        [{"id": "ds-txn", "type": "dataset", "as": ["Q4-2025 snapshot"]}]
    a["relations"] = [{"s": "ds-txn", "type": "owned-by", "o": "data-eng-cards", "quote": "Owned by data-eng-cards"}]
    w.inject({"ds-txn-2025q4": a})
    w.run("dream")
    assert "ds-txn" not in ents(w.graph()), "a one-note entity with no home is not an entity"
    n = len(w.calls())
    (w.root / "ALIASES.md").write_text(w.text("ALIASES.md") + "- cards.txn_daily = ds-txn\n")
    g = w.graph()
    E = ents(g)
    assert "ds-txn" not in E and "ds-txn" in E["cards.txn_daily"]["aka"]
    r = rels(g)[("cards.txn_daily", "owned-by", "data-eng-cards")]
    assert P + "ds-txn-2025q4.md:5" in r["evidence"]
    assert any(m["path"] == P + "ds-txn-2025q4.md" for m in E["cards.txn_daily"]["mentions"])
    w.run("dream")
    assert len(w.calls()) == n
    return "hand alias moved ds-txn's relations and pointers onto cards.txn_daily, 0 calls"


def A17():
    w = World()
    w.run("dream")
    assert ents(w.graph())["feat-velocity-v2"]["headline"] == P + "post-period-leak.md"
    n = len(w.calls())
    os.remove(w.root / (P + "post-period-leak.md"))
    g = w.graph()
    e = ents(g)["feat-velocity-v2"]
    notes = {x["path"]: x for x in g["notes"]}
    live = [(notes[m["path"]]["line"] in m["lines"], notes[m["path"]]["kind"] in ("finding", "decision"),
             notes[m["path"]]["updated"], m["path"]) for m in e["mentions"] if not notes[m["path"]]["superseded_by"]]
    want = max(live)[3]
    assert e["headline"] == want == P + "feat-velocity-v3.md", (e["headline"], want)
    assert e["home"] == P + "feat-velocity-v2.md"
    assert len(w.calls()) == n
    return f"headline post-period-leak → {want} after deletion, 0 calls · home note feat-velocity-v2.md"


def A18():
    w = World()
    w.run("dream")
    c = convergence(w.graph())
    return f"fake dreamer: {c['ids_for_true']} ids for {c['true_found']} true entities (ratio {c['ratio']})"


def A19():
    d = Path(tempfile.mkdtemp(prefix="memdream-perf-"))
    root = d / "memory"
    rnd = random.Random(7)
    words = "churn txn velocity util limit score tier label holdout recall auc spend merchant fraud risk offer " \
            "cohort tenure balance payment cash travel grocery fuel online branch mobile email call retention".split()
    ids = sorted({f"{rnd.choice(words)}-{rnd.choice(words)}-{rnd.choice(words)}" for _ in range(2600)})[:2000]
    types = ["dataset", "feature", "model", "metric", "segment", "concept"]
    etype = {i: rnd.choice(types) for i in ids}
    (root / "_dream" / "notes").mkdir(parents=True)
    alias_lines = []
    for k in range(1000):
        proj = f"proj-{k % 20:02d}"
        mine = [ids[(2 * k) % 2000], ids[(2 * k + 1) % 2000]] + rnd.sample(ids, 4)
        body = f"---\nupdated: 2026-{1 + k % 9:02d}-{1 + k % 27:02d}\n---\n# Note {k}: {mine[0]} drives {mine[1]}\n" + \
            "\n".join(f"Line about `{e}` and its use, {k}.{j}." for j, e in enumerate(mine)) + "\n"
        p = root / proj / f"note-{k:04d}.md"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(body)
        h = mem.hashlib.sha256(p.read_bytes()).hexdigest()
        rec = {"kind": "finding", "summary": f"Note {k}", "refs": [], "dropped": {}, "path": p.relative_to(root).as_posix(),
               "sha": h, "entities": [{"id": e, "type": etype[e], "as": [e], "lines": [5 + j]} for j, e in enumerate(mine)],
               "relations": [{"s": mine[0], "type": rnd.choice(["uses", "feeds", "fitted-on", "trained-on"]), "o": mine[i],
                              "quote": mine[i], "line": 5 + i} for i in (1, 2, 3)]}
        (root / "_dream" / "notes" / f"{h[:12]}.json").write_text(json.dumps(rec))
    for k in range(0, 200, 2):
        alias_lines.append(f"- {ids[k]} = {ids[k + 1]}")
    (root / "ALIASES.md").write_text(mem.ALIASES_HEAD + "\n".join(alias_lines) + "\n")
    (root / "EDGES.md").write_text(mem.EDGES_SEED)
    man = {}
    cur, former, _, _ = mem.scan(root, man)
    et, at = mem.vocab_texts(root)
    t0 = time.perf_counter()
    g = mem.build(root, {"seen": [mem.fold(i) for i in ids]}, cur, former, et, at)
    t_merge = time.perf_counter() - t0
    E = {e["id"]: e for e in g["entities"]}
    alines, nots, _ = mem.parse_aliases(at)
    occ = [(n["path"], e) for n in g["notes"] for e in rd_ext(root, n["sha"])["entities"]]
    _, _, gkeys = mem.merge_entities(occ, alines, nots)
    new = rnd.sample(list(E), 200)
    t0 = time.perf_counter()
    pairs = mem.candidates(E, new, gkeys, nots)
    t_cand = time.perf_counter() - t0
    env = {k: v for k, v in os.environ.items() if not k.startswith("MEMORY_")}
    subprocess.run([sys.executable, str(MEM), "--root", str(root), "dream"], capture_output=True, env=env, check=True)
    t0 = time.perf_counter()
    subprocess.run([sys.executable, str(MEM), "--root", str(root), "ask", f"what do we know about {ids[10]}?"], capture_output=True, env=env, check=True)
    t_where = time.perf_counter() - t0
    edit = root / "proj-03" / "note-0003.md"
    edit.write_text(edit.read_text() + "edited\n")
    t0 = time.perf_counter()
    subprocess.run([sys.executable, str(MEM), "--root", str(root), "ask", f"what do we know about {ids[10]}?"], capture_output=True, env=env, check=True)
    t_where_stale = time.perf_counter() - t0
    shutil.rmtree(d)
    assert len(g["notes"]) == 1000 and len(E) >= 1500, (len(g["notes"]), len(E))
    assert t_merge < 1 and t_where < 0.8 and t_cand < 2, (t_merge, t_where, t_cand)
    return (f"1000 notes, {len(E)} entities, {len(g['relations'])} relations: merge {t_merge:.2f}s · ask {t_where:.2f}s "
            f"(after an edit, re-merge in memory: {t_where_stale:.2f}s) · review candidates for 200 new ids {t_cand:.2f}s "
            f"({len(pairs)} pairs)")


def rd_ext(root, sha12):
    return json.loads((root / "_dream" / "notes" / f"{sha12}.json").read_text())


def A20():
    """Vocabulary and identity: closed relation types, entity homes, no one-note or file entities."""
    w = World()
    a = w.oracle("exp-014")
    a["entities"] += [{"id": "nb/exp014_xgb.ipynb", "type": "tool", "as": ["nb/exp014_xgb.ipynb"]},
                      {"id": "vel-ratio-30-90", "type": "feature", "as": ["vel_ratio_30_90"]}]
    a["relations"].append({"s": "xgboost", "type": "zorbs", "o": "holdout-2025q4", "quote": "Model: XGBoost"})
    w.inject({"exp-014": a})
    w.run("dream")
    g = w.graph()
    E = ents(g)
    assert "nb/exp014_xgb.ipynb" not in E and "vel-ratio-30-90" not in E
    assert not any(r["type"] == "zorbs" for r in g["relations"])
    assert any("rarer unknown relation types dropped" in c["msg"] for c in g["checks"])
    homes = {e["id"]: e["home"] for e in g["entities"] if e["home"]}
    assert homes.get("feat-velocity-v3") == P + "feat-velocity-v3.md" and homes.get("churn-xgb-v3") == P + "churn-xgb-v3.md"
    assert all(len(e["mentions"]) >= 2 or e["home"] for e in g["entities"])
    return f"{len(E)} entities, {len(homes)} with a home note; files, one-note ids and unknown types left out"


def A24():
    """Big memories (forced with MEMORY_WIDE): ask greps only the named project, takes general areas along for
    questions that name none, and patches notes written since the dream into the last graph."""
    w = World()
    shutil.copytree(w.root / "churn-2026", w.root / "churn-2025")  # a sibling project with the same note ids
    (w.root / "prefs").mkdir()
    (w.root / "prefs/rate-decimals.md").write_text("# Rates in reports use one decimal place\n"
                                                   "Churn and default rates get one decimal, e.g. 6.8%.\n")
    w.run("dream")
    big = {"MEMORY_WIDE": "10"}
    heads = lambda out: re.findall(r"^▸ (\S+)", out, flags=re.M)  # noqa: E731
    got = heads(w.run("ask", "In churn-2026, what came of exp-014?", env=big))
    assert got and all(h.startswith(P) for h in got), got
    out = w.run("ask", "How many decimal places do rates get in reports?", env=big)
    assert "prefs/rate-decimals.md" in heads(out), out[:400]
    (w.root / P / "dec-tiers-v3.md").write_text(
        "---\nsupersedes: [dec-risk-tiers]\nupdated: 2026-10-31\n---\n"
        "# Risk-tier cuts moved to 0.25 and 0.55 for churn-xgb-v3\n"
        "The current risk-tier cuts are 0.25 (email) and 0.55 (call), set on churn-xgb-v3 scores.\n")
    t0 = time.perf_counter()
    out = w.run("ask", "In churn-2026, what are the current risk-tier cuts?", env=big)
    assert P + "dec-tiers-v3.md" in heads(out) and "SUPERSEDED → dec-tiers-v3" in out, out[:600]
    took = time.perf_counter() - t0
    w.run("dream", env=big)  # big outputs: no graph.json; an overview and one page per area
    dd = w.root / "_dream"
    assert not (dd / "graph.json").exists() and (dd / "graph.html").exists() and (dd / "index.db").exists()
    sig = json.loads((dd / "viz/_sig.json").read_text())
    assert {"churn-2026", "churn-2025", "prefs", "log"} <= set(sig), sig
    mt = {a: (dd / f"viz/{a}.html").stat().st_mtime_ns for a in sig}
    (w.root / "prefs/rate-decimals.md").write_text("# Rates in reports use one decimal place\n"
                                                   "Churn and default rates get one decimal, e.g. 6.8%. Counts get none.\n")
    w.run("dream", env=big)
    redrawn = sorted(a for a in sig if (dd / f"viz/{a}.html").stat().st_mtime_ns != mt[a])
    assert redrawn == ["prefs"], redrawn
    assert "rate-decimals" in w.run("ask", "How many decimal places do rates get in reports?", env=big)
    return (f"scoped: {len(got)} notes, all in churn-2026 (its copy churn-2025 left out) · general question → prefs · "
            f"note written after the dream supersedes dec-risk-tiers in ask ({took:.1f}s, no rebuild) · big dream: "
            f"no graph.json, {len(sig)} area pages; after one edit only {redrawn} redrawn")


def A25():
    """Small memories: when printing the whole memory costs about the same as the surgical answer, ask prints all of
    it, each question pointing at its notes — never less complete than `cat memory/**`."""
    w = World()
    qs = ["What do we know about feat-velocity-v2?", "What came of exp-014?", "Why was the velocity feature rebuilt?",
          "What is the current churn model and its AUC?", "What depends on cards.txn_daily?", "Who owns cards.txn_daily?",
          "What are the risk tier cutoffs?", "What did exp-015 find about tenure?", "When is the next retrain?",
          "What is recall@10 on holdout-2025q4?"]
    out = w.run("ask", *qs, model=False)
    assert "## memory — complete (30 notes" in out, out[:300]
    heads = set(re.findall(r"^▸ (\S+)", out, flags=re.M))
    notes = {p.relative_to(w.root).as_posix() for p in w.root.rglob("*.md") if "_dream" not in p.parts and p.name not in mem.SKIP}
    assert notes <= heads, notes - heads
    secs = re.split(r"^## ", out, flags=re.M)[1:]
    assert all(re.search(r"^▸ ", s, re.M) for s in secs[:len(qs)]), "a question without pointers"
    raw = sum(len(p.read_text()) for p in w.root.rglob("*.md") if "_dream" not in p.parts)
    assert len(out) <= 1.5 * raw, (len(out), raw)
    two = w.run("ask", *qs[:2], model=False)
    assert "— complete (" not in two and len(two) < 0.5 * len(out), len(two)
    return f"10 questions → the whole memory ({len(out)} chars; raw notes {raw}), every note headed; 2 questions → surgical ({len(two)} chars)"


def A26():
    """A project named in plain words scopes the search, even when the stemmer would shorten the folder's name."""
    w = World()
    (w.root / "pricing").mkdir()
    (w.root / "pricing/price-gbm-v1.md").write_text(
        "---\ntype: model\n---\n# price-gbm-v1 is the current pricing model: MAE 3.2 on holdout-2026q1\n"
        "Gradient boosting on card spend; it replaces the rules table.\n")
    out = w.run("ask", "what is the current model in pricing?", model=False)
    heads = re.findall(r"^▸ (\S+)", out, flags=re.M)
    assert heads and all(h.startswith("pricing/") for h in heads), heads
    assert "price-gbm-v1" in out
    return f"'in pricing' scoped to pricing/ ({len(heads)} note); the stem 'pric' no longer hides the folder"


def A27():
    """A note with NUL bytes is still found by ask (grep -a) and flagged by check (C9)."""
    w = World()
    (w.root / P / "nul-note.md").write_bytes(b"# binary-looking note zebra-nul\nbody\x00with zebra-nul\n")
    w.run("dream", model=False)
    chk = w.run("check", model=False)
    assert re.search(r"^C9 ×1", chk, re.M) and "nul-note.md" in chk, chk[:400]
    out = w.run("ask", "zebra-nul", model=False)
    assert P + "nul-note.md" in out, out[:300]
    return "NUL-byte note: found by ask, flagged C9 by check"


def A28():
    """A question whose words occur nowhere is marked weak instead of heading an unrelated note like a hit."""
    w = World()
    weak = w.run("ask", "what is the meaning of zxqv?", model=False)
    assert "(weak match" in weak and "'zxqv'" in weak, weak[:300]
    good = w.run("ask", "what came of exp-014?", "who owns cards.txn_daily?", "why was the velocity feature rebuilt?", model=False)
    assert "(weak match" not in good
    return "unknown word → weak-match marker naming it; real questions unmarked"


def A29():
    """A task that names the meeting or report, not the person, still brings the person's preferences (two hops)."""
    w = World()
    (w.root / "prefs").mkdir()
    (w.root / "reporting").mkdir()
    (w.root / "prefs/chloe-martin-no-pie.md").write_text("# Chloe Martin bans pie charts in campaign reporting\n"
                                                        "Sorted bars with direct labels instead.\n")
    (w.root / "prefs/chloe-martin-codes.md").write_text("# Chloe Martin refers to campaigns by code, not by title\n"
                                                       "Codes like CMP-2026-014 in every label.\n")
    (w.root / "reporting/weekly-kpi-deck.md").write_text("# The weekly KPI deck has a campaign slide; it goes to Chloe Martin\n"
                                                        "Six recipients; slide 6 is campaigns.\n")
    out = w.run("ask", "Make the chart for the weekly KPI deck's campaign slide", model=False)
    assert "preferences and house rules" in out, out[:400]
    for p in ("prefs/chloe-martin-no-pie.md", "prefs/chloe-martin-codes.md"):
        assert p in out, (p, out)
    return "task names the deck, not the person: the roster note names her, both preferences attached"


def A30():
    """Kinds without a model: filename prefixes and areas give kinds; general areas are judged on kinded notes only."""
    w = World()
    (w.root / "prefs").mkdir()
    (w.root / "prefs/me-decimals.md").write_text("# I round rates to one decimal in every readout\nSo 6.8%, not 6.83%.\n")
    (w.root / "reporting").mkdir()
    (w.root / "reporting/chart-colour.md").write_text("# Chart colour: brand blue first, grey for context\n")
    w.run("dream", model=False)
    g = w.graph()
    kinds = {n["id"]: n["kind"] for n in g["notes"]}
    want = {"exp-014": "experiment", "dec-risk-tiers": "decision", "feat-velocity-v2": "feature", "ds-txn-2025q4": "dataset",
            "churn-xgb-v3": "model", "q-churn-drivers": "question", "finding-new-accounts": "finding",
            "me-decimals": "preference", "chart-colour": "rule", "2026-10-30": "log"}
    bad = {k: (kinds.get(k), v) for k, v in want.items() if kinds.get(k) != v}
    assert not bad, bad
    by_area = {}
    for n in g["notes"]:
        by_area.setdefault(n["project"], []).append(n["path"])
    gen = mem.general_areas(by_area, lambda p: kinds[Path(p).stem])
    assert gen == {"prefs", "reporting", "log"}, gen
    n_k = sum(1 for k in kinds.values() if k != "note")
    return f"{n_k}/{len(kinds)} notes kinded with no model; general areas = {sorted(gen)}"


def cc_world(w):
    """A mock of Claude Code's auto-memory directory beside the fixture."""
    cc = w.dir / "cc"
    cc.mkdir()
    (cc / "MEMORY.md").write_text("# index\n- [Testing](feedback_testing.md) — tests hit a real database\n")
    (cc / "feedback_testing.md").write_text("---\ntype: feedback\nmodified: 2026-10-25T15:00:00Z\n---\n"
                                          "# Integration tests must hit a real database, not mocks\nA mocked test passed while prod failed.\n")
    (cc / "user_role.md").write_text("---\ntype: user\nmodified: 2026-10-20T09:00:00Z\n---\n"
                                   "# The user is a data scientist on the cards team and prefers terse answers\n")
    return cc


def A31():
    """Claude Code's auto memory is read in the same ask call, under its own mark, and never written to."""
    w = World()
    cc = cc_world(w)
    before = {p.name: p.read_bytes() for p in cc.iterdir()}
    env = {"MEMORY_CC_DIR": str(cc)}
    out = w.run("ask", "how should integration tests be written?", "what came of exp-014?", model=False, env=env)
    assert "▸ claude-code: feedback_testing.md · feedback · 2026-10-25" in out, out[:600]
    assert "MEMORY.md" not in out
    sec = out.split("## what came of exp-014?")[0]
    assert "real database" in sec, sec
    assert "claude-code:" not in w.run("ask", "how should integration tests be written?", model=False,
                                       env={**env, "MEMORY_SOURCES": "notes"})
    w.run("check", model=False, env=env)
    assert {p.name: p.read_bytes() for p in cc.iterdir()} == before, "ask or check wrote into Claude Code's directory"
    for verb in (["dream"], ["log", "x"], ["viz"]):
        r = subprocess.run([sys.executable, str(MEM), "--root", str(cc), *verb], capture_output=True, text=True, env=w.env)
        assert r.returncode == 2 and "never" in r.stderr, (verb, r.returncode, r.stderr)
    assert {p.name for p in cc.iterdir()} == set(before), "dream/log/viz wrote into Claude Code's directory"
    return "auto-memory topic file shown with origin, type and modified date; MEMORY.md skipped; dream/log/viz refused; directory untouched"


def A32():
    """dream writes memory/DIGEST.md: ≤ 40 lines, how to ask, the user's own preferences, the newest live decisions
    and models; nothing superseded; not a note itself; the nothing-new short cut still holds."""
    w = World()
    (w.root / "prefs").mkdir()
    (w.root / "prefs/me-decimals.md").write_text("# I round rates to one decimal in every readout\n")
    w.run("dream", model=False)
    d = w.text("DIGEST.md")
    lines = d.rstrip("\n").split("\n")
    assert len(lines) <= 40 and "memory.py ask" in d.replace("scripts/memory.py", "memory.py") or " ask " in d, d[:300]
    assert "## your own preferences" in d and "one decimal" in d
    assert "churn-xgb-v3" in d and "churn-xgb-v2" not in d, d
    assert "DIGEST.md" not in {n["id"] + ".md" for n in w.graph()["notes"]}
    w.run("dream", model=False)
    out = w.run("dream", model=False)
    assert "0 indexed (0 calls)" in out
    assert w.text("DIGEST.md") == d
    return f"DIGEST.md: {len(lines)} lines, {len(d)} chars; preferences and live heads listed, superseded left out"


def A33():
    """Notes in Claude Code's convention parse: type: feedback → rule, modified: → the date."""
    w = World()
    (w.root / P / "cc-style.md").write_text("---\ntype: feedback\nmodified: 2026-10-25T15:00:00Z\n---\n"
                                           "# Integration tests must hit a real database\n")
    w.run("dream", model=False)
    n = note(w.graph(), P + "cc-style.md")
    assert n["kind"] == "rule" and n["updated"] == "2026-10-25", n
    return "type: feedback → rule; modified: → 2026-10-25"


TESTS = [A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16, A17, A18, A19, A20, A24,
         A25, A26, A27, A28, A29, A30, A31, A32, A33]


def main():
    want = set(sys.argv[1:])
    results, failed = [], 0
    for t in TESTS:
        if want and t.__name__ not in want:
            continue
        t0 = time.perf_counter()
        try:
            detail, ok = t(), True
        except Exception as e:  # noqa: BLE001
            detail, ok = f"{type(e).__name__}: {e}\n{traceback.format_exc(limit=3)}", False
            failed += 1
        dt_ = time.perf_counter() - t0
        print(f"{'PASS' if ok else 'FAIL'} {t.__name__} ({dt_:.1f}s) {detail}")
        results.append({"id": t.__name__, "pass": ok, "detail": detail, "secs": round(dt_, 1)})
    (HERE / "acceptance.json").write_text(json.dumps(results, indent=1, ensure_ascii=False))
    print(f"{len(results) - failed}/{len(results)} passed")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
