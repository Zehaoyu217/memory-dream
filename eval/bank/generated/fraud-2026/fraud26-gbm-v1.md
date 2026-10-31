---
from: [fraud-2025/fraud25-gbm-v2, fraud-2025/feat-f25-velocity-v1, feat-f26-device-age, ds-f26-labels-2026]
supersedes: [fraud-2025/fraud25-gbm-v2]
updated: 2026-02-10
---
# fraud26-gbm-v1 replaces the fraud-2025 champion; trained with immature labels
LightGBM on the 2025 velocity feature plus device age, trained on 2025-07 to 2025-12 CNP transactions.
Labels were not yet maturity-cut, so immature frauds were counted as legit (the flaw in fraud26-find-label-bias).
Superseded by fraud26-gbm-v2 on 2026-05-27.
