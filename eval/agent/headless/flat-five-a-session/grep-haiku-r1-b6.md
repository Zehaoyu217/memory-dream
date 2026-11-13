## Q1
disp-lgbm-v3 is the note in force; it replaced disp-lgbm-v2, which replaced disp-lgbm-v1. disp-lgbm-v3 is built on disp-lgbm-v2, dec-disp-fraud-score-in, exp-307-dispute-triage and feat-disp-fraud-score.
Notes: work/disp-lgbm-v1.md, work/disp-lgbm-v2.md, work/disp-lgbm-v3.md, work/dec-disp-fraud-score-in.md, work/exp-307-dispute-triage.md, work/feat-disp-fraud-score.md

## Q2
cb-elasticity-v1 rests directly on the 2025 Q4 cashback pilot dataset (ds-cb-pilot-2025q4) and feat-cb-spend-base. Both trace back to the monthly spend panel dataset (ds-cb-spend-panel).
Notes: work/cb-elasticity-v1.md, work/ds-cb-pilot-2025q4.md, work/feat-cb-spend-base.md, work/ds-cb-spend-panel.md

## Q3
Both mq3-response-gbm-v1 and mq3-uplift-tlearner-v1 build directly on feat-mq3-app-sessions-30d (30-day app sessions), feat-mq3-prior-treat (prior campaign contact) and feat-mq3-recency-v1 (recency).
Notes: work/feat-mq3-app-sessions-30d.md, work/feat-mq3-prior-treat.md, work/feat-mq3-recency-v1.md, work/mq3-response-gbm-v1.md, work/mq3-uplift-tlearner-v1.md

## Q4
Four decisions rest on ds-cb-call-linkage. dec-cb-metric-24h builds on it directly. dec-cb-metric-48h gets there through fnd-cb-def-sensitivity (exp-306) and fnd-cb-repeat-contact (exp-307). dec-cb-handoff-v2 gets there through fnd-cb-repeat-contact. dec-cb-rollout-60 gets there through fnd-cb-volume-shift.
Notes: work/dec-cb-metric-24h.md, work/dec-cb-metric-48h.md, work/dec-cb-handoff-v2.md, work/dec-cb-rollout-60.md, work/ds-cb-call-linkage.md, work/exp-306-chatbot-deflection.md, work/exp-307-chatbot-deflection.md, work/fnd-cb-def-sensitivity.md, work/fnd-cb-repeat-contact.md, work/fnd-cb-volume-shift.md

## Q5
ed-gbm-v3 is the note in force; it replaced ed-gbm-v2, which replaced ed-gbm-v1. ed-gbm-v3 is built on ed-gbm-v2, the bureau slope lift experiment (exp-207-early-delinquency) and feat-ed-bureau-slope-v1.
Notes: work/ed-gbm-v1.md, work/ed-gbm-v2.md, work/ed-gbm-v3.md, work/exp-207-early-delinquency.md, work/feat-ed-bureau-slope-v1.md