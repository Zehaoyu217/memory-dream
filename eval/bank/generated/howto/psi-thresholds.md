---
updated: 2025-10-14
supersedes: [howto/psi-thresholds-v1]
---
# PSI bands are below 0.10 stable, 0.10 to 0.25 monitor, above 0.25 investigate
Compute PSI on decile bins from the training distribution, with at least 500 accounts in the scored population. Below 0.10 is stable. From 0.10 to 0.25 is monitor, which means one line in the weekly PSI log. Above 0.25 is investigate before any score is used in decisions. A retrain is requested only if PSI is above 0.25 and KS also drops by 0.02 or more.
The 0.20 retrain line was dropped after the Q4 2025 seasonal shifts pushed six features past 0.20 while KS moved only from 0.31 to 0.30.
