## Q1
disp-lgbm-v3 is the one in force. It replaced disp-lgbm-v2, which had replaced disp-lgbm-v1, and it builds on dec-disp-fraud-score-in, disp-lgbm-v2, exp-307-dispute-triage and feat-disp-fraud-score.
Notes: work/disp-lgbm-v3.md, work/dec-disp-fraud-score-in.md, work/disp-lgbm-v2.md, work/exp-307-dispute-triage.md, work/feat-disp-fraud-score.md

## Q2
cb-elasticity-v1 rests on two dataset notes: ds-cb-pilot-2025q4 directly, and ds-cb-spend-panel through feat-cb-spend-base. Neither dataset note names a further note as its source, so the chain ends there.
Notes: work/cb-elasticity-v1.md, work/feat-cb-spend-base.md, work/ds-cb-pilot-2025q4.md, work/ds-cb-spend-panel.md

## Q3
Both models build directly on feat-mq3-app-sessions-30d, feat-mq3-prior-treat and feat-mq3-recency-v1.
Notes: work/mq3-response-gbm-v1.md, work/mq3-uplift-tlearner-v1.md, work/feat-mq3-app-sessions-30d.md, work/feat-mq3-prior-treat.md, work/feat-mq3-recency-v1.md

## Q4
Four decisions rest on ds-cb-call-linkage. dec-cb-metric-24h builds on it directly. dec-cb-metric-48h rests on it through fnd-cb-def-sensitivity and fnd-cb-repeat-contact, dec-cb-rollout-60 through fnd-cb-volume-shift, and dec-cb-handoff-v2 through fnd-cb-repeat-contact.
Notes: work/dec-cb-metric-24h.md, work/dec-cb-metric-48h.md, work/dec-cb-rollout-60.md, work/dec-cb-handoff-v2.md, work/ds-cb-call-linkage.md, work/exp-306-chatbot-deflection.md, work/fnd-cb-def-sensitivity.md, work/exp-307-chatbot-deflection.md, work/fnd-cb-repeat-contact.md, work/fnd-cb-volume-shift.md

## Q5
ed-gbm-v3 is the one in force. It replaced ed-gbm-v2, which had replaced ed-gbm-v1, and it builds on ed-gbm-v2, exp-207-early-delinquency (the bureau slope lift experiment) and feat-ed-bureau-slope-v1.
Notes: work/ed-gbm-v3.md, work/ed-gbm-v2.md, work/exp-207-early-delinquency.md, work/feat-ed-bureau-slope-v1.md