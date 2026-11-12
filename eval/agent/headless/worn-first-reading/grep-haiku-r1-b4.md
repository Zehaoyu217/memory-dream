## Q1
All four decision notes rest on ds-cr-ivr-paths. dec-cr-lgbm builds directly on cr-lgbm-v1, which uses feat-cr-ivr-path-v1. dec-cr-caller-v2 gets there through fnd-cr-leak-corrected and exp-104, and dec-cr-cost-matrix and dec-cr-pilot through cr-lgbm-v3.
Notes: call-center-routing/dec-cr-lgbm.md, call-center-routing/dec-cr-caller-v2.md, call-center-routing/dec-cr-cost-matrix.md, call-center-routing/dec-cr-pilot.md

## Q2
The note in force at the end of that line is cli-xgb-v3, the two-model uplift score. It builds on exp-106 (the out-of-time AUC check for v2), exp-107 and find-cli-uplift-wins.
Notes: credit-line-increase/cli-xgb-v3.md, credit-line-increase/exp-106.md, credit-line-increase/exp-107.md, credit-line-increase/find-cli-uplift-wins.md

## Q3
Only merchant-risk/feat-mrisk-dispute-ratio builds directly on ds-disp-merchant-link. dec-mrisk-dispute-feature names that dataset as a dependency but does not list it under "Builds on".
Notes: merchant-risk/feat-mrisk-dispute-ratio.md

## Q4
cr-lgbm-v1 rests on two dataset notes: ds-cr-calls, which underlies every feature, and ds-cr-ivr-paths, which feeds the IVR path feature through feat-cr-ivr-path-v1.
Notes: call-center-routing/ds-cr-calls.md, call-center-routing/ds-cr-ivr-paths.md

## Q5
Both fraud25-gbm-v1 and fraud25-gbm-v2 build directly on the amount-ratio, device-age, hour-band and velocity-v1 feature notes.
Notes: fraud-2025/feat-f25-amt-ratio.md, fraud-2025/feat-f25-device-age.md, fraud-2025/feat-f25-hour-band.md, fraud-2025/feat-f25-velocity-v1.md

## Q6
clv-bgnbd-v1 is the only current model that builds directly on a replaced note. It uses feat-clv-arpu-v1, the six-month revenue feature that feat-clv-arpu-v2 replaced, and it is still kept as the marketing sanity check.
Notes: customer-lifetime-value/clv-bgnbd-v1.md

## Q7
Three decision notes rest on ds-cb-spend-panel. dec-cb-extend-flat-pilot goes through find-cb-flat-wins, exp-201 and ds-cb-pilot-2025q4. dec-cb-adopt-banded-tiers goes through cb-elasticity-v2 and feat-cb-grocery-share, and dec-cb-threshold-2500 builds on dec-cb-adopt-banded-tiers.
Notes: cashback-redesign/dec-cb-extend-flat-pilot.md, cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/dec-cb-threshold-2500.md

## Q8
The note in force at the end of that line is disp-lgbm-v3, the fraud-score model that replaced v2. It builds on dec-disp-fraud-score-in, disp-lgbm-v2, exp-307 and feat-disp-fraud-score.
Notes: dispute-triage/disp-lgbm-v3.md, dispute-triage/dec-disp-fraud-score-in.md, dispute-triage/disp-lgbm-v2.md, dispute-triage/exp-307.md, dispute-triage/feat-disp-fraud-score.md

## Q9
Only model-monitoring/mm-limit-glm-v2 builds directly on feat-fsm-util-ratio from another project. The other two notes that use it, exp-105 and fsm-churn-xgb-v2, are in feature-store-migration itself.
Notes: model-monitoring/mm-limit-glm-v2.md

## Q10
cb-elasticity-v1 rests on two dataset notes. ds-cb-pilot-2025q4 is used directly, and ds-cb-spend-panel is reached through feat-cb-spend-base.
Notes: cashback-redesign/ds-cb-pilot-2025q4.md, cashback-redesign/ds-cb-spend-panel.md