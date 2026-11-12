## Q1
Both build directly on feat-c25-payment-behaviour (payment ratio and late counts) and feat-c25-txn-recency (card recency).
Notes: churn-2025/feat-c25-payment-behaviour.md, churn-2025/feat-c25-txn-recency.md

## Q2
cb-uplift-v1 is still current and builds on feat-cb-spend-base, which feat-cb-spend-band-v2 replaced.
Notes: cashback-redesign/cb-uplift-v1.md, cashback-redesign/feat-cb-spend-base.md

## Q3
Four decisions rest on feat-app-util-new: dec-app-cutoff-v3 and dec-app-rebuild-v4 directly or via app-scorecard-v3 and find-app-gini-v3-drift, and dec-app-cutoff-v4 and dec-app-no-gbm via the app-gbm-v1 and app-scorecard-v3 chain.
Notes: application-scorecard/dec-app-cutoff-v3.md, application-scorecard/dec-app-cutoff-v4.md, application-scorecard/dec-app-no-gbm.md, application-scorecard/dec-app-rebuild-v4.md

## Q4
cr-lgbm-v3 is in force; it builds on cr-lgbm-v2 (the replaced second router), ds-cr-intent-labels, exp-106 and the cost-matrix threshold finding fnd-cr-threshold.
Notes: call-center-routing/cr-lgbm-v3.md, call-center-routing/cr-lgbm-v2.md, call-center-routing/ds-cr-intent-labels.md, call-center-routing/exp-106.md, call-center-routing/fnd-cr-threshold.md

## Q5
Only feat-ror-churn-score (retention-offers-roi) builds directly on churn-gbm-2025-v2. ror-uplift-v1 uses that score only through feat-ror-churn-score, so it is indirect.
Notes: retention-offers-roi/feat-ror-churn-score.md

## Q6
app-gbm-v2 traces back to ds-app-applications-2024 through app-gbm-v1, app-scorecard-v3, feat-app-thin-file, feat-app-util-new and feat-app-velocity-apps. It also reaches ds-app-reject-sample through find-app-reject-inference-gain and exp-501.
Notes: application-scorecard/ds-app-applications-2024.md, application-scorecard/ds-app-reject-sample.md

## Q7
csb-lr-base and csb-xgb-v1 both build directly on feat-csb-spend-raw and feat-csb-tenure-band.
Notes: churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-tenure-band.md

## Q8
churn-lr-base-2025 is still current as the monitoring challenger and builds on feat-c25-util-v1, which feat-c25-util-v2 replaced.
Notes: churn-2025/churn-lr-base-2025.md, churn-2025/feat-c25-util-v1.md

## Q9
Three decisions rest on ds-bt-offer-log: dec-bt-margin-label and dec-bt-cut-mailer-top30 via exp-107 and bt-xgb-v2/feat-bt-revolve-share, and dec-bt-drop-post-offer-features via find-bt-limit-leak and exp-104.
Notes: balance-transfer-propensity/dec-bt-margin-label.md, balance-transfer-propensity/dec-bt-cut-mailer-top30.md, balance-transfer-propensity/dec-bt-drop-post-offer-features.md

## Q10
dec-cb-threshold-2500 is in force and replaces dec-cb-adopt-banded-tiers, which had replaced dec-cb-extend-flat-pilot. It builds on dec-cb-adopt-banded-tiers, exp-206-breakeven-sim and find-cb-breakeven-lift.
Notes: cashback-redesign/dec-cb-threshold-2500.md, cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/exp-206-breakeven-sim.md, cashback-redesign/find-cb-breakeven-lift.md