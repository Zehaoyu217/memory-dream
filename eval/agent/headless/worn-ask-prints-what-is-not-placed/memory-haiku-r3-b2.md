## Q1
Both notes build directly on feat-c25-payment-behaviour and feat-c25-txn-recency. The other feature each one uses (util-v2 for the GBM, util-v1 for the LR baseline) is different.
Notes: churn-2025/feat-c25-payment-behaviour.md, churn-2025/feat-c25-txn-recency.md

## Q2
cb-uplift-v1 is still current and builds directly on feat-cb-spend-base, which was replaced by feat-cb-spend-band-v2. The other current models (cb-elasticity-v2, cb-sim-v1) build on no replaced feature or dataset.
Notes: cashback-redesign/cb-uplift-v1.md, cashback-redesign/feat-cb-spend-base.md, cashback-redesign/feat-cb-spend-band-v2.md

## Q3
Four decisions rest on feat-app-util-new: dec-app-cutoff-v3, dec-app-no-gbm, dec-app-rebuild-v4 and dec-app-cutoff-v4. The tool's count of 16 dependent notes matches this list.
Notes: application-scorecard/dec-app-cutoff-v3.md, application-scorecard/dec-app-no-gbm.md, application-scorecard/dec-app-rebuild-v4.md, application-scorecard/dec-app-cutoff-v4.md

## Q4
cr-lgbm-v3 is in force, after cr-lgbm-v1 was replaced by cr-lgbm-v2 and then cr-lgbm-v2 by cr-lgbm-v3. It is built on cr-lgbm-v2, ds-cr-intent-labels, exp-106 and fnd-cr-threshold.
Notes: call-center-routing/cr-lgbm-v3.md, call-center-routing/cr-lgbm-v2.md, call-center-routing/ds-cr-intent-labels.md, call-center-routing/exp-106.md, call-center-routing/fnd-cr-threshold.md

## Q5
Only one note from another project builds directly on churn-gbm-2025-v2: feat-ror-churn-score in retention-offers-roi, which scores with it.
Notes: retention-offers-roi/feat-ror-churn-score.md

## Q6
app-gbm-v2 rests on two dataset notes: ds-app-applications-2024 (through app-gbm-v1, feat-app-util-new, feat-app-velocity-apps and app-scorecard-v3) and ds-app-reject-sample (through exp-501).
Notes: application-scorecard/ds-app-applications-2024.md, application-scorecard/ds-app-reject-sample.md

## Q7
csb-lr-base and csb-xgb-v1 both build directly on feat-csb-spend-raw and feat-csb-tenure-band.
Notes: churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-tenure-band.md

## Q8
Only churn-lr-base-2025 qualifies. It is not superseded and builds directly on feat-c25-util-v1, which was replaced by feat-c25-util-v2.
Notes: churn-2025/churn-lr-base-2025.md, churn-2025/feat-c25-util-v1.md, churn-2025/feat-c25-util-v2.md

## Q9
Five decisions rest on ds-bt-offer-log: dec-bt-drop-post-offer-features, dec-bt-cut-mailer-top30 and dec-bt-margin-label in balance-transfer-propensity, and dec-pa-6m-default and dec-pa-no-12m-subprime in promo-apr-test. dec-bt-margin-label reaches it through exp-107-margin-label and bt-xgb-v2.
Notes: balance-transfer-propensity/dec-bt-drop-post-offer-features.md, balance-transfer-propensity/dec-bt-cut-mailer-top30.md, balance-transfer-propensity/dec-bt-margin-label.md, promo-apr-test/dec-pa-6m-default.md, promo-apr-test/dec-pa-no-12m-subprime.md

## Q10
dec-cb-threshold-2500 is in force, after dec-cb-extend-flat-pilot was replaced by dec-cb-adopt-banded-tiers and that was replaced by dec-cb-threshold-2500. It is built on dec-cb-adopt-banded-tiers, exp-206-breakeven-sim and find-cb-breakeven-lift.
Notes: cashback-redesign/dec-cb-threshold-2500.md, cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/exp-206-breakeven-sim.md, cashback-redesign/find-cb-breakeven-lift.md