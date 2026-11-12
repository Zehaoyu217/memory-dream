## Q1
Four decision notes rest on ds-cr-ivr-paths, all through feat-cr-ivr-path-v1 and the models built after it: dec-cr-lgbm, dec-cr-caller-v2, dec-cr-cost-matrix and dec-cr-pilot.
Notes: call-center-routing/dec-cr-lgbm.md, call-center-routing/dec-cr-caller-v2.md, call-center-routing/dec-cr-cost-matrix.md, call-center-routing/dec-cr-pilot.md

## Q2
The line runs cli-xgb-v1 → cli-xgb-v2 → cli-xgb-v3, so cli-xgb-v3 is current. It is built on exp-107 and find-cli-uplift-wins, and it replaces cli-xgb-v2.
Notes: credit-line-increase/cli-xgb-v3.md, credit-line-increase/exp-107.md, credit-line-increase/find-cli-uplift-wins.md

## Q3
Only one note in another project builds directly on it: merchant-risk/feat-mrisk-dispute-ratio.
Notes: merchant-risk/feat-mrisk-dispute-ratio.md

## Q4
cr-lgbm-v1 rests on two datasets: ds-cr-calls (through feat-cr-caller-history-v1) and ds-cr-ivr-paths (through feat-cr-ivr-path-v1).
Notes: call-center-routing/ds-cr-calls.md, call-center-routing/ds-cr-ivr-paths.md

## Q5
Both models build directly on four features: feat-f25-amt-ratio, feat-f25-device-age, feat-f25-hour-band and feat-f25-velocity-v1. Only v2 adds feat-f25-mcc-travel.
Notes: fraud-2025/feat-f25-amt-ratio.md, fraud-2025/feat-f25-device-age.md, fraud-2025/feat-f25-hour-band.md, fraud-2025/feat-f25-velocity-v1.md

## Q6
None. The only current model is clv-ml-v2, and it builds directly on clv-ml-v1 and feat-clv-hazard, neither of which is a replaced feature or dataset (clv-ml-v1 is a replaced model, not a feature or dataset). The models that did use the replaced feat-clv-arpu-v1 (clv-bgnbd-v1) are themselves superseded.
Notes: customer-lifetime-value/clv-ml-v2.md, customer-lifetime-value/feat-clv-hazard.md

## Q7
Three decision notes rest on ds-cb-spend-panel: dec-cb-extend-flat-pilot, dec-cb-threshold-2500 and dec-cb-adopt-banded-tiers.
Notes: cashback-redesign/dec-cb-extend-flat-pilot.md, cashback-redesign/dec-cb-threshold-2500.md, cashback-redesign/dec-cb-adopt-banded-tiers.md

## Q8
The line runs disp-lgbm-v1 → disp-lgbm-v2 → disp-lgbm-v3, so disp-lgbm-v3 is current. It is built on dec-disp-fraud-score-in, disp-lgbm-v2, exp-307 and feat-disp-fraud-score.
Notes: dispute-triage/disp-lgbm-v3.md, dispute-triage/dec-disp-fraud-score-in.md, dispute-triage/disp-lgbm-v2.md, dispute-triage/exp-307.md, dispute-triage/feat-disp-fraud-score.md

## Q9
Only one note in another project builds directly on it: model-monitoring/mm-limit-glm-v2.
Notes: model-monitoring/mm-limit-glm-v2.md

## Q10
cb-elasticity-v1 builds only on feat-cb-spend-base, which says in its text that it "builds on the monthly account spend panel" (`cb.spend_panel`). So the one dataset it rests on is ds-cb-spend-panel. The memory tool's link map does not show this step because the note names the dataset in words, not by its id.
Notes: cashback-redesign/feat-cb-spend-base.md, cashback-redesign/ds-cb-spend-panel.md