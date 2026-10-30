#!/usr/bin/env python3
"""Pull each A21 subagent's final report out of its transcript and tally its API usage.

  extract.py <out_dir> name=transcript.jsonl [name=transcript.jsonl ...]
Writes <out_dir>/<name>.md (the report) and prints one JSON line of usage per run: tool calls,
API requests, and tokens (fresh input, cache read, cache write, output). Nothing else is printed.
"""
import json
import sys
from pathlib import Path


def report_text(rows):
    for r in reversed(rows):
        m = r.get("message")
        if not isinstance(m, dict) or m.get("role") != "assistant" or not isinstance(m.get("content"), list):
            continue
        for c in m["content"]:
            if c.get("type") == "tool_use" and "andback" in (c.get("name") or ""):
                inp = c.get("input") or {}
                return next((v for v in inp.values() if isinstance(v, str) and "## Q" in v), json.dumps(inp))
        texts = [c.get("text", "") for c in m["content"] if c.get("type") == "text"]
        if any("## Q" in t for t in texts):
            return "\n".join(texts)
    return ""


def usage(rows):
    seen, u = set(), {"tool_calls": 0, "requests": 0, "input": 0, "cache_read": 0, "cache_write": 0, "output": 0}
    for r in rows:
        m = r.get("message")
        if not isinstance(m, dict) or m.get("role") != "assistant":
            continue
        for c in m.get("content") or []:
            if c.get("type") == "tool_use" and "andback" not in (c.get("name") or ""):
                u["tool_calls"] += 1
        mid = m.get("id")
        if mid in seen or not m.get("usage"):
            continue
        seen.add(mid)
        x = m["usage"]
        u["requests"] += 1
        u["input"] += x.get("input_tokens", 0)
        u["cache_read"] += x.get("cache_read_input_tokens", 0)
        u["cache_write"] += x.get("cache_creation_input_tokens", 0)
        u["output"] += x.get("output_tokens", 0)
    u["total"] = u["input"] + u["cache_read"] + u["cache_write"] + u["output"]
    return u


if __name__ == "__main__":
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    for arg in sys.argv[2:]:
        name, path = arg.split("=", 1)
        rows = [json.loads(ln) for ln in open(path) if ln.strip()]
        (out / f"{name}.md").write_text(report_text(rows))
        print(json.dumps({"run": name, **usage(rows)}))
