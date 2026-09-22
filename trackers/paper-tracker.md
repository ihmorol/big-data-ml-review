# Paper Tracker — Big Data with Machine Learning: A Review

One table, 20 rows — one row per selected paper, everything the team needs on that row. Metadata (title, link, year, journal, access, PDF) is filled in; the working columns are empty for us to fill as we read and write. Same 20 IDs everywhere in the project: TBD-1 … TBD-5, BDR-1 … BDR-5, JoBD-1 … JoBD-5, AIR-1 … AIR-5.

**Pool:** rev 3, locked 2026-09-15 · 20 papers (5 per journal) + 29 vetted alternates · review period 2025–2027 (all items are 2025–2026; no 2027-dated item exists yet). 5 of 20 full texts are already in `papers/`.
**Repo:** https://github.com/ihmorol/big-data-ml-review — the tracker is regenerated from it by `code/build_tracker.py`; re-run that script after a paper swap. Cells the team has already filled are carried over, so a regeneration only refreshes metadata.

## How to use it

- **Work in the master table.** Find your paper by ID, fill the empty cells in that row. Never delete a row; never guess a number.
- **Who fills what:** the reader fills `Reader`, `Read status`, `Dataset & scale`, `Headline result`, `Limitations` · the theme leads fill `Draft §` and `Notes` (quotable line + page) · `S2 · S5` is the quick quality score (0–2 each) from the reader · the integration editor keeps the board current.
- **Status vocabulary, exactly these words:** `Not started` · `Skimmed` · `Read` · `Deep-read`. Draft § uses the outline's codes: §3.3 methods · §3.4 platforms · §3.5 applications · §3.6 cross-cutting · §3.7 future.
- **`†`** marks values taken from the indexed abstract — verify them against the full text, then drop the marker.
- **Keep each cell on one line** (a line break inside a cell breaks the Notion import), and keep the `ID` values unchanged — they are the keys that tie this page to `sources/`, `papers/` and the rest of the repo.

Supporting documents, all in the repo: [papers-pool.md](https://github.com/ihmorol/big-data-ml-review/blob/main/trackers/papers-pool.md) (selection record + swap rules) · [team-tasks.md](https://github.com/ihmorol/big-data-ml-review/blob/main/trackers/team-tasks.md) (roles + timeline) · [writing-progress.md](https://github.com/ihmorol/big-data-ml-review/blob/main/trackers/writing-progress.md) (marks + session log) · [sources/](https://github.com/ihmorol/big-data-ml-review/tree/main/sources) (one extraction note per paper) · [paper/references.bib](https://github.com/ihmorol/big-data-ml-review/blob/main/paper/references.bib) (the BibTeX below, as a file).

## Summary

### The corpus

| Metric | Value |
|---|---|
| Papers | 20 — exactly 5 per journal (the assignment forces 5 × 4) |
| Journals | IEEE Transactions on Big Data · Big Data Research · Journal of Big Data · Artificial Intelligence Review |
| Years | 2025: 12 · 2026: 8 · 2027: 0 |
| Article type | 15 original research · 5 review articles (all AIR, kept as a documented exception per the supervisor clarification of 2026-09-15) |
| Access | 14 open access · 6 paywalled (TBD-1, TBD-2, TBD-3, TBD-5, BDR-3, BDR-5 — institutional access needed) |
| Citations (OpenAlex 2026-09-15) | 393 across the pool · most-cited AIR-1 (134) · six papers at 0 |
| Verification | 20/20 selected papers verified against Crossref on 2026-09-15 |
| Deadline | 2026-09-27 — plan to have the paper done on the 26th |

### How the 20 papers were chosen (the numbers behind Fig. 1)

| Stage | All four journals | IEEE TBD | BDR | JoBD | AIR | Source file |
|---|---|---|---|---|---|---|
| Retrieved from OpenAlex (2025+) | 1519 | 296 | 101 | 480 | 642 | results/openalex_raw/*.json |
| Passed the keyword screen (ML + big-data hit) | 441 | 70 | 10 | 177 | 184 | results/screen/*.csv |
| Candidates verified against Crossref | 49 | 11 | 11 | 12 | 15 | results/pool_selected.json |
| Included in the review | 20 | 5 | 5 | 5 | 5 | the master table below |

Recount from those files before drawing Fig. 1 — the screen counts come from the keyword rules in `code/screen_pool.py`.

### What the 20 papers cover (the §3.2 branches)

Five branches from `notes/landscape-report.md`, used for Fig. 2. Every paper sits in exactly one branch; R2's Branch cell in the master table repeats it.

| Branch | Theme | Papers | Count |
|---|---|---|---|
| B1 | Scalable and interpretable learning methods | TBD-1, TBD-4, TBD-5, BDR-5, JoBD-5 | 5 |
| B2 | Platforms, pipelines, and infrastructure | BDR-2, BDR-3, JoBD-4 | 3 |
| B3 | Applications and domains | BDR-1, BDR-4, JoBD-1, JoBD-3, AIR-2 | 5 |
| B4 | Foundation models and LLMs | TBD-2, TBD-3, AIR-1, AIR-3 | 4 |
| B5 | Privacy, governance, and evaluation | JoBD-2, AIR-4, AIR-5 | 3 |

- **Straddlers (visible, not hidden):** BDR-2 is federated learning as a privacy mechanism *and* as 6G infrastructure · JoBD-2 is privacy machinery on a healthcare application · JoBD-3 is a prompt-engineering method tested on affective computing · TBD-2 is an LLM method paper running on industrial production data · AIR-4 couples generative models to a governance problem · TBD-5 is a methods contribution evaluated only on security data.
- **Empty cells in the taxonomy** — no reinforcement-learning-at-scale paper, no purely theoretical contribution, no 2027-dated item. These are findings for the cross-cutting section, not gaps in our search.
- **Theme labels:** the per-paper "theme" values in `trackers/papers-pool.md` are pod-specific (ten labels for twenty papers, some overlapping). The Branch list above is the authoritative grouping for Fig. 2.

### Access, swaps and thin spots

- **Paywalled (6):** TBD-1, TBD-2, TBD-3, TBD-5, BDR-3, BDR-5. Try institutional access first; if a paper stays unobtainable, swap it rather than writing from the abstract: TBD-A5 (OA) for any TBD item · BDR-A1 or BDR-A2 (both OA) for BDR-3/BDR-5 — see Appendix C.
- **Thin metadata:** BDR-3, BDR-4 and BDR-5 have no indexed abstracts, and evaluation specifics are missing from most abstracts across the pool — `Dataset & scale`, `Headline result` and `Limitations` must come from the full texts.
- **AIR exception:** if the supervisor rejects the five review articles, promote AIR-A6…A10 (pre-verified research articles) from Appendix C and re-balance the branches.

## R1 — Master table: the 20 papers

- **Pods:** IEEE TBD = Pod 1 (Members 1-2) · Big Data Research = Pod 2 (Members 3-4) · Journal of Big Data = Pod 3 (Members 5-6) · AI Review = Pod 4 (Members 7-8).
- **Column guide:** `PDF` and the paper title link to the file and the DOI · `Method / platform` is the abstract-level value to verify · `S2 · S5` is 0–2 for rigor and for relevance to this review (medium appraisal: those two items are enough) · `Notes` takes the quotable line with its page or section number.
- **Full texts** live in `papers/<journal>/<ID>_<Author>_<Year>_<ShortTitle>.pdf`; extraction notes in `sources/<ID>_*.md`.

| ID | Paper (DOI) | Year | Journal · type | Access | PDF | Reader | Read status | Method / platform † | Dataset & scale | Headline result | Limitations (theirs / ours) | Draft § | S2 · S5 | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TBD-1 | [PEXP: A Scalable Parallel Tree-Based Framework for Interpreting Models on Big Data](https://doi.org/10.1109/tbdata.2026.3668673) | 2026 | IEEE TBD · research | PAID — institutional access | — | — | — | PEXP — parallel tree-based post-hoc explainer: distribution-aware perturbation + kernel weighting, Parallel Ensemble Trees (Bagging/Boosting); no platform named † | NOT AVAILABLE — full text not read (paywalled); case study = smart-city video anomaly detection, no dataset or size named | Qualitative only — "significant advantages over mainstream interpretable methods in both runtime efficiency and quality of explanations"; no metrics or baselines named | Theirs: none stated in abstract / Ours: advantages unquantified · explanation fidelity asserted not measured · single-domain case study (smart-city video) · whether parallelism is data-parallel (Spark-style) or algorithmic is unclear | §3.3 | 1 · 2 | Pool's only paper treating explanation cost itself as the scalability bottleneck; abstract-level only (no numbers). Quotable: "critically, computational inefficiency … large-scale datasets" (abstract, DOI). |
| TBD-2 | [TS-MLLM: A Multi-Modal Large Language Model-based Framework for Industrial Time-Series Big Data Analysis](https://doi.org/10.1109/tbdata.2026.3695338) | 2026 | IEEE TBD · research | PAID — institutional access | — | — | — | TS-MLLM — unified multimodal LLM: industrial time-series patch modeling + Spectrum-aware Vision-Language Model Adaptation (SVLMA) + Temporal-centric Multi-modal Attention Fusion (TMAF); no platform named † | NOT AVAILABLE — full text not read (paywalled); abstract says "multiple industrial benchmarks", no dataset or size named | Qualitative only — "significantly outperforms state-of-the-art methods, particularly in few-shot and complex scenarios"; no metrics or named baselines | Theirs: none stated in abstract / Ours: "first to jointly model" claim unverifiable · baselines unnamed · industrial benchmarks unnamed, so scale and external validity unknown · LLM deployment cost/latency unaddressed | §3.5 | 1 · 2 | Pool's only 3-modality (temporal + spectral image + text) LLM for industrial PHM; straddler B4×B2 (LLM method on production data). Abstract-level only. |
| TBD-3 | [GraphLLM: Boosting Graph Reasoning Ability of Large Language Model](https://doi.org/10.1109/tbdata.2025.3627488) | 2025 | IEEE TBD · research | PAID — institutional access | — | — | — | GraphLLM — end-to-end coupling of graph-learning models with an LLM via a Dynamic Task Configuration System; hierarchical local-structure analyzers + global-pattern synthesizers † | NOT AVAILABLE — full text not read (paywalled); evaluated on "four fundamental graph reasoning tasks", no benchmark or size named | +54.44% average accuracy across four graph-reasoning tasks and 96.45% context reduction vs the Graph2Text baseline (abstract; per-task breakdown and whether relative/absolute not stated) | Theirs: none stated in abstract / Ours: 54.44% is an aggregate over unnamed tasks · baselines unnamed · no named graph size, so the "large-scale graph" claim is unevidenced | §3.5 | 1 · 2 | Pool's only LLM graph-reasoning paper and only one quantifying a context-window reduction (96.45%). Numbers are abstract-level only. |
| TBD-4 | [Knowledge Aggregation Transformer Network for Multivariate Time Series Classification](https://doi.org/10.1109/tbdata.2025.3594294) | 2025 | IEEE TBD · research | OA (green) | — | — | — | KATN (Knowledge Aggregation Transformer Network) — 4 aggregation blocks, each additively merging MResNet (local) + multi-head attention (global), then FC alignment + GELU † | 13 UEA archive datasets (MTSC); compared vs 6 SOTA transformer variants and 18 existing MTSC algorithms — individual dataset names/sizes NOT AVAILABLE in the abstract | Lowest AVG_rank among all compared methods; vs 6 SOTA transformers a 'win'/'tie'/'lose' record of 9/6/15 (rank-based; per-dataset accuracies not reported) | Theirs: none stated in abstract / Ours: rank aggregates + W/T/L only, no per-dataset accuracies or variance · no efficiency/cost numbers · UEA series lengths modest vs true big-data streaming | §3.3 | 1 · 2 | Pool's clearest purpose-built transformer with a formal rank-based protocol on a named public archive (UEA); only headline evidence is a cross-dataset rank. Abstract-level only. |
| TBD-5 | [Enhanced Approaches for Anomaly Detection in Streaming Data: Coupling Gaussian Distributions With Space Trees and Adaptive AutoEncoders](https://doi.org/10.1109/tbdata.2026.3679567) | 2026 | IEEE TBD · research | PAID — institutional access | — | — | — | Gaussian Space Trees (GSTrees — space-partitioning ensemble + Gaussian modelling) and Gaussian Weighted ADWIN AutoEncoder (GWAAE — drift-aware AE); streaming, no offline retraining † | 3 named public datasets processed as streams — ECG5000, Credit Card Fraud Detection, SMTP; sizes NOT AVAILABLE in the abstract | ECG5000: GSTrees >94% on all metrics, GWAAE ROC-AUC >89%; SMTP: both ROC-AUC >80%; Credit Card Fraud: recall >82%, ROC-AUC >94% with low false positive/negative rates | Theirs: none stated in abstract / Ours: threshold-style values ("over X%") not precise · no named baselines · moderate-size tabular/stream benchmarks, so "big data" rests on velocity not volume · no significance tests | §3.3 | 2 · 2 | Pool's only paper evaluating two complementary online detectors with per-dataset recall/ROC-AUC — the cleanest streaming, drift-aware, no-retraining case. Abstract-level only. |
| BDR-1 | [Explainable malware detection through integrated graph reduction and learning techniques](https://doi.org/10.1016/j.bdr.2025.100555) | 2025 | Big Data Research · research | OA (hybrid) | — | — | — | Integrated framework — novel graph reduction on CFG/FCG program graphs + GNN detection + GNNExplainer subgraph explanations † | NOT AVAILABLE — no dataset named in the abstract; no malware/benign counts or graph-scale figures | Qualitative only — graph reduction "significantly reduces the size and complexity of the input graphs, while maintaining the detection performance"; no metrics or baselines named | Theirs: none stated in abstract / Ours: "significantly reduces" carries no numbers · dataset/families/graph scale unnamed · baselines unnamed · explainability quality has no fidelity metric | §3.5 | 1 · 2 | Pool's only paper where the data structure itself (graph size) is the obstacle, fusing graph reduction with analyst-facing GNNExplainer subgraphs. Abstract-level only. |
| BDR-2 | [Efficient training: Federated learning cost analysis](https://doi.org/10.1016/j.bdr.2025.100510) | 2025 | Big Data Research · research | OA (hybrid) | — | — | — | Comparative cost analysis of federated learning approaches across training time, communication overhead, and energy consumption for 6G distributed/edge training † | NOT AVAILABLE — no dataset named in the abstract; simulation vs testbed and device count unstated | Qualitative only — "FL can significantly accelerate the training process while reducing the data transferred across the network"; no timing/energy/bandwidth figures or named baselines | Theirs: none explicit (own caveat: effectiveness "depends on the specific FL approach and the network conditions") / Ours: no numbers · no datasets, FL algorithms, or settings named · no accuracy trade-off alongside the cost axes · energy methodology unstated | §3.4 | 1 · 2 | Pool's only paper pricing federated training (time/communication/energy) for 6G — FL as an economics/energy question. Straddler B2×B5. Abstract-level only. |
| BDR-3 | [Opinion fraud detection on massive datasets by spark](https://doi.org/10.1016/j.bdr.2026.100590) | 2026 | Big Data Research · research | PAID — institutional access | — | — | — | NOT AVAILABLE — abstract not indexed (paywalled); title indicates Spark-based opinion/fraud detection | NOT AVAILABLE — abstract not indexed (paywalled) | NOT AVAILABLE — abstract not indexed (paywalled) | Theirs: NOT AVAILABLE — abstract not indexed / Ours: describable only at title level; full text must be read before any scalar claim | §3.4 | — · 2 | Pool's only unambiguous Apache Spark/cluster contribution; highest-priority retrieval gap (fully paywalled, no abstract anywhere). Title-level only. |
| BDR-4 | [Heterogeneous Graph-based Risk Assessment for Internet Financial Companies with Company Big Data](https://doi.org/10.1016/j.bdr.2026.100620) | 2026 | Big Data Research · research | OA (green) | — | — | — | NOT AVAILABLE — abstract not indexed (preprint access blocked); title indicates a heterogeneous graph-based risk-assessment method | NOT AVAILABLE — abstract not indexed (green SSRN preprint blocked at retrieval) | NOT AVAILABLE — abstract not indexed (green SSRN preprint blocked at retrieval) | Theirs: NOT AVAILABLE — abstract not indexed / Ours: describable only at title level; a free SSRN green preprint exists but was Cloudflare-blocked | §3.5 | — · 2 | Pool's only graph-learning paper on natively relational financial/company data; retrievable via SSRN preprint (blocker = bot-protection, not paywall). Title-level only. |
| BDR-5 | [Large-scale least squares regression based on fast spectral embedding and random Fourier feature mapping](https://doi.org/10.1016/j.bdr.2026.100589) | 2026 | Big Data Research · research | PAID — institutional access | — | — | — | NOT AVAILABLE — abstract not indexed (paywalled); title indicates fast spectral embedding + random Fourier feature mapping for large-scale least squares | NOT AVAILABLE — abstract not indexed (paywalled) | NOT AVAILABLE — abstract not indexed (paywalled) | Theirs: NOT AVAILABLE — abstract not indexed / Ours: describable only at title level; must be read before any scalar or comparative claim | §3.3 | — · 1 | Pool's only classical statistical-learning/regression method — the sole non-deep representative of scaling classical learning. Title-level only. |
| JoBD-1 | [A deep learning-based framework for large-scale plant disease detection using big data analytics in precision agriculture](https://doi.org/10.1186/s40537-025-01265-9) | 2025 | Journal of Big Data · research | OA (gold) | — | — | — | WY-CN-NASNetLarge — NASNetLarge (ImageNet-pretrained, ~88M params), 80 frozen layers + custom head, AdamW + mixed precision FP16/FP32, Grad-CAM; baselines ResNet152V2/InceptionResNetV2/DenseNet201/ViT | YellowRWheat-NLSCorn — 30,000 images / 12 classes (24k/3k/3k) merged from Yellow-Rust-19 + CD&S + PlantVillage; platform = Kaggle single-GPU (Tesla P100) — no Spark/Hadoop | 97.33% accuracy on the 12-class dataset (26 epochs), beating DenseNet201 96.40%, InceptionResNetV2 95.70%, ResNet152V2 93.23%, ViT 41.3%; 95.60% on Yellow-Rust-19 | Theirs (p.34): regional dataset constraints · advanced-GPU dependence · only 2 diseases · no real-field validation / Ours: "big data" nominal (single GPU, no distributed engine) · no significance tests · ViT baseline a strawman (41.3%) · oversampling by duplication risks leakage | §3.5 | 2 · 2 | Pool's only agriculture/plant-disease application; strongest ablation of a training recipe. "Big data" = image volume, contradicting the corpus's stricter infrastructure usage. |
| JoBD-2 | [A privacy-enhanced framework for collaborative Big Data analysis in healthcare using adaptive federated learning aggregation](https://doi.org/10.1186/s40537-025-01169-8) | 2025 | Journal of Big Data · research | OA (gold) | — | — | — | Adaptive FL aggregation — server switches FedAvg↔FedSGD on divergence δ_t vs τ=0.10; ResNet (27 MB)/VGG16 (552 MB) local models; centralised-arm differential privacy (σ²=0.5, ε≈2.5); optional SMPC (Shamir SSS); simulated multi-cloud | 3 public datasets, 10 simulated non-IID clients — TB Chest X-ray 7,000 + Brain Tumor MRI 3,624 + Diabetic Retinopathy 3,662 (224×224, 70/15/15); no Spark/Hadoop | Adaptive aggregation up to 96.3% accuracy with ≈20% less execution time and ≈20% fewer rounds (320 s/15 epochs vs FedAvg 360 s/18); centralised+DP 96.0–98.3%; σ²=1.0 drops to 94.5% (ε=1.0) | Theirs: communication overhead under limited bandwidth · client compute limits · no real multi-cloud deployment (simulated only) / Ours: all federation simulated · DP applied to the centralised arm only · adaptive gain modest and untested statistically · SMOTE-before-partition leakage risk | §3.6 | 2 · 2 | Pool's only adaptive FedAvg↔FedSGD switching rule and only full privacy–utility trade-off table (accuracy vs ε vs MB) for healthcare FL. Contradicts JoBD-4's latency-first design. |
| JoBD-3 | [Advancing multimodal emotion recognition in big data through prompt engineering and deep adaptive learning](https://doi.org/10.1186/s40537-025-01264-w) | 2025 | Journal of Big Data · research | OA (gold) | — | — | — | 10-phase MER pipeline — Mistral-7B/HuBERT/LLaVA+TimeSformer/MediaPipe Pose encoders, Dynamic Prompt Engineering, AdaptiveGNN + HAN-GNN + Cross-Modality Transformer Fusion, prototypical contrastive learning, GAN augmentation, Optuna, ONNX export | IEMOCAP + MELD (~25k utterances); external SAVEE 480 and CMU-MOSEAS (100/lang); test splits IEMOCAP 1,623 / MELD 2,610; ONNX Runtime — no distributed engine | IEMOCAP 99.82% / MELD 99.81% test accuracy (AUC≈0.999, MCC≈0.998); SAVEE 99.78%; CMU-MOSEAS 99.1–99.4%; train ≈5 min, inference 0.3–0.5 ms — claimed 25–30 pt leap over ~70% SOTA | Theirs: model complexity vs edge deployment · limited cultural/sensor generalisation · no post-hoc XAI / Ours: accuracies implausibly high vs MER literature (likely leakage/eval flaw) · inconsistent dataset naming (MOSEI vs MOSEAS) · SOTA comparison mixes datasets/tasks · 100 samples/lang too small | §3.5 | 2 · 2 | Pool's only 4-modality (text+audio+video+motion) fusion framework and only zero-shot cross-lingual evaluation; reported accuracies flagged as anomalously high — verify before quoting. |
| JoBD-4 | [Cloud based real-time multivariate multi-step prediction of systolic blood pressure and heart rate using temporal convolutional network and Apache Spark](https://doi.org/10.1186/s40537-025-01207-5) | 2025 | Journal of Big Data · research | OA (gold) | — | — | — | FCMS-iDMM — multi-task TCN (best) + LSTM/GRU/seq2seq baselines, Optuna tuning; online = simulated sensor → Kafka → Spark Streaming sliding window → TCN; fog/cloud tiers | MIMIC-III, minute-by-minute SBP+HR for 2 patients (5–20 min obs → 8–25 min target, 80/20 split); Kafka+Spark Streaming on simulated sensors | Multi-task TCN 8-min: HR RMSE 1.5428 / MAE 1.0871; SBP RMSE 4.1446 / MAE 2.4323 — best at all horizons, beats LSTM/GRU/seq2seq (p<0.05); multi-task beats single-task | Theirs: no XAI · centralised training (FL as future work) · no real clinical deployment · single dataset · no transformer baselines / Ours: n=2 patients only · MIMIC-II vs MIMIC-III inconsistency · pipeline tested on simulated sensors only · Table 9 mislabels own best model | §3.4 | 2 · 2 | Pool's only Kafka+Spark+fog/cloud streaming deployment and only multi-task joint SBP+HR forecasting; n=2 and the MIMIC-II/III inconsistency are the key caveats. |
| JoBD-5 | [Graph neural network approach with spatial structure to anomaly detection of network data](https://doi.org/10.1186/s40537-025-01149-y) | 2025 | Journal of Big Data · research | OA (gold) | — | — | — | Unsupervised 3-module framework — MI-based feature slicing; Poincaré-ball graph embedding with a novel distance gain factor (conformal, negative-curvature-preserving); improved DGI augmentation; GAT classifier | CICIDS2017 (3,119,345 records, 13.75% anomalies, 78 feats), UNSW-NB15 (2,540,044, 11.47%, 49), CampusNet-Logs (1,249,354 proprietary, 4.40%, 11); single VM (24 cores, 96 GB) — no distributed engine | Beats all baselines — CICIDS F1 0.8366/MCC 0.4646, UNSW F1 0.9341/MCC 0.9049, CampusNet F1 0.9913; edge-weight optimisation ≈2× node augmentation (F1 +0.1355 vs +0.0438 on CICIDS) | Theirs: best for global not local anomalies · Poincaré embedding overhead on large graphs hinders real-time · no temporal modelling / Ours: no significance tests · "twice the contribution" loose (mixed metrics) · slowest model (34–39 s per 1k records) · single-VM, table artefacts | §3.3 | 2 · 2 | Pool's only hyperbolic-space (Poincaré ball) embedding and only edge-weight vs node-attribute ablation in graph anomaly detection; concedes its own scalability overhead. |
| AIR-1 | [Agentic AI: a comprehensive survey of architectures, applications, and future directions](https://doi.org/10.1007/s10462-025-11422-4) | 2025 | AI Review · review | OA (hybrid) | [PDF](https://github.com/ihmorol/big-data-ml-review/blob/main/papers/AIR/AIR-1_AbouAli_2025_AgenticAI.pdf) | Ikramul Hasan | Read | symbolic agents (MDP/POMDP, BDI, SOAR) vs neural agents (LLM orchestration — LangChain, AutoGen, CrewAI, RAG) · no platform — conceptual survey, but flags the cloud-compute bill | No datasets — survey. Evidence base: 90 papers (78 core + 12 seminal), Jan 2018–Mar 2025, PRISMA 2020 | Two paradigms, not one: symbolic (planners, BDI/SOAR) vs neural/generative (LLM orchestration). Domain decides the pick — symbolic/hybrid in safety-critical work (healthcare, legal), neural in data-rich fields (finance, education); neuro-symbolic is the proposed way forward | Theirs: search stops Mar 2025 · 12 of 90 studies added outside the PRISMA flow · proprietary systems under-documented / Ours: taxonomy asserted, not tested · "all 90 studies fit" is self-reported · no cost numbers behind the compute warning | §3.5 · §3.7 | 1 · 2 | "symbolic and hybrid architectures dominate safety-critical applications like healthcare and robotics, while pure neural systems thrive in data-rich, adaptive domains such as finance and education." (p. 24) |
| AIR-2 | [Artificial intelligence advances in anomaly detection for telecom networks](https://doi.org/10.1007/s10462-025-11108-x) | 2025 | AI Review · review | OA (hybrid) | [PDF](https://github.com/ihmorol/big-data-ml-review/blob/main/papers/AIR/AIR-2_Edozie_2025_TelecomAnomalyDetection.pdf) | Ikramul Hasan | Read | classical ML (Isolation Forest, k-NN, LOF, XGBoost) → deep learning (LSTM, autoencoders, VAE, MSCRED, DeepAnT, Telemanom) → GNNs, transformers, federated learning, XAI · no platform used; Hadoop/Spark mentioned as history only | No datasets of their own (stated p. 33): 3,084 screened → 160 included. Five dataset categories described (5G streams, sensor telemetry, security logs, traffic logs, synthetic) — no benchmark named, no sizes | Rule-based detection is obsolete; deep learning reports 85–97% accuracy but pays in latency (autoencoders 2,000–7,000 ms vs Isolation Forest 100–400 ms). The real blocker is deployment — compute cost, edge latency, model drift — not accuracy | Theirs: no data of their own · label scarcity and class imbalance · model drift and retraining cost · edge latency vs model size / Ours: accuracy ranges tied to no named dataset · no baselines · no volume numbers behind the "big data" framing · no LLM coverage · reference years contain typos | §3.5 · §3.6 | 1 · 2 | "Traditional methods of anomaly detection, which rely on rule-based systems, are no longer effective in today's fast-evolving telecom landscape." (p. 1) |
| AIR-3 | [From classical machine learning to emerging foundation models: review on multimodal data integration for cancer research](https://doi.org/10.1007/s10462-026-11522-9) | 2026 | AI Review · review | OA (hybrid) | [PDF](https://github.com/ihmorol/big-data-ml-review/blob/main/papers/AIR/AIR-3_Muneer_2026_MultimodalFoundationModelsCancer.pdf) | Ikramul Hasan | Read | classical ML (SVM/RF) → deep latent fusion (CNN/VAE/GNN) → foundation models (scGPT, OmniCLIP, Nicheformer) · multimodal cancer big data (omics, WSIs, radiology, EHR) | No primary data — review. Evidence base: 54 core studies (PRISMA: 3,280 screened → 54 included) + taxonomy of FMs (scGPT >33M cells, Nicheformer 110M cells, OmniCLIP 2.2M paired tissue images) | Intermediate and attention-based latent fusions significantly outperform early/late fusion in survival and metastasis prediction; foundation models enable few-shot learning for rare cancers; severe translational gap (>90% retrospective; near-zero prospective trials/approvals) | Theirs: extreme data heterogeneity and missing modalities in real clinics · high compute/GPU cost · lack of mechanistic interpretability · near-zero prospective trials or FDA clearances / Ours: 69-page secondary survey with no standardized experimental baselines · unharmonized metrics · oncology-specific framing | §3.3 · §3.5 | 1 · 2 | "The performance, reliability, and ultimate clinical utility of any AI model are inextricably bound to the fidelity, structure, and integrity of the data upon which it is trained." (p. 46) |
| AIR-4 | [Review of generative AI for synthetic data generation: a healthcare perspective](https://doi.org/10.1007/s10462-025-11440-2) | 2025 | AI Review · review | OA (hybrid) | [PDF](https://github.com/ihmorol/big-data-ml-review/blob/main/papers/AIR/AIR-4_Waseem_2025_SyntheticDataHealthcare.pdf) | — | — | Structured narrative survey (not PRISMA) of 5 generative families — GANs, VAEs, Transformers, diffusion, federated generative — plus DP/PATE/secure-aggregation privacy machinery; taxonomy Figure 1 | No primary data (p.60). Cited benchmarks: MIMIC-III/IV, eICU, ISIC 2018–2020, BraTS, IXI, MSD, IU-Xray, UCR, ECG/EEG — scales to 250k+ patients, 15M PubMed abstracts, 20 hospitals | No family wins everywhere — diffusion leads image fidelity (sCT MAE 43 HU, SSIM 0.965); GAN augmentation +2.8–6.7 pp histopathology AUROC; VAEs win structured EHR (<3% downstream gap); FID/SSIM do not track downstream clinical usefulness | Theirs: structured survey not systematic (no exclusion counts, p.4) · no numerical quality scores · heterogeneous benchmarks force qualitative synthesis · no data generated (p.60) / Ours: corpus size never reported · no re-analysis (all numbers second-hand) · Table 13 mixes peer-reviewed/preprints/abstract-only · DP/privacy reported thinly · coverage skews to imaging/EHR | §3.6 | 1 · 2 | Pool's only synthetic-data generation source — unifies 5 generative families with a cross-domain quantitative table (Table 13) and HIPAA/GDPR/EU AI Act mapping. |
| AIR-5 | [A survey of deep multivariate time-series models with an empirical reproducibility audit](https://doi.org/10.1007/s10462-026-11674-8) | 2026 | AI Review · review | OA (hybrid) | [PDF](https://github.com/ihmorol/big-data-ml-review/blob/main/papers/AIR/AIR-5_Vats_2026_DeepMultivariateTimeSeriesSurvey.pdf) | — | — | Narrative survey with a 3-axis taxonomy (paradigm × task × capability) + targeted reproducibility audit re-running 8 official codebases under one protocol (seed 42 baseline, 5–10 seed runs), 1σ/2σ descriptive rule | 17 benchmark resources (Table 4) + C-MAPSS; largest SMD 1.42M×38, WADI 1.22M×103, Traffic 862 channels; single NVIDIA Tesla V100 (32 GB) — no big-data platform | Broad trends reproduce but exact numbers often do not — aLLM4TS MSL F1 82.26→79.25±0.40, TimeCMA all 16 settings low (ETTh2 h96 MSE 0.286→0.330), TSCMamba EigenWorms 87.00→42.82%; "single-run evaluations often overestimate model stability" (p.4) | Theirs: deliberately deep-learning-centric · audit intentionally limited (8 models, one protocol) · 2σ rule descriptive, not a significance test / Ours: no formal search protocol/PRISMA corpus count · low verdicts blend method with the auditors' environment · internally inconsistent clustering run counts · contamination named but never tested | §3.6 | 2 · 2 | Pool's only empirical reproducibility audit (8 official codebases, per-seed SD) — the evidentiary basis for the review's evaluation-fragmentation claim. Quotable: "single-run evaluations often overestimate model stability" (p.4). |

Cell rules: name datasets with their scale (rows, GB, nodes) — "large-scale" alone is not evidence · list the baselines the authors compared against, since "no baseline" is itself a finding · keep every number that produces the headline result.

## R2 — Claim-to-evidence ledger

Append a row for every number, comparison or "first/only" claim in the manuscript: which paper backs it, where exactly, and who checked it. The row below is the format — replace it as real claims appear. Status flow: `Draft` → `Checked` (a second member opened the source and found the number) → `Frozen` (in the submitted text). Abstract-only backing is fine for a description, never for a number.

| Claim ID | Claim (as written) | Backing paper(s) | Evidence (number + page/section) | Used in draft (§) | Checked by | Status |
|---|---|---|---|---|---|---|
| C-01 | Deep learning, and increasingly LLM/foundation-model backbones, dominates current big-data ML research. | TBD-2, TBD-3, JoBD-3, AIR-3, AIR-4, AIR-5 | TBD-2 abstract claims first joint temporal+spectral+text modelling; JoBD-3 uses Mistral-7B/HuBERT/LLaVA (p.20); AIR-3 title "From classical machine learning to emerging foundation models" | §3.3 · §3.5 | — | Draft |
| C-02 | The corpus shows an active shift from classical/purpose-built models toward LLM and foundation-model backbones. | TBD-2, TBD-3, JoBD-3, AIR-3, AIR-5 | AIR-3 classical→deep→foundation-model arc (abstract); TBD-3 couples an LLM with graph learning (abstract); AIR-5 §3.2 lists LLM-reprogramming + native TS foundation models (Table 3, p.12) | §3.3 · §3.7 | — | Draft |
| C-03 | Explainability is a recurring and largely unsolved requirement across domains. | TBD-1, BDR-1, JoBD-3, JoBD-4, AIR-4 | TBD-1 abstract "computational inefficiency … large-scale datasets"; BDR-1 "a simple binary classification … is insufficient for malware analysts" (abstract); JoBD-4 "limited interpretability" (p.40); JoBD-3 "lacks dedicated post-hoc explainability tools" (p.56) | §3.6 | — | Draft |
| C-04 | Federated/distributed learning is the dominant privacy mechanism, and it trades accuracy and cost for data locality. | BDR-2, JoBD-2, AIR-4 | JoBD-2 adaptive aggregation up to 96.3%, ≈20% faster/fewer rounds (p.1); σ²=1.0 → 94.5% at ε=1.0 (Table 11, p.39); BDR-2 abstract "FL can significantly accelerate the training process while reducing the data transferred" | §3.4 · §3.6 | — | Draft |
| C-05 | Real-time/streaming pipelines are emerging, but are evaluated on architecture rather than measured operational latency. | JoBD-4, TBD-5, BDR-3 | JoBD-4 Kafka→Spark Streaming→fog/cloud tiers (p.16); TBD-5 GSTrees/GWAAE on streamed ECG5000/Credit Card/SMTP (abstract); BDR-3 title "…on massive datasets by spark" | §3.4 | — | Draft |
| C-06 | Reported evaluation results are often numerically irreproducible; single-run estimates overstate model stability. | AIR-5 | aLLM4TS MSL F1 82.26→79.25±0.40 (Table 7, p.27); TimeCMA all 16 settings low (ETTh2 h96 MSE 0.286→0.330, Table 16); "single-run evaluations often overestimate model stability" (p.4) | §3.6 | — | Draft |
| C-07 | In several application papers the "big data" framing rests on data variety or image volume rather than distributed scale. | JoBD-1, JoBD-2, JoBD-3 | JoBD-1 trains 30,000 images on a single Kaggle GPU, no Spark/Hadoop (p.20); JoBD-3 uses ONNX Runtime, ~25k utterances (p.16); JoBD-2 uses 10 simulated clients, no Spark/Hadoop (p.16) | §3.4 · §3.6 | — | Draft |
| C-08 | Graph-structured learning is a major method family spanning security, network, and finance domains. | BDR-1, BDR-4, JoBD-5, TBD-3 | JoBD-5 Poincaré-ball GAT on CICIDS2017/UNSW-NB15/CampusNet (p.15); BDR-4 title heterogeneous-graph risk assessment; JOBD-5 F1 up to 0.9913 (Table 5, p.17) | §3.3 · §3.5 | — | Draft |
| C-09 | Several headline numbers in the corpus are either unquantified at abstract level or anomalously high versus the literature. | TBD-3, JoBD-3, TBD-5 | TBD-3 "+54.44% average accuracy" over four unnamed tasks (abstract); JoBD-3 99.82%/99.81% on IEMOCAP/MELD vs ~70% literature (p.53); TBD-5 threshold-style ">94%" values (abstract) | §3.6 | — | Draft |
| C-10 | Streaming anomaly detection is being met by lightweight/online methods that avoid offline retraining. | TBD-5, JoBD-5, AIR-2 | TBD-5 GSTrees >94% ECG5000 and recall >82%/ROC-AUC >94% on fraud (abstract); AIR-2 "Traditional methods … rule-based systems, are no longer effective" (p.1) | §3.3 · §3.5 | — | Draft |
| C-11 | Multimodal fusion is a leading architecture choice for heterogeneous big data. | TBD-2, JoBD-3, AIR-3 | TBD-2 Temporal-centric Multi-modal Attention Fusion (TMAF) (abstract); JoBD-3 four-modality fusion pipeline (p.20); AIR-3 intermediate/attention-based latent fusion outperforms early/late (abstract) | §3.3 | — | Draft |
| C-12 | Time-series modelling at scale is dominated by transformer and attention architectures. | TBD-4, TBD-2, AIR-5, JoBD-4 | TBD-4 KATN lowest AVG_rank vs 6 SOTA transformers and 18 MTSC algorithms on 13 UEA datasets (abstract); AIR-5 Transformer-based Axis-1 paradigm (Table 3, p.12) | §3.3 | — | Draft |
| C-13 | Scalability claims are frequently architectural rather than empirically measured. | TBD-1, BDR-2, JoBD-1 | TBD-1 abstract gives no platform, dataset, or metric despite "large-scale datasets"; BDR-2 abstract gives no timing/energy/bandwidth figures; JoBD-1 "large-scale" = a single-GPU image dataset (p.20) | §3.6 | — | Draft |
| C-14 | Part of the 2025–2026 record is effectively inaccessible, constraining the review's evidence base. | BDR-3, BDR-4, BDR-5, TBD-1, TBD-2, TBD-3, TBD-5 | BDR-3/BDR-4/BDR-5 have no indexed abstract (source notes); TBD-1/2/3/5 are paywalled with no OA copy (source notes) | §3.6 · §3.7 | — | Draft |
| C-15 | An unresolved tension runs through the corpus between centralised data pooling and privacy-preserving locality. | BDR-2, JoBD-2, JoBD-4, AIR-4 | BDR-2 prices federated training (abstract); JoBD-2 DP reduces accuracy 96.5→94.5% (Table 11, p.39); JoBD-4 explicitly defers privacy ("federated learning … in future work", p.40) | §3.6 | — | Draft |
| C-16 | Efficiency and latency, not accuracy, are emerging as the binding constraint at scale. | TBD-3, JoBD-3, JoBD-4, BDR-2 | TBD-3 96.45% context reduction (abstract); JoBD-3 0.3–0.5 ms/sample inference (p.43); JoBD-4 TCN fastest runtime (p.31); BDR-2 cost measured in time/communication/energy (abstract) | §3.3 · §3.4 | — | Draft |
| C-17 | Public benchmark datasets for industrial and clinical time-series remain concentrated and modest in scale. | AIR-5, JoBD-4, TBD-4 | AIR-5 largest MTS benchmark SMD 1.42M×38 (Table 4, p.22); JoBD-4 evaluates MIMIC-III for 2 patients only (p.22); TBD-4 evaluates on the 13 UEA datasets (abstract) | §3.5 | — | Draft |
| C-18 | Security and anomaly detection is the single most-represented application domain in the corpus. | BDR-1, JoBD-5, TBD-5, AIR-2, BDR-3 | Branch map: B1 (TBD-5, JoBD-5) + B3 (BDR-1, AIR-2) + B2 (BDR-3) all touch detection; JoBD-5/CICIDS (p.15), TBD-5 fraud/ECG (abstract), AIR-2 telecom anomaly detection | §3.5 | — | Draft |
| C-19 | Fidelity/summary metrics do not reliably track downstream usefulness. | AIR-4, AIR-5 | AIR-4 "FID and SSIM … do not always align with downstream diagnostic performance or clinical trustworthiness" (p.16); AIR-5 "reported performance gains may be influenced by experimental variance rather than purely architectural improvements" (p.36) | §3.6 | — | Draft |
| C-20 | Lightweight or classical methods can match or beat deep models on specific tasks. | TBD-5, BDR-5, JoBD-1 | TBD-5 GSTrees matches/beats deep autoencoders on streams (abstract); BDR-5 scales classical least-squares regression (title); JoBD-1 CNN 97.33% vs ViT 41.3% (p.30–31) | §3.3 · §3.6 | — | Draft |
| C-21 | The corpus contains no reinforcement-learning-at-scale paper and no purely theoretical contribution. | corpus (all 20) | Branch map in §Summary — no RL-at-scale item; taxonomy empty cells (paper-tracker §"What the 20 papers cover") | §3.6 · §3.7 | — | Draft |

## Appendix A — BibTeX (20 entries)

Key rule: `firstauthorlastnameYYYYkeyword`. Fields come from the OpenAlex/Crossref records in `results/pool_selected.json`; `% TODO` lines mark what to verify at the publisher during the references pass. The same entries are in `paper/references.bib`, which a reference manager (Zotero, Mendeley, JabRef) imports in one step.

#### TBD-1 · jiang2026pexp

```bibtex
% TODO: compound surname(s) parsed mechanically - verify against the publisher page
@article{jiang2026pexp,
  author   = {Wendong Jiang and Chih-Yung Chang and Tzu-Chia Huang and Yu-Ting Chin and Sinha Roy, Diptendu},
  title    = {PEXP: A Scalable Parallel Tree-Based Framework for Interpreting Models on Big Data},
  journal  = {IEEE Transactions on Big Data},
  year     = {2026},
  volume   = {12},
  number   = {4},
  pages    = {1177--1194},
  doi      = {10.1109/tbdata.2026.3668673},
  url      = {https://doi.org/10.1109/tbdata.2026.3668673},
  note     = {Research article; pool ID TBD-1}
}
```

#### TBD-2 · wang2026mllm

```bibtex
% TODO: volume/issue not indexed yet (early access) - verify at IEEE Xplore
@article{wang2026mllm,
  author   = {Haiteng Wang and Yugong Li and Y C Zhu and Jingheng Yan and Lei Ren and Laurence T. Yang},
  title    = {TS-MLLM: A Multi-Modal Large Language Model-based Framework for Industrial Time-Series Big Data Analysis},
  journal  = {IEEE Transactions on Big Data},
  year     = {2026},
  doi      = {10.1109/tbdata.2026.3695338},
  url      = {https://doi.org/10.1109/tbdata.2026.3695338},
  note     = {Research article; pool ID TBD-2}
}
```

#### TBD-3 · chai2025graphllm

```bibtex
@article{chai2025graphllm,
  author   = {Ziwei Chai and Tianjie Zhang and Liang Wu and Kaiqiao Han and Xiaohai Hu and Xuanwen Huang},
  title    = {GraphLLM: Boosting Graph Reasoning Ability of Large Language Model},
  journal  = {IEEE Transactions on Big Data},
  year     = {2025},
  volume   = {12},
  number   = {2},
  pages    = {475--483},
  doi      = {10.1109/tbdata.2025.3627488},
  url      = {https://doi.org/10.1109/tbdata.2025.3627488},
  note     = {Research article; pool ID TBD-3}
}
```

#### TBD-4 · xiao2025katn

```bibtex
@article{xiao2025katn,
  author   = {Zhiwen Xiao and Huanlai Xing and Rong Qu and Hui Li and Huagang Tong and Shouxi Luo},
  title    = {Knowledge Aggregation Transformer Network for Multivariate Time Series Classification},
  journal  = {IEEE Transactions on Big Data},
  year     = {2025},
  volume   = {11},
  number   = {6},
  pages    = {3413--3429},
  doi      = {10.1109/tbdata.2025.3594294},
  url      = {https://doi.org/10.1109/tbdata.2025.3594294},
  note     = {Research article; pool ID TBD-4}
}
```

#### TBD-5 · gunbilek2026enhanced

```bibtex
% TODO: compound surname(s) parsed mechanically - verify against the publisher page
@article{gunbilek2026enhanced,
  author   = {Ercan Gunbilek and Akusta Dağdevıren, Züleyha and Hasan Bulut},
  title    = {Enhanced Approaches for Anomaly Detection in Streaming Data: Coupling Gaussian Distributions With Space Trees and Adaptive AutoEncoders},
  journal  = {IEEE Transactions on Big Data},
  year     = {2026},
  volume   = {12},
  number   = {4},
  pages    = {1318--1331},
  doi      = {10.1109/tbdata.2026.3679567},
  url      = {https://doi.org/10.1109/tbdata.2026.3679567},
  note     = {Research article; pool ID TBD-5}
}
```

#### BDR-1 · mohammadian2025explainable

```bibtex
@article{mohammadian2025explainable,
  author   = {Hesamodin Mohammadian and Griffin Higgins and Samuel Ansong and Roozbeh Razavi‐Far and Ali A. Ghorbani},
  title    = {Explainable malware detection through integrated graph reduction and learning techniques},
  journal  = {Big Data Research},
  year     = {2025},
  volume   = {41},
  pages    = {100555},
  doi      = {10.1016/j.bdr.2025.100555},
  url      = {https://doi.org/10.1016/j.bdr.2025.100555},
  note     = {Research article; pool ID BDR-1}
}
```

#### BDR-2 · teixeira2025efficient

```bibtex
@article{teixeira2025efficient,
  author   = {Rafael Teixeira and Leonardo Almeida and Mário Antunes and Diogo Gomes and Rui L. Aguiar},
  title    = {Efficient training: Federated learning cost analysis},
  journal  = {Big Data Research},
  year     = {2025},
  volume   = {40},
  pages    = {100510},
  doi      = {10.1016/j.bdr.2025.100510},
  url      = {https://doi.org/10.1016/j.bdr.2025.100510},
  note     = {Research article; pool ID BDR-2}
}
```

#### BDR-3 · ghodsi2026opinion

```bibtex
@article{ghodsi2026opinion,
  author   = {Shahab Ghodsi and Ali Moeini},
  title    = {Opinion fraud detection on massive datasets by spark},
  journal  = {Big Data Research},
  year     = {2026},
  volume   = {43},
  pages    = {100590},
  doi      = {10.1016/j.bdr.2026.100590},
  url      = {https://doi.org/10.1016/j.bdr.2026.100590},
  note     = {Research article; pool ID BDR-3}
}
```

#### BDR-4 · liu2026heterogeneous

```bibtex
@article{liu2026heterogeneous,
  author   = {Qigang Liu and Yuxin Qiu and Yuhang Jia and Yinfan Wang and Maoguo Wu},
  title    = {Heterogeneous Graph-based Risk Assessment for Internet Financial Companies with Company Big Data},
  journal  = {Big Data Research},
  year     = {2026},
  volume   = {45},
  pages    = {100620},
  doi      = {10.1016/j.bdr.2026.100620},
  url      = {https://doi.org/10.1016/j.bdr.2026.100620},
  note     = {Research article; pool ID BDR-4}
}
```

#### BDR-5 · li2026large

```bibtex
@article{li2026large,
  author   = {Xingyu Li and Jinglei Liu},
  title    = {Large-scale least squares regression based on fast spectral embedding and random Fourier feature mapping},
  journal  = {Big Data Research},
  year     = {2026},
  volume   = {43},
  pages    = {100589},
  doi      = {10.1016/j.bdr.2026.100589},
  url      = {https://doi.org/10.1016/j.bdr.2026.100589},
  note     = {Research article; pool ID BDR-5}
}
```

#### JoBD-1 · elfouly2025deep

```bibtex
% TODO: article number not indexed - verify at the publisher
@article{elfouly2025deep,
  author   = {Mahmoud Khaled Elfouly and Amr Abdelaziz and Wael H. Gomaa and Mohammed Abdalla},
  title    = {A deep learning-based framework for large-scale plant disease detection using big data analytics in precision agriculture},
  journal  = {Journal of Big Data},
  year     = {2025},
  volume   = {12},
  number   = {1},
  doi      = {10.1186/s40537-025-01265-9},
  url      = {https://doi.org/10.1186/s40537-025-01265-9},
  note     = {Research article; pool ID JoBD-1}
}
```

#### JoBD-2 · haripriya2025privacy

```bibtex
% TODO: article number not indexed - verify at the publisher
@article{haripriya2025privacy,
  author   = {Rahul Haripriya and Nilay Khare and Manish Pandey and Sreemoyee Biswas},
  title    = {A privacy-enhanced framework for collaborative Big Data analysis in healthcare using adaptive federated learning aggregation},
  journal  = {Journal of Big Data},
  year     = {2025},
  volume   = {12},
  number   = {1},
  doi      = {10.1186/s40537-025-01169-8},
  url      = {https://doi.org/10.1186/s40537-025-01169-8},
  note     = {Research article; pool ID JoBD-2}
}
```

#### JoBD-3 · wafa2025advancing

```bibtex
% TODO: article number not indexed - verify at the publisher
% TODO: compound surname(s) parsed mechanically - verify against the publisher page
@article{wafa2025advancing,
  author   = {Abeer A. Wafa and Mai M. Eldefrawi and Salah Farhan, Marwa},
  title    = {Advancing multimodal emotion recognition in big data through prompt engineering and deep adaptive learning},
  journal  = {Journal of Big Data},
  year     = {2025},
  volume   = {12},
  number   = {1},
  doi      = {10.1186/s40537-025-01264-w},
  url      = {https://doi.org/10.1186/s40537-025-01264-w},
  note     = {Research article; pool ID JoBD-3}
}
```

#### JoBD-4 · saleh2025cloud

```bibtex
% TODO: article number not indexed - verify at the publisher
@article{saleh2025cloud,
  author   = {Hager Saleh and Nora El-Rashidy and Sherif Mostafa and Abdulaziz AlMohimeed and Shaker El–Sappagh and Zainab H. Ali},
  title    = {Cloud based real-time multivariate multi-step prediction of systolic blood pressure and heart rate using temporal convolutional network and Apache Spark},
  journal  = {Journal of Big Data},
  year     = {2025},
  volume   = {12},
  number   = {1},
  doi      = {10.1186/s40537-025-01207-5},
  url      = {https://doi.org/10.1186/s40537-025-01207-5},
  note     = {Research article; pool ID JoBD-4}
}
```

#### JoBD-5 · zhang2025graph

```bibtex
% TODO: article number not indexed - verify at the publisher
@article{zhang2025graph,
  author   = {Han Zhang and Yun Zhou and Huahu Xu and Jiangang Shi and Xinhua Lin and Yiqin Gao},
  title    = {Graph neural network approach with spatial structure to anomaly detection of network data},
  journal  = {Journal of Big Data},
  year     = {2025},
  volume   = {12},
  number   = {1},
  doi      = {10.1186/s40537-025-01149-y},
  url      = {https://doi.org/10.1186/s40537-025-01149-y},
  note     = {Research article; pool ID JoBD-5}
}
```

#### AIR-1 · abouali2025agentic

```bibtex
% TODO: article number not indexed - verify at the publisher
% TODO: compound surname(s) parsed mechanically - verify against the publisher page
@article{abouali2025agentic,
  author   = {Abou Ali, Mohamad and Fadi Dornaika and Jinan Charafeddine},
  title    = {Agentic AI: a comprehensive survey of architectures, applications, and future directions},
  journal  = {Artificial Intelligence Review},
  year     = {2025},
  volume   = {59},
  number   = {1},
  doi      = {10.1007/s10462-025-11422-4},
  url      = {https://doi.org/10.1007/s10462-025-11422-4},
  note     = {Review article; pool ID AIR-1}
}
```

#### AIR-2 · edozie2025telecom

```bibtex
% TODO: article number not indexed - verify at the publisher
@article{edozie2025telecom,
  author   = {Enerst Edozie and Aliyu Nuhu Shuaibu and Bashir Olaniyi Sadiq and Ukagwu Kelechi John},
  title    = {Artificial intelligence advances in anomaly detection for telecom networks},
  journal  = {Artificial Intelligence Review},
  year     = {2025},
  volume   = {58},
  number   = {4},
  doi      = {10.1007/s10462-025-11108-x},
  url      = {https://doi.org/10.1007/s10462-025-11108-x},
  note     = {Review article; pool ID AIR-2}
}
```

#### AIR-3 · muneer2026classical

```bibtex
% TODO: article number not indexed - verify at the publisher
@article{muneer2026classical,
  author   = {Amgad Muneer and Muhammad Waqas and Maliazurina B. Saad and Eman Showkatian and Rukhmini Bandyopadhyay and Hui Xu},
  title    = {From classical machine learning to emerging foundation models: review on multimodal data integration for cancer research},
  journal  = {Artificial Intelligence Review},
  year     = {2026},
  volume   = {59},
  number   = {4},
  doi      = {10.1007/s10462-026-11522-9},
  url      = {https://doi.org/10.1007/s10462-026-11522-9},
  note     = {Review article; pool ID AIR-3}
}
```

#### AIR-4 · waseem2025synthetic

```bibtex
% TODO: article number not indexed - verify at the publisher
% TODO: compound surname(s) parsed mechanically - verify against the publisher page
@article{waseem2025synthetic,
  author   = {Hafiz Muhammad Waseem and ul Islam, Saif and Nicholas Matragkas and Gregory Epiphaniou and Theodoros N. Arvanitis and Carsten Maple},
  title    = {Review of generative AI for synthetic data generation: a healthcare perspective},
  journal  = {Artificial Intelligence Review},
  year     = {2025},
  volume   = {59},
  number   = {2},
  doi      = {10.1007/s10462-025-11440-2},
  url      = {https://doi.org/10.1007/s10462-025-11440-2},
  note     = {Review article; pool ID AIR-4}
}
```

#### AIR-5 · vats2026survey

```bibtex
% TODO: volume/issue not indexed yet (online first) - verify at SpringerLink
% TODO: article number not indexed - verify at the publisher
@article{vats2026survey,
  author   = {Vaishnavi Vats and Huisu Kim and Eduardo Linares and Young‐Kyoon Suh},
  title    = {A survey of deep multivariate time-series models with an empirical reproducibility audit},
  journal  = {Artificial Intelligence Review},
  year     = {2026},
  doi      = {10.1007/s10462-026-11674-8},
  url      = {https://doi.org/10.1007/s10462-026-11674-8},
  note     = {Review article; pool ID AIR-5}
}
```

## Appendix B — Reference strings, Springer Basic

Generated in the style the assignment requires: `Lastname FN (Year) Title. Journal Vol(Issue):pages. https://doi.org/…`. Don't retype these by hand — re-run the script after a swap. Clearing the Flags column is the references lead's checklist (author names are split mechanically, so compound surnames are flagged rather than guessed).

| ID | Reference string (Springer Basic) | Flags |
|---|---|---|
| TBD-1 | Jiang W, Chang CY, Huang TC, Chin YT, Sinha Roy D (2026) PEXP: A Scalable Parallel Tree-Based Framework for Interpreting Models on Big Data. IEEE Transactions on Big Data 12(4):1177–1194. https://doi.org/10.1109/tbdata.2026.3668673 | compound surname parsed mechanically - verify |
| TBD-2 | Wang H, Li Y, Zhu YC, Yan J, Ren L, Yang LT (2026) TS-MLLM: A Multi-Modal Large Language Model-based Framework for Industrial Time-Series Big Data Analysis. IEEE Transactions on Big Data [volume/pages to verify]. https://doi.org/10.1109/tbdata.2026.3695338 | verify volume/pages (online first) |
| TBD-3 | Chai Z, Zhang T, Wu L, Han K, Hu X, Huang X (2025) GraphLLM: Boosting Graph Reasoning Ability of Large Language Model. IEEE Transactions on Big Data 12(2):475–483. https://doi.org/10.1109/tbdata.2025.3627488 | — |
| TBD-4 | Xiao Z, Xing H, Qu R, Li H, Tong H, Luo S (2025) Knowledge Aggregation Transformer Network for Multivariate Time Series Classification. IEEE Transactions on Big Data 11(6):3413–3429. https://doi.org/10.1109/tbdata.2025.3594294 | — |
| TBD-5 | Gunbilek E, Akusta Dağdevıren Z, Bulut H (2026) Enhanced Approaches for Anomaly Detection in Streaming Data: Coupling Gaussian Distributions With Space Trees and Adaptive AutoEncoders. IEEE Transactions on Big Data 12(4):1318–1331. https://doi.org/10.1109/tbdata.2026.3679567 | compound surname parsed mechanically - verify |
| BDR-1 | Mohammadian H, Higgins G, Ansong S, Razavi‐Far R, Ghorbani AA (2025) Explainable malware detection through integrated graph reduction and learning techniques. Big Data Research 41:100555. https://doi.org/10.1016/j.bdr.2025.100555 | — |
| BDR-2 | Teixeira R, Almeida L, Antunes M, Gomes D, Aguiar RL (2025) Efficient training: Federated learning cost analysis. Big Data Research 40:100510. https://doi.org/10.1016/j.bdr.2025.100510 | — |
| BDR-3 | Ghodsi S, Moeini A (2026) Opinion fraud detection on massive datasets by spark. Big Data Research 43:100590. https://doi.org/10.1016/j.bdr.2026.100590 | — |
| BDR-4 | Liu Q, Qiu Y, Jia Y, Wang Y, Wu M (2026) Heterogeneous Graph-based Risk Assessment for Internet Financial Companies with Company Big Data. Big Data Research 45:100620. https://doi.org/10.1016/j.bdr.2026.100620 | — |
| BDR-5 | Li X, Liu J (2026) Large-scale least squares regression based on fast spectral embedding and random Fourier feature mapping. Big Data Research 43:100589. https://doi.org/10.1016/j.bdr.2026.100589 | — |
| JoBD-1 | Elfouly MK, Abdelaziz A, Gomaa WH, Abdalla M (2025) A deep learning-based framework for large-scale plant disease detection using big data analytics in precision agriculture. Journal of Big Data 12(1) [article no. to verify]. https://doi.org/10.1186/s40537-025-01265-9 | verify article number |
| JoBD-2 | Haripriya R, Khare N, Pandey M, Biswas S (2025) A privacy-enhanced framework for collaborative Big Data analysis in healthcare using adaptive federated learning aggregation. Journal of Big Data 12(1) [article no. to verify]. https://doi.org/10.1186/s40537-025-01169-8 | verify article number |
| JoBD-3 | Wafa AA, Eldefrawi MM, Salah Farhan M (2025) Advancing multimodal emotion recognition in big data through prompt engineering and deep adaptive learning. Journal of Big Data 12(1) [article no. to verify]. https://doi.org/10.1186/s40537-025-01264-w | verify article number; compound surname parsed mechanically - verify |
| JoBD-4 | Saleh H, El-Rashidy N, Mostafa S, AlMohimeed A, El–Sappagh S, Ali ZH (2025) Cloud based real-time multivariate multi-step prediction of systolic blood pressure and heart rate using temporal convolutional network and Apache Spark. Journal of Big Data 12(1) [article no. to verify]. https://doi.org/10.1186/s40537-025-01207-5 | verify article number |
| JoBD-5 | Zhang H, Zhou Y, Xu H, Shi J, Lin X, Gao Y (2025) Graph neural network approach with spatial structure to anomaly detection of network data. Journal of Big Data 12(1) [article no. to verify]. https://doi.org/10.1186/s40537-025-01149-y | verify article number |
| AIR-1 | Abou Ali M, Dornaika F, Charafeddine J (2025) Agentic AI: a comprehensive survey of architectures, applications, and future directions. Artificial Intelligence Review 59(1) [article no. to verify]. https://doi.org/10.1007/s10462-025-11422-4 | verify article number; compound surname parsed mechanically - verify; review article (AIR exception) |
| AIR-2 | Edozie E, Shuaibu AN, Sadiq BO, John UK (2025) Artificial intelligence advances in anomaly detection for telecom networks. Artificial Intelligence Review 58(4) [article no. to verify]. https://doi.org/10.1007/s10462-025-11108-x | verify article number; review article (AIR exception) |
| AIR-3 | Muneer A, Waqas M, Saad MB, Showkatian E, Bandyopadhyay R, Xu H (2026) From classical machine learning to emerging foundation models: review on multimodal data integration for cancer research. Artificial Intelligence Review 59(4) [article no. to verify]. https://doi.org/10.1007/s10462-026-11522-9 | verify article number; review article (AIR exception) |
| AIR-4 | Waseem HM, ul Islam S, Matragkas N, Epiphaniou G, Arvanitis TN, Maple C (2025) Review of generative AI for synthetic data generation: a healthcare perspective. Artificial Intelligence Review 59(2) [article no. to verify]. https://doi.org/10.1007/s10462-025-11440-2 | verify article number; compound surname parsed mechanically - verify; review article (AIR exception) |
| AIR-5 | Vats V, Kim H, Linares E, Suh Y (2026) A survey of deep multivariate time-series models with an empirical reproducibility audit. Artificial Intelligence Review [volume/pages to verify]. https://doi.org/10.1007/s10462-026-11674-8 | verify volume/pages (online first); verify article number; review article (AIR exception) |

## Appendix C — Alternates bench (29) and swap protocol

All 29 are Crossref-verified and held in `results/pool_selected.json`. Nothing here is cited in the paper — they are insurance against access failures and against the AIR review-article exception being rejected.

| ID | Title | Access | DOI | Held for |
|---|---|---|---|---|
| TBD-A1 | Big Data-Driven Advancements and Future Directions in Vehicle Perception Technologies: From Autonomous Driving to Modular Buses | PAID | [link](https://doi.org/10.1109/tbdata.2025.3527208) | General hold (vetted alternate) |
| TBD-A2 | Digital Twin Data Management: A Comprehensive Review | PAID | [link](https://doi.org/10.1109/tbdata.2025.3533891) | General hold (vetted alternate) |
| TBD-A3 | Ensemble Approaches for Dynamic Data Stream Classification Under Label Scarcity | PAID | [link](https://doi.org/10.1109/tbdata.2025.3570072) | General hold (vetted alternate) |
| TBD-A4 | A Fast Linearithmic Graph Clustering Approach for Big Data Using Gravitational Attraction Principle | PAID | [link](https://doi.org/10.1109/tbdata.2025.3639917) | General hold (vetted alternate) |
| TBD-A5 | SARF: Sparsity-Aware Reconstruction Framework for Large-Scale Datasets | OA | [link](https://doi.org/10.1109/tbdata.2025.3639968) | Designated swap for any TBD paywalled item (OA) |
| TBD-A6 | Hierarchical Multi-Relational Graph Representation Learning for Large-Scale Prediction of Drug-Drug Interactions | PAID | [link](https://doi.org/10.1109/tbdata.2025.3536924) | Research-only backup for TBD |
| BDR-A1 | Deep neural network modeling for financial time series analysis | OA | [link](https://doi.org/10.1016/j.bdr.2025.100553) | Swap if BDR-3/BDR-5 access fails (OA) |
| BDR-A2 | A novel approach for job matching and skill recommendation using transformers and the O*NET database | OA | [link](https://doi.org/10.1016/j.bdr.2025.100509) | Swap if BDR-3/BDR-5 access fails (OA) |
| BDR-A3 | Scalable QoS-aware cloud service composition for big data workflows: A model-driven MJAYA optimization approach | PAID | [link](https://doi.org/10.1016/j.bdr.2026.100629) | General hold (vetted alternate) |
| BDR-A4 | ImDMI: Improved Distributed M-Invariance model to achieve privacy continuous big data publishing using Apache Spark | PAID | [link](https://doi.org/10.1016/j.bdr.2025.100519) | General hold (vetted alternate) |
| BDR-A5 | Hybrid quantum GAN- integrated synthetic data generation with privacy-embedded attention framework for financial forecasting and risk analysis | PAID | [link](https://doi.org/10.1016/j.bdr.2026.100604) | General hold (vetted alternate) |
| BDR-A6 | Optimization of differential privacy mechanism for big data privacy protection | PAID | [link](https://doi.org/10.1016/j.bdr.2026.100634) | General hold (vetted alternate) |
| JoBD-A1 | A hybrid deep learning–blockchain framework for reliable fraud detection: a big data–driven approach for real-time FinTech systems | OA | [link](https://doi.org/10.1186/s40537-026-01506-5) | General hold (vetted alternate) |
| JoBD-A2 | Artificial Intelligence-driven privacy preservation in the internet of vehicles: a comprehensive systematic literature review | OA | [link](https://doi.org/10.1186/s40537-025-01360-x) | General hold (vetted alternate) |
| JoBD-A3 | A systematic literature study of machine learning techniques based intrusion detection: datasets, models, challenges, and future directions | OA | [link](https://doi.org/10.1186/s40537-025-01323-2) | General hold (vetted alternate) |
| JoBD-A4 | BlueEdge: application design for big data cleaning processing using mobile edge computing environments | OA | [link](https://doi.org/10.1186/s40537-025-01262-y) | General hold (vetted alternate) |
| JoBD-A5 | Data science, big data, and machine learning are coming of age | OA | [link](https://doi.org/10.1186/s40537-025-01172-z) | General hold (vetted alternate) |
| JoBD-A6 | Comprehensive review of artificial intelligence applications in renewable energy systems: current implementations and emerging trends | OA | [link](https://doi.org/10.1186/s40537-025-01178-7) | General hold (vetted alternate) |
| JoBD-A7 | Towards precision in IoT-based healthcare systems: a hybrid optimized framework for big data classification | OA | [link](https://doi.org/10.1186/s40537-025-01243-1) | General hold (vetted alternate) |
| AIR-A1 | Agentic AI systems in the age of generative models: architectures, cloud scalability, and real-world applications | OA | [link](https://doi.org/10.1007/s10462-025-11458-6) | General hold (vetted alternate) |
| AIR-A2 | Safeguarding large language models: a survey | OA | [link](https://doi.org/10.1007/s10462-025-11389-2) | General hold (vetted alternate) |
| AIR-A3 | Graph neural networks for anomaly detection: a systematic review of dynamic temporal approaches | OA | [link](https://doi.org/10.1007/s10462-026-11532-7) | General hold (vetted alternate) |
| AIR-A4 | Synergizing blockchain and AI to fortify IoT security: a comprehensive review | OA | [link](https://doi.org/10.1007/s10462-025-11434-0) | General hold (vetted alternate) |
| AIR-A5 | Artificial intelligence for weather and climate: a survey of methods, benchmarks, and scientific machine learning challenges | OA | [link](https://doi.org/10.1007/s10462-026-11690-8) | General hold (vetted alternate) |
| AIR-A6 | Physics-informed machine learning for advancing computational medical imaging: integrating data-driven approaches with fundamental physical principles | OA | [link](https://doi.org/10.1007/s10462-025-11303-w) | Research-only insurance if the AIR review exception is rejected |
| AIR-A7 | Exploring privacy mechanisms and metrics in federated learning | OA | [link](https://doi.org/10.1007/s10462-025-11170-5) | Research-only insurance if the AIR review exception is rejected |
| AIR-A8 | Scaling transformers for time series forecasting: do pretrained large models outperform small-scale alternatives? | OA | [link](https://doi.org/10.1007/s10462-025-11481-7) | Research-only insurance if the AIR review exception is rejected |
| AIR-A9 | XAI-HD: an explainable artificial intelligence framework for heart disease detection | OA | [link](https://doi.org/10.1007/s10462-025-11385-6) | Research-only insurance if the AIR review exception is rejected |
| AIR-A10 | Cloud-edge-end collaborative caching and UAV-assisted offloading decision based on the fusion of deep reinforcement learning algorithms | OA | [link](https://doi.org/10.1007/s10462-025-11391-8) | Research-only insurance if the AIR review exception is rejected |

**Swap protocol** — only the integration editor approves a swap: use the alternate named for that journal in `Held for` first · check it against the same criteria as the original in `notes/selection-backing.md` · keep the branch balance above intact (like branch for like branch) · re-run `python code/build_tracker.py` so this page, the BibTeX and the CSVs pick the swap up · update `trackers/papers-pool.md` and the session log, then re-import this page into Notion.

## Appendix D — Column dictionary

Who fills what, and with which words. Anything not listed here stays free text, one line per cell.

| Column | Allowed values / format | Owner |
|---|---|---|
| ID | TBD-1 … TBD-5, BDR-1 … BDR-5, JoBD-1 … JoBD-5, AIR-1 … AIR-5 — never changes | fixed |
| Reader | member name (pod leads assign, at least 2 papers per member) | pod lead |
| Read status | Not started · Skimmed · Read · Deep-read | reader |
| Method / platform | what the paper builds and the platform it runs on (Spark, streaming, fog/cloud, cluster …) | reader |
| Dataset & scale | named datasets with scale: rows, GB, nodes, patients, streams | reader |
| Headline result | the paper's main number, with the metric and the baseline it beats | reader |
| Limitations (theirs / ours) | authors' admitted limits, then ours: weak baselines, no statistical tests, unevidenced scale claims | reader |
| Draft § | §3.3 methods · §3.4 platforms · §3.5 applications · §3.6 cross-cutting · §3.7 future (per `paper/outline.md`) | theme lead |
| S2 · S5 | 0 · 1 · 2 each: S2 method described well enough to reproduce, S5 relevance to this review | reader |
| Notes | unique contribution, or the quotable line with page/section; agreement or contradiction with another pool ID | theme lead |
| Branch | B1 scalable/interpretable methods · B2 platforms/infrastructure · B3 applications/domains · B4 foundation models/LLMs · B5 privacy/governance/evaluation | taxonomy lead |
| Dates | ISO YYYY-MM-DD | all |

`†` marks abstract-level values — verify against the full text. `—` means not yet filled: leave it empty rather than guessing.

## Revision log

Newest first. Add a row for every swap, import or structural change.

| Rev | Date | Change | By |
|---|---|---|---|
| 2 | 2026-09-22 | Tracker populated from the 20 source notes: R1 working columns (Method/platform, Dataset & scale, Headline result, Limitations, Draft §, S2 · S5, Notes) filled for the 17 empty rows; R2 claim-to-evidence ledger seeded with 21 claims (C-01…C-21); Draft § mapping applied per branch map (B1/B4→§3.3, B2→§3.4, B3→§3.5, B5→§3.6; straddler overrides TBD-2/TBD-3→§3.5, JoBD-2→§3.6, JoBD-3→§3.5). | workspace automation |
| 1 | 2026-09-15 | Tracker created from pool rev 3 (20 selected + 29 alternates): single master table for the team, claim ledger, BibTeX, Springer Basic reference strings, alternates bench. | workspace automation |

