---
from: [clv-ml-v2, ds-clv-cohort-panel]
updated: 2026-02-10
---
# clv-ml-v2 MAPE rises to 19.8% on the 2022 and 2023 cohorts
- On the newer cohorts clv-ml-v2 is less accurate than on the 2021 H1 holdout (15.2%).
- Likely cause: changed offer mix and lower limits in 2023, which the model has not seen.
- Monitored monthly; triggers the retrain in exp-507.
