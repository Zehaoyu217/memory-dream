## Q1
Two decision notes rest on feat-xs-balance-proxy: dec-xs-top-decile-offer (via exp-405-top-decile and the boosting model with payroll) and dec-xs-retrain-quarterly (via exp-407-oot-2026h1 and find-xs-drift-2026). The balance proxy is replaced by feat-xs-payroll-flag-v2 but still sits upstream of both decisions.
Notes: work/feat-xs-balance-proxy.md, work/xs-gbm-v1.md, work/feat-xs-payroll-flag-v2.md, work/xs-gbm-v2.md, work/exp-405-top-decile.md, work/exp-407-oot-2026h1.md, work/find-xs-drift-2026.md, work/dec-xs-top-decile-offer.md, work/dec-xs-retrain-quarterly.md

## Q2
mrisk-gbm-v3 is the model in force, after mrisk-gbm-v1 was replaced by v2 and v2 by v3. It builds on exp-507-merchant-risk, feat-mrisk-dispute-ratio and mrisk-gbm-v2.
Notes: work/mrisk-gbm-v3.md, work/exp-507-merchant-risk.md, work/feat-mrisk-dispute-ratio.md, work/mrisk-gbm-v2.md

## Q3
cli-logreg-baseline traces back to two dataset roots, ds-cli-eligible-pop and ds-cli-outcome-90d. It builds on the full-pay versus minimum-pay feature, feat-cli-spend-velocity and feat-cli-util-v1, and those lead back to the two roots.
Notes: work/cli-logreg-baseline.md, work/feat-cli-pay-behaviour.md, work/feat-cli-spend-velocity.md, work/feat-cli-util-v1.md, work/q-cli-utilization-trigger.md, work/ds-cli-eligible-pop.md, work/ds-cli-outcome-90d.md

## Q4
Two decision notes rest on ds-clv-holdout-2021h1: dec-clv-ship-ml-v1 and dec-clv-ship-ml-v2. The chain runs through exp-501, which builds on the holdout and is the basis for clv-bgnbd-v1 and clv-ml-v1. The holdout is only used as an eval set in exp-502 and dec-clv-include-losses, so those do not count.
Notes: work/ds-clv-holdout-2021h1.md, work/exp-501-customer-lifetime-value.md, work/clv-bgnbd-v1.md, work/clv-ml-v1.md, work/dec-clv-ship-ml-v1.md, work/dec-clv-ship-ml-v2.md

## Q5
pbs-kmeans-v1 was replaced by pbs-gmm-v2, which was replaced by pbs-gmm-v3, the segment model in force. pbs-gmm-v3 builds on exp-403-payment-behavior-segments, feat-pbs-timing-v2 and pbs-gmm-v2.
Notes: work/pbs-gmm-v3.md, work/exp-403-payment-behavior-segments.md, work/feat-pbs-timing-v2.md, work/pbs-gmm-v2.md

## Q6
xs-call-uplift-v1 traces back to the dataset ds-xs-offer-log, the offer log of 1.42M eligible cardholder-waves, through two routes. The first is the call-contact dataset ds-xs-callcentre, which joins to the offer log, feeding the recent-call feature and the naive call comparison. The second is the propensity covariates taken from the offer log, which are built on q-xs-propensity.
Notes: work/xs-call-uplift-v1.md, work/feat-xs-call-recent.md, work/find-xs-call-overstated.md, work/exp-403-callcentre-naive.md, work/ds-xs-callcentre.md, work/ds-xs-offer-log.md, work/q-xs-propensity.md

## Q7
Three decision notes rest on ds-disp-analyst-labels: dec-disp-labels-two-analyst directly, and dec-disp-autoresolve-090 and dec-disp-autoresolve-095 through disp-lgbm-v1 and disp-lgbm-v2. dec-disp-fraud-score-in does not count, because it builds on exp-307 and feat-disp-fraud-score and the labels only appear as the eval set.
Notes: work/ds-disp-analyst-labels.md, work/dec-disp-labels-two-analyst.md, work/disp-lgbm-v1.md, work/disp-lgbm-v2.md, work/dec-disp-autoresolve-090.md, work/dec-disp-autoresolve-095.md

## Q8
rs-xgb-v3 is the recovery model in force, after rs-xgb-v1 was replaced by rs-xgb-v2 and v2 by v3. It builds on exp-308-recovery-scoring and rs-xgb-v2.
Notes: work/rs-xgb-v3.md, work/exp-308-recovery-scoring.md, work/rs-xgb-v2.md

## Q9
clv-bgnbd-v1 rests on ds-clv-cohort-panel through both of its features, the six-month revenue feature (via ds-clv-revenue-monthly) and the months-on-book feature. Its accuracy-test input is most likely exp-501, which builds on ds-clv-holdout-2021h1, so that holdout is a second root. The accuracy test has no note of its own, so that last link is inferred.
Notes: work/clv-bgnbd-v1.md, work/feat-clv-arpu-v1.md, work/ds-clv-revenue-monthly.md, work/feat-clv-tenure.md, work/ds-clv-cohort-panel.md, work/exp-501-customer-lifetime-value.md, work/ds-clv-holdout-2021h1.md

## Q10
Two decision notes rest on ds-ed-bureau-join: dec-ed-gbm-for-watchlist, through find-ed-gbm-vs-logit, exp-201 and the champion ed-logit-v1, and dec-ed-promote-v3, through feat-ed-bureau-slope-v1 and ed-gbm-v3.
Notes: work/ds-ed-bureau-join.md, work/ed-logit-v1.md, work/exp-201-early-delinquency.md, work/find-ed-gbm-vs-logit.md, work/dec-ed-gbm-for-watchlist.md, work/feat-ed-bureau-slope-v1.md, work/ed-gbm-v3.md, work/dec-ed-promote-v3.md