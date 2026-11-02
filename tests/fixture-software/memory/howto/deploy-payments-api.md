---
updated: 2026-08-05
---
# How to deploy payments-api: CI green, staging soak 30 minutes, prod-eu canary 5% for 20 minutes, then full
1. `make release VERSION=vX.Y.Z` on a green main; CI must show every test green.
2. Deploy to `staging`; soak 30 minutes with the replay job `load/replay-latest`.
3. Deploy to `prod-eu` as a 5% canary for 20 minutes; watch `payments-api-errors` and `capture-lag-high`.
4. Full rollout. Rollback at any step: `make rollback REV=<previous version>`.
The release manager on rotation runs it; Priya Nair's rules on release notes apply.
