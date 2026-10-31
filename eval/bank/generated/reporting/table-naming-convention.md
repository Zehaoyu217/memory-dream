---
updated: 2026-02-23
---
# Reporting views are named `rpt_<domain>_<grain>_<metric>`, e.g. `rpt_retention_monthly_pct`
- The domain is the business area (retention, collections, fraud, onboarding); the grain is the time grain (daily, weekly, monthly).
- The metric suffix states the unit: `_pct`, `_usd`, `_cnt`.
- Views that do not follow the pattern are not used in decks.
