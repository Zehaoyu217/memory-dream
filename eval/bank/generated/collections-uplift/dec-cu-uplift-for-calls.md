---
from: [find-cu-response-misranks, exp-105]
updated: 2025-12-15
---
# Decision: route early-collections calls by uplift rank (cu-uplift-v2), not response rank
Agreed 2025-12-15 by Lena Fischer (credit risk) and Raj Patel (collections).
Calls go to the top 20% by cu-uplift-v2 score among 1-29 DPD accounts; the rest get SMS.
Reason: find-cu-response-misranks showed the response ranking spends calls on accounts that pay anyway.
cu-resp-v1 stays as an explainability reference only.
