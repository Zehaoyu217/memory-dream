#!/usr/bin/env python3
"""Show that adding a relation type by hand later costs 0 model calls: links kept aside in the cache appear.

  add_type_demo.py <indexed memory root>
"""
import importlib.util
import shutil
import sys
import tempfile
from pathlib import Path

spec = importlib.util.spec_from_file_location("m", Path(__file__).resolve().parent.parent / "skills/memory-dream/scripts/memory.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
src = Path(sys.argv[1])
g0 = m.load(src)[0]
d = Path(tempfile.mkdtemp()) / "memory"
shutil.copytree(src, d, ignore=shutil.ignore_patterns("pending"))
edges = (src / "EDGES.md").read_text()
(d / "EDGES.md").write_text(edges.replace(
    "drop:", "- prefers: person X likes style or tool Y | aka: favours, likes\n"
             "- predicts: model X estimates target Y | aka: forecasts\ndrop:", 1))
g1 = m.load(d)[0]


def count(g):
    return {t: sum(1 for r in g["relations"] if r["type"] == t) for t in ("prefers", "predicts")}


print(f"relations before: {len(g0['relations'])} {count(g0)} | after adding 2 types to EDGES.md: "
      f"{len(g1['relations'])} {count(g1)} — 0 model calls")
shutil.rmtree(d.parent)
