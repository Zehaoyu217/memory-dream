#!/usr/bin/env python3
"""Where the design should win (REVIEW.md phase E): question sets that grep answers badly, measured offline.

  adversarial.py <memory root> <questions.jsonl…> [--index-world <root>] [--show]

Sets, all built from existing data with no model:
  stale   bank questions whose gold names a superseded note and its successor: does `ask` head the successor above
          the old note and mark the old one SUPERSEDED? (grep prints both unmarked; the agent must open frontmatter)
  scatter bank questions with 2+ gold notes: all gold headed, and characters, for `ask` against the grep strategies
          (one grep printing every matching line; `cat` of the named project folder)
  alias   on a world with a real index: "what do we know about <surface form>?" for entities whose written name is
          not their id; gold = the entity's home or headline note. `ask` with the index, `ask` without, grep of the form.
"""
import contextlib
import importlib.util
import io
import json
from collections import Counter
import os
import random
import re
import statistics
import subprocess
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

MEM = Path(os.environ.get("MEM_PY") or Path(__file__).resolve().parent.parent / "skills/memory-dream/scripts/memory.py")
_spec = importlib.util.spec_from_file_location("memory", MEM)
mem = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mem)


def run_ask(root, qs, env=None):
    buf, old = io.StringIO(), dict(os.environ)
    os.environ.update(env or {})
    try:
        with contextlib.redirect_stdout(buf):
            mem.main(["ask", "--root", str(root), *qs])
    finally:
        os.environ.clear()
        os.environ.update(old)
    return buf.getvalue()


def sections(out):
    parts = re.split(r"^## (.*)$", out, flags=re.M)
    return [(parts[i], parts[i + 1]) for i in range(1, len(parts) - 1, 2)]


def heads(sec):
    return re.findall(r"^▸ (\S+)", sec, re.M)


def grep_lines(root, pats, where=None):
    with tempfile.NamedTemporaryFile("w", suffix=".pat", delete=False) as f:
        f.write("\n".join(sorted(pats)) + "\n")
    r = subprocess.run(["grep", "-rniaF", "--include=*.md", "--exclude-dir=_dream", "-f", f.name, str(where or root)],
                       capture_output=True, text=True, errors="replace")
    os.unlink(f.name)
    hits = defaultdict(list)
    for ln in r.stdout.splitlines():
        m = re.match(r"(.*?):(\d+):(.*)$", ln)
        if m:
            hits[os.path.relpath(m.group(1), root)].append(m.group(3))
    return hits


def stale(root, qs, g, show):
    """Questions whose gold has an old → new pair: did ask put the successor above the old note, marked?"""
    sup = {e["dst"]: e["src"] for e in g["edges"] if e["rel"] == "supersedes"}
    items = [q for q in qs if any(o in q["notes"] and sup[o] in q["notes"] for o in sup)]
    if not items:
        return {"n": 0}
    present = above = marked = both = unmarked = 0
    for i in range(0, len(items), 10):
        batch = items[i:i + 10]
        out = run_ask(root, [q["q"] for q in batch])
        for q, (_, sec) in zip(batch, sections(out)):
            hs = heads(sec)
            pairs = [(o, sup[o]) for o in sup if o in q["notes"] and sup[o] in q["notes"]]
            ok_present = all(n in hs for o, n in pairs)
            ok_above = all(n in hs and (o not in hs or hs.index(n) < hs.index(o)) for o, n in pairs)
            ok_mark = all(o not in hs or re.search(r"^▸ " + re.escape(o) + r".*SUPERSEDED", sec, re.M) for o, n in pairs)
            present += ok_present
            above += ok_above
            marked += ok_mark
            both += ok_above and ok_mark
            unmarked += not ok_mark  # an old note shown as if current: the trap grep sets, sprung
            if show and not (ok_above and ok_mark):
                print("  stale miss:", q["q"][:90], pairs, hs[:4])
    n = len(items)
    return {"n": n, "successor_headed": round(present / n, 3), "successor_above_old": round(above / n, 3),
            "old_marked_superseded_when_shown": round(marked / n, 3), "old_shown_unmarked": round(unmarked / n, 3),
            "above_and_marked": round(both / n, 3)}


def scatter(root, qs, show):
    """Questions with 2+ gold notes: all gold found, and characters read, for ask vs grep strategies."""
    items = [q for q in qs if len(q["notes"]) >= 2]
    if not items:
        return {"n": 0}
    folders = {p.name for p in root.iterdir() if p.is_dir() and p.name != "_dream"}
    size = {p.relative_to(root).as_posix(): p.stat().st_size for p in root.rglob("*.md") if "_dream" not in p.parts}
    res = {"ask": [0, []], "grep lines": [0, []], "cat named folder": [0, []]}
    for i in range(0, len(items), 10):
        batch = items[i:i + 10]
        out = run_ask(root, [q["q"] for q in batch])
        for q, (_, sec) in zip(batch, sections(out)):
            gold = set(q["notes"])
            hs = set(heads(sec))
            res["ask"][0] += gold <= hs
            res["ask"][1].append(len(sec))
            pats = list(mem.qterms(q["q"]))
            hits = grep_lines(root, pats)
            res["grep lines"][0] += gold <= set(hits)
            res["grep lines"][1].append(sum(len(l) + 1 for ls in hits.values() for l in ls))
            named = [t for t in pats if t in folders]
            if named:
                fs = {f for f in size if f.split("/")[0] in named}
                res["cat named folder"][0] += gold <= fs
                res["cat named folder"][1].append(sum(size[f] for f in fs))
    out = {"n": len(items)}
    for k, (hit, chars) in res.items():
        n = len(chars) or 1
        out[k] = {"all_gold": round(hit / n, 3), "chars_per_q": round(statistics.mean(chars)) if chars else None, "n": len(chars)}
    return out


def alias(index_root, show):
    """On a world with a real index: surface forms that differ from the id. Gold = home or headline note."""
    g = mem.load(index_root)[0]
    items = []
    for e in g["entities"]:
        gold = e["home"] or e["headline"]
        if not gold:
            continue
        for nm in e["names"][:6]:
            s = nm["name"]
            if mem.fold(s) != mem.fold(e["id"]) and 3 <= len(s) <= 40 and not re.search(r"[`\"]", s) and mem.fold(s) not in mem.fold(gold):
                items.append({"q": f"what do we know about {s}?", "gold": gold, "form": s, "id": e["id"]})
                break
    if not items:
        return {"n": 0}
    res = {"ask (index)": 0, "ask (no index)": 0, "grep the form": 0}
    chars = {"ask (index)": [], "ask (no index)": []}
    for i in range(0, len(items), 10):
        batch = items[i:i + 10]
        for name, env in (("ask (index)", {}), ("ask (no index)", {"MEMORY_NO_INDEX": "1"})):
            out = run_ask(index_root, [q["q"] for q in batch], env)
            for q, (_, sec) in zip(batch, sections(out)):
                res[name] += q["gold"] in heads(sec)
                chars[name].append(len(sec))
        for q in batch:
            hits = grep_lines(index_root, [q["form"].lower()])
            res["grep the form"] += q["gold"] in hits
            if show and q["gold"] not in hits:
                print("  alias (grep miss):", q["form"], "→", q["id"], "gold", q["gold"])
    n = len(items)
    return {"n": n, **{k: round(v / n, 3) for k, v in res.items()},
            "chars_per_q": {k: round(statistics.mean(v)) for k, v in chars.items()}}


NONSENSE = ["zorbax rate", "quill index", "the brindle ratio", "velvet scoring", "the tarn method", "marlow cutoff",
            "the saffron holdout", "obelisk features", "the kelp model", "dunlin uplift"]
MADE_UP = ["quillbeam", "tarnwick", "vexhollow", "obrindle", "saffmoor", "kelverin", "dunmarsh", "pyrelock", "wendralt", "moskvane",
           "corrilane", "brastwick", "jorvaney", "lintharbor", "ferrowick", "ostmarle", "tavenrook", "ulmbright", "greysloe", "haddenmere",
           "orvinstone", "pellamoor", "sidrathe", "quenbarrow", "thistlecrag", "varnholt", "wrenfield", "yarrowden", "zelmbrook", "ashcombe"]


def absence(root, g, show):
    """Questions about things the memory does not hold (phase G, after MOOSEDev's negation set): a version that was
    never written (churn-xgb-v3 → -v9), a made-up id with a real prefix, a nonsense term beside a real word. A good
    answer says so: "(no match" or a "(weak match …" marker naming the unknown token. A confident header is a false
    positive. Grep's "every matching line" strategy is the comparator: any line at all counts as a confident answer."""
    ids = sorted({n["id"] for n in g["notes"]})
    rnd = random.Random(7)
    ver = [i for i in ids if re.search(r"-v\d+$", i)]
    bumps = [re.sub(r"-v\d+$", "-v9", i) for i in rnd.sample(ver, min(40, len(ver)))]
    bumps = [b for b in bumps if b not in ids][:30]
    made = [f"{p}-{w}" for p, w in zip(rnd.sample(["feat", "exp", "dec", "ds", "fnd", "find", "q"] * 5, 30), MADE_UP)]
    qs = [("version bump", f"what do we know about {x}?", x) for x in bumps] + \
         [("made-up id", f"what do we know about {x}?", x) for x in made] + \
         [("nonsense term", f"what is {t}?", t) for t in NONSENSE]
    flagged, grep_quiet, n_by = Counter(), Counter(), Counter()
    for i in range(0, len(qs), 10):
        batch = qs[i:i + 10]
        out = run_ask(root, [q for _, q, _ in batch])
        for (kind, q, form), (_, sec) in zip(batch, sections(out)):
            n_by[kind] += 1
            ok = "(no match" in sec or "weak match" in sec
            flagged[kind] += ok
            words = [w for w in re.findall(r"[a-z0-9][a-z0-9.-]*", form.lower()) if len(w) >= 3 and w not in ("the",)]
            grep_quiet[kind] += not grep_lines(root, words)
            if show and not ok:
                print("  absence (confident):", q, "→", heads(sec)[:2])
    n = sum(n_by.values())
    return {"n": n, "ask flagged": round(sum(flagged.values()) / n, 3), "grep lines empty": round(sum(grep_quiet.values()) / n, 3),
            "by kind": {k: f"{flagged[k]}/{n_by[k]}" for k in n_by}}


def main():
    args = sys.argv[1:]
    show = "--show" in args
    index_root = Path(args[args.index("--index-world") + 1]).resolve() if "--index-world" in args else None
    files = [a for a in args[1:] if a.endswith(".jsonl")]
    root = Path(args[0]).resolve()
    qs = [json.loads(x) for f in files for x in Path(f).read_text().splitlines() if x.strip()]
    g = mem.load(root)[0]
    out = {"stale": stale(root, qs, g, show), "scatter": scatter(root, qs, show), "absence": absence(root, g, show)}
    if index_root:
        out["alias"] = alias(index_root, show)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
