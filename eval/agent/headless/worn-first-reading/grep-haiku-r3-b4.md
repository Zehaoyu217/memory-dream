## Q1
Four decision notes rest on ds-cr-ivr-paths: dec-cr-lgbm (via cr-lgbm-v1 and feat-cr-ivr-path-v1), dec-cr-cost-matrix and dec-cr-pilot (via cr-lgbm-v3, which descends from cr-lgbm-v1 through cr-lgbm-v2 and exp-105), and dec-cr-caller-v2 (via fnd-cr-leak-corrected, which builds on exp-104, a read of cr-lgbm-v1).
Notes: call-center-routing/dec-cr-lgbm.md, call-center-routing/dec-cr-caller-v2.md, call-center-routing/dec-cr-cost-matrix.md, call-center-routing/dec-cr-pilot.md

## Q2
cli-xgb-v3 is the note in force: it replaces cli-xgb-v2, which had replaced cli-xgb-v1. cli-xgb-v3 builds on exp-106 (the out-of-time AUC check for v2), exp-107 and find-cli-uplift-wins.
Notes: credit-line-increase/cli-xgb-v3.md, credit-line-increase/exp-106.md, credit-line-increase/exp-107.md, credit-line-increase/find-cli-uplift-wins.md

## Q3
Only one note in another project builds directly on ds-disp-merchant-link: merchant-risk's feat-mrisk-dispute-ratio.
Notes: merchant-risk/feat-mrisk-dispute-ratio.md

## Q4
cr-lgbm-v1 rests on two dataset notes: ds-cr-calls (through feat-cr-caller-history-v1 and feat-cr-transcript-tfidf-v1) and ds-cr-ivr-paths (through feat-cr-ivr-path-v1).
Notes: call-center-routing/ds-cr-calls.md, call-center-routing/ds-cr-ivr-paths.md

## Q5
Both fraud25-gbm-v1 and fraud25-gbm-v2 build directly on four feature notes: feat-f25-amt-ratio, feat-f25-device-age, feat-f25-hour-band and feat-f25-velocity-v1.
Notes: fraud-2025/feat-f25-amt-ratio.md, fraud-2025/feat-f25-device-age.md, fraud-2025/feat-f25-hour-band.md, fraud-2025/feat-f25-velocity-v1.md

## Q6
clv-bgnbd-v1 is the only current model that builds directly on a replaced feature. It builds on feat-clv-arpu-v1, which was replaced by feat-clv-arpu-v2. I counted it as current because no note supersedes it, although it is now only a marketing sanity check. clv-ml-v2 uses only current features.
Notes: customer-lifetime-value/clv-bgnbd-v1.md, customer-lifetime-value/feat-clv-arpu-v1.md

## Q7
Three decision notes rest on ds-cb-spend-panel: dec-cb-adopt-banded-tiers (via cb-elasticity-v2 and cb-elasticity-v1), dec-cb-extend-flat-pilot (via find-cb-flat-wins, exp-201 and ds-cb-pilot-2025q4), and dec-cb-threshold-2500 (via exp-206, which builds on cb-sim-v1 and then ds-cb-rewards-ledger).
Notes: cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/dec-cb-extend-flat-pilot.md, cashback-redesign/dec-cb-threshold-2500.md

## Q8
disp-lgbm-v3 is the note in force: it replaces disp-lgbm-v2, which had replaced disp-lgbm-v1. disp-lgbm-v3 builds on dec-disp-fraud-score-in, disp-lgbm-v2, exp-307 and feat-disp-fraud-score.
Notes: dispute-triage/disp-lgbm-v3.md, dispute-triage/dec-disp-fraud-score-in.md, dispute-triage/disp-lgbm-v2.md, dispute-triage/exp-307.md, dispute-triage/feat-disp-fraud-score.md

## Q9
Only one note in another project builds directly on feat-fsm-util-ratio: model-monitoring's mm-limit-glm-v2.
Notes: model-monitoring/mm-limit-glm-v2.md

## Q10
cb-elasticity-v1 rests on two dataset notes: ds-cb-pilot-2025q4 (directly, and as the pilot dataset) and ds-cb-spend-panel (through ds-cb-pilot-2025q4 and feat-cb-spend-base).
Notes: cashback-redesign/ds-cb-pilot-2025q4.md, cashback-redesign/ds-cb-spend-panel.md