#!/usr/bin/env python3
"""List every tool call of an A21 run: tool, what it asked for, result size. Plus per-request context size.

  calls.py name=transcript.jsonl [...]
"""
import json
import sys


def summarize(path):
    rows = [json.loads(x) for x in open(path) if x.strip()]
    calls, sizes, ctx, seen = [], {}, [], set()
    for r in rows:
        m = r.get("message")
        if not isinstance(m, dict):
            continue
        for c in m.get("content") or [] if isinstance(m.get("content"), list) else []:
            if c.get("type") == "tool_use" and "andback" not in (c.get("name") or ""):
                inp = c.get("input") or {}
                what = inp.get("command") or inp.get("file_path") or json.dumps(inp)[:80]
                calls.append((c["id"], c["name"], " ".join(str(what).split())[:110]))
            if c.get("type") == "tool_result":
                body = c.get("content")
                text = body if isinstance(body, str) else "".join(x.get("text", "") for x in body or [] if isinstance(x, dict))
                sizes[c.get("tool_use_id")] = len(text)
        if m.get("role") == "assistant" and m.get("usage") and m.get("id") not in seen:
            seen.add(m.get("id"))
            u = m["usage"]
            ctx.append(u.get("input_tokens", 0) + u.get("cache_read_input_tokens", 0) + u.get("cache_creation_input_tokens", 0))
    return calls, sizes, ctx


for arg in sys.argv[1:]:
    name, path = arg.split("=", 1)
    calls, sizes, ctx = summarize(path)
    total = sum(sizes.get(i, 0) for i, _, _ in calls)
    print(f"== {name}: {len(calls)} tool calls, {total:,} chars of tool output, "
          f"{len(ctx)} requests, context per request {min(ctx):,}–{max(ctx):,} tokens")
    for i, tool, what in calls:
        print(f"   {tool:5} {sizes.get(i, 0):6,} ch  {what}")
