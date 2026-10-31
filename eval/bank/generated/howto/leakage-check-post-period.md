---
updated: 2025-04-07
---
# A feature that reads days after the observation date is a leak until proven otherwise
For each feature, record the latest `event_date` it reads. It must be on or before `observation_date`. `scripts/leak_scan.py` runs this for every feature in the registry and fails the build on any violation.
The dispute-count feature `feat_disp_cnt_90d_v1` read 14 days past observation. Restricted to days on or before observation, holdout AUC fell from 0.79 to 0.72, so it was rebuilt as v2 and v1 was removed from training.
