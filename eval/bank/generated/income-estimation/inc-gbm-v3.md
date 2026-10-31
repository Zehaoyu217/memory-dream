---
from: [inc-gbm-v2, find-inc-log-target-gain, ds-inc-verified-2026]
updated: 2026-03-04
supersedes: [inc-gbm-v2]
---
# inc-gbm-v3: log-target estimate, MAPE 19% on the verified 2026 sample (n=1,980)
Same features as v2 with a log of verified income as the target instead of raw stated income.
Eval: verified-2026 holdout (n=1,980 of ds-inc-verified-2026), MAPE 19% against 31% for inc-gbm-v2 on the same rows.
Current estimate model; self-employed bias is in find-inc-self-employed-bias.
