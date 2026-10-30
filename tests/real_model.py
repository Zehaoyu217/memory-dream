#!/usr/bin/env python3
"""Real-model acceptance: A3 (Haiku, command mode), A18 (entity convergence), A10 bookkeeping (file mode).

  python3 tests/real_model.py a3 <workdir>        # copy fixture, dream with Haiku twice, report
  python3 tests/real_model.py a10-prep <workdir>  # copy fixture, dream in file mode (writes prompts)
  python3 tests/real_model.py a10-next <workdir>  # dream again after the memory-dreamer subagent ran
  python3 tests/real_model.py report <workdir>    # convergence + checks for an indexed world
"""
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
MEM = HERE.parent / "skills/memory-dream/scripts/memory.py"
_spec = importlib.util.spec_from_file_location("memory", MEM)
mem = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mem)
sys.path.insert(0, str(HERE))
from truth import convergence  # noqa: E402


def run(root, *args, env=None):
    t0 = time.time()
    r = subprocess.run([sys.executable, str(MEM), "--root", str(root), *args], capture_output=True, text=True,
                       env={**os.environ, **(env or {})})
    if r.returncode:
        raise SystemExit(r.stderr)
    return r.stdout.strip(), round(time.time() - t0, 1)


def one_pass(root):
    """The graph from the cached extractions with empty vocabularies: entities before any review."""
    man = json.loads((root / "_dream/manifest.json").read_text())
    cur, former, _, _ = mem.scan(root, man)
    return mem.build(root, {**man, "seen": [], "queue": []}, cur, former, mem.EDGES_SEED, mem.ALIASES_HEAD)


def report(root):
    g = mem.load(root)[0]
    before, after = convergence(one_pass(root)), convergence(g)
    costs = []
    log = root.parent / "cost.jsonl"
    if log.exists():
        costs = [json.loads(x) for x in log.read_text().splitlines()]
    by = Counter()
    for c in costs:
        by[c["kind"] + "_calls"] += 1
        by[c["kind"] + "_usd"] += c["cost"] or 0
    return {"notes": len(g["notes"]), "indexed": sum(n["indexed"] for n in g["notes"]),
            "entities": len(g["entities"]), "relations": len(g["relations"]),
            "proposed": [(p["type"], p["uses"]) for p in g["proposed"]], "checks": dict(Counter(c["code"] for c in g["checks"])),
            "c4": [c["msg"] for c in g["checks"] if c["code"] == "C4"][:12],
            "convergence_one_pass": before, "convergence_after_review": after,
            "cost": {k: round(v, 4) if isinstance(v, float) else v for k, v in by.items()},
            "edges_md": (root / "EDGES.md").read_text(), "aliases_md": (root / "ALIASES.md").read_text()}


def main():
    verb, work = sys.argv[1], Path(sys.argv[2]).resolve()
    root = work / "memory"
    env = {"MEMORY_LLM": f"{sys.executable} {HERE / 'haiku_cmd.py'}", "DREAM_COST_LOG": str(work / "cost.jsonl")}
    out = {}
    if verb in ("a3", "a10-prep"):
        shutil.rmtree(work, ignore_errors=True)
        work.mkdir(parents=True)
        shutil.copytree(HERE / "fixture/memory", root)
    if verb == "a3":
        out["dream1"] = run(root, "dream", "-j", "6", env=env)
        out["dream2"] = run(root, "dream", "-j", "6", env=env)
    elif verb == "a10-prep":
        out["dream1"] = run(root, "dream", env={"MEMORY_LLM": ""})
    elif verb == "a10-next":
        out["dream"] = run(root, "dream", env={"MEMORY_LLM": ""})
        out["pending"] = sorted(p.name for p in (root / "_dream/pending").glob("*.prompt.md"))
    if verb != "a10-prep":
        out["report"] = report(root)
    (work / f"{verb}.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
    print(json.dumps(out, indent=1, ensure_ascii=False)[:6000])


if __name__ == "__main__":
    main()
