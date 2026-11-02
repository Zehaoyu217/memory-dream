---
from: [bug-double-charge, lib-retry-v1]
updated: 2026-07-31
---
# Fixed-delay retries amplified load 2.4 times for nine minutes on 2026-07-30; timeouts rose from 0.3% to 7.9%
During the failover window every client retried after exactly 500 ms (lib-retry-v1), so `acquirer-gateway` saw
2.4 times its normal request rate from 09:12 to 09:21 and its timeouts rose from 0.3% to 7.9%. Jittered exponential
backoff in a replay cut the peak to 1.3 times (2026-07-31, `load/replay-0730`). Owner Priya Nair.
