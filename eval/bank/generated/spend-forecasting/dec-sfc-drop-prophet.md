---
from: [exp-206, sfc-prophet-v1]
updated: 2025-11-24
---
# Decision: drop Prophet from the segment forecast
Prophet gave 6.9% 1-month MAPE against 5.1% for sfc-lgbm-v2 (exp-206), and fits about 40 times slower.
No ensemble planned; the time cost is not justified by the gain.
sfc-prophet-v1 stays in the repo for reference only.
