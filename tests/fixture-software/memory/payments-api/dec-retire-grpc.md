---
updated: 2026-09-10
---
# The gRPC endpoint of payments-api is retired on 2026-12-15; clients move to HTTP
Decision, 2026-09-10. Two callers remain on gRPC: `orders-service` and `reporting-batch`, 3.2% of traffic in
2026-08. The HTTP API has carried every feature since rel-v3-4-0. Removal PR planned for the 2026-12 release.
Owner Priya Nair; orders-team confirmed their migration for 2026-11-20.
