"""
Kambaata LLM Cultural Hallucination Benchmark
Reproducible descriptive analysis.

Input:
  annotation_final.csv with one row per item/model and the columns:
  Model, Accuracy_0_4, Fabrication_None_Minor_Severe,
  Narrative_Substitution_0_3, Geography_Conflation_Y_N

This script deliberately does not invent missing scores.
"""
import pandas as pd

MODELS = ["ChatGPT", "Gemini", "Claude", "DeepSeek"]

df = pd.read_csv("annotation_final.csv")

required = [
    "Item ID", "Model", "Accuracy_0_4",
    "Fabrication_None_Minor_Severe",
    "Narrative_Substitution_0_3",
    "Geography_Conflation_Y_N"
]
missing = [c for c in required if c not in df.columns]
if missing:
    raise ValueError(f"Missing columns: {missing}")

if df[required].isna().any().any():
    raise ValueError("Missing final annotations detected. Fill annotation_final.csv before analysis.")

# Basic checks
if len(df) != 308:
    raise ValueError(f"Expected 308 scored rows, found {len(df)}.")
counts = df.groupby("Model").size()
for m in MODELS:
    if counts.get(m, 0) != 77:
        raise ValueError(f"{m}: expected 77 rows, found {counts.get(m, 0)}.")

# Model summary
df["Any_Fabrication"] = df["Fabrication_None_Minor_Severe"].isin(["Minor", "Severe"])
df["Severe_Fabrication"] = df["Fabrication_None_Minor_Severe"].eq("Severe")
df["Geography_Conflation"] = df["Geography_Conflation_Y_N"].eq("Y")

summary = df.groupby("Model").agg(
    responses=("Item ID", "size"),
    mean_accuracy=("Accuracy_0_4", "mean"),
    sd_accuracy=("Accuracy_0_4", "std"),
    any_fabrication=("Any_Fabrication", "mean"),
    severe_fabrication=("Severe_Fabrication", "mean"),
    mean_narrative_substitution=("Narrative_Substitution_0_3", "mean"),
    geography_conflation=("Geography_Conflation", "mean"),
).reindex(MODELS)

summary["any_fabrication_pct"] = 100 * summary["any_fabrication"]
summary["severe_fabrication_pct"] = 100 * summary["severe_fabrication"]
summary["geography_conflation_pct"] = 100 * summary["geography_conflation"]

summary.to_csv("model_summary_recomputed.csv")
print(summary.round(4))
