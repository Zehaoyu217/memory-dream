#!/usr/bin/env python3
"""The knowledge-graph page for any graph, as one HTML file that opens offline.

  python3 demo/knowledge-graph/build.py <graph.json | memory folder> <out.html> [options]
  python3 demo/knowledge-graph/build.py <nodes.csv> <links.csv> <out.html> [options]
  options: --title "…"  --theme paper|star|gala|moon|fanfare|noir  --colour COLUMN

--theme: the look the page opens in: paper (the default), star (a star map at night), gala (a purple show at night,
starlight and lotto wheels), moon (moonlit: pale lilac and silver under a great moon, sparkles and drifting ribbons,
pearl rings), fanfare (a violet stage under sweeping spotlights, a checkered floor, bunting, marquee bulbs round
each island, candy-bright lotto balls) or noir (black and white on a checkered stage under one warm spotlight, white
and silver things, card suits round a picked thing, purple only as an accent); the last four fling confetti when a
thing is picked. A switch in its header picks among the six.

A memory: the same page `memory.py viz` and every dream write to memory/_dream/knowledge-graph.html (it needs a memory
dreamed with a model command: the things and their links are what its keepers read). Its tag columns are the type
(family/type), the projects whose notes name a thing and the tags of those notes.

Any other graph, as JSON: {"nodes": [{"id": …}], "links": [{"source": …, "target": …}]} ("edges" works for "links").
A node's "label" names it, "group" puts it on an island (without groups, or when one group holds more than half the
nodes, the islands are the communities of the links) and "size" sizes its dot (the number of links when absent).
Every other field of a node is a tag column: type, team, status, owner, whatever the data has. A value is text, or a
path whose levels are split by "/" (dataset/table/daily: the legend opens Datasets into Tables into Daily), or a list
of them (a thing with several), or text with ";" between values. The page colours by any column (a switch in its
legend), the first by default ("type" if there is one, or --colour): the seven top-level values with the most things
a colour each, the rest one grey, "Everything else"; pointing at any level lights its things, clicking hides them,
and search finds the values too. An optional "columns" entry beside "nodes" says more about a column:
  "columns": {"type": {"name": "Kind", "parents": {"table": "dataset", "view": "dataset"},
                       "names": {"dataset": "Datasets"}, "colours": {"dataset": "#2b8073"}}}
parents puts flat values under others (a hierarchy over a column), names and colours (hex) set the legend's words
and hues. A link may add "type" and "text" (the line shown with it). Nodes with no link are left out.

Or as two CSV files, a table each: nodes (an id column, and label, group, size and tag columns as above) and links
(source, target, and type and text). A cell with ";" in it holds several values.

The page is skills/memory-dream/assets/knowledge-graph.html, written under the html-harness habits; memory.py's kg_*
functions fill it. d3 7.9.0 (ISC) is pasted in.
"""
import csv
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "skills" / "memory-dream" / "scripts"))
import memory as M  # noqa: E402

RESERVED = ("id", "label", "group", "size")


def from_memory(root, title):
    M.load_domain(root)
    g, _ = M.load(root)
    data = M.kg_data(root, g)
    if not data:
        raise SystemExit(f"{root}: no two things are linked; dream it with a model command first")
    if title:
        data["title"] = data["headline"] = title
    return data


def from_json(doc, title, colour=None):
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
    home, isles = M.kg_islands({i: str(nodes[i].get("group") or "") for i in kept}, [(x["s"], x["t"]) for x in links],
                               labels, middle="in no group", kind="group")
    # the tag columns: every field of a node but its id, label, group and size, in the order they first appear
    about = doc.get("columns") if isinstance(doc.get("columns"), dict) else {}
    keys = []
    for i in kept:
        keys += [k for k, v in nodes[i].items() if k not in RESERVED and k not in keys and not isinstance(v, dict)]
    tags = {i: {} for i in kept}
    for k in keys:
        parents = (about.get(k) or {}).get("parents")
        for i in kept:
            c = M.kg_cell(nodes[i].get(k), parents if isinstance(parents, dict) else None)
            if c is not None:
                tags[i][k] = c
    keys = [k for k in keys if any(k in t for t in tags.values())]
    if not keys:                                           # no column at all: one, so the legend still counts them
        keys = ["type"]
        for i in kept:
            tags[i]["type"] = "thing"
    first = colour if colour in keys else "type" if "type" in keys else keys[0]
    keys.remove(first)
    keys.insert(0, first)
    columns = []
    for k in keys:
        a = about.get(k) or {}
        col = {"key": k, "name": str(a.get("name") or k.replace("_", " ").replace("-", " ").capitalize())}
        if isinstance(a.get("names"), dict):
            col["names"] = {M.kg_path(p): str(n) for p, n in a["names"].items()}
        given = a.get("colours") or a.get("colors")
        if isinstance(given, dict):
            col["colours"] = {M.kg_path(p): str(c) for p, c in given.items()}
        elif k == "type":
            col["colours"] = M.KG_COLOURS                  # the common families keep the hues they have in a memory
        columns.append(col)
    index = {i: k for k, i in enumerate(kept)}
    things = [{"id": i, "label": labels[i], "n": nodes[i].get("size") or deg[i], "home": home[i], "tags": tags[i],
               "names": [labels[i]], "notes": []} for i in kept]
    for x in links:
        x["s"], x["t"] = index[x["s"]], index[x["t"]]
    clusters = any(v["kind"] == "cluster" for v in isles.values())
    return {"title": title or "Knowledge graph", "headline": title or f"{len(things):,} things, {len(links):,} links",
            "lede": "Every thing in the graph and every link between two of them. "
                    + ("An island is a group of things that link mostly to each other." if clusters else "An island is a group."),
            "stats": [("things", len(things)), ("links", len(links)), ("islands", len(isles))],
            "meta": {"notes": 0, "isles": isles, "inverse": {}}, "columns": columns, "things": things, "links": links, "notes": []}


def from_csv(nodes_csv, links_csv):
    """Two tables as the JSON above: a cell with ';' in it holds several values; size, when a number, sizes the dot."""
    def rows(p):
        with open(p, newline="", encoding="utf-8-sig") as f:
            return [{(k or "").strip(): (v or "").strip() for k, v in r.items() if k} for r in csv.DictReader(f)]
    nodes = []
    for r in rows(nodes_csv):
        n = {k: v for k, v in r.items() if v != ""}
        if "size" in n:
            try:
                n["size"] = float(n["size"])
            except ValueError:
                del n["size"]
        if "id" in n:
            nodes.append(n)
    return {"nodes": nodes, "links": [r for r in rows(links_csv) if r.get("source") and r.get("target")]}


def main(argv):
    flags = {"--title", "--theme", "--colour", "--color"}
    pos, opt, k = [], {}, 1
    while k < len(argv):
        if argv[k] in flags and k + 1 < len(argv):
            opt[argv[k]] = argv[k + 1]
            k += 2
        else:
            pos.append(argv[k])
            k += 1
    if len(pos) < 2 or (pos[0].endswith(".csv") and len(pos) < 3):
        raise SystemExit(__doc__)
    title, theme = opt.get("--title"), opt.get("--theme", "paper")
    colour = opt.get("--colour") or opt.get("--color")
    src = Path(pos[0]).expanduser()
    if src.suffix == ".csv":
        data, out = from_json(from_csv(src, Path(pos[1]).expanduser()), title, colour), Path(pos[2]).expanduser()
    else:
        out = Path(pos[1]).expanduser()
        data = from_memory(src.resolve(), title) if src.is_dir() else from_json(json.loads(src.read_text()), title, colour)
    page = M.kg_page(**data, theme=theme)
    out.write_text(page)
    print(f"{out}: {len(data['things']):,} things, {len(data['links']):,} links, {len(data['meta']['isles'])} islands, "
          f"{len(data['columns'])} tag column{'s' if len(data['columns']) != 1 else ''} · {len(page) / 1e6:.1f} MB")


if __name__ == "__main__":
    main(sys.argv)
