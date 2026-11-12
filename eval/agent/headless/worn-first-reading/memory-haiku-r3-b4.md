## Q1
Four decision notes rest on ds-cr-ivr-paths: dec-cr-lgbm (via cr-logreg-v1 and cr-lgbm-v1), dec-cr-caller-v2 (via fnd-cr-leak-corrected), and dec-cr-cost-matrix and dec-cr-pilot (both via cr-lgbm-v3).
Notes: call-center-routing/dec-cr-lgbm.md, call-center-routing/dec-cr-caller-v2.md, call-center-routing/dec-cr-cost-matrix.md, call-center-routing/dec-cr-pilot.md

## Q2
The note in force is cli-xgb-v3 (cli-xgb-v1 → v2 → v3). It is built on exp-107 and find-cli-uplift-wins, and it replaces cli-xgb-v2.
Notes: credit-line-increase/cli-xgb-v3.md, credit-line-increase/exp-107.md, credit-line-increase/find-cli-uplift-wins.md

## Q3
Only merchant-risk/feat-mrisk-dispute-ratio was built directly on ds-disp-merchant-link from another project.
Notes: merchant-risk/feat-mrisk-dispute-ratio.md

## Q4
cr-lgbm-v1 rests on two dataset notes: ds-cr-calls (via feat-cr-caller-history-v1 and cr-logreg-v1) and ds-cr-ivr-paths (via feat-cr-ivr-path-v1 and cr-logreg-v1).
Notes: call-center-routing/ds-cr-calls.md, call-center-routing/ds-cr-ivr-paths.md

## Q5
fraud25-gbm-v1 and fraud25-gbm-v2 both build directly on feat-f25-amt-ratio, feat-f25-device-age, feat-f25-hour-band and feat-f25-velocity-v1.
Notes: fraud-2025/feat-f25-amt-ratio.md, fraud-2025/feat-f25-device-age.md, fraud-2025/feat-f25-hour-band.md, fraud-2025/feat-f25-velocity-v1.md

## Q6
None. clv-ml-v2 is the only current model, and it builds directly on clv-ml-v1 (a model, not a feature or dataset) and on feat-clv-hazard, which has not been replaced.
Notes: customer-lifetime-value/clv-ml-v2.md

## Q7
Three decision notes rest on ds-cb-spend-panel: dec-cb-extend-flat-pilot, dec-cb-adopt-banded-tiers and dec-cb-threshold-2500.
Notes: cashback-redesign/dec-cb-extend-flat-pilot.md, cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/dec-cb-threshold-2500.md

## Q8
The note in force is disp-lgbm-v3 (disp-lgbm-v1 → v2 → v3). It is built on dec-disp-fraud-score-in, disp-lgbm-v2, exp-307 and feat-disp-fraud-score.
Notes: dispute-triage/disp-lgbm-v3.md, dispute-triage/dec-disp-fraud-score-in.md, dispute-triage/disp-lgbm-v2.md, dispute-triage/exp-307.md, dispute-triage/feat-disp-fraud-score.md

## Q9
Only model-monitoring/mm-limit-glm-v2 was built directly on feat-fsm-util-ratio from another project.
Notes: model-monitoring/mm-limit-glm-v2.md

## Q10
The recorded graph stops at feat-cb-spend-base, which has no recorded upstream, so the answer rests on the note text: cb-elasticity-v1 builds directly on the Q4 2025 pilot dataset, and feat-cb-spend-base builds on the monthly spend panel, a link missing from its recorded build list. The dataset notes are therefore ds-cb-pilot-2025q4 and ds-cb-spend-panel.
Notes: cashback-redesign/ds-cb-pilot-2025q4.md, cashback-redesign/ds-cb-spend-panel.md