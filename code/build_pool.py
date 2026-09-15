"""Build the verified selection manifest for the 20-paper pool + alternates.

Finds each selected work in the OpenAlex pulls by distinctive title fragment,
verifies existence/metadata via Crossref (two-step protocol, step 1), and
writes results/pool_selected.json + results/table1.csv.
Content claims stay abstract/metadata-level per the citation protocol.
"""
import csv
import json
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "results" / "openalex_raw"

# (id, journal_file, title_fragment, theme, role, ml_methods, bd_context)
SELECTION = [
    ("TBD-1", "IEEE_TBD", "PEXP", "Scalable & interpretable ML", "selected", "tree-based parallel model interpretation", "big data; parallel framework"),
    ("TBD-2", "IEEE_TBD", "Blockchain-Empowered Federated Learning", "Federated & privacy-preserving learning", "selected", "federated learning + blockchain incentives/security", "distributed training across parties"),
    ("TBD-3", "IEEE_TBD", "GraphLLM", "LLMs & foundation models", "selected", "LLM for graph reasoning", "graph-structured large data"),
    ("TBD-4", "IEEE_TBD", "Knowledge Aggregation Transformer Network", "Time series & streaming", "selected", "transformer for multivariate time series classification", "high-volume sensor/time-series data"),
    ("TBD-5", "IEEE_TBD", "Enhanced Approaches for Anomaly Detection in Streaming Data", "Security & anomaly detection", "selected", "statistical + ML anomaly detection", "data streams (velocity)"),
    ("BDR-1", "BDR", "Explainable malware detection", "Security & anomaly detection", "selected", "graph reduction + learning, explainable malware detection", "large malware corpora"),
    ("BDR-2", "BDR", "Efficient training: Federated learning cost", "Federated & privacy-preserving learning", "selected", "federated learning training-cost analysis", "distributed/edge training"),
    ("BDR-3", "BDR", "Opinion fraud detection on massive datasets", "Platforms & infrastructure", "selected", "fraud detection ML on Spark", "massive datasets; Spark cluster"),
    ("BDR-4", "BDR", "Heterogeneous Graph-based Risk Assessment for Internet Financial Companies", "Applications & domains", "selected", "heterogeneous graph-based risk assessment", "company big data (explicit in title)"),
    ("BDR-5", "BDR", "Large-scale least squares regression", "Scalable & interpretable ML", "selected", "fast spectral embedding + random Fourier features regression", "large-scale data"),
    ("JoBD-1", "JoBD", "Big Data Analytics in IoT, social media", "Platforms & infrastructure", "selected", "multi-domain BD analytics survey (IoT, social, NLP, security)", "IoT/social-media/NLP/security data"),
    ("JoBD-2", "JoBD", "privacy-enhanced framework for collaborative Big Data analysis in healthcare", "Healthcare applications", "selected", "adaptive privacy-preserving collaborative analytics", "healthcare big data"),
    ("JoBD-3", "JoBD", "Advancing multimodal emotion recognition in big data", "Applications & domains", "selected", "GAN + dynamic prompt engineering, multimodal deep learning", "multimodal big data (explicit in title)"),
    ("JoBD-4", "JoBD", "Cloud based real-time multivariate multi-step prediction of systolic blood pressure", "Healthcare + fog/cloud streaming", "selected", "temporal convolutional network (TCN) multi-step forecasting", "fog/cloud streaming pipeline with Apache Spark (explicit in title)"),
    ("JoBD-5", "JoBD", "Graph neural network approach with spatial structure to anomaly detection", "Security & anomaly detection", "selected", "GNN anomaly detection", "network traffic data"),
    ("AIR-1", "AIR", "Agentic AI: a comprehensive survey", "Agentic AI & RAG", "selected", "agentic AI architectures/applications (survey)", "large-scale generative systems"),
    ("AIR-2", "AIR", "anomaly detection for telecom networks", "Security & anomaly detection", "selected", "AI anomaly detection for telecom (survey)", "telecom network big data"),
    ("AIR-3", "AIR", "From classical machine learning to emerging foundation models", "LLMs & foundation models", "selected", "classical ML to foundation models, multimodal (review)", "multimodal big data"),
    ("AIR-4", "AIR", "generative AI for synthetic data generation", "Data quality & governance", "selected", "generative AI synthetic data (review)", "healthcare data scarcity/privacy"),
    ("AIR-5", "AIR", "deep multivariate time-series models", "Data quality & governance", "selected", "deep multivariate TS models + reproducibility audit", "multivariate time series at scale"),
    ("TBD-A1", "IEEE_TBD", "Vehicle Perception Technologies", "alternate", "alternate", "BD-driven vehicle perception review", "autonomous-driving sensor data"),
    ("TBD-A2", "IEEE_TBD", "Digital Twin Data Management", "alternate", "alternate", "digital-twin data management review", "digital-twin pipelines"),
    ("TBD-A3", "IEEE_TBD", "Ensemble Approaches for Dynamic Data Stream Classification", "alternate", "alternate", "ensemble data-stream classification", "label-scarce streams"),
    ("TBD-A4", "IEEE_TBD", "Fast Linearithmic Graph Clustering", "alternate", "alternate", "linearithmic graph clustering", "big graphs"),
    ("TBD-A5", "IEEE_TBD", "SARF", "alternate", "alternate", "sparsity-aware reconstruction", "large-scale datasets"),
    ("BDR-A1", "BDR", "Deep neural network modeling for financial time series", "alternate", "alternate", "DNN financial time series", "market data"),
    ("BDR-A2", "BDR", "job matching and skill recommendation using transformers", "alternate", "alternate", "transformer recommendation", "O*NET labor data"),
    ("BDR-A3", "BDR", "Scalable QoS-aware cloud service composition", "alternate", "alternate", "model-driven optimization for workflows", "cloud big-data workflows"),
    ("BDR-A4", "BDR", "ImDMI", "alternate", "alternate", "distributed privacy model for publishing", "big data publishing"),
    ("BDR-A5", "BDR", "Hybrid quantum GAN", "alternate", "alternate", "quantum GAN synthetic data", "privacy-embedded generation"),
    ("JoBD-A1", "JoBD", "blockchain framework for reliable fraud detection", "alternate", "alternate", "DL + blockchain fraud detection", "big-data-driven fraud"),
    ("JoBD-A2", "JoBD", "privacy preservation in the internet of vehicles", "alternate", "alternate", "AI privacy preservation survey", "IoV data"),
    ("JoBD-A3", "JoBD", "systematic literature study of machine learning techniques based intrusion", "alternate", "alternate", "ML intrusion-detection survey", "network security data"),
    ("JoBD-A4", "JoBD", "BlueEdge", "alternate", "alternate", "big-data cleaning via mobile edge computing", "edge computing"),
    ("JoBD-A5", "JoBD", "Data science, big data, and machine learning are coming of age", "alternate", "alternate", "field-maturation position paper", "cross-domain"),
    ("JoBD-A6", "JoBD", "renewable energy systems", "alternate", "alternate", "AI/ML for renewable energy systems (review)", "energy-system big data"),
    ("JoBD-A7", "JoBD", "large-scale plant disease detection", "alternate", "alternate", "DL framework for large-scale plant disease detection", "big data analytics (explicit in title)"),
    ("TBD-A6", "IEEE_TBD", "TS-MLLM", "alternate", "alternate", "multimodal LLM for industrial time-series big data", "industrial big data (explicit in title)"),
    ("BDR-A6", "BDR", "Optimization of differential privacy mechanism", "alternate", "alternate", "differential privacy optimization", "big data publishing"),
    ("AIR-A1", "AIR", "Agentic AI systems in the age of generative models", "alternate", "alternate", "agentic AI + cloud scalability", "cloud-scale generative systems"),
    ("AIR-A2", "AIR", "Safeguarding large language models", "alternate", "alternate", "LLM safety survey", "large-scale LLM deployment"),
    ("AIR-A3", "AIR", "Graph neural networks for anomaly detection", "alternate", "alternate", "GNN anomaly detection survey", "dynamic temporal graphs"),
    ("AIR-A4", "AIR", "Synergizing blockchain and AI to fortify IoT security", "alternate", "alternate", "blockchain + AI for IoT security", "IoT big data"),
    ("AIR-A5", "AIR", "Artificial intelligence for weather and climate", "alternate", "alternate", "AI methods/benchmarks for climate", "climate-scale data"),
]


def load(jf):
    return json.loads((RAW / f"{jf}.json").read_text(encoding="utf-8"))


def crossref(doi):
    url = f"https://api.crossref.org/works/{doi}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "bda-review-pool/1.0 (mailto:team8.bda@example.edu)"})
        with urllib.request.urlopen(req, timeout=30) as r:
            m = json.load(r)["message"]
        return {
            "cr_title": (m.get("title") or [""])[0],
            "cr_journal": (m.get("container-title") or [""])[0],
            "cr_year": (m.get("issued", {}).get("date-parts") or [[None]])[0][0],
            "cr_type": m.get("type"),
        }
    except Exception as e:
        return {"cr_title": f"ERROR: {e}", "cr_journal": "", "cr_year": None, "cr_type": ""}


pool, table = [], []
for pid, jf, frag, theme, role, ml, bd in SELECTION:
    works = load(jf)
    m = [w for w in works if frag.lower() in (w["title"] or "").lower()]
    if not m:
        print(f"{pid} NOT FOUND IN PULL: {frag}")
        continue
    w = m[0]
    if len(m) > 1:
        print(f"{pid} AMBIGUOUS ({len(m)} matches): {frag}")
    cr = crossref(w["doi"])
    norm = lambda s: " ".join((s or "").lower().split())
    # IEEE early-access pattern: OpenAlex = online date, Crossref = issue year.
    # Both count as published within 2025-2027; require title identity + both years in period.
    period = {"2025", "2026", "2027"}
    t_ok = norm(frag)[:30] in norm(cr["cr_title"]) or norm(cr["cr_title"])[:30] in norm(w["title"])
    ok = t_ok and str(cr["cr_year"]) in period and w["date"][:4] in period
    rec = {
        "id": pid, "journal_file": jf, "journal": w["journal"], "role": role,
        "theme": theme, "ml_methods": ml, "bd_context": bd,
        "doi": w["doi"], "title": w["title"], "date": w["date"], "year": w["date"][:4],
        "is_oa": w["is_oa"], "oa_status": w["oa_status"], "cited_by": w["cited_by"],
        "authors": w["authors"], "biblio": w["biblio"], "abstract": w["abstract"],
        "crossref": cr, "verified": ok,
    }
    pool.append(rec)
    if role == "selected":
        table.append(rec)
    flag = "OK " if ok else "CHECK"
    print(f"{flag} {pid} [{w['date']}] OA={w['is_oa']} c={w['cited_by']:>3} {w['title'][:65]}")
    time.sleep(0.15)

(ROOT / "results" / "pool_selected.json").write_text(
    json.dumps(pool, ensure_ascii=False, indent=1), encoding="utf-8")

# Article-type classification for the "research papers" requirement audit.
# AIR is a review-oriented journal; its articles are reviews by design.
TYPE_OVERRIDES = {
    "TBD-2": "survey", "JoBD-1": "survey + benchmark",
    "AIR-1": "survey", "AIR-2": "review", "AIR-3": "review",
    "AIR-4": "review", "AIR-5": "survey",
}

with (ROOT / "results" / "table1.csv").open("w", newline="", encoding="utf-8-sig") as f:
    wr = csv.writer(f)
    wr.writerow(["ID", "Authors (first 3)", "Year", "Title", "Journal", "Type", "OA",
                 "Theme", "ML methods (abstract-level)", "Big-data context (abstract-level)",
                 "Cited by (OpenAlex)", "DOI"])
    for r in table:
        au = "; ".join(r["authors"][:3]) + (" et al." if len(r["authors"]) > 3 else "")
        wr.writerow([r["id"], au, r["year"], r["title"], r["journal"],
                     TYPE_OVERRIDES.get(r["id"], "research article"),
                     "yes" if r["is_oa"] else "no (flag: needs access)",
                     r["theme"], r["ml_methods"], r["bd_context"], r["cited_by"], r["doi"]])

sel_ok = sum(1 for r in pool if r["role"] == "selected" and r["verified"])
print(f"\nverified {sel_ok}/20 selected; pool + table1.csv written")
