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
import bisect
import datetime as dt
import difflib
import functools
import hashlib
import json
import math
import os
import posixpath
import re
import sqlite3
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
WIDE = int(os.environ.get("MEMORY_WIDE", "10000"))  # above this many notes, ask greps only where a question points
GENERAL = {"prefs", "reporting", "glossary", "corrections", "howto", "qa", "people", "log"}  # areas that span projects
WORK = {"question", "experiment", "finding", "decision", "dataset", "feature", "model", "metric"}  # project kinds

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

@functools.lru_cache(maxsize=1 << 20)
def _fold(s):
    return re.sub(r"[\s_.-]+", "-", s.strip().lower())


def fold(s):
    """Identity key: case, spaces, `_`, `.` and `-` don't distinguish (cards.txn_daily = cards-txn-daily)."""
    return _fold(s if isinstance(s, str) else str(s))


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
    for d, dirs, files in os.walk(root):
        dirs[:] = [x for x in dirs if not x.startswith(".") and not (d == str(root) and x == "_dream")]
        base = os.path.relpath(d, root).replace(os.sep, "/")
        for f in files:
            if not f.endswith(".md") or f in SKIP or f.startswith("."):
                continue
            rel = f if base == "." else f"{base}/{f}"
            st, o = os.stat(os.path.join(d, f)), old.get(rel)
            same = o and o.get("mtime") == st.st_mtime_ns and o.get("size") == st.st_size
            cur[rel] = {"sha": o["sha"] if same else hashlib.sha256((root / rel).read_bytes()).hexdigest(),
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


SLUG = re.compile(r"(?<![\w/-])([a-z][a-z0-9]*(?:-[a-z0-9]+)+)(?![\w-])")


def note_facts(text):
    """What the graph needs from a note's text: frontmatter lineage and dates, the `# ` line, links, body slugs."""
    fm, title, tline, links = parse_note(text)
    return {"fm": {k: fm[k] for k in ("from", "supersedes", "type", "updated") if k in fm}, "title": title,
            "line": tline, "links": links, "nul": "\x00" in text,  # binary-looking: C9
            "ids": sorted(set(SLUG.findall(text.lower().split("\n", tline)[-1]))) if tline else []}


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


def merge_entities(occ, alines, nots, homes=None, stats=None):
    """Entity groups as one union-find: ALIASES lines, folded-id equality, the surface-form rule.
    An entity is kept when it has a home (a note whose slug is its id), is mentioned in >= 2 notes, or is
    named in ALIASES.md; files and notebooks are not entities (grep finds them)."""
    homes, st = homes or {}, stats if stats is not None else Counter()
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
                        st["refused_" + ("not_line" if p in nots else "versions")] += 1
                        return
        par[rb] = ra
        mem[ra] |= mem.pop(rb)

    def roots():
        return len({find(k) for k in raw})

    raw, surf, typ = defaultdict(Counter), defaultdict(Counter), defaultdict(Counter)
    ment = defaultdict(lambda: defaultdict(set))
    for path, e in occ:
        k = fold(e["id"])
        raw[k][e["id"]] += 1
        typ[k][e["type"]] += 1
        for a in e["as"]:
            surf[k][a] += 1
        ment[k][path] |= set(e["lines"])
    st["mentions"], st["ids_as_written"], st["after_folding"] = len(occ), sum(len(v) for v in raw.values()), len(raw)
    lead = {}
    for li, ids in enumerate(alines):
        fs = [fold(i) for i in ids]
        explicit |= {frozenset((x, y)) for x in fs for y in fs if x != y}
        for f in fs:
            lead.setdefault(f, (li, ids[0]))
            join(fs[0], f, force=True)
    if stats is not None:  # counting groups costs a pass over every id
        st["after_aliases_md"] = roots()
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
    if stats is not None:
        st["after_surface_rule"] = roots()
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
        if FILEISH.search(fold(c)):
            st["dropped_file_like"] += 1
            continue
        if not (home or len(mm) >= 2 or led):
            st["dropped_one_note"] += 1
            continue
        st["kept_with_home" if home else "kept_in_2plus_notes" if len(mm) >= 2 else "kept_by_aliases_md"] += 1
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


def notes_part(root, man, cur, former, xs=None, facts=None):
    """The half of the graph that the vocabulary does not touch: notes, lineage edges, note warnings."""
    checks = []
    notes, aux, by_stem = {}, {}, defaultdict(list)
    for rel in sorted(cur):
        h = cur[rel]["sha"]
        f = facts[rel] if facts is not None and rel in facts else note_facts(read(root / rel))
        fm, title, tline, links = f["fm"], f["title"], f["line"], f["links"]
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
        aux[rel] = {"fm": fm, "links": links, "x": x, "mt": cur[rel]["mtime"], "ids": set(f["ids"])}
        by_stem[notes[rel]["id"]].append(rel)
        if not title:
            checks.append(("C6", f"{rel}: no '# ' line"))
        if f.get("nul"):
            checks.append(("C9", f"{rel}: contains NUL bytes (binary-looking); keep notes plain text"))
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
    return {"notes": notes, "aux": aux, "edges": edges, "checks": checks}


def build(root, man, cur, former, et, at, xs=None, now=None, facts=None, base=None):
    """The graph = union of current notes' cached subgraphs, renamed by EDGES.md and ALIASES.md. `base` reuses the
    note half (notes_part) when only the vocabulary changed."""
    now = now or dt.datetime.now()
    types, alias, drop, _, bad_e = parse_edges(et)
    alines, nots, bad_a = parse_aliases(at)
    checks = [("C8", f"EDGES.md:{i}: {s}") for i, s in bad_e] + [("C8", f"ALIASES.md:{i}: {s}") for i, s in bad_a]
    base = base or notes_part(root, man, cur, former, xs, facts)
    notes, aux, edges = base["notes"], base["aux"], base["edges"]
    checks += base["checks"]

    occ = [(rel, e) for rel in notes if aux[rel]["x"] for e in aux[rel]["x"].get("entities", [])]
    homes = defaultdict(list)  # a note whose slug is an entity's id is that entity's home
    for rel, n in notes.items():
        if n["project"] != "log":
            homes[fold(n["id"])].append(rel)
    dedup = Counter()
    ents, cmap, gkeys = merge_entities(occ, alines, nots, homes, dedup)
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
            "dedup": dict(dedup),
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
        g = rd(root / "_dream" / "graph.json") or read_index(root / "_dream")
        if g and g.get("v") == V:
            return g, former
    elif len(cur) > WIDE:  # rebuilding takes minutes here: patch the last graph for what changed since the dream
        g = rd(root / "_dream" / "graph.json") or read_index(root / "_dream")
        if g and g.get("v") == V:
            return patch(root, g, man, cur), former
    return build(root, man, cur, former, et, at), former


def fresh_note(root, rel, cur, stems):
    """A note changed since the last dream: its record and its from:/supersedes: edges, from its text alone."""
    fm, title, tline, _ = parse_note(read(root / rel))
    up = fm.get("updated", "")
    proj = rel.split("/")[0] if "/" in rel else ""
    n = {"path": rel, "id": posixpath.basename(rel)[:-3], "project": proj, "title": title, "line": tline,
         "kind": (fm.get("type") or ("log" if proj == "log" else "note")).lower(), "superseded_by": [],
         "updated": up[:10] if re.match(r"\d{4}-\d\d-\d\d", up) else
         dt.date.fromtimestamp(cur[rel]["mtime"] / 1e9).isoformat(), "sha": cur[rel]["sha"][:12], "indexed": False}
    edges = []
    for kind in ("from", "supersedes"):
        for v in fm_list(fm.get(kind)):
            c = stems.get(posixpath.basename(re.sub(r"^\[\[|\]\]$|\.md$", "", v.strip())), [])
            mine = [x for x in c if x.split("/")[0] == rel.split("/")[0]]
            if (mine or c) and sorted(mine or c)[0] != rel:
                edges.append({"src": rel, "dst": sorted(mine or c)[0], "rel": kind})
    return n, edges


def patch(root, g, man, cur):
    """The last dream's graph with changed and new notes re-read (title, kind, date, from:/supersedes:) and
    deleted ones gone. Their entities wait for the next dream; grep reads their text as usual."""
    old = {p: f["sha"] for p, f in man.get("files", {}).items()}
    notes = {n["path"]: n for n in g["notes"] if n["path"] in cur}
    changed = [p for p in cur if old.get(p) != cur[p]["sha"]]
    stems = defaultdict(list)
    for p in cur:
        stems[posixpath.basename(p)[:-3]].append(p)
    ch = set(changed)
    edges = [e for e in g["edges"] if e["src"] not in ch and e["src"] in notes and e["dst"] in notes]
    for rel in changed:
        notes[rel], es = fresh_note(root, rel, cur, stems)
        edges += es
    for n in notes.values():
        n["superseded_by"] = []
    for e in edges:
        if e["rel"] == "supersedes":
            notes[e["dst"]]["superseded_by"].append(e["src"])
    if len(notes) < len(g["notes"]):  # something was deleted
        for e in g["entities"]:
            e["mentions"] = [m for m in e["mentions"] if m["path"] in notes]
    return {**g, "notes": [notes[p] for p in sorted(notes)], "edges": edges}


# ---------- dream caches and the index ----------

def extraction_files(dd):
    """{sha12: mtime_ns} of the extraction files in _dream/notes/."""
    if not (dd / "notes").is_dir():
        return {}
    with os.scandir(dd / "notes") as it:
        return {e.name[:-5]: e.stat().st_mtime_ns for e in it if e.name.endswith(".json")}


class Store:
    """dream's caches in _dream/store.db: parsed note facts by path, extractions by content hash (the files in
    _dream/notes/ stay the source; a row is used only while its file's mtime matches)."""
    def __init__(self, dd):
        self.dd = dd
        self.db = sqlite3.connect(dd / "store.db")
        self.db.executescript("CREATE TABLE IF NOT EXISTS facts(path TEXT PRIMARY KEY, sha TEXT, rec TEXT);"
                              "CREATE TABLE IF NOT EXISTS x(sha TEXT PRIMARY KEY, mt INTEGER, rec TEXT);")

    def facts(self, root, cur):
        have = {p: (h, r) for p, h, r in self.db.execute("SELECT path, sha, rec FROM facts")}
        out, new = {}, []
        for rel, f in cur.items():
            h, r = have.get(rel, (None, None))
            rec = json.loads(r) if h == f["sha"] else None
            if rec is not None and "nul" in rec:  # rows written before the C9 field are re-read once
                out[rel] = rec
            else:
                out[rel] = note_facts(read(root / rel))
                new.append((rel, f["sha"], json.dumps(out[rel])))
        with self.db:
            self.db.executemany("INSERT OR REPLACE INTO facts VALUES (?,?,?)", new)
            self.db.executemany("DELETE FROM facts WHERE path=?", [(q,) for q in have if q not in cur])
        return out

    def extractions(self, shas):
        files = extraction_files(self.dd)
        have = {h: (mt, r) for h, mt, r in self.db.execute("SELECT sha, mt, rec FROM x")}
        xs, add = {}, []
        for h in shas:
            if h not in files:
                continue
            mt, r = have.get(h, (None, None))
            x = json.loads(r) if mt == files[h] else rd(self.dd / "notes" / f"{h}.json")
            if x:
                xs[h] = x
                if mt != files[h]:
                    add.append((h, files[h], json.dumps(x)))
        with self.db:
            self.db.executemany("INSERT OR REPLACE INTO x VALUES (?,?,?)", add)
            self.db.executemany("DELETE FROM x WHERE sha=?", [(h,) for h in have if h not in xs])
        return xs

    def put(self, h, x):
        with self.db:
            self.db.execute("INSERT OR REPLACE INTO x VALUES (?,?,?)",
                            (h, (self.dd / "notes" / f"{h}.json").stat().st_mtime_ns, json.dumps(x)))


def write_index(dd, g):
    """The graph as SQLite (_dream/index.db): `ask` on a big memory reads only the rows a question needs."""
    tmp = dd / "index.db.tmp"
    if tmp.exists():
        tmp.unlink()
    db = sqlite3.connect(tmp)
    db.executescript("""PRAGMA journal_mode=OFF; PRAGMA synchronous=OFF;
        CREATE TABLE meta(k TEXT PRIMARY KEY, v TEXT);
        CREATE TABLE notes(path TEXT PRIMARY KEY, id TEXT, area TEXT, title TEXT, line INT, kind TEXT, updated TEXT,
                           sha TEXT, indexed INT, sup TEXT);
        CREATE TABLE edges(src TEXT, dst TEXT, rel TEXT);
        CREATE TABLE ents(id TEXT PRIMARY KEY, type TEXT, home TEXT, headline TEXT, aka TEXT, names TEXT);
        CREATE TABLE ment(eid TEXT, path TEXT, lines TEXT);
        CREATE TABLE names(k TEXT, eid TEXT);
        CREATE TABLE rels(s TEXT, type TEXT, o TEXT, ev TEXT);
        CREATE TABLE checks(code TEXT, msg TEXT);""")
    with db:
        db.executemany("INSERT INTO meta VALUES (?,?)", [(k, json.dumps(g[k])) for k in ("v", "built", "proposed", "review", "dedup")])
        db.executemany("INSERT INTO notes VALUES (?,?,?,?,?,?,?,?,?,?)",
                       ((n["path"], n["id"], n["project"], n["title"], n["line"], n["kind"], n["updated"], n["sha"],
                         int(n["indexed"]), json.dumps(n["superseded_by"])) for n in g["notes"]))
        db.executemany("INSERT INTO edges VALUES (?,?,?)", ((e["src"], e["dst"], e["rel"]) for e in g["edges"]))
        db.executemany("INSERT INTO ents VALUES (?,?,?,?,?,?)", ((e["id"], e["type"], e["home"], e["headline"],
                                                                 json.dumps(e["aka"]), json.dumps(e["names"])) for e in g["entities"]))
        db.executemany("INSERT INTO ment VALUES (?,?,?)",
                       ((e["id"], m["path"], json.dumps(m["lines"])) for e in g["entities"] for m in e["mentions"]))
        db.executemany("INSERT INTO names VALUES (?,?)", ((k, e["id"]) for e in g["entities"] for k in
                                                          {fold(x) for x in [e["id"], *e["aka"], *(n["name"] for n in e["names"])] if len(x) >= 3}))
        db.executemany("INSERT INTO rels VALUES (?,?,?,?)", ((r["s"], r["type"], r["o"], json.dumps(r["evidence"])) for r in g["relations"]))
        db.executemany("INSERT INTO checks VALUES (?,?)", ((c["code"], c["msg"]) for c in g["checks"]))
    db.executescript("CREATE INDEX e_src ON edges(src); CREATE INDEX e_dst ON edges(dst); CREATE INDEX m_eid ON ment(eid);"
                     "CREATE INDEX n_k ON names(k); CREATE INDEX r_s ON rels(s); CREATE INDEX r_o ON rels(o);")
    db.close()
    tmp.replace(dd / "index.db")


def index_db(dd):
    p = dd / "index.db"
    return sqlite3.connect(f"file:{p}?mode=ro", uri=True) if p.exists() else None


def read_index(dd):
    """The whole graph back from index.db (check, viz and tests on big memories; ask reads rows instead)."""
    db = index_db(dd)
    if not db:
        return None
    meta = {k: json.loads(v) for k, v in db.execute("SELECT k, v FROM meta")}
    ment = defaultdict(list)
    for eid, p, ls in db.execute("SELECT eid, path, lines FROM ment ORDER BY rowid"):
        ment[eid].append({"path": p, "lines": json.loads(ls)})
    g = {**meta,
         "notes": [{"path": p, "id": i, "project": a, "title": t, "line": ln, "kind": k, "superseded_by": json.loads(sup),
                    "updated": u, "sha": h, "indexed": bool(x)}
                   for p, i, a, t, ln, k, u, h, x, sup in db.execute("SELECT * FROM notes ORDER BY rowid")],
         "entities": [{"id": i, "type": t, "home": h, "aka": json.loads(a), "names": json.loads(nm), "headline": hl,
                       "mentions": ment[i]} for i, t, h, hl, a, nm in db.execute("SELECT * FROM ents ORDER BY rowid")],
         "relations": [{"s": s_, "type": t, "o": o, "evidence": json.loads(ev)} for s_, t, o, ev in db.execute("SELECT * FROM rels ORDER BY rowid")],
         "edges": [{"src": a, "dst": b, "rel": r} for a, b, r in db.execute("SELECT * FROM edges ORDER BY rowid")],
         "checks": [{"code": c, "msg": m} for c, m in db.execute("SELECT * FROM checks ORDER BY rowid")]}
    db.close()
    return g


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


class Known:
    """Entities by mention count and each project's top ones: one sort serves every prompt of a wave."""
    def __init__(self, ents, local=80):
        self.local = local
        self.by_n = sorted(ents.values(), key=lambda e: (-len(e["mentions"]), fold(e["id"])))
        self.projs = [{m["path"].split("/")[0] for m in e["mentions"]} for e in self.by_n]
        self.top = defaultdict(list)
        for i, ps in enumerate(self.projs):
            for p in ps:
                if len(self.top[p]) < local:
                    self.top[p].append(i)


def known_lines(ents, project, local=80, shared=20):
    """KNOWN for a prompt: this project's entities, then the most-mentioned shared ones (small prompts)."""
    kn = ents if isinstance(ents, Known) and ents.local >= local else Known(ents if isinstance(ents, dict) else
                                                                              {e["id"]: e for e in ents.by_n}, local)
    rest = []
    for i, ps in enumerate(kn.projs):
        if len(rest) >= shared:
            break
        if project not in ps:
            rest.append(i)
    es = [kn.by_n[i] for i in kn.top.get(project, [])[:local] + rest]
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
    if (not args.all and not args.review and man.get("v") == V and man.get("unindexed") == 0 and not man.get("due")
            and {p: f["sha"] for p, f in cur.items()} == {p: f["sha"] for p, f in man.get("files", {}).items()}
            and man.get("vsig") == vsig(*vocab_texts(root)) and (dd / "index.db").exists() and (dd / "graph.html").exists()
            and not any(pend.glob("*.json")) and {f["sha"][:12] + ".json" for f in cur.values()} <= set(os.listdir(dd / "notes"))):
        print(f"dream: {len(cur)} notes · 0 indexed (0 calls) · nothing new since {man.get('dreamed', '?')}")
        return
    failed, attempts = man.get("failed", {}), man.get("attempts", {})
    st = Counter()
    by_sha = {}
    for rel in sorted(cur):
        by_sha.setdefault(cur[rel]["sha"][:12], rel)
    store = Store(dd)
    facts = store.facts(root, cur)
    xs = store.extractions(by_sha)
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
        u = facts[rel]["fm"].get("updated", "")
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
        store.put(h, rec)
        xs[h] = rec
        failed.pop(h, None)
        attempts.pop(h, None)
        st["indexed"] += 1

    if cmd:  # command mode: waves of -j parallel calls, KNOWN refreshed between waves
        j = max(1, args.j)
        with ThreadPoolExecutor(j) as ex:
            ents = None
            for w in range(0, len(todo), j):
                if ents is None or len(cur) <= WIDE or w // j % 10 == 0:
                    ents = Known(entities_now())
                wave = todo[w:w + j]
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
        ents = Known(entities_now()) if any(h not in xs or args.all for h in todo) else None
        for h in todo:
            if h in xs and not args.all:
                continue
            wr(pend / f"{h}.prompt.md", prompt_for(h, ents))
        for pp in pend.glob("*.prompt.md"):  # stale prompts: note changed or gone
            k = pp.name[:-len(".prompt.md")]
            if not (k in by_sha or k == "review"):
                pp.unlink()

    base = {}

    def graph():  # after a review only the vocabulary changed: the note half is reused
        e2, a2 = vocab_texts(root)
        base.update(base or notes_part(root, {**man, "failed": failed}, cur, former, xs, facts))
        return build(root, {**man, "failed": failed}, cur, former, e2, a2, xs=xs, now=now, facts=facts, base=base)

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
    if len(cur) > WIDE:  # big: no 380 MB graph.json; an overview page and one page per area
        (dd / "graph.json").unlink() if (dd / "graph.json").exists() else None
        write_viz_big(root, g, dd)
    else:
        wr(dd / "graph.json", g)
        write_viz(root, g, dd / "graph.html")
    write_index(dd, g)
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
                              "dreamed": now.isoformat(timespec="seconds"),
                              "unindexed": sum(1 for n in g["notes"] if not n["indexed"]),
                              "due": bool(cmd and (g["proposed"] or g["review"]))})
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

class Lazy(dict):
    """A dict that fills a missing key from a function and keeps it."""
    def __init__(self, fn):
        super().__init__()
        self.fn = fn

    def __missing__(self, k):
        v = self[k] = self.fn(k)
        return v


class View:
    """The graph in memory, for ask on small memories."""
    def __init__(self, g):
        self.g = g
        self._names = None
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

    def name_map(self):
        if self._names is None:
            self._names = defaultdict(set)  # folded name → entity ids, for alias expansion
            for e in self.g["entities"]:
                for x in [e["id"], *e["aka"], *(n["name"] for n in e["names"])]:
                    if len(x) >= 3:
                        self._names[fold(x)].add(e["id"])
        return self._names

    def names_of(self, k):
        return self.name_map().get(k, set())

    def multi_names(self, low):
        """Entity names of 2-3 words that the question spells out."""
        lw = " " + low.replace("-", " ") + " "
        return [(nm, ids) for nm, ids in self.name_map().items()
                if 2 <= len(nm.replace("-", " ").split()) <= 3 and f" {nm.replace('-', ' ')} " in lw]


class DbView:
    """index.db for ask on big memories: every note's row, everything else read when a question needs it. Notes
    changed since the dream are read from their text (lineage now; entities at the next dream)."""
    def __init__(self, root, man, cur):
        db = self.db = index_db(root / "_dream")
        self.notes = {p: {"path": p, "id": i, "project": a, "title": t, "line": ln, "kind": k, "updated": u,
                          "superseded_by": json.loads(sup)}
                      for p, i, a, t, ln, k, u, sup in db.execute(
                          "SELECT path, id, area, title, line, kind, updated, sup FROM notes")}
        old = {p: f["sha"] for p, f in man.get("files", {}).items()}
        changed = {p for p in cur if old.get(p) != cur[p]["sha"]}
        gone = {p for p in self.notes if p not in cur}
        for p in gone:
            del self.notes[p]
        mine, added = {}, defaultdict(list)
        if changed:
            stems = defaultdict(list)
            for p in cur:
                stems[posixpath.basename(p)[:-3]].append(p)
            for rel in changed:
                self.notes[rel], mine[rel] = fresh_note(root, rel, cur, stems)
                for e in mine[rel]:
                    added[e["dst"]].append(e)
            for n in self.notes.values():
                if changed.intersection(n["superseded_by"]):
                    n["superseded_by"] = [x for x in n["superseded_by"] if x not in changed]
            for rel, es in mine.items():
                for e in es:
                    if e["rel"] == "supersedes" and e["dst"] in self.notes:
                        self.notes[e["dst"]]["superseded_by"].append(rel)
        skip = changed | gone
        E = lambda rows: [{"src": a, "dst": b, "rel": r} for a, b, r in rows]  # noqa: E731
        self.frm = Lazy(lambda p: mine[p] if p in mine else [e for e in E(db.execute(
            "SELECT src, dst, rel FROM edges WHERE src=?", (p,))) if e["dst"] in self.notes and p not in skip])
        self.down = Lazy(lambda p: [e for e in E(db.execute("SELECT src, dst, rel FROM edges WHERE dst=?", (p,)))
                                    if e["src"] not in skip] + added[p])
        R = lambda rows: [{"s": a, "type": t, "o": b, "evidence": json.loads(ev)} for a, t, b, ev in rows]  # noqa: E731
        self.out_r = Lazy(lambda i: R(db.execute("SELECT s, type, o, ev FROM rels WHERE s=?", (i,))))
        self.in_r = Lazy(lambda i: R(db.execute("SELECT s, type, o, ev FROM rels WHERE o=?", (i,))))
        self.ents = Lazy(self._ent)
        self._names = Lazy(lambda k: {i for (i,) in db.execute("SELECT eid FROM names WHERE k=?", (k,))})

    def _ent(self, i):
        row = self.db.execute("SELECT id, type, home, headline, aka, names FROM ents WHERE id=?", (i,)).fetchone()
        if not row:
            raise KeyError(i)
        ms = [{"path": p, "lines": json.loads(ls)} for p, ls in self.db.execute("SELECT path, lines FROM ment WHERE eid=?", (i,))
              if p in self.notes]
        return {"id": row[0], "type": row[1], "home": row[2], "headline": row[3], "aka": json.loads(row[4]),
                "names": json.loads(row[5]), "mentions": ms}

    def names_of(self, k):
        return self._names[k]

    def multi_names(self, low):
        ws, out = low.replace("-", " ").split(), []
        for n in (2, 3):
            for i in range(len(ws) - n + 1):
                k = fold(" ".join(ws[i:i + n]))
                if self._names[k]:
                    out.append((k, self._names[k]))
        return out


def open_view(root):
    """What ask reads: the graph in memory for small memories, index.db rows on demand for big ones."""
    man = rd(root / "_dream" / "manifest.json", {}) or {}
    if len(man.get("files", {})) > WIDE and (root / "_dream" / "index.db").exists():
        cur = scan(root, man)[0]
        if len(cur) > WIDE:
            return DbView(root, man, cur)
    return View(load(root)[0])



def check(args, root):
    g, _ = load(root)
    d = g.get("dedup") or {}
    if d:
        print(f"dedup: {d.get('mentions', 0)} entity mentions · {d.get('ids_as_written', 0)} ids as written → "
              f"{d.get('after_folding', 0)} after folding → {d.get('after_aliases_md', 0)} after ALIASES.md → "
              f"{d.get('after_surface_rule', 0)} after the surface rule · kept {len(g['entities'])} "
              f"({d.get('kept_with_home', 0)} with a home note, {d.get('kept_in_2plus_notes', 0)} in 2+ notes, "
              f"{d.get('kept_by_aliases_md', 0)} by ALIASES.md) · dropped {d.get('dropped_one_note', 0)} one-note, "
              f"{d.get('dropped_file_like', 0)} file-like · refused {d.get('refused_versions', 0)} version merges, "
              f"{d.get('refused_not_line', 0)} by not: lines")
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
          "dep": re.compile(r"\b(depend\w*|uses?|used by|feeds?|inputs?|downstream|trained on)\b", re.I),
          # a task, not a question: someone's taste and the house rules should shape what gets made
          "task": re.compile(r"^\s*(please\s+)?(make|build|draft|write|prepare|create|put together|set up|design|plot|"
                             r"format|produce|update|add|summari[sz]e|sketch|lay out|turn)\b|\bhow (should|do|would|can) "
                             r"(i|we) (present|show|report|format|chart|plot|write|name|round|label|lay out|display)\b", re.I)}
ART = re.compile(r"\b(chart|plot|graph|table|deck|slide|email|notebook|query|sql|model card|alert|report|page|dashboard|"
                 r"memo|summary|readout|title|label|column|axis|axes|colou?r)s?\b", re.I)
WORD = re.compile(r"[A-Za-z0-9@%$][A-Za-z0-9_.@%/+$-]*")
# Read-path constants, each with the measurement that set it (.specs/memory-dream/REVIEW.md F1, F4, F7).
COMPLETE_MAX_NOTES = 200  # only this small a memory is considered for printing whole (reading every note is cheap)
COMPLETE_RATIO = 1.2  # print the whole memory when it costs <= this x the surgical output; then nothing is missed
WEAK_SHARE = 0.5  # weak match: a question word found nowhere, and the best note covers <= this share of the words
TASTE_MAX, TASTE_FLOOR = 12, 0.15  # taste notes printed (were 6, 0.25): house-rule recall 0.39 -> 0.42, +25% chars


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
            if "-" in t and not re.search(r"\d", t):  # a hyphenated phrase ("call-routing") also searches as its words
                for part in t.split("-"):  # bank: gold 0.888 -> 0.894, numbers 0.969 -> 0.976, +4% chars
                    if len(part) >= 3 and part not in STOP:
                        pats.setdefault(stem(part), 1.0)
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


def grep_lines(root, pats, areas=None):
    """One `grep -F` pass over the notes (or only these top-level areas) for every pattern → {path: [(line, text)]}.
    Python if grep is missing."""
    hits = defaultdict(list)
    where = [str(root)] if areas is None else [str(root / a) for a in areas if a and (root / a).is_dir()]
    if not pats or not where:
        return hits
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".pat", delete=False, encoding="utf-8") as f:
        f.write("\n".join(sorted(pats)) + "\n")
    out = None
    try:
        r = subprocess.run(["grep", "-rniaF", "--include=*.md", "--exclude-dir=_dream", "-f", f.name, *where],  # -a: a NUL byte must not hide a note
                           capture_output=True, text=True, errors="replace")
        out = r.stdout if r.returncode in (0, 1) else None
    except OSError:
        pass
    finally:
        os.unlink(f.name)
    if out is None:
        for p in (q for w in where for q in Path(w).rglob("*.md")):
            rel = p.relative_to(root).as_posix()
            if rel.startswith("_dream/"):
                continue
            for i, ln in enumerate(read(p).split("\n"), 1):
                if any(x in ln.lower() for x in pats):
                    hits[rel].append((i, ln))
        return hits
    pre = str(root).rstrip("/") + "/"
    for ln in out.splitlines():
        m = re.match(r"(.*?):(\d+):(.*)$", ln)
        if m:
            rel = m.group(1)[len(pre):] if m.group(1).startswith(pre) else Path(m.group(1)).resolve().relative_to(root).as_posix()
            if posixpath.basename(rel) not in SKIP:
                hits[rel].append((int(m.group(2)), m.group(3)))
    return hits


def catalog(v):
    """Every note's id and `# ` line in one lowercase string, for routing questions to areas."""
    paths = sorted(v.notes)
    lines = [(v.notes[p]["id"] + " " + (v.notes[p]["title"] or "")).lower().replace("\n", " ") for p in paths]
    starts, k = [], 0
    for ln in lines:
        starts.append(k)
        k += len(ln) + 1
    return paths, "\n".join(lines), starts


def route(pats, cat):
    """Areas whose note ids and titles match the question best (idf-weighted, each pattern once per area).
    → (areas, hint): at most 8 areas; a hint when many match about equally."""
    paths, text, starts = cat
    score = Counter()
    for t, w in pats.items():
        if len(t) < 3 or text.count(t) > max(50, len(paths) // 50):  # too common to say where to look
            continue
        hit, i = set(), text.find(t)
        while i >= 0:
            k = bisect.bisect_right(starts, i) - 1
            if i == 0 or not text[i - 1].isalnum():
                hit.add(k)
            i = text.find(t, i + 1)
        idf = math.log(1 + len(paths) / max(1, len(hit)))
        for a in {paths[k].split("/")[0] if "/" in paths[k] else "" for k in hit}:
            score[a] += w * idf
    if not score:
        return None, ""
    best = max(score.values())
    near = [a for a, s_ in score.most_common() if s_ >= 0.9 * best]
    hint = f"{len(near)} areas match about equally ({', '.join(sorted(near)[:4])}, …): name the project" if len(near) > 8 else ""
    return [a for a, s_ in score.most_common(8) if s_ >= 0.6 * best], hint


def ask(args, root):
    v = open_view(root)
    qs = [q.strip() for q in (args.questions or []) for q in q.split("\n") if q.strip()]
    if args.file:
        qs += [q.strip() for q in read(Path(args.file)).split("\n") if q.strip()]
    if not qs:
        print("ask: give one or more questions")
        return
    stems = defaultdict(list)
    for p, n in v.notes.items():
        stems[n["id"].lower()].append(p)
    folders = {p.split("/")[0].lower() for p in v.notes if "/" in p}
    big, by_area, cat = len(v.notes) > WIDE, defaultdict(list), None
    for p in v.notes:
        by_area[p.split("/")[0] if "/" in p else ""].append(p)
    general = {a for a, ps in by_area.items() if a.lower() in GENERAL or  # by name, or mostly not project work
               sum(v.notes[p]["kind"] in WORK for p in ps) < 0.8 * len(ps)}
    taste_pool = {p for a in general for p in by_area[a]}
    per_q = []
    for q in qs:
        pats = qterms(q)
        own = list(pats)
        raw = {t.lower().rstrip(".,;:?!)'\"").strip("-/") for t in WORD.findall(q)}  # unstemmed: folder names
        intent = {k for k, rx in INTENT.items() if rx.search(q)}
        low = " " + q.lower() + " "
        # the index only adds aliases of things the question names by id; loose names never become patterns
        by_id = {i for t in pats if 0 < len(v.names_of(fold(t))) <= 2 for i in v.names_of(fold(t))}
        hit_ents = by_id | {i for nm, ids in v.multi_names(low) if len(ids) <= 2 for i in ids}
        for eid in hit_ents:
            e = v.ents[eid]
            for x in [e["id"], *e["aka"], *(n["name"] for n in e["names"][:4])]:
                if 3 <= len(x) <= 30 and len(x.split()) <= 3 and len(v.names_of(fold(x))) <= 2:
                    pats.setdefault(x.lower(), 1.5)
        # "in the aml-alerts project": matched on the question's own words, since the stemmer turns pricing into pric;
        # general areas are not scopes by word ("… in reporting" asks about reporting, -p reporting scopes to it)
        scope = {args.p.lower()} if args.p else {t for t in raw | set(pats) if t in folders and t not in GENERAL}
        scoped_pats = scope | {stem(s) for s in scope} | \
            {stem(p) for s in scope for p in s.split("-") if len(p) >= 3}  # the folder's name is a scope, not a pattern
        named = {p for t in pats for p in stems.get(t, [])} | \
                {p for t in pats for p in ([t] if t in v.notes else [t + ".md"] if t + ".md" in v.notes else [])}
        if scope:
            named = {p for p in named if p.split("/")[0].lower() in scope}
        areas, hint = None, ""  # None: grep everything (memories up to WIDE notes)
        if big:
            areas = sorted({a for a in by_area if a.lower() in scope}) if scope else None
            if not scope:  # where to look: titles that match, notes it names, areas that mention the ids it names
                cat = cat or catalog(v)
                areas, hint = route(pats, cat)
                ids = [t for t in own if len(t) >= 4 and re.search(r"[0-9._@-]", t)]
                named = {p for p in named if len(stems.get(v.notes[p]["id"].lower(), ())) <= 3}  # a name used everywhere names nothing
                near = {p.split("/")[0] for p in named if "/" in p}
                for t in ids:  # each id points at the areas that mention it, unless it is mentioned everywhere
                    at = {m["path"].split("/")[0] for e in v.names_of(fold(t)) for m in v.ents[e]["mentions"]}
                    near |= at if len(at) <= 12 else set()
                near = near if len(near) <= 12 else set()
                near |= {a for a in general if not near}  # no project in sight: the general areas too
                if not areas and not near and ids:  # ids the index does not know: grep everything for them alone
                    near = {p.split("/")[0] for p in grep_lines(root, ids) if "/" in p}
                    near = near if len(near) <= 12 else set()
                areas = sorted(set(areas or []) | near) if areas or near else None
            if "task" in intent and areas is not None:
                areas = sorted(set(areas) | general)
        pool = v.notes if areas is None else [p for a in areas for p in by_area[a]]
        paths = {p: [t for t in pats if len(t) >= 4 and t not in scoped_pats and t in p.lower()] for p in pool
                 if not scope or p.split("/")[0].lower() in scope}
        per_q.append({"q": q, "pats": {t: w for t, w in pats.items() if t not in scoped_pats}, "intent": intent, "hint": hint,
                      "ents": hit_ents, "by_id": by_id, "named": named, "scope": scope, "areas": areas,
                      "paths": {p: ts for p, ts in paths.items() if ts}})
    groups = defaultdict(list)  # questions that grep the same areas share one grep
    for x in per_q:
        groups[None if x["areas"] is None else tuple(x["areas"])].append(x)
    for areas, xs in groups.items():
        allpats = {p for x in xs for p in x["pats"]}
        hits = grep_lines(root, allpats, areas)
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
        N = max(len(v.notes) if areas is None else sum(len(by_area[a]) for a in areas), 1)
        idf = {p: math.log(1 + N / df[p]) for p in df}
        by_file = defaultdict(list)
        for (path, no), (ms, text) in line_pats.items():
            by_file[path].append((no, ms, text))
        for x in xs:
            x["ranked"] = rank(x, by_file, idf, v)
            x["taste"] = taste(x, by_file, v, taste_pool) if "task" in x["intent"] else []
    budget = args.budget or 900 * len(qs) + 1500

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

    def render(complete):
        """complete=False: the answering lines under each question. complete=True: each question points at its
        notes, then the whole memory follows once, by area — for small memories, where that costs about the same."""
        printed, out = {}, []
        for x in per_q:
            out.append(f"## {x['q']}")
            if x["hint"]:
                out.append(f"  ({x['hint']})")
            if x.get("weak"):
                out.append(f"  ({x['weak']} — try other words, or grep memory/)")
            for eid in sorted(x["ents"])[:2] if "dep" in x["intent"] else []:
                out.append(entity_line(v, eid))
            if complete:
                out += [f"▸ {p}" for p, _ in x["ranked"]] + [f"▸ {p}" for p in x["taste"]]
                if not x["ranked"]:
                    out.append("  (no match — try other words, or grep memory/)")
                continue
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
            if x["taste"]:
                out.append("  preferences and house rules for this task:")
                for p in x["taste"]:
                    out.append(f"▸ {p} · {v.notes[p]['title']}")
        if complete:
            out.append(f"## memory — complete ({len(v.notes)} notes by area, oldest first; SUPERSEDED marks history)")
            for path in sorted(v.notes, key=lambda p: (p.split("/")[0] if "/" in p else "", v.notes[p]["updated"], p)):
                out.append(header(path))
                out += [f"  {t.strip()}" for _, t in body(path)]
        return "\n".join(out)

    text = render(False)
    if len(v.notes) <= COMPLETE_MAX_NOTES:  # a small memory: print all of it when that costs about the same (F1)
        whole = render(True)
        if len(whole) <= COMPLETE_RATIO * len(text):
            text = whole
    print(text)


def taste(x, by_file, v, pool):
    """A task ("make the chart for Chloe's readout") → the preferences and house rules that should shape it. Scored
    inside the general areas only, so project notes that share a word cannot crowd them out. A person (or a family of
    rules) named in the task, or matched through their meetings and reports, brings all their notes; rules about the
    artifact asked for (chart, table, deck …) come along."""
    pats, n = x["pats"], max(len(pool), 1)
    cand = {p: rows for p, rows in by_file.items() if p in pool and p in v.notes}
    df = Counter(t for rows in cand.values() for t in {t for _, ms, _ in rows for t in ms})
    score = {}
    for p, rows in cand.items():
        got = Counter()
        for no, ms, _ in rows:
            for t in ms:
                if t in pats:
                    got[t] += 2 if no == v.notes[p]["line"] else 1
        s_ = sum(pats[t] * math.log(1 + n / df[t]) * (2 if " " in t else 1) for t in got)
        if s_:
            score[p] = s_
    fam = defaultdict(list)  # prefs/<first>-<last>-<topic>.md: one person; chart-style-*: one family of rules
    for p in pool:
        parts = v.notes[p]["id"].lower().split("-")
        if len(parts) >= 3 and parts[0].isalpha() and parts[1].isalpha():
            fam[f"{parts[0]}-{parts[1]}"].append(p)
    fam = {k: ps for k, ps in fam.items() if len(ps) >= 2}
    words = re.findall(r"[a-z]+", re.sub(r"'s\b", "", x["q"].lower()))
    firsts = defaultdict(set)
    for k in fam:
        firsts[k.split("-")[0]].add(k)
    named = {k for k in fam if k in {f"{a}-{b}" for a, b in zip(words, words[1:])}}
    named |= {next(iter(ks)) for f, ks in firsts.items() if len(ks) == 1 and f in words}
    for p, _s in sorted(score.items(), key=lambda z: -z[1])[:3]:  # two hops: a person named in a matched house note
        for _no, _ms, txt in cand.get(p, []):  # (the roster of their meeting, their report) is the audience
            low_t = txt.lower()
            for k in fam:
                if k not in named and re.search(r"\b" + k.replace("-", "[ -]") + r"\b", low_t):
                    named.add(k)
    top = max(score.values(), default=0) or 1.0
    for k in named:
        for p in fam[k]:
            score[p] = score.get(p, 0) + top + 1
    for k, ps in fam.items():  # matched through context (their meeting, their report): the whole person comes along
        got = sum(score.get(p, 0) for p in ps)
        if k not in named and got >= 0.5 * top:
            for p in ps:
                score[p] = max(score.get(p, 0), 0.6 * got)
    arts = {stem(m.group(1).lower()) for m in ART.finditer(x["q"])}
    for p in pool:
        t = (v.notes[p]["title"] or "").lower()
        if arts and any(re.search(r"\b" + re.escape(a), t) for a in arts):
            score[p] = score.get(p, 0) + 0.5 * top
        if v.notes[p]["id"].lower().startswith("me-"):  # your own taste applies to every task
            score[p] = score.get(p, 0) + 0.5 * top
    shown = {p for p, _ in x["ranked"]}
    ranked = sorted(((p, s_) for p, s_ in score.items() if p not in shown), key=lambda z: (-z[1], z[0]))
    return [p for p, s_ in ranked[:TASTE_MAX] if s_ >= TASTE_FLOOR * ranked[0][1]] if ranked else []


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
    inside = {a.lower() for a in (x["scope"] or x.get("areas") or ())}
    for eid in x["ents"]:  # notes that mention a matched entity, findings and decisions first
        for m in v.ents[eid]["mentions"]:
            if inside and m["path"].split("/")[0].lower() not in inside:
                continue
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
    # weak match (F4): a word of the question occurs nowhere in the memory and the best note covers at most half of
    # the question's words — say so instead of heading an unrelated note like a hit
    content = {t for t, w in pats.items() if w >= 1 and " " not in t}
    missing = sorted(t for t in content if t not in idf)
    hit = set(base.get(picks[0][0], {})) if picks else set()
    strong = any(pats.get(t, 0) >= 1.5 for t in hit)  # an id, a number or a word pair matched: not a guess
    x["weak"] = ""
    if picks and missing and not strong and not x["named"] and not x["ents"] and content \
            and len(hit & content) <= WEAK_SHARE * len(content):
        x["weak"] = "weak match: " + ", ".join(f"'{t}'" for t in missing[:3]) + " found nowhere in memory"
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
    g, _ = load(root)
    if len(g["notes"]) > WIDE and not args.out:
        n = write_viz_big(root, g, root / "_dream", force=True)
        print(f"{root / '_dream' / 'graph.html'}: overview of {len(g['notes'])} notes; {n} area pages in "
              f"{root / '_dream' / 'viz'} — open it in a browser")
        return
    out = Path(args.out).expanduser() if args.out else root / "_dream" / "graph.html"
    write_viz(root, g, out)
    print(f"{out}: {len(g['notes'])} notes, {len(g['entities'])} entities — open it in a browser")


def viz_template():
    return read(Path(__file__).resolve().parent.parent / "assets" / "viz.html")


def render_viz(data, out, tpl=None):
    tpl = tpl or viz_template()
    island = "{\n" + ",\n".join(f'"{k}": ' + ("[\n" + ",\n".join(json.dumps(r, ensure_ascii=False) for r in v) + "\n]"
                                             if isinstance(v, list) else json.dumps(v)) for k, v in data.items()) + "\n}\n"
    a = tpl.index('id="data-graph"')
    a = tpl.index("\n", a) + 1
    wr(out, tpl[:a] + island.replace("</", "<\\/") + tpl[tpl.index("</script>", a):])


def note_text(root, n):
    try:
        ls = read(root / n["path"]).split("\n")
    except OSError:
        ls = []
    return [x for x in ls[(n["line"] or 1) - 1:] if x.strip()][:14]


def write_viz(root, g, out):
    """A self-contained HTML viewer of the graph: map, overview, explorer, health."""
    render_viz({"built": g["built"], "notes": [{**n, "text": note_text(root, n)} for n in g["notes"]],
                "entities": g["entities"], "relations": g["relations"], "edges": g["edges"], "checks": g["checks"],
                "review": g["review"], "proposed": g["proposed"]}, out)


def write_viz_big(root, g, dd, force=False):
    """Big memories: _dream/graph.html is an overview of areas, _dream/viz/<area>.html one viewer per area, rewritten
    only when something in the area changed. → number of area pages written."""
    def area(p):
        return p.split("/")[0] if "/" in p else "(root)"
    tpl = viz_template()
    notes = {n["path"]: n for n in g["notes"]}
    by, e_by, m_by, r_by, c_by = (defaultdict(list) for _ in range(5))
    for n in g["notes"]:
        by[area(n["path"])].append(n)
    for e in g["edges"]:
        for a in {area(e["src"]), area(e["dst"])}:
            e_by[a].append(e)
    for e in g["entities"]:
        ms = defaultdict(list)
        for m in e["mentions"]:
            ms[area(m["path"])].append(m)
        for a, mm in ms.items():
            m_by[a].append((e, mm))
    for r in g["relations"]:
        for a in {area(ev.rsplit(":", 1)[0]) for ev in r["evidence"]}:
            r_by[a].append(r)
    checks = [c for c in g["checks"] if c["code"] != "C5"]
    for c in checks:
        head = c["msg"].split(":")[0]
        if "/" in head:
            c_by[area(head)].append(c)
    pages = dd / "viz"
    pages.mkdir(parents=True, exist_ok=True)
    old = rd(pages / "_sig.json", {}) or {}
    sigs, wrote = {}, 0
    tsig = hashlib.sha1(tpl.encode()).hexdigest()[:12]
    for a, ns in by.items():
        sig = hashlib.sha1(json.dumps([tsig, [[n["path"], n["sha"], n["kind"], n["superseded_by"]] for n in ns],
                                       [[e["src"], e["dst"], e["rel"]] for e in e_by[a]],
                                       [[e["id"], e["type"], e["home"]] for e, _ in m_by[a]],  # not names: a hub's new spelling would redraw everything
                                       [[r["s"], r["type"], r["o"]] for r in r_by[a]], [c["msg"] for c in c_by[a]]]).encode()).hexdigest()[:16]
        sigs[a] = sig
        out = pages / f"{a}.html"
        if not force and old.get(a) == sig and out.exists():
            continue
        stubs = {p: {**notes[p], "text": []} for e in e_by[a] for p in (e["src"], e["dst"]) if area(p) != a and p in notes}
        render_viz({"mode": "area", "area": a, "home": "../graph.html", "built": g["built"],
                    "notes": [{**n, "text": note_text(root, n)} for n in ns] + list(stubs.values()),
                    "entities": [{**e, "names": e["names"][:6], "aka": e["aka"][:6], "mentions": mm} for e, mm in m_by[a]],
                    "relations": [{**r, "evidence": [x for x in r["evidence"] if area(x.rsplit(":", 1)[0]) == a]} for r in r_by[a]],
                    "edges": e_by[a],
                    "checks": c_by[a], "review": [], "proposed": []}, out, tpl)
        wrote += 1
    for a in set(old) - set(sigs):
        (pages / f"{a}.html").unlink() if (pages / f"{a}.html").exists() else None
    wr(pages / "_sig.json", sigs)
    general = {a for a, ns in by.items() if a.lower() in GENERAL or sum(n["kind"] in WORK for n in ns) < 0.8 * len(ns)}
    w = Counter()
    for e in g["edges"]:
        a, b = area(e["src"]), area(e["dst"])
        if a != b and "log" not in (a, b):
            w[tuple(sorted((a, b)))] += 1
    for e in g["entities"]:
        ps = sorted({area(m["path"]) for m in e["mentions"]} - {"log"})
        if 2 <= len(ps) <= 50:  # an entity everywhere links nothing in particular
            for i in range(len(ps)):
                for j in range(i + 1, len(ps)):
                    w[(ps[i], ps[j])] += 1 / (len(ps) - 1)
    best = defaultdict(list)
    for k, x in w.items():
        for a in k:
            best[a].append((x, k))
    keep = {k for lst in best.values() for _, k in sorted(lst, reverse=True)[:3]}
    linked = {p for e in g["edges"] for p in (e["src"], e["dst"])}
    render_viz({"mode": "overview", "built": g["built"], "pages": "viz/",
                "totals": {"notes": len(g["notes"]), "entities": len(g["entities"]), "relations": len(g["relations"]),
                           "edges": len(g["edges"]), "areas": len(by), "checks": dict(Counter(c["code"] for c in g["checks"]))},
                "areas": [{"id": a, "n": len(by[a]), "general": a in general,
                           "kinds": dict(Counter(n["kind"] for n in by[a]).most_common()),
                           "updated": max(n["updated"] for n in by[a]), "superseded": sum(bool(n["superseded_by"]) for n in by[a]),
                           "warnings": len(c_by[a]), "edges": len(e_by[a])} for a in sorted(by)],
                "area_links": [{"a": a, "b": b, "w": round(w[(a, b)], 2)} for a, b in sorted(keep)],
                "checks": checks[:300],
                "chains": [{"path": n["path"], "title": n["title"], "by": n["superseded_by"]} for n in g["notes"] if n["superseded_by"]][:300],
                "orphans": [{"path": n["path"], "title": n["title"], "kind": n["kind"]} for n in g["notes"]
                            if n["path"] not in linked and n["kind"] != "log"][:300],
                "review": g["review"], "proposed": g["proposed"],
                "notes": [], "entities": [], "relations": [], "edges": []}, dd / "graph.html", tpl)
    return wrote


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
