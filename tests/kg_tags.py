#!/usr/bin/env python3
"""The knowledge-graph page's tag columns, end to end through the skill's scripts/graph_page.py, no browser needed:
CSV with a ';' list, '/' paths, empty cells and size; JSON with a parents hierarchy, names, colours and --colour;
a graph with no tag column at all. Prints PASS/FAIL per check; exits 1 on any failure.  python3 tests/kg_tags.py"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILD = [sys.executable, str(ROOT / "skills" / "memory-dream" / "scripts" / "graph_page.py")]
ok = True


def check(name, cond, extra=""):
    global ok
    ok = ok and bool(cond)
    print("PASS" if cond else "FAIL", name, "" if cond else extra)


def islands(page):
    s = page.read_text()
    def one(i):
        a = s.index(f'id="{i}">')
        a = s.index("\n", a) + 1
        return json.loads(s[a:s.index("</script>", a)])
    return one("data-columns"), {t["id"]: t for t in one("data-things")}


def run(*args):
    r = subprocess.run(BUILD + [str(a) for a in args], capture_output=True, text=True)
    return r.returncode == 0, (r.stdout + r.stderr)[-400:]


with tempfile.TemporaryDirectory() as d:
    T = Path(d)
    # a table each: id, label, group, size and three tag columns, a ';' list, a '/' path, an empty cell
    (T / "nodes.csv").write_text("id,label,group,size,type,owner,stage\n"
                                 "a,Alpha,g1,3,dataset/table,ana;bo,live\n"
                                 "b,Beta,g1,,dataset/view,bo,\n"
                                 "c,Gamma,g2,,model,cy,draft\n"
                                 "d,Delta,g2,2,model/gbm,ana,live\n")
    (T / "links.csv").write_text("source,target,type,text\na,b,uses,a uses b\nb,c,feeds,\nc,d,replaces,\nd,a,uses,\n")
    built, log = run(T / "nodes.csv", T / "links.csv", T / "csv.html")
    check("CSV builds", built, log)
    cols, by = islands(T / "csv.html")
    check("every other column a tag column: categories (type first), then numbers", [c["key"] for c in cols] == ["type", "owner", "stage", "size"], cols)
    check("a cell with ';' holds several values", by["a"]["tags"].get("owner") == ["ana", "bo"], by["a"])
    check("a '/' path keeps its levels", by["d"]["tags"]["type"] == "model/gbm", by["d"])
    check("an empty cell is no value", "stage" not in by["b"]["tags"], by["b"])
    check("size is a number tag and sizes the dot; label and group are not tags", by["a"]["n"] == 3 and by["a"]["tags"].get("size") == 3
          and next(c for c in cols if c["key"] == "size").get("number") and not {"label", "group"} & set(by["a"]["tags"]), by["a"])
    # JSON: flat values put under parents, the column's name, legend names and hues, the colour column chosen
    doc = {"nodes": [{"id": "t1", "kind": "table", "team": "risk"}, {"id": "t2", "kind": "view", "team": ["risk", "fraud"]},
                     {"id": "m1", "kind": "gbm", "team": "fraud"}, {"id": "x", "kind": "daily/table", "team": "ops", "flag": True}],
           "links": [{"source": "t1", "target": "t2"}, {"source": "t2", "target": "m1"}, {"source": "m1", "target": "x"}],
           "columns": {"kind": {"name": "Kind", "parents": {"table": "dataset", "view": "dataset", "gbm": "model", "dataset": "data"},
                                "names": {"data": "All data"}, "colours": {"data": "#123456"}}}}
    (T / "g.json").write_text(json.dumps(doc))
    built, log = run(T / "g.json", T / "json.html", "--colour", "team")
    check("JSON builds", built, log)
    cols, by = islands(T / "json.html")
    kind = next((c for c in cols if c["key"] == "kind"), {})
    check("--colour puts its column first", cols[0]["key"] == "team", cols)
    check("parents walk a flat value up to its root", by["t1"]["tags"]["kind"] == "data/dataset/table", by["t1"])
    check("a list holds several values", by["t2"]["tags"]["team"] == ["risk", "fraud"], by["t2"])
    check("a value whose head has no parent stays", by["x"]["tags"]["kind"] == "daily/table", by["x"])
    check("the column's name, legend names and hues", kind.get("name") == "Kind" and kind.get("names", {}).get("data") == "All data"
          and kind.get("colours", {}).get("data") == "#123456", kind)
    check("yes/no is text", by["x"]["tags"].get("flag") == "yes", by["x"])
    # text tags: a definition is a tag too, kept whole (no levels, no ';'), never the colours; the rule can be overridden
    defs = [f"A daily table of card spend; region {k}/{k + 1}, about {k * 37} rows" for k in range(16)]
    doc = {"nodes": [{"id": f"n{k}", "type": "dataset" if k % 2 else "model", "definition": defs[k], "sku": f"S-{k}", "code": "ab"[k % 2]}
                     for k in range(16)],
           "links": [{"source": f"n{k}", "target": f"n{k + 1}", "type": "feeds"} for k in range(15)],
           "columns": {"code": {"text": True}, "sku": {"text": False}},
           "link_types": {"feeds": {"name": "Feeds", "inverse": "Fed by"}}}
    (T / "t.json").write_text(json.dumps(doc))
    built, log = run(T / "t.json", T / "t.html", "--colour", "definition")
    check("text JSON builds", built, log)
    cols, by = islands(T / "t.html")
    kinds = {c["key"]: bool(c.get("text")) for c in cols}
    check("a long or mostly-unique column is text", kinds.get("definition") is True, cols)
    check("a text value is kept whole", by["n3"]["tags"]["definition"] == defs[3], by["n3"])
    check("a text column never opens the colours, even asked", cols[0]["key"] == "type", [c["key"] for c in cols])
    check("'text': true and false override the rule", kinds.get("code") is True and kinds.get("sku") is False, kinds)
    s = (T / "t.html").read_text()
    a = s.index('id="data-meta">'); a = s.index("\n", a) + 1
    meta = json.loads(s[a:s.index("</script>", a)])
    check("link_types name a link type both ways", meta.get("forward", {}).get("feeds") == "Feeds" and meta.get("inverse", {}).get("feeds") == "Fed by", meta)
    # four sorts: time (ISO dates: year/month/day, read as dates) and number beside category and text; a link's own
    # direction (-> <- o-o, or its type's), weight and tags; another number column as the size or the weight
    doc = {"nodes": [{"id": f"m{k}", "type": "model", "created": f"2025-{k % 12 + 1:02d}-0{k % 9 + 1}", "rows": k * 100, "auc": 0.5 + k / 100}
                     for k in range(14)],
           "links": [{"source": "m0", "target": "m1", "type": "feeds", "weight": 4, "seen": "2026-01-05", "via": "scan"},
                     {"source": "m2", "target": "m3", "type": "feeds", "direction": "<-", "via": "manual"},
                     {"source": "m4", "target": "m5", "type": "same-as"},
                     {"source": "m5", "target": "m4", "type": "same-as"},
                     {"source": "m6", "target": "m7", "type": "rhymes", "direction": "o-o", "score": 0.9},
                     {"source": "m8", "target": "m9", "type": "twin"}, {"source": "m9", "target": "m10", "type": "uses", "score": 0.2},
                     {"source": "m10", "target": "m11", "type": "uses"}, {"source": "m12", "target": "m13", "type": "uses"}],
           "columns": {"auc": {"use": "size"}}, "link_columns": {"score": {"use": "weight"}},
           "link_types": {"twin": {"direction": "o-o", "name": "Twin of"}}}
    (T / "s.json").write_text(json.dumps(doc))
    built, log = run(T / "s.json", T / "s.html")
    check("sorts JSON builds", built, log)
    cols, by = islands(T / "s.html")
    sort = {c["key"]: next((k for k in ("time", "number", "text") if c.get(k)), "category") for c in cols}
    check("ISO dates are a time tag, a path year/month/day", sort.get("created") == "time" and by["m3"]["tags"]["created"] == "2025/04/04", (sort, by["m3"]))
    created = next(c for c in cols if c["key"] == "created")
    check("a time reads as a date", created.get("names", {}).get("2025/04/04") == "4 Apr 2025" and created["names"].get("2025/04") == "Apr 2025", created.get("names"))
    check("numbers are a number tag", sort.get("rows") == "number" and by["m3"]["tags"]["rows"] == 300, (sort, by["m3"]))
    check("'use': 'size' sizes the dot by another number", by["m3"]["n"] == 0.53, by["m3"])
    s = (T / "s.html").read_text()
    a = s.index('id="data-meta">'); a = s.index("\n", a) + 1
    meta = json.loads(s[a:s.index("</script>", a)])
    a = s.index('id="data-links">'); a = s.index("\n", a) + 1
    raw = json.loads(s[a:s.index("</script>", a)])
    ids = [t["id"] for t in json.loads(s[s.index("\n", s.index('id="data-things">')) + 1:s.index("</script>", s.index('id="data-things">'))])]
    ln = {(ids[l["s"]], ids[l["t"]], l["type"]): l for l in raw}
    check("<- turns a link round", ("m3", "m2", "feeds") in ln and ("m2", "m3", "feeds") not in ln, list(ln))
    check("o-o: no direction, one link however it is written", [k for k in ln if k[2] == "same-as"] in ([("m4", "m5", "same-as")], [("m5", "m4", "same-as")])
          and all(l.get("dir") == 0 for k, l in ln.items() if k[2] in ("same-as", "rhymes", "twin")), list(ln))
    check("a link type's own direction (link_types)", ln.get(("m8", "m9", "twin"), {}).get("dir") == 0 and meta["forward"].get("twin") == "Twin of", meta.get("forward"))
    check("a link's tags: category, time, number", ln[("m0", "m1", "feeds")].get("tags") == {"weight": 4, "seen": "2026/01/05", "via": "scan"}, ln[("m0", "m1", "feeds")])
    lsort = {c["key"]: next((k for k in ("time", "number", "text") if c.get(k)), "category") for c in meta["link_columns"]}
    check("link columns told by their values", lsort == {"weight": "number", "seen": "time", "via": "category", "score": "number"}, lsort)
    check("'use': 'weight' weighs links by another number", ln[("m6", "m7", "rhymes")].get("w") == 0.9 and "w" not in ln[("m0", "m1", "feeds")], (ln[("m6", "m7", "rhymes")], ln[("m0", "m1", "feeds")]))
    check("search's link values, every level", meta["link_values"].get("via") == {"scan": 1, "manual": 1} and meta["link_values"]["seen"].get("2026") == 1, meta["link_values"])
    check("links with no direction counted", meta.get("both") == 3, meta.get("both"))
    # a link's tags and direction from a CSV table too
    (T / "l.csv").write_text("source,target,type,direction,weight,since\na,b,uses,->,2,2024-03\nc,b,uses,<-,,\nc,d,same-as,,,\n")
    built, log = run(T / "nodes.csv", T / "l.csv", T / "lc.html")
    check("CSV links build", built, log)
    s = (T / "lc.html").read_text()
    a = s.index('id="data-links">'); a = s.index("\n", a) + 1
    raw = json.loads(s[a:s.index("</script>", a)])
    check("CSV: a link's weight, time and direction", any(l.get("w") == 2 and (l.get("tags") or {}).get("since") == "2024/03" for l in raw)
          and sum(1 for l in raw if l.get("dir") == 0) == 1, raw)
    # nothing declared, nothing tidy: nested objects spread out, n/a and blanks as no value, required parts by other names
    doc = {"nodes": [{"data": {"id": "a", "name": "Alpha", "score": 0.4, "properties": {"tier": 1, "region": "eu"}}},
                     {"data": {"id": "b", "name": "Beta", "score": "n/a", "properties": {"tier": 2, "region": "us"}}},
                     {"key": "c", "title": "Gamma", "score": 0.9, "properties": {"region": "eu"}, "when": ""}],
           "links": [{"data": {"source": "a", "target": "b", "properties": {"since": "2024-05", "confidence": "unknown"}}},
                     {"from": "b", "to": "c", "properties": {"since": "2025-01", "confidence": 0.7}},
                     {"start": {"id": "c", "labels": ["X"]}, "end": {"id": "a"}, "type": "uses"}]}
    (T / "messy.json").write_text(json.dumps(doc))
    built, log = run(T / "messy.json", T / "messy.html")
    check("messy, undeclared data builds", built, log)
    cols, by = islands(T / "messy.html")
    sort = {c["key"]: (c["name"], next((k for k in ("time", "number", "text") if c.get(k)), "category")) for c in cols}
    check("required parts by other names: data wrapper, key, name, title", set(by) == {"a", "b", "c"} and by["a"]["label"] == "Alpha" and by["c"]["label"] == "Gamma", by)
    check("nested objects spread out, named by their last part", sort.get("properties.region") == ("Region", "category") and sort.get("properties.tier") == ("Tier", "number"), sort)
    check("n/a is no value: the column stays a number", sort.get("score") == ("Score", "number") and "score" not in by["b"]["tags"], (sort, by["b"]))
    s = (T / "messy.html").read_text()
    a = s.index('id="data-meta">'); a = s.index("\n", a) + 1
    meta = json.loads(s[a:s.index("</script>", a)])
    lsort = {c["key"]: next((k for k in ("time", "number", "text") if c.get(k)), "category") for c in meta["link_columns"]}
    a = s.index('id="data-links">'); a = s.index("\n", a) + 1
    raw = json.loads(s[a:s.index("</script>", a)])
    check("a link's ends by other names: from/to, start/end, a data wrapper", len(raw) == 3, raw)
    check("a link's nested tags: unknown is no value", lsort == {"properties.since": "time", "properties.confidence": "number"}, lsort)
    check("the rest of a nested end is not a tag", not any("start" in k or "end" in k for l in raw for k in (l.get("tags") or {})), raw)
    # no tag column at all: one, so the legend still counts the things
    (T / "bare.json").write_text(json.dumps({"nodes": [{"id": "p"}, {"id": "q"}], "links": [{"source": "p", "target": "q"}]}))
    built, log = run(T / "bare.json", T / "bare.html")
    cols, by = islands(T / "bare.html")
    check("no tag column: every thing a 'thing'", built and [c["key"] for c in cols] == ["type"] and by["p"]["tags"] == {"type": "thing"}, (cols, by))
print("kg_tags: all pass" if ok else "kg_tags: FAILED")
sys.exit(0 if ok else 1)
