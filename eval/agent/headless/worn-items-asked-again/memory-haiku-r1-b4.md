## Q1
Four decision notes rest on ds-cr-ivr-paths, all through feat-cr-ivr-path-v1: dec-cr-lgbm (via cr-lgbm-v1), dec-cr-caller-v2 (via cr-lgbm-v2 and cr-lgbm-v3), dec-cr-cost-matrix (via cr-lgbm-v3), and dec-cr-pilot (via the same chain).
Notes: call-center-routing/dec-cr-lgbm.md, call-center-routing/dec-cr-caller-v2.md, call-center-routing/dec-cr-cost-matrix.md, call-center-routing/dec-cr-pilot.md

## Q2
cli-xgb-v3 is the one in force. It is built directly on exp-107 and find-cli-uplift-wins, and through them on the older v1 chain (exp-102, cli-xgb-v1, and the v1 datasets and features).
Notes: credit-line-increase/cli-xgb-v3.md, credit-line-increase/exp-107.md, credit-line-increase/find-cli-uplift-wins.md

## Q3
Only merchant-risk/feat-mrisk-dispute-ratio was built directly on ds-disp-merchant-link. The merchant-risk decision dec-mrisk-dispute-feature names that dataset as a dependency in its text but builds on the feature note.
Notes: merchant-risk/feat-mrisk-dispute-ratio.md

## Q4
cr-lgbm-v1 rests on two dataset notes: ds-cr-calls, through feat-cr-caller-history-v1 and cr-logreg-v1, and ds-cr-ivr-paths, through feat-cr-ivr-path-v1.
Notes: call-center-routing/ds-cr-calls.md, call-center-routing/ds-cr-ivr-paths.md

## Q5
Both models build directly on four features: feat-f25-amt-ratio, feat-f25-device-age, feat-f25-hour-band and feat-f25-velocity-v1. Both also build on the ds-f25-labels dataset, which is not a feature.
Notes: fraud-2025/feat-f25-amt-ratio.md, fraud-2025/feat-f25-device-age.md, fraud-2025/feat-f25-hour-band.md, fraud-2025/feat-f25-velocity-v1.md

## Q6
None. clv-ml-v2 is the only current model, and it builds directly on feat-clv-hazard, which has not been replaced, and on the superseded model clv-ml-v1 (a model, not a feature or dataset).
Notes: customer-lifetime-value/clv-ml-v2.md, customer-lifetime-value/feat-clv-hazard.md

## Q7
Three decision notes rest on ds-cb-spend-panel: dec-cb-adopt-banded-tiers, dec-cb-extend-flat-pilot and dec-cb-threshold-2500. They do so through the elasticity, pilot and feature notes built on the panel.
Notes: cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/dec-cb-extend-flat-pilot.md, cashback-redesign/dec-cb-threshold-2500.md

## Q8
disp-lgbm-v3 is the one in force. It is built directly on dec-disp-fraud-score-in, disp-lgbm-v2, exp-307 and feat-disp-fraud-score, and through them on the rest of the v1 and v2 chain.
Notes: dispute-triage/disp-lgbm-v3.md, dispute-triage/dec-disp-fraud-score-in.md, dispute-triage/disp-lgbm-v2.md, dispute-triage/exp-307.md, dispute-triage/feat-disp-fraud-score.md

## Q9
Only model-monitoring/mm-limit-glm-v2 was built directly on feat-fsm-util-ratio from another project.
Notes: model-monitoring/mm-limit-glm-v2.md

## Q10
cb-elasticity-v1 rests on two dataset notes: ds-cb-pilot-2025q4 directly, and ds-cb-spend-panel both directly and through feat-cb-spend-base.
Notes: cashback-redesign/ds-cb-pilot-2025q4.md, cashback-redesign/ds-cb-spend-panel.md