---
from: []
updated: 2025-02-03
---
# Can a GBM beat the logistic scorecard for 30+ within 3 months well enough to replace it on the watchlist?
The watchlist currently uses ed-logit-v1, a 14-variable logistic scorecard in production since 2022.
Test: AUC, Gini and KS on early-delinquency-holdout-2024q4, with the same inputs where possible.
Decision needed: whether a gradient-boosted model is stable enough across thin-file and full-file segments to replace the scorecard.
