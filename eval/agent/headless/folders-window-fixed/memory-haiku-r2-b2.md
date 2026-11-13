## Q1
Both notes build directly on feat-c25-payment-behaviour and feat-c25-txn-recency. churn-gbm-2025-v2 also uses feat-c25-util-v2, and churn-lr-base-2025 uses feat-c25-util-v1 and feat-c25-app-sessions.
Notes: churn-2025/feat-c25-payment-behaviour.md, churn-2025/feat-c25-txn-recency.md

## Q2
Only cb-uplift-v1 is a current model (it has no replacement marker) that builds directly on a replaced feature, feat-cb-spend-base, which was replaced by feat-cb-spend-band-v2. cb-elasticity-v1 also builds on feat-cb-spend-base, but it is itself replaced by cb-elasticity-v2, so it is excluded.
Notes: cashback-redesign/cb-uplift-v1.md

## Q3
Four decision notes rest on feat-app-util-new: dec-app-cutoff-v3 and dec-app-cutoff-v4, dec-app-no-gbm, and dec-app-rebuild-v4. They reach it through app-scorecard-v3 and the GBM and experiment chain.
Notes: application-scorecard/dec-app-cutoff-v3.md, application-scorecard/dec-app-cutoff-v4.md, application-scorecard/dec-app-no-gbm.md, application-scorecard/dec-app-rebuild-v4.md

## Q4
cr-lgbm-v3 is in force now; cr-lgbm-v1 was replaced by cr-lgbm-v2, which was replaced by cr-lgbm-v3. cr-lgbm-v3 builds directly on cr-lgbm-v2, ds-cr-intent-labels, exp-106 and fnd-cr-threshold.
Notes: call-center-routing/cr-lgbm-v3.md, call-center-routing/cr-lgbm-v2.md, call-center-routing/ds-cr-intent-labels.md, call-center-routing/exp-106.md, call-center-routing/fnd-cr-threshold.md

## Q5
Only feat-ror-churn-score in retention-offers-roi builds directly on churn-gbm-2025-v2. ror-uplift-v1 mentions it, but it builds on feat-ror-churn-score rather than on the model itself.
Notes: retention-offers-roi/feat-ror-churn-score.md

## Q6
app-gbm-v2 rests on two dataset notes, ds-app-applications-2024 and ds-app-reject-sample, directly or through app-gbm-v1, app-scorecard-v3, exp-501, and the other notes in its chain.
Notes: application-scorecard/ds-app-applications-2024.md, application-scorecard/ds-app-reject-sample.md

## Q7
Both models build directly on feat-csb-spend-raw and feat-csb-tenure-band. csb-xgb-v1 also uses feat-csb-deposit-volatility, which csb-lr-base does not.
Notes: churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-tenure-band.md

## Q8
churn-lr-base-2025 is the only current churn-2025 model that builds directly on a replaced feature: feat-c25-util-v1, which was replaced by feat-c25-util-v2. churn-gbm-2025-v2 builds only on current inputs, and churn-gbm-2025 is superseded.
Notes: churn-2025/churn-lr-base-2025.md

## Q9
Three decision notes rest on ds-bt-offer-log: dec-bt-drop-post-offer-features, dec-bt-cut-mailer-top30, and dec-bt-margin-label. dec-bt-margin-label reaches it through exp-107-margin-label and bt-xgb-v2. A note in this folder names an unplaced input, so the memory cannot fully confirm it, but the chain through bt-xgb-v2 supports it.
Notes: balance-transfer-propensity/dec-bt-drop-post-offer-features.md, balance-transfer-propensity/dec-bt-cut-mailer-top30.md, balance-transfer-propensity/dec-bt-margin-label.md

## Q10
dec-cb-threshold-2500 is in force; dec-cb-extend-flat-pilot was replaced by dec-cb-adopt-banded-tiers, which was replaced by dec-cb-threshold-2500. dec-cb-threshold-2500 builds directly on dec-cb-adopt-banded-tiers, exp-206-breakeven-sim and find-cb-breakeven-lift.
Notes: cashback-redesign/dec-cb-threshold-2500.md, cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/exp-206-breakeven-sim.md, cashback-redesign/find-cb-breakeven-lift.md