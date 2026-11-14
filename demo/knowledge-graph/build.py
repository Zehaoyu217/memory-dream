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
dreamed with a model command: the things and their links are what its keepers read). Its things' tags are the type
(family/type), the projects whose notes name a thing, the tags of those notes, when it was last noted, and About, the
line of the note that best says what it is; its links' tags are the kind of note that states each, when, and whether
that note was replaced.

Any other graph, as JSON: {"nodes": [...], "links": [...]} ("edges" works for "links"). The data model:

  A thing (a node): "id" (required, unique), "label" (the name shown; the id when absent) and "group" (its island;
  without groups, or when one group holds more than half the nodes, the islands are the communities of the links).
  Every other field is a tag. A node with no link is left out.
  A link: "source" and "target" (ids, required), "type" (links-to when absent), "direction" (-> from source to target,
  the default; <- from target to source; o-o none: equal, related, the same either way) and "text" (the line that
  says so, at most 220 characters). Every other field is a tag. One link per ends, type and direction.
  A tag: a column, in each row a value or several (a list, or ";" between them). Four sorts, told by the values:
    category  values that repeat (type, team, status); a value may be a path whose levels are split by "/"
              (dataset/table/daily). The page colours by one category (a switch in its legend; "type" first, or
              --colour): the seven top-level values with the most things a colour each, the rest one grey; the
              legend opens each value into the levels under it; pointing lights, clicking hides; search finds them.
    time      ISO dates or moments (2025-11, 2025-11-03, 2025-11-03T10:22Z): a category of year / month / day, read
              as 2025, Nov 2025, 3 Nov 2025, in the order of time.
    number    every value a number (weight, confidence, rows): shown with its owner. A thing's "size" sizes its dot
              (its number of links when absent) and a link's "weight" its line and how hard it pulls its ends together.
    text      long, or mostly its own (a definition, a description, a citation): kept whole, shown with its owner
              and searched with it.
  Weight, time and provenance are tags like any other: provenance is whichever tags say where a link comes from (a
  category such as the system that found it, a time such as when, a text such as the citation).

Three optional entries beside them hold the vocabulary:
  "columns":      {"type": {"name": "Kind", "parents": {"table": "dataset"}, "names": {"dataset": "Datasets"},
                            "colours": {"dataset": "#2b8073"}},
                   "definition": {"sort": "text"}, "rows": {"use": "size"}}
  "link_columns": {"confidence": {"use": "weight"}, "observed": {"name": "Seen"}}
  "link_types":   {"feeds": {"name": "Feeds", "inverse": "Fed by"}, "same-as": {"direction": "o-o"}}
parents puts flat values under others (a hierarchy over a column), names and colours (hex) set the legend's words
and hues, "sort" settles a column's sort (category, time, number, text), and "use" makes another number column the
size or the weight. link_types says how a link type reads forwards and back, and its direction when a link does not
say (same-as, related-to, similar-to, equivalent-to and compared-with have none; the rest point source to target).

Or as two CSV files, a table each: nodes (an id column, label, group and tag columns) and links (source, target, and
type, direction, text and tag columns). A cell with ";" in it holds several values.

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

NODE_RESERVED = ("id", "label", "group")
LINK_RESERVED = ("source", "target", "type", "direction", "text", "id")
SORTS = ("category", "time", "number", "text")
BOTH = {"same-as", "related-to", "similar-to", "equivalent-to", "compared-with"}   # no direction unless told
ARROWS = {"->": 1, "→": 1, "out": 1, "forward": 1, "<-": -1, "←": -1, "in": -1, "back": -1, "backward": -1,
          "o-o": 0, "<->": 0, "↔": 0, "--": 0, "-": 0, "none": 0, "both": 0, "undirected": 0, "bidirectional": 0}


def from_memory(root, title):
    M.load_domain(root)
    g, _ = M.load(root)
    data = M.kg_data(root, g)
    if not data:
        raise SystemExit(f"{root}: no two things are linked; dream it with a model command first")
    if title:
        data["title"] = data["headline"] = title
    return data


def tag_columns(rows, about, reserved):
    """The tag columns of some rows (nodes or links): every field but the reserved ones, in the order they first
    appear, each of a sort told by its values or settled by "sort" in `about`. -> (keys, {key: sort}, [tags per row])"""
    keys = []
    for r in rows:
        keys += [k for k, v in r.items() if k not in reserved and k not in keys and not isinstance(v, dict)]
    sorts, tags = {}, [{} for _ in rows]
    for k in keys:
        a = about.get(k) or {}
        s = a.get("sort") if a.get("sort") in SORTS else "text" if a.get("text") is True else "category" if a.get("text") is False else None
        sorts[k] = s or M.kg_sort([r.get(k) for r in rows])
        parents = a.get("parents") if isinstance(a.get("parents"), dict) else None
        for r, t in zip(rows, tags):
            c = M.kg_cell(r.get(k), parents, sorts[k])
            if c is not None:
                t[k] = c
    keys = [k for k in keys if any(k in t for t in tags)]
    return keys, {k: sorts[k] for k in keys}, tags


def column(k, a, sort, tags):
    """A tag column as the page reads it: its key, name and sort, the legend's names and hues, what it is used for."""
    col = {"key": k, "name": str(a.get("name") or k.replace("_", " ").replace("-", " ").capitalize())}
    if sort != "category":
        col[sort] = True                                   # time, number or text
    names = {M.kg_path(p): str(n) for p, n in a["names"].items()} if isinstance(a.get("names"), dict) else {}
    if sort == "time":                                     # 2025, Nov 2025, 3 Nov 2025
        names = {**M.kg_time_names(v for t in tags for v in M.kg_vals(t.get(k))), **names}
    if names:
        col["names"] = names
    given = a.get("colours") or a.get("colors")
    if isinstance(given, dict):
        col["colours"] = {M.kg_path(p): str(c) for p, c in given.items()}
    elif k == "type" and sort == "category":
        col["colours"] = M.KG_COLOURS                      # the common families keep the hues they have in a memory
    if a.get("use") in ("size", "weight") and sort == "number":
        col["use"] = a["use"]
    return col


def from_json(doc, title, colour=None):
    nodes = {str(n["id"]): n for n in doc.get("nodes", [])}
    kinds = doc.get("link_types") if isinstance(doc.get("link_types"), dict) else {}

    def arrow(x, ty):                                      # 1: source to target, 0: none; <- is turned round below
        d = x.get("direction")
        if d is None:
            d = (kinds.get(ty) or {}).get("direction") if isinstance(kinds.get(ty), dict) else None
        if d is None:
            return 0 if ty in BOTH else 1
        return ARROWS.get(str(d).strip().lower(), 1)
    seen, links, given = set(), [], []
    for x in doc.get("links", doc.get("edges", [])):
        s, t, ty = str(x["source"]), str(x["target"]), str(x.get("type") or "links-to")
        d = arrow(x, ty)
        if d < 0:
            s, t, d = t, s, 1
        key = (s, t, ty, d) if d else (min(s, t), max(s, t), ty, d)
        if s == t or s not in nodes or t not in nodes or key in seen:
            continue
        seen.add(key)
        links.append({"s": s, "t": t, "type": ty, "q": str(x.get("text") or "")[:220], "note": None, **({} if d else {"dir": 0})})
        given.append(x)
    if not links:
        raise SystemExit("no links between the nodes given")
    deg = Counter(i for x in links for i in (x["s"], x["t"]))
    kept = sorted(deg, key=lambda i: (-deg[i], i))
    labels = {i: str(nodes[i].get("label") or i) for i in kept}
    home, isles = M.kg_islands({i: str(nodes[i].get("group") or "") for i in kept}, [(x["s"], x["t"]) for x in links],
                               labels, middle="in no group", kind="group")
    # the things' tags: every field of a node but its id, label and group
    about = doc.get("columns") if isinstance(doc.get("columns"), dict) else {}
    keys, sorts, rows = tag_columns([nodes[i] for i in kept], about, NODE_RESERVED)
    tags = dict(zip(kept, rows))
    cats = [k for k in keys if sorts[k] in ("category", "time")]
    if not cats:                                           # no category at all: one, so the legend still counts them
        k0 = "type" if "type" not in keys else "kind"
        keys, sorts, cats = [k0] + keys, {k0: "category", **sorts}, [k0]
        for i in kept:
            tags[i][k0] = "thing"
    first = colour if colour in cats else "type" if "type" in cats else cats[0]
    keys = [first] + [k for k in cats if k != first] + [k for k in keys if sorts[k] == "number"] + [k for k in keys if sorts[k] == "text"]
    columns = [column(k, about.get(k) or {}, sorts[k], [tags[i] for i in kept]) for k in keys]
    size = next((c["key"] for c in columns if c.get("use") == "size"), "size" if sorts.get("size") == "number" else None)
    # the links' tags: every field but source, target, type, direction, text and id
    link_about = doc.get("link_columns") if isinstance(doc.get("link_columns"), dict) else {}
    lkeys, lsorts, ltags = tag_columns(given, link_about, LINK_RESERVED)
    link_columns = [column(k, link_about.get(k) or {}, lsorts[k], ltags) for k in lkeys]
    weight = next((c["key"] for c in link_columns if c.get("use") == "weight"), "weight" if lsorts.get("weight") == "number" else None)
    for l, t in zip(links, ltags):
        if t:
            l["tags"] = t
        w = M.kg_vals(t.get(weight))[:1] if weight else []
        if w and w[0] > 0 and w[0] != 1:
            l["w"] = w[0]

    def dot(i):                                            # its size, or its number of links
        v = M.kg_vals(tags[i].get(size))[:1] if size else []
        return v[0] if v and v[0] > 0 else deg[i]
    index = {i: k for k, i in enumerate(kept)}
    things = [{"id": i, "label": labels[i], "n": dot(i), "home": home[i], "tags": tags[i], "names": [labels[i]], "notes": []}
              for i in kept]
    for x in links:
        x["s"], x["t"] = index[x["s"]], index[x["t"]]
    clusters = any(v["kind"] == "cluster" for v in isles.values())
    forward = {str(t): str(d["name"]) for t, d in kinds.items() if isinstance(d, dict) and d.get("name")}
    inverse = {str(t): str(d["inverse"]) for t, d in kinds.items() if isinstance(d, dict) and d.get("inverse")}
    return {"title": title or "Knowledge graph", "headline": title or f"{len(things):,} things, {len(links):,} links",
            "lede": "Every thing in the graph and every link between two of them. "
                    + ("An island is a group of things that link mostly to each other." if clusters else "An island is a group."),
            "stats": [("things", len(things)), ("links", len(links)), ("islands", len(isles))],
            "meta": {"notes": 0, "isles": isles, "inverse": inverse, "forward": forward, "link_columns": link_columns,
                     "link_values": M.kg_counts(ltags, link_columns), "both": sum(1 for x in links if x.get("dir") == 0)},
            "columns": columns, "things": things, "links": links, "notes": []}


def from_csv(nodes_csv, links_csv):
    """Two tables as the JSON above: a cell with ';' in it holds several values; empty cells hold none."""
    def rows(p):
        with open(p, newline="", encoding="utf-8-sig") as f:
            return [{(k or "").strip(): (v or "").strip() for k, v in r.items() if k} for r in csv.DictReader(f)]
    nodes = [{k: v for k, v in r.items() if v != ""} for r in rows(nodes_csv)]
    links = [{k: v for k, v in r.items() if v != ""} for r in rows(links_csv)]
    return {"nodes": [n for n in nodes if "id" in n], "links": [r for r in links if r.get("source") and r.get("target")]}


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
