#!/usr/bin/env python3
"""Agent arms run headless, each with what it cost: one `claude -p` a batch of questions, scored exactly.

  python3 eval/agent/run_headless.py prepare <dreamed memory> <arms dir>
        <arms>/grep/memory      the notes alone (no registry, no _dream/): what an agent with grep has
        <arms>/memory/memory    the same notes with their dreamed memory, and <arms>/memory/skills/memory-dream
  python3 eval/agent/run_headless.py run <grep|memory> <model> <arms dir> <questions.jsonl> <out dir>
        [--runs 3] [--batch 10] [-j 4] [--only 1,2] [--tidy] [--flat] [--window 100000] [--max-turns 80]
        one call a batch and a run; answers to <out>/<arm>-<model>-r<run>-b<batch>.md, the CLI's own usage and cost
        to <out>/usage.jsonl, every tool call to <out>/calls/…jsonl
  python3 eval/agent/run_headless.py table <questions.jsonl> <out dir> [--batch 10] [--arms <arms dir>]
        per arm and model: exact answers, recall, precision, $ and seconds a ten questions, tool calls, over the runs

The agent's world is its workspace: the prompt says so, and `table` counts the tool calls that named a path under a
home folder outside it (there should be none; the answer key is never under the arms dir; scratch files an agent
writes under /tmp are not counted). `--tidy` words the prompt for a bank whose
links are lines of frontmatter; without it the prompt says that a note states its links in its own text.
The model's own name, tokens and dollars come from the CLI's result (`total_cost_usd`, list prices), not from an
estimate. Quoted in RESULTS.md phase S.

`--window N` holds an arm to a context of N tokens: the CLI is told to compact the conversation at that size
(CLAUDE_CODE_AUTO_COMPACT_WINDOW, 100,000 at the least) and not to use the million-token window that Haiku 5.5 and
Opus 5.5 otherwise run with (CLAUDE_CODE_DISABLE_1M_CONTEXT). It is where compaction starts and not a wall, so what
it did is measured: each batch's row keeps the largest request it sent (`peak`, tokens in, cached ones included)
and how often it was compacted (`compacts`), and `table` prints both. `--flat` words the prompt for a bank whose
project notes are all in one folder (eval/hard/make_flat.py).
"""
import collections
import json
import os
import re
import shutil
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO / "eval"))
REG = {"KINDS.md", "TYPES.md", "EDGES.md", "ALIASES.md", "CONFLICTS.md", "DIGEST.md", "TAGS.md", "SETUP.md"}
TAIL = """Reply in exactly this format, nothing else:
## Q1
<answer in 1–3 sentences>
Notes: <the paths of the notes that answer the question, comma-separated, like {like}>
"""
LAYOUT = {False: "one folder per project, plus prefs/, reporting/,\nglossary/, corrections/, howto/ and qa/",
          True: "the notes of every project are in one folder, work/, and\nnothing but a note's own name and words says which project it belongs to; beside it prefs/, reporting/,\nglossary/, corrections/, howto/ and qa/"}
LINKS = {True: "frontmatter `from:` names the notes a note was built on and `supersedes:` the notes it overturns",
         False: "a note says in its own text what it was built on and what it replaces, by the other note's id or in a few "
                "words; there is no frontmatter for it"}


def prepare(mem, arms):
    mem, arms = Path(mem), Path(arms)
    if arms.exists():
        raise SystemExit(f"{arms} exists: give a fresh arms dir")
    shutil.copytree(mem, arms / "memory" / "memory")
    shutil.copytree(REPO / "skills" / "memory-dream", arms / "memory" / "skills" / "memory-dream",
                    ignore=shutil.ignore_patterns("__pycache__"))
    n = 0
    for f in mem.rglob("*.md"):
        rel = f.relative_to(mem)
        if rel.parts[0].startswith(("_", ".")) or (len(rel.parts) == 1 and rel.name in REG):
            continue
        (arms / "grep" / "memory" / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(f, arms / "grep" / "memory" / rel)
        n += 1
    print(f"{arms}/grep: {n} notes · {arms}/memory: the dreamed memory and the skill")


def prompt_for(arm, W, batch, tidy, flat=False):
    ql = "".join(f"Q{i} {q['q']}\n" for i, q in enumerate(batch, 1))
    tail = TAIL.replace("{like}", "work/exp-104-fraud-2025.md" if flat else "fraud-2025/exp-104.md")
    head = (f"You are answering questions about a data-science team's past work. Work only inside {W} — do not read or\n"
            f"search anything outside it.\n")
    if arm == "grep":
        return (head + f"The team's notes are markdown files under {W}/memory/ ({LAYOUT[flat]}; one note per question, experiment, finding, decision, or\n"
                f"dataset/feature/model description; the `# ` line states the point; {LINKS[tidy]}; log/ holds daily\n"
                f"scratch lines). Find what you need with grep, find, ls and cat via Bash, or with Read" + ("" if flat else "; you may cat whole folders") + ".\n"
                f"This is a read-only task: do not write or edit anything.\n"
                f"Answer these {len(batch)} questions:\n{ql}{tail}")
    skill = (W / "skills/memory-dream/SKILL.md").read_text()
    desc = re.search(r"^description: (.*)$", skill, flags=re.M).group(1)
    step1 = re.search(r"^1\. \*\*Read first, once\.\*\*.*?(?=^2\. )", skill, flags=re.M | re.S).group(0).rstrip()
    return (head + f"The team's memory is in {W}/memory/ ({LINKS[tidy]}). You have this skill:\n"
            f"  memory-dream: {desc}\n"
            f"  memory.py = python3 {W}/skills/memory-dream/scripts/memory.py --root {W}/memory\n"
            f"  How to read it, from the skill:\n{step1}\n"
            f"  (Full instructions, if you need them: {W}/skills/memory-dream/SKILL.md)\n"
            f"This is a read-only task: do not write or edit notes and do not run `dream` or `log`.\n"
            f"Answer these {len(batch)} questions:\n{ql}{tail}")


def outside(calls, W):
    """Tool calls that name a path under a home folder which is not the workspace: the notes of another world, or the
    answer key. Scratch files an agent writes under /tmp are its own business, and so is a long tool result that the
    CLI itself spilled to a file and the agent read back."""
    return sum(1 for c in calls if any(str(W) not in m and "/tool-results" not in m
                                       for m in re.findall(r"/(?:Users|home)/[^\s\"']+", json.dumps(c["input"]))))


def one(arm, model, W, batch, tidy, turns, flat=False, window=0):
    cmd = ["claude", "-p", "--model", model, "--tools", "Bash,Read,Grep,Glob", "--allowedTools", "Bash", "Read", "Grep", "Glob",
           "--setting-sources", "", "--strict-mcp-config", "--no-session-persistence", "--output-format", "stream-json", "--verbose",
           "--max-turns", str(turns)]
    env = dict(os.environ)
    if window:
        env.update(CLAUDE_CODE_AUTO_COMPACT_WINDOW=str(window), CLAUDE_CODE_DISABLE_1M_CONTEXT="1")
    t0 = time.time()
    try:
        r = subprocess.run(cmd, input=prompt_for(arm, W, batch, tidy, flat), cwd=W, capture_output=True, text=True, timeout=3600, env=env)
        out = r.stdout
    except subprocess.TimeoutExpired as e:
        out = (e.stdout or b"").decode() if isinstance(e.stdout, bytes) else (e.stdout or "")
    calls, res, seen, sizes = [], {}, set(), {"peak": 0, "compacts": 0}
    for ln in out.split("\n"):
        try:
            ev = json.loads(ln)
        except ValueError:
            continue
        if ev.get("type") == "assistant":
            m = ev.get("message") or {}
            for c in m.get("content") or []:
                if c.get("type") == "tool_use":
                    calls.append({"tool": c.get("name"), "input": c.get("input")})
            u = m.get("usage") or {}
            if m.get("id") not in seen:  # one request may come as several events: its tokens in are counted once
                seen.add(m.get("id"))
                sizes["peak"] = max(sizes["peak"], u.get("input_tokens", 0) + u.get("cache_read_input_tokens", 0) + u.get("cache_creation_input_tokens", 0))
        elif ev.get("type") == "system" and ev.get("subtype") == "compact_boundary":
            sizes["compacts"] += 1
        elif ev.get("type") == "result":
            res = ev
    return res, calls, round(time.time() - t0, 1), sizes


def run(arm, model, arms, qfile, out, runs, size, j, only, tidy, turns, flat=False, window=0):
    W, out = (Path(arms) / arm).resolve(), Path(out)
    qs = [json.loads(x) for x in Path(qfile).read_text().splitlines() if x.strip()]
    batches = [qs[k:k + size] for k in range(0, len(qs), size)]
    (out / "calls").mkdir(parents=True, exist_ok=True)
    jobs = [(r, b) for r in range(1, runs + 1) for b in range(1, len(batches) + 1) if not only or b in only]
    jobs = [(r, b) for r, b in jobs if not (out / f"{arm}-{model}-r{r}-b{b}.md").exists()]  # a run that is on file is not paid for twice

    def do(job):
        r, b = job
        res, calls, secs, sizes = one(arm, model, W, batches[b - 1], tidy, turns, flat, window)
        name = f"{arm}-{model}-r{r}-b{b}"
        (out / f"{name}.md").write_text(res.get("result") or "")
        (out / "calls" / f"{name}.jsonl").write_text("".join(json.dumps(c) + "\n" for c in calls))
        u = res.get("usage") or {}
        row = {"arm": arm, "model": model, "run": r, "batch": b, "questions": len(batches[b - 1]), "cost": res.get("total_cost_usd"),
               "turns": res.get("num_turns"), "tools": len(calls), "seconds": secs, "ms": res.get("duration_ms"),
               "in": u.get("input_tokens", 0) + u.get("cache_read_input_tokens", 0) + u.get("cache_creation_input_tokens", 0),
               "out": u.get("output_tokens"), "models": sorted((res.get("modelUsage") or {})), "error": res.get("is_error"),
               "subtype": res.get("subtype"), "workspace": str(W), "outside": outside(calls, W), "window": window, **sizes}
        with open(out / "usage.jsonl", "a") as f:
            f.write(json.dumps(row) + "\n")
        return row
    with ThreadPoolExecutor(max(1, j)) as ex:
        for row in ex.map(do, jobs):
            print(f"  {row['arm']} {row['model']} run {row['run']} batch {row['batch']}: ${row['cost'] or 0:.4f} · {row['tools']} tool calls · "
                  f"{row['seconds']:.0f} s · largest request {row['peak']:,} tokens" + (f", compacted {row['compacts']} times" if row["compacts"] else "")
                  + (" · ERROR " + str(row["subtype"]) if row["error"] or not row["cost"] else ""), flush=True)


def table(qfile, out, size, arms=None):
    from linkage import tally
    out = Path(out)
    qs = [json.loads(x) for x in Path(qfile).read_text().splitlines() if x.strip()]
    batches = [qs[k:k + size] for k in range(0, len(qs), size)]
    rows = {}
    for ln in (out / "usage.jsonl").read_text().splitlines():
        r = json.loads(ln)
        rows[(r["arm"], r["model"], r["run"], r["batch"])] = r  # the last line for a run and a batch counts
    by = collections.defaultdict(list)
    for (arm, model, run_, b), r in sorted(rows.items()):
        f = out / f"{arm}-{model}-r{run_}-b{b}.md"
        ex, full, rec, pre, kinds, near = tally(batches[b - 1], f.read_text() if f.exists() else "")
        cf = out / "calls" / f"{arm}-{model}-r{run_}-b{b}.jsonl"
        if cf.exists() and (r.get("workspace") or arms):  # counted again from the calls on file, by today's rule
            r["outside"] = outside([json.loads(x) for x in cf.read_text().splitlines() if x.strip()],
                                   r.get("workspace") or (Path(arms) / arm).resolve())
        by[(arm, model)].append({**r, "exact": ex, "full": full, "rec": rec * len(batches[b - 1]), "pre": pre * len(batches[b - 1]),
                                 "kinds": kinds, "near": near})
    print("arm · model · runs × questions · exact answers · exact, or in force with its chain · whole set named · recall · precision · "
          "$ a ten questions · seconds a ten · tool calls a ten · calls that named a path outside the workspace")
    for (arm, model), rs in sorted(by.items()):
        n = sum(r["questions"] for r in rs)
        per_run = collections.defaultdict(lambda: [0, 0])
        for r in rs:
            per_run[r["run"]][0] += r["exact"]
            per_run[r["run"]][1] += r["questions"]
        runs = " · ".join(f"{a}/{b}" for a, b in (per_run[k] for k in sorted(per_run)))
        kinds = collections.defaultdict(lambda: [0, 0])
        for r in rs:
            for k, (a, b) in r["kinds"].items():
                kinds[k][0] += a
                kinds[k][1] += b
        ten = 10 / n
        near = sum(r["near"] for r in rs)
        print(f"{arm} · {'+'.join(rs[0]['models']) or model} · {len(per_run)} × {n // max(1, len(per_run))} · {sum(r['exact'] for r in rs)}/{n} "
              f"({sum(r['exact'] for r in rs) / n:.0%}; by run {runs}) · {near}/{n} ({near / n:.0%}) · {sum(r['full'] for r in rs) / n:.0%} · "
              f"{sum(r['rec'] for r in rs) / n:.2f} · "
              f"{sum(r['pre'] for r in rs) / n:.2f} · {sum(r['cost'] or 0 for r in rs) * ten:.4f} · {sum(r['seconds'] for r in rs) * ten:.0f} · "
              f"{sum(r['tools'] for r in rs) * ten:.1f} · {sum(r['outside'] for r in rs)}")
        print("    exact by kind: " + ", ".join(f"{k} {a}/{b}" for k, (a, b) in sorted(kinds.items())))
        if any("peak" in r for r in rs):
            w = {r.get("window") for r in rs}
            print(f"    context: window {' or '.join('none set' if not x else f'{x:,}' for x in sorted(w, key=str))} · largest request "
                  f"{max(r.get('peak', 0) for r in rs):,} tokens · batches over 100,000: {sum(r.get('peak', 0) > 100000 for r in rs)} of {len(rs)} · "
                  f"compactions {sum(r.get('compacts', 0) for r in rs)}")


if __name__ == "__main__":
    a = sys.argv[1:]
    opt = lambda k, d: a[a.index(k) + 1] if k in a else d  # noqa: E731
    if len(a) == 3 and a[0] == "prepare":
        prepare(a[1], a[2])
    elif len(a) >= 6 and a[0] == "run":
        run(a[1], a[2], a[3], a[4], a[5], int(opt("--runs", 3)), int(opt("--batch", 10)), int(opt("-j", 4)),
            {int(x) for x in opt("--only", "").split(",") if x}, "--tidy" in a, int(opt("--max-turns", 80)), "--flat" in a,
            int(opt("--window", 0)))
    elif len(a) >= 3 and a[0] == "table":
        table(a[1], a[2], int(opt("--batch", 10)), opt("--arms", None))
    else:
        raise SystemExit(__doc__)
