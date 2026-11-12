#!/usr/bin/env python3
"""How much of the lineage that the frontmatter used to carry does a memory of the worn bank hold? No model.

  python3 eval/hard/lineage_score.py <dreamed worn memory> <truth.json> [--areas a,b,…]

truth.json (from make_hard.py) has every `from` and `supersedes` link of the tidy bank and how the worn bank states
it. The dreamed memory's graph is compared with it, link by link:

  as lineage    the graph has the same edge, same direction (from frontmatter there is none: a keeper read it)
  as a mention  the graph links the two notes only as `refs`: it knows one names the other, not which way or why
  missing       no edge between the two notes
  wrong         lineage edges of the graph that the truth does not have (shown beside the count that is right)

Counted over all links, and apart for the three ways a link is stated: by the other note's id where the note always
had it, by its id in the added sentence, by a phrase in the added sentence. Quoted in RESULTS.md phase S.
"""
import collections
import json
import sys
from pathlib import Path


def main(argv):
    mem, truth = Path(argv[1]), json.loads(Path(argv[2]).read_text())
    only = set(argv[argv.index("--areas") + 1].split(",")) if "--areas" in argv else None
    gf = mem / "_dream" / "graph.json"
    g = json.loads(gf.read_text())
    edges = collections.defaultdict(set)
    for e in g["edges"]:
        edges[(e["src"], e["dst"])].add(e["rel"])
        if e["rel"] == "refs":
            edges[(e["dst"], e["src"])].add("refs~")
    area = lambda p: p.split("/")[0]  # noqa: E731
    rows = collections.defaultdict(collections.Counter)
    true = set()
    for e in truth["edges"]:
        if only and area(e["src"]) not in only:
            continue
        true.add((e["src"], e["dst"], e["rel"]))
        how = truth["stated"].get(f"{e['src']} {e['rel']} {e['dst']}", "?")
        got = edges.get((e["src"], e["dst"]), set())
        res = "as lineage" if e["rel"] in got else "as a mention" if got & {"refs", "refs~", "from", "supersedes"} else "missing"
        rows[(e["rel"], how)][res] += 1
        rows[(e["rel"], "all")][res] += 1
    made = [(e["src"], e["dst"], e["rel"]) for e in g["edges"] if e["rel"] in ("from", "supersedes")
            and (not only or area(e["src"]) in only)]
    wrong = [x for x in made if x not in true]
    print("link · how the worn bank states it · links · as lineage · as a mention · missing")
    for (rel, how), c in sorted(rows.items()):
        n = sum(c.values())
        print(f"{rel:<10} · {how:<24} · {n:>5} · {c['as lineage']:>5} ({c['as lineage'] / n:4.0%}) · {c['as a mention']:>5} ({c['as a mention'] / n:4.0%}) · "
              f"{c['missing']:>5} ({c['missing'] / n:4.0%})")
    right = len(made) - len(wrong)
    print(f"lineage edges in the graph: {len(made)}, of which {right} are true ({right / max(1, len(made)):.0%}) and {len(wrong)} are not"
          + (": " + "; ".join(f"{s} {r} {d}" for s, d, r in wrong[:4]) if wrong else ""))
    by = collections.Counter(e.get("by", "frontmatter") for e in g["edges"] if e["rel"] in ("from", "supersedes") and (not only or area(e["src"]) in only))
    print("by:", dict(by), "· dedup counts:", {k: v for k, v in (g.get("dedup") or {}).items() if k.startswith("lineage")})


if __name__ == "__main__":
    main(sys.argv)
