## Q1
Chloe Martin wants lift as a point estimate with its 95% confidence interval, e.g. "+1.8 pts (95% CI +0.6 to +3.0)", with cost per response in $ beside it in the same table. She does not show p-values, because business readers take "p = 0.04" as proof.
Sources: memory/prefs/chloe-martin-campaign-readout.md

## Q2
She highlights the winning campaign in orange #E07B24 and greys out all other campaigns (mid-grey). She avoids brand blue because blue series were read as "baseline" in the Q3 2025 campaign readout. Team chart style allows only one orange highlight per chart; primary series are brand blue #1F4E9A.
Sources: memory/prefs/chloe-martin-highlight-orange.md, memory/reporting/chart-style-colour.md

## Q3
The current rule for `cli-` models is a drift review when PSI is above 0.20 on a top-20 feature (effective 2026-06-01; other model families keep 0.25). A later general correction (2026-06-10) sets PSI above 0.10 to investigate and above 0.25 to a retrain review with an OOT check, and does not mention credit-line models, so the two overlap and the 0.20 cli rule is the more specific one to apply.
Sources: memory/reporting/monthly-review-psi-trigger-v2.md, memory/corrections/psi-two-tier-thresholds.md

## Q4
Default rates, PD and roll rates in risk tables are shown to 2 decimals in percent (e.g. 3.84%). Gini and KS are also 2 decimals, and exposure is in $m to 1 decimal. General percentages (retention, share, campaign response) use 1 decimal.
Sources: memory/reporting/rounding-percent.md, memory/prefs/lena-fischer-risk-rounding.md

## Q5
Offer tiers come from the `offers.tier_matrix` table. Credit-line and pricing tiers run A to E, with A the highest (best promotional APRs) and E the lowest; the older glossary saying A was lowest is superseded. Retention offers use a separate matrix (v3, in force since 2025-09-01) with five tiers T0 to T4 by churn decile and value band.
Sources: memory/corrections/tier-a-highest.md, memory/retention-offers-roi/ds-ror-tier-matrix.md

## Q6
Use 1.9% blended interchange for the book. The earlier 2.5% was the premium-card rate only; standard cards sit around 1.6-1.8%. The Q4 2025 finance pack used 2.5% and was restated to 1.9%.
Sources: memory/corrections/interchange-blended.md

## Q7
No. OOT must be a period after the training window that was never used for training, tuning or feature selection. The last months of training data are in-time validation, not OOT. The current split is by observation date with a six-month gap and a three-month OOT tail.
Sources: memory/corrections/oot-not-training-tail.md, memory/howto/oot-split-by-observation-date.md

## Q8
DPD counts from the payment due date. Day 1 starts the day after the due date, and a payment posted on the due date still counts as current (0 DPD). This was fixed in the `cards.payments_daily` pipeline on 2026-01-15; the earlier 2025-11 rule that made the due date day 1 was off by one.
Sources: memory/corrections/dpd-due-date-offbyone.md, memory/corrections/dpd-due-date.md

## Q9
Report it as lift, not uplift. Uplift is reported only on randomised holdouts (treatment and control randomised). Differences from observational campaign data in `marketing.campaign_responses` are called lift. For example, the Oct 2025 CLI report's 1.8 pp "uplift" was observational; the randomised uplift was 0.9 pp.
Sources: memory/corrections/uplift-randomised-only.md, memory/howto/uplift-eval-qini-at-20pct.md

## Q10
The dispute-count feature `feat_disp_cnt_90d_v1` read 14 days past the observation date, a leak that inflated holdout AUC from 0.72 to 0.79. It was rebuilt as v2, which reads only days on or before observation, and v1 was removed from training. The leak scan (`scripts/leak_scan.py`) now fails the build on any such violation.
Sources: memory/qa/dispute-feature-leak.md, memory/howto/leakage-check-post-period.md