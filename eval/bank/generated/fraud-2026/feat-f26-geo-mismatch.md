---
from: [ds-f26-cnp-txn]
updated: 2026-06-30
---
# feat-f26-geo-mismatch: billing country differs from IP country
Binary flag, 1 when the billing country and the IP-geolocated country differ.
Added in fraud26-gbm-v3; positive rate about 4.8% of CNP traffic.
PSI rose to 0.14 after August 2026 (fraud26-find-geo-drift); monitor.
