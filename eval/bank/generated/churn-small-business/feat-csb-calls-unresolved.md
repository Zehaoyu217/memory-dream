---
from: []
updated: 2025-10-16
---
# feat-csb-calls-unresolved: count of unresolved service calls in the last 90 days
- Source `callcenter.calls`, rows where resolution is open or escalated, in the 90 days before the snapshot.
- First build double-counted calls with a repeated call_id (about 6% of rows); fixed in exp-207.
- Used in csb-xgb-v2 only.
