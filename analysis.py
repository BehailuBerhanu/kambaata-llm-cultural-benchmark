"""
Reproduce the main descriptive results from the public annotation dataset.

Usage:
    python analysis.py

Requires:
    pandas
    scipy
"""
from pathlib import Path
import pandas as pd
from scipy.stats import wilcoxon

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "annotations.csv"
OUT = ROOT / "results"

df = pd.read_csv(DATA)
models = ["ChatGPT", "Gemini", "Claude", "DeepSeek"]

required = [
    "Item ID", "Model Tested", "Accuracy (0-4)",
    "Fabrication (None/Minor/Severe)",
    "Narrative Substitution (0-3)",
    "Geography Conflation (Y/N)"
]
missing = [c for c in required if c not in df.columns]
if missing:
    raise ValueError(f"Missing required columns: {missing}")

if len(df) != 308:
    raise ValueError(f"Expected 308 scored rows, found {len(df)}.")
if df["Item ID"].nunique() != 77:
    raise ValueError("Expected 77 unique benchmark items.")
if df.duplicated(["Item ID", "Model Tested"]).any():
    raise ValueError("Duplicate item/model rows found.")
for model in models:
    n = (df["Model Tested"] == model).sum()
    if n != 77:
        raise ValueError(f"{model}: expected 77 rows, found {n}.")

df["Any Fabrication"] = df["Fabrication (None/Minor/Severe)"].isin(["Minor", "Severe"])
df["Severe Fabrication"] = df["Fabrication (None/Minor/Severe)"].eq("Severe")
df["Geo Conflation"] = df["Geography Conflation (Y/N)"].eq("Y")

summary = df.groupby("Model Tested").agg(
    responses=("Item ID", "size"),
    mean_accuracy=("Accuracy (0-4)", "mean"),
    sd_accuracy=("Accuracy (0-4)", "std"),
    any_fabrication=("Any Fabrication", "mean"),
    severe_fabrication=("Severe Fabrication", "mean"),
    mean_narrative_substitution=("Narrative Substitution (0-3)", "mean"),
    geography_conflation=("Geo Conflation", "mean")
).reindex(models)

summary["any_fabrication_pct"] = summary["any_fabrication"] * 100
summary["severe_fabrication_pct"] = summary["severe_fabrication"] * 100
summary["geography_conflation_pct"] = summary["geography_conflation"] * 100
summary.to_csv(OUT / "recomputed_model_summary.csv")

rows = []
for i, m1 in enumerate(models):
    for m2 in models[i+1:]:
        a = df[df["Model Tested"] == m1].set_index("Item ID")["Accuracy (0-4)"].sort_index()
        b = df[df["Model Tested"] == m2].set_index("Item ID")["Accuracy (0-4)"].sort_index()
        stat, p = wilcoxon(a, b, zero_method="wilcox", alternative="two-sided")
        rows.append({"model_1": m1, "model_2": m2, "n_pairs": len(a),
                     "wilcoxon_W": stat, "p_raw": p})

pairwise = pd.DataFrame(rows)
# Holm-Bonferroni adjustment
order = pairwise["p_raw"].sort_values().index
m = len(pairwise)
sorted_p = pairwise.loc[order, "p_raw"].to_numpy()
adj = (m - range(m)) * sorted_p
adj = pd.Series(adj, index=order).cummax().clip(upper=1)
pairwise["p_holm"] = adj
pairwise.to_csv(OUT / "pairwise_wilcoxon.csv", index=False)

print(summary.round(4))
print("\nPairwise Wilcoxon:")
print(pairwise.round(6))
