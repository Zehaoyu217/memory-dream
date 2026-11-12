## Q1
churn-gbm-2025-v2 and churn-lr-base-2025 both build directly on two feature notes: feat-c25-payment-behaviour and feat-c25-txn-recency. They differ on utilisation (v2 uses util-v2, the baseline uses util-v1), and only the baseline uses app sessions.
Notes: churn-2025/feat-c25-payment-behaviour.md, churn-2025/feat-c25-txn-recency.md

## Q2
Two current models qualify: cb-elasticity-v1 and cb-uplift-v1. Both are still in force and both build directly on feat-cb-spend-base, which was replaced by feat-cb-spend-band-v2.
Notes: cashback-redesign/cb-elasticity-v1.md, cashback-redesign/cb-uplift-v1.md

## Q3
Four decision notes rest on feat-app-util-new, all through other notes (it feeds app-scorecard-v3 first): dec-app-cutoff-v3, dec-app-no-gbm, dec-app-rebuild-v4 and dec-app-cutoff-v4. No notes in other projects rest on it.
Notes: application-scorecard/dec-app-cutoff-v3.md, application-scorecard/dec-app-no-gbm.md, application-scorecard/dec-app-rebuild-v4.md, application-scorecard/dec-app-cutoff-v4.md

## Q4
The line runs cr-lgbm-v1 → cr-lgbm-v2 → cr-lgbm-v3, and cr-lgbm-v3 is the router in force now. It is built on cr-lgbm-v2 (now replaced), ds-cr-intent-labels, exp-106 and fnd-cr-threshold.
Notes: call-center-routing/cr-lgbm-v3.md, call-center-routing/cr-lgbm-v2.md, call-center-routing/ds-cr-intent-labels.md, call-center-routing/exp-106.md, call-center-routing/fnd-cr-threshold.md

## Q5
Only retention-offers-roi/feat-ror-churn-score is built directly on churn-gbm-2025-v2. Other retention-offers-roi notes, such as ror-uplift-v1, rest on it only through feat-ror-churn-score.
Notes: retention-offers-roi/feat-ror-churn-score.md

## Q6
app-gbm-v2 rests on two dataset notes. ds-app-applications-2024 comes in through app-scorecard-v3, its features and exp-501. ds-app-reject-sample comes in through find-app-reject-inference-gain → exp-501.
Notes: application-scorecard/ds-app-applications-2024.md, application-scorecard/ds-app-reject-sample.md

## Q7
csb-lr-base and csb-xgb-v1 both build directly on feat-csb-spend-raw (since replaced by feat-csb-spend-sa-v2) and feat-csb-tenure-band.
Notes: churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-tenure-band.md

## Q8
Only churn-lr-base-2025 qualifies. It is still current and builds directly on feat-c25-util-v1, which was replaced by feat-c25-util-v2. churn-gbm-2025-v2 builds only on current inputs.
Notes: churn-2025/churn-lr-base-2025.md

## Q9
Three decisions in the project rest on ds-bt-offer-log: dec-bt-drop-post-offer-features, dec-bt-margin-label and dec-bt-cut-mailer-top30. Two more in promo-apr-test rest on it through bt-xgb-v3: dec-pa-6m-default and dec-pa-no-12m-subprime.
Notes: balance-transfer-propensity/dec-bt-drop-post-offer-features.md, balance-transfer-propensity/dec-bt-margin-label.md, balance-transfer-propensity/dec-bt-cut-mailer-top30.md, promo-apr-test/dec-pa-6m-default.md, promo-apr-test/dec-pa-no-12m-subprime.md

## Q10
The line runs dec-cb-extend-flat-pilot → dec-cb-adopt-banded-tiers → dec-cb-threshold-2500, and dec-cb-threshold-2500 is in force now (top tier starts at $2,500). It is built on dec-cb-adopt-banded-tiers (now replaced), exp-206-breakeven-sim and find-cb-breakeven-lift.
Notes: cashback-redesign/dec-cb-threshold-2500.md, cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/exp-206-breakeven-sim.md, cashback-redesign/find-cb-breakeven-lift.md