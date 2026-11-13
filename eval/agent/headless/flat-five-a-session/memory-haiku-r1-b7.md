## Q1
cb-escalate-v1 rests directly on ds-cb-escalation-labels and feat-cb-prior-calls-v1. Through those it reaches ds-cb-call-linkage and ds-cb-sessions, so the dataset notes are ds-cb-escalation-labels, ds-cb-call-linkage and ds-cb-sessions.
Notes: work/ds-cb-escalation-labels.md, work/ds-cb-call-linkage.md, work/ds-cb-sessions.md

## Q2
nps-gbm-v1 and nps-gbm-v2 both build directly on the complaint call flag, the theme shares and the transaction frequency feature. nps-gbm-v2 also builds on feat-nps-fee-shock-v2, which nps-gbm-v1 does not use.
Notes: work/feat-nps-complaint-flag-v1.md, work/feat-nps-theme-share-v1.md, work/feat-nps-txn-freq-v1.md

## Q3
Five decision notes rest on feat-c25-util-v2: dec-c25-ship-gbm-v2 and dec-c25-drop-app-sessions (through the churn-2025 models and experiments), and dec-ror-value-band-v2, dec-ror-reallocate-t3 and dec-ror-matrix-v4 (through the retention-offer ROI chain).
Notes: work/dec-c25-ship-gbm-v2.md, work/dec-c25-drop-app-sessions.md, work/dec-ror-value-band-v2.md, work/dec-ror-reallocate-t3.md, work/dec-ror-matrix-v4.md

## Q4
The note in force at the end of the line is fraud26-gbm-v3, which replaced fraud26-gbm-v2 (itself a replacement of fraud26-gbm-v1 and then fraud25-gbm-v2). fraud26-gbm-v3 is built directly on exp-207-fraud-2026, feat-f26-amt-zscore, feat-f26-geo-mismatch and fraud26-gbm-v2.
Notes: work/fraud26-gbm-v3.md, work/exp-207-fraud-2026.md, work/feat-f26-amt-zscore.md, work/feat-f26-geo-mismatch.md, work/fraud26-gbm-v2.md

## Q5
churn-gbm-2025-v2 rests on four dataset notes, reached directly or through its feature, experiment and decision inputs: ds-c25-accounts-snapshot, ds-c25-app-engagement, ds-c25-churn-labels and ds-c25-oot-2024h1.
Notes: work/ds-c25-accounts-snapshot.md, work/ds-c25-app-engagement.md, work/ds-c25-churn-labels.md, work/ds-c25-oot-2024h1.md