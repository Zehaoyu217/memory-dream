#!/usr/bin/env python3
"""Does `ask` give the same answer every time? (RESULTS phase J) No model.

  stability.py <memory root> [--seeds 0,1,2] [--every 4] [--show N]

Three question sets go through `ask`, ten per call, like an agent:
  alias  "what do we know about <surface form>?" as eval/adversarial.py builds them (only when the memory has an index)
  bank   eval/questions/bank-*.jsonl
  tasks  eval/taste/tasks.jsonl and tasks-holdout.jsonl (the preferences block)
once per variant, and each variant is compared with the first run, question by question:
  seed N      another PYTHONHASHSEED, a fresh process
  files a-z   grep's files listed in ascending path order, as another filesystem might list them
  files z-a   descending
  no grep     the Python matcher that stands in on a machine with no grep
  alone       every --every-th question asked alone, and in sevens, against the same questions in tens (notes only:
              the "(above)" marks of a shared call differ by design)
Counted per set: questions whose printed section differs (text), whose notes come in another order (order), whose
set of notes differs (notes), and that flip on "every gold note headed" (flips). All zeros is the pass; exit 1 otherwise.

MEM_PY=<another memory.py> measures that script instead (say `git show <commit>:skills/memory-dream/scripts/memory.py`
saved to a file). A script other than the one that dreamed the memory re-merges the graph on every call: slower, same
answers. MEMORY_WIDE=100 measures the routed read path of big memories on a small one.
"""
import contextlib
import importlib.util
import io
import json
import os
import re
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
MEM = Path(os.environ.get("MEM_PY") or HERE.parent / "skills/memory-dream/scripts/memory.py")
SETS = ("alias", "bank", "tasks")


def questions(mem, root):
    """[(set, question, gold notes)] — the alias set as adversarial.py builds it, then the bank, then the tasks."""
    items = []
    for e in mem.load(root)[0]["entities"]:
        gold = e["home"] or e["headline"]
        for nm in e["names"][:6] if gold else []:
            s = nm["name"]
            if mem.fold(s) != mem.fold(e["id"]) and 3 <= len(s) <= 40 and not re.search(r"[`\"]", s) and mem.fold(s) not in mem.fold(gold):
                items.append(("alias", f"what do we know about {s}?", [gold]))
                break
    files = sorted((HERE / "questions").glob("bank-*.jsonl")) + [HERE / "taste/tasks.jsonl", HERE / "taste/tasks-holdout.jsonl"]
    for f in files:
        for ln in f.read_text().splitlines():
            if ln.strip():
                d = json.loads(ln)
                items.append(("tasks" if f.parent.name == "taste" else "bank", d["q"], d["notes"]))
    return items


def worker(root, order, batch, every, out):
    """One run in this process: every question's section and the notes it heads, written to `out` as JSON."""
    spec = importlib.util.spec_from_file_location("memory", MEM)
    mem = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mem)
    if order != "found":
        grep = mem.grep_lines

        def listed(r, pats, areas=None):
            h = grep(r, pats, areas)
            return {k: h[k] for k in sorted(h, reverse=order == "z-a")}
        mem.grep_lines = listed
    items, rows = questions(mem, root)[::every], []
    for i in range(0, len(items), batch):
        part, buf = items[i:i + batch], io.StringIO()
        with contextlib.redirect_stdout(buf):
            mem.main(["ask", "--root", str(root), *[q for _, q, _ in part]])
        cut = re.split(r"^## (.*)$", buf.getvalue(), flags=re.M)
        secs = [cut[j + 1] for j in range(1, len(cut) - 1, 2)]
        assert len(secs) >= len(part), f"{len(secs)} sections for {len(part)} questions"
        rows += [{"set": s, "q": q, "gold": gold, "sec": sec, "heads": re.findall(r"^▸ (\S+)", sec, re.M)}
                 for (s, q, gold), sec in zip(part, secs)]
    Path(out).write_text(json.dumps(rows))


def compare(base, other, text=True):
    d = {s: Counter() for s in SETS}
    for x, y in zip(base, other):
        c = d[x["set"]]
        c["text"] += text and x["sec"] != y["sec"]
        c["order"] += x["heads"] != y["heads"]
        c["notes"] += set(x["heads"]) != set(y["heads"])
        c["flips"] += (set(x["gold"]) <= set(x["heads"])) != (set(y["gold"]) <= set(y["heads"]))
    return d


def main(argv):
    if "--worker" in argv:
        root, order, batch, every, out = argv[argv.index("--worker") + 1:][:5]
        return worker(Path(root), order, int(batch), int(every), out)
    root = Path(argv[0]).resolve()
    opt = lambda k, default: argv[argv.index(k) + 1] if k in argv else default  # noqa: E731
    seeds, every, show = opt("--seeds", "0,1,2").split(","), int(opt("--every", "4")), int(opt("--show", "0"))
    tmp = Path(tempfile.mkdtemp(prefix="stability-"))
    runs = [(f"seed {s}", s, "found", 10, 1, {}) for s in seeds] + \
           [("files a-z", seeds[0], "a-z", 10, 1, {}), ("files z-a", seeds[0], "z-a", 10, 1, {}),
            ("no grep", seeds[0], "found", 10, 1, {"PATH": str(tmp / "no-bin")}),  # nothing on the path: grep is not found
            ("in tens", seeds[0], "found", 10, every, {}), ("alone", seeds[0], "found", 1, every, {}),
            ("in sevens", seeds[0], "found", 7, every, {})]
    procs = []
    for name, seed, order, batch, ev, env in runs:  # every run is its own process: its own hash seed
        out = tmp / (name.replace(" ", "-") + ".json")
        procs.append((name, out, subprocess.Popen([sys.executable, __file__, "--worker", str(root), order, str(batch), str(ev), str(out)],
                                                  env=dict(os.environ, PYTHONHASHSEED=seed, **env))))
    got = {}
    for name, out, p in procs:
        if p.wait() != 0:
            raise SystemExit(f"run '{name}' failed")
        got[name] = json.loads(out.read_text())
    first = got[runs[0][0]]
    n = Counter(x["set"] for x in first)
    score = {s: {"n": n[s], "gold": round(sum(len(set(x["gold"]) & set(x["heads"])) / len(x["gold"]) for x in first if x["set"] == s) / n[s], 4),
                 "complete": sum(set(x["gold"]) <= set(x["heads"]) for x in first if x["set"] == s)} for s in SETS if n[s]}
    sets = [s for s in SETS if n[s]]
    print(f"{MEM}\n{root}: " + " · ".join(f"{s} {score[s]['n']} questions, gold {score[s]['gold']}, complete {score[s]['complete']}" for s in sets))
    print(f"\n{'against the first run':24}" + "".join(f"{s + ' text/order/notes/flips':>34}" for s in sets))
    table, bad = {}, 0
    for name, *_ in runs[1:]:
        if name == "in tens":
            continue
        shared = name in ("alone", "in sevens")
        d = compare(got["in tens"] if shared else first, got[name], text=not shared)
        table[name] = {s: dict(d[s]) for s in sets}
        bad += sum(sum(d[s].values()) for s in sets)
        cell = lambda c: f"{'-' if shared else c['text']}/{c['order']}/{c['notes']}/{c['flips']}"  # noqa: E731
        print(f"{name + (f' (every {every}th)' if shared else ''):24}" + "".join(f"{cell(d[s]):>34}" for s in sets))
        k = 0
        for x, y in zip(got["in tens"] if shared else first, got[name]):
            if k < show and set(x["heads"]) != set(y["heads"]):
                k += 1
                print(f"    {x['q'][:96]}\n      only before: {sorted(set(x['heads']) - set(y['heads']))}\n      only here:   {sorted(set(y['heads']) - set(x['heads']))}")
    print("\n" + json.dumps({"questions": dict(n), "score": score, "differences": table, "stable": not bad}))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
