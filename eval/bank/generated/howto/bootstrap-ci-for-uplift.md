---
updated: 2025-12-01
---
# Uplift intervals come from 500 account-level bootstrap resamples, 95% percentile
Resample accounts with replacement within each arm, 500 times. Recompute uplift@20% on each resample and take the 2.5th and 97.5th percentiles. Resampling at the offer or campaign level understates the width, so do not do that.
