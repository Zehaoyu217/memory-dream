## Q1
Four decision notes rest on ds-cr-ivr-paths: dec-cr-lgbm, dec-cr-caller-v2, dec-cr-cost-matrix and dec-cr-pilot. They reach it through feat-cr-ivr-path-v1 and the models and findings built on it.
Notes: call-center-routing/dec-cr-lgbm.md, call-center-routing/dec-cr-caller-v2.md, call-center-routing/dec-cr-cost-matrix.md, call-center-routing/dec-cr-pilot.md

## Q2
cli-xgb-v3 is in force now. It is built directly on exp-107 and find-cli-uplift-wins.
Notes: credit-line-increase/cli-xgb-v3.md, credit-line-increase/exp-107.md, credit-line-increase/find-cli-uplift-wins.md

## Q3
Only one note in another project is built directly on ds-disp-merchant-link: merchant-risk/feat-mrisk-dispute-ratio.
Notes: merchant-risk/feat-mrisk-dispute-ratio.md

## Q4
cr-lgbm-v1 rests on two dataset notes: ds-cr-calls (through feat-cr-caller-history-v1 and cr-logreg-v1) and ds-cr-ivr-paths (through feat-cr-ivr-path-v1 and cr-logreg-v1).
Notes: call-center-routing/ds-cr-calls.md, call-center-routing/ds-cr-ivr-paths.md

## Q5
Four feature notes are built directly by both fraud25-gbm-v1 and fraud25-gbm-v2: feat-f25-amt-ratio, feat-f25-device-age, feat-f25-hour-band and feat-f25-velocity-v1.
Notes: fraud-2025/feat-f25-amt-ratio.md, fraud-2025/feat-f25-device-age.md, fraud-2025/feat-f25-hour-band.md, fraud-2025/feat-f25-velocity-v1.md

## Q6
None. The only current model is clv-ml-v2, and it builds directly on clv-ml-v1 (a model, not a feature or dataset) and on feat-clv-hazard, which has not been replaced.
Notes: customer-lifetime-value/clv-ml-v2.md

## Q7
Three decision notes rest on ds-cb-spend-panel: dec-cb-extend-flat-pilot, dec-cb-adopt-banded-tiers and dec-cb-threshold-2500. The chain runs through feat-cb-spend-base, which the memory index does not link to the panel, but its own text says it builds on the monthly account spend panel.
Notes: cashback-redesign/dec-cb-extend-flat-pilot.md, cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/dec-cb-threshold-2500.md

## Q8
disp-lgbm-v3 is in force now. It is built directly on disp-lgbm-v2, exp-307, feat-disp-fraud-score and dec-disp-fraud-score-in.
Notes: dispute-triage/disp-lgbm-v3.md, dispute-triage/disp-lgbm-v2.md, dispute-triage/exp-307.md, dispute-triage/feat-disp-fraud-score.md, dispute-triage/dec-disp-fraud-score-in.md

## Q9
Only one note in another project is built directly on feat-fsm-util-ratio: model-monitoring/mm-limit-glm-v2.
Notes: model-monitoring/mm-limit-glm-v2.md

## Q10
cb-elasticity-v1 is built directly on feat-cb-spend-base, which in turn builds on the monthly account spend panel. That makes ds-cb-spend-panel the only dataset note it rests on, though the link is recorded in feat-cb-spend-base's text rather than its header.
Notes: cashback-redesign/ds-cb-spend-panel.md