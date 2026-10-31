---
from: [cu-uplift-v3, find-cu-sms-cost, find-cu-bureau-lift]
updated: 2026-03-25
---
# Decision: promote cu-uplift-v3 to call routing; SMS for 1-7 DPD, calls for the top 20% of 8-29 DPD
Approved 2026-03-25 by Lena Fischer and Raj Patel, with Aisha Khan (MLOps) signing off on the scoring job.
Routing: 1-7 DPD accounts get SMS by default and a call only if in the top 20% by uplift v3. 8-29 DPD accounts in the top 20% get calls.
Expected gain: uplift +0.005 over v2 on collections-uplift-oot-2026h1. Cost change is small because most calls were already routed by v2.
Channel mix for 8-29 DPD non-top accounts is being set by the wave-2 channel test in collections-channel-mix.
