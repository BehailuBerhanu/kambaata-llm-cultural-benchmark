# Consistency Audit — v1.0 Candidate

**Status: NOT YET PUBLICATION-FINAL**

The paper PDF in `paper/when-ai-doesnt-know-kembata.pdf` and the scored workbook in
`archive/source_workbook_scored.xlsx` were checked independently.

## Dataset completeness

- Benchmark items: 77
- Raw responses: 308
- Scored responses: 308
- 77 responses per model
- No duplicate item/model rows
- All four required scoring fields are populated

## Important discrepancy found

The paper reports the following ChatGPT fabrication figures:

- Any fabrication: **57.1%**
- Severe fabrication: **24.7%**

The supplied scored workbook currently contains:

- Any fabrication: **43/77 = 55.8%**
- Severe fabrication: **18/77 = 23.4%**

The workbook therefore does **not** reproduce those two published ChatGPT figures.

The other headline means and several model-level rates do match closely, but the discrepancy affects
the paired fabrication comparisons as well.

### Consequence

Do **not** create the public GitHub release/Zenodo DOI yet.

Before release, choose one authoritative source:

1. Correct the workbook so it contains the exact finalized scores used for the paper; **or**
2. Recompute the paper's affected tables/statistics from the current workbook and issue a corrected paper.

Do not silently edit either source to force a match.

The clean repository structure in this candidate package is ready; only the paper/dataset consistency issue remains.
