## Q1
Four decision notes rest on ds-cr-ivr-paths: dec-cr-lgbm directly through cr-lgbm-v1 and the IVR path feature, and dec-cr-caller-v2, dec-cr-cost-matrix and dec-cr-pilot through the later router and caller-history notes.
Notes: call-center-routing/dec-cr-lgbm.md, call-center-routing/dec-cr-caller-v2.md, call-center-routing/dec-cr-cost-matrix.md, call-center-routing/dec-cr-pilot.md

## Q2
cli-xgb-v1 was superseded by cli-xgb-v2, which was superseded by cli-xgb-v3, and cli-xgb-v3 is in force. It was built on exp-106, exp-107 and find-cli-uplift-wins.
Notes: credit-line-increase/cli-xgb-v3.md, credit-line-increase/exp-106.md, credit-line-increase/exp-107.md, credit-line-increase/find-cli-uplift-wins.md

## Q3
One note of another project was built directly on ds-disp-merchant-link: feat-mrisk-dispute-ratio in merchant-risk.
Notes: merchant-risk/feat-mrisk-dispute-ratio.md

## Q4
cr-lgbm-v1 rests on two dataset notes: ds-cr-calls, and ds-cr-ivr-paths, which is built on ds-cr-calls.
Notes: call-center-routing/ds-cr-calls.md, call-center-routing/ds-cr-ivr-paths.md

## Q5
Both fraud25-gbm-v1 and fraud25-gbm-v2 build directly on four feature notes: the amount-to-median ratio, device age, hour band and velocity-v1 features.
Notes: fraud-2025/feat-f25-amt-ratio.md, fraud-2025/feat-f25-device-age.md, fraud-2025/feat-f25-hour-band.md, fraud-2025/feat-f25-velocity-v1.md

## Q6
None. clv-ml-v2 is the only current model in customer-lifetime-value, and it builds directly on clv-ml-v1 (superseded, but a model, not a feature or dataset), exp-505, feat-clv-arpu-v2 and feat-clv-hazard, none of which is marked as replaced.
Notes: customer-lifetime-value/clv-ml-v2.md

## Q7
Three decision notes rest on ds-cb-spend-panel: dec-cb-adopt-banded-tiers, dec-cb-extend-flat-pilot and dec-cb-threshold-2500. The chain is incomplete because ds-cb-spend-panel's inputs (cb_spend_panel.sql, cards.txn_daily) have no notes, so a decision resting on those could be missed.
Notes: cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/dec-cb-extend-flat-pilot.md, cashback-redesign/dec-cb-threshold-2500.md

## Q8
disp-lgbm-v1 was superseded by disp-lgbm-v2, which was superseded by disp-lgbm-v3, and disp-lgbm-v3 is in force. It was built on dec-disp-fraud-score-in, disp-lgbm-v2, exp-307 and feat-disp-fraud-score.
Notes: dispute-triage/disp-lgbm-v3.md, dispute-triage/dec-disp-fraud-score-in.md, dispute-triage/disp-lgbm-v2.md, dispute-triage/exp-307.md, dispute-triage/feat-disp-fraud-score.md

## Q9
One note of another project was built directly on feat-fsm-util-ratio: mm-limit-glm-v2 in model-monitoring.
Notes: model-monitoring/mm-limit-glm-v2.md

## Q10
cb-elasticity-v1 rests on two dataset notes: ds-cb-pilot-2025q4 directly, and ds-cb-spend-panel directly and through feat-cb-spend-base. The chain stops at ds-cb-spend-panel's unlinked inputs (cb_spend_panel.sql, cards.txn_daily).
Notes: cashback-redesign/ds-cb-pilot-2025q4.md, cashback-redesign/ds-cb-spend-panel.md