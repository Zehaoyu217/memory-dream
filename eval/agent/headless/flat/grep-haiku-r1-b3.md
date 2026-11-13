## Q1
Only dec-cr-lgbm is confirmed to rest on ds-cr-ivr-paths, through cr-lgbm-v1 and feat-cr-ivr-path-v1. dec-cr-pilot and dec-cr-cost-matrix sit on cr-lgbm-v3, and I did not trace whether its v2 ancestor uses ivr-paths. dec-cr-caller-v2 is unresolved because the note I expected for its "out-of-time router check" (fnd-cr-leak-v1) has a different title.
Notes: work/ds-cr-ivr-paths.md, work/feat-cr-ivr-path-v1.md, work/cr-lgbm-v1.md, work/dec-cr-lgbm.md, work/dec-cr-pilot.md, work/dec-cr-cost-matrix.md, work/cr-lgbm-v3.md

## Q2
cli-xgb-v1 says it is superseded by cli-xgb-v2, and the note in force is cli-xgb-v3, which replaces v2. cli-xgb-v3 builds on the out-of-time AUC check for v2 (exp-106-credit-line-increase), exp-107-credit-line-increase and find-cli-uplift-wins.
Notes: work/cli-xgb-v1.md, work/cli-xgb-v2.md, work/cli-xgb-v3.md, work/exp-106-credit-line-increase.md, work/exp-107-credit-line-increase.md, work/find-cli-uplift-wins.md

## Q3
cr-lgbm-v1 rests on two dataset notes: ds-cr-ivr-paths directly (through feat-cr-ivr-path-v1), and ds-cr-calls, which is the "inbound calls table" that ds-cr-ivr-paths builds on. I did not trace the datasets behind its other feature notes (caller history, tenure and transcript TF-IDF).
Notes: work/ds-cr-ivr-paths.md, work/ds-cr-calls.md, work/cr-lgbm-v1.md

## Q4
The four feature notes both fraud25-gbm-v1 and fraud25-gbm-v2 build on directly are the amount-to-median ratio, device age, authorisation hour band and velocity features. The titles match the descriptions in both models. v2 also uses feat-f25-mcc-travel, but v1 does not.
Notes: work/feat-f25-amt-ratio.md, work/feat-f25-device-age.md, work/feat-f25-hour-band.md, work/feat-f25-velocity-v1.md, work/fraud25-gbm-v1.md, work/fraud25-gbm-v2.md

## Q5
Three decision notes rest on ds-cb-spend-panel: dec-cb-adopt-banded-tiers, dec-cb-threshold-2500 and dec-cb-extend-flat-pilot. The first two go through cb-elasticity-v2 and cb-elasticity-v1 to feat-cb-spend-base. dec-cb-extend-flat-pilot goes through find-cb-flat-wins, which builds on cb-elasticity-v1.
Notes: work/ds-cb-spend-panel.md, work/feat-cb-spend-base.md, work/cb-elasticity-v1.md, work/cb-elasticity-v2.md, work/find-cb-flat-wins.md, work/dec-cb-adopt-banded-tiers.md, work/dec-cb-threshold-2500.md, work/dec-cb-extend-flat-pilot.md

## Q6
disp-lgbm-v1 says it is superseded by disp-lgbm-v2, and the note in force is disp-lgbm-v3. disp-lgbm-v3 builds on dec-disp-fraud-score-in, disp-lgbm-v2, exp-307-dispute-triage and feat-disp-fraud-score.
Notes: work/disp-lgbm-v1.md, work/disp-lgbm-v2.md, work/disp-lgbm-v3.md, work/dec-disp-fraud-score-in.md, work/exp-307-dispute-triage.md, work/feat-disp-fraud-score.md

## Q7
cb-elasticity-v1 rests on two dataset notes: ds-cb-pilot-2025q4 directly, and ds-cb-spend-panel, which both ds-cb-pilot-2025q4 and feat-cb-spend-base build on.
Notes: work/ds-cb-pilot-2025q4.md, work/ds-cb-spend-panel.md, work/cb-elasticity-v1.md

## Q8
Three feature notes are shared directly by mq3-response-gbm-v1 and mq3-uplift-tlearner-v1: feat-mq3-app-sessions-30d, feat-mq3-prior-treat and feat-mq3-recency-v1. The response model also uses the 90-day email opens feature, which the uplift model does not.
Notes: work/feat-mq3-app-sessions-30d.md, work/feat-mq3-prior-treat.md, work/feat-mq3-recency-v1.md, work/mq3-response-gbm-v1.md, work/mq3-uplift-tlearner-v1.md

## Q9
Four decision notes rest on ds-cb-call-linkage: dec-cb-metric-24h directly, and dec-cb-metric-48h, dec-cb-handoff-v2 and dec-cb-rollout-60 through the experiments and findings that build on it. The links go through exp-306 (for fnd-cb-def-sensitivity), exp-307 (for fnd-cb-repeat-contact) and fnd-cb-volume-shift. This closes the open Q9 references.
Notes: work/ds-cb-call-linkage.md, work/dec-cb-metric-24h.md, work/dec-cb-metric-48h.md, work/dec-cb-handoff-v2.md, work/dec-cb-rollout-60.md, work/fnd-cb-def-sensitivity.md, work/fnd-cb-repeat-contact.md, work/exp-306-chatbot-deflection.md, work/exp-307-chatbot-deflection.md, work/fnd-cb-volume-shift.md

## Q10
ed-gbm-v1 says it is superseded by ed-gbm-v2, and the note in force is ed-gbm-v3. ed-gbm-v3 builds on ed-gbm-v2, exp-207-early-delinquency (the bureau slope experiment) and feat-ed-bureau-slope-v1.
Notes: work/ed-gbm-v1.md, work/ed-gbm-v2.md, work/ed-gbm-v3.md, work/exp-207-early-delinquency.md, work/feat-ed-bureau-slope-v1.md