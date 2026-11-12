## Q1
Four decision notes rest on ds-cr-ivr-paths: dec-cr-lgbm, dec-cr-caller-v2, dec-cr-cost-matrix and dec-cr-pilot. The first builds on it directly through cr-lgbm-v1. The other three reach it through the same chain of models and experiments.
Notes: call-center-routing/dec-cr-lgbm.md, call-center-routing/dec-cr-caller-v2.md, call-center-routing/dec-cr-cost-matrix.md, call-center-routing/dec-cr-pilot.md

## Q2
cli-xgb-v3 is in force: it replaced cli-xgb-v2, which had replaced cli-xgb-v1. It builds on exp-107 and find-cli-uplift-wins.
Notes: credit-line-increase/cli-xgb-v3.md, credit-line-increase/exp-107.md, credit-line-increase/find-cli-uplift-wins.md

## Q3
Only one note from another project builds directly on ds-disp-merchant-link: merchant-risk's feat-mrisk-dispute-ratio.
Notes: merchant-risk/feat-mrisk-dispute-ratio.md

## Q4
cr-lgbm-v1 rests on two dataset notes, ds-cr-calls and ds-cr-ivr-paths. It reaches ds-cr-calls through feat-cr-caller-history-v1 and ds-cr-ivr-paths through feat-cr-ivr-path-v1.
Notes: call-center-routing/ds-cr-calls.md, call-center-routing/ds-cr-ivr-paths.md

## Q5
Both fraud25-gbm-v1 and fraud25-gbm-v2 build directly on four features: the amount-to-median ratio, device age, authorisation hour band and velocity v1.
Notes: fraud-2025/feat-f25-amt-ratio.md, fraud-2025/feat-f25-device-age.md, fraud-2025/feat-f25-hour-band.md, fraud-2025/feat-f25-velocity-v1.md

## Q6
None. The only current customer-lifetime-value model with a direct link to a replaced note is clv-ml-v2, which builds on clv-ml-v1. That is a model, not a feature or dataset.
Notes: customer-lifetime-value/clv-ml-v2.md, customer-lifetime-value/clv-ml-v1.md

## Q7
Three decision notes rest on ds-cb-spend-panel: dec-cb-threshold-2500 and dec-cb-adopt-banded-tiers through cb-elasticity-v1, and dec-cb-extend-flat-pilot through find-cb-flat-wins. None of them builds on it directly.
Notes: cashback-redesign/dec-cb-threshold-2500.md, cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/dec-cb-extend-flat-pilot.md

## Q8
disp-lgbm-v3 is in force: it replaced disp-lgbm-v2, which had replaced disp-lgbm-v1. It builds on dec-disp-fraud-score-in, disp-lgbm-v2, exp-307 and feat-disp-fraud-score.
Notes: dispute-triage/disp-lgbm-v3.md, dispute-triage/dec-disp-fraud-score-in.md, dispute-triage/disp-lgbm-v2.md, dispute-triage/exp-307.md, dispute-triage/feat-disp-fraud-score.md

## Q9
Two notes from other projects build directly on feat-fsm-util-ratio: model-monitoring's mm-limit-glm-v2 is one. The other is the feature-store-migration note fsm-churn-xgb-v2, which is in the same project, so it does not count here.
Notes: model-monitoring/mm-limit-glm-v2.md

## Q10
cb-elasticity-v1 rests on two dataset notes: ds-cb-pilot-2025q4 directly, and ds-cb-spend-panel through ds-cb-pilot-2025q4.
Notes: cashback-redesign/ds-cb-pilot-2025q4.md, cashback-redesign/ds-cb-spend-panel.md