## Q1
Both models build directly on feat-c25-payment-behaviour and feat-c25-txn-recency. Those are the only feature notes that appear in both notes' build lists.
Notes: churn-2025/churn-gbm-2025-v2.md, churn-2025/churn-lr-base-2025.md, churn-2025/feat-c25-payment-behaviour.md, churn-2025/feat-c25-txn-recency.md

## Q2
None. The only replaced feature in this project is feat-cb-spend-base, and no current model builds directly on it. cb-elasticity-v1, which did, is replaced by cb-elasticity-v2.
Notes: cashback-redesign/cb-elasticity-v2.md, cashback-redesign/cb-sim-v1.md, cashback-redesign/feat-cb-spend-band-v2.md

## Q3
Four decision notes rest on feat-app-util-new, all through other notes: dec-app-cutoff-v3, dec-app-no-gbm, dec-app-rebuild-v4 and dec-app-cutoff-v4. None of them builds on it directly.
Notes: application-scorecard/dec-app-cutoff-v3.md, application-scorecard/dec-app-no-gbm.md, application-scorecard/dec-app-rebuild-v4.md, application-scorecard/dec-app-cutoff-v4.md

## Q4
cr-lgbm-v3 is the note in force now. It builds on cr-lgbm-v2, ds-cr-intent-labels, exp-106 and fnd-cr-threshold.
Notes: call-center-routing/cr-lgbm-v3.md, call-center-routing/cr-lgbm-v2.md, call-center-routing/ds-cr-intent-labels.md, call-center-routing/exp-106.md, call-center-routing/fnd-cr-threshold.md

## Q5
Only one note in another project is built directly on churn-gbm-2025-v2: retention-offers-roi/feat-ror-churn-score, which scores the October 2025 snapshot with it.
Notes: retention-offers-roi/feat-ror-churn-score.md

## Q6
app-gbm-v2 rests on two dataset notes: ds-app-applications-2024 and ds-app-reject-sample.
Notes: application-scorecard/ds-app-applications-2024.md, application-scorecard/ds-app-reject-sample.md

## Q7
Both build directly on feat-csb-spend-raw and feat-csb-tenure-band.
Notes: churn-small-business/csb-lr-base.md, churn-small-business/csb-xgb-v1.md, churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-tenure-band.md

## Q8
churn-lr-base-2025 is the only current model that builds directly on a replaced feature: feat-c25-util-v1, which is superseded by feat-c25-util-v2.
Notes: churn-2025/churn-lr-base-2025.md, churn-2025/feat-c25-util-v1.md

## Q9
Five decision notes rest on ds-bt-offer-log, all through other notes: dec-bt-drop-post-offer-features and dec-bt-cut-mailer-top30 in balance-transfer-propensity, dec-bt-margin-label in the same project, and dec-pa-6m-default and dec-pa-no-12m-subprime in promo-apr-test.
Notes: balance-transfer-propensity/dec-bt-drop-post-offer-features.md, balance-transfer-propensity/dec-bt-cut-mailer-top30.md, balance-transfer-propensity/dec-bt-margin-label.md, promo-apr-test/dec-pa-6m-default.md, promo-apr-test/dec-pa-no-12m-subprime.md

## Q10
dec-cb-threshold-2500 is in force now. It builds on dec-cb-adopt-banded-tiers, exp-206-breakeven-sim and find-cb-breakeven-lift.
Notes: cashback-redesign/dec-cb-threshold-2500.md, cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/exp-206-breakeven-sim.md, cashback-redesign/find-cb-breakeven-lift.md