## Q1
Both build directly on feat-mq3-recency-v1, feat-mq3-app-sessions-30d and feat-mq3-prior-treat. The response model also takes feat-mq3-email-open-90d, and the T-learner also takes ds-mq3-q2-rct.
Notes: marketing-uplift-q3/feat-mq3-recency-v1.md, marketing-uplift-q3/feat-mq3-app-sessions-30d.md, marketing-uplift-q3/feat-mq3-prior-treat.md

## Q2
inc-linear-baseline is the only current model built directly on the replaced feat-inc-payroll-cadence-v1 (superseded by v2). It is a baseline and not used in production. inc-gbm-v1 also used v1, but it is superseded.
Notes: income-estimation/inc-linear-baseline.md, income-estimation/feat-inc-payroll-cadence-v1.md

## Q3
dec-cb-metric-24h rests on it directly. dec-cb-metric-48h rests on it through exp-306 and fnd-cb-def-sensitivity, and through exp-307 and fnd-cb-repeat-contact. dec-cb-handoff-v2 rests on it through fnd-cb-repeat-contact. dec-cb-rollout-60 rests on it directly through fnd-cb-volume-shift, and also through dec-cb-metric-48h.
Notes: chatbot-deflection/dec-cb-metric-24h.md, chatbot-deflection/dec-cb-metric-48h.md, chatbot-deflection/dec-cb-handoff-v2.md, chatbot-deflection/dec-cb-rollout-60.md

## Q4
The line runs ed-gbm-v1, then ed-gbm-v2, then ed-gbm-v3, which is in force now. ed-gbm-v3 is built directly on ed-gbm-v2, feat-ed-bureau-slope-v1 and exp-207.
Notes: early-delinquency/ed-gbm-v3.md, early-delinquency/ed-gbm-v2.md, early-delinquency/feat-ed-bureau-slope-v1.md, early-delinquency/exp-207.md

## Q5
Only one note in another project is built directly on dec-f25-champion-v2: fraud-2026/dec-f26-replace-f25, which replaces the fraud-2025 champion.
Notes: fraud-2026/dec-f26-replace-f25.md

## Q6
cb-escalate-v1 rests on ds-cb-escalation-labels directly and on ds-cb-call-linkage through feat-cb-prior-calls-v1. Both of those rest on ds-cb-sessions, the root dataset note.
Notes: chatbot-deflection/cb-escalate-v1.md, chatbot-deflection/ds-cb-sessions.md, chatbot-deflection/ds-cb-escalation-labels.md, chatbot-deflection/ds-cb-call-linkage.md

## Q7
nps-gbm-v1 and nps-gbm-v2 both build directly on feat-nps-theme-share-v1, feat-nps-txn-freq-v1 and feat-nps-complaint-flag-v1.
Notes: nps-drivers/feat-nps-theme-share-v1.md, nps-drivers/feat-nps-txn-freq-v1.md, nps-drivers/feat-nps-complaint-flag-v1.md

## Q8
mq3-response-gbm-v1 is the only current model built directly on a replaced feature. It uses feat-mq3-recency-v1, which feat-mq3-recency-v2 replaced, and the response model stays in use as a reporting metric. mq3-uplift-tlearner-v1 also uses v1, but it is superseded by mq3-uplift-xl-v2.
Notes: marketing-uplift-q3/mq3-response-gbm-v1.md, marketing-uplift-q3/feat-mq3-recency-v1.md, marketing-uplift-q3/feat-mq3-recency-v2.md

## Q9
Five decisions rest on feat-c25-util-v2. Two are in churn-2025 and rest on it directly or through exp-104 and exp-105, or through churn-gbm-2025-v2. Three are in retention-offers-roi and rest on it through churn-gbm-2025-v2, feat-ror-churn-score, ror-uplift-v1 and ror-roi-v1, which feed exp-404, fnd-ror-realloc-gain and ror-roi-v2. This chain crosses into the retention-offers-roi project.
Notes: churn-2025/dec-c25-ship-gbm-v2.md, churn-2025/dec-c25-drop-app-sessions.md, retention-offers-roi/dec-ror-reallocate-t3.md, retention-offers-roi/dec-ror-matrix-v4.md, retention-offers-roi/dec-ror-value-band-v2.md

## Q10
The line runs fraud25-gbm-v1, then fraud25-gbm-v2, then fraud26-gbm-v1, then fraud26-gbm-v2, and fraud26-gbm-v3 is in force now. fraud26-gbm-v3 is built directly on fraud26-gbm-v2, feat-f26-geo-mismatch, feat-f26-amt-zscore and exp-207.
Notes: fraud-2026/fraud26-gbm-v3.md, fraud-2026/fraud26-gbm-v2.md, fraud-2026/feat-f26-geo-mismatch.md, fraud-2026/feat-f26-amt-zscore.md, fraud-2026/exp-207.md