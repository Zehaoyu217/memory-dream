## Q1
Both models build directly on three features: feat-mq3-recency-v1, feat-mq3-app-sessions-30d and feat-mq3-prior-treat. mq3-response-gbm-v1 also uses feat-mq3-email-open-90d, but mq3-uplift-tlearner-v1 does not.
Notes: marketing-uplift-q3/feat-mq3-recency-v1.md, marketing-uplift-q3/feat-mq3-app-sessions-30d.md, marketing-uplift-q3/feat-mq3-prior-treat.md

## Q2
No. The only current model in income-estimation is inc-gbm-v3, and its direct inputs are inc-gbm-v2 (a replaced model, not a feature or dataset), find-inc-log-target-gain and ds-inc-verified-2026, so none is a replaced feature or dataset.
Notes: income-estimation/inc-gbm-v3.md

## Q3
Four decision notes rest on ds-cb-call-linkage: dec-cb-metric-24h directly, and dec-cb-rollout-60, dec-cb-handoff-v2 and dec-cb-metric-48h through other notes.
Notes: chatbot-deflection/dec-cb-metric-24h.md, chatbot-deflection/dec-cb-rollout-60.md, chatbot-deflection/dec-cb-handoff-v2.md, chatbot-deflection/dec-cb-metric-48h.md

## Q4
ed-gbm-v3 is in force (ed-gbm-v1 was replaced by ed-gbm-v2, which was replaced by ed-gbm-v3). It is built directly on ed-gbm-v2, feat-ed-bureau-slope-v1 and exp-207, and those rest on the utilisation-trend, cash-advance and min-pay features beneath them.
Notes: early-delinquency/ed-gbm-v3.md, early-delinquency/ed-gbm-v2.md, early-delinquency/feat-ed-bureau-slope-v1.md, early-delinquency/exp-207.md

## Q5
Only one note from another project is built directly on dec-f25-champion-v2: fraud-2026/dec-f26-replace-f25, which replaces the fraud-2025 champion.
Notes: fraud-2026/dec-f26-replace-f25.md

## Q6
cb-escalate-v1 rests on three dataset notes: ds-cb-escalation-labels directly, and ds-cb-call-linkage and ds-cb-sessions through feat-cb-prior-calls-v1 and ds-cb-call-linkage.
Notes: chatbot-deflection/ds-cb-escalation-labels.md, chatbot-deflection/ds-cb-call-linkage.md, chatbot-deflection/ds-cb-sessions.md

## Q7
Both models build directly on feat-nps-txn-freq-v1, feat-nps-complaint-flag-v1 and feat-nps-theme-share-v1. nps-gbm-v2 also uses feat-nps-fee-shock-v2, exp-405 and nps-gbm-v1.
Notes: nps-drivers/feat-nps-txn-freq-v1.md, nps-drivers/feat-nps-complaint-flag-v1.md, nps-drivers/feat-nps-theme-share-v1.md

## Q8
mq3-response-gbm-v1 is the only current model that builds directly on a replaced feature: feat-mq3-recency-v1, which was replaced by feat-mq3-recency-v2. The other current models (mq3-uplift-xl-v2 and mq3-channel-rct-v1) use only current inputs.
Notes: marketing-uplift-q3/mq3-response-gbm-v1.md, marketing-uplift-q3/feat-mq3-recency-v1.md

## Q9
Five decision notes rest on feat-c25-util-v2: dec-c25-ship-gbm-v2 and dec-c25-drop-app-sessions in churn-2025, and dec-ror-value-band-v2, dec-ror-reallocate-t3 and dec-ror-matrix-v4 in retention-offers-roi.
Notes: churn-2025/dec-c25-ship-gbm-v2.md, churn-2025/dec-c25-drop-app-sessions.md, retention-offers-roi/dec-ror-value-band-v2.md, retention-offers-roi/dec-ror-reallocate-t3.md, retention-offers-roi/dec-ror-matrix-v4.md

## Q10
fraud26-gbm-v3 is in force (fraud25-gbm-v1 → fraud25-gbm-v2 → fraud26-gbm-v1 → fraud26-gbm-v2 → fraud26-gbm-v3). It is built directly on fraud26-gbm-v2, feat-f26-geo-mismatch, feat-f26-amt-zscore and exp-207.
Notes: fraud-2026/fraud26-gbm-v3.md, fraud-2026/fraud26-gbm-v2.md, fraud-2026/feat-f26-geo-mismatch.md, fraud-2026/feat-f26-amt-zscore.md, fraud-2026/exp-207.md