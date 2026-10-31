---
updated: 2025-03-18
---
# PSI alert at 0.10 watch and 0.20 retrain (superseded)
Until October 2025 a PSI above 0.20 on any scored feature triggered a retrain request, and 0.10 to 0.20 triggered a watch note. Bins were deciles of the training distribution, computed in `psi_report.py`.
The rule fired on normal Q4 seasonality with no change in KS, so it is superseded by `howto/psi-thresholds`.
