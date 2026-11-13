## Q1
cb-escalate-v1 is built on the escalation label dataset and feat-cb-prior-calls-v1. The label dataset is built on ds-cb-sessions, and the prior-calls feature is built on ds-cb-call-linkage, which is itself built on ds-cb-sessions. So it rests on three dataset notes: ds-cb-escalation-labels, ds-cb-call-linkage and ds-cb-sessions.
Notes: work/ds-cb-escalation-labels.md, work/ds-cb-call-linkage.md, work/ds-cb-sessions.md

## Q2
Both models build directly on three feature notes: the complaint flag (feat-nps-complaint-flag-v1), theme shares (feat-nps-theme-share-v1) and transaction frequency (feat-nps-txn-freq-v1). Only v2 adds fee shock v2.
Notes: work/feat-nps-complaint-flag-v1.md, work/feat-nps-theme-share-v1.md, work/feat-nps-txn-freq-v1.md

## Q3
Two churn-2025 decisions rest on it through exp-104/105/106 and churn-gbm-2025-v2: dec-c25-drop-app-sessions and dec-c25-ship-gbm-v2. Three retention-offer decisions also rest on it, because feat-ror-churn-score is built on churn-gbm-2025-v2 and feeds ror-uplift-v1 → ror-roi-v1 → exp-404 → fnd-ror-cashback-roi: dec-ror-reallocate-t3, dec-ror-matrix-v4 and dec-ror-value-band-v2.
Notes: work/dec-c25-drop-app-sessions.md, work/dec-c25-ship-gbm-v2.md, work/dec-ror-reallocate-t3.md, work/dec-ror-matrix-v4.md, work/dec-ror-value-band-v2.md

## Q4
The line runs fraud25-gbm-v1 → fraud25-gbm-v2 → fraud26-gbm-v1 → fraud26-gbm-v2 → fraud26-gbm-v3, and fraud26-gbm-v3 is the model in force now. (fraud25-gbm-v3 was a challenger that was never promoted and did not replace v2.) fraud26-gbm-v3 is built on exp-207-fraud-2026 (the geo-mismatch and amount z-score experiment), feat-f26-amt-zscore, feat-f26-geo-mismatch and fraud26-gbm-v2.
Notes: work/fraud26-gbm-v3.md, work/exp-207-fraud-2026.md, work/feat-f26-amt-zscore.md, work/feat-f26-geo-mismatch.md, work/fraud26-gbm-v2.md

## Q5
It rests on four dataset notes. The accounts snapshot comes in through the util, payment and recency features. App engagement comes in through feat-c25-app-sessions and the decision to drop app sessions. The churn labels come in through dec-c25-label-60d and exp-101. The 2024 holdout comes in through churn-lr-base-2025.
Notes: work/ds-c25-accounts-snapshot.md, work/ds-c25-app-engagement.md, work/ds-c25-churn-labels.md, work/ds-c25-oot-2024h1.md

## Q6
Both build directly on feat-rdm-app-installed and feat-rdm-last-activity-v1. rdm-uplift-v1 mentions prior response and balance band in its text, but its "Builds on" line does not list them.
Notes: work/feat-rdm-app-installed.md, work/feat-rdm-last-activity-v1.md

## Q7
Four decisions rest on it. dec-csb-90d-window is built on it directly. dec-csb-tenure-floor comes through csb-lr-base and exp-202. dec-csb-ship-xgb-v1 comes through csb-xgb-v1 and fnd-csb-volatility-lift. dec-csb-ship-xgb-v2 comes through csb-xgb-v2.
Notes: work/dec-csb-90d-window.md, work/dec-csb-tenure-floor.md, work/dec-csb-ship-xgb-v1.md, work/dec-csb-ship-xgb-v2.md

## Q8
find-hp-naive-effect (+11.6pp) was replaced by find-hp-adjusted-effect (-6.1pp), which was replaced by find-hp-effect-v2 (-4.7pp), the note in force now. find-hp-effect-v2 is built on exp-404-hardship-programs (difference-in-differences), exp-408-hardship-programs (propensity matching on the holdout) and find-hp-adjusted-effect.
Notes: work/find-hp-effect-v2.md, work/exp-404-hardship-programs.md, work/exp-408-hardship-programs.md, work/find-hp-adjusted-effect.md

## Q9
csb-lr-base is built directly on ds-csb-churn-labels and ds-csb-oot-2025q1. Through those notes and through feat-csb-spend-raw and feat-csb-tenure-band, it also rests on ds-csb-biz-accounts.
Notes: work/ds-csb-churn-labels.md, work/ds-csb-oot-2025q1.md, work/ds-csb-biz-accounts.md

## Q10
Both build directly on feat-trv-cross-border-share and feat-trv-seasonality-adj. Only v3 adds feat-trv-funnel-v2.
Notes: work/feat-trv-cross-border-share.md, work/feat-trv-seasonality-adj.md