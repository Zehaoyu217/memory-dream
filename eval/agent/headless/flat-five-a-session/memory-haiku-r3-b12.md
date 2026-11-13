## Q1
xs-call-uplift-v1 rests on two dataset notes: `ds-xs-callcentre` (the call-centre contacts joined to offers) and `ds-xs-offer-log`, reached through exp-403-callcentre-naive, feat-xs-call-recent and find-xs-call-overstated. The chain also includes q-xs-propensity, and the note's own text names the naive comparison, recent-call feature and overstated finding, which the graph did not link to notes.
Notes: work/xs-call-uplift-v1.md, work/exp-403-callcentre-naive.md, work/feat-xs-call-recent.md, work/find-xs-call-overstated.md, work/ds-xs-callcentre.md, work/ds-xs-offer-log.md

## Q2
Four decision notes rest on ds-disp-analyst-labels: dec-disp-labels-two-analyst directly, and dec-disp-autoresolve-090, dec-disp-autoresolve-095 and dec-disp-fraud-score-in through the disp-lgbm and dispute-triage notes built on it.
Notes: work/dec-disp-labels-two-analyst.md, work/dec-disp-autoresolve-090.md, work/dec-disp-autoresolve-095.md, work/dec-disp-fraud-score-in.md

## Q3
The line is rs-xgb-v1, then rs-xgb-v2, then rs-xgb-v3, so rs-xgb-v3 is the one in force. It is built directly on exp-308-recovery-scoring and rs-xgb-v2.
Notes: work/rs-xgb-v3.md, work/exp-308-recovery-scoring.md, work/rs-xgb-v2.md

## Q4
clv-bgnbd-v1 rests on two dataset notes, `ds-clv-revenue-monthly` and `ds-clv-cohort-panel`, reached through feat-clv-arpu-v1 and feat-clv-tenure. The note also builds on "the bg/nbd versus gbm accuracy test", which no note in the memory matched, so the chain may be incomplete.
Notes: work/clv-bgnbd-v1.md, work/feat-clv-arpu-v1.md, work/feat-clv-tenure.md, work/ds-clv-revenue-monthly.md, work/ds-clv-cohort-panel.md

## Q5
Two decision notes rest on ds-ed-bureau-join: dec-ed-promote-v3, through ed-gbm-v3 and find-ed-bureau-slope, and dec-ed-gbm-for-watchlist, through ed-logit-v1 and find-ed-gbm-vs-logit.
Notes: work/dec-ed-promote-v3.md, work/dec-ed-gbm-for-watchlist.md