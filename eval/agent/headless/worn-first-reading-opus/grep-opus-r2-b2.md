## Q1
Both models build directly on two feature notes: feat-c25-payment-behaviour (payment ratio and late counts) and feat-c25-txn-recency (days since last card transaction). churn-lr-base-2025 also uses app sessions and util-v1, while churn-gbm-2025-v2 uses util-v2 instead.
Notes: churn-2025/feat-c25-payment-behaviour.md, churn-2025/feat-c25-txn-recency.md

## Q2
cb-uplift-v1 is the only one. It is still current, but it builds directly on feat-cb-spend-base, which feat-cb-spend-band-v2 has since replaced. cb-elasticity-v2 and cb-sim-v1 only build on inputs that are still current, and cb-elasticity-v1 has itself been replaced.
Notes: cashback-redesign/cb-uplift-v1.md

## Q3
Four decision notes rest on it. feat-app-util-new feeds app-scorecard-v3, which then leads to dec-app-cutoff-v3 directly and to dec-app-no-gbm (via app-gbm-v1 and exp-503/exp-504). It also leads to dec-app-rebuild-v4 (via app-gbm-v2 and find-app-gini-v3-drift) and to dec-app-cutoff-v4 (via app-scorecard-v4, exp-507 and the exp-506 → find-app-income-lift path). dec-app-cutoff-v3 has since been replaced by dec-app-cutoff-v4.
Notes: application-scorecard/dec-app-cutoff-v3.md, application-scorecard/dec-app-no-gbm.md, application-scorecard/dec-app-rebuild-v4.md, application-scorecard/dec-app-cutoff-v4.md

## Q4
cr-lgbm-v1 was replaced by cr-lgbm-v2, which was replaced by cr-lgbm-v3, the router in force now. cr-lgbm-v3 builds on cr-lgbm-v2, ds-cr-intent-labels, exp-106 and fnd-cr-threshold (the cost-matrix misroute finding).
Notes: call-center-routing/cr-lgbm-v3.md, call-center-routing/cr-lgbm-v2.md, call-center-routing/ds-cr-intent-labels.md, call-center-routing/exp-106.md, call-center-routing/fnd-cr-threshold.md

## Q5
Only one note builds on it directly: feat-ror-churn-score in project retention-offers-roi. ror-uplift-v1 mentions the churn-2025 model, but it builds on feat-ror-churn-score rather than on churn-gbm-2025-v2 itself.
Notes: retention-offers-roi/feat-ror-churn-score.md

## Q6
app-gbm-v2 rests on two dataset notes: ds-app-applications-2024 and ds-app-reject-sample. The first comes in through app-gbm-v1, app-scorecard-v3 and its features. The second comes in through find-app-reject-inference-gain, exp-501 and q-app-reject-inference.
Notes: application-scorecard/ds-app-applications-2024.md, application-scorecard/ds-app-reject-sample.md

## Q7
Both models build directly on feat-csb-spend-raw and feat-csb-tenure-band. csb-xgb-v1 also uses feat-csb-deposit-volatility.
Notes: churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-tenure-band.md

## Q8
churn-lr-base-2025 is the only one. It is still current, but it builds directly on feat-c25-util-v1, which feat-c25-util-v2 has since replaced. churn-gbm-2025-v2 only builds on current features, and churn-gbm-2025 (v1) has itself been replaced.
Notes: churn-2025/churn-lr-base-2025.md

## Q9
All three decision notes in the project rest on it. dec-bt-drop-post-offer-features gets there via find-bt-limit-leak and exp-104. dec-bt-margin-label gets there via exp-107, bt-xgb-v2 and the features. dec-bt-cut-mailer-top30 gets there via bt-xgb-v3.
Notes: balance-transfer-propensity/dec-bt-drop-post-offer-features.md, balance-transfer-propensity/dec-bt-margin-label.md, balance-transfer-propensity/dec-bt-cut-mailer-top30.md

## Q10
dec-cb-extend-flat-pilot was replaced by dec-cb-adopt-banded-tiers, which was replaced by dec-cb-threshold-2500, the decision in force now. dec-cb-threshold-2500 builds on dec-cb-adopt-banded-tiers, exp-206-breakeven-sim and find-cb-breakeven-lift.
Notes: cashback-redesign/dec-cb-threshold-2500.md, cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/exp-206-breakeven-sim.md, cashback-redesign/find-cb-breakeven-lift.md