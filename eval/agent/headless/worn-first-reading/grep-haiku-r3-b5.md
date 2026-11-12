## Q1
Both models build on feat-mq3-app-sessions-30d, feat-mq3-prior-treat and feat-mq3-recency-v1. mq3-response-gbm-v1 also uses the 90-day email-open feature, and mq3-uplift-tlearner-v1 also uses ds-mq3-q2-rct.
Notes: marketing-uplift-q3/mq3-response-gbm-v1.md, marketing-uplift-q3/mq3-uplift-tlearner-v1.md, marketing-uplift-q3/feat-mq3-app-sessions-30d.md, marketing-uplift-q3/feat-mq3-prior-treat.md, marketing-uplift-q3/feat-mq3-recency-v1.md

## Q2
inc-linear-baseline is not marked superseded and builds directly on feat-inc-payroll-cadence-v1, which feat-inc-payroll-cadence-v2 replaced. The only other current model, inc-gbm-v3, builds on no replaced feature or dataset.
Notes: income-estimation/inc-linear-baseline.md, income-estimation/feat-inc-payroll-cadence-v1.md, income-estimation/feat-inc-payroll-cadence-v2.md

## Q3
dec-cb-metric-24h builds on ds-cb-call-linkage directly. dec-cb-metric-48h rests on it through fnd-cb-def-sensitivity and exp-306, dec-cb-rollout-60 through fnd-cb-volume-shift, and dec-cb-handoff-v2 through fnd-cb-repeat-contact and exp-307.
Notes: chatbot-deflection/dec-cb-metric-24h.md, chatbot-deflection/dec-cb-metric-48h.md, chatbot-deflection/dec-cb-rollout-60.md, chatbot-deflection/dec-cb-handoff-v2.md, chatbot-deflection/ds-cb-call-linkage.md, chatbot-deflection/exp-306.md, chatbot-deflection/exp-307.md, chatbot-deflection/fnd-cb-def-sensitivity.md, chatbot-deflection/fnd-cb-volume-shift.md, chatbot-deflection/fnd-cb-repeat-contact.md

## Q4
The line runs ed-gbm-v1, then ed-gbm-v2 (replaces v1), then ed-gbm-v3 (replaces v2), which is in force. ed-gbm-v3 builds on ed-gbm-v2, exp-207 (the bureau slope lift experiment) and feat-ed-bureau-slope-v1.
Notes: early-delinquency/ed-gbm-v1.md, early-delinquency/ed-gbm-v2.md, early-delinquency/ed-gbm-v3.md, early-delinquency/exp-207.md, early-delinquency/feat-ed-bureau-slope-v1.md

## Q5
Only fraud-2026/dec-f26-replace-f25.md, which builds directly on fraud-2025/dec-f25-champion-v2.
Notes: fraud-2026/dec-f26-replace-f25.md

## Q6
cb-escalate-v1 builds directly on ds-cb-escalation-labels and, through feat-cb-prior-calls-v1, on ds-cb-call-linkage. Both trace back to ds-cb-sessions, the root dataset.
Notes: chatbot-deflection/cb-escalate-v1.md, chatbot-deflection/ds-cb-escalation-labels.md, chatbot-deflection/feat-cb-prior-calls-v1.md, chatbot-deflection/ds-cb-call-linkage.md, chatbot-deflection/ds-cb-sessions.md

## Q7
Both build directly on feat-nps-complaint-flag-v1, feat-nps-theme-share-v1 and feat-nps-txn-freq-v1.
Notes: nps-drivers/nps-gbm-v1.md, nps-drivers/nps-gbm-v2.md, nps-drivers/feat-nps-complaint-flag-v1.md, nps-drivers/feat-nps-theme-share-v1.md, nps-drivers/feat-nps-txn-freq-v1.md

## Q8
mq3-response-gbm-v1 is still in use as a reporting metric and builds directly on feat-mq3-recency-v1, which feat-mq3-recency-v2 replaced. The other current model, mq3-uplift-xl-v2, builds on no replaced feature or dataset.
Notes: marketing-uplift-q3/mq3-response-gbm-v1.md, marketing-uplift-q3/feat-mq3-recency-v1.md, marketing-uplift-q3/feat-mq3-recency-v2.md

## Q9
dec-c25-drop-app-sessions rests on feat-c25-util-v2 through exp-105 and exp-104. dec-c25-ship-gbm-v2 rests on it through churn-gbm-2025-v2.
Notes: churn-2025/dec-c25-drop-app-sessions.md, churn-2025/dec-c25-ship-gbm-v2.md, churn-2025/exp-104.md, churn-2025/exp-105.md, churn-2025/churn-gbm-2025-v2.md, churn-2025/feat-c25-util-v2.md

## Q10
The line runs fraud25-gbm-v1, then fraud25-gbm-v2 (replaces v1), then fraud26-gbm-v1 (replaces fraud25-gbm-v2), then fraud26-gbm-v2, then fraud26-gbm-v3, which is in force. fraud26-gbm-v3 builds on exp-207, feat-f26-amt-zscore, feat-f26-geo-mismatch and fraud26-gbm-v2.
Notes: fraud-2025/fraud25-gbm-v1.md, fraud-2025/fraud25-gbm-v2.md, fraud-2026/fraud26-gbm-v1.md, fraud-2026/fraud26-gbm-v2.md, fraud-2026/fraud26-gbm-v3.md, fraud-2026/exp-207.md, fraud-2026/feat-f26-amt-zscore.md, fraud-2026/feat-f26-geo-mismatch.md