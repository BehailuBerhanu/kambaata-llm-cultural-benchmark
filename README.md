# Kambaata LLM Cultural Hallucination Benchmark — Reproducibility Package v0.1

Author: Behailu Berhanu
Study: *When AI Doesn't Know Kembata*
Benchmark: 77 manually verified questions × 4 models = 308 raw responses

## What is included

- `benchmark_items.csv` — the 77-item Item Bank extracted from the original workbook.
- `raw_responses_and_existing_annotations.csv` — all 308 raw response rows currently present in the source workbook, plus whatever annotations are actually present there.
- `annotation_template.csv` — a clean scoring sheet matching the published rubric.
- `SCORING_RUBRIC.md` — scoring definitions used by the paper.
- `analysis.py` — reproducible descriptive analysis that refuses to run if final annotations are missing.
- `source_audit.json` — machine-readable audit of what was actually present in the source workbook.
- `source_workbook_original.xlsx` — the original workbook used as the extraction source.

## Critical reproducibility note

The current published paper states that all 308 responses were human-finalized and that the complete benchmark workbook contains all four finalized scores for all 308 rows.

The workbook currently available in this package contains all 308 raw responses, but only **2 of the 308 rows have populated scoring fields** in the source file. Therefore this package **does not pretend that the incomplete workbook is the final scored dataset**.

Before public release, replace the annotation data with the actual final human-finalized 308-row scoring workbook and save it as:

`annotation_final.csv`

Then run:

`python analysis.py`

The script checks that there are exactly 308 rows and exactly 77 rows for each of ChatGPT, Gemini, Claude, and DeepSeek. It will stop rather than silently filling missing values.

## Study configuration

Models:
- OpenAI — GPT-5.6 Luna
- Google — Gemini 3.6 Flash
- Anthropic — Claude Sonnet 5
- DeepSeek — DeepSeek-V3

Collection:
- 10–11 August 2026
- English prompts
- vendor-default sampling
- one response per item/model
- no few-shot examples
- no additional system instructions

## Dataset structure

Each benchmark item contains a question, domain, fixed ground truth, source, and page reference. Each model response is associated with an item ID and model. The published scoring dimensions are Accuracy, Fabrication, Narrative Substitution, and Geography Conflation.

## Reproducibility principle

Never reconstruct row-level annotations from aggregate percentages in the paper. The final row-level scores must come from the actual human-finalized scoring workbook.
