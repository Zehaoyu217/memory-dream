## Q1
Both build directly on feat-c25-payment-behaviour (payment ratio and late counts) and feat-c25-txn-recency (days since last card transaction).
Notes: churn-2025/feat-c25-payment-behaviour.md, churn-2025/feat-c25-txn-recency.md

## Q2
cb-uplift-v1 is still current and builds directly on feat-cb-spend-base, which was replaced by feat-cb-spend-band-v2.
Notes: cashback-redesign/cb-uplift-v1.md, cashback-redesign/feat-cb-spend-base.md

## Q3
Four decision notes rest on feat-app-util-new: dec-app-cutoff-v3 directly (via app-scorecard-v3), and dec-app-cutoff-v4, dec-app-no-gbm and dec-app-rebuild-v4 through app-scorecard-v3 → app-gbm-v1 → app-gbm-v2 and the exp-503/exp-504/exp-507 chain.
Notes: application-scorecard/feat-app-util-new.md, application-scorecard/app-scorecard-v3.md, application-scorecard/app-gbm-v1.md, application-scorecard/app-gbm-v2.md, application-scorecard/app-scorecard-v4.md, application-scorecard/exp-503.md, application-scorecard/exp-504.md, application-scorecard/exp-507.md, application-scorecard/dec-app-cutoff-v3.md, application-scorecard/dec-app-cutoff-v4.md, application-scorecard/dec-app-no-gbm.md, application-scorecard/dec-app-rebuild-v4.md

## Q4
cr-lgbm-v1 was replaced by cr-lgbm-v2, which was replaced by cr-lgbm-v3, the note in force. cr-lgbm-v3 builds on cr-lgbm-v2, ds-cr-intent-labels, exp-106 and fnd-cr-threshold (the cost-matrix misroute finding).
Notes: call-center-routing/cr-lgbm-v3.md, call-center-routing/cr-lgbm-v2.md, call-center-routing/ds-cr-intent-labels.md, call-center-routing/exp-106.md, call-center-routing/fnd-cr-threshold.md

## Q5
Only feat-ror-churn-score (retention-offers-roi) builds directly on churn-2025/churn-gbm-2025-v2. ror-uplift-v1 uses that score but reaches it through feat-ror-churn-score, not in its own "Builds on" line.
Notes: retention-offers-roi/feat-ror-churn-score.md

## Q6
app-gbm-v2 rests on two dataset notes: ds-app-applications-2024 (directly through app-gbm-v1 and find-app-reject-inference-gain → exp-501, and through the features and app-scorecard-v3 built on it) and ds-app-reject-sample (through exp-501).
Notes: application-scorecard/app-gbm-v2.md, application-scorecard/app-gbm-v1.md, application-scorecard/app-scorecard-v3.md, application-scorecard/find-app-reject-inference-gain.md, application-scorecard/exp-501.md, application-scorecard/ds-app-applications-2024.md, application-scorecard/ds-app-reject-sample.md

## Q7
csb-lr-base and csb-xgb-v1 both build directly on feat-csb-spend-raw (trailing three-month spend) and feat-csb-tenure-band.
Notes: churn-small-business/csb-lr-base.md, churn-small-business/csb-xgb-v1.md, churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-tenure-band.md

## Q8
churn-lr-base-2025 is still current (the monitoring challenger) and builds directly on feat-c25-util-v1, the over-limit utilisation feature that was replaced by feat-c25-util-v2. churn-gbm-2025-v2 is also current, but it builds only on non-replaced notes.
Notes: churn-2025/churn-lr-base-2025.md, churn-2025/feat-c25-util-v1.md

## Q9
Three decision notes rest on ds-bt-offer-log. dec-bt-drop-post-offer-features reaches it through find-bt-limit-leak and exp-104. dec-bt-margin-label and dec-bt-cut-mailer-top30 reach it through exp-107, bt-xgb-v2 and feat-bt-revolve-share, and bt-xgb-v3.
Notes: balance-transfer-propensity/dec-bt-drop-post-offer-features.md, balance-transfer-propensity/dec-bt-margin-label.md, balance-transfer-propensity/dec-bt-cut-mailer-top30.md, balance-transfer-propensity/ds-bt-offer-log.md, balance-transfer-propensity/find-bt-limit-leak.md, balance-transfer-propensity/exp-104-limit-headroom-full.md, balance-transfer-propensity/exp-107-margin-label.md, balance-transfer-propensity/bt-xgb-v3.md, balance-transfer-propensity/bt-xgb-v2.md, balance-transfer-propensity/feat-bt-revolve-share.md

## Q10
dec-cb-extend-flat-pilot was replaced by dec-cb-adopt-banded-tiers, which was replaced by dec-cb-threshold-2500, the note in force. dec-cb-threshold-2500 builds on dec-cb-adopt-banded-tiers, exp-206-breakeven-sim and find-cb-breakeven-lift.
Notes: cashback-redesign/dec-cb-extend-flat-pilot.md, cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/dec-cb-threshold-2500.md, cashback-redesign/exp-206-breakeven-sim.md, cashback-redesign/find-cb-breakeven-lift.md