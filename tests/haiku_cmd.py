#!/usr/bin/env python3
"""Dreamer command for memory.py: prompt on stdin → answer on stdout, via headless Claude Code Haiku.

No tools, no user/project settings, no MCP servers, no session file. If $DREAM_COST_LOG is set,
appends one JSON line per call: cost, tokens, duration. Use as:
  MEMORY_LLM="python3 tests/haiku_cmd.py" memory.py dream -j 6
"""
import json
import os
import subprocess
import sys

MODEL = os.environ.get("DREAM_MODEL", "haiku")
cmd = ["claude", "-p", "--model", MODEL, "--tools", "", "--setting-sources", "", "--strict-mcp-config",
       "--no-session-persistence", "--output-format", "json"]
if os.environ.get("DREAM_EFFORT"):  # e.g. low: less thinking per call
    cmd += ["--effort", os.environ["DREAM_EFFORT"]]
prompt = sys.stdin.read()
r = subprocess.run(cmd, input=prompt, capture_output=True, text=True)
try:
    d = json.loads(r.stdout)
except ValueError:
    sys.stderr.write(r.stderr or r.stdout)
    sys.exit(1)
if os.environ.get("DREAM_COST_LOG"):
    u = d.get("usage") or {}
    kind = "review" if prompt.startswith("You keep") else "gist" if prompt.startswith("Summarise") else "extract"
    with open(os.environ["DREAM_COST_LOG"], "a") as f:
        f.write(json.dumps({"kind": kind, "cost": d.get("total_cost_usd"), "ms": d.get("duration_ms"),
                            "in": u.get("input_tokens", 0) + u.get("cache_read_input_tokens", 0)
                            + u.get("cache_creation_input_tokens", 0), "out": u.get("output_tokens"),
                            "error": d.get("is_error")}) + "\n")
if d.get("is_error"):
    sys.exit(1)
print(d.get("result", ""))
