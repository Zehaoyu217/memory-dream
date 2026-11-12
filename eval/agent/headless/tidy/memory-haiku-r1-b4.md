## Q1
Four decision notes rest on ds-cr-ivr-paths: dec-cr-lgbm, dec-cr-caller-v2, dec-cr-cost-matrix and dec-cr-pilot. They reach it through feat-cr-ivr-path-v1 and the models and experiments built on it.
Notes: call-center-routing/dec-cr-lgbm.md, call-center-routing/dec-cr-caller-v2.md, call-center-routing/dec-cr-cost-matrix.md, call-center-routing/dec-cr-pilot.md

## Q2
cli-xgb-v3 is in force at the end of the v1, v2, v3 line. It is built directly on exp-106, exp-107 and find-cli-uplift-wins.
Notes: credit-line-increase/cli-xgb-v3.md, credit-line-increase/exp-106.md, credit-line-increase/exp-107.md, credit-line-increase/find-cli-uplift-wins.md

## Q3
Only merchant-risk/feat-mrisk-dispute-ratio is built directly on ds-disp-merchant-link from another project.
Notes: merchant-risk/feat-mrisk-dispute-ratio.md

## Q4
cr-lgbm-v1 rests on two dataset notes: ds-cr-calls and ds-cr-ivr-paths.
Notes: call-center-routing/cr-lgbm-v1.md, call-center-routing/ds-cr-calls.md, call-center-routing/ds-cr-ivr-paths.md

## Q5
Both fraud25-gbm-v1 and fraud25-gbm-v2 build directly on feat-f25-velocity-v1, feat-f25-device-age, feat-f25-amt-ratio and feat-f25-hour-band. v2 also adds feat-f25-mcc-travel.
Notes: fraud-2025/fraud25-gbm-v1.md, fraud-2025/fraud25-gbm-v2.md, fraud-2025/feat-f25-velocity-v1.md, fraud-2025/feat-f25-device-age.md, fraud-2025/feat-f25-amt-ratio.md, fraud-2025/feat-f25-hour-band.md

## Q6
clv-bgnbd-v1 is the only current model that builds directly on a replaced feature. It uses feat-clv-arpu-v1, which was replaced by feat-clv-arpu-v2.
Notes: customer-lifetime-value/clv-bgnbd-v1.md, customer-lifetime-value/feat-clv-arpu-v1.md, customer-lifetime-value/feat-clv-arpu-v2.md

## Q7
Three decision notes rest on ds-cb-spend-panel: dec-cb-adopt-banded-tiers, dec-cb-extend-flat-pilot and dec-cb-threshold-2500.
Notes: cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/dec-cb-extend-flat-pilot.md, cashback-redesign/dec-cb-threshold-2500.md

## Q8
disp-lgbm-v3 is in force at the end of the v1, v2, v3 line. It is built directly on disp-lgbm-v2, feat-disp-fraud-score, exp-307 and dec-disp-fraud-score-in.
Notes: dispute-triage/disp-lgbm-v3.md, dispute-triage/disp-lgbm-v2.md, dispute-triage/feat-disp-fraud-score.md, dispute-triage/exp-307.md, dispute-triage/dec-disp-fraud-score-in.md

## Q9
Only model-monitoring/mm-limit-glm-v2 is built directly on feat-fsm-util-ratio from another project.
Notes: model-monitoring/mm-limit-glm-v2.md, feature-store-migration/feat-fsm-util-ratio.md

## Q10
cb-elasticity-v1 rests on two dataset notes: ds-cb-pilot-2025q4 directly, and ds-cb-spend-panel through feat-cb-spend-base.
Notes: cashback-redesign/cb-elasticity-v1.md, cashback-redesign/ds-cb-pilot-2025q4.md, cashback-redesign/ds-cb-spend-panel.md