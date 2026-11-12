## Q1
feat-c25-payment-behaviour and feat-c25-txn-recency are the two feature notes that both churn-gbm-2025-v2 and churn-lr-base-2025 build on directly.
Notes: churn-2025/feat-c25-payment-behaviour.md, churn-2025/feat-c25-txn-recency.md

## Q2
cb-uplift-v1 is a current model that still builds directly on feat-cb-spend-base, which feat-cb-spend-band-v2 replaced.
Notes: cashback-redesign/cb-uplift-v1.md, cashback-redesign/feat-cb-spend-base.md, cashback-redesign/feat-cb-spend-band-v2.md

## Q3
Four decisions rest on feat-app-util-new: dec-app-cutoff-v3 directly (via app-scorecard-v3), and dec-app-cutoff-v4, dec-app-rebuild-v4 and dec-app-no-gbm through the chain app-gbm-v1 → app-scorecard-v3 → feat-app-util-new.
Notes: application-scorecard/dec-app-cutoff-v3.md, application-scorecard/dec-app-cutoff-v4.md, application-scorecard/dec-app-rebuild-v4.md, application-scorecard/dec-app-no-gbm.md

## Q4
cr-lgbm-v3 is in force (it replaced cr-lgbm-v2, which had replaced cr-lgbm-v1). It builds on cr-lgbm-v2, ds-cr-intent-labels, exp-106 and fnd-cr-threshold.
Notes: call-center-routing/cr-lgbm-v3.md, call-center-routing/cr-lgbm-v2.md, call-center-routing/ds-cr-intent-labels.md, call-center-routing/exp-106.md, call-center-routing/fnd-cr-threshold.md

## Q5
Only feat-ror-churn-score (retention-offers-roi) builds directly on churn-gbm-2025-v2. ror-uplift-v1 uses the score too, but only through that feature.
Notes: retention-offers-roi/feat-ror-churn-score.md

## Q6
app-gbm-v2 rests on two dataset notes: ds-app-applications-2024, which is the root of the chain (via app-gbm-v1, app-scorecard-v3, feat-app-thin-file and exp-501), and ds-app-reject-sample (via exp-501 and find-app-reject-inference-gain). The v8 score it also takes as an input is defined outside this project, so I did not trace it.
Notes: application-scorecard/ds-app-applications-2024.md, application-scorecard/ds-app-reject-sample.md

## Q7
csb-lr-base and csb-xgb-v1 both build directly on feat-csb-spend-raw and feat-csb-tenure-band.
Notes: churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-tenure-band.md

## Q8
churn-lr-base-2025 is the only current model that builds directly on a replaced feature: its "month-end over-limit utilisation" input is feat-c25-util-v1, which feat-c25-util-v2 replaced. churn-gbm-2025-v2 does not use the replaced feature.
Notes: churn-2025/churn-lr-base-2025.md, churn-2025/feat-c25-util-v1.md, churn-2025/feat-c25-util-v2.md

## Q9
dec-bt-drop-post-offer-features, dec-bt-margin-label and dec-bt-cut-mailer-top30 all rest on ds-bt-offer-log. The first reaches it via find-bt-limit-leak and exp-104; the other two via exp-107, bt-xgb-v2 and feat-bt-revolve-share.
Notes: balance-transfer-propensity/dec-bt-cut-mailer-top30.md, balance-transfer-propensity/dec-bt-drop-post-offer-features.md, balance-transfer-propensity/dec-bt-margin-label.md

## Q10
dec-cb-threshold-2500 is in force; it replaced dec-cb-adopt-banded-tiers, which had replaced dec-cb-extend-flat-pilot. It builds on dec-cb-adopt-banded-tiers, exp-206-breakeven-sim and find-cb-breakeven-lift.
Notes: cashback-redesign/dec-cb-threshold-2500.md, cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/exp-206-breakeven-sim.md, cashback-redesign/find-cb-breakeven-lift.md