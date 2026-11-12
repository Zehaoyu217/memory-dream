## Q1
cld-gbm-v3 is in force; it replaced cld-gbm-v2, which had replaced cld-gbm-v1. It is built directly on feat-cld-payment-shock and cld-gbm-v2.
Notes: limit-decrease-policy/cld-gbm-v3.md, limit-decrease-policy/feat-cld-payment-shock.md, limit-decrease-policy/cld-gbm-v2.md

## Q2
cc-ft-v1 rests on three dataset notes: ds-cc-taxonomy-v3 directly, and ds-cc-qa-labels and feat-cc-embed-v1 each trace back to ds-cc-tickets-raw. So the dataset notes are ds-cc-tickets-raw, ds-cc-qa-labels and ds-cc-taxonomy-v3.
Notes: complaint-classification/ds-cc-tickets-raw.md, complaint-classification/ds-cc-qa-labels.md, complaint-classification/ds-cc-taxonomy-v3.md

## Q3
Two decisions rest on feat-xs-balance-proxy: dec-xs-top-decile-offer, via xs-gbm-v2 (which uses feat-xs-payroll-flag-v2, built on the balance proxy), and dec-xs-retrain-quarterly, via exp-407, which is built on xs-gbm-v2. dec-xs-call-low-deciles does not trace back to the balance proxy.
Notes: cross-sell-savings/dec-xs-top-decile-offer.md, cross-sell-savings/dec-xs-retrain-quarterly.md

## Q4
mrisk-gbm-v3 is in force; it replaced mrisk-gbm-v2, which had replaced mrisk-gbm-v1. It is built directly on mrisk-gbm-v2, feat-mrisk-dispute-ratio and exp-507.
Notes: merchant-risk/mrisk-gbm-v3.md, merchant-risk/mrisk-gbm-v2.md, merchant-risk/feat-mrisk-dispute-ratio.md, merchant-risk/exp-507.md

## Q5
cli-logreg-baseline traces back to a single dataset root, ds-cli-eligible-pop. It also rests on ds-cli-outcome-90d, which comes from ds-cli-eligible-pop and feeds feat-cli-spend-velocity.
Notes: credit-line-increase/ds-cli-eligible-pop.md, credit-line-increase/ds-cli-outcome-90d.md

## Q6
Two decisions rest on ds-clv-holdout-2021h1: dec-clv-ship-ml-v1, via exp-501, clv-ml-v1 and exp-503; and dec-clv-ship-ml-v2, via clv-ml-v2, which is built on clv-ml-v1. dec-clv-include-losses and dec-clv-discount-rate do not trace back to the holdout.
Notes: customer-lifetime-value/dec-clv-ship-ml-v1.md, customer-lifetime-value/dec-clv-ship-ml-v2.md

## Q7
pbs-gmm-v3 is in force; it replaced pbs-gmm-v2, which had replaced pbs-kmeans-v1. It is built directly on pbs-gmm-v2, feat-pbs-timing-v2 and exp-403.
Notes: payment-behavior-segments/pbs-gmm-v3.md, payment-behavior-segments/pbs-gmm-v2.md, payment-behavior-segments/feat-pbs-timing-v2.md, payment-behavior-segments/exp-403.md

## Q8
xs-call-uplift-v1 rests on two dataset notes: ds-xs-callcentre, which feeds feat-xs-call-recent and exp-403, and ds-xs-offer-log, which is the upstream source of ds-xs-callcentre.
Notes: cross-sell-savings/ds-xs-callcentre.md, cross-sell-savings/ds-xs-offer-log.md

## Q9
Four decisions rest on ds-disp-analyst-labels: dec-disp-labels-two-analyst directly; dec-disp-autoresolve-090 and dec-disp-autoresolve-095 via the exp-301 to exp-305 chain and disp-lgbm-v2; and dec-disp-fraud-score-in via exp-306 and exp-307.
Notes: dispute-triage/dec-disp-labels-two-analyst.md, dispute-triage/dec-disp-autoresolve-090.md, dispute-triage/dec-disp-autoresolve-095.md, dispute-triage/dec-disp-fraud-score-in.md

## Q10
rs-xgb-v3 is in force; it replaced rs-xgb-v2, which had replaced rs-xgb-v1. It is built directly on rs-xgb-v2 and exp-308.
Notes: recovery-scoring/rs-xgb-v3.md, recovery-scoring/rs-xgb-v2.md, recovery-scoring/exp-308.md