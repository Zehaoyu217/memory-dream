#!/usr/bin/env python3
"""What do plain graph methods find in a dreamed memory's graph? (PLAN.md §7) Standard library, no model, seconds.

  graph_probe.py <memory root> [--conflicts <a reviewed CONFLICTS.md>]

Reads `_dream/graph.json` and prints, method by method, what it finds today:
  cycles     strongly connected groups in each link type and in note lineage (a `replaces` or `from` loop is a
             contradiction by construction)
  hubs       things mentioned across many areas, and how many have no note of their own (one name for several things?)
  bridges    links whose removal splits the graph, and how many rest on one line of evidence
  parallel   pairs of things joined by two link types at once (a type that implies another; a smell)
  roles      what links the things of one family usually carry, and the roles several projects share
  twins      things with the same typed neighbours (siblings: the near-misses of each other's definitions)
  exact      Weisfeiler-Lehman colours: how rarely two things have exactly the same surroundings
  conflicts  with --conflicts: do shared things tell the judged supersessions from the judged compatible pairs?
Nothing is written. The last line is the same numbers as JSON.
"""
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

root = Path(sys.argv[1])
g = json.loads((root / "_dream/graph.json").read_text())
ents = {e["id"]: e for e in g["entities"]}
rels = [r for r in g["relations"] if r["s"] in ents and r["o"] in ents]
notes = {n["path"]: n for n in g["notes"]}
out_json = {"notes": len(notes), "things": len(ents), "links": len(rels)}
fam = lambda t: t.split("/")[0]  # noqa: E731
area = lambda p: p.split("/")[0] if "/" in p else ""  # noqa: E731
areas_of = lambda v: {area(m["path"]) for m in ents[v]["mentions"]}  # noqa: E731


def sccs(nodes, out):
    """Strongly connected components of two or more nodes (Tarjan, iterative)."""
    index, low, on, stack, res, k = {}, {}, set(), [], [], 0
    for r in sorted(nodes):
        if r in index:
            continue
        index[r] = low[r] = k
        k += 1
        stack.append(r)
        on.add(r)
        work = [(r, iter(sorted(out.get(r, ()))))]
        while work:
            v, it = work[-1]
            for w in it:
                if w not in index:
                    index[w] = low[w] = k
                    k += 1
                    stack.append(w)
                    on.add(w)
                    work.append((w, iter(sorted(out.get(w, ())))))
                    break
                if w in on:
                    low[v] = min(low[v], index[w])
            else:
                work.pop()
                if work:
                    low[work[-1][0]] = min(low[work[-1][0]], low[v])
                if low[v] == index[v]:
                    comp = []
                    while True:
                        w = stack.pop()
                        on.discard(w)
                        comp.append(w)
                        if w == v:
                            break
                    if len(comp) >= 2:
                        res.append(sorted(comp))
    return res


print(f"{len(notes)} notes · {len(g['edges'])} lineage edges · {len(ents)} things · {len(rels)} links · "
      f"{len({r['type'] for r in rels})} link words ({sum(1 for t in {r['type'] for r in rels} if not t.startswith('other/'))} are types) · "
      f"{len({e['type'] for e in ents.values()})} thing words")

# ---- cycles
print("\ncycles — per link type: links · loops · of them two things pointing at each other · e.g.")
by_type, n_links, out_json["cycles"] = defaultdict(lambda: defaultdict(set)), Counter(r["type"] for r in rels), {}
for r in rels:
    by_type[r["type"]][r["s"]].add(r["o"])
for T, n in n_links.most_common():
    if T.startswith("other/") or n < 15:
        continue
    cs = sccs(set(by_type[T]) | {o for s in by_type[T] for o in by_type[T][s]}, by_type[T])
    out_json["cycles"][T] = len(cs)
    print(f"   {T:14} {n:5} · {len(cs):3} · {sum(1 for c in cs if len(c) == 2):3} · {cs[0][:3] if cs else '-'}")
lin = defaultdict(set)
for e in g["edges"]:
    if e["rel"] in ("from", "supersedes"):
        lin[e["src"]].add(e["dst"])
cs = sccs(set(lin) | {d for s in lin for d in lin[s]}, lin)
out_json["lineage_cycles"] = len(cs)
print(f"   lineage (from, supersedes): {len(cs)} loops holding {sum(map(len, cs))} notes · e.g. {cs[0][:3] if cs else '-'}")

# ---- hubs
adj = defaultdict(set)
for r in rels:
    adj[r["s"]].add(r["o"])
    adj[r["o"]].add(r["s"])
spread = [v for v in ents if len(areas_of(v)) >= 5]
homeless = [v for v in spread if not ents[v]["home"]]
out_json["hubs"] = {"in_5_areas": len(spread), "no_own_note": len(homeless)}
print(f"\nhubs — things mentioned in 5+ areas: {len(spread)} · with no note of their own: {len(homeless)} · the widest:")
for v in sorted(ents, key=lambda v: (-len(ents[v]["mentions"]), v))[:6]:
    print(f"   {v:24} {ents[v]['type']:8} {len(ents[v]['mentions']):4} notes in {len(areas_of(v)):2} areas · {len(adj[v]):3} neighbours · "
          f"own note: {ents[v]['home'] or 'none'}")

# ---- components and bridges
seen, comps = set(), []
for v in sorted(ents):
    if v in seen:
        continue
    todo, comp = [v], []
    seen.add(v)
    while todo:
        x = todo.pop()
        comp.append(x)
        for y in adj[x]:
            if y not in seen:
                seen.add(y)
                todo.append(y)
    comps.append(comp)
big = max(comps, key=len)
disc, low, par, bridges, t = {}, {}, {}, [], 0
for r0 in big:
    if r0 in disc:
        continue
    disc[r0] = low[r0] = t
    t += 1
    work = [(r0, iter(sorted(adj[r0])))]
    while work:
        v, it = work[-1]
        for w in it:
            if w not in disc:
                par[w] = v
                disc[w] = low[w] = t
                t += 1
                work.append((w, iter(sorted(adj[w]))))
                break
            if w != par.get(v):
                low[v] = min(low[v], disc[w])
        else:
            work.pop()
            if work:
                u = work[-1][0]
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    bridges.append(frozenset((u, v)))
ev = defaultdict(set)
for r in rels:
    ev[frozenset((r["s"], r["o"]))] |= set(r["evidence"])
thin = sum(1 for b in bridges if len(ev[b]) <= 1)
alone = sum(1 for c in comps if len(c) == 1)
out_json["components"] = {"n": len(comps), "largest": len(big), "no_link": alone, "bridges": len(bridges), "bridges_one_line": thin}
print(f"\nbridges — {len(comps)} components, the largest holds {len(big)} of {len(ents)} things; {alone} things have no link · "
      f"{len(bridges)} bridges, {thin} resting on one line of evidence")

# ---- parallel links
pt = defaultdict(set)
for r in rels:
    pt[(r["s"], r["o"])].add(r["type"])
par2 = Counter(tuple(sorted(ts)) for ts in pt.values() if len(ts) >= 2)
out_json["parallel_pairs"] = sum(par2.values())
print(f"\nparallel — {sum(par2.values())} pairs joined by 2+ link words · most common: "
      + " · ".join(f"{a} + {b} ×{n}" for (a, b, *_), n in par2.most_common(5)))

# ---- roles and expected links
role = defaultdict(set)
for r in rels:
    if not r["type"].startswith("other/"):
        role[r["s"]].add((r["type"], ">", fam(ents[r["o"]]["type"])))
        role[r["o"]].add((r["type"], "<", fam(ents[r["s"]]["type"])))
groups, n_fam, carry = defaultdict(list), Counter(fam(ents[v]["type"]) for v in role), Counter()
for v, s in role.items():
    for x in s:
        carry[(fam(ents[v]["type"]), x)] += 1
    if len(s) >= 2:
        groups[(fam(ents[v]["type"]), tuple(sorted(s)))].append(v)
shared = {k: vs for k, vs in groups.items() if len(vs) >= 3 and len(set().union(*map(areas_of, vs))) >= 3}
out_json["roles"] = {"distinct": len(groups), "shared_by_3_things_in_3_areas": len(shared)}
print(f"\nroles — {len(groups)} distinct among {sum(map(len, groups.values()))} things with 2+ typed links · {len(shared)} shared by 3+ things across 3+ areas:")
for (f, s), vs in sorted(shared.items(), key=lambda kv: (-len(kv[1]), kv[0]))[:4]:
    print(f"   {len(vs):3} × {f}: " + ", ".join(f"{t}{d}{o}" for t, d, o in s))
print("   links most things of a family carry:")
expected = {}
for (f, x), n in sorted(carry.items(), key=lambda kv: (-kv[1], kv[0])):
    if n_fam[f] >= 30 and n / n_fam[f] >= 0.7:
        expected[f"{f}: {x[0]}{x[1]}{x[2]}"] = round(n / n_fam[f], 2)
        print(f"      {f}: {x[0]}{x[1]}{x[2]}  {n}/{n_fam[f]} = {n / n_fam[f]:.0%} — the other {n_fam[f] - n} are gaps to look at")
out_json["expected_links"] = expected

# ---- structural twins
sig, inv = defaultdict(set), defaultdict(set)
for r in rels:
    sig[r["s"]].add((r["type"], ">", r["o"]))
    sig[r["o"]].add((r["type"], "<", r["s"]))
for v, s in sig.items():
    for x in s:
        inv[x].add(v)
both = Counter()
for vs in inv.values():
    if 2 <= len(vs) <= 40:
        for a, b in combinations(sorted(vs), 2):
            both[(a, b)] += 1
twins = sorted(((n / len(sig[a] | sig[b]), n, a, b) for (a, b), n in both.items()
                if n >= 2 and fam(ents[a]["type"]) == fam(ents[b]["type"]) and n / len(sig[a] | sig[b]) >= 0.5), reverse=True)
named = {frozenset((p["a"], p["b"])) for p in g.get("review", [])}
out_json["twins"] = {"pairs": len(twins), "also_named_alike": sum(1 for *_, a, b in twins if frozenset((a, b)) in named)}
print(f"\ntwins — {len(twins)} pairs of one family share 2+ typed neighbours (Jaccard >= 0.5); "
      f"{out_json['twins']['also_named_alike']} of them are also in the name-based review list of {len(named)}")
for j, n, a, b in twins[:4]:
    print(f"   {j:.2f} · {n} shared · {a}  ~  {b}")

# ---- exact equivalence
col = {v: ents[v]["type"] for v in ents}
for _ in range(2):
    col = {v: hashlib.sha1((col[v] + "|" + "|".join(sorted(f"{t}{d}{col[o]}" for t, d, o in sig[v]))).encode()).hexdigest()[:10]
           for v in ents}
cls, linked = Counter(col.values()), [v for v in ents if sig[v]]
same = sum(1 for v in linked if cls[col[v]] >= 2)
out_json["exact"] = {"linked": len(linked), "share_exact_surroundings": same}
print(f"\nexact — Weisfeiler-Lehman, 2 rounds: {same} of {len(linked)} linked things have exactly the same surroundings as another "
      f"({same / max(1, len(linked)):.0%}): matching partial graphs needs approximate, seeded alignment, not hashing")

# ---- conflicts judged by a review
if "--conflicts" in sys.argv:
    note_ents, rows = defaultdict(set), defaultdict(list)
    for e in ents.values():
        for m in e["mentions"]:
            note_ents[m["path"]].add(e["id"])
    stems = defaultdict(list)
    for p in notes:
        stems[p.split("/")[-1][:-3]].append(p)

    def find(x):
        x = x if x.endswith(".md") else x + ".md"
        return x if x in notes else (stems[x.split("/")[-1][:-3]] + [None])[0] if len(stems[x.split("/")[-1][:-3]]) == 1 else None
    for ln in Path(sys.argv[sys.argv.index("--conflicts") + 1]).read_text().splitlines():
        m = re.match(r"-\s*(\S+)\s*([>?])\s*(\S+)", ln)
        c = re.match(r"compatible:\s*(\S+)\s*/\s*(\S+)", ln)
        a, b, verdict = (m.group(1), m.group(3), "supersedes" if m.group(2) == ">" else "unsure") if m else \
            (c.group(1), c.group(2), "compatible") if c else (None, None, None)
        a, b = (find(a), find(b)) if a else (None, None)
        if a and b:
            u = note_ents[a] | note_ents[b]
            rows[verdict].append(len(note_ents[a] & note_ents[b]) / len(u) if u else 0.0)
    print(f"\nconflicts — pairs a review judged, by the share of things the two notes have in common:")
    out_json["conflicts"] = {}
    base = len(rows["supersedes"]) / max(1, len(rows["supersedes"]) + len(rows["compatible"]))
    for thr in (0.0, 0.2, 0.3, 0.4):
        tp, fp = sum(x >= thr for x in rows["supersedes"]), sum(x >= thr for x in rows["compatible"])
        out_json["conflicts"][str(thr)] = {"supersedes": tp, "compatible": fp}
        print(f"   share >= {thr}: {tp} of {len(rows['supersedes'])} supersessions and {fp} of {len(rows['compatible'])} compatible pairs kept"
              f" -> precision {tp / max(1, tp + fp):.0%}" + (" (every pair the title words proposed)" if thr == 0 else ""))
print("\n" + json.dumps(out_json))
