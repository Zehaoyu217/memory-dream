## Q1
Both models build directly on feat-c25-payment-behaviour and feat-c25-txn-recency. churn-gbm-2025-v2 also uses feat-c25-util-v2, and churn-lr-base-2025 uses feat-c25-util-v1 and feat-c25-app-sessions.
Notes: churn-2025/churn-gbm-2025-v2.md, churn-2025/churn-lr-base-2025.md, churn-2025/feat-c25-payment-behaviour.md, churn-2025/feat-c25-txn-recency.md

## Q2
cb-uplift-v1 is the only current model that builds on a replaced feature: it uses feat-cb-spend-base, which feat-cb-spend-band-v2 replaced. cb-elasticity-v1 also uses feat-cb-spend-base, but it is superseded by cb-elasticity-v2, so it does not count.
Notes: cashback-redesign/cb-uplift-v1.md, cashback-redesign/feat-cb-spend-band-v2.md

## Q3
Four decision notes rest on feat-app-util-new: dec-app-cutoff-v3, dec-app-no-gbm, dec-app-rebuild-v4 and dec-app-cutoff-v4. All four reach it through other notes, not directly.
Notes: application-scorecard/feat-app-util-new.md, application-scorecard/dec-app-cutoff-v3.md, application-scorecard/dec-app-no-gbm.md, application-scorecard/dec-app-rebuild-v4.md, application-scorecard/dec-app-cutoff-v4.md

## Q4
The note in force is cr-lgbm-v3, which replaced cr-lgbm-v2 (itself a replacement for cr-lgbm-v1). cr-lgbm-v3 is built on cr-lgbm-v2, ds-cr-intent-labels, exp-106 and fnd-cr-threshold.
Notes: call-center-routing/cr-lgbm-v1.md, call-center-routing/cr-lgbm-v2.md, call-center-routing/cr-lgbm-v3.md, call-center-routing/ds-cr-intent-labels.md, call-center-routing/exp-106.md, call-center-routing/fnd-cr-threshold.md

## Q5
Only one note from another project is built directly on churn-gbm-2025-v2: retention-offers-roi/feat-ror-churn-score, which scores with it. Other folders reach it only through that note.
Notes: retention-offers-roi/feat-ror-churn-score.md, churn-2025/churn-gbm-2025-v2.md

## Q6
app-gbm-v2 rests on two dataset notes: ds-app-applications-2024 and ds-app-reject-sample. It gets there through app-gbm-v1, find-app-reject-inference-gain, exp-501, feat-app-util-new, feat-app-velocity-apps, feat-app-thin-file and q-app-reject-inference.
Notes: application-scorecard/app-gbm-v2.md, application-scorecard/ds-app-applications-2024.md, application-scorecard/ds-app-reject-sample.md

## Q7
Both models build directly on feat-csb-spend-raw and feat-csb-tenure-band.
Notes: churn-small-business/csb-lr-base.md, churn-small-business/csb-xgb-v1.md, churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-tenure-band.md

## Q8
churn-lr-base-2025 is the only current model that builds directly on a replaced feature. It uses feat-c25-util-v1, which feat-c25-util-v2 replaced. churn-gbm-2025-v2 uses only current features.
Notes: churn-2025/churn-lr-base-2025.md, churn-2025/feat-c25-util-v1.md

## Q9
Five decision notes rest on ds-bt-offer-log: dec-bt-drop-post-offer-features, dec-bt-cut-mailer-top30, dec-bt-margin-label, dec-pa-6m-default and dec-pa-no-12m-subprime. The last two are in the promo-apr-test folder.
Notes: balance-transfer-propensity/dec-bt-drop-post-offer-features.md, balance-transfer-propensity/dec-bt-cut-mailer-top30.md, balance-transfer-propensity/dec-bt-margin-label.md, promo-apr-test/dec-pa-6m-default.md, promo-apr-test/dec-pa-no-12m-subprime.md

## Q10
The note in force is dec-cb-threshold-2500, which replaced dec-cb-adopt-banded-tiers (itself a replacement for dec-cb-extend-flat-pilot). dec-cb-threshold-2500 is built on dec-cb-adopt-banded-tiers, exp-206-breakeven-sim and find-cb-breakeven-lift.
Notes: cashback-redesign/dec-cb-extend-flat-pilot.md, cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/dec-cb-threshold-2500.md, cashback-redesign/exp-206-breakeven-sim.md, cashback-redesign/find-cb-breakeven-lift.md