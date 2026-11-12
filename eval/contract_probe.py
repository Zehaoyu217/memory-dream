#!/usr/bin/env python3
"""What the shipped code does for the v0.5 contract, measured. No model, standard library, about three minutes.

  python3 eval/contract_probe.py <a dreamed memory>     e.g. the bank-index world of HANDOFF.md "Picking it up"

Six experiments, each on a throwaway copy; the memory given is never written to. The numbers are quoted in
.specs/memory-dream/PLAN.md (rev 3) and RESULTS.md phases K, M and N. Experiments 1, 3 and 4 show the way v0.4
did it and then the way built since.

  1 drop       one note in the middle of a supersession chain, deleted by hand and then taken out with `memory.py
               drop`: what is left of it each way
  2 built on   how many notes a drop would take with it if it followed `from:` (why built-on notes are marked, not deleted)
  3 copy in    a second memory copied in under a folder: areas, kinds, lineage; then the same folder as an origin,
               with and without `trust: preferences`
  4 absorb     a graph someone else's model wrote (entity cards, relations.jsonl, its sources: eval/absorb/policy-kb)
               through the file-mode socket, asked across the two, the host's own gate answers compared before and
               after, then taken out by hand; then the same through `memory.py absorb`, joined by one line, and dropped
  5 documents  plain documents as notes, whole and split at headings: retrieval and what the note rules say
  6 sets       "list every <kind> of <area>": how much of the set `ask` prints, against one line per note
"""
import collections
import hashlib
import json
import os
import re
import shutil
import statistics
import subprocess
import sys
import tempfile
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
MEM = REPO / "skills/memory-dream/scripts/memory.py"
ENV = {k: v for k, v in os.environ.items() if not k.startswith("MEMORY_")}  # no model, no store, default knobs


def run(root, *args):
    return subprocess.run([sys.executable, str(MEM), "--root", str(root), *args], env=ENV, capture_output=True, text=True).stdout


def graph(root):
    return json.loads((Path(root) / "_dream" / "graph.json").read_text())


def same(g):
    """A graph as text with its build time taken out: equal text, equal graph."""
    return json.dumps({k: v for k, v in g.items() if k != "built"}, sort_keys=True)


def copy(src, tmp, name):
    dst = Path(tmp) / name / "memory"
    shutil.copytree(src, dst)  # copy2: modification times kept, so the copy's manifest still matches
    return dst


def headed(out):
    """The notes an `ask` answer heads, in order."""
    return re.findall(r"^▸ (\S+\.md)", out, flags=re.M)


def pct(vals, p):
    return sorted(vals)[min(len(vals) - 1, int(len(vals) * p))]


# ---------- 1 and 2: drop ----------

def drop(src, tmp):
    g = graph(src)
    notes = {n["path"]: n for n in g["notes"]}
    kids, sups = collections.defaultdict(set), collections.defaultdict(set)
    for e in g["edges"]:
        if e["rel"] == "from":
            kids[e["dst"]].add(e["src"])
        elif e["rel"] == "supersedes":
            sups[e["src"]].add(e["dst"])
    # a note in the middle of a chain: it replaced something and was itself replaced; its drop cuts the chain when
    # it was the only successor of what it replaced
    mid = sorted(p for p, n in notes.items() if n["superseded_by"] and any(notes[q]["superseded_by"] == [p] for q in sups[p]))
    ends = sorted(p for p, n in notes.items() if not n["superseded_by"] and sups[p])
    print(f"1 drop · {len(notes)} notes; {len(mid)} sit in the middle of a supersession chain, {len(ends)} at its live end")
    if not mid:
        print("  no chain to cut in this memory")
        return
    pick = sorted(mid, key=lambda p: (-len(kids[p]), p))[0]
    pred = sorted(q for q in sups[pick] if notes[q]["superseded_by"] == [pick])[0]
    root = copy(src, tmp, "drop")
    q = f"what is {notes[pred]['id']}?"
    before = run(root, "ask", q)
    (root / pick).unlink()
    line = run(root, "dream").strip()
    after, g2 = run(root, "ask", q), graph(root)
    n2 = {n["path"]: n for n in g2["notes"]}
    ev = lambda r: {x.rsplit(":", 1)[0] for x in r["evidence"]}  # noqa: E731
    rels, rels2 = {(r["s"], r["type"], r["o"]): r for r in g["relations"]}, {(r["s"], r["type"], r["o"]) for r in g2["relations"]}
    only = [k for k, r in rels.items() if ev(r) == {pick}]
    ents2 = {e["id"] for e in g2["entities"]}
    solo = [e["id"] for e in g["entities"] if {m["path"] for m in e["mentions"]} == {pick}]
    head = lambda out: next((ln for ln in out.split("\n") if ln.startswith(f"▸ {pred} ")), "")  # noqa: E731
    stem = notes[pick]["id"]
    print(f"  deleted by hand: {pick} ({len(kids[pick])} notes built on it; it replaced {pred}) → {line}")
    print(f"  derived graph: the note gone {pick not in n2} · things that were only there, gone {sum(e not in ents2 for e in solo)}/{len(solo)}"
          f" · links resting only on it, gone {sum(k not in rels2 for k in only)}/{len(only)}"
          f" · evidence still pointing at it {sum(pick in ev(r) for r in g2['relations'])}"
          f" · mentions still listing it {sum(any(m['path'] == pick for m in e['mentions']) for e in g2['entities'])}")
    print(f"  lineage: {pred} superseded before {bool(notes[pred]['superseded_by'])}, after {bool(n2[pred]['superseded_by'])}"
          f" · `ask` marks it SUPERSEDED before {'SUPERSEDED' in head(before)}, after {'SUPERSEDED' in head(after)}")
    left = [k for k in kids[pick] if k in n2]
    warn = [c for c in g2["checks"] if c["code"] == "C2" and stem in c["msg"]]
    print(f"  notes built on it: {len(left)} of {len(kids[pick])} still there, told apart only by {len(warn)} C2 lines ('… not found')")
    print(f"  its reading still in the cache: {(root / '_dream' / 'notes' / (notes[pick]['sha'] + '.json')).exists()} (kept 30 days)")
    gone = [c["msg"] for c in g2["checks"] if c["code"] == "C15"]
    print(f"  and the dream says so: {len(gone)} C15 line" + (f" — {gone[0][:150]}" if gone else ""))

    # the same note taken out with `memory.py drop` (step 0 of the plan, RESULTS phase M)
    root = copy(src, tmp, "drop-cmd")
    line = [ln for ln in run(root, "drop", pick, "--yes").split("\n") if ln.startswith("dream:")][0]
    after, g3 = run(root, "ask", q), graph(root)
    n3 = {n["path"]: n for n in g3["notes"]}
    rec = next(d for d in g3["dropped"] if d["path"] == pick)
    tomb = [ln for ln in (root / "CONFLICTS.md").read_text().split("\n") if ln.startswith(f"dropped: {pick}")]
    heads = run(root, "ask", "--list", "--all")
    print(f"  taken out with `drop --yes`: {line}")
    print(f"  lineage: {pred} superseded after {bool(n3[pred]['superseded_by'])}, by {', '.join(n3[pred]['superseded_by'])}"
          f" · `ask` marks it SUPERSEDED {'SUPERSEDED' in head(after)}")
    print(f"  notes built on it: {sum(k in n3 for k in kids[pick])} of {len(kids[pick])} still there, {len(rec['built_on_by'])} recorded, "
          f"{sum(f'{stem} (dropped)' in ln for ln in heads.split(chr(10)))} say '(dropped)' on their line of the map, "
          f"{sum(c['code'] == 'C14' for c in g3['checks'])} C14 lines, {sum(c['code'] == 'C2' and stem in c['msg'] for c in g3['checks'])} C2 lines")
    print(f"  its reading in the cache: {(root / '_dream' / 'notes' / (notes[pick]['sha'] + '.json')).exists()} · in CONFLICTS.md: {tomb[0] if tomb else 'nothing'}")

    # 2: what a drop that followed from: would take
    def closure(p):
        seen, todo = set(), [p]
        while todo:
            for k in kids[todo.pop()]:
                if k not in seen:
                    seen.add(k)
                    todo.append(k)
        return seen
    sizes = {p: len(closure(p)) for p in notes}
    vals = list(sizes.values())
    top = max(sizes, key=lambda p: (sizes[p], p))
    print(f"2 built on · notes reached through from:, any depth: {sum(1 for v in vals if v)} of {len(vals)} notes have some · median "
          f"{statistics.median(vals):g} · mean {statistics.mean(vals):.1f} · p90 {pct(vals, .9)} · max {max(vals)} "
          f"({top}, across {len({q.split('/')[0] for q in closure(top)})} areas)")


# ---------- 3: a second memory copied in ----------

def copy_in(src, tmp):
    solo = Path(tmp) / "solo" / "memory"
    shutil.copytree(REPO / "tests/fixture-software/memory", solo, ignore=shutil.ignore_patterns("log", "_dream"))
    run(solo, "dream")
    s = graph(solo)
    root = copy(src, tmp, "copyin")
    shutil.copytree(solo, root / "ext", ignore=shutil.ignore_patterns("_dream", "*.md~", "KINDS.md", "TYPES.md", "EDGES.md", "ALIASES.md",
                                                                      "CONFLICTS.md", "DIGEST.md"))
    run(root, "dream")
    g = graph(root)
    mine = [n for n in g["notes"] if n["path"].startswith("ext/")]
    sn = {n["path"]: n for n in s["notes"]}
    changed = [(n["path"], sn[n["path"][4:]]["kind"], n["kind"]) for n in mine if sn[n["path"][4:]]["kind"] != n["kind"]]
    em = collections.Counter(e["rel"] for e in g["edges"] if e["src"].startswith("ext/"))
    es = collections.Counter(e["rel"] for e in s["edges"])
    print(f"3 copy in · {len(mine)} notes of a second memory under ext/ · areas {len({n['project'] for n in sn.values()})} → "
          f"{len({n['project'] for n in mine})} ({', '.join(sorted({n['project'] for n in mine}))})"
          f" · lineage edges kept {sum(em.values())}/{sum(es.values())}"
          f" · kinds changed {len(changed)}: " + "; ".join(f"{p[4:]} {a}→{b}" for p, a, b in changed))

    # the same folder as an origin: one file, ORIGIN.md (step 1 of the plan, RESULTS phase N)
    tasks = ["Draft the changelog email for Priya Nair", "Make the latency chart for the platform review"]

    def served(out):
        """The origin's notes that `ask` lists as preferences and house rules for a task (its instruction block)."""
        got = []
        for sec in out.split("\n## ")[:len(tasks)]:
            if "preferences and house rules for this task:" in sec:  # up to the block of other bases, which informs only
                block = sec.split("preferences and house rules for this task:")[1].split("  in other bases (they inform")[0]
                got += [p for p in headed(block) if p.startswith("ext/")]
        return got
    plain = served(run(root, "ask", *tasks))
    for trust in ("answers", "answers, preferences"):
        (root / "ext" / "ORIGIN.md").write_text(f"# ORIGIN — ext: a second team's memory, copied in\nfrom: tests/fixture-software\ntrust: {trust}\n")
        run(root, "dream")
        g = graph(root)
        mine = [n for n in g["notes"] if n["path"].startswith("ext/")]
        changed = [(n["path"], sn[n["path"][4:]]["kind"], n["kind"]) for n in mine if sn[n["path"][4:]]["kind"] != n["kind"]]
        em = collections.Counter(e["rel"] for e in g["edges"] if e["src"].startswith("ext/"))
        got = sorted(set(served(run(root, "ask", *tasks))))
        digest = (root / "DIGEST.md").read_text()
        print(f"  with ext/ORIGIN.md, trust: {trust} · areas {len({n['project'] for n in mine})} ({', '.join(sorted({n['project'] for n in mine}))})"
              f" · lineage edges kept {sum(em.values())}/{sum(es.values())} · kinds changed {len(changed)}"
              + (": " + "; ".join(f"{p[4:]} {a}→{b}" for p, a, b in changed) if changed else "")
              + f" · its notes served as preferences to two host tasks: {len(got)}" + (f" ({', '.join(p[4:] for p in got)})" if got else "")
              + f" · its notes in the host's digest: {sum('ext/' in ln for ln in digest.split(chr(10)))}")
    print(f"  (without ORIGIN.md the same tasks were served {len(plain)}"
          + (f": {', '.join(p[4:] for p in plain)})" if plain else ": a copied preference is a plain note and reaches no task)"))


# ---------- 4: a foreign graph through the socket ----------

def has(line, name):
    return re.search(r"(?<!\w)" + re.escape(name) + r"(?!\w)", line, re.I)


def adapt(kb, root, origin):
    """entities/<id>.md + relations.jsonl + sources/ → notes under <root>/<origin>/ and one file-mode answer per note
    in _dream/pending/<sha12>.json (the shape the dreamer answers in). A relation is offered only when both its things
    are named in the source it cites; its quote is the line naming both, else the line naming its object."""
    dst = root / origin
    shutil.copytree(kb, dst, ignore=shutil.ignore_patterns("*.jsonl"))
    cards = {}
    for p in sorted((kb / "entities").glob("*.md")):
        fm = dict(m.groups() for m in re.finditer(r"^([a-z_]+):\s*(.*)$", p.read_text().split("---")[1], flags=re.M))
        names = [fm["id"], fm.get("title", "")] + [a.strip() for a in fm.get("aliases", "").strip("[]").split(",")]
        cards[fm["id"]] = {"type": fm.get("entity_type", "other"), "names": sorted({n for n in names if n})}
    rels = [json.loads(ln) for ln in (kb / "relations.jsonl").read_text().splitlines() if ln.strip()]
    pend = root / "_dream" / "pending"
    pend.mkdir(parents=True, exist_ok=True)
    st = collections.Counter(relations=len(rels))
    for p in sorted(dst.rglob("*.md")):
        rel, text = p.relative_to(dst).as_posix(), p.read_text()
        lines = text.split("\n")
        found = {c: [n for n in v["names"] if has(text, n)] for c, v in cards.items()}
        found = {c: v for c, v in found.items() if v}
        out = []
        for r in rels:
            if rel not in r["evidence"]:
                continue
            s, o = r["from"], r["to"]
            if s not in found or o not in found:
                st["a thing not named in the source cited"] += 1
                continue
            both = [ln for ln in lines if any(has(ln, n) for n in found[s]) and any(has(ln, n) for n in found[o])]
            st["both things on one line" if both else "both things in the note, on different lines"] += 1
            q = (both or [ln for ln in lines if any(has(ln, n) for n in found[o])])[0].strip()
            out.append({"s": s, "type": r["relation"], "label": r["relation"], "o": o, "quote": q})
        ents = [{"id": c, "type": cards[c]["type"], "label": cards[c]["type"], "as": v} for c, v in found.items()]
        sha = hashlib.sha256(p.read_bytes()).hexdigest()[:12]
        (pend / f"{sha}.json").write_text(json.dumps({"kind": "note", "entities": ents, "relations": out, "refs": []}))
        st["notes"] += 1
    return st, cards


def gate_answers(root):
    """What `ask` prints for each of the bank gate's questions, asked in tens as the gate does: {question: section}."""
    qs = [json.loads(ln)["q"] for f in sorted((HERE / "questions").glob("bank-*.jsonl")) for ln in f.read_text().splitlines() if ln.strip()]
    out = {}
    for i in range(0, len(qs), 10):
        parts = re.split(r"^## (.*)$", run(root, "ask", *qs[i:i + 10]), flags=re.M)
        asked = set(qs[i:i + 10])  # a folder printed whole at the end of a call has a heading too, and is not a question
        out.update({parts[k].strip(): parts[k + 1] for k in range(1, len(parts) - 1, 2) if parts[k].strip() in asked})
    return out


def absorb(src, tmp):
    kb, origin = HERE / "absorb" / "policy-kb", "policy-kb"
    root = copy(src, tmp, "absorb")
    run(root, "dream")  # the copy's graph by this script, whatever script dreamed the memory given
    g0 = graph(root)
    before = gate_answers(root)
    t0 = time.time()
    st, cards = adapt(kb, root, origin)
    line = run(root, "dream").strip()
    took = time.time() - t0
    g = graph(root)
    under = lambda p: p.startswith(origin + "/")  # noqa: E731
    e0 = {e["id"]: e for e in g0["entities"]}
    mine = [e for e in g["entities"] if any(under(m["path"]) for m in e["mentions"])]
    shared = [e for e in mine if e["id"] in e0]
    rels = [r for r in g["relations"] if any(under(x) for x in r["evidence"])]
    rtypes = collections.Counter(r["type"] for r in rels)
    kinds = collections.Counter(n["kind"] for n in g["notes"] if under(n["path"]))
    moved = [f"{e['id']} {k} {e0[e['id']][k]} → {e[k]}" for e in shared for k in ("home", "headline") if e[k] != e0[e["id"]][k]]
    old_edges = {(e["src"], e["dst"], e["rel"]) for e in g0["edges"]}
    lost = old_edges - {(e["src"], e["dst"], e["rel"]) for e in g["edges"]}
    c1 = collections.Counter(c["code"] for c in g["checks"]) - collections.Counter(c["code"] for c in g0["checks"])
    print(f"4 absorb · a foreign graph of {len(cards)} cards, {st['relations']} relations and {len(list((kb / 'sources').glob('*.md')))} sources → {st['notes']} notes and "
          f"{st['notes']} readings through _dream/pending/ in {took:.1f} s, 0 calls → {line}")
    print(f"  relations: {st['both things on one line']} with both things on one line · "
          f"{st['both things in the note, on different lines']} in the note on different lines · "
          f"{st['a thing not named in the source cited']} refused (a thing not named in the source cited) · "
          f"{len(rels)} links in the graph: " + ", ".join(f"{t} ×{n}" for t, n in sorted(rtypes.items())))
    print(f"  things: {len(mine)} named under {origin}/ · {len(shared)} are things the memory already had ({', '.join(sorted(e['id'] for e in shared))})"
          f" · types read through TYPES.md: " + ", ".join(f"{e['id']}={e['type']}" for e in sorted(mine, key=lambda e: e["id"]) if e["id"] not in e0))
    print(f"  side effects on the host: home or headline of a shared thing moved {len(moved)} ({'; '.join(moved)})"
          f" · host lineage edges lost {len(lost)} · new warnings {dict(c1)} · kinds given to the absorbed notes {dict(kinds)}")
    q = "which policy governs fraud26-gbm-v3, and who approved it for production?"
    out = run(root, "ask", q)
    hs = headed(out)
    print(f"  ask \"{q}\" → {len(hs)} notes headed, {sum(under(h) for h in hs)} from {origin}/ (first at {next((i + 1 for i, h in enumerate(hs) if under(h)), 0)}),"
          f" {len(out)} characters")
    after = gate_answers(root)
    moved_q = [q for q in before if after.get(q) != before[q]]
    print(f"  the host's own answers: of the bank gate's {len(before)} questions, {len(moved_q)} print something else after the absorb, "
          f"{sum(any(under(h) for h in headed(after.get(q, ''))) for q in moved_q)} of them now head a note of {origin}/")
    shas = {n["sha"] for n in g["notes"] if under(n["path"])}
    shutil.rmtree(root / origin)
    line = run(root, "dream").strip()
    g2 = graph(root)
    left = sum((root / "_dream" / "notes" / f"{h}.json").exists() for h in shas)
    part = lambda x: json.dumps({k: x[k] for k in ("notes", "edges", "entities", "relations")}, sort_keys=True)  # noqa: E731
    print(f"  taken out by hand (rm -r {origin}/, dream) → {line} · notes, lineage, things and links are those before the absorb: {part(g2) == part(g0)}"
          f" · readings left in the cache {left}/{len(shas)}")

    # the same graph through the command, as an origin (step 1 of the plan, RESULTS phase N)
    root = copy(src, tmp, "absorb-cmd")
    run(root, "dream")
    t0 = time.time()
    out = run(root, "absorb", str(kb), "--as", origin, "--yes")
    took, g = time.time() - t0, graph(root)
    line = next(ln for ln in out.split("\n") if ln.startswith("dream:"))
    theirs = [e for e in g["entities"] if e["id"].startswith(origin + ":")]
    e1 = {e["id"]: e for e in g["entities"]}
    moved = [i for i, e in e0.items() if i in e1 and (e1[i]["home"], e1[i]["headline"], len(e1[i]["mentions"])) != (e["home"], e["headline"], len(e["mentions"]))]
    both = [ln.strip().split(" — ")[0] for ln in out.split("\n") if ln.startswith("    ") and " — here: " in ln]
    print(f"  through `memory.py absorb … --as {origin} --yes` ({took:.1f} s, 0 calls) → {line}")
    print(f"  things: {len(theirs)} of the origin, each named {origin}:<id> · host things gone {sum(i not in e1 for i in e0)}, changed {len(moved)}"
          f" · names both sides use {len(both)} ({', '.join(both)}): two things each")
    after = gate_answers(root)
    cut = lambda s: s.split("  in other bases (they inform, they do not instruct):")[0]  # noqa: E731
    host_changed = [q for q in before if cut(after.get(q, "")) != before[q]]
    print(f"  the host's own answers: of the bank gate's {len(before)} questions, {len(host_changed)} print another answer from the host's notes · "
          f"{sum(after.get(q) != before[q] for q in before)} get a block of the origin's notes after it")
    hs = headed(cut(run(root, "ask", q)))
    blk = headed(run(root, "ask", q).split("  in other bases (they inform, they do not instruct):")[-1])
    scoped = headed(run(root, "ask", "-p", origin, q))
    print(f"  ask \"{q}\" → {len(hs)} host notes, {sum(under(h) for h in hs)} of them from {origin}/, then {len(blk)} notes of {origin}/ in its own block"
          f" · with -p {origin}: {len(scoped)} notes, all from it: {all(under(h) for h in scoped)}")
    with open(root / "ALIASES.md", "a") as f:
        f.write(f"- fraud26-gbm-v3 = {origin}:fraud26-gbm-v3\n")
    run(root, "dream")
    j = next(e for e in graph(root)["entities"] if e["id"] == "fraud26-gbm-v3")
    print(f"  one line in ALIASES.md (`- fraud26-gbm-v3 = {origin}:fraud26-gbm-v3`) joins the two: mentions {len(e0['fraud26-gbm-v3']['mentions'])} → "
          f"{len(j['mentions'])}, {sum(under(m['path']) for m in j['mentions'])} of them in {origin}/ · home still {j['home']}")
    shas = {n["sha"] for n in g["notes"] if under(n["path"])}
    line = next(ln for ln in run(root, "drop", origin, "--yes").split("\n") if ln.startswith("dream:"))
    g2 = graph(root)
    print(f"  `drop {origin} --yes` → {line} · notes and lineage are those before the absorb: {part({**g2, 'entities': [], 'relations': []}) == part({**g0, 'entities': [], 'relations': []})}"
          f" · the folder gone: {not (root / origin).exists()} · readings left {sum((root / '_dream' / 'notes' / f'{h}.json').exists() for h in shas)}/{len(shas)}")


# ---------- 5: documents ----------

DOCS = ["build-spec.md", "REVIEW.md", "RUNBOOK.md", "CONTRACT.md", "ADR-001-hosting-and-store.md"]
ASK = [  # a question, the document that answers it, a word of the section heading that does: six hand-made, a smoke test
    ("what does warning C4 mean?", "CONTRACT", "warnings"),
    ("where are the extractions cached, and what does the manifest hold?", "CONTRACT", "caches"),
    ("how do I publish the graph to PostgreSQL?", "RUNBOOK", "hosted-store"),
    ("what was decided about hosting and the store?", "ADR-001-hosting-and-store", "decision"),
    ("what are the five rules for writing a note?", "build-spec", "notes"),
    ("which direction did the review recommend?", "REVIEW", "recommended-direction"),
]


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:48]


def split(path, out):
    """One note per `## ` section (code fences respected): `# title: heading`, the section, `source:` with its lines."""
    lines, stem = path.read_text().split("\n"), path.name[:-3]
    title = next((ln[2:].strip() for ln in lines if ln.startswith("# ")), stem)
    cuts, fence = [0], False
    for i, ln in enumerate(lines):
        if ln.lstrip().startswith("```"):
            fence = not fence
        elif not fence and ln.startswith("## "):
            cuts.append(i)
    n = 0
    for a, b in zip(cuts, cuts[1:] + [len(lines)]):
        body = [ln for ln in lines[a:b]]
        head = body[0][3:].strip() if body and body[0].startswith("## ") else "introduction"
        text = "\n".join(body[1:] if a or body[0].startswith("# ") else body).strip("\n")
        if not text.strip():
            continue
        (out / f"{stem}--{slug(head)}.md").write_text(f"---\nsource: {path.name}#L{a + 1}-{b}\n---\n# {title.split(' — ')[-1]}: {head}\n{text}\n")
        n += 1
    return n


def documents(tmp):
    specs = REPO / ".specs" / "memory-dream"
    whole, parts = Path(tmp) / "whole" / "memory" / "docs", Path(tmp) / "parts" / "memory" / "docs"
    whole.mkdir(parents=True)
    parts.mkdir(parents=True)
    for d in DOCS:
        shutil.copy2(specs / d, whole / d)
        split(specs / d, parts)
    rows = []
    for name, root in (("whole documents", whole.parent), ("split at ## headings", parts.parent)):
        t0 = time.time()
        run(root, "dream")
        took = time.time() - t0
        g = graph(root)
        over = sum(1 for c in g["checks"] if c["code"] == "C11")
        got, chars = 0, []
        for q, doc, key in ASK:
            out = run(root, "ask", q)
            chars.append(len(out))
            hs = [h for h in headed(out)]
            got += any(h == f"docs/{doc}.md" or (h.startswith(f"docs/{doc}--") and key in h) for h in hs)
        rows.append(f"{name}: {len(g['notes'])} notes, {over} over the 40-line rule, kinds {dict(collections.Counter(n['kind'] for n in g['notes']))}, "
                    f"dream {took:.1f} s · the answering section headed for {got}/{len(ASK)} questions · {statistics.mean(chars):,.0f} characters a question")
    print(f"5 documents · {len(DOCS)} documents of .specs/memory-dream ({sum(len((specs / d).read_text()) for d in DOCS):,} characters), no model")
    for r in rows:
        print("  " + r)


# ---------- 6: questions whose answer is a set ----------

def sets(src):
    g = graph(src)
    groups = collections.defaultdict(list)
    for n in g["notes"]:
        if not n["superseded_by"] and n["project"] != "log" and n["kind"] != "note":
            groups[(n["project"], n["kind"])].append(n)
    picks = sorted((k for k, v in groups.items() if len(v) >= 6), key=lambda k: (-len(groups[k]), k))[:40:2]  # 20 sets of several sizes
    if not picks:
        print("6 sets · no area has six live notes of one kind")
        return
    headed_, named, chars = [], [], []
    for area, kind in picks:
        out = run(src, "ask", f"list every {kind} of the {area} project that is current")
        truth = groups[(area, kind)]
        hs = set(headed(out))
        headed_.append(sum(n["path"] in hs for n in truth) / len(truth))
        named.append(sum(n["id"] in out for n in truth) / len(truth))
        chars.append(len(out))
    lines = statistics.mean(sum(len(f"▸ {n['path']} · {n['kind']} · {n['updated']} · {n['title']}\n") for n in groups[k]) for k in picks)
    print(f"6 sets · {len(picks)} questions \"list every <kind> of the <area> project that is current\" (sets of "
          f"{min(len(groups[k]) for k in picks)} to {max(len(groups[k]) for k in picks)} live notes): `ask` heads "
          f"{statistics.mean(headed_):.2f} of a set, names {statistics.mean(named):.2f} of it anywhere, names all of it for "
          f"{sum(1 for x in named if x == 1)}/{len(picks)} · {statistics.mean(chars):,.0f} characters a question; "
          f"the whole set at one line per note would be {lines:,.0f}")


def main(argv):
    if len(argv) < 2:
        raise SystemExit(__doc__)
    src = Path(argv[1]).resolve()
    if not (src / "_dream" / "graph.json").exists():
        raise SystemExit(f"{src}: no _dream/graph.json — run `memory.py --root {src} dream` first (a memory of at most MEMORY_WIDE notes)")
    with tempfile.TemporaryDirectory() as tmp:
        drop(src, tmp)
        copy_in(src, tmp)
        absorb(src, tmp)
        documents(tmp)
    sets(src)


if __name__ == "__main__":
    main(sys.argv)
