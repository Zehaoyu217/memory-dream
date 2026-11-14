#!/usr/bin/env python3
"""A memory's knowledge graph as one page to show, offline: every thing its notes name and every link a note states
between two of them, each link with the line that says it.

  python3 demo/knowledge-graph/build.py <dreamed memory> <out.html> [--title "What these notes know"]

The memory must have been dreamed with a model command: the things and their links are what its keepers read, and a
memory dreamed with no model has none. One HTML file comes out, with d3 7.9.0 (ISC, vendor/) inside it, so it opens
anywhere with no network. The page is page.html, written under the html-harness habits; this script only fills its
data islands and its masthead.
"""
import collections
import html
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
GENERAL = {"prefs", "reporting", "glossary", "corrections", "howto", "qa", "people", "log", ""}
# six groups of things, one colour each: a graph of 1,000 things reads by a handful of hues, not by twenty
GROUPS = [
    ("models", "Models and experiments", "#2a55a3", ["model", "experiment"]),
    ("data", "Data and features", "#2b8073", ["dataset", "feature", "segment", "table"]),
    ("metrics", "Metrics", "#6b7a90", ["metric"]),
    ("knowledge", "Findings and decisions", "#7c5ea6", ["finding", "decision", "question"]),
    ("terms", "Terms and documents", "#b0874a", ["term", "document", "policy", "flag", "rule"]),
    ("people", "People, teams and projects", "#9aa1aa", ["person", "team", "project"]),
]
OTHER = ("other", "Everything else", "#b9bec5")


def group_of(kind):
    for g, _, _, kinds in GROUPS:
        if kind in kinds:
            return g
    return "other"


def area_of(path):
    return path.split("/")[0] if "/" in path else ""


def home_of(paths):
    """The island a thing lives on: the project that holds at least 60% of its project notes; a thing no project
    names lives in the shared folder that names it most (glossary, people…); a thing several projects share has
    no island and sits in the middle ("")."""
    projects = collections.Counter(area_of(p) for p in paths if area_of(p) not in GENERAL)
    if projects:
        top, n = projects.most_common(1)[0]
        return top if n / sum(projects.values()) >= 0.6 else ""
    folders = collections.Counter(area_of(p) for p in paths)
    return min(folders, key=lambda a: (-folders[a], a)) if folders else ""


def lines_of(root, path, cache={}):
    if path not in cache:
        try:
            cache[path] = (root / path).read_text().split("\n")
        except OSError:
            cache[path] = []
    return cache[path]


def island(rows):
    """A data island: one record per line, and nothing in it that closes a script."""
    body = "[\n" + ",\n".join("  " + json.dumps(r, ensure_ascii=False, separators=(",", ":")) for r in rows) + "\n]"
    return body.replace("</", "<\\/")


def main(argv):
    if len(argv) < 3:
        raise SystemExit(__doc__)
    root, out = Path(argv[1]).resolve(), Path(argv[2])
    title = argv[argv.index("--title") + 1] if "--title" in argv else None
    g = json.loads((root / "_dream" / "graph.json").read_text())
    notes = {n["path"]: n for n in g["notes"]}
    ents = {e["id"]: e for e in g["entities"]}

    # links: one per (from, to, type), with the line of the note that states it
    seen, links = set(), []
    for r in g["relations"]:
        s, o = r["s"], r["o"]
        if s == o or s not in ents or o not in ents or (s, o, r["type"]) in seen:
            continue
        seen.add((s, o, r["type"]))
        ev = (r.get("evidence") or [""])[0]
        path, _, line = ev.rpartition(":")
        quote = ""
        if path and line.isdigit():
            ls = lines_of(root, path)
            if 0 < int(line) <= len(ls):
                quote = re.sub(r"^\s*(#+|[-*])\s*", "", ls[int(line) - 1]).strip()
                quote = quote if len(quote) <= 220 else quote[:217].rstrip() + "…"
        links.append({"s": s, "t": o, "type": r["type"], "q": quote, "note": path if path in notes else None})
    linked = {l["s"] for l in links} | {l["t"] for l in links}

    # things: the ones with at least one link
    kept = sorted(linked, key=lambda i: (-len({m["path"] for m in ents[i]["mentions"]}), i))
    index = {i: k for k, i in enumerate(kept)}
    used_notes = {m["path"] for i in kept for m in ents[i]["mentions"]} | {l["note"] for l in links if l["note"]}
    note_list = sorted(p for p in used_notes if p in notes)
    note_index = {p: k for k, p in enumerate(note_list)}
    things = []
    for i in kept:
        e = ents[i]
        paths = sorted({m["path"] for m in e["mentions"]})
        home = home_of(paths)
        names = [x["name"].strip("`") for x in sorted(e.get("names") or [], key=lambda x: -x.get("n", 0))]
        label = names[0] if names else i
        things.append({"id": i, "label": label, "type": e["type"], "g": group_of(e["type"].split("/")[0]), "n": len(paths),
                       "home": home, "names": names[:6], "notes": [note_index[p] for p in paths if p in note_index]})
    for l in links:
        l["s"], l["t"] = index[l["s"]], index[l["t"]]
        l["note"] = note_index.get(l["note"]) if l["note"] else None
    note_rows = [{"p": p, "t": notes[p]["title"], "k": notes[p]["kind"], "d": notes[p].get("updated") or "",
                  "a": area_of(p), "old": 1 if notes[p].get("superseded_by") else 0}
                 for p in note_list]
    groups = [{"g": a, "name": b, "color": c, "kinds": d} for a, b, c, d in GROUPS]
    if any(t["g"] == "other" for t in things):
        groups.append({"g": OTHER[0], "name": OTHER[1], "color": OTHER[2], "kinds": []})
    projects = len({t["home"] for t in things if t["home"] not in GENERAL})
    folders = sorted({t["home"] for t in things if t["home"] and t["home"] in GENERAL})
    meta = {"notes": len(g["notes"]), "things": len(things), "links": len(links), "projects": projects, "folders": folders}

    page = (HERE / "page.html").read_text()
    d3 = (HERE / "vendor" / "d3.v7.9.0.min.js").read_text()
    stats = "".join(f"<div><dt>{a}</dt><dd>{b:,}</dd></div>" for a, b in
                    (("things", meta["things"]), ("links", meta["links"]), ("projects", projects), ("notes", meta["notes"])))
    fill = {
        "@@TITLE@@": html.escape(title or "Knowledge graph"),
        "@@EYEBROW@@": "Memory · knowledge graph",
        "@@HEADLINE@@": html.escape(title or f"What {meta['notes']:,} notes know"),
        "@@LEDE@@": ("Every thing the notes name and every link a note states between two of them, each with the line that "
                     "says so. An island is a project; the middle holds what several projects share."),
        "@@STATS@@": stats,
        "@@META@@": json.dumps(meta),
        "@@GROUPS@@": island(groups),
        "@@THINGS@@": island(things),
        "@@LINKS@@": island(links),
        "@@NOTES@@": island(note_rows),
    }
    for k, v in fill.items():
        assert page.count(k) == 1, k
        page = page.replace(k, v)
    page = page.replace("@@D3@@", d3)  # last: the library's text is never searched for markers
    out.write_text(page)
    print(f"{out}: {meta['things']:,} things, {meta['links']:,} links, {projects} projects, {meta['notes']:,} notes · {len(page) / 1e6:.1f} MB")


if __name__ == "__main__":
    main(sys.argv)
