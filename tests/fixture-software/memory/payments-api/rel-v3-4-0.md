---
from: [fix-double-charge, lib-retry-v2]
updated: 2026-08-05
---
# Release v3.4.0, 2026-08-05: idempotency keys in Postgres, retry library v2
Deployed to `prod-eu` at 10:40 CET after a 20-minute canary at 5%. Contains PR #412 (fix-double-charge) and
PR #418 (lib-retry-v2). CI: 1,796 tests green in 9 minutes. Rollback: `make rollback REV=v3.3.2`. No incidents in
the first 48 hours. Release manager Dan Okafor.
