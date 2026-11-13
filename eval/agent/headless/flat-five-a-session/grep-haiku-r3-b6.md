## Q1
disp-lgbm-v3 is in force: v1 was replaced by v2, and v2 by v3. disp-lgbm-v3 is built on dec-disp-fraud-score-in, disp-lgbm-v2, exp-307-dispute-triage and feat-disp-fraud-score.
Notes: work/disp-lgbm-v3.md, work/dec-disp-fraud-score-in.md, work/disp-lgbm-v2.md, work/exp-307-dispute-triage.md, work/feat-disp-fraud-score.md

## Q2
cb-elasticity-v1 rests on two datasets: ds-cb-pilot-2025q4 directly, and ds-cb-spend-panel, which sits behind both the pilot note and feat-cb-spend-base. ds-cb-spend-panel has no further builds-on, so it is the start of the chain.
Notes: work/cb-elasticity-v1.md, work/feat-cb-spend-base.md, work/ds-cb-pilot-2025q4.md, work/ds-cb-spend-panel.md

## Q3
Both notes build directly on feat-mq3-app-sessions-30d, feat-mq3-prior-treat and feat-mq3-recency-v1.
Notes: work/mq3-response-gbm-v1.md, work/mq3-uplift-tlearner-v1.md, work/feat-mq3-app-sessions-30d.md, work/feat-mq3-prior-treat.md, work/feat-mq3-recency-v1.md

## Q4
Four decisions rest on ds-cb-call-linkage: dec-cb-metric-24h (direct), dec-cb-metric-48h (via fnd-cb-def-sensitivity, from exp-306), dec-cb-handoff-v2 (via fnd-cb-repeat-contact, from exp-307), and dec-cb-rollout-60 (via fnd-cb-volume-shift and dec-cb-handoff-v2). The links to exp-306 and exp-307 are inferred from the notes' wording ("containment window replay", "same-intent repeat call check"), not from an explicit builds-on name.
Notes: work/dec-cb-metric-24h.md, work/dec-cb-metric-48h.md, work/dec-cb-handoff-v2.md, work/dec-cb-rollout-60.md, work/ds-cb-call-linkage.md, work/exp-306-chatbot-deflection.md, work/fnd-cb-def-sensitivity.md, work/exp-307-chatbot-deflection.md, work/fnd-cb-repeat-contact.md, work/fnd-cb-volume-shift.md, work/feat-cb-prior-calls-v1.md

## Q5
ed-gbm-v3 is in force: ed-gbm-v1 was replaced by v2, and v2 by v3. ed-gbm-v3 is built on ed-gbm-v2, exp-207-early-delinquency (the bureau slope lift experiment) and feat-ed-bureau-slope-v1.
Notes: work/ed-gbm-v3.md, work/ed-gbm-v2.md, work/exp-207-early-delinquency.md, work/feat-ed-bureau-slope-v1.md