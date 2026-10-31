---
updated: 2026-07-07
supersedes: [reporting/significance-holm-correction]
---
# For more than 10 segments, use Benjamini-Hochberg at FDR 0.05; Holm still applies up to 10
- Test families of up to 10 segments keep the Holm correction at family-wise alpha 0.05.
- Families of more than 10 segments use Benjamini-Hochberg at false-discovery rate 0.05.
- Reason: Holm on 40 segments in the 2026-06 campaign test found nothing, though three segments had stable positive lift in both halves of the test.
- Adjusted values for both methods are kept in the analysis notebook.
