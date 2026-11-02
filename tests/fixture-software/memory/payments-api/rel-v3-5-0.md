---
from: [adr-capture-outbox, adr-idempotency-v3, svc-capture-worker]
updated: 2026-09-25
---
# Release v3.5.0, 2026-09-25: asynchronous capture at 100% of merchants, 30-day idempotency keys
Deployed to `prod-eu` at 09:30 CET; canary 5% for 20 minutes, then full. `capture_async` raised from 40% to 100% of
merchants over 2026-09-25 and 2026-09-26. Contains PR #431 (outbox and worker) and PR #437 (30-day keys with the
body hash). CI: 1,842 tests green in 11 minutes. Rollback: `make rollback REV=v3.4.0` and set `capture_async` to 0%.
Release manager Dan Okafor.
