#!/usr/bin/env python3
"""A K-times bigger memory from an indexed one, for scale tests: K-1 sibling copies of every project.

  make_world.py <indexed memory root> <out memory root> --copies K

Copy k of project P is a sibling project with different facts:
  - project-local ids get a code infix: fraud-2026 → fraud-xab-2026, exp-014 → exp-xab-014 (note names, and
    hyphenated ids with a digit that general notes never use); shared tables and terms stay shared
  - every number in the note body moves its last digit (0.81 → 0.83); years, dates and ids stay
  - its cached extraction is copied through the same rewrite, so the copy counts as already indexed (no model calls)
General areas and the log stay 1×: one person keeps one set of preferences. Originals are untouched, so
questions and their gold notes still hold.
"""
import argparse
import hashlib
import json
import re
import shutil
from collections import defaultdict
from pathlib import Path

GENERAL = {"prefs", "reporting", "glossary", "corrections", "howto", "qa", "log"}
TOKEN = re.compile(r"(?<![A-Za-z0-9_.-])([A-Za-z][A-Za-z0-9]*(?:-[A-Za-z0-9]+)+)(?![A-Za-z0-9_])")
NUM = re.compile(r"(?<![A-Za-z0-9_.,-])(\d+(?:[.,]\d+)*)(?![A-Za-z0-9_-]|[.,]\d)")
KEEP = {"path", "sha", "model", "indexed_at"}


def code(k):
    a, b = divmod(k - 1, 26)
    return "x" + "abcdefghijklmnopqrstuvwxyz"[a] + "abcdefghijklmnopqrstuvwxyz"[b]


def infix(tok, c):
    head, rest = tok.split("-", 1)
    return f"{head}-{c.upper() if head.isupper() else c}-{rest}"


def bump(m, s):
    t = m.group(1)
    if re.fullmatch(r"(19|20)\d\d", t):
        return t
    return t[:-1] + str((int(t[-1]) + s) % 10)


def rewrite(text, local, c, s, body_from=0):
    head, body = text[:body_from], text[body_from:]
    sub = lambda z: TOKEN.sub(lambda m: infix(m.group(1), c) if m.group(1).lower() in local else m.group(1), z)  # noqa: E731
    return sub(head), NUM.sub(lambda m: bump(m, s), sub(body))


def body_start(text):
    if text.startswith("---\n"):
        j = text.find("\n---", 4)
        if j > 0:
            return text.find("\n", j + 1) + 1
    return 0


def walk(x, f):
    if isinstance(x, str):
        return f(x)
    if isinstance(x, list):
        return [walk(v, f) for v in x]
    if isinstance(x, dict):
        return {k: (v if k in KEEP else walk(v, f)) for k, v in x.items()}
    return x


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("out")
    ap.add_argument("--copies", type=int, required=True)
    a = ap.parse_args()
    src, out = Path(a.src), Path(a.out)
    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(src, out, ignore=shutil.ignore_patterns("graph.json", "graph.html", "pending"))
    man = json.loads((src / "_dream/manifest.json").read_text())
    texts = {p.relative_to(src).as_posix(): p.read_text() for p in src.rglob("*.md")
             if not p.relative_to(src).as_posix().startswith("_dream/") and "/" in p.relative_to(src).as_posix()}
    where = defaultdict(set)
    for rel, t in texts.items():
        for m in TOKEN.finditer(t):
            where[m.group(1).lower()].add(rel.split("/")[0])
    projects = sorted({r.split("/")[0] for r in texts} - GENERAL)
    slugs = {Path(r).stem.lower() for r in texts if r.split("/")[0] not in GENERAL and "-" in Path(r).stem}
    local = set(projects) | slugs | {t for t, ps in where.items() if any(ch.isdigit() for ch in t) and not ps & GENERAL}
    local -= {t for t in local if re.fullmatch(r"(19|20)\d\d(-\d\d){1,2}", t)}  # dates
    n = 0
    for k in range(1, a.copies):
        c, s = code(k), 1 + k % 9
        for rel, t in texts.items():
            p = rel.split("/")[0]
            if p in GENERAL:
                continue
            h, b = rewrite(t, local, c, s, body_start(t))
            t2 = h + b
            rel2 = "/".join(infix(x, c) if x.lower() in local else x for x in rel[:-3].split("/")) + ".md"
            (out / rel2).parent.mkdir(parents=True, exist_ok=True)
            (out / rel2).write_text(t2)
            f = man["files"].get(rel)
            xp = src / "_dream/notes" / f"{f['sha'][:12]}.json" if f else None
            if xp and xp.exists():
                x = walk(json.loads(xp.read_text()), lambda z: "".join(rewrite(z, local, c, s, 0)))
                sha = hashlib.sha256(t2.encode()).hexdigest()
                x.update(path=rel2, sha=sha)
                (out / "_dream/notes" / f"{sha[:12]}.json").write_text(json.dumps(x))
            n += 1
    print(f"{len(texts)} source notes · {len(projects)} projects × {a.copies} · {len(local)} local ids · wrote {n} copies")


if __name__ == "__main__":
    main()
