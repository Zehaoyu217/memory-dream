## Q1
cld-gbm-v1 was superseded by cld-gbm-v2, which was superseded by cld-gbm-v3, the note in force. cld-gbm-v3 is built on cld-gbm-v2 and feat-cld-payment-shock (the payment-shock feature builds on feat-cld-util-after-decrease).
Notes: limit-decrease-policy/cld-gbm-v3.md, limit-decrease-policy/cld-gbm-v2.md, limit-decrease-policy/feat-cld-payment-shock.md

## Q2
cc-ft-v1 rests on three dataset notes directly or through its inputs: ds-cc-qa-labels and ds-cc-taxonomy-v3 directly, and ds-cc-tickets-raw through feat-cc-embed-v1 and ds-cc-qa-labels.
Notes: complaint-classification/cc-ft-v1.md, complaint-classification/ds-cc-qa-labels.md, complaint-classification/ds-cc-taxonomy-v3.md, complaint-classification/ds-cc-tickets-raw.md

## Q3
Two decision notes rest on feat-xs-balance-proxy. dec-xs-top-decile-offer rests on it through xs-gbm-v2, and dec-xs-retrain-quarterly rests on it through exp-407-oot-2026h1 and find-xs-drift-2026.
Notes: cross-sell-savings/dec-xs-top-decile-offer.md, cross-sell-savings/dec-xs-retrain-quarterly.md

## Q4
mrisk-gbm-v1 was superseded by mrisk-gbm-v2, which was superseded by mrisk-gbm-v3, the note in force. mrisk-gbm-v3 is built on mrisk-gbm-v2, exp-507 and feat-mrisk-dispute-ratio.
Notes: merchant-risk/mrisk-gbm-v3.md, merchant-risk/mrisk-gbm-v2.md, merchant-risk/exp-507.md, merchant-risk/feat-mrisk-dispute-ratio.md

## Q5
cli-logreg-baseline rests on two dataset notes: ds-cli-eligible-pop and ds-cli-outcome-90d, both through its feature notes and q-cli-utilization-trigger.
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/ds-cli-eligible-pop.md, credit-line-increase/ds-cli-outcome-90d.md

## Q6
Two decision notes rest on ds-clv-holdout-2021h1: dec-clv-ship-ml-v1 and dec-clv-ship-ml-v2, both through the experiment and model chain (exp-501, clv-ml-v1, clv-ml-v2, exp-505).
Notes: customer-lifetime-value/dec-clv-ship-ml-v1.md, customer-lifetime-value/dec-clv-ship-ml-v2.md

## Q7
pbs-kmeans-v1 was superseded by pbs-gmm-v2, which was superseded by pbs-gmm-v3, the note in force. pbs-gmm-v3 is built on exp-403, feat-pbs-timing-v2 and pbs-gmm-v2.
Notes: payment-behavior-segments/pbs-gmm-v3.md, payment-behavior-segments/exp-403.md, payment-behavior-segments/feat-pbs-timing-v2.md, payment-behavior-segments/pbs-gmm-v2.md

## Q8
xs-call-uplift-v1 rests on two dataset notes: ds-xs-callcentre directly through exp-403-callcentre-naive and feat-xs-call-recent, and ds-xs-offer-log through q-xs-propensity and ds-xs-callcentre.
Notes: cross-sell-savings/ds-xs-callcentre.md, cross-sell-savings/ds-xs-offer-log.md

## Q9
Four decision notes rest on ds-disp-analyst-labels: dec-disp-labels-two-analyst directly, and dec-disp-autoresolve-090, dec-disp-autoresolve-095 and dec-disp-fraud-score-in through the model and experiment chain.
Notes: dispute-triage/dec-disp-labels-two-analyst.md, dispute-triage/dec-disp-autoresolve-090.md, dispute-triage/dec-disp-autoresolve-095.md, dispute-triage/dec-disp-fraud-score-in.md

## Q10
rs-xgb-v1 was superseded by rs-xgb-v2, which was superseded by rs-xgb-v3, the note in force. rs-xgb-v3 is built on rs-xgb-v2 and exp-308.
Notes: recovery-scoring/rs-xgb-v3.md, recovery-scoring/rs-xgb-v2.md, recovery-scoring/exp-308.md