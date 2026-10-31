---
from: [ds-sfc-segment-monthly, feat-sfc-season-v2]
updated: 2025-11-20
---
# sfc-prophet-v1: Prophet with holidays gives 1-month MAPE 6.9%, rejected
Prophet per segment with the retail calendar as holidays.
1-month MAPE 6.9% on sfc-bt-2024 (exp-206), about 40 times the fit time of sfc-lgbm-v2.
Not carried forward; see dec-sfc-drop-prophet.
