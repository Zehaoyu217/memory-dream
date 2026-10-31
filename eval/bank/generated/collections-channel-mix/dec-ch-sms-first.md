---
from: [find-ch-sms-matches-call, ch-propensity-v1, feat-ch-optout-flag-v1]
updated: 2025-10-20
---
# Decision: SMS first for 1-7 DPD accounts, with a call only where the channel model says so
Agreed 2025-10-20 by Raj Patel and Lena Fischer (credit risk).
1-7 DPD accounts get SMS first. A call follows only where ch-propensity-v1 scores the call higher. Opt-out accounts (feat-ch-optout-flag-v1) are excluded before choice.
This matches the 1-7 DPD routing in collections-uplift dec-cu-promote-v3.
