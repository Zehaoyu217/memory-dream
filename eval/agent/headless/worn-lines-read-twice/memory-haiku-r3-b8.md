## Q1
cld-gbm-v3 is in force at the end of the cld-gbm-v1 → v2 → v3 line. It is built on cld-gbm-v2 and feat-cld-payment-shock.
Notes: limit-decrease-policy/cld-gbm-v3.md, limit-decrease-policy/cld-gbm-v2.md, limit-decrease-policy/feat-cld-payment-shock.md

## Q2
cc-ft-v1 rests on three dataset notes directly (ds-cc-qa-labels, ds-cc-taxonomy-v3) and on ds-cc-tickets-raw through feat-cc-embed-v1.
Notes: complaint-classification/ds-cc-qa-labels.md, complaint-classification/ds-cc-taxonomy-v3.md, complaint-classification/ds-cc-tickets-raw.md

## Q3
Two decision notes rest on feat-xs-balance-proxy: dec-xs-top-decile-offer (through xs-gbm-v1 and xs-gbm-v2) and dec-xs-retrain-quarterly (through exp-407-oot-2026h1 and find-xs-drift-2026). The ask output also flagged dec-xs-retrain-quarterly as possibly resting on it through an unplaced link, so treat that chain as inferred.
Notes: cross-sell-savings/dec-xs-top-decile-offer.md, cross-sell-savings/dec-xs-retrain-quarterly.md

## Q4
mrisk-gbm-v3 is in force at the end of the mrisk-gbm-v1 → v2 → v3 line. It is built on exp-507, feat-mrisk-dispute-ratio (borrowed from dispute-triage) and mrisk-gbm-v2.
Notes: merchant-risk/mrisk-gbm-v3.md, merchant-risk/exp-507.md, merchant-risk/feat-mrisk-dispute-ratio.md, merchant-risk/mrisk-gbm-v2.md

## Q5
cli-logreg-baseline rests on two dataset notes: ds-cli-eligible-pop (directly through feat-cli-pay-behaviour and feat-cli-util-v1, and through q-cli-utilization-trigger) and ds-cli-outcome-90d (directly through feat-cli-spend-velocity).
Notes: credit-line-increase/ds-cli-eligible-pop.md, credit-line-increase/ds-cli-outcome-90d.md

## Q6
Two decision notes rest on ds-clv-holdout-2021h1: dec-clv-ship-ml-v1 and dec-clv-ship-ml-v2, both reached through exp-501 and the model chain.
Notes: customer-lifetime-value/dec-clv-ship-ml-v1.md, customer-lifetime-value/dec-clv-ship-ml-v2.md

## Q7
pbs-gmm-v3 is in force at the end of the pbs-kmeans-v1 → pbs-gmm-v2 → pbs-gmm-v3 line. It is built on exp-403, feat-pbs-timing-v2 and pbs-gmm-v2.
Notes: payment-behavior-segments/pbs-gmm-v3.md, payment-behavior-segments/exp-403.md, payment-behavior-segments/feat-pbs-timing-v2.md, payment-behavior-segments/pbs-gmm-v2.md

## Q8
xs-call-uplift-v1 rests on two dataset notes: ds-xs-callcentre (directly through exp-403-callcentre-naive and feat-xs-call-recent) and ds-xs-offer-log (through q-xs-propensity and the offer-log chain).
Notes: cross-sell-savings/ds-xs-callcentre.md, cross-sell-savings/ds-xs-offer-log.md

## Q9
Four decision notes rest on ds-disp-analyst-labels: dec-disp-labels-two-analyst (directly), dec-disp-autoresolve-090 and dec-disp-autoresolve-095 (through exp-304, exp-305 and disp-lgbm-v2), and dec-disp-fraud-score-in (through exp-306 and exp-307). I only saw the first 22 entries of the ask output, but these four decisions all appear in its chains.
Notes: dispute-triage/dec-disp-labels-two-analyst.md, dispute-triage/dec-disp-autoresolve-090.md, dispute-triage/dec-disp-autoresolve-095.md, dispute-triage/dec-disp-fraud-score-in.md

## Q10
rs-xgb-v3 is in force at the end of the rs-xgb-v1 → v2 → v3 line. It is built on rs-xgb-v2 and exp-308.
Notes: recovery-scoring/rs-xgb-v3.md, recovery-scoring/rs-xgb-v2.md, recovery-scoring/exp-308.md