## Q1
Both build directly on feat-c25-payment-behaviour and feat-c25-txn-recency. churn-gbm-2025-v2 also uses feat-c25-util-v2, and churn-lr-base-2025 also uses feat-c25-app-sessions and feat-c25-util-v1.
Notes: churn-2025/feat-c25-payment-behaviour.md, churn-2025/feat-c25-txn-recency.md

## Q2
cb-uplift-v1 is still current and builds directly on feat-cb-spend-base, which feat-cb-spend-band-v2 has replaced. The other current models (cb-elasticity-v2, cb-sim-v1) build only on current features and datasets.
Notes: cashback-redesign/cb-uplift-v1.md

## Q3
Four decision notes rest on feat-app-util-new: dec-app-cutoff-v3, dec-app-no-gbm, dec-app-rebuild-v4 and dec-app-cutoff-v4. They reach it through app-scorecard-v3, app-gbm-v1 and app-gbm-v2 and the notes built on them.
Notes: application-scorecard/dec-app-cutoff-v3.md, application-scorecard/dec-app-no-gbm.md, application-scorecard/dec-app-rebuild-v4.md, application-scorecard/dec-app-cutoff-v4.md

## Q4
cr-lgbm-v3 is in force at the end of the line. It is built directly on cr-lgbm-v2, ds-cr-intent-labels, exp-106 and fnd-cr-threshold.
Notes: call-center-routing/cr-lgbm-v3.md, call-center-routing/cr-lgbm-v2.md, call-center-routing/ds-cr-intent-labels.md, call-center-routing/exp-106.md, call-center-routing/fnd-cr-threshold.md

## Q5
Only feat-ror-churn-score builds directly on churn-gbm-2025-v2. ror-uplift-v1 uses that score as an input but does not list it under "Builds on", so I have not counted it as a direct build.
Notes: retention-offers-roi/feat-ror-churn-score.md

## Q6
app-gbm-v2 rests on two dataset notes: ds-app-applications-2024 and ds-app-reject-sample.
Notes: application-scorecard/ds-app-applications-2024.md, application-scorecard/ds-app-reject-sample.md

## Q7
Both csb-lr-base and csb-xgb-v1 build directly on feat-csb-spend-raw and feat-csb-tenure-band.
Notes: churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-tenure-band.md

## Q8
churn-lr-base-2025 is the only current model that builds directly on a replaced feature. It uses feat-c25-util-v1, which feat-c25-util-v2 has replaced.
Notes: churn-2025/churn-lr-base-2025.md, churn-2025/feat-c25-util-v1.md

## Q9
Five decision notes rest on ds-bt-offer-log: dec-bt-drop-post-offer-features, dec-bt-cut-mailer-top30, dec-bt-margin-label, dec-pa-6m-default and dec-pa-no-12m-subprime. The last two are in the promo-apr-test project.
Notes: balance-transfer-propensity/dec-bt-drop-post-offer-features.md, balance-transfer-propensity/dec-bt-cut-mailer-top30.md, balance-transfer-propensity/dec-bt-margin-label.md, promo-apr-test/dec-pa-6m-default.md, promo-apr-test/dec-pa-no-12m-subprime.md

## Q10
dec-cb-threshold-2500 is in force at the end of the line. It is built directly on dec-cb-adopt-banded-tiers, exp-206-breakeven-sim and find-cb-breakeven-lift.
Notes: cashback-redesign/dec-cb-threshold-2500.md, cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/exp-206-breakeven-sim.md, cashback-redesign/find-cb-breakeven-lift.md