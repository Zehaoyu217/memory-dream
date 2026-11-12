## Q1
Both models build directly on `feat-c25-payment-behaviour` and `feat-c25-txn-recency`. Each also has its own other inputs: churn-gbm-2025-v2 uses util-v2 and the app-session drop decision, and churn-lr-base-2025 uses util-v1 and the app-session feature.
Notes: churn-2025/churn-gbm-2025-v2.md, churn-2025/churn-lr-base-2025.md, churn-2025/feat-c25-payment-behaviour.md, churn-2025/feat-c25-txn-recency.md

## Q2
`cb-uplift-v1` is still current (no supersede marker) but builds directly on `feat-cb-spend-base`, which was replaced by `feat-cb-spend-band-v2`. No other current cashback model builds on a replaced feature or dataset.
Notes: cashback-redesign/cb-uplift-v1.md, cashback-redesign/feat-cb-spend-base.md

## Q3
Directly, `app-scorecard-v3` rests on `feat-app-util-new`. Through the chain, four decisions rest on it: `dec-app-cutoff-v3`, `dec-app-no-gbm`, `dec-app-rebuild-v4` and `dec-app-cutoff-v4`.
Notes: application-scorecard/feat-app-util-new.md, application-scorecard/app-scorecard-v3.md, application-scorecard/dec-app-cutoff-v3.md, application-scorecard/dec-app-no-gbm.md, application-scorecard/dec-app-rebuild-v4.md, application-scorecard/dec-app-cutoff-v4.md

## Q4
The line runs cr-lgbm-v1 → cr-lgbm-v2 → cr-lgbm-v3, so `cr-lgbm-v3` is in force. It builds on `cr-lgbm-v2`, `ds-cr-intent-labels`, `exp-106` and `fnd-cr-threshold`.
Notes: call-center-routing/cr-lgbm-v3.md, call-center-routing/cr-lgbm-v2.md, call-center-routing/ds-cr-intent-labels.md, call-center-routing/exp-106.md, call-center-routing/fnd-cr-threshold.md

## Q5
Only one note in another project builds directly on `churn-gbm-2025-v2`: `feat-ror-churn-score` in retention-offers-roi.
Notes: retention-offers-roi/feat-ror-churn-score.md

## Q6
`app-gbm-v2` rests on two dataset notes: `ds-app-applications-2024` (directly through feat-app-util-new, feat-app-velocity-apps and the v3 chain) and `ds-app-reject-sample` (through exp-501 and q-app-reject-inference).
Notes: application-scorecard/app-gbm-v2.md, application-scorecard/ds-app-applications-2024.md, application-scorecard/ds-app-reject-sample.md

## Q7
Both models build directly on `feat-csb-spend-raw` and `feat-csb-tenure-band`.
Notes: churn-small-business/csb-lr-base.md, churn-small-business/csb-xgb-v1.md, churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-tenure-band.md

## Q8
`churn-lr-base-2025` is still current (no supersede marker) but builds directly on `feat-c25-util-v1`, which was replaced by `feat-c25-util-v2`. No other current churn-2025 model builds on a replaced feature or dataset.
Notes: churn-2025/churn-lr-base-2025.md, churn-2025/feat-c25-util-v1.md

## Q9
Three decisions in balance-transfer-propensity rest directly or through the chain on `ds-bt-offer-log`: `dec-bt-drop-post-offer-features`, `dec-bt-cut-mailer-top30` and `dec-bt-margin-label`. Two promo-apr-test decisions also rest on it: `dec-pa-6m-default` and `dec-pa-no-12m-subprime`.
Notes: balance-transfer-propensity/ds-bt-offer-log.md, balance-transfer-propensity/dec-bt-drop-post-offer-features.md, balance-transfer-propensity/dec-bt-cut-mailer-top30.md, balance-transfer-propensity/dec-bt-margin-label.md, promo-apr-test/dec-pa-6m-default.md, promo-apr-test/dec-pa-no-12m-subprime.md

## Q10
The line runs dec-cb-extend-flat-pilot → dec-cb-adopt-banded-tiers → dec-cb-threshold-2500, so `dec-cb-threshold-2500` is in force. It builds on `dec-cb-adopt-banded-tiers`, `exp-206-breakeven-sim` and `find-cb-breakeven-lift`.
Notes: cashback-redesign/dec-cb-threshold-2500.md, cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/exp-206-breakeven-sim.md, cashback-redesign/find-cb-breakeven-lift.md, cashback-redesign/dec-cb-extend-flat-pilot.md