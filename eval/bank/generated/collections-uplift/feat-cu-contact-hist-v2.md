---
from: [ds-cu-call-outcomes]
updated: 2025-03-14
---
# feat-cu-contact-hist-v2 counts contacts in the last 30 days by channel, with days since last PTP
Version 2 of the contact-history feature. Version 1 was a plain contact count with no channel split.
Features: count of SMS, call and email contacts in the last 30 days, days since last PTP, days since last contact.
Source: `callcenter.calls` plus the SMS delivery log. Email counts exclude opens.
Adds +0.012 AUC to cu-resp-v1 on holdout-2025q1 (n=24,860).
