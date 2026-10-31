---
from: [exp-505, clv-ml-v1, feat-clv-arpu-v2, feat-clv-hazard]
updated: 2025-11-12
supersedes: [clv-ml-v1]
---
# clv-ml-v2: LightGBM for net 36-month margin with offer-netted ARPU and hazard, MAPE 15.2%
- Features: arpu v2, retention hazard, tenure, loss rate; trained on 2019 to 2021 cohorts.
- Holdout clv-oot-2021h1 (n=318,400): MAPE 15.2%.
- Current CLV model for finance and marketing; adopted by dec-clv-ship-ml-v2.
