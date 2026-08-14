# Kambaata LLM Cultural Benchmark

**When AI Doesn't Know Kembata: Hallucination, cultural substitution, and uncertainty in four general-purpose language models answering questions about an under-documented Ethiopian culture**

Author: **Behailu Berhanu**  
Version: **1.0 candidate — consistency review pending**  
Benchmark: **77 manually verified questions × 4 models = 308 responses**  
Collection: **10–11 August 2026**

## What this repository contains

This repository is the reproducibility package for the Kambaata LLM Cultural Hallucination Benchmark.

The benchmark evaluates four general-purpose language models on fine-grained Kambaata cultural knowledge across 21 domains. Each response was scored on:

1. Accuracy (0–4)
2. Fabrication (None / Minor / Severe)
3. Narrative Substitution (0–3)
4. Geography Conflation (Y/N)

The accompanying paper describes the methodology, findings, limitations, and implications.

## Repository structure

```text
.
├── README.md
├── CITATION.cff
├── LICENSE-MIT
├── DATA-LICENSE-CC-BY-4.0.md
├── SCORING_RUBRIC.md
├── analysis.py
├── requirements.txt
│
├── data/
│   ├── benchmark_items.csv
│   ├── ground_truth.csv
│   ├── raw_responses.csv
│   └── annotations.csv
│
├── paper/
│   └── when-ai-doesnt-know-kembata.pdf
│
├── results/
│   ├── recomputed_model_summary.csv
│   ├── pairwise_wilcoxon.csv
│   └── audit.json
│
└── archive/
    └── source_workbook_scored.xlsx
```

## Reproduce the main analysis

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python analysis.py
```

The script checks the dataset structure before analysis. It expects exactly 77 items and 308 scored item/model rows, with 77 responses for each model.

## Data provenance

The benchmark item bank was fixed before model querying. Ground truth was documented against the study's documentary source set and community knowledge. Raw model responses are preserved verbatim in `data/raw_responses.csv`; final annotations are in `data/annotations.csv`.

The archived Excel workbook is retained under `archive/` as the source workbook used to construct this release.

## Important limitations

- All prompts were administered in English.
- Each model answered each item once.
- The tested model versions and vendor interfaces are time-specific.
- A single community-member annotator finalized the scores, so inter-annotator reliability could not be calculated.
- The benchmark is a focused cultural knowledge evaluation, not a general ranking of model intelligence or overall factuality.
- Results should not be generalized to all model versions or all under-documented cultures.

## Citation

If you use this benchmark, please cite the paper and the repository release. The `CITATION.cff` file contains machine-readable citation metadata.

## Data and code licensing

The analysis code is released under the MIT License.

The benchmark data are released under CC BY 4.0, subject to applicable third-party rights and model-provider terms. See the data license file for details.

## Contact

**Behailu Berhanu**


> **Release status:** This package is a candidate build. See `CONSISTENCY_AUDIT.md` before publishing or minting a DOI.
