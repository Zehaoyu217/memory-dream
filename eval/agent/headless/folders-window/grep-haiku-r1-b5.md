## Q1
Both models share three feature bases: feat-mq3-app-sessions-30d, feat-mq3-prior-treat, and feat-mq3-recency-v1.
Notes: marketing-uplift-q3/mq3-response-gbm-v1.md, marketing-uplift-q3/mq3-uplift-tlearner-v1.md, marketing-uplift-q3/feat-mq3-app-sessions-30d.md, marketing-uplift-q3/feat-mq3-prior-treat.md, marketing-uplift-q3/feat-mq3-recency-v1.md

## Q2
inc-linear-baseline builds on feat-inc-payroll-cadence-v1, which feat-inc-payroll-cadence-v2 replaced on 2025-12-16. The current inc-gbm-v3 builds on no replaced feature or dataset. The baseline is not in production, so this is the only current model that rests on a replaced input.
Notes: income-estimation/inc-linear-baseline.md, income-estimation/feat-inc-payroll-cadence-v1.md, income-estimation/feat-inc-payroll-cadence-v2.md

## Q3
Four decision notes rest on ds-cb-call-linkage: dec-cb-metric-24h, dec-cb-metric-48h (which replaces dec-cb-metric-24h), dec-cb-handoff-v2, and dec-cb-rollout-60. The last two reach it through the exp-307 and fnd-cb-volume-shift chains.
Notes: chatbot-deflection/ds-cb-call-linkage.md, chatbot-deflection/dec-cb-metric-24h.md, chatbot-deflection/dec-cb-metric-48h.md, chatbot-deflection/dec-cb-handoff-v2.md, chatbot-deflection/dec-cb-rollout-60.md

## Q4
The ed-gbm-v1 line runs ed-gbm-v1 → ed-gbm-v2 → ed-gbm-v3, and ed-gbm-v3 is the one in force (promoted by dec-ed-promote-v3 on 2026-06-18, which replaces dec-ed-gbm-for-watchlist). ed-gbm-v3 builds on ed-gbm-v2, feat-ed-util-trend-v1, feat-ed-cashadv-v1, feat-ed-minpay-v2, feat-ed-bureau-slope-v1, the bureau slope lift experiment, and the 2026 H1 out-of-time set.
Notes: early-delinquency/ed-gbm-v1.md, early-delinquency/ed-gbm-v2.md, early-delinquency/ed-gbm-v3.md, early-delinquency/dec-ed-promote-v3.md

## Q5
Only fraud-2026/dec-f26-replace-f25.md builds directly on dec-f25-champion-v2. It is the decision that made fraud26-gbm-v1 replace the 2025 champion.
Notes: fraud-2026/dec-f26-replace-f25.md

## Q6
The only dataset root behind cb-escalate-v1 is ds-cb-sessions. Both ds-cb-escalation-labels (the target) and ds-cb-call-linkage (via feat-cb-prior-calls-v1) build on it, so they are not roots themselves.
Notes: chatbot-deflection/ds-cb-sessions.md, chatbot-deflection/ds-cb-escalation-labels.md, chatbot-deflection/ds-cb-call-linkage.md, chatbot-deflection/feat-cb-prior-calls-v1.md, chatbot-deflection/cb-escalate-v1.md

## Q7
Both models share three feature bases: feat-nps-complaint-flag-v1, feat-nps-theme-share-v1, and feat-nps-txn-freq-v1. nps-gbm-v2 also adds feat-nps-fee-shock-v2.
Notes: nps-drivers/nps-gbm-v1.md, nps-drivers/nps-gbm-v2.md, nps-drivers/feat-nps-complaint-flag-v1.md, nps-drivers/feat-nps-theme-share-v1.md, nps-drivers/feat-nps-txn-freq-v1.md

## Q8
mq3-response-gbm-v1 is still current as a reporting metric (dec-mq3-target-uplift), and it builds on feat-mq3-recency-v1, which feat-mq3-recency-v2 replaced. The targeting model mq3-uplift-xl-v2 builds only on current inputs (its other upstream is the superseded mq3-uplift-tlearner-v1, which is a model rather than a feature or dataset).
Notes: marketing-uplift-q3/mq3-response-gbm-v1.md, marketing-uplift-q3/feat-mq3-recency-v1.md, marketing-uplift-q3/feat-mq3-recency-v2.md

## Q9
Two decision notes rest on feat-c25-util-v2. dec-c25-ship-gbm-v2 builds directly on churn-gbm-2025-v2, which uses util-v2, and it needs the util-v2 time-matched join. dec-c25-drop-app-sessions builds on exp-105, which is exp-104 on util-v2 with app sessions removed. dec-c25-ship-gbm-v1 and dec-c25-label-60d do not rest on util-v2.
Notes: churn-2025/feat-c25-util-v2.md, churn-2025/churn-gbm-2025-v2.md, churn-2025/exp-104.md, churn-2025/exp-105.md, churn-2025/dec-c25-ship-gbm-v2.md, churn-2025/dec-c25-drop-app-sessions.md

## Q10
The fraud25-gbm-v1 line ends at fraud25-gbm-v2, which is in force because dec-f25-champion-v2 promoted it on 2025-06-30. fraud25-gbm-v3 was not promoted (dec-f25-no-v3 keeps v2 live). fraud25-gbm-v2 builds on the fraud label arrival lag (ds-f25-labels), feat-f25-amt-ratio, feat-f25-device-age, feat-f25-hour-band, feat-f25-mcc-travel, feat-f25-velocity-v1, and fraud25-gbm-v1.
Notes: fraud-2025/fraud25-gbm-v1.md, fraud-2025/fraud25-gbm-v2.md, fraud-2025/dec-f25-champion-v2.md, fraud-2025/dec-f25-no-v3.md, fraud-2025/ds-f25-labels.md