## Q1
Both build directly on feat-mq3-app-sessions-30d, feat-mq3-prior-treat and feat-mq3-recency-v1. The response model also uses the 90-day email-open feature, which the uplift model does not.
Notes: marketing-uplift-q3/mq3-response-gbm-v1.md, marketing-uplift-q3/mq3-uplift-tlearner-v1.md, marketing-uplift-q3/feat-mq3-app-sessions-30d.md, marketing-uplift-q3/feat-mq3-prior-treat.md, marketing-uplift-q3/feat-mq3-recency-v1.md

## Q2
Only inc-linear-baseline. It is not marked superseded and still builds on the basic payroll cadence feature, feat-inc-payroll-cadence-v1, which feat-inc-payroll-cadence-v2 replaced. The live model, inc-gbm-v3, builds only on current inputs.
Notes: income-estimation/inc-linear-baseline.md, income-estimation/feat-inc-payroll-cadence-v1.md, income-estimation/feat-inc-payroll-cadence-v2.md

## Q3
dec-cb-metric-24h rests on ds-cb-call-linkage directly. dec-cb-metric-48h, dec-cb-handoff-v2 and dec-cb-rollout-60 rest on it through exp-306/fnd-cb-def-sensitivity, exp-307/fnd-cb-repeat-contact and fnd-cb-volume-shift respectively.
Notes: chatbot-deflection/ds-cb-call-linkage.md, chatbot-deflection/dec-cb-metric-24h.md, chatbot-deflection/dec-cb-metric-48h.md, chatbot-deflection/dec-cb-handoff-v2.md, chatbot-deflection/dec-cb-rollout-60.md, chatbot-deflection/exp-306.md, chatbot-deflection/fnd-cb-def-sensitivity.md, chatbot-deflection/exp-307.md, chatbot-deflection/fnd-cb-repeat-contact.md, chatbot-deflection/fnd-cb-volume-shift.md

## Q4
ed-gbm-v3 is in force. It builds on ed-gbm-v2, the bureau slope lift experiment (exp-207) and feat-ed-bureau-slope-v1.
Notes: early-delinquency/ed-gbm-v1.md, early-delinquency/ed-gbm-v2.md, early-delinquency/ed-gbm-v3.md, early-delinquency/exp-207.md, early-delinquency/feat-ed-bureau-slope-v1.md

## Q5
Only dec-f26-replace-f25, which builds on fraud-2025/dec-f25-champion-v2 and replaces fraud25-gbm-v2 with fraud26-gbm-v1.
Notes: fraud-2026/dec-f26-replace-f25.md

## Q6
cb-escalate-v1 rests on ds-cb-escalation-labels and feat-cb-prior-calls-v1. Those rest on ds-cb-sessions and ds-cb-call-linkage, so the dataset notes are ds-cb-sessions, ds-cb-call-linkage and ds-cb-escalation-labels.
Notes: chatbot-deflection/cb-escalate-v1.md, chatbot-deflection/feat-cb-prior-calls-v1.md, chatbot-deflection/ds-cb-escalation-labels.md, chatbot-deflection/ds-cb-call-linkage.md, chatbot-deflection/ds-cb-sessions.md

## Q7
Both build on feat-nps-complaint-flag-v1, feat-nps-theme-share-v1 and feat-nps-txn-freq-v1. nps-gbm-v2 also builds on feat-nps-fee-shock-v2.
Notes: nps-drivers/nps-gbm-v1.md, nps-drivers/nps-gbm-v2.md, nps-drivers/feat-nps-complaint-flag-v1.md, nps-drivers/feat-nps-theme-share-v1.md, nps-drivers/feat-nps-txn-freq-v1.md

## Q8
Only mq3-response-gbm-v1. It is still in use as a reporting metric and builds on feat-mq3-recency-v1, which feat-mq3-recency-v2 replaced. The live uplift model, mq3-uplift-xl-v2, uses only current inputs.
Notes: marketing-uplift-q3/mq3-response-gbm-v1.md, marketing-uplift-q3/feat-mq3-recency-v1.md, marketing-uplift-q3/feat-mq3-recency-v2.md

## Q9
dec-c25-drop-app-sessions rests on feat-c25-util-v2 through exp-105 and exp-104. dec-c25-ship-gbm-v2 rests on it through churn-gbm-2025-v2.
Notes: churn-2025/feat-c25-util-v2.md, churn-2025/exp-104.md, churn-2025/exp-105.md, churn-2025/dec-c25-drop-app-sessions.md, churn-2025/churn-gbm-2025-v2.md, churn-2025/dec-c25-ship-gbm-v2.md

## Q10
fraud26-gbm-v3 is in force, the end of the line fraud25-gbm-v1 → fraud25-gbm-v2 → fraud26-gbm-v1 → fraud26-gbm-v2 → fraud26-gbm-v3. It builds on fraud26-gbm-v2, exp-207, feat-f26-amt-zscore and feat-f26-geo-mismatch.
Notes: fraud-2025/fraud25-gbm-v1.md, fraud-2025/fraud25-gbm-v2.md, fraud-2026/fraud26-gbm-v1.md, fraud-2026/fraud26-gbm-v2.md, fraud-2026/fraud26-gbm-v3.md, fraud-2026/exp-207.md, fraud-2026/feat-f26-amt-zscore.md, fraud-2026/feat-f26-geo-mismatch.md