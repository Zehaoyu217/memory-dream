## Q1
Both models build directly on `feat-c25-payment-behaviour` and `feat-c25-txn-recency`. Each also has its own other inputs: churn-gbm-2025-v2 uses feat-c25-util-v2 and churn-lr-base-2025 uses feat-c25-util-v1.
Notes: churn-2025/feat-c25-payment-behaviour.md, churn-2025/feat-c25-txn-recency.md

## Q2
Two current cashback-redesign models build directly on `feat-cb-spend-base`, which has been replaced by `feat-cb-spend-band-v2`: cb-uplift-v1 and cb-elasticity-v1. cb-elasticity-v1 carries no SUPERSEDED marker, but cb-elasticity-v2's text says it replaces that estimate, and no supersedes link is recorded, so treat its status as uncertain.
Notes: cashback-redesign/cb-uplift-v1.md, cashback-redesign/cb-elasticity-v1.md

## Q3
Four decisions rest on feat-app-util-new: dec-app-cutoff-v3 and dec-app-no-gbm, plus dec-app-rebuild-v4 and dec-app-cutoff-v4 (the last three through app-scorecard-v3, app-gbm-v2 and app-scorecard-v4).
Notes: application-scorecard/dec-app-cutoff-v3.md, application-scorecard/dec-app-no-gbm.md, application-scorecard/dec-app-rebuild-v4.md, application-scorecard/dec-app-cutoff-v4.md

## Q4
The line ends at cr-lgbm-v3, which is in force now. It is built directly on cr-lgbm-v2, ds-cr-intent-labels, exp-106 and fnd-cr-threshold.
Notes: call-center-routing/cr-lgbm-v3.md, call-center-routing/cr-lgbm-v2.md, call-center-routing/ds-cr-intent-labels.md, call-center-routing/exp-106.md, call-center-routing/fnd-cr-threshold.md

## Q5
Only one note from another project is built directly on churn-gbm-2025-v2: retention-offers-roi/feat-ror-churn-score, which scores the October 2025 snapshot with it. Fifteen other-project notes rest on churn-2025 more broadly, but they do so through other notes.
Notes: retention-offers-roi/feat-ror-churn-score.md

## Q6
Following app-gbm-v2 back to the start, it rests on two dataset notes: ds-app-applications-2024 and ds-app-reject-sample.
Notes: application-scorecard/ds-app-applications-2024.md, application-scorecard/ds-app-reject-sample.md

## Q7
Both csb-lr-base and csb-xgb-v1 build directly on feat-csb-spend-raw and feat-csb-tenure-band.
Notes: churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-tenure-band.md

## Q8
Only churn-lr-base-2025 is a current model that builds directly on a replaced feature: it uses feat-c25-util-v1, which has been replaced by feat-c25-util-v2. churn-gbm-2025-v2 builds only on current features and datasets.
Notes: churn-2025/churn-lr-base-2025.md

## Q9
Five decisions rest on ds-bt-offer-log: dec-bt-drop-post-offer-features, dec-bt-cut-mailer-top30 and dec-bt-margin-label in balance-transfer-propensity, plus promo-apr-test/dec-pa-6m-default and promo-apr-test/dec-pa-no-12m-subprime.
Notes: balance-transfer-propensity/dec-bt-drop-post-offer-features.md, balance-transfer-propensity/dec-bt-cut-mailer-top30.md, balance-transfer-propensity/dec-bt-margin-label.md, promo-apr-test/dec-pa-6m-default.md, promo-apr-test/dec-pa-no-12m-subprime.md

## Q10
The line ends at dec-cb-threshold-2500, which is in force now. It is built directly on dec-cb-adopt-banded-tiers, exp-206-breakeven-sim and find-cb-breakeven-lift.
Notes: cashback-redesign/dec-cb-threshold-2500.md, cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/exp-206-breakeven-sim.md, cashback-redesign/find-cb-breakeven-lift.md