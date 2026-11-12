## Q1
One note in another project builds directly on fraud26-gbm-v3: dispute-triage's feat-disp-fraud-score, which says "Builds on the cards.disputes dataset and fraud-2026/fraud26-gbm-v3". The dispute-triage decision dec-disp-fraud-score-in only says it "creates a dependency" on the model; its build line names exp-307 and the feature, not the model, so it isn't counted.
Notes: dispute-triage/feat-disp-fraud-score.md

## Q2
Following everything back from churn-gbm-2025-v2 reaches all four churn-2025 dataset notes. These are the accounts snapshot, app engagement (through feat-c25-app-sessions and q-c25-app-lift), the churn labels (through exp-101 and fnd-c25-90d-feedback-lag) and the c25-oot-2024h1 holdout (through churn-lr-base-2025).
Notes: churn-2025/ds-c25-accounts-snapshot.md, churn-2025/ds-c25-app-engagement.md, churn-2025/ds-c25-churn-labels.md, churn-2025/ds-c25-oot-2024h1.md

## Q3
Both models build directly on the app-installed flag and on last-activity v1. rdm-propensity-lr also uses balance band and prior response, but rdm-uplift-v1 doesn't list those directly.
Notes: reactivation-dormant/feat-rdm-app-installed.md, reactivation-dormant/feat-rdm-last-activity-v1.md

## Q4
rdm-propensity-lr is still kept as the baseline and builds directly on feat-rdm-last-activity-v1, which feat-rdm-last-activity-v2 replaced. rdm-uplift-v1 also uses v1 but has itself been replaced by rdm-uplift-v2, and v2 uses the newer feature.
Notes: reactivation-dormant/rdm-propensity-lr.md

## Q5
All four decision notes in the project rest on ds-csb-churn-labels. dec-csb-90d-window builds on it directly. dec-csb-tenure-floor gets there through exp-202 and csb-lr-base. dec-csb-ship-xgb-v1 gets there through csb-xgb-v1, fnd-csb-volatility-lift, exp-203/exp-204 and csb-lr-base. dec-csb-ship-xgb-v2 gets there through csb-xgb-v2 and dec-csb-ship-xgb-v1.
Notes: churn-small-business/dec-csb-90d-window.md, churn-small-business/dec-csb-tenure-floor.md, churn-small-business/dec-csb-ship-xgb-v1.md, churn-small-business/dec-csb-ship-xgb-v2.md

## Q6
The line runs find-hp-naive-effect → find-hp-adjusted-effect → find-hp-effect-v2. find-hp-effect-v2 (−4.7pp) is the one in force now. It builds on exp-404 (the difference-in-differences experiment), exp-408 (the caliper propensity-matching run on the holdout) and find-hp-adjusted-effect.
Notes: hardship-programs/find-hp-effect-v2.md, hardship-programs/exp-404.md, hardship-programs/exp-408.md, hardship-programs/find-hp-adjusted-effect.md

## Q7
One note in another project builds directly on inc-gbm-v3: application-scorecard's feat-app-income-est. Other scorecard notes (exp-506, exp-507, app-scorecard-v4) use the income estimate only through that feature.
Notes: application-scorecard/feat-app-income-est.md

## Q8
csb-lr-base rests on three dataset notes: ds-csb-churn-labels and ds-csb-oot-2025q1 directly, and ds-csb-biz-accounts through those two and through the spend and tenure features.
Notes: churn-small-business/ds-csb-biz-accounts.md, churn-small-business/ds-csb-churn-labels.md, churn-small-business/ds-csb-oot-2025q1.md

## Q9
Both models build directly on the cross-border share feature and the seasonality adjustment feature. trv-ridge-v3 also adds feat-trv-funnel-v2.
Notes: travel-spend-recovery/feat-trv-cross-border-share.md, travel-spend-recovery/feat-trv-seasonality-adj.md

## Q10
ror-uplift-v1 has not been replaced and builds directly on feat-ror-value-band-v1, which feat-ror-value-band-v2 replaced. ror-roi-v2 already uses value band v2, and ror-roi-v1 has been superseded.
Notes: retention-offers-roi/ror-uplift-v1.md