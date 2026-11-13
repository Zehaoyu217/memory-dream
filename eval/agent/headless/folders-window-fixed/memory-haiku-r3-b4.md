## Q1
Four decision notes rest on ds-cr-ivr-paths: dec-cr-lgbm, dec-cr-caller-v2, dec-cr-cost-matrix and dec-cr-pilot. All four reach it through cr-lgbm-v1 or the feature and finding notes built on it.
Notes: call-center-routing/dec-cr-lgbm.md, call-center-routing/dec-cr-caller-v2.md, call-center-routing/dec-cr-cost-matrix.md, call-center-routing/dec-cr-pilot.md

## Q2
cli-xgb-v3 is the note in force at the end of the line (cli-xgb-v1 was replaced by cli-xgb-v2, which was replaced by v3). cli-xgb-v3 is built on exp-106, exp-107 and find-cli-uplift-wins.
Notes: credit-line-increase/cli-xgb-v3.md, credit-line-increase/exp-106.md, credit-line-increase/exp-107.md, credit-line-increase/find-cli-uplift-wins.md

## Q3
Only one note of another project is built directly on ds-disp-merchant-link: merchant-risk/feat-mrisk-dispute-ratio. The merchant-risk decision note dec-mrisk-dispute-feature names the dependency in words but builds directly on feat-mrisk-dispute-ratio, so it is not a direct build.
Notes: merchant-risk/feat-mrisk-dispute-ratio.md

## Q4
cr-lgbm-v1 rests on two dataset notes: ds-cr-calls and ds-cr-ivr-paths. It reaches ds-cr-calls through feat-cr-caller-history-v1 and cr-logreg-v1, and ds-cr-ivr-paths through feat-cr-ivr-path-v1.
Notes: call-center-routing/ds-cr-calls.md, call-center-routing/ds-cr-ivr-paths.md

## Q5
Both fraud25-gbm-v1 and fraud25-gbm-v2 build directly on four feature notes: feat-f25-amt-ratio, feat-f25-device-age, feat-f25-hour-band and feat-f25-velocity-v1. The label dataset ds-f25-labels is shared too, but it is a dataset, not a feature.
Notes: fraud-2025/feat-f25-amt-ratio.md, fraud-2025/feat-f25-device-age.md, fraud-2025/feat-f25-hour-band.md, fraud-2025/feat-f25-velocity-v1.md

## Q6
None. clv-ml-v2 is the only current model in customer-lifetime-value, and it builds directly on feat-clv-arpu-v2 and feat-clv-hazard, which are both current. Its only replaced input is the model clv-ml-v1, which does not count as a feature or dataset.
Notes: customer-lifetime-value/clv-ml-v2.md

## Q7
Three decision notes rest on ds-cb-spend-panel: dec-cb-adopt-banded-tiers, dec-cb-extend-flat-pilot and dec-cb-threshold-2500. They reach it through cb-elasticity-v2, find-cb-flat-wins, exp-206 and similar notes built on it.
Notes: cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/dec-cb-extend-flat-pilot.md, cashback-redesign/dec-cb-threshold-2500.md

## Q8
disp-lgbm-v3 is the note in force (disp-lgbm-v1 was replaced by disp-lgbm-v2, which was replaced by v3). disp-lgbm-v3 is built on dec-disp-fraud-score-in, disp-lgbm-v2, exp-307 and feat-disp-fraud-score.
Notes: dispute-triage/disp-lgbm-v3.md, dispute-triage/dec-disp-fraud-score-in.md, dispute-triage/disp-lgbm-v2.md, dispute-triage/exp-307.md, dispute-triage/feat-disp-fraud-score.md

## Q9
Only one note of another project is built directly on feat-fsm-util-ratio: model-monitoring/mm-limit-glm-v2. The other notes that cite it (exp-105 and fsm-churn-xgb-v2) are in feature-store-migration itself.
Notes: model-monitoring/mm-limit-glm-v2.md

## Q10
cb-elasticity-v1 rests directly on ds-cb-pilot-2025q4 and feat-cb-spend-base, and through feat-cb-spend-base on ds-cb-spend-panel. The chain stops there: ds-cb-spend-panel is built from cards.txn_daily and cb_spend_panel.sql, and neither has a note in memory.
Notes: cashback-redesign/ds-cb-pilot-2025q4.md, cashback-redesign/ds-cb-spend-panel.md