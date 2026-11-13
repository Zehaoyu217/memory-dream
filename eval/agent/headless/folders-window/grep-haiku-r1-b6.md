## Q1
Only one note in another project builds directly on fraud26-gbm-v3: dispute-triage's feat-disp-fraud-score, which takes the model's score for each dispute. The dispute decision (dec-disp-fraud-score-in) depends on it only through that feature.
Notes: dispute-triage/feat-disp-fraud-score.md

## Q2
churn-gbm-2025-v2 rests on four dataset notes, reached through its feature, experiment and decision chain: the account-month population, the 60-day churn labels, the app-engagement data, and the 2024 holdout. The app-session decision and the baseline model are the routes that reach the app-engagement and holdout datasets.
Notes: churn-2025/ds-c25-accounts-snapshot.md, churn-2025/ds-c25-churn-labels.md, churn-2025/ds-c25-app-engagement.md, churn-2025/ds-c25-oot-2024h1.md

## Q3
Both rdm-propensity-lr and rdm-uplift-v1 build directly on feat-rdm-app-installed and feat-rdm-last-activity-v1.
Notes: reactivation-dormant/feat-rdm-app-installed.md, reactivation-dormant/feat-rdm-last-activity-v1.md

## Q4
rdm-propensity-lr is the only current model that builds directly on a replaced feature: it uses feat-rdm-last-activity-v1, which feat-rdm-last-activity-v2 replaced in June 2025. rdm-uplift-v2 uses only current features, and rdm-uplift-v1 is no longer current.
Notes: reactivation-dormant/rdm-propensity-lr.md

## Q5
Four decisions rest on ds-csb-churn-labels: dec-csb-90d-window directly, and dec-csb-tenure-floor, dec-csb-ship-xgb-v1 and dec-csb-ship-xgb-v2 through the csb-lr-base and exp-202/exp-203/exp-206 chain.
Notes: churn-small-business/dec-csb-90d-window.md, churn-small-business/dec-csb-tenure-floor.md, churn-small-business/dec-csb-ship-xgb-v1.md, churn-small-business/dec-csb-ship-xgb-v2.md

## Q6
The line runs find-hp-naive-effect, then find-hp-adjusted-effect, then find-hp-effect-v2, which is the note in force (-4.7pp). find-hp-effect-v2 is built on the difference-in-differences experiment exp-404, the propensity matching holdout experiment exp-408, and find-hp-adjusted-effect.
Notes: hardship-programs/find-hp-effect-v2.md, hardship-programs/exp-404.md, hardship-programs/exp-408.md, hardship-programs/find-hp-adjusted-effect.md

## Q7
Only one note in another project builds directly on inc-gbm-v3: application-scorecard's feat-app-income-est, which uses the income estimate band.
Notes: application-scorecard/feat-app-income-est.md

## Q8
csb-lr-base rests on three dataset notes: ds-csb-biz-accounts (through its features and labels), ds-csb-churn-labels, and ds-csb-oot-2025q1.
Notes: churn-small-business/ds-csb-biz-accounts.md, churn-small-business/ds-csb-churn-labels.md, churn-small-business/ds-csb-oot-2025q1.md

## Q9
trv-ridge-v2 and trv-ridge-v3 both build directly on feat-trv-cross-border-share and feat-trv-seasonality-adj.
Notes: travel-spend-recovery/feat-trv-cross-border-share.md, travel-spend-recovery/feat-trv-seasonality-adj.md

## Q10
ror-uplift-v1 is the only current model that builds directly on a replaced feature: it uses feat-ror-value-band-v1, which feat-ror-value-band-v2 replaced. ror-roi-v2 uses only current features, and ror-roi-v1 is superseded.
Notes: retention-offers-roi/ror-uplift-v1.md