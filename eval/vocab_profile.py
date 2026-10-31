#!/usr/bin/env python3
"""Profile the entity and relation vocabulary of an indexed memory: what the dreamer produced, and how much is noise.

  vocab_profile.py <memory root>
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

root = Path(sys.argv[1])
g = json.loads((root / "_dream/graph.json").read_text())
stems = {n["path"].rsplit("/", 1)[-1][:-3] for n in g["notes"]}
E, R = g["entities"], g["relations"]
noteid = [e["id"] for e in E if e["id"] in stems or any(a in stems for a in e["aka"])]
files = [e["id"] for e in E if re.search(r"\.(py|sql|ipynb|csv|md)$|^nb[/.-]|notebook|script|\.ipynb", e["id"])]
single = [e for e in E if len(e["mentions"]) == 1]
sep = Counter(re.sub(r"[._\s-]+", "-", e["id"].lower()) for e in E)
out = {
    "notes": len(g["notes"]), "entities": len(E), "entity_types": Counter(e["type"] for e in E).most_common(12),
    "entity_is_a_note_id": len(noteid), "examples_note_id": noteid[:5],
    "files_or_notebooks": len(files), "examples_files": files[:5],
    "mentioned_in_one_note": len(single),
    "collide_if_dot_dash_underscore_alike": sum(v - 1 for v in sep.values() if v > 1),
    "relations": len(R), "relation_types": len({r["type"] for r in R}),
    "entities_with_home_note": sum(1 for e in E if e.get("home")),
    "unknown_type_checks": [c["msg"] for c in g["checks"] if c["code"] == "C7" and "relation type" in c["msg"]][:6],
    "top_relation_types": Counter(r["type"] for r in R).most_common(15),
    "edges_md_types": sum(1 for ln in (root / "EDGES.md").read_text().split("\n") if ln.startswith("- ")),
    "proposed_pending": len(g["proposed"]), "pairs_pending": len(g["review"]),
}
print(json.dumps(out, indent=1))
