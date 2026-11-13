## Q1
Both `churn-gbm-2025-v2` and `churn-lr-base-2025` build directly on `feat-c25-payment-behaviour` and `feat-c25-txn-recency`.
Notes: churn-2025/churn-gbm-2025-v2.md, churn-2025/churn-lr-base-2025.md, churn-2025/feat-c25-payment-behaviour.md, churn-2025/feat-c25-txn-recency.md

## Q2
`cb-uplift-v1` is the only current model that builds directly on a replaced feature or dataset: it uses `feat-cb-spend-base`, which `feat-cb-spend-band-v2` replaced.
Notes: cashback-redesign/cb-uplift-v1.md, cashback-redesign/feat-cb-spend-band-v2.md

## Q3
Four decision notes rest on `feat-app-util-new`: `dec-app-cutoff-v3`, `dec-app-no-gbm`, `dec-app-rebuild-v4` and `dec-app-cutoff-v4`.
Notes: application-scorecard/dec-app-cutoff-v3.md, application-scorecard/dec-app-no-gbm.md, application-scorecard/dec-app-rebuild-v4.md, application-scorecard/dec-app-cutoff-v4.md

## Q4
`cr-lgbm-v3` is in force. It was built directly on `cr-lgbm-v2`, `ds-cr-intent-labels`, `exp-106` and `fnd-cr-threshold`.
Notes: call-center-routing/cr-lgbm-v1.md, call-center-routing/cr-lgbm-v2.md, call-center-routing/cr-lgbm-v3.md, call-center-routing/ds-cr-intent-labels.md, call-center-routing/exp-106.md, call-center-routing/fnd-cr-threshold.md

## Q5
Only `feat-ror-churn-score` in retention-offers-roi was built directly on `churn-gbm-2025-v2`.
Notes: retention-offers-roi/feat-ror-churn-score.md

## Q6
`app-gbm-v2` rests on two dataset notes: `ds-app-applications-2024` directly, and `ds-app-reject-sample` through `exp-501`.
Notes: application-scorecard/ds-app-applications-2024.md, application-scorecard/ds-app-reject-sample.md

## Q7
`csb-lr-base` and `csb-xgb-v1` both build directly on `feat-csb-spend-raw` and `feat-csb-tenure-band`.
Notes: churn-small-business/csb-lr-base.md, churn-small-business/csb-xgb-v1.md, churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-tenure-band.md

## Q8
`churn-lr-base-2025` is the only current model that builds directly on a replaced feature: it uses `feat-c25-util-v1`, which `feat-c25-util-v2` replaced.
Notes: churn-2025/churn-lr-base-2025.md

## Q9
Five decision notes rest on `ds-bt-offer-log`: `dec-bt-cut-mailer-top30`, `dec-bt-drop-post-offer-features`, `dec-bt-margin-label`, `promo-apr-test/dec-pa-6m-default` and `promo-apr-test/dec-pa-no-12m-subprime`. `dec-bt-margin-label` also has one link the memory could not match to a note, so it may rest on `ds-bt-offer-log` by a different route.
Notes: balance-transfer-propensity/dec-bt-cut-mailer-top30.md, balance-transfer-propensity/dec-bt-drop-post-offer-features.md, balance-transfer-propensity/dec-bt-margin-label.md, balance-transfer-propensity/ds-bt-offer-log.md, promo-apr-test/dec-pa-6m-default.md, promo-apr-test/dec-pa-no-12m-subprime.md

## Q10
`dec-cb-threshold-2500` is in force. It was built directly on `dec-cb-adopt-banded-tiers`, `exp-206-breakeven-sim` and `find-cb-breakeven-lift`.
Notes: cashback-redesign/dec-cb-extend-flat-pilot.md, cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/dec-cb-threshold-2500.md, cashback-redesign/exp-206-breakeven-sim.md, cashback-redesign/find-cb-breakeven-lift.md