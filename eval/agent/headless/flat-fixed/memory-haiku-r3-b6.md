## Q1
Two decision notes rest on feat-xs-balance-proxy: dec-xs-top-decile-offer (directly through xs-gbm-v2) and dec-xs-retrain-quarterly (through find-xs-drift-2026 and exp-407-oot-2026h1). The tool also listed 26 other notes as possibly built on it, but none of them is confirmed, so I left them out.
Notes: work/dec-xs-top-decile-offer.md, work/dec-xs-retrain-quarterly.md

## Q2
mrisk-gbm-v1 was replaced by mrisk-gbm-v2, which was replaced by mrisk-gbm-v3. mrisk-gbm-v3 is in force and is built on exp-507-merchant-risk, feat-mrisk-dispute-ratio and mrisk-gbm-v2.
Notes: work/mrisk-gbm-v3.md, work/exp-507-merchant-risk.md, work/feat-mrisk-dispute-ratio.md, work/mrisk-gbm-v2.md

## Q3
cli-logreg-baseline rests on two dataset notes: ds-cli-eligible-pop directly, through feat-cli-util-v1 and feat-cli-pay-behaviour, and ds-cli-outcome-90d, through feat-cli-spend-velocity. The `ask` output resolved the query to churn-lr-base-2025 instead, so I traced the chain from cli-logreg-baseline's own frontmatter.
Notes: work/cli-logreg-baseline.md, work/ds-cli-eligible-pop.md, work/ds-cli-outcome-90d.md

## Q4
Two decision notes rest on ds-clv-holdout-2021h1: dec-clv-ship-ml-v1 (through clv-ml-v1) and dec-clv-ship-ml-v2 (through clv-ml-v2).
Notes: work/dec-clv-ship-ml-v1.md, work/dec-clv-ship-ml-v2.md

## Q5
pbs-kmeans-v1 was replaced by pbs-gmm-v2, which was replaced by pbs-gmm-v3. pbs-gmm-v3 is in force and is built on exp-403-payment-behavior-segments, feat-pbs-timing-v2 and pbs-gmm-v2.
Notes: work/pbs-gmm-v3.md, work/exp-403-payment-behavior-segments.md, work/feat-pbs-timing-v2.md, work/pbs-gmm-v2.md

## Q6
xs-call-uplift-v1 rests on two dataset notes: ds-xs-callcentre directly through exp-403-callcentre-naive and feat-xs-call-recent, and ds-xs-offer-log through q-xs-propensity.
Notes: work/xs-call-uplift-v1.md, work/ds-xs-callcentre.md, work/ds-xs-offer-log.md

## Q7
Two decision notes rest on ds-disp-analyst-labels: dec-disp-labels-two-analyst directly, and dec-disp-autoresolve-090, dec-disp-autoresolve-095 and dec-disp-fraud-score-in through other notes. The tool listed these as resting on it, though only dec-disp-fraud-score-in was printed in its output.
Notes: work/dec-disp-labels-two-analyst.md, work/dec-disp-autoresolve-090.md, work/dec-disp-autoresolve-095.md, work/dec-disp-fraud-score-in.md

## Q8
rs-xgb-v1 was replaced by rs-xgb-v2, which was replaced by rs-xgb-v3. rs-xgb-v3 is in force and is built on exp-308-recovery-scoring and rs-xgb-v2.
Notes: work/rs-xgb-v3.md, work/exp-308-recovery-scoring.md, work/rs-xgb-v2.md

## Q9
clv-bgnbd-v1 rests on three dataset notes: ds-clv-cohort-panel, ds-clv-holdout-2021h1 and ds-clv-revenue-monthly.
Notes: work/clv-bgnbd-v1.md, work/ds-clv-cohort-panel.md, work/ds-clv-holdout-2021h1.md, work/ds-clv-revenue-monthly.md

## Q10
Two decision notes rest on ds-ed-bureau-join: dec-ed-promote-v3 and dec-ed-gbm-for-watchlist, both through ed-gbm-v3 or feat-ed-bureau-slope-v1.
Notes: work/dec-ed-promote-v3.md, work/dec-ed-gbm-for-watchlist.md