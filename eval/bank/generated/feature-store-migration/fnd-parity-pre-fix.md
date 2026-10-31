---
from: [exp-101]
updated: 2025-11-06
---
# Before fixes, 13 of 214 features disagree between store and legacy, and local-time windows are the main cause
After exp-101 the store and legacy values disagree on 13 features. Nine use month-end local-time windows, and payment lag is off on 3.1 percent of rows.
Working hypothesis: the store runs in UTC and the notebooks in local time, so windows that end near midnight land on different days. Confirmed in exp-102.
Superseded by fnd-parity-post-fix (2026-01-14) once the UTC and util-ratio fixes went in.
