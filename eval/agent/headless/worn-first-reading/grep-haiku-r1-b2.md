## Q1
Both notes build directly on feat-c25-payment-behaviour and feat-c25-txn-recency. Neither shares the other features: churn-gbm-2025-v2 uses util-v2 and the LR baseline uses util-v1.
Notes: churn-2025/churn-gbm-2025-v2.md, churn-2025/churn-lr-base-2025.md, churn-2025/feat-c25-payment-behaviour.md, churn-2025/feat-c25-txn-recency.md

## Q2
cb-uplift-v1 is still current and builds directly on feat-cb-spend-base, which was replaced by feat-cb-spend-band-v2.
Notes: cashback-redesign/cb-uplift-v1.md, cashback-redesign/feat-cb-spend-base.md, cashback-redesign/feat-cb-spend-band-v2.md

## Q3
Four decision notes rest on feat-app-util-new. It feeds app-scorecard-v3 directly, and the chain runs through exp-506, find-app-income-lift and exp-503/exp-504 down to app-gbm-v1 and app-gbm-v2, which build on app-scorecard-v3.
Notes: application-scorecard/dec-app-cutoff-v3.md, application-scorecard/dec-app-cutoff-v4.md, application-scorecard/dec-app-no-gbm.md, application-scorecard/dec-app-rebuild-v4.md

## Q4
The note in force is cr-lgbm-v3, which replaced cr-lgbm-v2 and that had replaced cr-lgbm-v1. cr-lgbm-v3 builds on cr-lgbm-v2, ds-cr-intent-labels, exp-106 and the cost-matrix misroute finding fnd-cr-threshold.
Notes: call-center-routing/cr-lgbm-v3.md, call-center-routing/cr-lgbm-v2.md, call-center-routing/ds-cr-intent-labels.md, call-center-routing/exp-106.md, call-center-routing/fnd-cr-threshold.md

## Q5
Only feat-ror-churn-score builds directly on churn-2025/churn-gbm-2025-v2. ror-uplift-v1 uses that score only indirectly, through feat-ror-churn-score.
Notes: retention-offers-roi/feat-ror-churn-score.md

## Q6
app-gbm-v2 rests on app-gbm-v1 and find-app-reject-inference-gain. Following those back gives two dataset notes: ds-app-applications-2024 (via app-scorecard-v3, feat-app-thin-file, feat-app-velocity-apps and exp-501) and ds-app-reject-sample (via exp-501).
Notes: application-scorecard/ds-app-applications-2024.md, application-scorecard/ds-app-reject-sample.md

## Q7
Both csb-lr-base and csb-xgb-v1 build directly on feat-csb-spend-raw and feat-csb-tenure-band.
Notes: churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-tenure-band.md

## Q8
churn-lr-base-2025 is still current, as the monitoring challenger, and builds directly on feat-c25-util-v1, which was replaced by feat-c25-util-v2. churn-gbm-2025-v2 builds only on current features.
Notes: churn-2025/churn-lr-base-2025.md, churn-2025/feat-c25-util-v1.md, churn-2025/feat-c25-util-v2.md

## Q9
Three decision notes rest on ds-bt-offer-log, directly or through other notes. dec-bt-cut-mailer-top30 and dec-bt-margin-label reach it through bt-xgb-v2 and feat-bt-revolve-share. dec-bt-drop-post-offer-features reaches it through find-bt-limit-leak and exp-104.
Notes: balance-transfer-propensity/dec-bt-cut-mailer-top30.md, balance-transfer-propensity/dec-bt-drop-post-offer-features.md, balance-transfer-propensity/dec-bt-margin-label.md

## Q10
The note in force is dec-cb-threshold-2500, which replaced dec-cb-adopt-banded-tiers. That in turn replaced dec-cb-extend-flat-pilot. dec-cb-threshold-2500 builds on dec-cb-adopt-banded-tiers, exp-206-breakeven-sim and find-cb-breakeven-lift.
Notes: cashback-redesign/dec-cb-threshold-2500.md, cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/exp-206-breakeven-sim.md, cashback-redesign/find-cb-breakeven-lift.md