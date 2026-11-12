## Q1
Both models build directly on feat-mq3-app-sessions-30d, feat-mq3-prior-treat and feat-mq3-recency-v1. mq3-response-gbm-v1 also uses feat-mq3-email-open-90d, but mq3-uplift-tlearner-v1 does not.
Notes: marketing-uplift-q3/mq3-response-gbm-v1.md, marketing-uplift-q3/mq3-uplift-tlearner-v1.md, marketing-uplift-q3/feat-mq3-app-sessions-30d.md, marketing-uplift-q3/feat-mq3-prior-treat.md, marketing-uplift-q3/feat-mq3-recency-v1.md

## Q2
inc-linear-baseline is the only current model in income-estimation built directly on a replaced feature or dataset. It builds on feat-inc-payroll-cadence-v1, which was superseded by feat-inc-payroll-cadence-v2. It carries no SUPERSEDED marker itself.
Notes: income-estimation/inc-linear-baseline.md, income-estimation/feat-inc-payroll-cadence-v1.md

## Q3
Four decision notes rest on ds-cb-call-linkage: dec-cb-metric-24h and dec-cb-rollout-60 directly, and dec-cb-metric-48h and dec-cb-handoff-v2 through fnd-cb-repeat-contact and fnd-cb-def-sensitivity.
Notes: chatbot-deflection/dec-cb-metric-24h.md, chatbot-deflection/dec-cb-metric-48h.md, chatbot-deflection/dec-cb-handoff-v2.md, chatbot-deflection/dec-cb-rollout-60.md

## Q4
The line ends at ed-gbm-v3, which is in force. It builds directly on ed-gbm-v2, exp-207 and feat-ed-bureau-slope-v1. Its feature set also includes feat-ed-util-trend-v1, feat-ed-cashadv-v1 and feat-ed-minpay-v2.
Notes: early-delinquency/ed-gbm-v3.md, early-delinquency/ed-gbm-v2.md, early-delinquency/exp-207.md, early-delinquency/feat-ed-bureau-slope-v1.md, early-delinquency/feat-ed-util-trend-v1.md, early-delinquency/feat-ed-cashadv-v1.md, early-delinquency/feat-ed-minpay-v2.md

## Q5
Only one note of another project is built directly on dec-f25-champion-v2: fraud-2026/dec-f26-replace-f25, which replaces the 2025 champion from 2026-02-10.
Notes: fraud-2026/dec-f26-replace-f25.md

## Q6
cb-escalate-v1 rests on three dataset notes: ds-cb-escalation-labels directly, and ds-cb-call-linkage and ds-cb-sessions through feat-cb-prior-calls-v1.
Notes: chatbot-deflection/cb-escalate-v1.md, chatbot-deflection/ds-cb-escalation-labels.md, chatbot-deflection/ds-cb-call-linkage.md, chatbot-deflection/ds-cb-sessions.md

## Q7
Both nps-gbm-v1 and nps-gbm-v2 build directly on feat-nps-complaint-flag-v1, feat-nps-theme-share-v1 and feat-nps-txn-freq-v1.
Notes: nps-drivers/nps-gbm-v1.md, nps-drivers/nps-gbm-v2.md, nps-drivers/feat-nps-complaint-flag-v1.md, nps-drivers/feat-nps-theme-share-v1.md, nps-drivers/feat-nps-txn-freq-v1.md

## Q8
mq3-response-gbm-v1 is the only current model in marketing-uplift-q3 built directly on a replaced feature. It builds on feat-mq3-recency-v1, which was superseded by feat-mq3-recency-v2.
Notes: marketing-uplift-q3/mq3-response-gbm-v1.md, marketing-uplift-q3/feat-mq3-recency-v1.md

## Q9
Five decision notes rest on feat-c25-util-v2: dec-c25-ship-gbm-v2 and dec-c25-drop-app-sessions in churn-2025, and dec-ror-value-band-v2, dec-ror-reallocate-t3 and dec-ror-matrix-v4 in retention-offers-roi, all through intermediate notes.
Notes: churn-2025/dec-c25-ship-gbm-v2.md, churn-2025/dec-c25-drop-app-sessions.md, retention-offers-roi/dec-ror-value-band-v2.md, retention-offers-roi/dec-ror-reallocate-t3.md, retention-offers-roi/dec-ror-matrix-v4.md

## Q10
The line ends at fraud26-gbm-v3 in fraud-2026, which is in force. It builds directly on fraud26-gbm-v2, exp-207, feat-f26-amt-zscore and feat-f26-geo-mismatch.
Notes: fraud-2026/fraud26-gbm-v3.md, fraud-2026/fraud26-gbm-v2.md, fraud-2026/exp-207.md, fraud-2026/feat-f26-amt-zscore.md, fraud-2026/feat-f26-geo-mismatch.md