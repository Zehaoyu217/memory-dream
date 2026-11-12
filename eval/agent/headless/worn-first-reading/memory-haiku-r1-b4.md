## Q1
Four decision notes rest on ds-cr-ivr-paths: dec-cr-lgbm, dec-cr-caller-v2, dec-cr-cost-matrix and dec-cr-pilot. They reach it through the IVR path feature and the LightGBM router chain.
Notes: call-center-routing/dec-cr-lgbm.md, call-center-routing/dec-cr-caller-v2.md, call-center-routing/dec-cr-cost-matrix.md, call-center-routing/dec-cr-pilot.md

## Q2
cli-xgb-v3 is the note in force at the end of the line (cli-xgb-v1 was replaced by cli-xgb-v2, which was replaced by v3). It is built directly on exp-107 and find-cli-uplift-wins.
Notes: credit-line-increase/cli-xgb-v3.md, credit-line-increase/exp-107.md, credit-line-increase/find-cli-uplift-wins.md

## Q3
Only one note of another project is built directly on ds-disp-merchant-link: merchant-risk's feat-mrisk-dispute-ratio, which uses the merchant dispute-ratio join from September 2026.
Notes: merchant-risk/feat-mrisk-dispute-ratio.md

## Q4
cr-lgbm-v1 rests on two dataset notes: ds-cr-calls (through feat-cr-caller-history-v1 and cr-logreg-v1) and ds-cr-ivr-paths (through feat-cr-ivr-path-v1).
Notes: call-center-routing/ds-cr-calls.md, call-center-routing/ds-cr-ivr-paths.md

## Q5
Both fraud25-gbm-v1 and fraud25-gbm-v2 build directly on feat-f25-amt-ratio, feat-f25-device-age, feat-f25-hour-band and feat-f25-velocity-v1. v2 also adds feat-f25-mcc-travel, which v1 does not use.
Notes: fraud-2025/feat-f25-amt-ratio.md, fraud-2025/feat-f25-device-age.md, fraud-2025/feat-f25-hour-band.md, fraud-2025/feat-f25-velocity-v1.md

## Q6
None. clv-ml-v2 is the only current model in customer-lifetime-value, and it builds directly on clv-ml-v1 (a model, not a feature or dataset) and feat-clv-hazard, neither of which has been replaced.
Notes: customer-lifetime-value/clv-ml-v2.md

## Q7
Three decision notes rest on ds-cb-spend-panel: dec-cb-extend-flat-pilot, dec-cb-threshold-2500 and dec-cb-adopt-banded-tiers. They reach it through the pilot, spend-band and elasticity notes.
Notes: cashback-redesign/dec-cb-extend-flat-pilot.md, cashback-redesign/dec-cb-threshold-2500.md, cashback-redesign/dec-cb-adopt-banded-tiers.md

## Q8
disp-lgbm-v3 is the note in force (disp-lgbm-v1 was replaced by v2, which was replaced by v3). It is built directly on dec-disp-fraud-score-in, disp-lgbm-v2, exp-307 and feat-disp-fraud-score.
Notes: dispute-triage/disp-lgbm-v3.md, dispute-triage/dec-disp-fraud-score-in.md, dispute-triage/disp-lgbm-v2.md, dispute-triage/exp-307.md, dispute-triage/feat-disp-fraud-score.md

## Q9
Only one note of another project is built directly on feat-fsm-util-ratio: model-monitoring's mm-limit-glm-v2, which uses the store version of the utilisation ratio.
Notes: model-monitoring/mm-limit-glm-v2.md

## Q10
cb-elasticity-v1 rests on ds-cb-pilot-2025q4 (directly) and ds-cb-spend-panel (through feat-cb-spend-base). The graph edges list only feat-cb-spend-base, so these two dataset links come from the note text, not the recorded graph.
Notes: cashback-redesign/ds-cb-pilot-2025q4.md, cashback-redesign/ds-cb-spend-panel.md