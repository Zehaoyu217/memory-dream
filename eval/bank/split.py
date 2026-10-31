#!/usr/bin/env python3
"""Split Haiku-written bundles into a memory bank and question files, and validate them.

  split.py <bundles dir> <memory out dir> <questions out dir>

Bundle format (see brief.md): "=== FILE <path>" note blocks, "=== LOG" lines "YYYY-MM-DD HH:MM text",
"=== QUESTIONS" one JSON object per line. Logs merge into log/<date>.md with a [project] tag.
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path


def parse(text):
    blocks, cur = [], None
    for ln in text.split("\n"):
        m = re.match(r"^===\s*(FILE\s+(\S+)|LOG|QUESTIONS)\s*$", ln)
        if m:
            cur = {"kind": "file" if m.group(2) else m.group(1), "path": m.group(2), "lines": []}
            blocks.append(cur)
        elif cur is not None:
            cur["lines"].append(ln)
    return blocks


def main():
    src, out, qdir = (Path(a) for a in sys.argv[1:4])
    out.mkdir(parents=True, exist_ok=True)
    qdir.mkdir(parents=True, exist_ok=True)
    notes, logs, qs, report = {}, defaultdict(list), [], Counter()
    for b in sorted(src.glob("*.txt")):
        project = b.stem
        for blk in parse(b.read_text(encoding="utf-8")):
            if blk["kind"] == "file":
                path = blk["path"].strip().lstrip("/")
                if "/" not in path:
                    path = f"{project}/{path}"
                if not path.endswith(".md"):
                    path += ".md"
                body = "\n".join(blk["lines"]).strip("\n")
                if not body.strip():
                    report["empty_note"] += 1
                    continue
                if path in notes:
                    report["duplicate_path"] += 1
                notes[path] = body + "\n"
            elif blk["kind"] == "LOG":
                for ln in blk["lines"]:
                    m = re.match(r"\s*-?\s*(\d{4}-\d\d-\d\d)\s+(\d\d:\d\d)\s+(.*\S)", ln)
                    if m:
                        logs[m.group(1)].append((m.group(2), project, m.group(3)))
            else:
                for ln in blk["lines"]:
                    ln = ln.strip().rstrip(",")
                    if not ln.startswith("{"):
                        continue
                    try:
                        q = json.loads(ln)
                    except ValueError:
                        report["bad_question_json"] += 1
                        continue
                    fix = []
                    for n in q.get("notes") or []:
                        n = str(n).strip().lstrip("/")
                        n = n if "/" in n else f"{project}/{n}"
                        fix.append(n if n.endswith(".md") else n + ".md")
                    q.update(notes=fix, bundle=project)
                    qs.append(q)
    for d, rows in logs.items():
        notes[f"log/{d}.md"] = f"# log {d}\n\n" + "".join(f"- {t} [{p}] {x}\n" for t, p, x in sorted(rows))
    stems = Counter(Path(p).stem for p in notes)
    for path, text in notes.items():
        f = out / path
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(text, encoding="utf-8")
        lines = text.split("\n")
        report["notes"] += 1
        report["over_40_lines"] += len(lines) > 41
        report["no_title"] += not any(ln.startswith("# ") for ln in lines)
        fm = text.split("---")[1] if text.startswith("---") else ""
        for key in ("from", "supersedes"):
            m = re.search(rf"^{key}:\s*\[(.*?)\]", fm, re.M)
            for ref in (m.group(1).split(",") if m else []):
                ref = ref.strip().strip("'\"[]")
                if not ref:
                    continue
                cand = ref if ref.endswith(".md") else ref + ".md"
                ok = cand in notes or f"{path.split('/')[0]}/{cand}" in notes or stems[Path(ref).stem] >= 1
                report[f"{key}_refs"] += 1
                report[f"{key}_unresolved"] += not ok
    for q in qs:
        report["questions"] += 1
        report["question_gold_missing"] += any(n not in notes for n in q["notes"])
    by_bundle = defaultdict(list)
    for q in qs:
        by_bundle[q["bundle"]].append(q)
    for bundle, items in by_bundle.items():
        (qdir / f"bank-{bundle}.jsonl").write_text("".join(json.dumps(q, ensure_ascii=False) + "\n" for q in items),
                                                   encoding="utf-8")
    report["log_days"] = len(logs)
    print(json.dumps(dict(sorted(report.items())), indent=1))


if __name__ == "__main__":
    main()
