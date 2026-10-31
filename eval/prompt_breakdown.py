#!/usr/bin/env python3
"""What one extraction prompt is made of, for memories of different sizes: template, EDGES, KNOWN, the note.

  prompt_breakdown.py <memory root> [<memory root> ...]
Tokens are estimated as chars / 4. The CLI adds its own system prompt on top (measured input minus this).
"""
import importlib.util
import statistics as st
import sys
from pathlib import Path

spec = importlib.util.spec_from_file_location("m", Path(__file__).resolve().parent.parent / "skills/memory-dream/scripts/memory.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
for r in sys.argv[1:]:
    root = Path(r)
    g = m.load(root)[0]
    ents = {e["id"]: e for e in g["entities"]}
    edges = "\n".join(m.parse_edges(m.vocab_texts(root)[0])[3])
    tpl = len(m.fill(m.EXTRACT, edges="", known="", path="", text=""))
    kn = m.Known(ents)
    known = [len(m.known_lines(kn, n["project"])) for n in g["notes"] if n["project"] != "log"]
    note = [len(m.read(root / n["path"])) for n in g["notes"]]
    tot = tpl + len(edges) + st.median(known) + st.median(note)
    print(f"{root.parent.name}: {len(g['notes'])} notes, {len(ents)} entities | per prompt ≈ {tot / 4:.0f} tokens: "
          f"template {tpl / 4:.0f} · EDGES {len(edges) / 4:.0f} · KNOWN {st.median(known) / 4:.0f} (max {max(known) / 4:.0f}) · "
          f"note {st.median(note) / 4:.0f}")
