## Q1
Both mq3-response-gbm-v1 and mq3-uplift-tlearner-v1 build directly on three features: feat-mq3-app-sessions-30d, feat-mq3-prior-treat and feat-mq3-recency-v1. The T-learner also builds on the ds-mq3-q2-rct dataset, and the response model adds feat-mq3-email-open-90d.
Notes: marketing-uplift-q3/mq3-response-gbm-v1.md, marketing-uplift-q3/mq3-uplift-tlearner-v1.md, marketing-uplift-q3/feat-mq3-app-sessions-30d.md, marketing-uplift-q3/feat-mq3-prior-treat.md, marketing-uplift-q3/feat-mq3-recency-v1.md

## Q2
None. inc-gbm-v3 is the only current income-estimation model, and it builds on ds-inc-verified-2026 and find-inc-log-target-gain, neither of which has been replaced. Its only replaced input is the model inc-gbm-v2, which is not a feature or dataset.
Notes: income-estimation/inc-gbm-v3.md

## Q3
Four decision notes rest on ds-cb-call-linkage: dec-cb-metric-24h directly, and dec-cb-rollout-60, dec-cb-handoff-v2 and dec-cb-metric-48h through other notes built on it.
Notes: chatbot-deflection/dec-cb-metric-24h.md, chatbot-deflection/dec-cb-rollout-60.md, chatbot-deflection/dec-cb-handoff-v2.md, chatbot-deflection/dec-cb-metric-48h.md

## Q4
The note in force at the end of the line is ed-gbm-v3. It builds directly on ed-gbm-v2, exp-207 and feat-ed-bureau-slope-v1, and its feature list also includes feat-ed-util-trend-v1, feat-ed-cashadv-v1 and feat-ed-minpay-v2.
Notes: early-delinquency/ed-gbm-v3.md, early-delinquency/ed-gbm-v2.md, early-delinquency/exp-207.md, early-delinquency/feat-ed-bureau-slope-v1.md

## Q5
Only one note of another project builds directly on dec-f25-champion-v2: the fraud-2026 decision dec-f26-replace-f25.
Notes: fraud-2026/dec-f26-replace-f25.md

## Q6
cb-escalate-v1 rests on three dataset notes: ds-cb-escalation-labels directly, and ds-cb-call-linkage and ds-cb-sessions through feat-cb-prior-calls-v1 and the linkage join.
Notes: chatbot-deflection/ds-cb-escalation-labels.md, chatbot-deflection/ds-cb-call-linkage.md, chatbot-deflection/ds-cb-sessions.md

## Q7
The three features both nps-gbm-v1 and nps-gbm-v2 build on directly are feat-nps-complaint-flag-v1, feat-nps-theme-share-v1 and feat-nps-txn-freq-v1.
Notes: nps-drivers/feat-nps-complaint-flag-v1.md, nps-drivers/feat-nps-theme-share-v1.md, nps-drivers/feat-nps-txn-freq-v1.md

## Q8
mq3-response-gbm-v1 is the only current model that builds directly on a replaced feature. It uses feat-mq3-recency-v1, which has been replaced by feat-mq3-recency-v2.
Notes: marketing-uplift-q3/mq3-response-gbm-v1.md, marketing-uplift-q3/feat-mq3-recency-v1.md, marketing-uplift-q3/feat-mq3-recency-v2.md

## Q9
Five decision notes rest on feat-c25-util-v2, all through other notes: dec-c25-ship-gbm-v2 and dec-c25-drop-app-sessions in churn-2025, and dec-ror-value-band-v2, dec-ror-reallocate-t3 and dec-ror-matrix-v4 in retention-offers-roi. None builds on it directly.
Notes: churn-2025/dec-c25-ship-gbm-v2.md, churn-2025/dec-c25-drop-app-sessions.md, retention-offers-roi/dec-ror-value-band-v2.md, retention-offers-roi/dec-ror-reallocate-t3.md, retention-offers-roi/dec-ror-matrix-v4.md

## Q10
The line runs fraud25-gbm-v1, then fraud25-gbm-v2, then fraud26-gbm-v1, then fraud26-gbm-v2, and ends at fraud26-gbm-v3, which is in force. fraud26-gbm-v3 builds directly on fraud26-gbm-v2, exp-207, feat-f26-amt-zscore and feat-f26-geo-mismatch.
Notes: fraud-2026/fraud26-gbm-v3.md, fraud-2026/fraud26-gbm-v2.md, fraud-2026/exp-207.md, fraud-2026/feat-f26-amt-zscore.md, fraud-2026/feat-f26-geo-mismatch.md