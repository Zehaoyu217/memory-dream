#!/usr/bin/env python3
"""memory-dream v0.4: notes are the truth; answering is grep plus a thin layer of lineage and names.

  memory.py ask "q1" "q2" ... [-p P]     grep with memory: every question in one call
  memory.py dream [--cmd C] [-j N] [--review] [--all]   index entities and relations (optional), write the viewer
  memory.py viz [--out F]                 the HTML viewer: overview, explorer, health
  memory.py check                         warnings in full
  memory.py log "text" [-p P]             append to today's log

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
KINDS = set("question experiment finding decision dataset feature model metric term preference rule log note".split())
TIMEOUT = int(os.environ.get("MEMORY_TIMEOUT", "300"))
KEEP_DAYS = 30
MIN_UNKNOWN_USES = 3  # an unknown relation type goes to review once it is used this often

EDGES_SEED = """# EDGES — relation types between entities, read "X <type> Y". Closed: only these types and their aliases
# (~ = read in reverse) are shown; other links the dreamer finds are kept aside in the cache and counted by
# `check`. Add a type or alias here by hand and they appear at the next merge (0 calls).
# Note-to-note links (from:, supersedes:, refs) are lineage, not relations.
mode: closed
- uses: X needs Y as an input (model uses feature; feature uses table) | aka: depends-on, consumes, built-on, built-from, derived-from, based-on, sourced-from, requires, reads, reads-from, joined-to, ~feeds, ~input-to, ~used-by, ~used-for, ~used-in
- produces: X creates or writes Y (job produces table; model produces scores) | aka: writes, writes-to, creates, outputs, generates, ~generated-by, ~produced-by, ~output-of
- part-of: X is a component of Y (column part-of table; feature part-of feature-set) | aka: member-of, column-of, subset-of, stored-in, ~contains, ~has, ~includes
- trained-on: model X was fit on dataset Y | aka: fit-on, fitted-on, trained-with
- evaluated-on: X was measured on dataset or segment Y | aka: tested-on, validated-on, measured-on, scored-on, backtested-on
- measured-by: X is judged by metric Y | aka: reports, reports-metric, has-metric, measures, measured-in, scored-by, optimizes, optimises, targets, ~metric-of
- replaces: X is the newer version of Y | aka: supersedes, retires, ~replaced-by, ~superseded-by
- owned-by: X is maintained or decided by person or team Y | aka: maintained-by, managed-by, run-by, approved-by, decided-by, set-by, signed-off-by, agreed-by, ~owns, ~maintains
drop: related-to, associated-with, about, mentions, relates-to, answers, answered-by, basis-for, evidence-for, led-to, leads-to, motivates, motivated-by, informs, follows, confirms, explains, supports, overturned-by, compared-to, compared-with, beats, outperforms, baseline-for, improves, causes, caused-by, affects, affected-by, excludes, excluded-from, removed-from, applies-to, applied-to, is-a, example-of
"""
ALIASES_HEAD = ("# ALIASES — entity ids that name the same thing; the first id on a line is canonical. "
                "Edit freely.\n")

EXTRACT = """Index this memory note for retrieval. Reply with JSON only:
{"kind": "question|experiment|finding|decision|dataset|feature|model|metric|term|preference|rule|log|note",
 "entities": [{"id": "...", "type": "dataset|feature|model|metric|segment|person|team|term|tool",
               "as": ["text copied verbatim from the note"]}],
 "relations": [{"s": "entity id", "type": "an EDGES type or alias", "o": "entity id",
                "quote": "short text copied verbatim from the note that states it"}],
 "refs": ["ids or paths of other notes the text explicitly points to"]}
Entities are things someone would look up across notes: tables, features, models, metrics, segments,
people, teams, defined terms. Not columns, files, notebooks, numbers, or note ids (those go in refs).
If an entity is in KNOWN, reuse its id. Otherwise id = its most specific name, lowercase, spaces to
hyphens; a table keeps its dots (cards.txn_daily).
Relations: only ones the note states, read "s <type> o". Use an EDGES type or one of its aliases
(aliases marked ~ read in reverse). If none fits but the note states a real link between two things,
name it in 1-3 words: it is kept aside, not shown, until the vocabulary covers it.
EDGES:
{edges}
KNOWN:
{known}
NOTE {path}:
{text}
"""
REVIEW = """You keep the vocabulary of a data-science memory.
RELATION TYPES, read "X <type> Y" (closed list):
{edges}
UNKNOWN TYPES the indexer used (uses; up to 3 examples "X — Y: quote"):
{proposals}
ENTITY PAIRS that may name the same thing (id, type, surface forms, one context line each):
{pairs}
Reply with JSON only:
{"types": {"<unknown>": "alias T" | "alias ~T" | "drop"},
 "entities": {"<a> / <b>": "same" | "different"}}
Map an unknown type to T only when it names the same link as T, as a synonym ("alias T") or read in
reverse ("alias ~T"). Drop it when it is a claim about an effect or a comparison (lifts, reduces,
improves, beats, predicts, inflates), a link between notes or decisions (answers, led-to, basis-for,
fixes), a request or a conversation (asked-by, raised-by), or anything else. When unsure, drop.
If unsure whether two entities are the same thing, answer different. Versions (v2, v3) are different.
"""


# ---------- small helpers ----------

def fold(s):
    """Identity key: case, spaces, `_`, `.` and `-` don't distinguish (cards.txn_daily = cards-txn-daily)."""
    return re.sub(r"[\s_.-]+", "-", str(s).strip().lower())


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


def ground(ans, text):
    """Keep only what the note supports: entities whose `as` text occurs in it, relations whose quote does."""
    dropped = {"entities": [], "relations": 0}
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
            rels.append({"s": kept[fold(s)]["id"], "type": t, "o": kept[fold(o)]["id"], "quote": q,
                         "line": line_at(text, m.start())})
        else:
            dropped["relations"] += 1
    kind = str(ans.get("kind") or "").strip().lower()
    return {"kind": kind if kind in KINDS else "note", "entities": ents,
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
        if re.match(r"mode\s*:", s, re.I):  # the vocabulary is closed; the line documents it
            continue
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
    """Review edits to the closed vocabulary: alias (t onto arg's aka) or drop (t onto the drop line)."""
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
    elif dk < 0:
        lines.append(f"drop: {t}")
    else:
        lines[dk] = lines[dk].rstrip() + ("" if lines[dk].rstrip().endswith(":") else ",") + " " + t
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

FILEISH = re.compile(r"\.(py|sql|ipynb|csv|parquet|json|md)$|notebook|^nb-|-script$")


def merge_entities(occ, alines, nots, homes=None):
    """Entity groups as one union-find: ALIASES lines, folded-id equality, the surface-form rule.
    An entity is kept when it has a home (a note whose slug is its id), is mentioned in >= 2 notes, or is
    named in ALIASES.md; files and notebooks are not entities (grep finds them)."""
    homes = homes or {}
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
        projects = Counter(p.split("/")[0] for p in mm)
        home = min((h for k in ks for h in homes.get(k, [])), default=None,
                   key=lambda h: (-projects[h.split("/")[0]], h))
        if FILEISH.search(fold(c)) or not (home or len(mm) >= 2 or led):
            continue
        ents[c] = {"id": c, "type": min(tc, key=lambda t: (-tc[t], t)), "home": home,
                   "aka": sorted({r for k in ks for r in raw[k]} - {c}),
                   "names": [{"name": a, "n": n} for a, n in sorted(names.items(), key=lambda z: (-z[1], z[0]))],
                   "headline": None, "mentions": [{"path": p, "lines": sorted(mm[p])} for p in sorted(mm)]}
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
            ha, hb = ents[a].get("home"), ents[b].get("home")
            if pair in out or (ha and hb and ha != hb) or decided(a, b, gkeys, nots):  # two home notes: two things
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
        stem_date = re.match(r"\d{4}-\d\d-\d\d$", posixpath.basename(rel)[:-3])  # log/YYYY-MM-DD.md
        up = up[:10] if re.match(r"\d{4}-\d\d-\d\d", up) else stem_date.group(0) if stem_date else \
            dt.date.fromtimestamp(cur[rel]["mtime"] / 1e9).isoformat()
        proj = rel.split("/")[0] if "/" in rel else ""
        notes[rel] = {"path": rel, "id": posixpath.basename(rel)[:-3], "project": proj, "title": title,
                      "line": tline,
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
    homes = defaultdict(list)  # a note whose slug is an entity's id is that entity's home
    for rel, n in notes.items():
        if n["project"] != "log":
            homes[fold(n["id"])].append(rel)
    ents, cmap, gkeys = merge_entities(occ, alines, nots, homes)
    rels, props = {}, {}
    for rel in notes:
        for r in (aux[rel]["x"] or {}).get("relations", []):
            s, o = cmap.get(fold(r["s"])), cmap.get(fold(r["o"]))
            t = fold(r["type"]).lstrip("~")
            if not s or not o or (t in drop and t not in alias):  # a listed type or alias wins over the drop line
                continue
            if t not in alias:  # closed vocabulary: unknown types are counted for review, not shown
                p = props.setdefault(t, {"type": t, "uses": 0, "examples": []})
                p["uses"] += 1
                if len(p["examples"]) < 3:
                    p["examples"].append(f"{s} — {o}: {r['quote']}")
                continue
            T, rev = alias[t]
            s, o = (o, s) if rev else (s, o)
            if s == o:
                continue
            rec = rels.setdefault((s, T, o), {"s": s, "type": T, "o": o, "evidence": []})
            ev = f"{rel}:{r['line']}"
            if ev not in rec["evidence"]:
                rec["evidence"].append(ev)
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
    seen = set(man.get("seen", []))
    pairs = candidates(ents, [c for c in ents if fold(c) not in seen], gkeys, nots)
    for a, b in man.get("queue", []):
        a, b = cmap.get(fold(a)), cmap.get(fold(b))
        if a and b and a != b and not decided(a, b, gkeys, nots):
            pairs.add(tuple(sorted((a, b), key=fold)))
    pairs = sorted(pairs, key=lambda p: (fold(p[0]), fold(p[1])))
    proposed = sorted((p for p in props.values() if p["uses"] >= MIN_UNKNOWN_USES), key=lambda p: (-p["uses"], p["type"]))
    rare = [p for p in props.values() if p["uses"] < MIN_UNKNOWN_USES]
    checks += [("C7", f"unknown relation type {p['type']} ×{p['uses']} awaits review") for p in proposed]
    if rare:
        checks.append(("C7", f"{len(rare)} rarer unknown relation types dropped ({sum(p['uses'] for p in rare)} relations)"))
    checks += [("C7", f"entities {a} / {b} await review") for a, b in pairs]
    return {"v": V, "built": now.strftime("%Y-%m-%dT%H:%M"),
            "notes": [notes[p] for p in sorted(notes)],
            "entities": [ents[c] for c in sorted(ents, key=fold)],
            "relations": sorted(rels.values(), key=lambda r: (fold(r["s"]), r["type"], fold(r["o"]))),
            "edges": edges, "proposed": proposed, "review": [{"a": a, "b": b} for a, b in pairs],
            "checks": [{"code": c, "msg": m} for c, m in sorted(checks, key=lambda z: z[0])]}


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


def known_lines(ents, project, local=80, shared=20):
    """KNOWN for a prompt: this project's entities, then the most-mentioned shared ones (small prompts)."""
    def inproj(e):
        return any(m["path"].split("/")[0] == project for m in e["mentions"])
    by_n = sorted(ents.values(), key=lambda e: (-len(e["mentions"]), fold(e["id"])))
    es = [e for e in by_n if inproj(e)][:local] + [e for e in by_n if not inproj(e)][:shared]
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

    homes = defaultdict(list)
    for rel in cur:
        if not rel.startswith("log/"):
            homes[fold(posixpath.basename(rel)[:-3])].append(rel)

    def entities_now():
        occ = [(rel, e) for rel in cur if cur[rel]["sha"][:12] in xs for e in xs[cur[rel]["sha"][:12]]["entities"]]
        return merge_entities(occ, alines, nots, homes)[0]

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
        rec = ground(ans, text)
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
            if not (k in by_sha or k == "review"):
                pp.unlink()

    def graph():
        e2, a2 = vocab_texts(root)
        return build(root, {**man, "failed": failed}, cur, former, e2, a2, xs=xs, now=now)

    g = graph()
    review = {"pairs": 0, "types": 0, "calls": 0, "aliases": 0, "mapped": 0}

    def apply_review(ans, props, pairs):
        e2, a2 = vocab_texts(root)
        types = parse_edges(e2)[0]
        mentions = {e["id"]: len(e["mentions"]) for e in g["entities"]}
        pmap = {fold(p["type"]): p for p in props}
        for t, v in (ans.get("types") or {}).items():  # closed vocabulary: map onto a listed type, or drop
            t, v = fold(t), str(v).strip().lower()
            tgt = v[5:].strip() if v.startswith("alias") else ""
            if t in pmap and tgt and fold(tgt.lstrip("~")) in types:
                e2 = edit_edges(e2, "alias", ("~" if tgt.startswith("~") else "") + t, fold(tgt.lstrip("~")))
                review["mapped"] += 1
            elif t in pmap and v == "drop":
                e2 = edit_edges(e2, "drop", t)
                review["mapped"] += 1
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
        props = g["proposed"][:40]
        pairs = [(r["a"], r["b"]) for r in g["review"]][:30]
        if not props and not pairs:
            return None, props, pairs
        ents = {e["id"]: e for e in g["entities"]}

        def ctx(e):
            m = e["mentions"][0]
            return read(root / m["path"]).split("\n")[m["lines"][0] - 1].strip()[:160]

        def desc(c):
            e = ents[c]
            return f"{c} ({e['type']}; " + "; ".join(f'"{n["name"]}"' for n in e["names"][:3]) + f") «{ctx(e)}»"
        pr = fill(REVIEW, edges="\n".join(parse_edges(vocab_texts(root)[0])[3]),
                  proposals="\n".join(f"- {p['type']}: uses {p['uses']}; "
                                      + "; ".join(f'"{x}"' for x in p["examples"]) for p in props) or "none",
                  pairs="\n".join(f"- {a} / {b}: {desc(a)} | {desc(b)}" for a, b in pairs) or "none")
        return pr, props, pairs

    due = args.review or g["proposed"] or g["review"]
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
        pr = review_prompt()[0] if (args.review or g["proposed"] or g["review"]) else None
        if pr:
            wr(pend / "review.prompt.md", pr)
        elif (pend / "review.prompt.md").exists():
            (pend / "review.prompt.md").unlink()

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
    write_viz(root, g, dd / "graph.html")
    old_index = root / "INDEX.md"  # earlier versions generated it; the viewer replaces it
    if old_index.exists() and read(old_index).startswith("# memory · "):
        old_index.unlink()
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
    out += f" · {review['mapped']} types mapped" if review["mapped"] else ""
    out += f" · {len(moved)} moved" if moved else ""
    out += f" · {len(deleted)} deleted" if deleted else ""
    out += f" · {pending if not cmd else sum(1 for n in g['notes'] if not n['indexed'])} pending"
    out += (" · " + " ".join(f"{c}×{n}" for c, n in sorted(codes.items()))) if codes else ""
    print(out)
    if pending:
        print(f"{pending} prompts listed in {pend / 'TODO.md'}: run the memory-dreamer subagent, "
              "then memory.py dream again")


# ---------- retrieval ----------

class View:
    def __init__(self, g):
        self.g = g
        self.notes = {n["path"]: n for n in g["notes"]}
        self.ents = {e["id"]: e for e in g["entities"]}
        self.out_r, self.in_r = defaultdict(list), defaultdict(list)
        for r in g["relations"]:
            self.out_r[r["s"]].append(r)
            self.in_r[r["o"]].append(r)
        self.frm, self.down = defaultdict(list), defaultdict(list)
        for e in g["edges"]:
            self.frm[e["src"]].append(e)
            self.down[e["dst"]].append(e)



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
        # the index only adds aliases of things the question names by id; loose names never become patterns
        by_id = {i for t in pats if fold(t) in names and len(names[fold(t)]) <= 2 for i in names[fold(t)]}
        hit_ents = by_id | {i for nm, ids in names.items() if 2 <= len(nm.replace("-", " ").split()) <= 3
                            and len(ids) <= 2 and f" {nm.replace('-', ' ')} " in low.replace("-", " ") for i in ids}
        for eid in hit_ents:
            e = v.ents[eid]
            for x in [e["id"], *e["aka"], *(n["name"] for n in e["names"][:4])]:
                if 3 <= len(x) <= 30 and len(x.split()) <= 3 and len(names.get(fold(x), ())) <= 2:
                    pats.setdefault(x.lower(), 1.5)
        scope = {args.p.lower()} if args.p else {t for t in pats if t in folders}  # "in the aml-alerts project"
        named = {p for t in pats for p in stems.get(t, [])} | \
                {p for t in pats for p in ([t] if t in v.notes else [t + ".md"] if t + ".md" in v.notes else [])}
        if scope:
            named = {p for p in named if p.split("/")[0].lower() in scope}
        paths = {p: [t for t in pats if len(t) >= 4 and t not in scope and t in p.lower()] for p in v.notes
                 if not scope or p.split("/")[0].lower() in scope}
        per_q.append({"q": q, "pats": {t: w for t, w in pats.items() if t not in scope}, "intent": intent,
                      "ents": hit_ents, "by_id": by_id, "named": named, "scope": scope, "paths": {p: ts for p, ts in paths.items() if ts}})
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
            w = 0.35 if eid in x["by_id"] else 0.15  # named outright: a stronger signal than a phrase match
            score[m["path"]] = score.get(m["path"], 0) + w * top * (1.5 if n and n["kind"] in ("finding", "decision") else 1)
    up = intent & {"up", "why", "dep"}
    seeds = sorted(score.items(), key=lambda z: -z[1])[:6]
    best_live = next((p for p, _ in seeds if v.notes.get(p) and not v.notes[p]["superseded_by"]), None)
    for p, s in seeds:
        n = v.notes.get(p)
        if not n:
            continue
        for succ in n["superseded_by"]:
            score[succ] = max(score.get(succ, 0), s * (1.1 if "current" in intent else 0.85))
            if "why" in intent:  # why it was replaced: what the successor built on
                for e in v.frm[succ]:
                    if e["rel"] in ("from", "refs") and e["dst"] != p:
                        score[e["dst"]] = max(score.get(e["dst"], 0), s * 0.6)
        if "current" in intent and n["superseded_by"]:
            score[p] = s * 0.85  # still shown (answers cite what was replaced), below its successor
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
            grp[r["type"]].append(r[end])
        parts += [f"{arrow} {t}: {', '.join(sorted(set(xs))[:8])}" for t, xs in sorted(grp.items())]
    return f"= {eid} ({e['type']}" + (f"; aka {', '.join(e['aka'][:3])}" if e["aka"] else "") + ") " + " · ".join(parts[:6])


def viz(args, root):
    """Write the HTML viewer (default memory/_dream/graph.html; `dream` refreshes it too)."""
    out = Path(args.out).expanduser() if args.out else root / "_dream" / "graph.html"
    g, _ = load(root)
    write_viz(root, g, out)
    print(f"{out}: {len(g['notes'])} notes, {len(g['entities'])} entities — open it in a browser")


def write_viz(root, g, out):
    """A self-contained HTML viewer of the graph: overview, explorer, health."""
    tpl = read(Path(__file__).resolve().parent.parent / "assets" / "viz.html")
    notes = []
    for n in g["notes"]:
        try:
            ls = read(root / n["path"]).split("\n")
        except OSError:
            ls = []
        notes.append({**n, "text": [x for x in ls[(n["line"] or 1) - 1:] if x.strip()][:14]})
    data = {"built": g["built"], "notes": notes, "entities": g["entities"], "relations": g["relations"],
            "edges": g["edges"], "checks": g["checks"], "review": g["review"], "proposed": g["proposed"]}
    island = "{\n" + ",\n".join(f'"{k}": ' + ("[\n" + ",\n".join(json.dumps(r, ensure_ascii=False) for r in v) + "\n]"
                                             if isinstance(v, list) else json.dumps(v)) for k, v in data.items()) + "\n}\n"
    a = tpl.index('id="data-graph"')
    a = tpl.index("\n", a) + 1
    wr(out, tpl[:a] + island.replace("</", "<\\/") + tpl[tpl.index("</script>", a):])


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
    d.add_argument("--review", action="store_true", help="review the vocabulary even if nothing is due")
    d.add_argument("--all", action="store_true", help="re-index every note")
    a = sp.add_parser("ask", parents=[common], help="answer questions: grep with memory, one call for many questions")
    a.add_argument("questions", nargs="*")
    a.add_argument("-f", "--file", help="questions, one per line")
    a.add_argument("-p", help="project")
    a.add_argument("--budget", type=int, help="chars before switching from whole notes to surgical lines")
    vz = sp.add_parser("viz", parents=[common], help="write the HTML viewer (dream refreshes it too)")
    vz.add_argument("--out", help="output file (default memory/_dream/graph.html)")
    sp.add_parser("check", parents=[common], help="warnings in full")
    lg = sp.add_parser("log", parents=[common], help="append to today's log")
    lg.add_argument("text")
    lg.add_argument("-p", help="project")
    args = ap.parse_args(argv)
    root = find_root(args.root or args.root0)
    {"dream": dream, "ask": ask, "viz": viz, "check": check, "log": log}[args.verb](args, root)


if __name__ == "__main__":
    main()
