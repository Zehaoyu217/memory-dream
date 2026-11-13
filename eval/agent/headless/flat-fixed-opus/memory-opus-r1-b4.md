## Q1
cb-escalate-v1 rests on three dataset notes. It uses ds-cb-escalation-labels directly. Through ds-cb-escalation-labels and feat-cb-prior-calls-v1 it also rests on ds-cb-call-linkage and ds-cb-sessions.
Notes: work/ds-cb-escalation-labels.md, work/ds-cb-call-linkage.md, work/ds-cb-sessions.md

## Q2
Both models build directly on feat-nps-complaint-flag-v1, feat-nps-theme-share-v1 and feat-nps-txn-freq-v1. nps-gbm-v2 also adds feat-nps-fee-shock-v2, which v1 does not use.
Notes: work/feat-nps-complaint-flag-v1.md, work/feat-nps-theme-share-v1.md, work/feat-nps-txn-freq-v1.md

## Q3
Five decisions rest on feat-c25-util-v2, all through other notes: dec-c25-ship-gbm-v2, dec-c25-drop-app-sessions, dec-ror-value-band-v2, dec-ror-reallocate-t3 and dec-ror-matrix-v4.
Notes: work/dec-c25-ship-gbm-v2.md, work/dec-c25-drop-app-sessions.md, work/dec-ror-value-band-v2.md, work/dec-ror-reallocate-t3.md, work/dec-ror-matrix-v4.md

## Q4
The line runs fraud25-gbm-v1 → fraud25-gbm-v2 → fraud26-gbm-v1 → fraud26-gbm-v2 → fraud26-gbm-v3, and fraud26-gbm-v3 is the model in force now. It is built on exp-207-fraud-2026, feat-f26-amt-zscore, feat-f26-geo-mismatch and fraud26-gbm-v2.
Notes: work/fraud26-gbm-v3.md, work/exp-207-fraud-2026.md, work/feat-f26-amt-zscore.md, work/feat-f26-geo-mismatch.md, work/fraud26-gbm-v2.md

## Q5
churn-gbm-2025-v2 rests on four dataset notes, all through other notes: ds-c25-accounts-snapshot, ds-c25-app-engagement, ds-c25-oot-2024h1 and ds-c25-churn-labels.
Notes: work/ds-c25-accounts-snapshot.md, work/ds-c25-app-engagement.md, work/ds-c25-oot-2024h1.md, work/ds-c25-churn-labels.md

## Q6
Both models build directly on feat-rdm-app-installed and feat-rdm-last-activity-v1.
Notes: work/feat-rdm-app-installed.md, work/feat-rdm-last-activity-v1.md

## Q7
Four decisions rest on ds-csb-churn-labels. dec-csb-90d-window uses it directly, and dec-csb-tenure-floor, dec-csb-ship-xgb-v1 and dec-csb-ship-xgb-v2 rest on it through other notes.
Notes: work/dec-csb-90d-window.md, work/dec-csb-tenure-floor.md, work/dec-csb-ship-xgb-v1.md, work/dec-csb-ship-xgb-v2.md

## Q8
The line runs find-hp-naive-effect → find-hp-adjusted-effect → find-hp-effect-v2, and find-hp-effect-v2 is the one in force now. It is built on exp-404-hardship-programs (the difference-in-differences experiment), exp-408-hardship-programs (the propensity matching on holdout-2025q4) and find-hp-adjusted-effect. The memory tool linked the matching experiment to exp-402, but the note's own text and its -4.7pp result match exp-408.
Notes: work/find-hp-effect-v2.md, work/exp-404-hardship-programs.md, work/exp-408-hardship-programs.md, work/find-hp-adjusted-effect.md

## Q9
csb-lr-base uses ds-csb-churn-labels and ds-csb-oot-2025q1 directly. Through them it also rests on ds-csb-biz-accounts.
Notes: work/ds-csb-churn-labels.md, work/ds-csb-oot-2025q1.md, work/ds-csb-biz-accounts.md

## Q10
Both models build directly on feat-trv-cross-border-share and feat-trv-seasonality-adj.
Notes: work/feat-trv-cross-border-share.md, work/feat-trv-seasonality-adj.md