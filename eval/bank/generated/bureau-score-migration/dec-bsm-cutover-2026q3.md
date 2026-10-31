---
from: [find-bsm-ks-parity, exp-305, bsm-cutoff-logit]
updated: 2026-08-25
---
# Decision: cut decision models over to v10 on 2026-09-01 with approval cutoff 652 on the v10 scale
Replaces the v8 cutoff of 640 for application decisions from 2026-09-01; exp-305 shows the same 58% approval rate and 4.1% bad rate.
Cutover uses bsm-app-gbm-v10b and bsm-cutoff-logit; the v8 fallback stays in place (dec-bsm-keep-v8-fallback).
Owner for the cutover is Aisha Khan; Sam Lee owns the model.
