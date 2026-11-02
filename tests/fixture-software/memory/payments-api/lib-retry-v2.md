---
from: [fnd-retry-amplification]
supersedes: [lib-retry-v1]
updated: 2026-08-04
---
# retry library v2: three attempts, 200 ms base with full jitter, 2 s cap, no retry on 4xx
`src/payments/retry.py`, PR #418. Exponential backoff of 200 ms times 2^n with full jitter, capped at 2 s, three
attempts in total; 4xx responses are never retried; a `Retry-After` header is honoured. Replaces lib-retry-v1, whose
fixed delay synchronised retries during the 2026-07-30 incident. Tests: `tests/test_retry.py` (9 cases). Owner Priya Nair.
