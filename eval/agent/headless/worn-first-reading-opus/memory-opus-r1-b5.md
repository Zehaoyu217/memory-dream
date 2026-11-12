## Q1
Both models build directly on feat-mq3-app-sessions-30d, feat-mq3-prior-treat and feat-mq3-recency-v1. feat-mq3-recency-v1 has since been replaced by feat-mq3-recency-v2.
Notes: marketing-uplift-q3/feat-mq3-app-sessions-30d.md, marketing-uplift-q3/feat-mq3-prior-treat.md, marketing-uplift-q3/feat-mq3-recency-v1.md

## Q2
Only inc-linear-baseline. It is still current and builds directly on feat-inc-payroll-cadence-v1, which was replaced by feat-inc-payroll-cadence-v2. inc-gbm-v3 is also current, but its direct inputs (ds-inc-verified-2026 and the rest) have not been replaced.
Notes: income-estimation/inc-linear-baseline.md, income-estimation/feat-inc-payroll-cadence-v1.md

## Q3
Four decisions rest on ds-cb-call-linkage. dec-cb-metric-24h is built on it directly, and it has since been replaced by dec-cb-metric-48h. dec-cb-metric-48h, dec-cb-handoff-v2 and dec-cb-rollout-60 rest on it through other notes (exp-306, exp-307, fnd-cb-repeat-contact and fnd-cb-volume-shift, among others).
Notes: chatbot-deflection/dec-cb-metric-24h.md, chatbot-deflection/dec-cb-metric-48h.md, chatbot-deflection/dec-cb-handoff-v2.md, chatbot-deflection/dec-cb-rollout-60.md

## Q4
The line runs ed-gbm-v1 → ed-gbm-v2 → ed-gbm-v3, so ed-gbm-v3 is in force now. It is built on ed-gbm-v2 (replaced), exp-207 and feat-ed-bureau-slope-v1.
Notes: early-delinquency/ed-gbm-v3.md, early-delinquency/ed-gbm-v2.md, early-delinquency/exp-207.md, early-delinquency/feat-ed-bureau-slope-v1.md

## Q5
One note from another project builds directly on dec-f25-champion-v2: dec-f26-replace-f25 in fraud-2026.
Notes: fraud-2026/dec-f26-replace-f25.md

## Q6
cb-escalate-v1 rests on three datasets. ds-cb-escalation-labels is a direct input. ds-cb-call-linkage comes in through feat-cb-prior-calls-v1. ds-cb-sessions, where the line starts, sits under both of them.
Notes: chatbot-deflection/ds-cb-escalation-labels.md, chatbot-deflection/ds-cb-call-linkage.md, chatbot-deflection/ds-cb-sessions.md

## Q7
Both models build directly on feat-nps-theme-share-v1, feat-nps-complaint-flag-v1 and feat-nps-txn-freq-v1. nps-gbm-v2 also adds feat-nps-fee-shock-v2.
Notes: nps-drivers/feat-nps-theme-share-v1.md, nps-drivers/feat-nps-complaint-flag-v1.md, nps-drivers/feat-nps-txn-freq-v1.md

## Q8
Only mq3-response-gbm-v1. It is still current and builds directly on feat-mq3-recency-v1, which was replaced by feat-mq3-recency-v2. mq3-uplift-tlearner-v1 also uses the old feature, but that model has itself been replaced, so it does not count.
Notes: marketing-uplift-q3/mq3-response-gbm-v1.md, marketing-uplift-q3/feat-mq3-recency-v1.md

## Q9
Two churn-2025 decisions rest on feat-c25-util-v2: dec-c25-ship-gbm-v2 (through churn-gbm-2025-v2) and dec-c25-drop-app-sessions (through exp-104, exp-105 and fnd-c25-app-lift-v2). Three retention-offers-roi decisions also rest on it, through feat-ror-churn-score and the models built on that: dec-ror-value-band-v2, dec-ror-reallocate-t3 and dec-ror-matrix-v4.
Notes: churn-2025/dec-c25-ship-gbm-v2.md, churn-2025/dec-c25-drop-app-sessions.md, retention-offers-roi/dec-ror-value-band-v2.md, retention-offers-roi/dec-ror-reallocate-t3.md, retention-offers-roi/dec-ror-matrix-v4.md

## Q10
The line runs fraud25-gbm-v1 → fraud25-gbm-v2 → fraud26-gbm-v1 → fraud26-gbm-v2 → fraud26-gbm-v3, so fraud26-gbm-v3 (in fraud-2026) is in force now. It is built directly on exp-207, feat-f26-amt-zscore, feat-f26-geo-mismatch and fraud26-gbm-v2 (replaced).
Notes: fraud-2026/fraud26-gbm-v3.md, fraud-2026/exp-207.md, fraud-2026/feat-f26-amt-zscore.md, fraud-2026/feat-f26-geo-mismatch.md, fraud-2026/fraud26-gbm-v2.md