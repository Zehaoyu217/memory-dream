## Q1
Both notes build directly on feat-mq3-app-sessions-30d, feat-mq3-prior-treat and feat-mq3-recency-v1. The response model also uses the email-opens feature, and the T-learner also uses the Q2 RCT dataset.
Notes: marketing-uplift-q3/mq3-response-gbm-v1.md, marketing-uplift-q3/mq3-uplift-tlearner-v1.md, marketing-uplift-q3/feat-mq3-app-sessions-30d.md, marketing-uplift-q3/feat-mq3-prior-treat.md, marketing-uplift-q3/feat-mq3-recency-v1.md

## Q2
inc-linear-baseline is the only current model that builds directly on a replaced feature. It rests on feat-inc-payroll-cadence-v1, which feat-inc-payroll-cadence-v2 replaced. The note is a baseline "not used in production" but is not marked superseded, so I counted it as current.
Notes: income-estimation/inc-linear-baseline.md, income-estimation/feat-inc-payroll-cadence-v1.md, income-estimation/feat-inc-payroll-cadence-v2.md

## Q3
All four chatbot-deflection decisions rest on ds-cb-call-linkage. dec-cb-metric-24h builds on it directly. dec-cb-metric-48h gets there through fnd-cb-def-sensitivity and exp-306. dec-cb-handoff-v2 gets there through fnd-cb-repeat-contact and exp-307. dec-cb-rollout-60 gets there through fnd-cb-volume-shift.
Notes: chatbot-deflection/dec-cb-metric-24h.md, chatbot-deflection/dec-cb-metric-48h.md, chatbot-deflection/dec-cb-handoff-v2.md, chatbot-deflection/dec-cb-rollout-60.md, chatbot-deflection/ds-cb-call-linkage.md, chatbot-deflection/exp-306.md, chatbot-deflection/exp-307.md, chatbot-deflection/fnd-cb-def-sensitivity.md, chatbot-deflection/fnd-cb-repeat-contact.md, chatbot-deflection/fnd-cb-volume-shift.md

## Q4
The line runs ed-gbm-v1, then ed-gbm-v2, then ed-gbm-v3. ed-gbm-v3 is in force: it was promoted to the watchlist on 2026-06-18. It builds on ed-gbm-v2, the 6-month bureau slope experiment (exp-207) and feat-ed-bureau-slope-v1.
Notes: early-delinquency/ed-gbm-v1.md, early-delinquency/ed-gbm-v2.md, early-delinquency/ed-gbm-v3.md, early-delinquency/exp-207.md, early-delinquency/feat-ed-bureau-slope-v1.md

## Q5
Only one note from another project builds directly on fraud-2025's dec-f25-champion-v2: fraud-2026/dec-f26-replace-f25, which replaces fraud25-gbm-v2 with fraud26-gbm-v1.
Notes: fraud-2026/dec-f26-replace-f25.md

## Q6
Following cb-escalate-v1 back to the start, it rests on three dataset notes. It uses ds-cb-escalation-labels directly and feat-cb-prior-calls-v1 directly. Those two lead to ds-cb-call-linkage and ds-cb-sessions.
Notes: chatbot-deflection/cb-escalate-v1.md, chatbot-deflection/ds-cb-escalation-labels.md, chatbot-deflection/feat-cb-prior-calls-v1.md, chatbot-deflection/ds-cb-call-linkage.md, chatbot-deflection/ds-cb-sessions.md

## Q7
nps-gbm-v1 and nps-gbm-v2 both build directly on feat-nps-complaint-flag-v1, feat-nps-theme-share-v1 and feat-nps-txn-freq-v1.
Notes: nps-drivers/nps-gbm-v1.md, nps-drivers/nps-gbm-v2.md, nps-drivers/feat-nps-complaint-flag-v1.md, nps-drivers/feat-nps-theme-share-v1.md, nps-drivers/feat-nps-txn-freq-v1.md

## Q8
mq3-response-gbm-v1 is the only current model that builds directly on a replaced feature. It rests on feat-mq3-recency-v1, which feat-mq3-recency-v2 replaced. It is still in use as a reporting metric, so I counted it as current. mq3-uplift-tlearner-v1 is excluded because it is superseded.
Notes: marketing-uplift-q3/mq3-response-gbm-v1.md, marketing-uplift-q3/feat-mq3-recency-v1.md, marketing-uplift-q3/feat-mq3-recency-v2.md

## Q9
Two churn-2025 decisions rest on feat-c25-util-v2. dec-c25-ship-gbm-v2 gets there through churn-gbm-2025-v2. dec-c25-drop-app-sessions gets there through exp-105 and exp-104. dec-c25-ship-gbm-v1 does not, because it rests on the v1 utilisation feature.
Notes: churn-2025/dec-c25-ship-gbm-v2.md, churn-2025/dec-c25-drop-app-sessions.md, churn-2025/churn-gbm-2025-v2.md, churn-2025/exp-104.md, churn-2025/exp-105.md, churn-2025/feat-c25-util-v2.md

## Q10
The line runs fraud25-gbm-v1, then fraud25-gbm-v2, then fraud26-gbm-v1, then fraud26-gbm-v2, then fraud26-gbm-v3. fraud26-gbm-v3 is in force and is marked current. It builds on fraud26-gbm-v2, feat-f26-amt-zscore, feat-f26-geo-mismatch and exp-207.
Notes: fraud-2025/fraud25-gbm-v1.md, fraud-2025/fraud25-gbm-v2.md, fraud-2026/fraud26-gbm-v1.md, fraud-2026/fraud26-gbm-v2.md, fraud-2026/fraud26-gbm-v3.md, fraud-2026/feat-f26-amt-zscore.md, fraud-2026/feat-f26-geo-mismatch.md, fraud-2026/exp-207.md