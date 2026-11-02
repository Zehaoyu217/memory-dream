#!/usr/bin/env python3
"""A/B the retrieval numbers under environment settings (phase I: typed-link one-liners), one table for all variants.

  ab_env.py <memory root> <questions.jsonl…> --var "name:ENV=v,ENV2=v2" [--var …] [--index-world <root>] [--types dependency,why]

Each variant runs eval/retrieval.py --by-type (gold, numbers, precision, complete answers, chars per question, and the
named types' gold recall) and eval/adversarial.py (stale successor-above, scatter all-gold, alias gold when --index-world
is given). Variants run in the same process environment plus the variant's settings. Output: a markdown table.
"""
import json
import os
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def first_json(text):
    dec = json.JSONDecoder()
    i = text.find("{")
    while i >= 0:
        try:
            return dec.raw_decode(text[i:])[0]
        except ValueError:
            i = text.find("{", i + 1)
    raise SystemExit("no JSON in:\n" + text[:800])


def main(argv):
    root = Path(argv[1]).resolve()
    qs = [a for a in argv[2:] if a.endswith(".jsonl")]
    variants, i = [], 0
    while "--var" in argv[i:]:
        j = argv.index("--var", i)
        name, _, env = argv[j + 1].partition(":")
        variants.append((name, dict(kv.split("=", 1) for kv in env.split(",") if kv)))
        i = j + 2
    index_world = argv[argv.index("--index-world") + 1] if "--index-world" in argv else None
    types = argv[argv.index("--types") + 1].split(",") if "--types" in argv else ["dependency", "why", "lineage", "current"]
    rows = []
    for name, env in variants:
        e = {**os.environ, **env}
        r = first_json(subprocess.run([sys.executable, HERE / "retrieval.py", root, *qs, "--by-type"], capture_output=True, text=True, env=e).stdout)
        adv = subprocess.run([sys.executable, HERE / "adversarial.py", root, *qs, *(["--index-world", index_world] if index_world else [])],
                             capture_output=True, text=True, env=e).stdout
        a = first_json(adv) if "{" in adv else {}
        bt = r.get("by_type", {})
        rows.append({"variant": name, "gold": r["note_recall"], "numbers": r["num_recall"], "precision": r["precision"], "complete": r["full_note_hit"],
                     "chars/q": r["chars_per_q"], **{f"{t} gold": (bt.get(t) or {}).get("gold") for t in types},
                     **{f"{t} complete": (bt.get(t) or {}).get("full") for t in types},
                     "stale above": (a.get("stale") or {}).get("successor_above_old"), "scatter all-gold": ((a.get("scatter") or {}).get("ask") or {}).get("all_gold"),
                     "alias gold": (a.get("alias") or {}).get("ask (index)"), "alias chars/q": ((a.get("alias") or {}).get("chars_per_q") or {}).get("ask (index)")})
    cols = list(rows[0].keys())
    print("| " + " | ".join(cols) + " |")
    print("|" + "---|" * len(cols))
    for r in rows:
        print("| " + " | ".join("" if r[c] is None else str(r[c]) for c in cols) + " |")
    print(json.dumps(rows))


if __name__ == "__main__":
    main(sys.argv)
