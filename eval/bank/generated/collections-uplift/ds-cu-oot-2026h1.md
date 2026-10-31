---
from: [ds-cu-treat-log]
updated: 2026-02-20
---
# collections-uplift-oot-2026h1 is the out-of-time eval set for uplift v3, built from Oct-Dec 2025 contacts
Built 2026-02-20 from `collections.cases` Oct-Dec 2025 snapshots after the routing change, with a 3% random holdback kept for measurement.
n=28,450 accounts with at least one eligible contact; control holdback n=860.
Use this set for model selection from 2026 on. holdout-2025q4 is retired for selection.
Labels mature at 14 days, so the set was frozen 2026-02-16, before the build.
