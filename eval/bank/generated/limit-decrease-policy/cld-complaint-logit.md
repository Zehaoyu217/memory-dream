---
from: [ds-cld-complaint-calls, feat-cld-util-after-decrease, feat-cld-complaint-flag]
updated: 2026-02-16
---
# cld-complaint-logit: logistic model for a complaint within 30 days of a decrease, AUC 0.68
Logistic regression on post-decrease utilisation, the complaint flag and tenure.
Eval: cld-complaint-test-2026q1, n=8,220 decreases, AUC 0.68, precision at top 10% of 0.22.
Used to rank decreases for the notice-first treatment in exp-207.
