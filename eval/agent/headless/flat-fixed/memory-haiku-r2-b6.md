## Q1
Two decision notes rest on feat-xs-balance-proxy: dec-xs-top-decile-offer (through xs-gbm-v2 and exp-405) and dec-xs-retrain-quarterly (through exp-407 and find-xs-drift-2026).
Notes: work/dec-xs-top-decile-offer.md, work/dec-xs-retrain-quarterly.md

## Q2
mrisk-gbm-v1 was replaced by mrisk-gbm-v2, which was replaced by mrisk-gbm-v3, the one in force now. mrisk-gbm-v3 is built on exp-507-merchant-risk, feat-mrisk-dispute-ratio and mrisk-gbm-v2.
Notes: work/mrisk-gbm-v3.md, work/exp-507-merchant-risk.md, work/feat-mrisk-dispute-ratio.md, work/mrisk-gbm-v2.md

## Q3
cli-logreg-baseline rests on two dataset notes. Its features come from ds-cli-eligible-pop (directly, and via feat-cli-util-v1 and feat-cli-pay-behaviour) and ds-cli-outcome-90d (via feat-cli-spend-velocity). The tool's chain printout was for churn-lr-base-2025, a different note, so I followed cli-logreg-baseline by hand. ds-cli-eligible-pop also names cards.limits_history, which has no dataset note in the folder.
Notes: work/ds-cli-eligible-pop.md, work/ds-cli-outcome-90d.md

## Q4
Two decision notes rest on ds-clv-holdout-2021h1: dec-clv-ship-ml-v1 (through clv-ml-v1) and dec-clv-ship-ml-v2 (through clv-ml-v2 and exp-505-customer-lifetime-value).
Notes: work/dec-clv-ship-ml-v1.md, work/dec-clv-ship-ml-v2.md

## Q5
pbs-kmeans-v1 was replaced by pbs-gmm-v2, which was replaced by pbs-gmm-v3, the one in force now. pbs-gmm-v3 is built on exp-403-payment-behavior-segments, feat-pbs-timing-v2 and pbs-gmm-v2.
Notes: work/pbs-gmm-v3.md, work/exp-403-payment-behavior-segments.md, work/feat-pbs-timing-v2.md, work/pbs-gmm-v2.md

## Q6
xs-call-uplift-v1 rests on two dataset notes: ds-xs-callcentre (directly, via exp-403-callcentre-naive and feat-xs-call-recent) and ds-xs-offer-log (via q-xs-propensity).
Notes: work/ds-xs-callcentre.md, work/ds-xs-offer-log.md

## Q7
Four decision notes rest on ds-disp-analyst-labels: dec-disp-labels-two-analyst (directly), and dec-disp-autoresolve-090, dec-disp-autoresolve-095 and dec-disp-fraud-score-in (through the dispute models and experiments).
Notes: work/dec-disp-labels-two-analyst.md, work/dec-disp-autoresolve-090.md, work/dec-disp-autoresolve-095.md, work/dec-disp-fraud-score-in.md

## Q8
rs-xgb-v1 was replaced by rs-xgb-v2, which was replaced by rs-xgb-v3, the one in force now. rs-xgb-v3 is built on exp-308-recovery-scoring and rs-xgb-v2.
Notes: work/rs-xgb-v3.md, work/exp-308-recovery-scoring.md, work/rs-xgb-v2.md

## Q9
clv-bgnbd-v1 rests on three dataset notes: ds-clv-cohort-panel, ds-clv-holdout-2021h1 (both via exp-501-customer-lifetime-value) and ds-clv-revenue-monthly (via feat-clv-arpu-v1).
Notes: work/ds-clv-cohort-panel.md, work/ds-clv-holdout-2021h1.md, work/ds-clv-revenue-monthly.md

## Q10
Two decision notes rest on ds-ed-bureau-join: dec-ed-gbm-for-watchlist (through ed-gbm-v2 and find-ed-gbm-vs-logit) and dec-ed-promote-v3 (through ed-gbm-v3, exp-207-early-delinquency and find-ed-bureau-slope).
Notes: work/dec-ed-gbm-for-watchlist.md, work/dec-ed-promote-v3.md