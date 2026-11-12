## Q1
Four decision notes rest on ds-cr-ivr-paths: dec-cr-lgbm, dec-cr-caller-v2, dec-cr-cost-matrix and dec-cr-pilot. Each reaches it through feat-cr-ivr-path-v1 and the model notes built on it.
Notes: call-center-routing/dec-cr-lgbm.md, call-center-routing/dec-cr-caller-v2.md, call-center-routing/dec-cr-cost-matrix.md, call-center-routing/dec-cr-pilot.md

## Q2
The note in force at the end of the cli-xgb-v1 line is cli-xgb-v3, a two-model T-learner uplift model. It is built directly on exp-107 and find-cli-uplift-wins.
Notes: credit-line-increase/cli-xgb-v3.md, credit-line-increase/exp-107.md, credit-line-increase/find-cli-uplift-wins.md

## Q3
Directly on ds-disp-merchant-link, from another project, is merchant-risk/feat-mrisk-dispute-ratio. merchant-risk/dec-mrisk-dispute-feature also names a direct dependency on that dataset in its text, though its recorded basis is the feature.
Notes: merchant-risk/feat-mrisk-dispute-ratio.md, merchant-risk/dec-mrisk-dispute-feature.md

## Q4
cr-lgbm-v1 rests on two dataset notes: ds-cr-calls and ds-cr-ivr-paths. The unplaced link in exp-101 ("logistic regression baseline and account tenure features") maps to cr-logreg-v1 and feat-cr-tenure-v1, which are already in the chain, so it adds no dataset.
Notes: call-center-routing/ds-cr-calls.md, call-center-routing/ds-cr-ivr-paths.md

## Q5
Both fraud25-gbm-v1 and fraud25-gbm-v2 build directly on four feature notes: feat-f25-amt-ratio, feat-f25-device-age, feat-f25-hour-band and feat-f25-velocity-v1.
Notes: fraud-2025/feat-f25-amt-ratio.md, fraud-2025/feat-f25-device-age.md, fraud-2025/feat-f25-hour-band.md, fraud-2025/feat-f25-velocity-v1.md

## Q6
None. The only current model in customer-lifetime-value is clv-ml-v2, and its direct feature and dataset inputs are feat-clv-hazard, which has not been replaced, plus the superseded model clv-ml-v1, which is a model rather than a feature or dataset.
Notes: customer-lifetime-value/clv-ml-v2.md, customer-lifetime-value/feat-clv-hazard.md

## Q7
Three decision notes rest on ds-cb-spend-panel: dec-cb-adopt-banded-tiers, dec-cb-extend-flat-pilot and dec-cb-threshold-2500. Each reaches it through the elasticity, band and pilot notes built on it.
Notes: cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/dec-cb-extend-flat-pilot.md, cashback-redesign/dec-cb-threshold-2500.md

## Q8
The note in force at the end of the disp-lgbm-v1 line is disp-lgbm-v3, which adds the fraud-2026 score. It is built directly on dec-disp-fraud-score-in, disp-lgbm-v2, exp-307 and feat-disp-fraud-score.
Notes: dispute-triage/disp-lgbm-v3.md, dispute-triage/dec-disp-fraud-score-in.md, dispute-triage/disp-lgbm-v2.md, dispute-triage/exp-307.md, dispute-triage/feat-disp-fraud-score.md

## Q9
Only mm-limit-glm-v2 in model-monitoring is built directly on feat-fsm-util-ratio from another project. The other notes that use the feature (exp-105, fsm-churn-xgb-v2) are in feature-store-migration itself.
Notes: model-monitoring/mm-limit-glm-v2.md

## Q10
cb-elasticity-v1 rests on two dataset notes: ds-cb-pilot-2025q4 directly, and ds-cb-spend-panel through feat-cb-spend-base. ds-cb-spend-panel is built from cards.txn_daily, which no note records, so the chain stops there.
Notes: cashback-redesign/ds-cb-pilot-2025q4.md, cashback-redesign/ds-cb-spend-panel.md