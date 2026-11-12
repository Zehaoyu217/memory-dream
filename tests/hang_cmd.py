#!/usr/bin/env python3
"""A command that never answers, for tests: it reads the prompt, starts a child that sleeps, and waits for it.
$HANG_PID names a file that gets the child's pid, so a test can see that the child was ended too."""
import os
import subprocess
import sys

sys.stdin.read()
child = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(600)"])
if os.environ.get("HANG_PID"):
    with open(os.environ["HANG_PID"], "w") as f:
        f.write(str(child.pid))
child.wait()
