---
updated: 2025-09-02
from: [howto/dedupe-disputes-by-case]
---
# Q: Why does the fraud dashboard show more disputes than cases? A: It counted rows in cards.disputes instead of distinct dispute_case_id.
Each status change writes a row. The 2025 H1 count of 14,920 rows corresponds to 5,740 distinct cases, a ratio of about 2.6.
The dashboard was fixed on 2025-09-02.
