## Q1
Both models build directly on three feature notes: feat-mq3-app-sessions-30d, feat-mq3-prior-treat and feat-mq3-recency-v1. The response model also uses the email-opens feature, and the T-learner also uses the Q2 RCT dataset.
Notes: marketing-uplift-q3/feat-mq3-app-sessions-30d.md, marketing-uplift-q3/feat-mq3-prior-treat.md, marketing-uplift-q3/feat-mq3-recency-v1.md

## Q2
inc-linear-baseline is the only one. Nothing has replaced it, but it builds on feat-inc-payroll-cadence-v1, which feat-inc-payroll-cadence-v2 replaced. inc-gbm-v1 also uses cadence-v1, but it has itself been replaced, and inc-gbm-v3 uses no replaced inputs.
Notes: income-estimation/inc-linear-baseline.md, income-estimation/feat-inc-payroll-cadence-v1.md

## Q3
Four decisions rest on it. dec-cb-metric-24h builds on it directly. dec-cb-metric-48h comes through exp-306, fnd-cb-def-sensitivity and fnd-cb-repeat-contact. dec-cb-handoff-v2 comes through exp-307 and fnd-cb-repeat-contact. dec-cb-rollout-60 comes through fnd-cb-volume-shift, dec-cb-handoff-v2 and dec-cb-metric-48h.
Notes: chatbot-deflection/dec-cb-metric-24h.md, chatbot-deflection/dec-cb-metric-48h.md, chatbot-deflection/dec-cb-handoff-v2.md, chatbot-deflection/dec-cb-rollout-60.md

## Q4
The line runs ed-gbm-v1 → ed-gbm-v2 → ed-gbm-v3, and ed-gbm-v3 is in force now. It builds on ed-gbm-v2, exp-207 (the bureau slope lift experiment) and feat-ed-bureau-slope-v1.
Notes: early-delinquency/ed-gbm-v3.md, early-delinquency/ed-gbm-v2.md, early-delinquency/exp-207.md, early-delinquency/feat-ed-bureau-slope-v1.md

## Q5
Only one note in another project builds directly on it: dec-f26-replace-f25 in fraud-2026, the decision that fraud26-gbm-v1 replaces the 2025 champion.
Notes: fraud-2026/dec-f26-replace-f25.md

## Q6
cb-escalate-v1 builds on the escalation labels and feat-cb-prior-calls-v1. The prior-calls feature builds on ds-cb-call-linkage, and both the labels and the linkage build on ds-cb-sessions. So it rests on three dataset notes: ds-cb-escalation-labels, ds-cb-call-linkage and ds-cb-sessions.
Notes: chatbot-deflection/ds-cb-escalation-labels.md, chatbot-deflection/ds-cb-call-linkage.md, chatbot-deflection/ds-cb-sessions.md

## Q7
Both versions build directly on feat-nps-complaint-flag-v1, feat-nps-theme-share-v1 and feat-nps-txn-freq-v1. v2 also adds feat-nps-fee-shock-v2.
Notes: nps-drivers/feat-nps-complaint-flag-v1.md, nps-drivers/feat-nps-theme-share-v1.md, nps-drivers/feat-nps-txn-freq-v1.md

## Q8
mq3-response-gbm-v1 is the only one. Nothing has replaced it, though it is no longer used for targeting, and it builds on feat-mq3-recency-v1, which feat-mq3-recency-v2 replaced. mq3-uplift-tlearner-v1 also uses recency-v1, but mq3-uplift-xl-v2 has replaced it.
Notes: marketing-uplift-q3/mq3-response-gbm-v1.md, marketing-uplift-q3/feat-mq3-recency-v1.md

## Q9
In churn-2025, two decisions rest on it: dec-c25-drop-app-sessions (through exp-104, exp-105 and fnd-c25-app-lift-v2) and dec-c25-ship-gbm-v2 (through churn-gbm-2025-v2). In retention-offers-roi, three more rest on it through feat-ror-churn-score, ror-uplift-v1 and ror-roi-v1: dec-ror-reallocate-t3, dec-ror-matrix-v4 and dec-ror-value-band-v2.
Notes: churn-2025/dec-c25-drop-app-sessions.md, churn-2025/dec-c25-ship-gbm-v2.md, retention-offers-roi/dec-ror-reallocate-t3.md, retention-offers-roi/dec-ror-matrix-v4.md, retention-offers-roi/dec-ror-value-band-v2.md

## Q10
The line continues into fraud-2026: fraud25-gbm-v1 → fraud25-gbm-v2 → fraud26-gbm-v1 → fraud26-gbm-v2 → fraud26-gbm-v3. fraud26-gbm-v3 is in force now. It builds on exp-207 (the geo-mismatch and amount z-score experiment), feat-f26-amt-zscore, feat-f26-geo-mismatch and fraud26-gbm-v2.
Notes: fraud-2026/fraud26-gbm-v3.md, fraud-2026/exp-207.md, fraud-2026/feat-f26-amt-zscore.md, fraud-2026/feat-f26-geo-mismatch.md, fraud-2026/fraud26-gbm-v2.md