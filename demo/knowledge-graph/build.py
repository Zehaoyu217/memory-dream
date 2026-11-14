#!/usr/bin/env python3
"""The knowledge-graph page for any graph, as one HTML file that opens offline.

  python3 demo/knowledge-graph/build.py <graph.json | memory folder> <out.html> [--title "…"] [--theme paper|star]

--theme: the look the page opens in, paper (the default) or star (a star map at night); a switch in its header flips
between the two.

A memory: the same page `memory.py viz` and every dream write to memory/_dream/knowledge-graph.html (it needs a memory
dreamed with a model command: the things and their links are what its keepers read).

Any other graph, as JSON: {"nodes": [{"id": …}], "links": [{"source": …, "target": …}]} ("edges" works for "links").
A node may add "label", "type" (the colours: the most common types get one each) and "group" (the islands; without
groups, or when one group holds more than half the nodes, the islands are the communities of the links), and "size"
(the dot; the number of links when absent). A link may add "type" and "text" (the line shown with it). Nodes with no
link are left out.

The page is skills/memory-dream/assets/knowledge-graph.html, written under the html-harness habits; memory.py's kg_*
functions fill it. d3 7.9.0 (ISC) is pasted in.
"""
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "skills" / "memory-dream" / "scripts"))
import memory as M  # noqa: E402


def from_memory(root, title):
    M.load_domain(root)
    g, _ = M.load(root)
    data = M.kg_data(root, g)
    if not data:
        raise SystemExit(f"{root}: no two things are linked; dream it with a model command first")
    if title:
        data["title"] = data["headline"] = title
    return data


def from_json(doc, title):
    nodes = {str(n["id"]): n for n in doc.get("nodes", [])}
    seen, links = set(), []
    for x in doc.get("links", doc.get("edges", [])):
        s, t, ty = str(x["source"]), str(x["target"]), str(x.get("type") or "links-to")
        if s == t or s not in nodes or t not in nodes or (s, t, ty) in seen:
            continue
        seen.add((s, t, ty))
        links.append({"s": s, "t": t, "type": ty, "q": str(x.get("text") or "")[:220], "note": None})
    if not links:
        raise SystemExit("no links between the nodes given")
    deg = Counter(i for x in links for i in (x["s"], x["t"]))
    kept = sorted(deg, key=lambda i: (-deg[i], i))
    labels = {i: str(nodes[i].get("label") or i) for i in kept}
    kind = {i: str(nodes[i].get("type") or "thing") for i in kept}
    home, isles = M.kg_islands({i: str(nodes[i].get("group") or "") for i in kept}, [(x["s"], x["t"]) for x in links],
                               labels, middle="in no group", kind="group")
    groups, group = M.kg_groups(kind)
    index = {i: k for k, i in enumerate(kept)}
    things = [{"id": i, "label": labels[i], "type": kind[i], "g": group[i], "n": nodes[i].get("size") or deg[i],
               "home": home[i], "names": [labels[i]], "notes": []} for i in kept]
    for x in links:
        x["s"], x["t"] = index[x["s"]], index[x["t"]]
    clusters = any(v["kind"] == "cluster" for v in isles.values())
    return {"title": title or "Knowledge graph", "headline": title or f"{len(things):,} things, {len(links):,} links",
            "lede": "Every thing in the graph and every link between two of them. "
                    + ("An island is a group of things that link mostly to each other." if clusters else "An island is a group."),
            "stats": [("things", len(things)), ("links", len(links)), ("islands", len(isles))],
            "meta": {"notes": 0, "isles": isles, "inverse": {}}, "groups": groups, "things": things, "links": links, "notes": []}


def main(argv):
    if len(argv) < 3:
        raise SystemExit(__doc__)
    src, out = Path(argv[1]).expanduser(), Path(argv[2]).expanduser()
    title = argv[argv.index("--title") + 1] if "--title" in argv else None
    theme = argv[argv.index("--theme") + 1] if "--theme" in argv else "paper"
    data = from_memory(src.resolve(), title) if src.is_dir() else from_json(json.loads(src.read_text()), title)
    page = M.kg_page(**data, theme=theme)
    out.write_text(page)
    print(f"{out}: {len(data['things']):,} things, {len(data['links']):,} links, {len(data['meta']['isles'])} islands"
          f" · {len(page) / 1e6:.1f} MB")


if __name__ == "__main__":
    main(sys.argv)
