---
from: [exp-104]
updated: 2026-07-08
supersedes: [fnd-cr-leak-v1]
---
# Caller history v1 leaked: its +0.05 gain on holdout-2025q4 came mostly from post-call contacts
The gain in fnd-cr-leak-v1 came from contacts after the call. On cr-oot-2026h1 the v1 model drops to 0.72 (exp-104).
Caller history must be cut at call start. Retrained v2 holds 0.73 on cr-oot-2026h1 (exp-105).
Caller history v1 is retired; dec-cr-caller-v2 records the change.
