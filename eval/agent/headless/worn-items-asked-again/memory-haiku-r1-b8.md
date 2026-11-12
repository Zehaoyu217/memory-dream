## Q1
cld-gbm-v3 is the model in force at the end of the cld-gbm-v1 line (v1 was replaced by v2, which was replaced by v3). It is built on cld-gbm-v2 and feat-cld-payment-shock.
Notes: limit-decrease-policy/cld-gbm-v3.md, limit-decrease-policy/cld-gbm-v2.md, limit-decrease-policy/feat-cld-payment-shock.md

## Q2
cc-ft-v1 rests on three dataset notes: ds-cc-qa-labels and ds-cc-taxonomy-v3 directly, and ds-cc-tickets-raw through feat-cc-embed-v1.
Notes: complaint-classification/ds-cc-qa-labels.md, complaint-classification/ds-cc-taxonomy-v3.md, complaint-classification/ds-cc-tickets-raw.md

## Q3
Two decisions rest on feat-xs-balance-proxy, both through xs-gbm-v1 and xs-gbm-v2: dec-xs-top-decile-offer and dec-xs-retrain-quarterly.
Notes: cross-sell-savings/dec-xs-top-decile-offer.md, cross-sell-savings/dec-xs-retrain-quarterly.md

## Q4
mrisk-gbm-v3 is the model in force at the end of the mrisk-gbm-v1 line (v1 was replaced by v2, which was replaced by v3). It is built on exp-507, feat-mrisk-dispute-ratio and mrisk-gbm-v2.
Notes: merchant-risk/mrisk-gbm-v3.md, merchant-risk/exp-507.md, merchant-risk/feat-mrisk-dispute-ratio.md, merchant-risk/mrisk-gbm-v2.md

## Q5
cli-logreg-baseline rests on two dataset notes: ds-cli-eligible-pop (via feat-cli-pay-behaviour and feat-cli-util-v1) and ds-cli-outcome-90d (via feat-cli-spend-velocity).
Notes: credit-line-increase/ds-cli-eligible-pop.md, credit-line-increase/ds-cli-outcome-90d.md

## Q6
Two decisions rest on ds-clv-holdout-2021h1: dec-clv-ship-ml-v1 and dec-clv-ship-ml-v2, both through exp-501 and exp-505.
Notes: customer-lifetime-value/dec-clv-ship-ml-v1.md, customer-lifetime-value/dec-clv-ship-ml-v2.md

## Q7
pbs-gmm-v3 is the segment model in force at the end of the pbs-kmeans-v1 line (v1 was replaced by pbs-gmm-v2, which was replaced by pbs-gmm-v3). It is built on exp-403, feat-pbs-timing-v2 and pbs-gmm-v2.
Notes: payment-behavior-segments/pbs-gmm-v3.md, payment-behavior-segments/exp-403.md, payment-behavior-segments/feat-pbs-timing-v2.md, payment-behavior-segments/pbs-gmm-v2.md

## Q8
xs-call-uplift-v1 rests on two dataset notes: ds-xs-callcentre directly (via exp-403-callcentre-naive and feat-xs-call-recent), and ds-xs-offer-log through it.
Notes: cross-sell-savings/ds-xs-callcentre.md, cross-sell-savings/ds-xs-offer-log.md

## Q9
Four decisions rest on ds-disp-analyst-labels: dec-disp-labels-two-analyst directly, and dec-disp-autoresolve-090, dec-disp-autoresolve-095 and dec-disp-fraud-score-in through other notes.
Notes: dispute-triage/dec-disp-labels-two-analyst.md, dispute-triage/dec-disp-autoresolve-090.md, dispute-triage/dec-disp-autoresolve-095.md, dispute-triage/dec-disp-fraud-score-in.md

## Q10
rs-xgb-v3 is the model in force at the end of the rs-xgb-v1 line (v1 was replaced by v2, which was replaced by v3). It is built on exp-308 and rs-xgb-v2.
Notes: recovery-scoring/rs-xgb-v3.md, recovery-scoring/exp-308.md, recovery-scoring/rs-xgb-v2.md