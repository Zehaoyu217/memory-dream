I've traced all ten dependency chains; here are the answers.

## Q1
Both models build directly on two feature notes: the payment-behaviour feature and the transaction-recency feature. Beyond those, churn-gbm-2025-v2 also uses util-v2, and churn-lr-base-2025 also uses app sessions and util-v1.
Notes: churn-2025/feat-c25-payment-behaviour.md, churn-2025/feat-c25-txn-recency.md

## Q2
cb-uplift-v1 is the only one. It is still current and builds directly on feat-cb-spend-base, which feat-cb-spend-band-v2 has since replaced. cb-elasticity-v2 and cb-sim-v1 rest only on notes that are still current, and cb-elasticity-v1 has itself been replaced.
Notes: cashback-redesign/cb-uplift-v1.md, cashback-redesign/feat-cb-spend-base.md

## Q3
Four decisions rest on it. feat-app-util-new feeds app-scorecard-v3, which leads to dec-app-cutoff-v3 directly. Through app-gbm-v1 and exp-503 it leads to dec-app-no-gbm. Through app-gbm-v2 and find-app-gini-v3-drift it leads to dec-app-rebuild-v4. Through app-scorecard-v4 and the exp-506 → find-app-income-lift chain it leads to dec-app-cutoff-v4.
Notes: application-scorecard/dec-app-cutoff-v3.md, application-scorecard/dec-app-no-gbm.md, application-scorecard/dec-app-rebuild-v4.md, application-scorecard/dec-app-cutoff-v4.md

## Q4
The line runs cr-lgbm-v1 → cr-lgbm-v2 → cr-lgbm-v3, and cr-lgbm-v3 is the router in force now. It is built on cr-lgbm-v2, ds-cr-intent-labels, exp-106 and fnd-cr-threshold (the cost-matrix misroute finding).
Notes: call-center-routing/cr-lgbm-v3.md, call-center-routing/cr-lgbm-v2.md, call-center-routing/ds-cr-intent-labels.md, call-center-routing/exp-106.md, call-center-routing/fnd-cr-threshold.md

## Q5
Only feat-ror-churn-score in retention-offers-roi builds on churn-gbm-2025-v2 directly. ror-uplift-v1 uses the score too, but it builds on it through feat-ror-churn-score rather than directly.
Notes: retention-offers-roi/feat-ror-churn-score.md

## Q6
app-gbm-v2 rests on two dataset notes, ds-app-applications-2024 and ds-app-reject-sample. The first comes through app-gbm-v1, app-scorecard-v3 and its features. The second comes through find-app-reject-inference-gain, exp-501 and q-app-reject-inference.
Notes: application-scorecard/ds-app-applications-2024.md, application-scorecard/ds-app-reject-sample.md

## Q7
Both build directly on feat-csb-spend-raw and feat-csb-tenure-band. csb-xgb-v1 also uses deposit volatility.
Notes: churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-tenure-band.md

## Q8
churn-lr-base-2025 is the only one. It is still kept as the monitoring challenger and builds directly on feat-c25-util-v1, which feat-c25-util-v2 replaced. churn-gbm-2025-v2 rests only on notes that are still current, and churn-gbm-2025 (v1) has itself been replaced.
Notes: churn-2025/churn-lr-base-2025.md, churn-2025/feat-c25-util-v1.md

## Q9
Three decisions in its own project rest on it: dec-bt-drop-post-offer-features (through exp-104 and find-bt-limit-leak), dec-bt-margin-label (through bt-xgb-v2, exp-107 and find-bt-margin-top30) and dec-bt-cut-mailer-top30 (through bt-xgb-v3). In promo-apr-test, two more rest on it through bt-xgb-v3, pa-bal-forecast-v1, the pa-margin models and find-pa-margin-corrected: dec-pa-6m-default and dec-pa-no-12m-subprime.
Notes: balance-transfer-propensity/dec-bt-drop-post-offer-features.md, balance-transfer-propensity/dec-bt-margin-label.md, balance-transfer-propensity/dec-bt-cut-mailer-top30.md, promo-apr-test/dec-pa-6m-default.md, promo-apr-test/dec-pa-no-12m-subprime.md

## Q10
The line runs dec-cb-extend-flat-pilot → dec-cb-adopt-banded-tiers → dec-cb-threshold-2500, and dec-cb-threshold-2500 (top tier starts at $2,500) is the decision in force now. It is built on dec-cb-adopt-banded-tiers, exp-206-breakeven-sim and find-cb-breakeven-lift.
Notes: cashback-redesign/dec-cb-threshold-2500.md, cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/exp-206-breakeven-sim.md, cashback-redesign/find-cb-breakeven-lift.md