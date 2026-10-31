---
from: [ds-mm-reference-train, feat-mm-util-trend-6m]
updated: 2025-02-03
---
# mm-limit-glm-v1: credit-limit increase propensity GLM, 19 features, AUC 0.704
Logistic GLM on 19 features, predicting a limit increase accepted within 60 days.
Evaluated on mm-oot-2024h2 (n=96,000 accounts): AUC 0.704.
Monitored against a flat training reference until the seasonal reference was adopted. Superseded by mm-limit-glm-v2 (2025-10-22).
