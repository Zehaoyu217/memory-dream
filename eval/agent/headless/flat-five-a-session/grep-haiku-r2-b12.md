## Q1
xs-call-uplift-v1 builds on the naive call-effect comparison (exp-403-callcentre-naive), the recent-call feature (feat-xs-call-recent) and the overstated call-effect finding (find-xs-call-overstated). Those trace back to the call-centre dataset (ds-xs-callcentre), then the offer log (ds-xs-offer-log), then the root question q-xs-propensity.

Notes: work/xs-call-uplift-v1.md, work/exp-403-callcentre-naive.md, work/feat-xs-call-recent.md, work/find-xs-call-overstated.md, work/ds-xs-callcentre.md, work/ds-xs-offer-log.md, work/q-xs-propensity.md

## Q2
Decisions resting on ds-disp-analyst-labels are dec-disp-labels-two-analyst (direct), dec-disp-autoresolve-090, dec-disp-autoresolve-095 and dec-disp-fraud-score-in, which rest on it through the dispute chain. I did not check dec-lbl-friendly-fraud or dec-cc-drop-dispute-v1 against the dispute chain, so they are not in this list.

Notes: work/ds-disp-analyst-labels.md, work/dec-disp-labels-two-analyst.md, work/dec-disp-autoresolve-090.md, work/dec-disp-autoresolve-095.md, work/dec-disp-fraud-score-in.md, work/ds-disp-disputes.md

## Q3
The rs-xgb-v1 line is rs-xgb-v1, superseded by rs-xgb-v2, superseded by rs-xgb-v3. The note in force is rs-xgb-v3, and no v4 exists. Its explicit build-on is exp-308-recovery-scoring, which I did not trace further back.

Notes: work/rs-xgb-v1.md, work/rs-xgb-v2.md, work/rs-xgb-v3.md, work/dec-rs-promote-v3.md

## Q4
clv-bgnbd-v1 builds on the BG/NBD versus GBM accuracy test, which is exp-501-customer-lifetime-value (22.6% vs 18.4% MAPE). That experiment rests on the 2021 H1 holdout (ds-clv-holdout-2021h1), and the holdout traces to the origination cohort panel (ds-clv-cohort-panel). The six-month average revenue feature is not traced to a dataset root.

Notes: work/clv-bgnbd-v1.md, work/exp-501-customer-lifetime-value.md, work/ds-clv-holdout-2021h1.md, work/ds-clv-cohort-panel.md, work/feat-clv-tenure.md

## Q5
Only dec-ed-promote-v3 rests on ds-ed-bureau-join. The chain runs ds-ed-bureau-join, then ed-logit-v1 and feat-ed-bureau-slope-v1, then ed-gbm-v3, then dec-ed-promote-v3. dec-ed-gbm-for-watchlist is excluded because it is not bureau-linked.

Notes: work/ds-ed-bureau-join.md, work/ed-logit-v1.md, work/feat-ed-bureau-slope-v1.md, work/ed-gbm-v3.md, work/dec-ed-promote-v3.md