---
updated: 2025-04-09
from: [howto/leakage-check-post-period]
---
# Q: Why was the dispute-count feature rebuilt? A: It read 14 days past observation, which inflated holdout AUC from 0.72 to 0.79.
The leak scan flagged `feat_disp_cnt_90d_v1` for reading past the observation date. The rebuilt v2 reads only days on or before observation.
