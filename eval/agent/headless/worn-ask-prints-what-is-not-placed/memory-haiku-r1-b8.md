## Q1
cld-gbm-v3 is in force: cld-gbm-v1 was replaced by cld-gbm-v2, which was replaced by cld-gbm-v3. It builds on cld-gbm-v2 and feat-cld-payment-shock, and through them on cld-gbm-v1, feat-cld-risk-band-v2, feat-cld-util-after-decrease, ds-cld-decrease-cohort and feat-cld-risk-band-v1.
Notes: limit-decrease-policy/cld-gbm-v3.md, limit-decrease-policy/cld-gbm-v2.md, limit-decrease-policy/feat-cld-payment-shock.md, limit-decrease-policy/cld-gbm-v1.md, limit-decrease-policy/feat-cld-risk-band-v2.md, limit-decrease-policy/feat-cld-util-after-decrease.md, limit-decrease-policy/ds-cld-decrease-cohort.md, limit-decrease-policy/feat-cld-risk-band-v1.md

## Q2
The dataset notes behind cc-ft-v1 are ds-cc-qa-labels and ds-cc-taxonomy-v3 directly, and ds-cc-tickets-raw through ds-cc-qa-labels and feat-cc-embed-v1.
Notes: complaint-classification/ds-cc-qa-labels.md, complaint-classification/ds-cc-taxonomy-v3.md, complaint-classification/ds-cc-tickets-raw.md

## Q3
Two decision notes rest on feat-xs-balance-proxy: dec-xs-top-decile-offer, through xs-gbm-v1 and xs-gbm-v2, and dec-xs-retrain-quarterly, through exp-407-oot-2026h1 and xs-gbm-v2.
Notes: cross-sell-savings/dec-xs-top-decile-offer.md, cross-sell-savings/dec-xs-retrain-quarterly.md

## Q4
mrisk-gbm-v3 is in force, replacing mrisk-gbm-v2 and built on it, with mrisk-gbm-v1 underneath. It also builds on exp-507 and feat-mrisk-dispute-ratio, which draws on dispute-triage's ds-disp-merchant-link.
Notes: merchant-risk/mrisk-gbm-v3.md, merchant-risk/mrisk-gbm-v2.md, merchant-risk/mrisk-gbm-v1.md, merchant-risk/exp-507.md, merchant-risk/feat-mrisk-dispute-ratio.md, merchant-risk/feat-mrisk-mcc-base.md, merchant-risk/exp-504.md

## Q5
The dataset notes behind cli-logreg-baseline are ds-cli-eligible-pop and ds-cli-outcome-90d, reached directly or through feat-cli-pay-behaviour, feat-cli-spend-velocity, feat-cli-util-v1 and q-cli-utilization-trigger.
Notes: credit-line-increase/ds-cli-eligible-pop.md, credit-line-increase/ds-cli-outcome-90d.md

## Q6
Two decision notes rest on ds-clv-holdout-2021h1: dec-clv-ship-ml-v1 and dec-clv-ship-ml-v2, both reached through exp-501.
Notes: customer-lifetime-value/dec-clv-ship-ml-v1.md, customer-lifetime-value/dec-clv-ship-ml-v2.md

## Q7
pbs-gmm-v3 is the segment model in force, replacing pbs-gmm-v2, which replaced pbs-kmeans-v1. It builds on pbs-gmm-v2, exp-403 and feat-pbs-timing-v2, and through them on the 12-month payment and statement-balance datasets.
Notes: payment-behavior-segments/pbs-gmm-v3.md, payment-behavior-segments/pbs-gmm-v2.md, payment-behavior-segments/pbs-kmeans-v1.md, payment-behavior-segments/exp-403.md, payment-behavior-segments/feat-pbs-timing-v2.md, payment-behavior-segments/feat-pbs-interest-paid.md

## Q8
The dataset notes behind xs-call-uplift-v1 are ds-xs-callcentre and ds-xs-offer-log, the latter reached through ds-xs-callcentre.
Notes: cross-sell-savings/ds-xs-callcentre.md, cross-sell-savings/ds-xs-offer-log.md

## Q9
Four decision notes rest on ds-disp-analyst-labels: dec-disp-labels-two-analyst directly, and dec-disp-autoresolve-090, dec-disp-autoresolve-095 and dec-disp-fraud-score-in through the models and experiments built on it.
Notes: dispute-triage/dec-disp-labels-two-analyst.md, dispute-triage/dec-disp-autoresolve-090.md, dispute-triage/dec-disp-autoresolve-095.md, dispute-triage/dec-disp-fraud-score-in.md

## Q10
rs-xgb-v3 is in force, replacing rs-xgb-v2, which replaced rs-xgb-v1. It builds on rs-xgb-v2, exp-308 and the recalibration on 2025 agency placements, and through rs-xgb-v2 on rs-xgb-v1, exp-306, feat-rs-contact-attempts and find-rs-region-proxy.
Notes: recovery-scoring/rs-xgb-v3.md, recovery-scoring/rs-xgb-v2.md, recovery-scoring/rs-xgb-v1.md, recovery-scoring/exp-308.md, recovery-scoring/exp-306.md, recovery-scoring/feat-rs-contact-attempts.md