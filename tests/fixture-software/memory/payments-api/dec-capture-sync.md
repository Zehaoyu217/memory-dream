---
from: [q-capture-mode]
updated: 2026-04-02
---
# Capture runs synchronously in the request path
Decision, 2026-04-02. Authorise and capture in one request; the p95 budget of 300 ms leaves room for the extra
acquirer round trip (about 90 ms p95 on staging). Simpler to reason about than a queue. Revisit if the budget is
missed. Owner Priya Nair.
