# Validation standard for scoring models, version 3
The Validation Standard is owned by the Independent Validation team.
A validation covers conceptual soundness, outcome analysis and ongoing monitoring.
Outcome analysis for a classifier reports AUC and KS on a holdout its developers did not tune on.
fraud26-gbm-v3 was validated against the Validation Standard on 2026-09-02.
A LightGBM model also needs a monotonicity check on its top five features.
