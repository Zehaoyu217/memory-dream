---
from: []
updated: 2025-01-20
---
# ep.assignments: one row per unit per test, hash-based, 4.2M units across 38 tests
Assignment is a hash of the unit id with a per-test salt, so the same unit always gets the same arm within a test.
Covers 2025-01 to 2026-04. Columns: test_id, unit_id, arm, assigned_at, and the assignment filter that was applied.
Owner: experiment-platform group. Read-only for test owners.
