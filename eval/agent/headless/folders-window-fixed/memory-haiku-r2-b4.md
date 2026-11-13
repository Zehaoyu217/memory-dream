## Q1
Four decision notes rest on ds-cr-ivr-paths: dec-cr-lgbm, dec-cr-caller-v2, dec-cr-cost-matrix and dec-cr-pilot. They reach it through feat-cr-ivr-path-v1 and the LightGBM router chain (cr-lgbm-v1 and its successors).
Notes: call-center-routing/dec-cr-lgbm.md, call-center-routing/dec-cr-caller-v2.md, call-center-routing/dec-cr-cost-matrix.md, call-center-routing/dec-cr-pilot.md

## Q2
The note in force at the end of the cli-xgb-v1 line is cli-xgb-v3 (cli-xgb-v1 was replaced by v2, which was replaced by v3). cli-xgb-v3 is built on exp-106, exp-107 and find-cli-uplift-wins.
Notes: credit-line-increase/cli-xgb-v3.md, credit-line-increase/exp-106.md, credit-line-increase/exp-107.md, credit-line-increase/find-cli-uplift-wins.md

## Q3
Only one note from another project was built directly on ds-disp-merchant-link: merchant-risk/feat-mrisk-dispute-ratio, which cites it as its source.
Notes: merchant-risk/feat-mrisk-dispute-ratio.md

## Q4
cr-lgbm-v1 rests on two dataset notes: ds-cr-calls (through feat-cr-caller-history-v1 and feat-cr-transcript-tfidf-v1) and ds-cr-ivr-paths (through feat-cr-ivr-path-v1).
Notes: call-center-routing/ds-cr-calls.md, call-center-routing/ds-cr-ivr-paths.md

## Q5
Both fraud25-gbm-v1 and fraud25-gbm-v2 build directly on four feature notes: amount ratio, device age, hour band and velocity-v1.
Notes: fraud-2025/feat-f25-amt-ratio.md, fraud-2025/feat-f25-device-age.md, fraud-2025/feat-f25-hour-band.md, fraud-2025/feat-f25-velocity-v1.md

## Q6
None. The only current model in customer-lifetime-value is clv-ml-v2, and it builds directly on feat-clv-arpu-v2 and feat-clv-hazard, neither of which has been replaced.
Notes: customer-lifetime-value/clv-ml-v2.md

## Q7
Three decision notes rest on ds-cb-spend-panel: dec-cb-adopt-banded-tiers, dec-cb-extend-flat-pilot and dec-cb-threshold-2500. The chain is incomplete, because ds-cb-spend-panel's raw source cards.txn_daily has no note and one other note cites an unplaced source.
Notes: cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/dec-cb-extend-flat-pilot.md, cashback-redesign/dec-cb-threshold-2500.md

## Q8
The note in force at the end of the disp-lgbm-v1 line is disp-lgbm-v3 (v1 was replaced by v2, which was replaced by v3). disp-lgbm-v3 is built on dec-disp-fraud-score-in, disp-lgbm-v2, exp-307 and feat-disp-fraud-score.
Notes: dispute-triage/disp-lgbm-v3.md, dispute-triage/dec-disp-fraud-score-in.md, dispute-triage/disp-lgbm-v2.md, dispute-triage/exp-307.md, dispute-triage/feat-disp-fraud-score.md

## Q9
One note from another project was built directly on feat-fsm-util-ratio: model-monitoring/mm-limit-glm-v2, which uses it in place of the legacy utilisation field.
Notes: model-monitoring/mm-limit-glm-v2.md

## Q10
cb-elasticity-v1 rests on two dataset notes: ds-cb-pilot-2025q4 directly, and ds-cb-spend-panel through feat-cb-spend-base. The spend panel's raw source, cards.txn_daily, is named in text but has no note, so the chain stops there.
Notes: cashback-redesign/ds-cb-pilot-2025q4.md, cashback-redesign/ds-cb-spend-panel.md