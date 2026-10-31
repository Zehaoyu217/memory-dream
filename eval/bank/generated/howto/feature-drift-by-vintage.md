---
updated: 2026-02-02
---
# Check feature drift by account vintage before reading a PSI spike as seasonal
Split the PSI computation by vintage: accounts opened in the last 12 months against older accounts. If the spike sits only in new accounts it is a mix change from acquisition. If it also sits in old accounts it is a behaviour or data change.
