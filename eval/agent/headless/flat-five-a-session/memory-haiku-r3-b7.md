## Q1
cb-escalate-v1 rests directly on the escalation label dataset and the prior-calls feature. Through those, it rests on the call-linkage dataset and the chat sessions dataset, so the dataset notes are ds-cb-escalation-labels, ds-cb-call-linkage and ds-cb-sessions.
Notes: work/ds-cb-escalation-labels.md, work/ds-cb-call-linkage.md, work/ds-cb-sessions.md

## Q2
Both nps-gbm-v1 and nps-gbm-v2 build directly on the complaint call flag, the theme share feature and the transaction frequency feature.
Notes: work/feat-nps-complaint-flag-v1.md, work/feat-nps-theme-share-v1.md, work/feat-nps-txn-freq-v1.md

## Q3
No decision note rests on feat-c25-util-v2 directly. Five do through the chain: dec-c25-drop-app-sessions, dec-c25-ship-gbm-v2, dec-ror-reallocate-t3, dec-ror-matrix-v4 and dec-ror-value-band-v2.
Notes: work/dec-c25-drop-app-sessions.md, work/dec-c25-ship-gbm-v2.md, work/dec-ror-reallocate-t3.md, work/dec-ror-matrix-v4.md, work/dec-ror-value-band-v2.md

## Q4
The line runs fraud25-gbm-v1 → fraud25-gbm-v2 → fraud26-gbm-v1 → fraud26-gbm-v2 → fraud26-gbm-v3, and fraud26-gbm-v3 is the one in force. It is built on exp-207-fraud-2026, feat-f26-amt-zscore, feat-f26-geo-mismatch and fraud26-gbm-v2.
Notes: work/fraud26-gbm-v3.md, work/exp-207-fraud-2026.md, work/feat-f26-amt-zscore.md, work/feat-f26-geo-mismatch.md, work/fraud26-gbm-v2.md

## Q5
churn-gbm-2025-v2 rests on four dataset notes, directly or through other notes: the accounts snapshot, app engagement, the 2024 H1 out-of-time holdout and the churn labels.
Notes: work/ds-c25-accounts-snapshot.md, work/ds-c25-app-engagement.md, work/ds-c25-oot-2024h1.md, work/ds-c25-churn-labels.md