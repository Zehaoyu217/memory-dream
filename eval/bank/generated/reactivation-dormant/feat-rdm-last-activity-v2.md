---
from: [feat-rdm-last-activity-v1, feat-rdm-app-installed]
updated: 2025-06-03
supersedes: [feat-rdm-last-activity-v1]
---
# feat-rdm-last-activity-v2: months since the last card transaction or app session, whichever is more recent
- Takes the most recent of the last card transaction (`cards.txn_daily`) and the last app session (`app.sessions_daily`).
- Accounts that browse but do not spend are no longer treated as fully dormant.
- Replaces feat-rdm-last-activity-v1 in rdm-uplift-v2.
