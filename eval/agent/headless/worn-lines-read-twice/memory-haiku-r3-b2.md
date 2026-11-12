## Q1
Both notes build directly on feat-c25-payment-behaviour and feat-c25-txn-recency. churn-gbm-2025-v2 also uses feat-c25-util-v2, and churn-lr-base-2025 uses feat-c25-util-v1 and feat-c25-app-sessions instead.
Notes: churn-2025/churn-gbm-2025-v2.md, churn-2025/churn-lr-base-2025.md, churn-2025/feat-c25-payment-behaviour.md, churn-2025/feat-c25-txn-recency.md

## Q2
Only cb-uplift-v1 fits. It is still current and builds directly on feat-cb-spend-base, which feat-cb-spend-band-v2 replaced. The other current models (cb-elasticity-v2, cb-sim-v1) build on notes that are not replaced. cb-elasticity-v1 also used feat-cb-spend-base, but v2 replaces it.
Notes: cashback-redesign/cb-uplift-v1.md, cashback-redesign/feat-cb-spend-base.md, cashback-redesign/feat-cb-spend-band-v2.md

## Q3
Four decisions rest on feat-app-util-new: dec-app-cutoff-v3, dec-app-no-gbm, dec-app-rebuild-v4 and dec-app-cutoff-v4. They reach it through app-scorecard-v3 and the models and experiments built on it.
Notes: application-scorecard/dec-app-cutoff-v3.md, application-scorecard/dec-app-no-gbm.md, application-scorecard/dec-app-rebuild-v4.md, application-scorecard/dec-app-cutoff-v4.md, application-scorecard/feat-app-util-new.md

## Q4
The line ends at cr-lgbm-v3, which is in force now. It builds directly on cr-lgbm-v2, ds-cr-intent-labels, exp-106 and fnd-cr-threshold, and through them on the cost-matrix finding and the caller-history v2 feature.
Notes: call-center-routing/cr-lgbm-v3.md, call-center-routing/cr-lgbm-v2.md, call-center-routing/ds-cr-intent-labels.md, call-center-routing/exp-106.md, call-center-routing/fnd-cr-threshold.md

## Q5
Only one note in another project is built directly on churn-gbm-2025-v2: retention-offers-roi/feat-ror-churn-score, which scores the October 2025 snapshot with it. The other notes that rest on it do so only through that feature.
Notes: retention-offers-roi/feat-ror-churn-score.md, churn-2025/churn-gbm-2025-v2.md

## Q6
app-gbm-v2 rests on two dataset notes: ds-app-applications-2024 and ds-app-reject-sample. It gets there through app-gbm-v1, exp-501, feat-app-util-new, feat-app-thin-file, feat-app-velocity-apps and the reject-inference question.
Notes: application-scorecard/app-gbm-v2.md, application-scorecard/ds-app-applications-2024.md, application-scorecard/ds-app-reject-sample.md

## Q7
Both notes build directly on feat-csb-spend-raw and feat-csb-tenure-band. csb-lr-base also uses ds-csb-churn-labels and ds-csb-oot-2025q1, and csb-xgb-v1 also uses feat-csb-deposit-volatility and dec-csb-tenure-floor.
Notes: churn-small-business/csb-lr-base.md, churn-small-business/csb-xgb-v1.md, churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-tenure-band.md

## Q8
Only churn-lr-base-2025 fits. It is a current model that builds directly on feat-c25-util-v1, which feat-c25-util-v2 replaced. churn-gbm-2025-v2 is current too, but its features are all current.
Notes: churn-2025/churn-lr-base-2025.md, churn-2025/feat-c25-util-v1.md, churn-2025/feat-c25-util-v2.md

## Q9
Five decisions rest on ds-bt-offer-log: dec-bt-drop-post-offer-features, dec-bt-cut-mailer-top30 and dec-bt-margin-label in balance-transfer-propensity, and dec-pa-6m-default and dec-pa-no-12m-subprime in promo-apr-test. They reach it through the bureau and holdout datasets, the bt-xgb models and the margin experiments.
Notes: balance-transfer-propensity/dec-bt-drop-post-offer-features.md, balance-transfer-propensity/dec-bt-cut-mailer-top30.md, balance-transfer-propensity/dec-bt-margin-label.md, promo-apr-test/dec-pa-6m-default.md, promo-apr-test/dec-pa-no-12m-subprime.md, balance-transfer-propensity/ds-bt-offer-log.md

## Q10
The line ends at dec-cb-threshold-2500, which is in force now. It builds directly on dec-cb-adopt-banded-tiers, exp-206-breakeven-sim and find-cb-breakeven-lift, and through them on cb-elasticity-v2, find-cb-band-elasticity, cb-sim-v1 and q-cb-breakeven-lift.
Notes: cashback-redesign/dec-cb-threshold-2500.md, cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/exp-206-breakeven-sim.md, cashback-redesign/find-cb-breakeven-lift.md