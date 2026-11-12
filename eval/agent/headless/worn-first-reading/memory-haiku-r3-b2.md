## Q1
Both models build directly on feat-c25-payment-behaviour and feat-c25-txn-recency. churn-gbm-2025-v2 also uses feat-c25-util-v2, and churn-lr-base-2025 also uses feat-c25-app-sessions and feat-c25-util-v1.
Notes: churn-2025/feat-c25-payment-behaviour.md, churn-2025/feat-c25-txn-recency.md, churn-2025/churn-gbm-2025-v2.md, churn-2025/churn-lr-base-2025.md

## Q2
Only cb-uplift-v1 qualifies: it is still current and builds directly on feat-cb-spend-base, which feat-cb-spend-band-v2 replaced. cb-elasticity-v1 also builds on feat-cb-spend-base, but cb-elasticity-v2 replaces it, so it is excluded.
Notes: cashback-redesign/cb-uplift-v1.md, cashback-redesign/feat-cb-spend-base.md

## Q3
Four decisions rest on feat-app-util-new: dec-app-cutoff-v3 (through app-scorecard-v3), dec-app-rebuild-v4 and dec-app-cutoff-v4 (through app-gbm-v2 and app-scorecard-v4), and dec-app-no-gbm (through exp-504).
Notes: application-scorecard/feat-app-util-new.md, application-scorecard/dec-app-cutoff-v3.md, application-scorecard/dec-app-rebuild-v4.md, application-scorecard/dec-app-cutoff-v4.md, application-scorecard/dec-app-no-gbm.md

## Q4
The note in force at the end of the line is cr-lgbm-v3, which replaced cr-lgbm-v2 and cr-lgbm-v1. It is built directly on cr-lgbm-v2, ds-cr-intent-labels, exp-106 and fnd-cr-threshold.
Notes: call-center-routing/cr-lgbm-v3.md, call-center-routing/cr-lgbm-v2.md, call-center-routing/ds-cr-intent-labels.md, call-center-routing/exp-106.md, call-center-routing/fnd-cr-threshold.md

## Q5
Only one note from another project was built directly on churn-gbm-2025-v2: feat-ror-churn-score in retention-offers-roi, which scores with that model.
Notes: retention-offers-roi/feat-ror-churn-score.md

## Q6
app-gbm-v2 rests on two dataset notes: ds-app-applications-2024 (directly through app-gbm-v1 and the feature and experiment chain) and ds-app-reject-sample (through exp-501 and find-app-reject-inference-gain).
Notes: application-scorecard/app-gbm-v2.md, application-scorecard/ds-app-applications-2024.md, application-scorecard/ds-app-reject-sample.md

## Q7
Both models build directly on feat-csb-spend-raw and feat-csb-tenure-band.
Notes: churn-small-business/csb-lr-base.md, churn-small-business/csb-xgb-v1.md, churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-tenure-band.md

## Q8
Only churn-lr-base-2025 qualifies: it is still current and builds directly on feat-c25-util-v1, which feat-c25-util-v2 replaced. churn-gbm-2025-v2 builds on no replaced feature or dataset note.
Notes: churn-2025/churn-lr-base-2025.md, churn-2025/feat-c25-util-v1.md

## Q9
Five decisions rest on ds-bt-offer-log, directly or through other notes: dec-bt-drop-post-offer-features, dec-bt-cut-mailer-top30 and dec-bt-margin-label in balance-transfer-propensity, and dec-pa-6m-default and dec-pa-no-12m-subprime in promo-apr-test.
Notes: balance-transfer-propensity/ds-bt-offer-log.md, balance-transfer-propensity/dec-bt-drop-post-offer-features.md, balance-transfer-propensity/dec-bt-cut-mailer-top30.md, balance-transfer-propensity/dec-bt-margin-label.md, promo-apr-test/dec-pa-6m-default.md, promo-apr-test/dec-pa-no-12m-subprime.md

## Q10
The note in force at the end of the line is dec-cb-threshold-2500, which replaced dec-cb-adopt-banded-tiers and dec-cb-extend-flat-pilot. It is built directly on dec-cb-adopt-banded-tiers, exp-206-breakeven-sim and find-cb-breakeven-lift.
Notes: cashback-redesign/dec-cb-threshold-2500.md, cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/exp-206-breakeven-sim.md, cashback-redesign/find-cb-breakeven-lift.md