# Figure data sources — traceability table

Every plotted element in `fig1`–`fig4` maps to a value, a paper ID, and the
source note it came from. Figures use the **manuscript citation numbers**
(`[1]`–`[20]` from `notes/writing-plan.md` §3.2), not the internal pool IDs
(TBD-x / AIR-x), because the manuscript cites papers by bracket number.

No value below is invented: each is either an exact reported number from a
source note, a threshold value quoted verbatim from an abstract, or a
**curated design coordinate** (a methodological judgement about the corpus,
marked as such) that is documented here so it is auditable.

---

## Citation-number ↔ pool-ID key (from `notes/writing-plan.md` §3.2)

| Cite | Pool ID | Short ref |
|---|---|---|
| [1] | TBD-4 | Xiao et al., KATN, IEEE TBD 2025 |
| [2] | TBD-5 | Gunbilek et al., streaming anomaly detection, IEEE TBD 2026 |
| [3] | JoBD-5 | Zhang et al., graph GNN anomaly detection, JoBD 2025 |
| [4] | BDR-5 | Li & Liu, large-scale least squares, BDR 2026 |
| [5] | TBD-1 | Jiang et al., PEXP, IEEE TBD 2026 |
| [6] | AIR-3 | Muneer et al., multimodal cancer FMs, AIR 2026 |
| [7] | BDR-2 | Teixeira et al., FL cost analysis, BDR 2025 |
| [8] | BDR-3 | Ghodsi & Moeini, opinion fraud by Spark, BDR 2026 |
| [9] | JoBD-4 | Saleh et al., cloud real-time SBP/HR TCN+Spark, JoBD 2025 |
| [10] | BDR-1 | Mohammadian et al., explainable malware detection, BDR 2025 |
| [11] | AIR-2 | Edozie et al., telecom anomaly detection, AIR 2025 |
| [12] | BDR-4 | Liu et al., heterogeneous graph risk assessment, BDR 2026 |
| [13] | JoBD-1 | Elfouly et al., plant disease detection, JoBD 2025 |
| [14] | JoBD-3 | Wafa et al., multimodal emotion recognition, JoBD 2025 |
| [15] | TBD-2 | Wang et al., TS-MLLM, IEEE TBD 2026 |
| [16] | TBD-3 | Chai et al., GraphLLM, IEEE TBD 2025 |
| [17] | AIR-1 | Abou Ali et al., Agentic AI survey, AIR 2025 |
| [18] | JoBD-2 | Haripriya et al., privacy-enhanced FL, JoBD 2025 |
| [19] | AIR-4 | Waseem et al., generative AI synthetic data, AIR 2025 |
| [20] | AIR-5 | Vats et al., deep MTS survey + reproducibility audit, AIR 2026 |

---

## Fig. 1 — Corpus landscape (`fig1_corpus_landscape`)

**Structure.** 20 points, one per paper, positioned on two curated axes:
x = data scale/kind (6 ordered categories), y = binding constraint (6 ordered
categories). Colour = journal; marker shape = original research vs review.

**Point-level data.** The coordinates are **curated design positions**
(methodological judgements derived from the source notes), not measured
quantities; each judgement is justified by the note evidence it rests on.
The four ground-truth attributes (journal, article type, branch, and the
evidence tier) are exact; the two axis positions are interpretive.

| Plot element | Curated axis value | Paper ID | Source note | Evidence for the axis placement |
|---|---|---|---|---|
| point [1] | x=Moderate/single-GPU, y=None | TBD-4 | `sources/TBD-4_*.md` | UEA archive (13 datasets), rank protocol; no platform named — "moderate" scale |
| point [2] | x=Streaming velocity, y=Platform/streaming | TBD-5 | `sources/TBD-5_*.md` | "online, no offline retraining" on three streamed datasets — velocity is the driver |
| point [3] | x=Large-scale framing, y=Compute/represent. | JoBD-5 | `sources/JoBD-5_*.md` | ~1.25–3.12 M records; Poincaré-ball embedding overhead is the admitted bottleneck |
| point [4] | x=Large-scale framing, y=Compute/represent. | BDR-5 | `sources/BDR-5_*.md` | title: "Large-scale least squares … fast spectral embedding + random Fourier features" (title-level only) |
| point [5] | x=Large-scale framing, y=None | TBD-1 | `sources/TBD-1_*.md` | abstract: "large-scale datasets"; explainer cost; no platform/dataset named |
| point [6] | x=Curated benchmarks, y=None | AIR-3 | `sources/AIR-3_*.md` | secondary PRISMA review of 54 studies; no primary data |
| point [7] | x=Institution/distributed, y=Privacy | BDR-2 | `sources/BDR-2_*.md` | federated training across 6G devices; cost = time/communication/energy |
| point [8] | x=Distributed platform, y=Platform/streaming | BDR-3 | `sources/BDR-3_*.md` | title: "…on massive datasets by spark" — cluster engine (title-level only) |
| point [9] | x=Streaming velocity, y=Platform/streaming | JoBD-4 | `sources/JoBD-4_*.md` | Kafka → Spark Streaming → fog/cloud tiers; sliding-window forecasting |
| point [10] | x=Large-scale framing, y=Explainability | BDR-1 | `sources/BDR-1_*.md` | "sheer size and complexity of these graph representations"; GNNExplainer subgraphs |
| point [11] | x=Curated benchmarks, y=Reproducibility | AIR-2 | `sources/AIR-2_*.md` | review; "No datasets were generated or analysed"; reports unattributed accuracy ranges |
| point [12] | x=Large-scale framing, y=None | BDR-4 | `sources/BDR-4_*.md` | "Company Big Data" heterogeneous graph; abstract not indexed (title-level only) |
| point [13] | x=Moderate/single-GPU, y=None | JoBD-1 | `sources/JoBD-1_*.md` | 30,000 images on a single Kaggle GPU, no Spark/Hadoop — C-07 |
| point [14] | x=Moderate/single-GPU, y=Compute/represent. | JoBD-3 | `sources/JoBD-3_*.md` | ~25k utterances, ONNX Runtime; model complexity vs edge deployment |
| point [15] | x=Moderate/single-GPU, y=None | TBD-2 | `sources/TBD-2_*.md` | "multiple industrial benchmarks", no scale named (abstract-only) |
| point [16] | x=Moderate/single-GPU, y=None | TBD-3 | `sources/TBD-3_*.md` | four unnamed graph-reasoning tasks; no graph size named |
| point [17] | x=Curated benchmarks, y=None | AIR-1 | `sources/AIR-1_*.md` | conceptual survey of 90 studies; no datasets or benchmarks |
| point [18] | x=Institution/distributed, y=Privacy | JoBD-2 | `sources/JoBD-2_*.md` | 10 simulated non-IID clients; DP/privacy–utility trade-off table |
| point [19] | x=Curated benchmarks, y=Privacy | AIR-4 | `sources/AIR-4_*.md` | structured survey; "No datasets were generated"; privacy/governance focus |
| point [20] | x=Curated benchmarks, y=Reproducibility | AIR-5 | `sources/AIR-5_*.md` | empirical reproducibility audit of 8 codebases — the only audit |

---

## Fig. 2 — Taxonomy (`fig2_taxonomy`)

**Structure.** Branch boxes B1–B5 with the exact paper→branch assignment from
`trackers/paper-tracker.md` ("What the 20 papers cover" / branch map), plus the
documented empty cells. Labels are citation numbers.

| Plot element | Value | Paper ID(s) | Source note / doc |
|---|---|---|---|
| B1 "Scalable & interpretable methods" (5 papers) | [1],[2],[3],[4],[5] | TBD-4, TBD-5, JoBD-5, BDR-5, TBD-1 | tracker branch map B1; `notes/thesis-and-structure.md` §6.3 |
| B2 "Platforms, pipelines & infrastructure" (3) | [7],[8],[9] | BDR-2, BDR-3, JoBD-4 | tracker branch map B2 |
| B3 "Applications & domains" (5) | [10],[11],[12],[13],[14] | BDR-1, AIR-2, BDR-4, JoBD-1, JoBD-3 | tracker branch map B3 |
| B4 "Foundation models & LLMs" (4) | [6],[15],[16],[17] | AIR-3, TBD-2, TBD-3, AIR-1 | tracker branch map B4 |
| B5 "Privacy, governance & evaluation" (3) | [18],[19],[20] | JoBD-2, AIR-4, AIR-5 | tracker branch map B5 |
| Empty cells (findings) | no RL-at-scale; no purely theoretical; no 2027 item | corpus (all 20) | tracker "Empty cells"; R2 C-21 |

Total = 5+3+5+4+3 = **20** (each paper placed exactly once).

---

## Fig. 3 — Reported-result anchors (`fig3_evidence_anchors`)

**Panel (a): classification / detection anchors** (percent; higher is better).

| Plot element | Value (%) | Paper ID | Source note | Exact source line |
|---|---|---|---|---|
| [14] IEMOCAP acc. | 99.82 | JoBD-3 | `sources/JoBD-3_*.md` | "**test 99.82%**" (Table 4, p.43) — flagged anomalously high (C-09) |
| [14] MELD acc. | 99.81 | JoBD-3 | `sources/JoBD-3_*.md` | "**test 99.81%**" (Table 5, p.45) |
| [3] CampusNet F1 | 99.13 | JoBD-5 | `sources/JoBD-5_*.md` | "CampusNet F1 **0.9913**" (Table 5, p.17) |
| [13] 12-class acc. | 97.33 | JoBD-1 | `sources/JoBD-1_*.md` | "**97.33% accuracy** … after 26 epochs" (p.3, Tables 6–7) |
| [18] adaptive agg. acc. | 96.30 | JoBD-2 | `sources/JoBD-2_*.md` | "up to **96.3% accuracy**" (abstract, p.1) |
| [18] centralised+DP (σ²=1.0) | 94.50 | JoBD-2 | `sources/JoBD-2_*.md` | "σ²=1.0 → **94.5%** / ε=1.0" (Table 11, p.39) |
| [2] ECG GSTrees >94% | 94.00 | TBD-5 | `sources/TBD-5_*.md` | "consistently achieving **over 94%**" (abstract) — threshold value |
| [2] fraud ROC-AUC >94% | 94.00 | TBD-5 | `sources/TBD-5_*.md` | "ROC-AUC of **over 94%**" (abstract) — threshold value |
| [3] UNSW F1 | 93.41 | JoBD-5 | `sources/JoBD-5_*.md` | "UNSW F1 **0.9341**" (Table 5, p.17) |
| [2] ECG GWAAE ROC-AUC >89% | 89.00 | TBD-5 | `sources/TBD-5_*.md` | "ROC-AUC of **over 89%**" (abstract) — threshold value |
| [3] CICIDS F1 | 83.66 | JoBD-5 | `sources/JoBD-5_*.md` | "CICIDS F1 **0.8366**" (Table 5, p.17) |
| [2] fraud recall >82% | 82.00 | TBD-5 | `sources/TBD-5_*.md` | "recall of **over 82%**" (abstract) — threshold value |
| [2] SMTP ROC-AUC >80% | 80.00 | TBD-5 | `sources/TBD-5_*.md` | "ROC-AUC … **above 80%**" (abstract) — threshold value |
| [11] review band 85–97 | 85–97 (range, not a point) | AIR-2 | `sources/AIR-2_*.md` | "clusters at **85–97%**" (Table 4, p.24) — second-hand, dataset-unattributed |

**"No comparable metric available" band (honest non-zero treatment):**
[4] BDR-5, [5] TBD-1, [8] BDR-3, [12] BDR-4, [15] TBD-2, [16] TBD-3.
**"Qualitative claims only":** [6] AIR-3, [7] BDR-2, [10] BDR-1, [17] AIR-1, [19] AIR-4.
Basis: `sources/*.md` "Evaluation + headline results" sections (NOT AVAILABLE /
qualitative) and tracker R2 C-13, C-14.

**Panel (b): regression-error anchors** (RMSE; lower is better).

| Plot element | Value (RMSE) | Paper ID | Source note | Exact source line |
|---|---|---|---|---|
| [9] HR 8-min | 1.5428 | JoBD-4 | `sources/JoBD-4_*.md` | "HR **RMSE 1.5428 / MAE 1.0871**" (Table 7, p.31) |
| [9] SBP 8-min | 4.1446 | JoBD-4 | `sources/JoBD-4_*.md` | "SBP **RMSE 4.1446 / MAE 2.4323**" (Table 7, p.31) |
| [20] as published | 11.62 | AIR-5 | `sources/AIR-5_*.md` | "FD001 **RMSE rises 11.62±0.19**" (Table 11, p.30) |
| [20] audit re-run | 12.39 | AIR-5 | `sources/AIR-5_*.md` | "→ **12.39±0.35**" (Table 11, p.30) — just past the 2σ threshold |

The arrow links the published value to the audit's re-run value for the same
model/dataset — the corpus's only measured reported→reproduced gap (R2 C-06, C-19).

---

## Fig. 4 — Method-generation shift (`fig4_method_shift`)

**Structure.** Stacked bar: papers per journal × method generation. Generation
is a **curated classification** from each note's "ML methods" section (and,
where available, the PDF); the underlying method facts are exact.

| Plot element | Value | Paper ID(s) | Source note |
|---|---|---|---|
| TBD × Deep / LLM-FM | 3 / 2 | [1]TBD-4, [2]TBD-5, [5]TBD-1 · [15]TBD-2, [16]TBD-3 | notes TBD-1..5 (LLM/FM for TBD-2, TBD-3) |
| BDR × Classical / Deep / not specified | 1 / 3 / 1 | [4]BDR-5 · [7]BDR-2, [10]BDR-1, [12]BDR-4 · [8]BDR-3 | BDR-5 title (classical RFF/spectral); BDR-3 abstract not indexed |
| JoBD × Deep / LLM-FM | 4 / 1 | [3]JoBD-5, [9]JoBD-4, [13]JoBD-1, [18]JoBD-2 · [14]JoBD-3 | JoBD-3 uses Mistral-7B/LLaVA (LLM/FM backbone) |
| AIR × Deep / LLM-FM | 3 / 2 | [11]AIR-2, [19]AIR-4, [20]AIR-5 · [6]AIR-3, [17]AIR-1 | AIR-3 title "…to emerging foundation models"; AIR-1 neural/generative agent survey |
| Totals | Deep 14, LLM/FM 5, Classical 1, not specified 1 = 20 | all | — |

Basis note: this figure supports R2 **C-01 / C-02** (classical → deep →
foundation-model shift). "Not specified" is shown explicitly rather than
guessing BDR-3's generation from its title.

---

## Fig. 5 — Selection flow (`fig5_selection_flow`)

**Structure.** PRISMA-style funnel, one stacked bar per stage (segments =
journal; x is log-scaled). Counts are exact, from `trackers/paper-tracker.md`
("How the 20 papers were chosen (the numbers behind Fig. 1)") and its
per-journal columns.

| Plot element | Total | Per-journal split (TBD/BDR/JoBD/AIR) | Source |
|---|---|---|---|
| Retrieved from OpenAlex (2025+) | 1519 | 296 / 101 / 480 / 642 | `results/openalex_raw/*.json` |
| Passed keyword screen (ML + big data) | 441 | 70 / 10 / 177 / 184 | `results/screen/*.csv`; `code/screen_pool.py` |
| Verified against Crossref | 49 | 11 / 11 / 12 / 15 | `results/pool_selected.json` |
| Included in the review | 20 | 5 / 5 / 5 / 5 | tracker master table (20 selected) |

Basis note: supports the Introduction's selection-method paragraph
(writing-plan §2.2 para I4). The log scale is labelled on the axis
(honest-axis rule).
