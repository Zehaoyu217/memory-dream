## Q1
Four decision notes rest on ds-cr-ivr-paths: dec-cr-lgbm (directly via cr-lgbm-v1 and exp-101), dec-cr-caller-v2, dec-cr-cost-matrix and dec-cr-pilot (all through later models or findings).
Notes: call-center-routing/dec-cr-lgbm.md, call-center-routing/dec-cr-caller-v2.md, call-center-routing/dec-cr-cost-matrix.md, call-center-routing/dec-cr-pilot.md

## Q2
cli-xgb-v3 is in force (cli-xgb-v1 was replaced by cli-xgb-v2, which was replaced by cli-xgb-v3). It builds on exp-107 and find-cli-uplift-wins, and it replaces cli-xgb-v2.
Notes: credit-line-increase/cli-xgb-v3.md, credit-line-increase/exp-107.md, credit-line-increase/find-cli-uplift-wins.md

## Q3
Only merchant-risk/feat-mrisk-dispute-ratio is recorded as built directly on ds-disp-merchant-link. merchant-risk/dec-mrisk-dispute-feature also states a direct dependency on it, but only in its text, not as a recorded link.
Notes: merchant-risk/feat-mrisk-dispute-ratio.md, merchant-risk/dec-mrisk-dispute-feature.md

## Q4
cr-lgbm-v1 rests on two dataset notes: ds-cr-calls (through feat-cr-caller-history-v1, feat-cr-transcript-tfidf-v1 and cr-logreg-v1) and ds-cr-ivr-paths (through feat-cr-ivr-path-v1). exp-101's words about the logistic regression baseline and tenure features map to cr-logreg-v1 and feat-cr-tenure-v1, which are already in that chain.
Notes: call-center-routing/ds-cr-calls.md, call-center-routing/ds-cr-ivr-paths.md

## Q5
The feature notes both models build on directly are feat-f25-amt-ratio, feat-f25-device-age, feat-f25-hour-band and feat-f25-velocity-v1.
Notes: fraud-2025/feat-f25-amt-ratio.md, fraud-2025/feat-f25-device-age.md, fraud-2025/feat-f25-hour-band.md, fraud-2025/feat-f25-velocity-v1.md

## Q6
None. The only current model, clv-ml-v2, builds directly on clv-ml-v1 (a model, not a feature or dataset) and feat-clv-hazard, and neither of those is replaced.
Notes: customer-lifetime-value/clv-ml-v2.md, customer-lifetime-value/feat-clv-hazard.md

## Q7
Three decision notes rest on ds-cb-spend-panel: dec-cb-adopt-banded-tiers and dec-cb-extend-flat-pilot (both superseded), and dec-cb-threshold-2500 (current). Each reaches it through cb-elasticity-v2, find-cb-band-elasticity or find-cb-breakeven-lift.
Notes: cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/dec-cb-extend-flat-pilot.md, cashback-redesign/dec-cb-threshold-2500.md

## Q8
disp-lgbm-v3 is in force (disp-lgbm-v1 was replaced by disp-lgbm-v2, which was replaced by disp-lgbm-v3). It builds on dec-disp-fraud-score-in, exp-307 and feat-disp-fraud-score, and it replaces disp-lgbm-v2.
Notes: dispute-triage/disp-lgbm-v3.md, dispute-triage/dec-disp-fraud-score-in.md, dispute-triage/exp-307.md, dispute-triage/feat-disp-fraud-score.md

## Q9
Only model-monitoring/mm-limit-glm-v2 is built directly on feat-fsm-util-ratio from another project. The other "util ratio" hits in the memory folder are different features (cli_util_ratio, bur_util_ratio).
Notes: model-monitoring/mm-limit-glm-v2.md

## Q10
cb-elasticity-v1 rests on two dataset notes: ds-cb-pilot-2025q4 (directly) and ds-cb-spend-panel (directly via feat-cb-spend-base, and via ds-cb-pilot-2025q4).
Notes: cashback-redesign/ds-cb-pilot-2025q4.md, cashback-redesign/ds-cb-spend-panel.md