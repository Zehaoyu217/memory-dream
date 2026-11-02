---
from: [bug-double-charge, adr-idempotency-v2]
updated: 2026-08-03
---
# Fix for the double charges: the idempotency check moves into the ledger transaction (PR #412)
PR #412 writes the key to `payments.idempotency_keys` in the same transaction as the ledger row, so a replay is
rejected even when Redis is empty. 14 new tests in `tests/test_idempotency.py`; a replay test of 10,000 duplicate
requests against staging produced 0 double charges (2026-08-02). Redis is now a cache only. Shipped in rel-v3-4-0.
Author Priya Nair, reviewed by Dan Okafor.
