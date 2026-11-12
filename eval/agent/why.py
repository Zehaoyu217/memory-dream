#!/usr/bin/env python3
"""Why did the agents with the memory answer worse than the agents with grep? Question by question, no model.

  python3 eval/agent/why.py <the dreamed bank-index world: .../memory>

For each of the thirty questions of batches P1, C-h1 and P2: what one `ask` call with the batch's ten questions
prints for it (the call the skill tells an agent to make), set against the reference answer:

  gold     the gold notes headed in the question's section, of those the reference names
  numbers  the numbers of the reference answer that appear in the section, of all its numbers
  chars    the section's size

and beside it the verdicts of judge-H.json (two passes) for Haiku and Opus with the memory and with grep. Then the
size of the folders the gold notes live in: what an agent that reads the folder whole would have in front of it.
Quoted in RESULTS.md phase L.
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MEM = HERE.parent.parent / "skills/memory-dream/scripts/memory.py"
ENV = {k: v for k, v in os.environ.items() if not k.startswith("MEMORY_")}
NUM = re.compile(r"\d+(?:\.\d+)?")


def ask(root, qs):
    out = subprocess.run([sys.executable, str(MEM), "--root", str(root), "ask", *qs], env=ENV, capture_output=True, text=True).stdout
    parts = re.split(r"^## (.*)$", out, flags=re.M)
    return len(out), [parts[i + 1] for i in range(1, len(parts) - 1, 2)], out


def main(root):
    judge = json.loads((HERE / "judge-H.json").read_text())
    v = lambda run, q: "/".join(judge[p][run]["verdicts"].get(q, {}).get("v", "?")[0] for p in ("pass1", "pass2"))  # noqa: E731
    tot = {"short": 0, "short_bad": 0, "full": 0, "full_bad": 0}
    for b in ("P1", "C-h1", "P2"):
        qs = [json.loads(x) for x in (HERE / "batches" / f"{b}.jsonl").read_text().splitlines() if x.strip()]
        size, secs, out = ask(root, [q["q"] for q in qs])
        # a folder printed whole at the end of the call (phase L) is in front of every question that points at it
        blocks = {m.group(1): set(re.findall(r"^▸ (\S+\.md)", m.group(2), flags=re.M))
                  for m in re.finditer(r"^## (\S+/) — the whole folder[^\n]*\n(.*?)(?=^## |\Z)", out, flags=re.M | re.S)}
        text = {f: "\n".join(m.group(2) for m in re.finditer(r"^## (\S+/) — the whole folder[^\n]*\n(.*?)(?=^## |\Z)", out, flags=re.M | re.S)
                             if m.group(1) == f) for f in blocks}
        print(f"\n{b}: one ask call for the ten questions prints {size:,} characters"
              + (f", {', '.join(blocks)} whole" if blocks else ""))
        print("  Q   gold headed  numbers  chars | Haiku mem  Haiku grep  Opus mem  Opus grep | first gold note")
        for i, (q, sec) in enumerate(zip(qs, secs), 1):
            heads = set(re.findall(r"^▸ (\S+\.md)", sec, flags=re.M))
            for line in re.findall(r"^  \((.*) is printed whole below", sec, flags=re.M):
                for f in line.split(", "):
                    heads |= blocks.get(f, set())
                    sec += text.get(f, "")
            gold = q.get("notes") or []
            nums = {n for n in NUM.findall(q["a"]) if len(n) > 1 or "." in n}
            have = {n for n in nums if n in sec}
            ok = all(g in heads for g in gold) and len(have) == len(nums)
            hm = v(f"H-mem-{b}", f"Q{i}")
            bad = hm != "c/c"
            tot["full" if ok else "short"] += 1
            tot["full_bad" if ok else "short_bad"] += bad
            print(f"  Q{i:<2}  {sum(g in heads for g in gold)}/{len(gold)}        {len(have)}/{len(nums):<2}     {len(sec):5,} |   {hm}        {v(f'H-grep-{b}', f'Q{i}')}"
                  f"         {v(f'G-mem-{b}', f'Q{i}')}       {v(f'G-grep-{b}', f'Q{i}')}    | {gold[0] if gold else '-'}{'' if ok else '   <- evidence short'}")
        areas = sorted({g.split("/")[0] for q in qs for g in q.get("notes") or []})
        sizes = {a: sum(p.stat().st_size for p in (Path(root) / a).glob("*.md")) for a in areas}
        print(f"  the gold notes live in {len(areas)} folder(s): " + ", ".join(f"{a} ({sizes[a]:,} characters whole)" for a in areas[:6])
              + (" …" if len(areas) > 6 else "") + f" · together {sum(sizes.values()):,}")
    print(f"\nHaiku with the memory, by what its one call showed: evidence complete for {tot['full']} questions, {tot['full_bad']} of them not "
          f"graded correct twice; evidence short for {tot['short']}, {tot['short_bad']} of them not graded correct twice")
    print("(c = correct, p = partial, w = wrong; two judge passes)")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    main(Path(sys.argv[1]).resolve())
