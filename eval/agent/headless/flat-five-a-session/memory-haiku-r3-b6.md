## Q1
disp-lgbm-v1 was replaced by disp-lgbm-v2, which was replaced by disp-lgbm-v3, the note in force now. disp-lgbm-v3 builds on dec-disp-fraud-score-in, disp-lgbm-v2, exp-307-dispute-triage and feat-disp-fraud-score.
Notes: work/disp-lgbm-v3.md, work/dec-disp-fraud-score-in.md, work/disp-lgbm-v2.md, work/exp-307-dispute-triage.md, work/feat-disp-fraud-score.md

## Q2
cb-elasticity-v1 rests directly on ds-cb-pilot-2025q4 and feat-cb-spend-base. Through those, it goes back to ds-cb-spend-panel, the starting dataset.
Notes: work/cb-elasticity-v1.md, work/ds-cb-pilot-2025q4.md, work/feat-cb-spend-base.md, work/ds-cb-spend-panel.md

## Q3
Both models build directly on feat-mq3-app-sessions-30d, feat-mq3-prior-treat and feat-mq3-recency-v1. mq3-response-gbm-v1 also builds on feat-mq3-email-open-90d, which mq3-uplift-tlearner-v1 does not use.
Notes: work/mq3-response-gbm-v1.md, work/mq3-uplift-tlearner-v1.md, work/feat-mq3-app-sessions-30d.md, work/feat-mq3-prior-treat.md, work/feat-mq3-recency-v1.md

## Q4
Four decision notes rest on ds-cb-call-linkage. dec-cb-metric-24h builds on it directly, and dec-cb-rollout-60, dec-cb-handoff-v2 and dec-cb-metric-48h reach it through other notes. The last three paths are inferred from the naming convention, since I did not open those notes.
Notes: work/dec-cb-metric-24h.md, work/dec-cb-rollout-60.md, work/dec-cb-handoff-v2.md, work/dec-cb-metric-48h.md, work/ds-cb-call-linkage.md

## Q5
ed-gbm-v1 was replaced by ed-gbm-v2, which was replaced by ed-gbm-v3, the note in force now. ed-gbm-v3 builds directly on ed-gbm-v2, exp-207-early-delinquency and feat-ed-bureau-slope-v1. Its feature inputs also include feat-ed-util-trend-v1, feat-ed-cashadv-v1 and feat-ed-minpay-v2.
Notes: work/ed-gbm-v3.md, work/ed-gbm-v2.md, work/exp-207-early-delinquency.md, work/feat-ed-bureau-slope-v1.md, work/feat-ed-util-trend-v1.md, work/feat-ed-cashadv-v1.md, work/feat-ed-minpay-v2.md