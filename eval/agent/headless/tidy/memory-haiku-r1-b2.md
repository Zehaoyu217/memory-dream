## Q1
Both models build directly on feat-c25-txn-recency and feat-c25-payment-behaviour. churn-gbm-2025-v2 also uses feat-c25-util-v2, and churn-lr-base-2025 also uses feat-c25-util-v1 and feat-c25-app-sessions.
Notes: churn-2025/churn-gbm-2025-v2.md, churn-2025/churn-lr-base-2025.md, churn-2025/feat-c25-txn-recency.md, churn-2025/feat-c25-payment-behaviour.md

## Q2
None. The only current model in cashback-redesign, cb-elasticity-v2, builds on feat-cb-spend-band-v2 and feat-cb-grocery-share, and neither is replaced. Its other direct input is the superseded model cb-elasticity-v1, which is a model rather than a feature or dataset.
Notes: cashback-redesign/cb-elasticity-v2.md, cashback-redesign/feat-cb-grocery-share.md

## Q3
Four decisions rest on feat-app-util-new: dec-app-cutoff-v3 and dec-app-no-gbm and dec-app-rebuild-v4 and dec-app-cutoff-v4. None builds on it directly; each reaches it through app-scorecard-v3, app-gbm-v1, app-gbm-v2 or app-scorecard-v4.
Notes: application-scorecard/feat-app-util-new.md, application-scorecard/dec-app-cutoff-v3.md, application-scorecard/dec-app-no-gbm.md, application-scorecard/dec-app-rebuild-v4.md, application-scorecard/dec-app-cutoff-v4.md

## Q4
cr-lgbm-v3 is in force; it replaced cr-lgbm-v2, which had replaced cr-lgbm-v1. cr-lgbm-v3 is built on cr-lgbm-v2, fnd-cr-threshold, ds-cr-intent-labels and exp-106.
Notes: call-center-routing/cr-lgbm-v3.md, call-center-routing/cr-lgbm-v2.md, call-center-routing/fnd-cr-threshold.md, call-center-routing/ds-cr-intent-labels.md, call-center-routing/exp-106.md

## Q5
Only one note: feat-ror-churn-score, which scores customers with churn-gbm-2025-v2 in the retention-offers-roi project.
Notes: retention-offers-roi/feat-ror-churn-score.md

## Q6
app-gbm-v2 rests on two dataset notes: ds-app-applications-2024, which is the base for the project, and ds-app-reject-sample, which feeds the reject-inference step.
Notes: application-scorecard/ds-app-applications-2024.md, application-scorecard/ds-app-reject-sample.md

## Q7
Both build directly on feat-csb-spend-raw and feat-csb-tenure-band.
Notes: churn-small-business/csb-lr-base.md, churn-small-business/csb-xgb-v1.md, churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-tenure-band.md

## Q8
churn-lr-base-2025 is the only one. It is still current and builds directly on feat-c25-util-v1, which was replaced by feat-c25-util-v2. churn-gbm-2025-v2 builds only on current inputs.
Notes: churn-2025/churn-lr-base-2025.md, churn-2025/feat-c25-util-v1.md, churn-2025/feat-c25-util-v2.md

## Q9
Five decisions rest on ds-bt-offer-log: dec-bt-drop-post-offer-features, dec-bt-cut-mailer-top30 and dec-bt-margin-label in balance-transfer-propensity, plus dec-pa-6m-default and dec-pa-no-12m-subprime in promo-apr-test. Each reaches it through the datasets, features and models built on it.
Notes: balance-transfer-propensity/ds-bt-offer-log.md, balance-transfer-propensity/dec-bt-drop-post-offer-features.md, balance-transfer-propensity/dec-bt-cut-mailer-top30.md, balance-transfer-propensity/dec-bt-margin-label.md, promo-apr-test/dec-pa-6m-default.md, promo-apr-test/dec-pa-no-12m-subprime.md

## Q10
dec-cb-threshold-2500 is in force; it replaced dec-cb-adopt-banded-tiers, which had replaced dec-cb-extend-flat-pilot. dec-cb-threshold-2500 is built on find-cb-breakeven-lift, exp-206-breakeven-sim and dec-cb-adopt-banded-tiers.
Notes: cashback-redesign/dec-cb-threshold-2500.md, cashback-redesign/find-cb-breakeven-lift.md, cashback-redesign/exp-206-breakeven-sim.md, cashback-redesign/dec-cb-adopt-banded-tiers.md