#!/usr/bin/env python3
"""Dreamer command for memory.py: prompt on stdin → answer on stdout, via headless Claude Code Haiku.

No tools, no user/project settings, no MCP servers, no session file. Cache-aware: memory.py sets
$MEMORY_STATIC_PREFIX to the length of the prompt's static part (template, EDGES, KNOWN — identical for
every note of a project); that part goes into the system prompt with --append-system-prompt, which the
CLI caches across calls, and only the note travels as the message. If $DREAM_COST_LOG is set, appends one
JSON line per call: cost, tokens (fresh, cached read, cache written), duration. Use as:
  MEMORY_LLM="python3 tests/haiku_cmd.py" memory.py dream -j 6
"""
import json
import os
import subprocess
import sys

MODEL = os.environ.get("DREAM_MODEL", "haiku")
cmd = ["claude", "-p", "--model", MODEL, "--tools", "", "--setting-sources", "", "--strict-mcp-config",
       "--no-session-persistence", "--output-format", "json"]
effort = os.environ.get("DREAM_EFFORT", "low")  # low by default: −13% per note, grounding catches the few extra slips
if effort and effort != "default":  # DREAM_EFFORT=default restores the CLI's own setting
    cmd += ["--effort", effort]
prompt = sys.stdin.read()
static = int(os.environ.get("MEMORY_STATIC_PREFIX") or 0)
if 0 < static < len(prompt) and not os.environ.get("DREAM_NO_CACHE"):
    cmd += ["--append-system-prompt", prompt[:static]]
    prompt = prompt[static:]
r = subprocess.run(cmd, input=prompt, capture_output=True, text=True)
try:
    d = json.loads(r.stdout)
except ValueError:
    sys.stderr.write(r.stderr or r.stdout)
    sys.exit(1)
if os.environ.get("DREAM_COST_LOG"):
    u = d.get("usage") or {}
    kind = "review" if prompt.startswith("You keep") or "ENTITY PAIRS" in prompt else "extract"
    with open(os.environ["DREAM_COST_LOG"], "a") as f:
        f.write(json.dumps({"kind": kind, "cost": d.get("total_cost_usd"), "ms": d.get("duration_ms"),
                            "in": u.get("input_tokens", 0) + u.get("cache_read_input_tokens", 0)
                            + u.get("cache_creation_input_tokens", 0), "fresh": u.get("input_tokens", 0),
                            "cached": u.get("cache_read_input_tokens", 0), "cache_write": u.get("cache_creation_input_tokens", 0),
                            "out": u.get("output_tokens"), "static": static, "error": d.get("is_error")}) + "\n")
if d.get("is_error"):
    sys.exit(1)
print(d.get("result", ""))
