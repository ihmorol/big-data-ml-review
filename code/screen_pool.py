"""Screen OpenAlex pulls down to BD+ML relevant candidates per journal.

Scoring: keyword hits on title (x3) and abstract. A work qualifies when both
an ML keyword and a big-data keyword hit. Surveys flagged separately (AIR
exemplar candidates). Output: results/screen/<journal>.csv sorted by score.
"""
import csv
import json
import re
from pathlib import Path

RAW = Path(__file__).resolve().parents[1] / "results" / "openalex_raw"
OUT = RAW.parent / "screen"
OUT.mkdir(parents=True, exist_ok=True)

ML = [
    "machine learning", "deep learning", "neural network", "large language model",
    " llm", "transformer", "classification", "clustering", "random forest",
    "gradient boosting", " xgboost", "convolutional", "graph neural", "gnn",
    "federated learning", "reinforcement learning", "ensemble learning",
    "anomaly detection", "predictive model", "supervised", "unsupervised",
    "transfer learning", "autoencoder", "attention mechanism", "data mining",
    "artificial intelligence", " ai ", "regression model", "svm", "support vector",
    "naive bayes", "decision tree", "k-means", "recommendation", "forecasting",
    "llms", "generative", "diffusion model", "foundation model",
]
BD = [
    "big data", "large-scale", "large scale", "scalab", "distributed",
    "spark", "hadoop", "streaming", "data stream", "massive", "high-dimensional",
    "high dimensional", "cloud computing", "edge computing", "data lake",
    "parallel", "mapreduce", "data-driven", "internet of things", " iot ",
    "sensor data", "real-time", "realtime", "petabyte", "heterogeneous data",
    "data volume", "volume, velocity", "5v", "hpc", "gpu cluster", "data warehouse",
]
SURVEY = re.compile(r"\b(survey|review|systematic|state of the art|state-of-the-art|taxonomy|landscape)\b", re.I)

def hits(text: str, terms: list[str]) -> int:
    t = text.lower()
    return sum(1 for k in terms if k in t)

for path in sorted(RAW.glob("*.json")):
    works = json.loads(path.read_text(encoding="utf-8"))
    rows = []
    for w in works:
        if w.get("type") not in ("article", "review"):
            continue
        title = w.get("title") or ""
        abstract = w.get("abstract") or ""
        ml = hits(title, ML) * 3 + hits(abstract, ML)
        bd = hits(title, BD) * 3 + hits(abstract, BD)
        if ml == 0 or bd == 0:
            continue
        rows.append({
            "doi": w.get("doi"), "title": title, "date": w.get("date"),
            "type": w.get("type"), "is_oa": w.get("is_oa"),
            "oa_status": w.get("oa_status"), "cited_by": w.get("cited_by"),
            "ml_score": ml, "bd_score": bd,
            "survey": 1 if SURVEY.search(title + " " + abstract[:400]) else 0,
            "authors": "; ".join(w.get("authors") or []),
            "abstract_snippet": abstract[:280],
        })
    rows.sort(key=lambda r: (r["ml_score"] + r["bd_score"], r["cited_by"] or 0), reverse=True)
    with (OUT / f"{path.stem}.csv").open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else ["doi"])
        writer.writeheader()
        writer.writerows(rows)
    surveys = sum(r["survey"] for r in rows)
    oas = sum(1 for r in rows if r["is_oa"])
    print(f"{path.stem}: screened {len(works)} -> {len(rows)} candidates ({oas} OA, {surveys} survey-flagged)")
