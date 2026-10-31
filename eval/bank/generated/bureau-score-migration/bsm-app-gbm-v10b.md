---
from: [bsm-app-gbm-v10a, feat-bsm-score-map-v2, feat-bsm-thin-file-flag]
updated: 2026-06-10
supersedes: [bsm-app-gbm-v10a]
---
# bsm-app-gbm-v10b: isotonic-mapped v10 model, AUC 0.80 and KS 0.37 on bureau-score-migration-oot-2026h1
Retrained on feat-bsm-score-map-v2 and feat-bsm-thin-file-flag with the source flag.
Eval: bureau-score-migration-oot-2026h1 (n=44,800), AUC 0.80, KS 0.37 (exp-306).
Candidate for cutover; cutoff set through bsm-cutoff-logit.
