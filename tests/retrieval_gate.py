#!/usr/bin/env python3
"""CI gate for the model-free retrieval numbers (README "Results"): build a world, dream with no model, run
eval/retrieval.py and eval/adversarial.py, and fail when a number drops under its floor.

  retrieval_gate.py bank      [--work DIR]   the 1,677-note bank (eval/bank/generated + tests/fixture/memory), 326 questions
  retrieval_gate.py software  [--work DIR]   tests/fixture-software/memory, eval/questions/software-*.jsonl
  retrieval_gate.py bank-index [--work DIR]  the bank with the real Haiku index restored from eval/real/bank-index (0 calls)
  retrieval_gate.py worn      [--work DIR]   the worn bank (eval/hard/make_hard.py: no lineage frontmatter, every link said in
                                             prose) with what Haiku read in it restored from eval/real/worn-index (0 calls):
                                             how much of the lineage the memory holds, against the answer key
  retrieval_gate.py flat      [--work DIR]   the flat bank (eval/hard/make_flat.py: the worn bank's forty project folders
                                             poured into one, 1,224 notes, too many to list or to read whole) with what
                                             Haiku read in it restored from eval/real/flat-index (0 calls)

Floors (set from the measured numbers minus a small margin; raise them when the numbers rise):
  bank:     gold ≥ 0.96 (0.93 until phase L, 2026-11-11: measured 0.939 before it and 0.978 after) · numbers ≥ 0.97 ·
            chars per question ≤ 3,000 · stale: successor above the old note ≥ 0.95, old marked 1.0 · absence flagged 1.0
  bank-index: the same, chars ≤ 3,200, and alias ≥ 0.80
  software: gold ≥ 0.90 · numbers ≥ 0.95 · stale: successor above ≥ 0.95 (when the set is non-empty), old marked 1.0
  worn:     `from` links held as lineage ≥ 0.98 (measured 0.995) · `supersedes` ≥ 0.98 (0.995) · lineage edges that are true
            ≥ 0.98 (0.990) · of the 98 linkage questions, the lineage alone gives the exact answer for ≥ 91 (93) and
            `ask` alone names every note of the answer for ≥ 82 (84)
  flat:     `from` links held as lineage ≥ 0.98 (measured 0.992) · `supersedes` ≥ 0.98 (0.995) · lineage edges that are true ≥ 0.97
            (0.985) · of the 72 questions of the flat bank, the lineage alone gives the exact answer for ≥ 64 (66)
"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MEM = ROOT / "skills/memory-dream/scripts/memory.py"
FLOORS = {"bank": {"gold": 0.96, "numbers": 0.97, "chars": 3000, "stale_above": 0.95, "stale_marked": 1.0, "absence": 1.0, "alias": None},
          "bank-index": {"gold": 0.96, "numbers": 0.97, "chars": 3200, "stale_above": 0.95, "stale_marked": 1.0, "absence": 1.0, "alias": 0.80},
          "software": {"gold": 0.90, "numbers": 0.95, "chars": 6000, "stale_above": 0.95, "stale_marked": 1.0, "absence": None, "alias": None}}


def run(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if r.returncode != 0:
        sys.stderr.write(r.stdout[-2000:] + r.stderr[-2000:])
        raise SystemExit(f"failed: {' '.join(map(str, cmd))}")
    return r.stdout


def first_json(text):
    """The first JSON object in a script's output (retrieval.py prints one line; adversarial.py one document)."""
    i = text.find("{")
    dec = json.JSONDecoder()
    while i >= 0:
        try:
            return dec.raw_decode(text[i:])[0]
        except ValueError:
            i = text.find("{", i + 1)
    raise SystemExit("no JSON in output:\n" + text[:1000])


def worn_bank(work):
    """The worn bank, made from the repository with no model: -> its folder (memory/ and truth.json)."""
    tidy, out = work / "tidy" / "memory", work / "worn"
    for d in (work / "tidy", out, work / "flat"):
        if d.exists():
            shutil.rmtree(d)
    run([sys.executable, ROOT / "eval/bank/assemble.py", ROOT / "eval/bank/generated", ROOT / "tests/fixture/memory", tidy])
    run([sys.executable, ROOT / "eval/real/bank-index/restore.py", tidy])
    run([sys.executable, MEM, "--root", tidy, "dream"])
    run([sys.executable, ROOT / "eval/hard/make_hard.py", tidy, out])
    return out


def flat(work):
    """The flat bank and its readings, all from the repository: one folder too large to list, lineage as read."""
    out = work / "flat"
    worn_dir = worn_bank(work)
    run([sys.executable, ROOT / "eval/hard/make_flat.py", worn_dir, ROOT / "eval/questions/linkage-100.jsonl", out])
    if (out / "questions.jsonl").read_text() != (ROOT / "eval/questions/linkage-flat.jsonl").read_text():
        raise SystemExit("flat: eval/questions/linkage-flat.jsonl is not what make_flat.py writes; copy <flat>/questions.jsonl over it")
    run([sys.executable, ROOT / "eval/real/flat-index/restore.py", out / "memory"])
    dreamed = run([sys.executable, MEM, "--root", out / "memory", "dream"])
    if "0 indexed (0 calls)" not in dreamed or "without entities" in dreamed:
        raise SystemExit("flat: the restored readings were not used (did make_flat.py write other notes?): " + dreamed)
    got = json.loads(run([sys.executable, ROOT / "eval/hard/lineage_score.py", out / "memory", out / "truth.json"]).strip().splitlines()[-1])
    got["answered"] = json.loads(run([sys.executable, ROOT / "eval/linkage.py", "lineage", out / "memory",
                                      out / "questions.jsonl"]).strip().splitlines()[-1])["answered"]
    floors = {"from": 0.98, "supersedes": 0.98, "true": 0.97, "answered": 64}
    bad = [f"{k}: {got[k]} (floor {v})" for k, v in floors.items() if got[k] < v]
    print(json.dumps({"world": "flat", **got}))
    if bad:
        raise SystemExit("retrieval gate failed: " + "; ".join(bad))
    print("retrieval gate ok")


def worn(work):
    """The worn bank and its readings, all from the repository: lineage as the keepers read it, scored exactly."""
    out = worn_bank(work)
    run([sys.executable, ROOT / "eval/real/worn-index/restore.py", out / "memory"])
    dreamed = run([sys.executable, MEM, "--root", out / "memory", "dream"])
    if "0 indexed (0 calls)" not in dreamed or "without entities" in dreamed:
        raise SystemExit("worn: the restored readings were not used (did make_hard.py write other notes?): " + dreamed)
    got = json.loads(run([sys.executable, ROOT / "eval/hard/lineage_score.py", out / "memory", out / "truth.json"]).strip().splitlines()[-1])
    asked = run([sys.executable, ROOT / "eval/linkage.py", "ask", out / "memory", ROOT / "eval/questions/linkage-100.jsonl"])
    got["ask_named"] = int(re.search(r"headed or named for (\d+)", asked).group(1))
    got["answered"] = json.loads(run([sys.executable, ROOT / "eval/linkage.py", "lineage", out / "memory",
                                      ROOT / "eval/questions/linkage-100.jsonl"]).strip().splitlines()[-1])["answered"]
    floors = {"from": 0.98, "supersedes": 0.98, "true": 0.98, "answered": 91, "ask_named": 82}
    bad = [f"{k}: {got[k]} (floor {v})" for k, v in floors.items() if got[k] < v]
    print(json.dumps({"world": "worn", **got}))
    if bad:
        raise SystemExit("retrieval gate failed: " + "; ".join(bad))
    print("retrieval gate ok")


def main(argv):
    world = argv[1] if len(argv) > 1 else "bank"
    work = Path(argv[argv.index("--work") + 1]) if "--work" in argv else Path(tempfile.mkdtemp(prefix="gate-"))
    if world == "worn":
        return worn(work)
    if world == "flat":
        return flat(work)
    mem = work / "memory"
    if mem.exists():
        shutil.rmtree(mem)
    if world in ("bank", "bank-index"):
        run([sys.executable, ROOT / "eval/bank/assemble.py", ROOT / "eval/bank/generated", ROOT / "tests/fixture/memory", mem])
        if world == "bank-index":  # the real Haiku readings and reviewed registries, no model call (eval/real/bank-index)
            run([sys.executable, ROOT / "eval/real/bank-index/restore.py", mem])
        qs = sorted((ROOT / "eval/questions").glob("bank-*.jsonl"))
    else:
        shutil.copytree(ROOT / "tests/fixture-software/memory", mem)
        qs = sorted((ROOT / "eval/questions").glob("software-*.jsonl"))
    out = run([sys.executable, MEM, "--root", mem, "dream"])
    # note-shape warnings fail both worlds; broken lineage fails the hand-written software fixture only (the Haiku-written
    # bank carries one C2 by construction, and the gate measures retrieval, not the bank's prose)
    if world == "bank-index" and "0 indexed (0 calls)" not in out:
        raise SystemExit("bank-index: the restored readings were not used: " + out)
    if re.search(r"\bC(6|11)×", out) or (world not in ("bank", "bank-index") and re.search(r"\bC(1|2)×", out)):
        raise SystemExit("dream reports lineage or note-shape warnings: " + out)
    r = first_json(run([sys.executable, ROOT / "eval/retrieval.py", mem, *qs]))
    a = first_json(run([sys.executable, ROOT / "eval/adversarial.py", mem, *qs, *(["--index-world", str(mem)] if world == "bank-index" else [])]))
    f = FLOORS[world]
    got = {"gold": r["note_recall"], "numbers": r["num_recall"], "chars": r["chars_per_q"],
           "stale_above": a["stale"].get("successor_above_old"), "stale_marked": a["stale"].get("old_marked_superseded_when_shown"),
           "absence": (a.get("absence") or {}).get("ask flagged"), "alias": (a.get("alias") or {}).get("ask (index)")}
    bad = []
    for k, floor in f.items():
        v = got.get(k)
        if floor is None or v is None:
            continue
        ok = v <= floor if k == "chars" else v >= floor
        if not ok:
            bad.append(f"{k}: {v} (floor {floor})")
    print(json.dumps({"world": world, "questions": r["questions"], "stale_n": a["stale"].get("n"), **got}))
    if bad:
        raise SystemExit("retrieval gate failed: " + "; ".join(bad))
    print("retrieval gate ok")


if __name__ == "__main__":
    main(sys.argv)
