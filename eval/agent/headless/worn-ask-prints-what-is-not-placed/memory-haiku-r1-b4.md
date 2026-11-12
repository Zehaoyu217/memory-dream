## Q1
Four decision notes rest on ds-cr-ivr-paths: dec-cr-lgbm, dec-cr-caller-v2, dec-cr-cost-matrix and dec-cr-pilot. Each reaches it through feat-cr-ivr-path-v1 or another model or experiment built on that feature.
Notes: call-center-routing/dec-cr-lgbm.md, call-center-routing/dec-cr-caller-v2.md, call-center-routing/dec-cr-cost-matrix.md, call-center-routing/dec-cr-pilot.md

## Q2
The line ends at cli-xgb-v3, which is in force now (cli-xgb-v1 was replaced by v2, and v2 by v3). cli-xgb-v3 builds directly on exp-107 and find-cli-uplift-wins, and it replaces cli-xgb-v2.
Notes: credit-line-increase/cli-xgb-v3.md, credit-line-increase/exp-107.md, credit-line-increase/find-cli-uplift-wins.md, credit-line-increase/cli-xgb-v2.md

## Q3
Only one note in another project builds directly on ds-disp-merchant-link: merchant-risk/feat-mrisk-dispute-ratio. The other direct child, feat-disp-merchant-cb-rate, is in dispute-triage itself.
Notes: merchant-risk/feat-mrisk-dispute-ratio.md

## Q4
cr-lgbm-v1 rests on two dataset notes: ds-cr-calls and ds-cr-ivr-paths. It reaches ds-cr-calls through feat-cr-caller-history-v1, feat-cr-transcript-tfidf-v1 and cr-logreg-v1, and ds-cr-ivr-paths through feat-cr-ivr-path-v1.
Notes: call-center-routing/ds-cr-calls.md, call-center-routing/ds-cr-ivr-paths.md

## Q5
fraud25-gbm-v1 and fraud25-gbm-v2 both build directly on four feature notes: feat-f25-amt-ratio, feat-f25-device-age, feat-f25-hour-band and feat-f25-velocity-v1.
Notes: fraud-2025/feat-f25-amt-ratio.md, fraud-2025/feat-f25-device-age.md, fraud-2025/feat-f25-hour-band.md, fraud-2025/feat-f25-velocity-v1.md

## Q6
None. The only current CLV model is clv-ml-v2, and it builds directly on clv-ml-v1 (a model, not a feature or dataset) and feat-clv-hazard, which has not been replaced.
Notes: customer-lifetime-value/clv-ml-v2.md

## Q7
Three decision notes rest on ds-cb-spend-panel: dec-cb-adopt-banded-tiers, dec-cb-extend-flat-pilot and dec-cb-threshold-2500.
Notes: cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/dec-cb-extend-flat-pilot.md, cashback-redesign/dec-cb-threshold-2500.md

## Q8
The line ends at disp-lgbm-v3, which is in force now (v1 was replaced by v2, and v2 by v3). disp-lgbm-v3 builds directly on dec-disp-fraud-score-in, exp-307 and feat-disp-fraud-score, and it replaces disp-lgbm-v2.
Notes: dispute-triage/disp-lgbm-v3.md, dispute-triage/dec-disp-fraud-score-in.md, dispute-triage/disp-lgbm-v2.md, dispute-triage/exp-307.md, dispute-triage/feat-disp-fraud-score.md

## Q9
Only one note in another project builds directly on feat-fsm-util-ratio: model-monitoring/mm-limit-glm-v2.
Notes: model-monitoring/mm-limit-glm-v2.md

## Q10
cb-elasticity-v1 rests on two dataset notes: ds-cb-pilot-2025q4 (directly) and ds-cb-spend-panel (directly, and also through feat-cb-spend-base).
Notes: cashback-redesign/ds-cb-pilot-2025q4.md, cashback-redesign/ds-cb-spend-panel.md