---
updated: 2026-05-04
supersedes: [reporting/table-naming-convention]
---
# From 2026-05-04 reporting views drop the `rpt_` prefix: `<domain>_<grain>_<metric>`
- New views are named `<domain>_<grain>_<metric>`, e.g. `retention_monthly_pct`, with the same suffix rules for units.
- Existing `rpt_` views keep working until 2026-09-30, then are retired.
- Reason: the `rpt_` prefix was added to tell views apart from raw tables, but the schema already separates them, so the prefix only doubled names in the catalogue.
