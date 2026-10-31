---
from: [fraud26-gbm-v1, feat-f26-velocity-v2, feat-f26-device-age, feat-f26-mcc-risk, dec-f26-maturity-60d, ds-f26-labels-2026, ds-f26-cnp-txn]
supersedes: [fraud26-gbm-v1]
updated: 2026-05-27
---
# fraud26-gbm-v2: velocity-v2 clean, MCC risk, 60-day maturity; AUC 0.927
LightGBM with feat-f26-velocity-v2, feat-f26-device-age and feat-f26-mcc-risk.
Trained only on labels at least 60 days old (dec-f26-maturity-60d).
fraud26-oot-2025q4: AUC 0.927, KS 0.70, recall@1% 0.58 (exp-206, 2026-05-22).
