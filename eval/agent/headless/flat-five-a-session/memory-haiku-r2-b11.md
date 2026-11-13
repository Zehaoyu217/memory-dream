## Q1
Two decision notes rest on feat-xs-balance-proxy: dec-xs-top-decile-offer (through xs-gbm-v2) and dec-xs-retrain-quarterly (through exp-407-oot-2026h1 and find-xs-drift-2026).
Notes: work/dec-xs-top-decile-offer.md, work/dec-xs-retrain-quarterly.md

## Q2
mrisk-gbm-v1 was replaced by mrisk-gbm-v2, which was replaced by mrisk-gbm-v3, the note in force now. mrisk-gbm-v3 is built on exp-507-merchant-risk, feat-mrisk-dispute-ratio and mrisk-gbm-v2.
Notes: work/mrisk-gbm-v3.md, work/exp-507-merchant-risk.md, work/feat-mrisk-dispute-ratio.md, work/mrisk-gbm-v2.md

## Q3
cli-logreg-baseline rests on two dataset notes: ds-cli-eligible-pop (directly, through feat-cli-util-v1 and feat-cli-pay-behaviour, and through ds-cli-outcome-90d) and ds-cli-outcome-90d (through feat-cli-spend-velocity). The tool printed a different model's chain (churn-lr-base-2025) under this question, so I traced this one by reading the notes.
Notes: work/cli-logreg-baseline.md, work/feat-cli-util-v1.md, work/feat-cli-spend-velocity.md, work/feat-cli-pay-behaviour.md, work/ds-cli-eligible-pop.md, work/ds-cli-outcome-90d.md

## Q4
None. The only linked note built on ds-clv-holdout-2021h1 is exp-501-customer-lifetime-value, and no decision note links to it. Several CLV notes, including the dec-clv-ship-ml-v1 and dec-clv-ship-ml-v2 decisions, evaluate on the same holdout by name (clv-oot-2021h1), but those links are not recorded.
Notes: work/ds-clv-holdout-2021h1.md, work/exp-501-customer-lifetime-value.md

## Q5
pbs-kmeans-v1 was replaced by pbs-gmm-v2, then by pbs-gmm-v3, and the decision dec-pbs-gmm-v3-current is in force now. dec-pbs-gmm-v3-current is built on fnd-pbs-five-segments and pbs-gmm-v3.
Notes: work/dec-pbs-gmm-v3-current.md, work/fnd-pbs-five-segments.md, work/pbs-gmm-v3.md