---
updated: 2025-04-22
---
# Feature names are feat_<source>_<metric>_<window>_v<n>
Pattern: `feat_<source>_<metric>_<window>_v<n>`, all lowercase, no spaces. Source is the short table name (`txn`, `pay`, `bur`, `lim`, `app`). Window is one of 7d, 30d, 90d or 365d. Example: `feat_txn_spend_sum_30d_v2`.
Any change to a feature definition bumps v. The old version stays in the registry until no live model reads it.
