## Q1
Four decision notes rest on ds-cr-ivr-paths: dec-cr-lgbm, dec-cr-caller-v2, dec-cr-cost-matrix and dec-cr-pilot. All four decisions in call-center-routing are downstream of it.
Notes: call-center-routing/dec-cr-lgbm.md, call-center-routing/dec-cr-caller-v2.md, call-center-routing/dec-cr-cost-matrix.md, call-center-routing/dec-cr-pilot.md

## Q2
cli-xgb-v1 was replaced by cli-xgb-v2, which was replaced by cli-xgb-v3, the note in force now. cli-xgb-v3 is built on exp-106, exp-107 and find-cli-uplift-wins, and it replaces cli-xgb-v2.
Notes: credit-line-increase/cli-xgb-v3.md, credit-line-increase/exp-106.md, credit-line-increase/exp-107.md, credit-line-increase/find-cli-uplift-wins.md

## Q3
Only one note of another project is built directly on ds-disp-merchant-link: merchant-risk/feat-mrisk-dispute-ratio.
Notes: merchant-risk/feat-mrisk-dispute-ratio.md

## Q4
cr-lgbm-v1 rests on two dataset notes: ds-cr-calls directly through cr-logreg-v1 and ds-cr-ivr-paths through feat-cr-ivr-path-v1.
Notes: call-center-routing/ds-cr-calls.md, call-center-routing/ds-cr-ivr-paths.md

## Q5
fraud25-gbm-v1 and fraud25-gbm-v2 both build directly on four feature notes: feat-f25-amt-ratio, feat-f25-device-age, feat-f25-hour-band and feat-f25-velocity-v1.
Notes: fraud-2025/feat-f25-amt-ratio.md, fraud-2025/feat-f25-device-age.md, fraud-2025/feat-f25-hour-band.md, fraud-2025/feat-f25-velocity-v1.md

## Q6
None. The only current model is clv-ml-v2, and it builds on feat-clv-arpu-v2 and feat-clv-hazard, neither of which has been replaced; its other direct input, clv-ml-v1, is a model, not a feature or dataset.
Notes: customer-lifetime-value/clv-ml-v2.md

## Q7
All three decision notes in cashback-redesign rest on ds-cb-spend-panel: dec-cb-adopt-banded-tiers, dec-cb-extend-flat-pilot and dec-cb-threshold-2500. The chain passes through cb-elasticity-v2, find-cb-flat-wins and exp-206-breakeven-sim, among others.
Notes: cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/dec-cb-extend-flat-pilot.md, cashback-redesign/dec-cb-threshold-2500.md

## Q8
disp-lgbm-v1 was replaced by disp-lgbm-v2, which was replaced by disp-lgbm-v3, the note in force now. disp-lgbm-v3 is built on dec-disp-fraud-score-in, disp-lgbm-v2, exp-307 and feat-disp-fraud-score.
Notes: dispute-triage/disp-lgbm-v3.md, dispute-triage/dec-disp-fraud-score-in.md, dispute-triage/disp-lgbm-v2.md, dispute-triage/exp-307.md, dispute-triage/feat-disp-fraud-score.md

## Q9
Only one note of another project is built directly on feat-fsm-util-ratio: model-monitoring/mm-limit-glm-v2.
Notes: model-monitoring/mm-limit-glm-v2.md

## Q10
cb-elasticity-v1 rests on two dataset notes: ds-cb-pilot-2025q4 directly and ds-cb-spend-panel through it and feat-cb-spend-base. The chain stops at ds-cb-spend-panel's inputs, cb_spend_panel.sql and cards.txn_daily, which have no linked notes.
Notes: cashback-redesign/ds-cb-pilot-2025q4.md, cashback-redesign/ds-cb-spend-panel.md