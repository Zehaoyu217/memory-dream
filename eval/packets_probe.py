#!/usr/bin/env python3
"""Does a keeper read a note as well inside a packet as alone, and what does each cost? One real run, Haiku.

  python3 eval/packets_probe.py prepare <dreamed bank-index world> <work dir> [--areas 10]
        two copies of the world, <work>/single and <work>/packets, with the readings of the same N project
        folders set aside in _dream/held/ (moved, not deleted): those notes are the ones a dream will read
  MEMORY_LLM="python3 tests/haiku_cmd.py" DREAM_COST_LOG=<work>/single.jsonl  python3 …/memory.py --root <work>/single/memory  dream -j 8
  MEMORY_LLM="python3 tests/haiku_cmd.py" DREAM_COST_LOG=<work>/packets.jsonl python3 …/memory.py --root <work>/packets/memory dream --packets -j 6
  python3 eval/packets_probe.py compare <work dir>
        per arm: notes read, calls, tokens, dollars, seconds of model time; things and links kept a note, what the
        check against the note refused; agreement with the readings on file; and by position in the packet

The readings on file (eval/real/bank-index, read one call a note on 2026-11-02) are the reference both arms are
compared with; the two arms are also compared with each other, since they are the same model on the same day.
Quoted in RESULTS.md phase S.
"""
import json
import shutil
import sys
from pathlib import Path


def fold(s):
    import re
    return re.sub(r"[\s_.-]+", "-", str(s).strip().lower())


def prepare(world, work, n_areas):
    world, work = Path(world), Path(work)
    man = json.loads((world / "_dream" / "manifest.json").read_text())
    general = {"prefs", "reporting", "glossary", "corrections", "howto", "qa", "people", "log", ""}
    areas = sorted({p.split("/")[0] for p in man["files"] if "/" in p} - general)
    step = max(1, len(areas) // n_areas)
    picked = areas[::step][:n_areas]  # spread over the alphabet, the same every time
    hold = sorted(f["sha"][:12] for p, f in man["files"].items() if p.split("/")[0] in picked)
    for arm in ("single", "packets"):
        dst = work / arm / "memory"
        if dst.exists():
            raise SystemExit(f"{dst} exists: give a fresh work dir")
        shutil.copytree(world, dst)
        held = dst / "_dream" / "held"
        held.mkdir()
        for h in hold:
            f = dst / "_dream" / "notes" / f"{h}.json"
            if f.exists():
                f.rename(held / f.name)
    (work / "sample.json").write_text(json.dumps({"areas": picked, "notes": len(hold)}))
    print(f"{len(hold)} notes of {len(picked)} folders set aside in each of {work}/single and {work}/packets: {', '.join(picked)}")


def reading(f):
    try:
        x = json.loads(f.read_text())
    except (OSError, ValueError):
        return None
    ents = {fold(e["id"]) for e in x.get("entities", [])}
    rels = {(fold(r["s"]), fold(r.get("type", "")), fold(r["o"])) for r in x.get("relations", [])}
    pairs = {(fold(r["s"]), fold(r["o"])) for r in x.get("relations", [])}
    d = x.get("dropped") or {}
    return {"ents": ents, "rels": rels, "pairs": pairs, "refused": len(d.get("entities", [])) + int(d.get("relations", 0) or 0)}


def jac(a, b):
    return len(a & b) / len(a | b) if a | b else 1.0


def compare(work):
    work = Path(work)
    arms = {}
    for arm in ("single", "packets"):
        dd = work / arm / "memory" / "_dream"
        held = {f.name[:-5]: reading(f) for f in sorted((dd / "held").glob("*.json"))}
        new = {h: reading(dd / "notes" / f"{h}.json") for h in held}
        log = [json.loads(x) for x in (work / f"{arm}.jsonl").read_text().splitlines()] if (work / f"{arm}.jsonl").exists() else []
        log = [c for c in log if c.get("kind") == "extract"]
        arms[arm] = {"held": held, "new": new, "log": log}
    mean = lambda xs: sum(xs) / len(xs) if xs else 0.0  # noqa: E731
    print("arm · notes read of asked · calls · tokens in (cached) · tokens out · $ · $ a note · model seconds · seconds a note")
    for arm, a in arms.items():
        got = [h for h, r in a["new"].items() if r]
        cost, tin = sum(c.get("cost") or 0 for c in a["log"]), sum(c.get("in") or 0 for c in a["log"])
        cached, out, ms = sum(c.get("cached") or 0 for c in a["log"]), sum(c.get("out") or 0 for c in a["log"]), sum(c.get("ms") or 0 for c in a["log"])
        n = max(1, len(got))
        print(f"{arm:<8} · {len(got)} of {len(a['held'])} · {len(a['log'])} · {tin:,} ({cached:,}) · {out:,} · {cost:.4f} · {cost / n:.5f} · {ms / 1000:.0f} · {ms / 1000 / n:.2f}")
    print("\narm · things a note · links a note · refused by the check a note · against the readings on file: same things (Jaccard) · same linked pairs · same typed links")
    ref = arms["single"]["held"]
    rows = {"on file": ref}
    rows.update({arm: a["new"] for arm, a in arms.items()})
    for name, rs in rows.items():
        hs = [h for h in ref if rs.get(h) and ref.get(h)]
        print(f"{name:<8} · {mean([len(rs[h]['ents']) for h in hs]):.2f} · {mean([len(rs[h]['rels']) for h in hs]):.2f} · {mean([rs[h]['refused'] for h in hs]):.2f} · "
              f"{mean([jac(rs[h]['ents'], ref[h]['ents']) for h in hs]):.3f} · {mean([jac(rs[h]['pairs'], ref[h]['pairs']) for h in hs]):.3f} · "
              f"{mean([jac(rs[h]['rels'], ref[h]['rels']) for h in hs]):.3f}   ({len(hs)} notes)")
    s, p = arms["single"]["new"], arms["packets"]["new"]
    both = [h for h in ref if s.get(h) and p.get(h)]
    print(f"\nthe two arms against each other, {len(both)} notes: same things {mean([jac(s[h]['ents'], p[h]['ents']) for h in both]):.3f} · "
          f"same linked pairs {mean([jac(s[h]['pairs'], p[h]['pairs']) for h in both]):.3f} · same typed links {mean([jac(s[h]['rels'], p[h]['rels']) for h in both]):.3f}")
    order = work / "packets-order.json"  # written by `positions`, when the prompts were saved
    if order.exists():
        pos = json.loads(order.read_text())
        quart = {q: [] for q in range(4)}
        for h, (i, n) in pos.items():
            if p.get(h) and s.get(h):
                quart[min(3, i * 4 // max(1, n))].append((len(p[h]["ents"]) + len(p[h]["rels"])) / max(1, len(s[h]["ents"]) + len(s[h]["rels"])))
        print("by place in the packet, things and links kept as a share of the same note read alone: "
              + " · ".join(f"quarter {q + 1}: {mean(v):.2f} ({len(v)})" for q, v in quart.items()))


def positions(work, saved):
    """Where each note stood in its packet, from the prompts a command saved (FAKE_SAVE-style folder of *.txt)."""
    import re
    pos = {}
    for f in sorted(Path(saved).glob("*")):
        ids = re.findall(r"^NOTE ([0-9a-f]{12}) ", f.read_text(), re.M)
        for i, h in enumerate(ids):
            pos.setdefault(h, (i, len(ids)))
    (Path(work) / "packets-order.json").write_text(json.dumps(pos))
    print(f"{len(pos)} notes placed, from {saved}")


if __name__ == "__main__":
    verb = sys.argv[1] if len(sys.argv) > 1 else ""
    if verb == "prepare":
        prepare(sys.argv[2], sys.argv[3], int(sys.argv[sys.argv.index("--areas") + 1]) if "--areas" in sys.argv else 10)
    elif verb == "compare":
        compare(sys.argv[2])
    elif verb == "positions":
        positions(sys.argv[2], sys.argv[3])
    else:
        raise SystemExit(__doc__)
