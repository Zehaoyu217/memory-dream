#!/usr/bin/env python3
"""memory-dream v0.4: notes are the truth; a cheap model builds a routing table over them.

  memory.py dream [--cmd C] [-j N] [--gists] [--review] [--all]
  memory.py where <terms...> [-p P]
  memory.py trace <note or entity> [--up|--down] [--rel t,...] [--depth N]
  memory.py check
  memory.py log "text" [-p P]

Stdlib only. Every verb rescans first; only `dream` calls the model or writes derived files.
Spec: .specs/memory-dream/build-spec.md
"""
import argparse
import datetime as dt
import difflib
import hashlib
import json
import math
import os
import posixpath
import re
import subprocess
import sys
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

V = "0.4"
SKIP = {"INDEX.md", "EDGES.md", "ALIASES.md", "README.md"}
KINDS = set("question experiment finding decision dataset feature model metric concept log note".split())
TIMEOUT = int(os.environ.get("MEMORY_TIMEOUT", "300"))
KEEP_DAYS = 30

EDGES_SEED = """# EDGES — relation types, read "X <type> Y". Edit freely; relations relabel on the next merge.
- uses: X needs Y as an input (model uses feature; feature uses table) | aka: depends-on, consumes, built-on, ~feeds
- produces: X creates or writes Y (notebook produces table; job produces scores) | aka: writes, creates, ~generated-by
- part-of: X is a component of Y (column part-of table; feature part-of feature-set) | aka: ~contains, ~has
- trained-on: model X was fit on dataset Y | aka: fit-on
- evaluated-on: X was measured on dataset or segment Y | aka: tested-on, validated-on
- replaces: X is the newer version of Y | aka: supersedes, ~replaced-by
- owned-by: X is maintained by person or team Y | aka: maintained-by, ~owns
drop: related-to, associated-with, about
"""
ALIASES_HEAD = ("# ALIASES — entity ids that name the same thing; the first id on a line is canonical. "
                "Edit freely.\n")

EXTRACT = """Index this memory note for retrieval. Reply with JSON only:
{"kind": "question|experiment|finding|decision|dataset|feature|model|metric|concept|log|note",
 "summary": "the main point in at most 25 words; copy numbers exactly",
 "entities": [{"id": "...", "type": "dataset|feature|model|metric|segment|person|concept|tool|project|other",
               "as": ["text copied verbatim from the note"]}],
 "relations": [{"s": "entity id", "type": "relation type", "o": "entity id",
                "quote": "short text copied verbatim from the note that states it",
                "def": "only for a type not in EDGES: a one-line definition"}],
 "refs": ["ids or paths of other notes the text explicitly points to"]}
Entities are named things someone would look up later: tables, columns, features, models,
metrics, segments, people, methods, tools. Not generic words.
If an entity is in KNOWN, reuse its id. Otherwise id = its most specific name, lowercase,
spaces to hyphens.
Relations: only ones the note states, read "s <type> o". Use an EDGES type or one of its
aliases (aliases marked ~ read in reverse). If none fits, name a new type and give "def".
EDGES:
{edges}
KNOWN:
{known}
NOTE {path}:
{text}
"""
REVIEW = """You keep the vocabulary of a data-science memory.
RELATION TYPES, read "X <type> Y":
{edges}
PROPOSED TYPES (definition; uses; up to 3 examples "X — Y: quote"):
{proposals}
ENTITY PAIRS that may name the same thing (id, type, surface forms, one context line each):
{pairs}
Reply with JSON only:
{"types": {"<proposed>": "alias T" | "alias ~T" | "new" | "drop"},
 "entities": {"<a> / <b>": "same" | "different"}}
If unsure between alias and new, answer new. If unsure whether two entities are the same
thing, answer different. Versions (v2, v3) are different things.
{merge}"""
MERGE_ASK = 'Also list existing types that mean the same as another, under "types", as "A": "alias B".\n'
GIST = """Summarise what a data-science memory knows about one entity, from the lines that mention it.
Reply with JSON only: {"gist": "at most 40 words; copy numbers exactly", "key": ["ids of the notes that matter most"]}
ENTITY {id} ({type})
LINES (note id · date · line: text):
{lines}
"""


# ---------- small helpers ----------

def fold(s):
    return re.sub(r"[\s_]+", "-", str(s).strip().lower())


def nums(s):
    return set(re.findall(r"\d+(?:\.\d+)?", s))


def versions(a, b):
    """Ids that differ only in digits name different versions; never merged by rule or review."""
    return a != b and re.sub(r"\d+", "", a) == re.sub(r"\d+", "", b)


def qpat(q):
    """Verbatim match, case-insensitive, whitespace runs collapsed, backticks/asterisks ignored."""
    toks = [t.strip("`*") for t in str(q).split()]
    toks = [t for t in toks if t]
    return re.compile(r"[\s`*]+".join(map(re.escape, toks)), re.I) if toks else None


def line_at(text, i):
    return text.count("\n", 0, i) + 1


def fill(tpl, **kw):
    return re.sub(r"\{(\w+)\}", lambda m: str(kw[m.group(1)]) if m.group(1) in kw else m.group(0), tpl)


def parse_json(out):
    if not out:
        return None
    i, j = out.find("{"), out.rfind("}")
    if i < 0 or j <= i:
        return None
    try:
        obj = json.loads(out[i:j + 1])
    except ValueError:
        return None
    return obj if isinstance(obj, dict) else None


def safe(s):
    return re.sub(r"[^\w.-]+", "_", s)[:120]


def read(p):
    return p.read_text(encoding="utf-8", errors="replace")


def rd(p, default=None):
    try:
        return json.loads(read(p))
    except (OSError, ValueError):
        return default


def wr(p, obj):
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_name(p.name + ".tmp")
    tmp.write_text(obj if isinstance(obj, str) else json.dumps(obj, ensure_ascii=False, indent=1),
                   encoding="utf-8")
    tmp.replace(p)


def mmdd(d):
    return d[5:10] if d else "--"


def find_root(arg):
    if arg:
        return Path(arg).expanduser().resolve()
    if os.environ.get("MEMORY_DIR"):
        return Path(os.environ["MEMORY_DIR"]).expanduser().resolve()
    here = Path.cwd().resolve()
    for d in (here, *here.parents):
        if (d / "memory").is_dir():
            return d / "memory"
    return here / "memory"


# ---------- notes ----------

def scan(root, man):
    """Current notes {path: {sha, mtime, size}}, re-hashing only files whose stat changed; detect moves."""
    old, cur = man.get("files", {}), {}
    if root.is_dir():
        for p in root.rglob("*.md"):
            rel = p.relative_to(root).as_posix()
            parts = rel.split("/")
            if parts[0] == "_dream" or p.name in SKIP or any(x.startswith(".") for x in parts):
                continue
            st, o = p.stat(), old.get(rel)
            same = o and o.get("mtime") == st.st_mtime_ns and o.get("size") == st.st_size
            cur[rel] = {"sha": o["sha"] if same else hashlib.sha256(p.read_bytes()).hexdigest(),
                        "mtime": st.st_mtime_ns, "size": st.st_size}
    oldf = man.get("former", {})
    former = {p: list(v) for p, v in oldf.items() if p in cur}
    arrived = defaultdict(list)
    for p in cur:
        if p not in old:
            arrived[cur[p]["sha"]].append(p)
    moved, deleted = [], []
    for p in (p for p in old if p not in cur):
        c = arrived.get(old[p]["sha"], [])
        if len(c) == 1:  # same content at exactly one new path: a move
            former[c[0]] = sorted(set(former.get(c[0], []) + [p] + oldf.get(p, [])))
            moved.append((p, c[0]))
        else:
            deleted.append(p)
    return cur, former, moved, deleted


def parse_note(text):
    """-> frontmatter dict, title, title line (1-based file line), body [[links]] outside code."""
    lines, fm, i0 = text.split("\n"), {}, 0
    if lines and lines[0].strip() == "---":
        for j in range(1, min(len(lines), 80)):
            if lines[j].strip() == "---":
                key = None
                for ln in lines[1:j]:
                    m = re.match(r"([A-Za-z_][\w-]*)\s*:\s*(.*)$", ln)
                    if m:
                        key = m.group(1).lower()
                        fm[key] = re.sub(r"\s+#.*$", "", m.group(2)).strip()
                    elif key and re.match(r"\s*-\s+", ln):
                        item = re.sub(r"\s+#.*$", "", ln.strip()[1:]).strip()
                        fm[key] = (fm[key] + ", " if fm[key] else "") + item
                i0 = j + 1
                break
    title, tline, fence, links = "", 0, False, []
    for k in range(i0, len(lines)):
        ln = lines[k]
        if ln.lstrip().startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        if not title and ln.startswith("# "):
            title, tline = ln[2:].strip(), k + 1
        links += re.findall(r"\[\[([^\]|#]+)", re.sub(r"`[^`]*`", "", ln))
    return fm, title, tline, links


def fm_list(v):
    v = (v or "").strip()
    if v.startswith("[") and v.endswith("]") and not re.fullmatch(r"\[\[[^\]]*\]\]", v):
        v = v[1:-1]
    out = []
    for x in v.split(","):
        x = re.sub(r"^\[\[(.*)\]\]$", r"\1", x.strip().strip("'\"")).strip()
        if x:
            out.append(x)
    return out


def ground(ans, text, title):
    """Keep only what the note supports: entities by `as`, relations by quote, summary by numbers."""
    dropped = {"entities": [], "relations": 0, "summary": False}
    ents, kept = [], {}
    for e in ans.get("entities") or []:
        if not isinstance(e, dict) or not str(e.get("id") or "").strip():
            continue
        ok = [a for a in (e.get("as") or []) if isinstance(a, str) and qpat(a) and qpat(a).search(text)]
        if not ok:
            dropped["entities"].append(str(e["id"]))
            continue
        lines = sorted({line_at(text, m.start()) for a in ok for m in qpat(a).finditer(text)})
        k = fold(e["id"])
        if k in kept:
            kept[k]["as"] = sorted(set(kept[k]["as"]) | set(ok))
            kept[k]["lines"] = sorted(set(kept[k]["lines"]) | set(lines))
            continue
        kept[k] = {"id": str(e["id"]).strip(), "type": str(e.get("type") or "other").strip().lower(),
                   "as": ok, "lines": lines}
        ents.append(kept[k])
    rels = []
    for r in ans.get("relations") or []:
        if not isinstance(r, dict):
            continue
        q = str(r.get("quote") or "")
        m = qpat(q).search(text) if qpat(q) else None
        s, o, t = (str(r.get(k) or "").strip() for k in ("s", "o", "type"))
        if m and t and fold(s) in kept and fold(o) in kept:
            rel = {"s": kept[fold(s)]["id"], "type": t, "o": kept[fold(o)]["id"], "quote": q,
                   "line": line_at(text, m.start())}
            if r.get("def"):
                rel["def"] = str(r["def"])
            rels.append(rel)
        else:
            dropped["relations"] += 1
    summary = str(ans.get("summary") or "").strip()
    if not summary or not nums(summary) <= nums(text):
        dropped["summary"] = bool(summary)
        summary = title
    kind = str(ans.get("kind") or "").strip().lower()
    return {"kind": kind if kind in KINDS else "note", "summary": summary, "entities": ents,
            "relations": rels, "refs": [str(x) for x in (ans.get("refs") or []) if isinstance(x, str)],
            "dropped": dropped}


# ---------- vocabularies ----------

def parse_edges(text):
    """-> types {T: {def, aka}}, alias {folded: (T, reversed)}, drop, raw type lines, bad lines."""
    types, alias, drop, tl, bad = {}, {}, set(), [], []
    for i, ln in enumerate(text.split("\n"), 1):
        s = ln.strip()
        if not s or s.startswith("#"):
            continue
        m = re.match(r"-\s*([^:|]+?)\s*:\s*(.*)$", s)
        d = re.match(r"drop\s*:(.*)$", s, re.I)
        if m:
            t = fold(m.group(1))
            parts = re.split(r"\|\s*aka\s*:", m.group(2), maxsplit=1)
            aka = [a.strip() for a in parts[1].split(",") if a.strip()] if len(parts) > 1 else []
            types[t] = {"def": parts[0].strip(), "aka": aka}
            alias.setdefault(t, (t, False))
            for a in aka:
                alias.setdefault(fold(a.lstrip("~")), (t, a.startswith("~")))
            tl.append(s)
        elif d:
            drop |= {fold(x) for x in d.group(1).split(",") if x.strip()}
        else:
            bad.append((i, s))
    return types, alias, drop, tl, bad


def split_pair(s):
    a, _, b = s.partition(" / ") if " / " in s else s.partition("/")
    return a.strip(), b.strip()


def parse_aliases(text):
    lines, nots, bad = [], set(), []
    for i, ln in enumerate(text.split("\n"), 1):
        s = ln.strip()
        if not s or s.startswith("#"):
            continue
        m = re.match(r"-\s*(.+?)\s*=\s*(.+)$", s)
        n = re.match(r"not\s*:(.+)$", s, re.I)
        if m:
            lines.append([m.group(1).strip()] + [x.strip() for x in m.group(2).split(",") if x.strip()])
        elif n and "/" in n.group(1):
            a, b = split_pair(n.group(1))
            nots.add(frozenset((fold(a), fold(b))))
        else:
            bad.append((i, s))
    return lines, nots, bad


def edit_edges(text, op, t, arg=""):
    """Review edits: alias (t onto arg's aka), new (t with def arg), drop, fold (type t into arg)."""
    lines = text.rstrip("\n").split("\n")

    def find(T):
        for k, ln in enumerate(lines):
            m = re.match(r"\s*-\s*([^:|]+?)\s*:", ln)
            if m and fold(m.group(1)) == T:
                return k
        return -1

    def add_aka(k, a):
        lines[k] += (", " if re.search(r"\|\s*aka\s*:", lines[k]) else " | aka: ") + a

    dk = next((k for k, ln in enumerate(lines) if re.match(r"\s*drop\s*:", ln, re.I)), -1)
    if op == "alias":
        add_aka(find(arg), t)
    elif op == "new":
        lines.insert(dk if dk >= 0 else len(lines), f"- {t}: {arg or t}")
    elif op == "drop":
        if dk < 0:
            lines.append(f"drop: {t}")
        else:
            lines[dk] = lines[dk].rstrip() + ("" if lines[dk].rstrip().endswith(":") else ",") + " " + t
    elif op == "fold":
        k = find(t)
        parts = re.split(r"\|\s*aka\s*:", lines[k], maxsplit=1)
        moved = [t] + ([a.strip() for a in parts[1].split(",") if a.strip()] if len(parts) > 1 else [])
        del lines[k]
        for a in moved:
            add_aka(find(arg), a)
    return "\n".join(lines) + "\n"


def edit_aliases(text, a, b, same, lead=None):
    lines = text.rstrip("\n").split("\n")
    if not same:
        lines.append(f"not: {a} / {b}")
        return "\n".join(lines) + "\n"
    for k, ln in enumerate(lines):
        m = re.match(r"\s*-\s*(.+?)\s*=\s*(.+)$", ln)
        if m:
            have = {fold(x) for x in [m.group(1)] + m.group(2).split(",")}
            if fold(a) in have or fold(b) in have:
                lines[k] += "".join(", " + x for x in (a, b) if fold(x) not in have)
                return "\n".join(lines) + "\n"
    first = lead or a
    lines.append(f"- {first} = {b if first == a else a}")
    return "\n".join(lines) + "\n"


# ---------- merge ----------

def merge_entities(occ, alines, nots):
    """Entity groups as one union-find: ALIASES lines, folded-id equality, the surface-form rule."""
    par, mem, explicit = {}, {}, set()

    def find(x):
        par.setdefault(x, x)
        mem.setdefault(x, {x})
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x

    def join(a, b, force=False):
        ra, rb = find(a), find(b)
        if ra == rb:
            return
        if not force:
            for x in mem[ra]:
                for y in mem[rb]:
                    p = frozenset((x, y))
                    if p in nots or (versions(x, y) and p not in explicit):
                        return
        par[rb] = ra
        mem[ra] |= mem.pop(rb)

    raw, surf, typ = defaultdict(Counter), defaultdict(Counter), defaultdict(Counter)
    ment = defaultdict(lambda: defaultdict(set))
    for path, e in occ:
        k = fold(e["id"])
        raw[k][e["id"]] += 1
        typ[k][e["type"]] += 1
        for a in e["as"]:
            surf[k][a] += 1
        ment[k][path] |= set(e["lines"])
    lead = {}
    for li, ids in enumerate(alines):
        fs = [fold(i) for i in ids]
        explicit |= {frozenset((x, y)) for x in fs for y in fs if x != y}
        for f in fs:
            lead.setdefault(f, (li, ids[0]))
            join(fs[0], f, force=True)
    sf_index = defaultdict(set)
    for k in raw:
        find(k)
        for a in surf[k]:
            sf_index[fold(a)].add(k)
    for k in raw:  # exactly one other entity writes this id as a surface form → one entity
        users = sf_index.get(k, set())
        others = users - {k}
        if len(users) <= 3 and len(others) == 1:
            join(k, next(iter(others)))
    groups = defaultdict(list)
    for k in raw:
        groups[find(k)].append(k)
    ents, cmap, gkeys = {}, {}, {}
    for ks in groups.values():
        allk = set(ks) | {k for k in mem[find(ks[0])] if k in lead}
        led = sorted(lead[k] for k in allk if k in lead)
        cand, sc, exact = Counter(), Counter(), Counter()
        for k in ks:
            cand.update(raw[k])
        for k in ks:
            for a, n in surf[k].items():
                for rid in cand:
                    sc[rid] += n * (fold(a) == fold(rid))
                    exact[rid] += n * (a == rid)
        c = led[0][1] if led else min(cand, key=lambda r: (-(cand[r] + sc[r]), -exact[r], r.lower(), r))
        tc, names, mm = Counter(), Counter(), defaultdict(set)
        for k in ks:
            tc.update(typ[k])
            names.update(surf[k])
            for p, ls in ment[k].items():
                mm[p] |= ls
        ents[c] = {"id": c, "type": min(tc, key=lambda t: (-tc[t], t)),
                   "aka": sorted({r for k in ks for r in raw[k]} - {c}),
                   "names": [{"name": a, "n": n} for a, n in sorted(names.items(), key=lambda z: (-z[1], z[0]))],
                   "headline": None, "mentions": [{"path": p, "lines": sorted(mm[p])} for p in sorted(mm)],
                   "gist": None}
        gkeys[c] = set(ks)
        for k in ks:
            cmap[k] = c
    return ents, cmap, gkeys


def candidates(ents, new, gkeys, nots, limit_ratio=0.85):
    """Review pairs: same type, sharing a non-generic surface form or with similar folded ids."""
    sfs = {c: {fold(n["name"]) for n in e["names"]} for c, e in ents.items()}
    cnt = Counter(s for v in sfs.values() for s in v)
    by_type = defaultdict(list)
    for c, e in ents.items():
        by_type[e["type"]].append(c)
    out, sm = set(), difflib.SequenceMatcher(autojunk=False)
    for a in new:
        fa = fold(a)
        sm.set_seq2(fa)
        mine = {s for s in sfs[a] if cnt[s] <= 3}
        for b in by_type[ents[a]["type"]]:
            fb = fold(b)
            if b == a or versions(fa, fb):
                continue
            pair = tuple(sorted((a, b), key=fold))
            if pair in out or decided(a, b, gkeys, nots):
                continue
            hit = bool(mine & sfs[b])
            if not hit and 2 * min(len(fa), len(fb)) >= limit_ratio * (len(fa) + len(fb)):
                sm.set_seq1(fb)
                hit = sm.real_quick_ratio() >= limit_ratio and sm.quick_ratio() >= limit_ratio \
                    and sm.ratio() >= limit_ratio
            if hit:
                out.add(pair)
    return out


def decided(a, b, gkeys, nots):
    return any(frozenset((x, y)) in nots for x in gkeys.get(a, {fold(a)}) for y in gkeys.get(b, {fold(b)}))


def build(root, man, cur, former, et, at, xs=None, now=None):
    """The graph = union of current notes' cached subgraphs, renamed by EDGES.md and ALIASES.md."""
    now = now or dt.datetime.now()
    types, alias, drop, _, bad_e = parse_edges(et)
    alines, nots, bad_a = parse_aliases(at)
    checks = [("C8", f"EDGES.md:{i}: {s}") for i, s in bad_e] + [("C8", f"ALIASES.md:{i}: {s}") for i, s in bad_a]
    notes, aux, by_stem = {}, {}, defaultdict(list)
    for rel in sorted(cur):
        h = cur[rel]["sha"]
        text = read(root / rel)
        fm, title, tline, links = parse_note(text)
        x = xs.get(h[:12]) if xs is not None else rd(root / "_dream" / "notes" / f"{h[:12]}.json")
        up = fm.get("updated", "")
        up = up[:10] if re.match(r"\d{4}-\d\d-\d\d", up) else \
            dt.date.fromtimestamp(cur[rel]["mtime"] / 1e9).isoformat()
        proj = rel.split("/")[0] if "/" in rel else ""
        notes[rel] = {"path": rel, "id": posixpath.basename(rel)[:-3], "project": proj, "title": title,
                      "line": tline, "summary": (x or {}).get("summary") or title,
                      "kind": (fm.get("type") or (x or {}).get("kind") or ("log" if proj == "log" else "note")).lower(),
                      "superseded_by": [], "updated": up, "sha": h[:12], "indexed": bool(x)}
        aux[rel] = {"fm": fm, "links": links, "x": x, "mt": cur[rel]["mtime"],
                    "ids": set(re.findall(r"(?<![\w/-])([a-z][a-z0-9]*(?:-[a-z0-9]+)+)(?![\w-])", text.lower().split("\n", tline)[-1]))
                    if tline else set()}
        by_stem[notes[rel]["id"]].append(rel)
        if not title:
            checks.append(("C6", f"{rel}: no '# ' line"))
        if not x:
            checks.append(("C3" if h[:12] in man.get("failed", {}) else "C5", f"{rel}: unindexed"))
        else:
            dr = x.get("dropped") or {}
            checks += [("C4", f"{rel}: entity {e} not in the note") for e in dr.get("entities", [])]
            checks += [("C4", f"{rel}: relation without its quote")] * dr.get("relations", 0)
            checks += [("C4", f"{rel}: summary number not in the note")] * bool(dr.get("summary"))
    old2cur = {o: p for p, olds in former.items() for o in olds if p in notes}
    oldstem = defaultdict(list)
    for o, p in old2cur.items():
        oldstem[posixpath.basename(o)[:-3]].append(p)

    def resolve(v, src):
        v = re.sub(r"^\[\[|\]\]$", "", v.strip()).strip()
        v = v[:-3] if v.endswith(".md") else v
        paths = [posixpath.normpath(posixpath.join(posixpath.dirname(src), v)) + ".md", posixpath.normpath(v) + ".md"]
        for c in paths:
            if c in notes:
                return c, ""
        stem, c = posixpath.basename(v), by_stem.get(posixpath.basename(v), [])
        if len(c) == 1:
            return c[0], ""
        if c:
            mine = [p for p in c if p.split("/")[0] == src.split("/")[0]]
            return sorted(mine or c)[0], "C1"
        for c in paths:
            if c in old2cur:
                return old2cur[c], ""
        return (sorted(oldstem[stem])[0], "") if oldstem.get(stem) else (None, "C2")

    edges, linked = [], set()
    for rel in notes:
        for kind in ("from", "supersedes"):
            for v in fm_list(aux[rel]["fm"].get(kind)):
                dst, w = resolve(v, rel)
                if w:
                    checks.append((w, f"{rel}: {kind} {v} " + (f"is ambiguous, using {dst}" if dst else "not found")))
                if dst and dst != rel and (rel, dst, kind) not in linked:
                    linked.add((rel, dst, kind))
                    edges.append({"src": rel, "dst": dst, "rel": kind})
        x = aux[rel]["x"] or {}
        proj = rel.split("/")[0]
        mentioned = [i for i in aux[rel]["ids"] if any(p_.split("/")[0] == proj for p_ in by_stem.get(i, []))]
        for v in aux[rel]["links"] + list(x.get("refs") or []) + sorted(mentioned):  # a slug written in the body points at that note
            dst = resolve(v, rel)[0]
            if dst and dst != rel and not any((rel, dst, k) in linked for k in ("from", "supersedes", "refs")):
                linked.add((rel, dst, "refs"))
                edges.append({"src": rel, "dst": dst, "rel": "refs"})
    for e in edges:
        if e["rel"] == "supersedes":
            notes[e["dst"]]["superseded_by"].append(e["src"])

    occ = [(rel, e) for rel in notes if aux[rel]["x"] for e in aux[rel]["x"].get("entities", [])]
    ents, cmap, gkeys = merge_entities(occ, alines, nots)
    rels, props = {}, {}
    for rel in notes:
        for r in (aux[rel]["x"] or {}).get("relations", []):
            s, o = cmap.get(fold(r["s"])), cmap.get(fold(r["o"]))
            t = fold(r["type"]).lstrip("~")
            if not s or not o or t in drop:
                continue
            T, rev = alias.get(t, (t, False))
            canon = t in alias
            s, o = (o, s) if rev else (s, o)
            if s == o:
                continue
            rec = rels.setdefault((s, T, o), {"s": s, "type": T, "o": o, "canon": canon, "evidence": []})
            ev = f"{rel}:{r['line']}"
            if ev not in rec["evidence"]:
                rec["evidence"].append(ev)
            if not canon:
                p = props.setdefault(T, {"type": T, "def": r.get("def") or "", "uses": 0, "examples": []})
                p["uses"] += 1
                p["def"] = p["def"] or r.get("def") or ""
                if len(p["examples"]) < 3:
                    p["examples"].append(f"{s} — {o}: {r['quote']}")
    for e in ents.values():
        best = None
        for m in e["mentions"]:
            n = notes[m["path"]]
            if n["superseded_by"]:
                continue
            key = (n["line"] in m["lines"], n["kind"] in ("finding", "decision"), n["updated"], aux[m["path"]]["mt"])
            if best is None or key > best[0]:
                best = (key, m["path"])
        e["headline"] = best[1] if best else None
        gf = rd(root / "_dream" / "entities" / f"{safe(e['id'])}.json")
        if gf and gf.get("hash") == mention_hash(e):
            e["gist"] = gf.get("gist")
    seen = set(man.get("seen", []))
    pairs = candidates(ents, [c for c in ents if fold(c) not in seen], gkeys, nots)
    for a, b in man.get("queue", []):
        a, b = cmap.get(fold(a)), cmap.get(fold(b))
        if a and b and a != b and not decided(a, b, gkeys, nots):
            pairs.add(tuple(sorted((a, b), key=fold)))
    pairs = sorted(pairs, key=lambda p: (fold(p[0]), fold(p[1])))
    proposed = sorted(props.values(), key=lambda p: (-p["uses"], p["type"]))
    checks += [("C7", f"type {p['type']}? ×{p['uses']}: {p['def']}") for p in proposed]
    checks += [("C7", f"entities {a} / {b} await review") for a, b in pairs]
    return {"v": V, "built": now.strftime("%Y-%m-%dT%H:%M"),
            "notes": [notes[p] for p in sorted(notes)],
            "entities": [ents[c] for c in sorted(ents, key=fold)],
            "relations": sorted(rels.values(), key=lambda r: (fold(r["s"]), r["type"], fold(r["o"]))),
            "edges": edges, "proposed": proposed, "review": [{"a": a, "b": b} for a, b in pairs],
            "checks": [{"code": c, "msg": m} for c, m in sorted(checks, key=lambda z: z[0])]}


def mention_hash(e):
    return hashlib.sha256(json.dumps(e["mentions"], sort_keys=True).encode()).hexdigest()[:12]


def vocab_texts(root):
    e, a = root / "EDGES.md", root / "ALIASES.md"
    return (read(e) if e.exists() else EDGES_SEED), (read(a) if a.exists() else ALIASES_HEAD)


def vsig(et, at):
    return hashlib.sha256((et + "\0" + at).encode()).hexdigest()[:16]


def load(root):
    """Freshness: reuse graph.json when nothing changed since the last dream, else re-merge in memory."""
    man = rd(root / "_dream" / "manifest.json", {}) or {}
    cur, former, _, _ = scan(root, man)
    et, at = vocab_texts(root)
    same = {p: f["sha"] for p, f in cur.items()} == {p: f["sha"] for p, f in man.get("files", {}).items()}
    if same and man.get("vsig") == vsig(et, at):
        g = rd(root / "_dream" / "graph.json")
        if g and g.get("v") == V:
            return g, former
    return build(root, man, cur, former, et, at), former


# ---------- dream ----------

def call_model(cmd, prompt):
    """One prompt on stdin, answer on stdout; retry once when unusable. -> (obj or None, calls)."""
    for n in (1, 2):
        try:
            r = subprocess.run(cmd, shell=True, input=prompt, capture_output=True, text=True, timeout=TIMEOUT)
            obj = parse_json(r.stdout) if r.returncode == 0 else None
        except subprocess.TimeoutExpired:
            obj = None
        if obj is not None:
            return obj, n
    return None, 2


def known_lines(ents, project, limit=300):
    def inproj(e):
        return any(m["path"].split("/")[0] == project for m in e["mentions"])
    es = sorted(ents.values(), key=lambda e: (not inproj(e), -len(e["mentions"]), fold(e["id"])))[:limit]
    return "\n".join(f"{e['id']} ({e['type']}): " + "; ".join(n["name"] for n in e["names"][:4]) for e in es) or "(none)"


def dream(args, root):
    root.mkdir(parents=True, exist_ok=True)
    for name, seed in (("EDGES.md", EDGES_SEED), ("ALIASES.md", ALIASES_HEAD)):
        if not (root / name).exists():
            wr(root / name, seed)
    dd, now = root / "_dream", dt.datetime.now()
    (dd / "notes").mkdir(parents=True, exist_ok=True)
    pend = dd / "pending"
    man = rd(dd / "manifest.json", {}) or {}
    cur, former, moved, deleted = scan(root, man)
    cmd = args.cmd or os.environ.get("MEMORY_LLM")
    failed, attempts = man.get("failed", {}), man.get("attempts", {})
    st = Counter()
    by_sha = {}
    for rel in sorted(cur):
        by_sha.setdefault(cur[rel]["sha"][:12], rel)
    xs = {h: x for h in by_sha for x in [rd(dd / "notes" / f"{h}.json")] if x}
    et, at = vocab_texts(root)
    _, _, _, tlines, _ = parse_edges(et)
    alines, nots, _ = parse_aliases(at)

    def entities_now():
        occ = [(rel, e) for rel in cur if cur[rel]["sha"][:12] in xs for e in xs[cur[rel]["sha"][:12]]["entities"]]
        return merge_entities(occ, alines, nots)[0]

    def upd(rel):
        u = parse_note(read(root / rel))[0].get("updated", "")
        return u if re.match(r"\d{4}-\d\d-\d\d", u) else dt.date.fromtimestamp(cur[rel]["mtime"] / 1e9).isoformat()

    todo = [h for h in by_sha if args.all or h not in xs]
    todo.sort(key=lambda h: (upd(by_sha[h]), by_sha[h]))

    def prompt_for(h, ents):
        rel = by_sha[h]
        return fill(EXTRACT, edges="\n".join(tlines), known=known_lines(ents, rel.split("/")[0]),
                    path=rel, text=read(root / rel))

    def ingest(h, ans):
        rel = by_sha[h]
        text = read(root / rel)
        rec = ground(ans, text, parse_note(text)[1])
        rec.update(path=rel, sha=cur[rel]["sha"], model=cmd or "file", indexed_at=now.isoformat(timespec="seconds"))
        wr(dd / "notes" / f"{h}.json", rec)
        xs[h] = rec
        failed.pop(h, None)
        attempts.pop(h, None)
        st["indexed"] += 1

    if cmd:  # command mode: waves of -j parallel calls, KNOWN refreshed between waves
        j = max(1, args.j)
        with ThreadPoolExecutor(j) as ex:
            for w in range(0, len(todo), j):
                wave, ents = todo[w:w + j], entities_now()
                for h, (obj, n) in zip(wave, ex.map(lambda h: call_model(cmd, prompt_for(h, ents)), wave)):
                    st["calls"] += n
                    if obj is None:
                        failed[h] = "unusable answer after one retry"
                    else:
                        ingest(h, obj)
    else:  # file mode: ingest answers beside prompts, write prompts for the rest
        pend.mkdir(parents=True, exist_ok=True)
        for pj in sorted(pend.glob("*.json")):
            h = pj.name[:-5]
            if h not in by_sha:
                continue
            obj = parse_json(read(pj))
            pj.unlink()
            if obj is not None:
                ingest(h, obj)
                (pend / f"{h}.prompt.md").unlink() if (pend / f"{h}.prompt.md").exists() else None
            elif attempts.get(h, 0) >= 1:
                failed[h] = "unusable answer after one retry"
                attempts.pop(h, None)
                (pend / f"{h}.prompt.md").unlink() if (pend / f"{h}.prompt.md").exists() else None
            else:
                attempts[h] = attempts.get(h, 0) + 1
        ents = entities_now()
        for h in todo:
            if h in xs and not args.all:
                continue
            wr(pend / f"{h}.prompt.md", prompt_for(h, ents))
        for pp in pend.glob("*.prompt.md"):  # stale prompts: note changed or gone
            k = pp.name[:-len(".prompt.md")]
            if not (k in by_sha or k == "review" or k.startswith("gist-")):
                pp.unlink()

    def graph():
        e2, a2 = vocab_texts(root)
        return build(root, {**man, "failed": failed}, cur, former, e2, a2, xs=xs, now=now)

    g = graph()
    review = {"pairs": 0, "types": 0, "calls": 0, "aliases": 0, "newtypes": 0}

    def apply_review(ans, props, pairs):
        e2, a2 = vocab_texts(root)
        types = parse_edges(e2)[0]
        mentions = {e["id"]: len(e["mentions"]) for e in g["entities"]}
        pmap = {fold(p["type"]): p for p in props}
        for t, v in (ans.get("types") or {}).items():
            t, v = fold(t), str(v).strip().lower()
            if t in pmap:
                if v.startswith("alias"):
                    tgt = v[5:].strip()
                    if fold(tgt.lstrip("~")) in types:
                        e2 = edit_edges(e2, "alias", ("~" if tgt.startswith("~") else "") + t, fold(tgt.lstrip("~")))
                        continue
                    v = "new"
                if v == "new":
                    e2 = edit_edges(e2, "new", t, pmap[t]["def"])
                    review["newtypes"] += 1
                elif v == "drop":
                    e2 = edit_edges(e2, "drop", t)
            elif t in types and v.startswith("alias") and len(types) > 20:
                b = fold(v[5:].strip().lstrip("~"))
                if b in types and b != t:
                    e2 = edit_edges(e2, "fold", t, b)
        asked = {frozenset((fold(a), fold(b))): (a, b) for a, b in pairs}
        for k, v in (ans.get("entities") or {}).items():
            a, b = split_pair(str(k))
            ab = asked.get(frozenset((fold(a), fold(b))))
            v = str(v).strip().lower()
            if ab and v in ("same", "different"):
                a, b = ab
                lead = a if mentions.get(a, 0) >= mentions.get(b, 0) else b
                a2 = edit_aliases(a2, a, b, v == "same", lead)
                review["aliases"] += v == "same"
        if e2 != vocab_texts(root)[0]:
            wr(root / "EDGES.md", e2)
        if a2 != vocab_texts(root)[1]:
            wr(root / "ALIASES.md", a2)

    def review_prompt():
        types = parse_edges(vocab_texts(root)[0])[0]
        props = [p for p in g["proposed"] if p["uses"] >= 2 or args.review]
        pairs = [(r["a"], r["b"]) for r in g["review"]][:30]
        if not props and not pairs and not (args.review and len(types) > 20):
            return None, props, pairs
        ents = {e["id"]: e for e in g["entities"]}

        def ctx(e):
            m = e["mentions"][0]
            return read(root / m["path"]).split("\n")[m["lines"][0] - 1].strip()[:160]

        def desc(c):
            e = ents[c]
            return f"{c} ({e['type']}; " + "; ".join(f'"{n["name"]}"' for n in e["names"][:3]) + f") «{ctx(e)}»"
        pr = fill(REVIEW, edges="\n".join(parse_edges(vocab_texts(root)[0])[3]),
                  proposals="\n".join(f"- {p['type']}: {p['def'] or '?'}; uses {p['uses']}; "
                                      + "; ".join(f'"{x}"' for x in p["examples"]) for p in props) or "none",
                  pairs="\n".join(f"- {a} / {b}: {desc(a)} | {desc(b)}" for a, b in pairs) or "none",
                  merge=MERGE_ASK if len(types) > 20 else "")
        return pr, props, pairs

    due = args.review or any(p["uses"] >= 2 for p in g["proposed"]) or g["review"]
    if cmd and due:
        pr, props, pairs = review_prompt()
        if pr:
            obj, n = call_model(cmd, pr)
            review.update(pairs=len(pairs), types=len(props), calls=n)
            if obj is not None:
                apply_review(obj, props, pairs)
                g = graph()
    elif not cmd:
        rj = pend / "review.json"
        if rj.exists():
            obj = parse_json(read(rj))
            props, pairs = g["proposed"], [(r["a"], r["b"]) for r in g["review"]]
            review.update(pairs=len(pairs), types=len(props))
            if obj is not None:
                apply_review(obj, props, pairs)
                g = graph()
            rj.unlink()
            (pend / "review.prompt.md").unlink() if (pend / "review.prompt.md").exists() else None
        pr = review_prompt()[0] if (args.review or any(p["uses"] >= 2 for p in g["proposed"]) or g["review"]) else None
        if pr:
            wr(pend / "review.prompt.md", pr)
        elif (pend / "review.prompt.md").exists():
            (pend / "review.prompt.md").unlink()

    if args.gists and gists(root, g, cmd, pend, st, now, args.j):
        g = graph()

    # cache upkeep: keep extractions referenced in the last KEEP_DAYS (edit reverts reuse them)
    refs = man.get("refs", {})
    today = now.date().isoformat()
    for h in by_sha:
        refs[h] = today
    cutoff = (now.date() - dt.timedelta(days=KEEP_DAYS)).isoformat()
    for f in (dd / "notes").glob("*.json"):
        h = f.name[:-5]
        last = refs.get(h) or dt.date.fromtimestamp(f.stat().st_mtime).isoformat()
        if h not in by_sha and last < cutoff:
            f.unlink()
            refs.pop(h, None)
    e2, a2 = vocab_texts(root)
    wr(dd / "graph.json", g)
    wr(root / "INDEX.md", index_md(g, now))
    todo_list = sorted(p for p in pend.glob("*.prompt.md")) if pend.exists() else []
    todo_list = [p for p in todo_list if not (pend / (p.name[:-len(".prompt.md")] + ".json")).exists()]
    pending = len(todo_list)
    if pending:  # the dreamer may have no way to list files: name them
        wr(pend / "TODO.md", "# pending prompts: answer each with <same name>.json\n"
           + "".join(f"{p.resolve()}\n" for p in todo_list))
    elif (pend / "TODO.md").exists():
        (pend / "TODO.md").unlink()
    wr(dd / "manifest.json", {"v": V, "files": cur, "former": former, "vsig": vsig(e2, a2),
                              "seen": sorted(fold(e["id"]) for e in g["entities"]),
                              "queue": [[r["a"], r["b"]] for r in g["review"]],
                              "failed": failed, "attempts": attempts, "refs": refs,
                              "dreamed": now.isoformat(timespec="seconds")})
    codes = Counter(c["code"] for c in g["checks"] if c["code"] != "C5")
    out = f"dream: {len(cur)} notes · {st['indexed']} indexed ({st['calls']} calls)"
    if review["pairs"] or review["types"]:
        pl = lambda n, w: f"{n} {w}" + ("s" if n != 1 else "")  # noqa: E731
        out += f" · review: {pl(review['pairs'], 'pair')}, {pl(review['types'], 'type')} " + \
            (f"({pl(review['calls'], 'call')})" if cmd else "(file mode)")
    out += f" · +{review['aliases']} aliases" if review["aliases"] else ""
    out += f" · +{review['newtypes']} types" if review["newtypes"] else ""
    out += f" · {st['gists']} gists ({st['gcalls']} calls)" if st["gists"] or st["gcalls"] else ""
    out += f" · {len(moved)} moved" if moved else ""
    out += f" · {len(deleted)} deleted" if deleted else ""
    out += f" · {pending if not cmd else sum(1 for n in g['notes'] if not n['indexed'])} pending"
    out += (" · " + " ".join(f"{c}×{n}" for c, n in sorted(codes.items()))) if codes else ""
    print(out)
    if pending:
        print(f"{pending} prompts listed in {pend / 'TODO.md'}: run the memory-dreamer subagent, "
              "then memory.py dream again")


def gists(root, g, cmd, pend, st, now, j):
    """Optional gists for entities in >= 3 notes whose mention set changed; numbers grounded."""
    notes = {n["path"]: n for n in g["notes"]}
    jobs = []
    for e in g["entities"]:
        if len(e["mentions"]) < 3:
            continue
        h, f = mention_hash(e), root / "_dream" / "entities" / f"{safe(e['id'])}.json"
        old = rd(f)
        if old and old.get("hash") == h:
            continue
        rows = []
        for m in sorted(e["mentions"], key=lambda m: notes[m["path"]]["updated"], reverse=True):
            tl = read(root / m["path"]).split("\n")
            for ln in m["lines"]:
                ctx = " ".join(x.strip() for x in tl[max(0, ln - 2):ln + 1] if x.strip())
                rows.append(f"- {notes[m['path']]['id']} · {notes[m['path']]['updated']} · {ln}: {ctx[:300]}")
        rows = rows[:30]
        jobs.append((e, h, f, fill(GIST, id=e["id"], type=e["type"], lines="\n".join(rows)), "\n".join(rows)))

    def keep(e, h, f, src, obj):
        ids = {notes[m["path"]]["id"] for m in e["mentions"]}
        gist = str(obj.get("gist") or "").strip()
        wr(f, {"id": e["id"], "hash": h, "gist": gist if gist and nums(gist) <= nums(src) else None,
               "key": [k for k in (obj.get("key") or []) if k in ids], "at": now.isoformat(timespec="seconds")})
        st["gists"] += 1

    if cmd:
        with ThreadPoolExecutor(max(1, j)) as ex:
            for (e, h, f, pr, src), (obj, n) in zip(jobs, ex.map(lambda jb: call_model(cmd, jb[3]), jobs)):
                st["gcalls"] += n
                if obj is not None:
                    keep(e, h, f, src, obj)
    else:
        for e, h, f, pr, src in jobs:
            pj, pp = pend / f"gist-{safe(e['id'])}.json", pend / f"gist-{safe(e['id'])}.prompt.md"
            obj = parse_json(read(pj)) if pj.exists() else None
            if obj is not None:
                keep(e, h, f, src, obj)
                pj.unlink()
                pp.unlink() if pp.exists() else None
            else:
                wr(pp, pr)
    return st["gists"]


def index_md(g, now):
    notes = g["notes"]
    byp = {n["path"]: n for n in notes}
    frm = defaultdict(list)
    for e in g["edges"]:
        if e["rel"] == "from":
            frm[e["src"]].append(byp[e["dst"]]["id"])

    def tail(n):
        s = f" · from {', '.join(frm[n['path']])}" if frm[n["path"]] else ""
        if n["superseded_by"]:
            s += " (superseded → " + ", ".join(byp[p]["id"] for p in n["superseded_by"]) + ")"
        return s

    pending = sum(1 for n in notes if not n["indexed"])
    warn = sum(1 for c in g["checks"] if c["code"] != "C5")
    nprop = sum(1 for r in g["relations"] if not r["canon"])
    out = [f"# memory · {g['built'].replace('T', ' ')} · {len(notes)} notes · {len(g['entities'])} entities · "
           f"{len(g['relations'])} relations ({nprop} proposed) · {pending} pending · {warn} warnings", "## projects"]
    projs = defaultdict(list)
    for n in notes:
        projs[n["project"] or "(root)"].append(n)
    for p in sorted(projs):
        out.append(f"- {p} · {len(projs[p])} notes · {mmdd(max(n['updated'] for n in projs[p]))}")
    week = (now.date() - dt.timedelta(days=7)).isoformat()
    recent = sorted((n for n in notes if n["updated"] >= week and n["kind"] != "log"),
                    key=lambda n: (n["updated"], n["path"]), reverse=True)[:10]
    out.append("## recent (7d)")
    out += [f"- {n['path']} · {n['kind']} · {mmdd(n['updated'])} — {n['title'] or n['path']}{tail(n)}" for n in recent]
    out.append("## entities (top 20 by notes, with headline)")
    for e in sorted(g["entities"], key=lambda e: (-len(e["mentions"]), fold(e["id"])))[:20]:
        hl = byp[e["headline"]]["title"] if e["headline"] else ""
        out.append(f"- {e['id']} · {e['type']} · {len(e['mentions'])} notes" + (f" — {hl}" if hl else ""))
    for p in sorted(projs):
        out.append(f"## {p}")
        for n in sorted(projs[p], key=lambda n: (n["updated"], n["path"]), reverse=True):
            rel = n["path"][len(p) + 1:] if n["project"] else n["path"]
            out.append(f"- {rel} · {n['kind']} · {mmdd(n['updated'])} — {n['title'] or n['path']}{tail(n)}")
    return "\n".join(out) + "\n"


# ---------- retrieval ----------

class View:
    def __init__(self, g):
        self.g = g
        self.notes = {n["path"]: n for n in g["notes"]}
        self.ents = {e["id"]: e for e in g["entities"]}
        self.efold = {}
        for e in g["entities"]:
            for k in [e["id"]] + e["aka"]:
                self.efold.setdefault(fold(k), e["id"])
        self.out_r, self.in_r = defaultdict(list), defaultdict(list)
        for r in g["relations"]:
            self.out_r[r["s"]].append(r)
            self.in_r[r["o"]].append(r)
        self.frm, self.down = defaultdict(list), defaultdict(list)
        for e in g["edges"]:
            self.frm[e["src"]].append(e)
            self.down[e["dst"]].append(e)

    def note_line(self, n, line=None):
        s = f"{n['path']}:{line or n['line'] or 1}  {n['kind']} {mmdd(n['updated'])}  {n['title'] or n['path']}"
        f = [self.notes[e["dst"]]["id"] for e in self.frm[n["path"]] if e["rel"] == "from"]
        s += f" · from {', '.join(f)}" if f else ""
        if n["superseded_by"]:
            s += " (superseded → " + ", ".join(self.notes[p]["id"] for p in n["superseded_by"]) + ")"
        return s


def where(args, root):
    g, _ = load(root)
    v, P = View(g), args.p
    terms = [t.lower() for t in args.terms]
    q = " ".join(terms)

    def inp(path):
        return not P or path.split("/")[0] == P

    ents = [e for e in g["entities"] if any(inp(m["path"]) for m in e["mentions"])]
    notes = [n for n in g["notes"] if inp(n["path"])]

    def etext(e):
        return " ".join([e["id"], *e["aka"], *(n["name"] for n in e["names"])]).lower()

    def ntext(n):
        return " ".join([n["path"], n["title"], n["summary"] or ""]).lower()

    if terms:
        def score(e):
            if fold(q) in {fold(x) for x in [e["id"], *e["aka"], *(n["name"] for n in e["names"])]}:
                return 3
            return 2 if all(t in " ".join([e["id"], *e["aka"]]).lower() for t in terms) else int(all(t in etext(e) for t in terms))
        em = sorted((e for e in ents if score(e)), key=lambda e: (-score(e), -len(e["mentions"]), fold(e["id"])))
        nm = [n for n in notes if all(t in ntext(n) for t in terms)]
        if not em and not nm:  # any term, then fuzzy
            em = sorted((e for e in ents if any(t in etext(e) for t in terms)),
                        key=lambda e: (-sum(t in etext(e) for t in terms), -len(e["mentions"])))
            nm = sorted((n for n in notes if any(t in ntext(n) for t in terms)),
                        key=lambda n: -sum(t in ntext(n) for t in terms))
        if not em and not nm:
            pool = {fold(e["id"]): ("e", e) for e in ents}
            pool.update({fold(n["id"]): ("n", n) for n in notes})
            for k in difflib.get_close_matches(fold(q), list(pool), n=8, cutoff=0.6):
                (em if pool[k][0] == "e" else nm).append(pool[k][1])
    else:
        em = sorted(ents, key=lambda e: (-len(e["mentions"]), fold(e["id"])))
        nm = notes
    shown = set()
    for e in em[:8]:
        names = ", ".join(f'"{n["name"]}"' for n in e["names"][:4])
        print(f"{e['id']} · {e['type']} · {len(e['mentions'])} notes" + (f" · aka {', '.join(e['aka'][:4])}" if e["aka"] else "")
              + (f" · as {names}" if names else ""))
        if e["headline"]:
            h = v.notes[e["headline"]]
            print(f"  headline {h['path']}:{h['line'] or 1}  {h['title']}")
        if e["gist"]:
            print(f"  gist {e['gist']}")
        for arrow, rs, end in (("←", v.in_r[e["id"]], "s"), ("→", v.out_r[e["id"]], "o")):
            grp = defaultdict(list)
            for r in rs:
                grp[r["type"] + ("" if r["canon"] else "?")].append(r)
            for t, rr in grp.items():
                ev = [x for r in rr for x in r["evidence"]]
                print(f"  {arrow} {t} {', '.join(r[end] for r in rr)}   {ev[0]}" + (f" (+{len(ev) - 1})" if len(ev) > 1 else ""))
        ms = sorted(e["mentions"], key=lambda m: (v.notes[m["path"]]["updated"], m["path"]), reverse=True)
        for m in ms[:8]:
            n = v.notes[m["path"]]
            print("  " + v.note_line(n, next((x for x in m["lines"] if x >= n["line"]), m["lines"][0])))
            shown.add(m["path"])
        if len(ms) > 8:
            print(f"  … +{len(ms) - 8}")
    if len(em) > 8:
        print(f"… +{len(em) - 8} entities: " + ", ".join(e["id"] for e in em[8:20]))
    rest = sorted((n for n in nm if n["path"] not in shown), key=lambda n: (n["updated"], n["path"]), reverse=True)
    if rest:
        print("notes")
        for n in rest[:30 if not terms else 12]:
            print("  " + v.note_line(n))
        if len(rest) > (30 if not terms else 12):
            print(f"  … +{len(rest) - (30 if not terms else 12)}")
    hits, listed = [], {x["path"] for x in rest} | shown
    if terms:
        for n in notes:
            if n["indexed"]:
                continue
            for i, ln in enumerate(read(root / n["path"]).split("\n"), 1):
                low = ln.lower()
                if all(t in low for t in terms) and not (n["path"] in listed and i == n["line"]):
                    hits.append(f"  {n['path']}:{i}  {ln.strip()[:140]}")
    if hits:
        print("unindexed")
        print("\n".join(hits[:12]) + (f"\n  … +{len(hits) - 12}" if len(hits) > 12 else ""))
    if not (em or rest or hits):
        print(f"no match for {q!r}" + (f" in {P}" if P else "") + " — try fewer terms, or grep memory/")


def tree(label, kids_of, root, depth):
    print(label)
    seen = {root}

    def rec(node, prefix, d):
        kids = kids_of(node)
        for i, (lab, lab_seen, child) in enumerate(kids):
            last = i == len(kids) - 1
            mark, ext = ("└─ ", "   ") if last else ("├─ ", "│  ")
            if child is not None and child in seen:
                print(prefix + mark + lab_seen)
                continue
            print(prefix + mark + lab)
            if child is not None:
                seen.add(child)
                if d < depth:
                    rec(child, prefix + ext, d + 1)
    rec(root, "", 1)


def trace(args, root):
    g, former = load(root)
    v, name = View(g), args.target
    rels = {fold(t) for t in args.rel.split(",")} if args.rel else None
    old2cur = {o: p for p, olds in former.items() for o in olds}
    path = None
    for c in (name, name + ".md"):
        path = path or (c if c in v.notes else old2cur.get(c))
    if not path:
        stems = [p for p, n in v.notes.items() if n["id"] == name] or \
                [p for o, p in old2cur.items() if posixpath.basename(o)[:-3] == name]
        path = sorted(stems)[0] if stems else None
    ent = v.efold.get(fold(name))
    if path and not args.entity:
        rootn = v.notes[path]

        def disp(p):
            return posixpath.basename(p) if posixpath.dirname(p) == posixpath.dirname(path) else p

        def lab(n):
            return f"{disp(n['path'])} · {n['kind']} · {mmdd(n['updated'])}"

        def kids(p):
            out = []
            if args.down:
                for e in v.down[p]:
                    if e["rel"] in ("from", "refs"):
                        n = v.notes[e["src"]]
                        out.append((f"← {e['rel']} {lab(n)}", f"← {e['rel']} {disp(n['path'])} (seen)", n["path"]))
                for s in v.notes[p]["superseded_by"]:
                    out.append((f"superseded by {lab(v.notes[s])}", "", None))
            else:
                for rk in ("from", "refs", "supersedes"):
                    for e in v.frm[p]:
                        if e["rel"] == rk:
                            n = v.notes[e["dst"]]
                            out.append((f"{rk} {lab(n)}", f"{rk} {disp(n['path'])} (seen)",
                                        None if rk == "supersedes" else n["path"]))
            return out
        tree(f"{path} · {rootn['kind']} · {mmdd(rootn['updated'])}", kids, path, args.depth)
        if ent:
            print(f"(also an entity: trace -e {ent}{' --down' if args.down else ''})")
        return
    if not ent:
        print(f"no note or entity named {name!r} — try memory.py where {name}")
        return
    def kids(c):
        out = []
        for r in sorted(v.in_r[c] if args.down else v.out_r[c], key=lambda r: (r["type"], fold(r["s"] + r["o"]))):
            if rels and r["type"] not in rels:
                continue
            other = r["s"] if args.down else r["o"]
            t = r["type"] + ("" if r["canon"] else "?")
            arrow = "←" if args.down else "→"
            ot = v.ents[other]["type"]
            out.append((f"{arrow} {t} {other} · {ot} · {r['evidence'][0]}", f"{arrow} {t} {other} · {ot} (seen)", other))
        return out
    tree(f"{ent} · {v.ents[ent]['type']}", kids, ent, args.depth)


def check(args, root):
    g, _ = load(root)
    by = defaultdict(list)
    for c in g["checks"]:
        by[c["code"]].append(c["msg"])
    if not by:
        print("check: no warnings")
    for code in sorted(by):
        print(f"{code} ×{len(by[code])}")
        for m in by[code]:
            print(f"  {m}")


def log(args, root):
    now = dt.datetime.now()
    f = root / "log" / f"{now.date().isoformat()}.md"
    f.parent.mkdir(parents=True, exist_ok=True)
    if not f.exists():
        f.write_text(f"# log {now.date().isoformat()}\n\n", encoding="utf-8")
    with f.open("a", encoding="utf-8") as fh:
        fh.write(f"- {now.strftime('%H:%M')} " + (f"[{args.p}] " if args.p else "") + args.text.strip() + "\n")
    print(f"{f.relative_to(root).as_posix()}: logged")


# ---------- ask: grep with memory ----------
# A thin layer on grep: the graph expands each question into grep patterns (aliases, ids), one grep -F
# pass finds the lines, and the graph orders the notes (current first, lineage) and heads them.

STOP = set("""a an and are as at be been being but by can could did do does doing done for from had has have
how i if in into is it its of on or our should so than that the their them then there these they this those
to us was were what when where which while who whom whose why will with would you your about any all also
each more most other some such only same too very just know known tell me give list show say said get make
made much many one we came come happened led lead ended end up""".split())
SYN = {"own": ["owner", "owned by", "maintain"], "owns": ["owner", "owned by", "maintain"],
       "depend": ["uses", "built on", "feeds", "reads"], "train": ["trained on", "fit on"],
       "defin": ["means", "definition"], "prefer": ["wants", "likes"]}
INTENT = {"current": re.compile(r"\b(current|currently|now|latest|today|still|valid|in force|production|live)\b", re.I),
          "down": re.compile(r"\b(came of|come of|became of|outcome|result\w*|happened|follow.?up)\b", re.I),
          "up": re.compile(r"\b(led to|lead to|what led|based on|rests? on|built on|evidence|came from|origin\w*)\b", re.I),
          "why": re.compile(r"\bwhy\b|\breason\b|\bcaused?\b", re.I),
          "dep": re.compile(r"\b(depend\w*|uses?|used by|feeds?|inputs?|downstream|trained on)\b", re.I)}
WORD = re.compile(r"[A-Za-z0-9@%$][A-Za-z0-9_.@%/+$-]*")


def stem(t):
    for suf in ("ings", "ing", "ies", "ed", "es", "s"):
        if t.isalpha() and t.endswith(suf) and len(t) - len(suf) >= 4:
            return t[:-len(suf)]
    return t


def qterms(q):
    """Question → {grep pattern: weight}: ids strong, numbers kept, words stemmed to prefixes, word pairs."""
    pats, words = {}, []
    for raw in WORD.findall(q):
        t = raw.lower().rstrip(".,;:?!)'\"").strip("-/")
        if len(t) < 2 or t in STOP:
            words.append(None)
            continue
        if re.fullmatch(r"[\d.,]+%?", t):
            pats[t] = max(pats.get(t, 0), 1.5)
        elif re.search(r"[._/@-]", t) or (re.search(r"\d", t) and re.search(r"[a-z]", t)):
            pats[t] = 3.0 if len(t) > 3 else 1.5
        elif len(t) >= 3:
            s = stem(t)
            pats[s] = max(pats.get(s, 0), 1.0)
            for x in SYN.get(s, []):
                pats.setdefault(x, 0.5)
        words.append(t)
    for a, b in zip(words, words[1:]):
        if a and b and a.isalpha() and b.isalpha():
            pats.setdefault(f"{a} {stem(b)}", 1.5)
    return pats


def boundary(p):
    return re.compile(r"(?<![a-z0-9])" + re.escape(p))


def grep_lines(root, pats):
    """One `grep -F` pass over the notes for every pattern → {path: [(line, text)]}. Python if grep is missing."""
    hits = defaultdict(list)
    if not pats:
        return hits
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".pat", delete=False, encoding="utf-8") as f:
        f.write("\n".join(sorted(pats)) + "\n")
    out = None
    try:
        r = subprocess.run(["grep", "-rniIF", "--include=*.md", "--exclude-dir=_dream", "-f", f.name, str(root)],
                           capture_output=True, text=True, errors="replace")
        out = r.stdout if r.returncode in (0, 1) else None
    except OSError:
        pass
    finally:
        os.unlink(f.name)
    if out is None:
        for p in root.rglob("*.md"):
            rel = p.relative_to(root).as_posix()
            if rel.startswith("_dream/"):
                continue
            for i, ln in enumerate(read(p).split("\n"), 1):
                if any(x in ln.lower() for x in pats):
                    hits[rel].append((i, ln))
        return hits
    for ln in out.splitlines():
        m = re.match(r"(.*?):(\d+):(.*)$", ln)
        if m:
            rel = Path(m.group(1)).resolve().relative_to(root).as_posix()
            if posixpath.basename(rel) not in SKIP:
                hits[rel].append((int(m.group(2)), m.group(3)))
    return hits


def ask(args, root):
    g, _ = load(root)
    v = View(g)
    qs = [q.strip() for q in (args.questions or []) for q in q.split("\n") if q.strip()]
    if args.file:
        qs += [q.strip() for q in read(Path(args.file)).split("\n") if q.strip()]
    if not qs:
        print("ask: give one or more questions")
        return
    names = defaultdict(set)  # folded name → entity ids, for alias expansion
    for e in g["entities"]:
        for x in [e["id"], *e["aka"], *(n["name"] for n in e["names"])]:
            if len(x) >= 3:
                names[fold(x)].add(e["id"])
    stems = defaultdict(list)
    for p, n in v.notes.items():
        stems[n["id"].lower()].append(p)
    folders = {p.split("/")[0].lower() for p in v.notes if "/" in p}
    per_q = []
    for q in qs:
        pats = qterms(q)
        intent = {k for k, rx in INTENT.items() if rx.search(q)}
        low = " " + q.lower() + " "
        hit_ents = {i for t in pats if fold(t) in names and len(names[fold(t)]) <= 2 for i in names[fold(t)]}
        hit_ents |= {i for nm, ids in names.items() if " " in nm.replace("-", " ") and len(ids) <= 2
                     and f" {nm.replace('-', ' ')} " in low.replace("-", " ") for i in ids}
        for eid in hit_ents:
            e = v.ents[eid]
            for x in [e["id"], *e["aka"], *(n["name"] for n in e["names"][:4])]:
                if len(x) >= 3 and len(names.get(fold(x), ())) <= 3:
                    pats.setdefault(x.lower(), 2.0)
        scope = {args.p.lower()} if args.p else {t for t in pats if t in folders}  # "in the aml-alerts project"
        named = {p for t in pats for p in stems.get(t, [])} | \
                {p for t in pats for p in ([t] if t in v.notes else [t + ".md"] if t + ".md" in v.notes else [])}
        if scope:
            named = {p for p in named if p.split("/")[0].lower() in scope}
        paths = {p: [t for t in pats if len(t) >= 4 and t not in scope and t in p.lower()] for p in v.notes
                 if not scope or p.split("/")[0].lower() in scope}
        per_q.append({"q": q, "pats": {t: w for t, w in pats.items() if t not in scope}, "intent": intent,
                      "ents": hit_ents, "named": named, "scope": scope, "paths": {p: ts for p, ts in paths.items() if ts}})
    allpats = {p for x in per_q for p in x["pats"]}
    hits = grep_lines(root, allpats)
    if args.p:
        hits = {p: h for p, h in hits.items() if p.split("/")[0] == args.p}
    rx = {p: boundary(p) for p in allpats}
    line_pats = {}  # (path, line) → patterns that really match there (word start)
    df = Counter()
    for path, rows in hits.items():
        seen = set()
        for no, text in rows:
            lowt = text.lower()
            ms = {p for p in allpats if p in lowt and rx[p].search(lowt)}
            if ms:
                line_pats[(path, no)] = (ms, text)
                seen |= ms
        df.update(seen)
    N = max(len(v.notes), 1)
    idf = {p: math.log(1 + N / df[p]) for p in df}
    by_file = defaultdict(list)
    for (path, no), (ms, text) in line_pats.items():
        by_file[path].append((no, ms, text))
    budget = args.budget or 900 * len(qs) + 1500
    for x in per_q:
        x["ranked"] = rank(x, by_file, idf, v)
    printed, out = {}, []

    def header(path):
        n = v.notes.get(path)
        if not n:
            return f"▸ {path}"
        s = f"▸ {path} · {n['kind']} · {n['updated']}"
        f = [v.notes[e["dst"]]["id"] for e in v.frm[path] if e["rel"] == "from"]
        sup = [v.notes[e["dst"]]["id"] for e in v.frm[path] if e["rel"] == "supersedes"]
        s += f" · from {', '.join(f)}" if f else ""
        s += f" · supersedes {', '.join(sup)}" if sup else ""
        s += (" · SUPERSEDED → " + ", ".join(v.notes[p]["id"] for p in n["superseded_by"])) if n["superseded_by"] else ""
        return s

    def body(path):
        """Compact note: title and body lines, no frontmatter, no blanks."""
        ls, n = read(root / path).split("\n"), v.notes.get(path, {})
        start = (n.get("line") or 1) - 1
        return [(i + 1, ln) for i, ln in enumerate(ls) if i >= start and ln.strip()]

    picked = {p for x in per_q for p, _ in x["ranked"]}
    full = sum(sum(len(t) + 6 for _, t in body(p)) for p in picked) <= budget
    for x in per_q:
        out.append(f"## {x['q']}")
        for eid in sorted(x["ents"])[:2] if "dep" in x["intent"] else []:
            out.append(entity_line(v, eid))
        for path, lines in x["ranked"]:
            want = body(path) if full else lines
            new = [(no, t) for no, t in want if no not in printed.get(path, set())]
            if path in printed and not new:
                out.append(header(path).split(" · ")[0] + " (above)")
                continue
            out.append(header(path) if path not in printed else header(path).split(" · ")[0] + " (more)")
            for no, t in new:
                out.append(f"  {t.strip()}" if full else f"  {no}: {t.strip()[:220]}")
            printed.setdefault(path, set()).update(no for no, _ in new)
        if not x["ranked"]:
            out.append("  (no match — try other words, or grep memory/)")
    print("\n".join(out))


def rank(x, by_file, idf, v):
    """Score notes by the patterns they contain (idf-weighted, title lines count double), then apply the
    graph: named notes first, successors of superseded notes, children for lineage, parents for why.
    Greedy pick that discounts patterns already covered. → [(path, [(line, text)])]"""
    pats, intent = x["pats"], x["intent"]
    base = {}
    for path, rows in by_file.items():
        n = v.notes.get(path)
        tl = n["line"] if n else 0
        got = Counter()
        for no, ms, _ in rows:
            for p in ms:
                if p in pats:
                    got[p] += 2 if no == tl else 1
        if got:
            base[path] = got
    score = {p: sum(pats[t] * idf[t] * (1 + math.log(c)) for t, c in got.items()) for p, got in base.items()}
    for p, ts in x["paths"].items():  # the slug names the thing: count it like a title hit
        score[p] = score.get(p, 0) + sum(pats.get(t, 1) * idf.get(t, 1) for t in ts)
    if x["scope"]:
        score = {p: s_ for p, s_ in score.items() if p.split("/")[0].lower() in x["scope"]}
    top = max(score.values(), default=0) or 1.0
    for p in x["named"]:
        score[p] = score.get(p, 0) + top + 1
    for eid in x["ents"]:  # notes that mention a matched entity, findings and decisions first
        for m in v.ents[eid]["mentions"]:
            n = v.notes.get(m["path"])
            score[m["path"]] = score.get(m["path"], 0) + 0.35 * top * (1.5 if n and n["kind"] in ("finding", "decision") else 1)
    up = intent & {"up", "why", "dep"}
    seeds = sorted(score.items(), key=lambda z: -z[1])[:6]
    best_live = next((p for p, _ in seeds if v.notes.get(p) and not v.notes[p]["superseded_by"]), None)
    for p, s in seeds:
        n = v.notes.get(p)
        if not n:
            continue
        for succ in n["superseded_by"]:
            score[succ] = max(score.get(succ, 0), s * (1.1 if "current" in intent else 0.85))
        if "current" in intent and n["superseded_by"]:
            score[p] = s * 0.6
        if "down" in intent or (p in x["named"] and not up and len(x["named"]) == 1) or \
                ("current" in intent and p == best_live):
            for e in v.down[p]:
                if e["rel"] in ("from", "refs"):
                    score[e["src"]] = max(score.get(e["src"], 0), s * (0.7 if "down" in intent else 0.5))
        if up:  # ancestors, two hops
            frontier = [(p, s)]
            for _ in range(2):
                nxt = []
                for q_, sq in frontier:
                    for e in v.frm[q_]:
                        if e["rel"] in ("from", "refs"):
                            w = sq * 0.6
                            score[e["dst"]] = max(score.get(e["dst"], 0), w)
                            nxt.append((e["dst"], w))
                frontier = nxt
    ranked = sorted(score.items(), key=lambda z: (-z[1], z[0]))
    picks = [(p, sc) for p, sc in ranked[:8] if sc >= 0.2 * ranked[0][1]] if ranked else []
    if os.environ.get("MEMORY_DEBUG"):
        sys.stderr.write(f"Q {x['q']} intent={sorted(intent)} named={sorted(x['named'])}\n  pats={pats}\n")
        for p, s in sorted(score.items(), key=lambda z: -z[1])[:12]:
            sys.stderr.write(f"  {s:7.2f} {p}{' PICK' if p in dict(picks) else ''}\n")
    res = []
    for k, (p, _) in enumerate(picks):
        n = v.notes.get(p)
        rows = sorted((r for r in by_file.get(p, []) if not n or r[0] >= n["line"]),  # body lines; the header has the lineage
                      key=lambda r: -sum(pats.get(t, 0) * idf.get(t, 0) for t in r[1]))
        keep = rows[:4 if k < 2 else 2]
        lines = {(no, t) for no, _, t in keep}
        if n and n["line"]:
            lines.add((n["line"], "# " + n["title"]))
        res.append((p, sorted(lines)))
    return res


def entity_line(v, eid):
    e = v.ents[eid]
    parts = []
    for arrow, rs, end in (("←", v.in_r[eid], "s"), ("→", v.out_r[eid], "o")):
        grp = defaultdict(list)
        for r in rs:
            if r["canon"]:
                grp[r["type"]].append(r[end])
        parts += [f"{arrow} {t}: {', '.join(sorted(set(xs))[:8])}" for t, xs in sorted(grp.items())]
    return f"= {eid} ({e['type']}" + (f"; aka {', '.join(e['aka'][:3])}" if e["aka"] else "") + ") " + " · ".join(parts[:6])


def grepv(args, root):
    """Plain grep over the notes, grouped by note and headed with kind · date · lineage · superseded → successor."""
    g, _ = load(root)
    v = View(g)
    r = subprocess.run(["grep", "-rnI", "--include=*.md", "--exclude-dir=_dream", *args.grep_args, str(root)],
                       capture_output=True, text=True, errors="replace")
    groups = defaultdict(list)
    for ln in r.stdout.splitlines():
        m = re.match(r"(.*?):(\d+):(.*)$", ln)
        if m:
            rel = Path(m.group(1)).resolve().relative_to(root).as_posix()
            if posixpath.basename(rel) not in SKIP:
                groups[rel].append(f"  {m.group(2)}: {m.group(3).strip()[:220]}")
    if not groups:
        print(r.stderr.strip() or "no match")
    for rel in sorted(groups, key=lambda p: v.notes.get(p, {}).get("updated", ""), reverse=True):
        n = v.notes.get(rel)
        h = f"▸ {rel}" + (f" · {n['kind']} · {n['updated']}" if n else "")
        if n and n["superseded_by"]:
            h += " · SUPERSEDED → " + ", ".join(v.notes[p]["id"] for p in n["superseded_by"])
        print(h + "\n" + "\n".join(groups[rel]))


def main(argv=None):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--root", help="memory dir (default: $MEMORY_DIR, nearest memory/ upward, ./memory)")
    ap = argparse.ArgumentParser(prog="memory.py", description="memory-dream v0.4")
    ap.add_argument("--root", dest="root0", help=argparse.SUPPRESS)
    sp = ap.add_subparsers(dest="verb", required=True)
    d = sp.add_parser("dream", parents=[common], help="index new notes, review vocabularies, merge")
    d.add_argument("--cmd", help='model command, prompt on stdin (default $MEMORY_LLM; none = file mode)')
    d.add_argument("-j", type=int, default=4, help="parallel calls")
    d.add_argument("--gists", action="store_true")
    d.add_argument("--review", action="store_true")
    d.add_argument("--all", action="store_true", help="re-index every note")
    w = sp.add_parser("where", parents=[common], help="pointers, headlines and relations")
    w.add_argument("terms", nargs="*")
    w.add_argument("-p", help="project")
    t = sp.add_parser("trace", parents=[common], help="lineage of a note, or relations of an entity")
    t.add_argument("target")
    ud = t.add_mutually_exclusive_group()
    ud.add_argument("--up", action="store_true")
    ud.add_argument("--down", action="store_true")
    t.add_argument("--rel", help="relation types, comma-separated")
    t.add_argument("--depth", type=int, default=3)
    t.add_argument("-e", "--entity", action="store_true", help="walk the entity even if a note has this name")
    sp.add_parser("check", parents=[common], help="warnings in full")
    lg = sp.add_parser("log", parents=[common], help="append to today's log")
    lg.add_argument("text")
    lg.add_argument("-p", help="project")
    a = sp.add_parser("ask", parents=[common], help="answer questions: grep with memory, one call for many questions")
    a.add_argument("questions", nargs="*")
    a.add_argument("-f", "--file", help="questions, one per line")
    a.add_argument("-p", help="project")
    a.add_argument("--budget", type=int, help="chars before switching from whole notes to surgical lines")
    gr = sp.add_parser("grep", parents=[common], help="grep the notes; hits grouped by note with lineage headers")
    gr.add_argument("grep_args", nargs=argparse.REMAINDER)
    args = ap.parse_args(argv)
    root = find_root(args.root or args.root0)
    {"dream": dream, "where": where, "trace": trace, "check": check, "log": log, "ask": ask,
     "grep": grepv}[args.verb](args, root)


if __name__ == "__main__":
    main()
