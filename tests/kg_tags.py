#!/usr/bin/env python3
"""The knowledge-graph page's tag columns, end to end through demo/knowledge-graph/build.py, no browser needed:
CSV with a ';' list, '/' paths, empty cells and size; JSON with a parents hierarchy, names, colours and --colour;
a graph with no tag column at all. Prints PASS/FAIL per check; exits 1 on any failure.  python3 tests/kg_tags.py"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILD = [sys.executable, str(ROOT / "demo" / "knowledge-graph" / "build.py")]
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
    check("every other column a tag column, type first", [c["key"] for c in cols] == ["type", "owner", "stage"], cols)
    check("a cell with ';' holds several values", by["a"]["tags"].get("owner") == ["ana", "bo"], by["a"])
    check("a '/' path keeps its levels", by["d"]["tags"]["type"] == "model/gbm", by["d"])
    check("an empty cell is no value", "stage" not in by["b"]["tags"], by["b"])
    check("size sizes the dot; label and group are not tags", by["a"]["n"] == 3.0 and not {"label", "group", "size"} & set(by["a"]["tags"]), by["a"])
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
    # no tag column at all: one, so the legend still counts the things
    (T / "bare.json").write_text(json.dumps({"nodes": [{"id": "p"}, {"id": "q"}], "links": [{"source": "p", "target": "q"}]}))
    built, log = run(T / "bare.json", T / "bare.html")
    cols, by = islands(T / "bare.html")
    check("no tag column: every thing a 'thing'", built and [c["key"] for c in cols] == ["type"] and by["p"]["tags"] == {"type": "thing"}, (cols, by))
print("kg_tags: all pass" if ok else "kg_tags: FAILED")
sys.exit(0 if ok else 1)
