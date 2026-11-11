## Q1
Chloe Martin reports campaign lift as a point estimate with its 95% confidence interval (e.g. "+1.8 pts (95% CI +0.6 to +3.0)") and does not show p-values, because business readers treat "p = 0.04" as proof.
Sources: memory/prefs/chloe-martin-campaign-readout.md

## Q2
She highlights the winning campaign in orange `#E07B24` and greys out all others. She does not use brand blue as the highlight because blue series were read as "baseline" in the Q3 2025 campaign readout. (Brand blue `#1F4E9A` is the team's default for primary series; orange is limited to one highlighted series per chart.)
Sources: memory/prefs/chloe-martin-highlight-orange.md, memory/reporting/chart-style-colour.md

## Q3
From 2026-06-01, any `cli-` model with a PSI above 0.20 on a top-20 feature triggers a drift review. Other models keep the 0.25 trigger. The older 0.25 trigger and the 0.10/0.25 two-tier rule are superseded for this purpose.
Sources: memory/reporting/monthly-review-psi-trigger-v2.md

## Q4
Default rates, PD and roll rates in risk tables are shown to 2 decimals in percent (e.g. 3.84%). Lena Fischer's risk-pack convention matches this, with Gini and KS also to 2 decimals and exposure in $m to 1 decimal. Other retention, share and campaign-response percentages use 1 decimal.
Sources: memory/reporting/rounding-percent.md, memory/prefs/lena-fischer-risk-rounding.md

## Q5
Offer tiers come from the `offers.tier_matrix` table. The credit-line and pricing bands run A to E, with A the highest (the older note calling A the lowest was corrected in 2025-05). The retention tier matrix v3 is a separate set, T0 to T4, by churn decile and value band, in force since 2025-09-01.
Sources: memory/corrections/tier-a-highest.md, memory/retention-offers-roi/ds-ror-tier-matrix.md

## Q6
Use a blended interchange rate of 1.9% of purchase value. The old 2.5% figure was the premium-card rate only, and standard cards sit around 1.6-1.8%.
Sources: memory/corrections/interchange-blended.md

## Q7
No. OOT is a period after the training window that was never used for training, tuning or feature selection. The last months of training data are in-time validation, not OOT. The current split is on observation date, with a six-month gap and a three-month OOT tail.
Sources: memory/corrections/oot-not-training-tail.md, memory/howto/oot-split-by-observation-date.md

## Q8
DPD counts from the payment due date (since 2025-11-01). Day 1 starts the day after the due date, and a payment posted on the due date still counts as current (0 DPD). This was fixed in the `cards.payments_daily` pipeline on 2026-01-15, which shifted Nov-Dec 2025 1-29 bucket counts by one day.
Sources: memory/corrections/dpd-due-date-offbyone.md, memory/corrections/dpd-due-date.md

## Q9
Report uplift only when treatment and control are randomised holdouts, computed as treated response rate minus control response rate in percentage points. A control group that was not randomised is reported as lift (an observational difference), not uplift. Example: Chloe Martin's Oct 2025 CLI report showed 1.8 pp "uplift" that was observational; the randomised uplift was 0.9 pp.
Sources: memory/corrections/uplift-randomised-only.md, memory/glossary/uplift.md (superseded)

## Q10
The dispute-count feature `feat_disp_cnt_90d_v1` read 14 days past the observation date, which was a leak. Restricting it to days on or before observation dropped holdout AUC from 0.79 to 0.72, so it was rebuilt as v2 and v1 was removed from training. The leak scan (`scripts/leak_scan.py`) now fails the build on any such violation.
Sources: memory/qa/dispute-feature-leak.md, memory/howto/leakage-check-post-period.md