---
from: [bsm-app-gbm-v8, feat-bsm-score-map-v1, feat-bsm-score-missing-impute]
updated: 2026-03-02
---
# bsm-app-gbm-v10a: same model with v10 features through the linear map, KS 0.34 on the 2026 cohorts
Retrained on v10 mapped by feat-bsm-score-map-v1, with the source flag from feat-bsm-score-missing-impute.
Eval: ds-bsm-v10-cohorts-2026 (n=71,300), AUC 0.78, KS 0.34 at 60-day delinquency.
Superseded by bsm-app-gbm-v10b (2026-06-10) after the isotonic map.
