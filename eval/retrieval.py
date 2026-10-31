#!/usr/bin/env python3
"""Offline retrieval eval for `memory.py ask`: no LLM, just "did the answer's evidence come back?".

  retrieval.py <memory root> <questions.jsonl> [more.jsonl ...] [--batch 10] [--budget N] [--show]

Per question: gold-note recall (gold notes headed in its section), number recall (numbers of the
reference answer present in what the agent would see for it), chars. Questions run in batches, one
`ask` call per batch, like an agent would.
"""
import contextlib
import importlib.util
import io
import json
import os
import re
import sys
import time
from pathlib import Path

MEM = Path(os.environ.get("MEM_PY") or Path(__file__).resolve().parent.parent / "skills/memory-dream/scripts/memory.py")
_spec = importlib.util.spec_from_file_location("memory", MEM)
mem = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mem)
NUM = re.compile(r"\d+(?:\.\d+)?")


def run_ask(root, qs, budget=None):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        mem.main(["ask", "--root", str(root), *(["--budget", str(budget)] if budget else []), *qs])
    return buf.getvalue()


def sections(out):
    parts = re.split(r"^## (.*)$", out, flags=re.M)
    return [(parts[i], parts[i + 1]) for i in range(1, len(parts) - 1, 2)]


def score(out, batch):
    printed = {}  # path → all lines printed for it anywhere
    cur = None
    for ln in out.split("\n"):
        m = re.match(r"▸ (\S+)", ln)
        if m:
            cur = m.group(1)
            printed.setdefault(cur, [])
        elif ln.startswith("  ") and cur:
            printed[cur].append(ln)
        elif ln.startswith("## "):
            cur = None
    rows = []
    for (qtext, sec), item in zip(sections(out), batch):
        heads = set(re.findall(r"^▸ (\S+)", sec, re.M))
        seen = sec + "\n" + "\n".join(x for p in heads for x in printed.get(p, []))
        gold = item.get("notes") or []
        nums = set(NUM.findall(item["a"])) - {str(y) for y in range(2020, 2031)}
        have = set(NUM.findall(seen))
        rows.append({"q": item["q"], "type": item.get("type"), "gold": gold,
                     "note_recall": sum(g in heads for g in gold) / len(gold) if gold else None,
                     "num_recall": len(nums & have) / len(nums) if nums else None,
                     "missing_notes": [g for g in gold if g not in heads], "missing_nums": sorted(nums - have),
                     "chars": len(sec)})
    return rows


def main():
    args = sys.argv[1:]
    batch_n = int(args[args.index("--batch") + 1]) if "--batch" in args else 10
    budget = int(args[args.index("--budget") + 1]) if "--budget" in args else None
    show = "--show" in args
    files = [a for a in args[1:] if a.endswith(".jsonl")]
    root = Path(args[0]).resolve()
    items = [json.loads(x) for f in files for x in Path(f).read_text().splitlines() if x.strip()]
    rows, total_chars, secs = [], 0, 0.0
    for i in range(0, len(items), batch_n):
        batch = items[i:i + batch_n]
        t0 = time.perf_counter()
        out = run_ask(root, [b["q"] for b in batch], budget)
        secs += time.perf_counter() - t0
        total_chars += len(out)
        rows += score(out, batch)
        if show:
            print(out)
    nr = [r["note_recall"] for r in rows if r["note_recall"] is not None]
    mr = [r["num_recall"] for r in rows if r["num_recall"] is not None]
    summary = {"questions": len(rows), "note_recall": round(sum(nr) / len(nr), 3) if nr else None,
               "num_recall": round(sum(mr) / len(mr), 3) if mr else None,
               "full_note_hit": sum(r["note_recall"] == 1 for r in rows if r["note_recall"] is not None),
               "chars_per_batch": round(total_chars / max(1, -(-len(items) // batch_n))),
               "chars_per_q": round(total_chars / max(1, len(rows))), "secs_per_batch": round(secs / max(1, -(-len(items) // batch_n)), 2)}
    print(json.dumps(summary))
    for r in rows:
        if (r["note_recall"] or 0) < 1 or (r["num_recall"] if r["num_recall"] is not None else 1) < 1:
            print(f"  miss [{r['type']}] {r['q'][:90]} | notes {r['missing_notes']} | nums {r['missing_nums']}")


if __name__ == "__main__":
    main()
