#!/usr/bin/env python3
"""Can a cheap model turn what an agent wrote into notes that can be trusted? One document, one call, gates in code.

  python3 eval/decompose_probe.py packet <source.md> <packet.md>      the one prompt for the model (it answers JSON)
  python3 eval/decompose_probe.py score  <source.md> <answer.json>    no model: gate every claim, then compare retrieval

The reading follows the method of the owner's claims base, in our own words: the document is cut at its headings; the
model returns, per section, small standalone claims, each with the exact text it rests on; the script then decides
what is kept. A claim is kept when its quote is found in its section, every number in the claim is in the quote or
the heading, the claim adds no negation the quote lacks, and the quote covers at least half of the claim's words.
What is stored as evidence is the document's own text at that place, never the model's copy of it.

`score` then builds two memories, the document whole and the kept claims as one note each, and asks the same
questions of both. The answer kept in eval/real/handoff-claims/ was written by Claude Haiku 5.5 on 2026-11-11 from
the HANDOFF.md of that day (source.md there). Quoted in PLAN.md (rev 3) and RESULTS.md phase K.
"""
import collections
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
MEM = REPO / "skills/memory-dream/scripts/memory.py"
ENV = {k: v for k, v in os.environ.items() if not k.startswith("MEMORY_")}
NEG = re.compile(r"\b(not|never|no|none|neither|nor|without|cannot)\b|n['’]t\b", re.I)
STOP = set("the a an and or of to in on for with by at from as is are was were be been it its this that these those which who "
           "has have had not but than then so if into per each also can may will would should".split())
ASK = [  # a question, a string the answer must contain: eight hand-made, a smoke test
    ("what did the two-step walk do for dependency questions?", "0.920"),
    ("how much did indexing the bank with Haiku cost?", "2.72"),
    ("what is the peak memory of a dream at 168,141 notes?", "4.8 GB"),
    ("has the Neo4j backend ever been run?", "never run"),
    ("how many notes a minute did -j 16 index?", "48 notes"),
    ("why did ask not print the same answer every time?", "hash seed"),
    ("which licence was added and who should confirm it?", "MIT"),
    ("what does the PostgreSQL store do when it is down?", "falls back"),
]
PROMPT = """You turn a working document into small notes for a memory that other agents will search.
The document is cut into sections, each headed `[S<n>] <heading path>`. For each section return its factual claims.

A claim:
- "s": the section id, e.g. "S7".
- "text": ONE fact, in one sentence that can be read alone. Name its subject in full (never "it", "this", "the
  above"). Keep dates, numbers, units, ids, file names and commands exactly as written. Keep every "not", "never",
  "only" and every condition. Do not infer, round, combine or compute anything.
- "quote": the exact text of the section that states it, copied character for character: a whole sentence, list item
  or table row, at least 8 characters. Every number in "text" must be in the quote or in the section heading.
- "kind": one of fact, decision, result, open, howto, caveat.
- "tags": one to three lowercase words for what it is about.
- "entities": the things someone would look up later (ids, files, commands, systems, people), each as
  {"id": "lowercase-with-hyphens", "as": "its words exactly as they stand in the quote"}.

Leave out headings, navigation, pointers to other sections and anything that states no fact. A section with nothing
to say gets no claim. Two claims may share one quote. Reply with JSON only: {"claims": [ ... ]}

DOCUMENT: %s
%s
"""


def sections(text):
    """[(id, heading path, first line, last line, text)] cut at # / ## / ### headings outside code fences."""
    lines, cuts, fence, path = text.split("\n"), [], False, []
    for i, ln in enumerate(lines):
        if ln.lstrip().startswith("```"):
            fence = not fence
        m = None if fence else re.match(r"(#{1,3}) (.*)", ln)
        if m:
            path = path[:len(m.group(1)) - 1] + [m.group(2).strip()]
            cuts.append((i, " > ".join(path)))
    out = []
    for k, (i, p) in enumerate(cuts):
        j = cuts[k + 1][0] if k + 1 < len(cuts) else len(lines)
        body = "\n".join(lines[i + 1:j]).strip("\n")
        if body.strip():
            out.append((f"S{len(out) + 1}", p, i + 2, j, body))
    return out


def find(quote, body):
    """Where the quote is in the section: exact, then with any run of spaces, then without regard to case."""
    i = body.find(quote)
    if i >= 0:
        return i, i + len(quote)
    toks = [re.escape(t) for t in quote.split()]
    if len("".join(quote.split())) < 8 or not toks:
        return None
    for flags in (0, re.I):
        m = re.search(r"\s+".join(toks), body, flags)
        if m:
            return m.start(), m.end()
    return None


def numbers(s):
    return {x.replace(",", "") for x in re.findall(r"\d[\d,]*(?:\.\d+)?", s)}


def words(s):
    return {w[:5] for w in re.findall(r"[a-z][a-z0-9_.@/-]+", s.lower()) if len(w) > 2 and w not in STOP}


def gate(c, secs):
    """-> (reason or '', evidence text from the document, first line, last line)."""
    sec = secs.get(str(c.get("s")))
    text, quote = str(c.get("text") or ""), str(c.get("quote") or "")
    if not sec or len(text) < 12:
        return "malformed", "", 0, 0
    _, path, first, _, body = sec
    span = find(quote, body)
    if not span:
        return "quote not in the section", "", 0, 0
    a = body.rfind("\n", 0, span[0]) + 1  # widen to whole lines: the evidence never cuts a word, a number or a table row
    b = body.find("\n", span[1])
    b = len(body) if b < 0 else b
    ev = body[a:b]
    l0 = first + body.count("\n", 0, a)
    l1 = l0 + ev.count("\n")
    if numbers(text) - numbers(ev) - numbers(path):
        return "a number not in the quote", ev, l0, l1
    if NEG.search(text) and not NEG.search(ev):
        return "a negation the quote lacks", ev, l0, l1
    w = words(text)
    if w and len(w & (words(ev) | words(path))) / len(w) < 0.5 and not ev.lstrip().startswith("|"):
        return "the quote covers under half of the claim", ev, l0, l1
    return "", ev, l0, l1


def run(root, *args):
    return subprocess.run([sys.executable, str(MEM), "--root", str(root), *args], env=ENV, capture_output=True, text=True).stdout


def score(src, ans):
    text = src.read_text()
    secs = {s[0]: s for s in sections(text)}
    claims = json.loads(ans.read_text())["claims"]
    kept, why = [], collections.Counter()
    for c in claims:
        r, ev, l0, l1 = gate(c, secs)
        why[r or "kept"] += 1
        if not r:
            kept.append((c, ev, l0, l1))
    silent = [s for s in secs.values() if len(re.sub(r"\s", "", s[4])) > 400 and not any(c["s"] == s[0] for c, *_ in kept)]
    ents = sum(1 for c, ev, *_ in kept for e in c.get("entities") or [] if isinstance(e, dict))
    ents_ok = sum(1 for c, ev, *_ in kept for e in c.get("entities") or [] if isinstance(e, dict) and str(e.get("as") or "\0") in ev)
    print(f"source: {src.name}, {len(text):,} characters, {len(text.splitlines())} lines, {len(secs)} sections with text")
    print(f"claims returned: {len(claims)} · kept {why['kept']} ({why['kept'] / max(1, len(claims)):.0%}) · refused: "
          + (", ".join(f"{k} {v}" for k, v in sorted(why.items()) if k != "kept") or "none"))
    print(f"sections with over 400 characters and no kept claim: {len(silent)}" + (" (" + "; ".join(s[1].split(' > ')[-1][:40] for s in silent) + ")" if silent else ""))
    print(f"entities on kept claims: {ents} · their words found in the evidence: {ents_ok} ({ents_ok / max(1, ents):.0%})"
          f" · tags: {len({t for c, *_ in kept for t in c.get('tags') or []})} distinct")
    chars_in = len(PROMPT) + len(text)
    chars_out = len(ans.read_text())
    print(f"the call: about {chars_in // 3:,} tokens in and {chars_out // 3:,} out at 3 characters a token · at $0.10 and $0.50 a million "
          f"(Haiku 5.5, a prompt under 100K tokens): ${chars_in / 3 * 0.10 / 1e6 + chars_out / 3 * 0.50 / 1e6:.4f}")
    with tempfile.TemporaryDirectory() as tmp:
        whole, parts = Path(tmp) / "whole" / "memory", Path(tmp) / "claims" / "memory"
        (whole / "handoff").mkdir(parents=True)
        (parts / "handoff").mkdir(parents=True)
        shutil.copy2(src, whole / "handoff" / "handoff.md")
        for n, (c, ev, l0, l1) in enumerate(kept, 1):
            tags = ", ".join(str(t) for t in c.get("tags") or [])
            quote = "\n".join("> " + ln for ln in ev.split("\n"))
            (parts / "handoff" / f"c-{n:03d}.md").write_text(
                f"---\nsource: {src.name}#L{l0}-{l1}\ntype: {c.get('kind', 'fact')}\ntags: [{tags}]\n---\n# {c['text']}\n{quote}\n")
        rows = []
        for name, root in (("the document whole", whole), ("one note a claim", parts)):
            run(root, "dream")
            hit, chars = 0, []
            for q, gold in ASK:
                out = run(root, "ask", q)
                chars.append(len(out))
                hit += gold.lower() in out.lower()
            rows.append(f"{name}: the answer is in what `ask` prints for {hit}/{len(ASK)} questions · {sum(chars) / len(chars):,.0f} characters a question")
        for r in rows:
            print("  " + r)


if __name__ == "__main__":
    if len(sys.argv) != 4 or sys.argv[1] not in ("packet", "score"):
        raise SystemExit(__doc__)
    src = Path(sys.argv[2])
    if sys.argv[1] == "packet":
        body = "\n\n".join(f"[{i}] {p}\n{t}" for i, p, _, _, t in sections(src.read_text()))
        Path(sys.argv[3]).write_text(PROMPT % (src.name, body))
        print(f"{sys.argv[3]}: {len(PROMPT % (src.name, body)):,} characters, {len(sections(src.read_text()))} sections")
    else:
        score(src, Path(sys.argv[3]))
