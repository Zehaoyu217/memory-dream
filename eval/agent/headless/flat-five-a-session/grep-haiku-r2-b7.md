## Q1
cb-escalate-v1 rests on three dataset notes. ds-cb-escalation-labels is its direct target, and it builds on ds-cb-sessions. Its other input, feat-cb-prior-calls-v1, builds on ds-cb-call-linkage, which builds on ds-cb-sessions.
Notes: work/ds-cb-escalation-labels.md, work/ds-cb-call-linkage.md, work/ds-cb-sessions.md

## Q2
Both nps-gbm-v1 and nps-gbm-v2 build directly on the complaint flag, the theme shares and the transaction frequency features.
Notes: work/feat-nps-complaint-flag-v1.md, work/feat-nps-theme-share-v1.md, work/feat-nps-txn-freq-v1.md

## Q3
Five decision notes rest on feat-c25-util-v2. Two build on it directly or via churn-gbm-2025-v2 (dec-c25-ship-gbm-v2, and dec-c25-drop-app-sessions via exp-105 and exp-104). Three go through the ror chain: feat-ror-churn-score, then ror-uplift-v1, ror-roi-v1 and exp-404, reaching dec-ror-reallocate-t3, dec-ror-matrix-v4 and dec-ror-value-band-v2.
Notes: work/dec-c25-drop-app-sessions.md, work/dec-c25-ship-gbm-v2.md, work/dec-ror-reallocate-t3.md, work/dec-ror-matrix-v4.md, work/dec-ror-value-band-v2.md

## Q4
fraud26-gbm-v3 is the one in force, at the end of fraud25-gbm-v1 → fraud25-gbm-v2 → fraud26-gbm-v1 → fraud26-gbm-v2 → fraud26-gbm-v3. It is built on fraud26-gbm-v2, the geo-mismatch and amount z-score experiment (exp-207-fraud-2026), feat-f26-geo-mismatch and feat-f26-amt-zscore.
Notes: work/fraud26-gbm-v3.md, work/fraud26-gbm-v2.md, work/exp-207-fraud-2026.md, work/feat-f26-geo-mismatch.md, work/feat-f26-amt-zscore.md

## Q5
churn-gbm-2025-v2 rests on four dataset notes. ds-c25-accounts-snapshot is the base population. ds-c25-churn-labels is the label source, reached through exp-101 and dec-c25-label-60d. ds-c25-oot-2024h1 is the 2024 holdout that the logistic baseline builds on. ds-c25-app-engagement is the source for the app-session features that were later dropped.
Notes: work/ds-c25-accounts-snapshot.md, work/ds-c25-churn-labels.md, work/ds-c25-oot-2024h1.md, work/ds-c25-app-engagement.md