## Q1
Both models build directly on feat-mq3-app-sessions-30d, feat-mq3-prior-treat and feat-mq3-recency-v1. The response model also uses feat-mq3-email-open-90d, which the T-learner does not.
Notes: marketing-uplift-q3/feat-mq3-app-sessions-30d.md, marketing-uplift-q3/feat-mq3-prior-treat.md, marketing-uplift-q3/feat-mq3-recency-v1.md

## Q2
inc-linear-baseline is the only current income-estimation model built directly on a replaced feature: it uses feat-inc-payroll-cadence-v1, which v2 replaced. inc-gbm-v3 builds on inc-gbm-v2, which is a model rather than a feature or dataset, so it does not count.
Notes: income-estimation/inc-linear-baseline.md

## Q3
Four decision notes rest on ds-cb-call-linkage: dec-cb-metric-24h directly, and dec-cb-metric-48h, dec-cb-handoff-v2 and dec-cb-rollout-60 through other notes.
Notes: chatbot-deflection/dec-cb-metric-24h.md, chatbot-deflection/dec-cb-metric-48h.md, chatbot-deflection/dec-cb-handoff-v2.md, chatbot-deflection/dec-cb-rollout-60.md

## Q4
The note in force at the end of that line is ed-gbm-v3, which builds on ed-gbm-v2, exp-207 and feat-ed-bureau-slope-v1.
Notes: early-delinquency/ed-gbm-v3.md, early-delinquency/ed-gbm-v2.md, early-delinquency/exp-207.md, early-delinquency/feat-ed-bureau-slope-v1.md

## Q5
Only fraud-2026/dec-f26-replace-f25 builds directly on dec-f25-champion-v2.
Notes: fraud-2026/dec-f26-replace-f25.md

## Q6
cb-escalate-v1 rests on three dataset notes: ds-cb-escalation-labels directly, and ds-cb-call-linkage and ds-cb-sessions through feat-cb-prior-calls-v1 and the labels.
Notes: chatbot-deflection/ds-cb-escalation-labels.md, chatbot-deflection/ds-cb-call-linkage.md, chatbot-deflection/ds-cb-sessions.md

## Q7
Both build directly on feat-nps-complaint-flag-v1, feat-nps-theme-share-v1 and feat-nps-txn-freq-v1.
Notes: nps-drivers/feat-nps-complaint-flag-v1.md, nps-drivers/feat-nps-theme-share-v1.md, nps-drivers/feat-nps-txn-freq-v1.md

## Q8
Only mq3-response-gbm-v1 is a current model built directly on a replaced feature: it still uses feat-mq3-recency-v1, which feat-mq3-recency-v2 replaced.
Notes: marketing-uplift-q3/mq3-response-gbm-v1.md

## Q9
Five decision notes rest on feat-c25-util-v2: dec-c25-ship-gbm-v2 and dec-c25-drop-app-sessions in churn-2025, and dec-ror-value-band-v2, dec-ror-reallocate-t3 and dec-ror-matrix-v4 in retention-offers-roi. All five do so through other notes.
Notes: churn-2025/dec-c25-ship-gbm-v2.md, churn-2025/dec-c25-drop-app-sessions.md, retention-offers-roi/dec-ror-value-band-v2.md, retention-offers-roi/dec-ror-reallocate-t3.md, retention-offers-roi/dec-ror-matrix-v4.md

## Q10
The note in force at the end of that line is fraud26-gbm-v3, which builds on exp-207, feat-f26-amt-zscore, feat-f26-geo-mismatch and fraud26-gbm-v2.
Notes: fraud-2026/fraud26-gbm-v3.md, fraud-2026/exp-207.md, fraud-2026/feat-f26-amt-zscore.md, fraud-2026/feat-f26-geo-mismatch.md, fraud-2026/fraud26-gbm-v2.md