## Q1
Four decision notes rest on ds-cr-ivr-paths: dec-cr-lgbm, dec-cr-caller-v2, dec-cr-cost-matrix and dec-cr-pilot. They reach it through feat-cr-ivr-path-v1 into cr-lgbm-v1, which feeds exp-104, fnd-cr-leak-corrected and exp-105, and on to cr-lgbm-v2 and cr-lgbm-v3.
Notes: call-center-routing/dec-cr-lgbm.md, call-center-routing/dec-cr-caller-v2.md, call-center-routing/dec-cr-cost-matrix.md, call-center-routing/dec-cr-pilot.md

## Q2
The note in force is cli-xgb-v3, which supersedes cli-xgb-v2 and replaced cli-xgb-v1. It is built on exp-106, exp-107 and find-cli-uplift-wins.
Notes: credit-line-increase/cli-xgb-v3.md, credit-line-increase/exp-106.md, credit-line-increase/exp-107.md, credit-line-increase/find-cli-uplift-wins.md

## Q3
Only one note from another project is built directly on ds-disp-merchant-link: merchant-risk/feat-mrisk-dispute-ratio. The other direct child, feat-disp-merchant-cb-rate, is in dispute-triage itself.
Notes: merchant-risk/feat-mrisk-dispute-ratio.md

## Q4
cr-lgbm-v1 rests on the dataset notes ds-cr-calls and ds-cr-ivr-paths. ds-cr-calls is the root, and ds-cr-ivr-paths sits under it via feat-cr-ivr-path-v1.
Notes: call-center-routing/ds-cr-calls.md, call-center-routing/ds-cr-ivr-paths.md

## Q5
Both fraud25-gbm-v1 and fraud25-gbm-v2 build directly on feat-f25-amt-ratio, feat-f25-device-age, feat-f25-hour-band and feat-f25-velocity-v1. They also share the ds-f25-labels dataset note, which is not a feature.
Notes: fraud-2025/feat-f25-amt-ratio.md, fraud-2025/feat-f25-device-age.md, fraud-2025/feat-f25-hour-band.md, fraud-2025/feat-f25-velocity-v1.md

## Q6
clv-bgnbd-v1 is still current and builds directly on feat-clv-arpu-v1, which was replaced by feat-clv-arpu-v2. The other current model, clv-ml-v2, builds only on current features.
Notes: customer-lifetime-value/clv-bgnbd-v1.md, customer-lifetime-value/feat-clv-arpu-v1.md

## Q7
Three decision notes rest on ds-cb-spend-panel: dec-cb-adopt-banded-tiers, dec-cb-extend-flat-pilot and dec-cb-threshold-2500. They reach it through find-cb-flat-wins, exp-202-tier-pilot and the elasticity and breakeven notes.
Notes: cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/dec-cb-extend-flat-pilot.md, cashback-redesign/dec-cb-threshold-2500.md

## Q8
The note in force is disp-lgbm-v3, which supersedes disp-lgbm-v2 and replaced disp-lgbm-v1. It is built on disp-lgbm-v2, feat-disp-fraud-score, exp-307 and dec-disp-fraud-score-in.
Notes: dispute-triage/disp-lgbm-v3.md, dispute-triage/disp-lgbm-v2.md, dispute-triage/feat-disp-fraud-score.md, dispute-triage/exp-307.md, dispute-triage/dec-disp-fraud-score-in.md

## Q9
Only one note from another project is built directly on feat-fsm-util-ratio: model-monitoring/mm-limit-glm-v2.
Notes: model-monitoring/mm-limit-glm-v2.md

## Q10
cb-elasticity-v1 rests on the dataset notes ds-cb-spend-panel and ds-cb-pilot-2025q4. It uses feat-cb-spend-base directly, and both feat-cb-spend-base and ds-cb-pilot-2025q4 trace back to ds-cb-spend-panel.
Notes: cashback-redesign/ds-cb-spend-panel.md, cashback-redesign/ds-cb-pilot-2025q4.md