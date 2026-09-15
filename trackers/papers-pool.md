# Papers pool — LOCKED rev 2 (2026-09-15): 20 selected, verified; 24 alternates held

Built by programmatic retrieval (OpenAlex full 2025+ output per journal, 1,519 works screened) + two cross-check agents, then Crossref-verified per paper. Full metadata/abstracts: `../results/pool_selected.json`; Table 1 data: `../results/table1.csv`; per-paper reading notes: `../sources/`; synthesis: `../notes/landscape-report.md`; **requirement-by-requirement backing for every selection: `../notes/selection-backing.md`**.

**Access key:** OA = freely readable · PAID = institutional access needed (no free copy or preprint found; see swap rule below).

## Journal 1 — IEEE Transactions on Big Data (SCIE, IF 8.1)

| # | Paper (first author et al., year) | Theme | Access | Verified |
|---|---|---|---|---|
| TBD-1 | PEXP: A Scalable Parallel Tree-Based Framework for Interpreting Models on Big Data (2026) | Scalable & interpretable ML | PAID | ✓ |
| TBD-2 | Blockchain-Empowered Federated Learning: Benefits, Challenges, and Solutions (2025) | Federated & privacy | PAID | ✓ |
| TBD-3 | GraphLLM: Boosting Graph Reasoning Ability of Large Language Model (2025/26) | LLMs & foundation models | PAID | ✓ |
| TBD-4 | Knowledge Aggregation Transformer Network for Multivariate Time Series Classification (2025) | Time series & streaming | **OA** | ✓ |
| TBD-5 | Enhanced Approaches for Anomaly Detection in Streaming Data (2026) | Security & anomaly detection | PAID | ✓ |

**Alternates (vetted, verified):** TBD-A1 Vehicle Perception Technologies review (c18) · TBD-A2 Digital Twin Data Management review (c23) · TBD-A3 Ensemble Approaches for Dynamic Data Stream Classification · TBD-A4 Fast Linearithmic Graph Clustering for Big Data · TBD-A5 SARF: Sparsity-Aware Reconstruction (**OA — designated swap for any TBD paywalled item**) · TBD-A6 TS-MLLM: Multi-Modal LLM for Industrial Time-Series Big Data (explicit "Big Data" + LLM title — compliance swap candidate)

## Journal 2 — Big Data Research (SCIE, IF 4.6)

| # | Paper | Theme | Access | Verified |
|---|---|---|---|---|
| BDR-1 | Explainable malware detection through integrated graph reduction and learning (2025) | Security & explainability | **OA** | ✓ |
| BDR-2 | Efficient training: Federated learning cost analysis (2025) | Federated & energy/cost | **OA** | ✓ |
| BDR-3 | Opinion fraud detection on massive datasets by spark (2026) | Platforms (Spark) | PAID | ✓ |
| BDR-4 | Heterogeneous Graph-based Risk Assessment for Internet Financial Companies with Company Big Data (2026) | Applications & finance | **OA** | ✓ |
| BDR-5 | Large-scale least squares regression via fast spectral embedding + random Fourier features (2026) | Scalable ML | PAID | ✓ |

**Alternates:** BDR-A1 Deep NN financial time series (**OA**, c7) · BDR-A2 Job matching/skill recommendation with transformers (**OA**, c13) · BDR-A3 Scalable QoS-aware cloud service composition for big data workflows · BDR-A4 ImDMI distributed privacy publishing · BDR-A5 Hybrid quantum GAN synthetic data generation · BDR-A6 Optimization of differential privacy mechanism for big data (moved from selection, rev 1)
**Swap rule:** if BDR-3 or BDR-5 access fails → swap in BDR-A1/BDR-A2 (both OA) and re-balance themes in the report.

## Journal 3 — Journal of Big Data (SCIE, IF 10.8; all OA)

| # | Paper | Theme | Access | Verified |
|---|---|---|---|---|
| JoBD-1 | Big Data Analytics in IoT, social media, NLP, and information security (2025) | Multi-domain survey + benchmark | OA | ✓ |
| JoBD-2 | Privacy-enhanced collaborative Big Data analysis in healthcare (2025) | Healthcare + privacy | OA | ✓ |
| JoBD-3 | Advancing multimodal emotion recognition in big data through prompt engineering and deep adaptive learning (2025) | Applications & multimedia | OA | ✓ |
| JoBD-4 | Cloud-based real-time multivariate multi-step prediction of SBP and HR (2025) | Healthcare + fog/cloud streaming | OA | ✓ |
| JoBD-5 | Graph neural network with spatial structure for network anomaly detection (2025) | GNN anomaly detection | OA | ✓ |

**Alternates:** JoBD-A1 Secure hybrid DL brain-tumor framework (c41) · JoBD-A2 AI privacy preservation in IoV review · JoBD-A3 ML-based intrusion detection systematic review (c13) · JoBD-A4 BlueEdge edge-computing data cleaning · JoBD-A5 "Data science, big data and ML coming of age" (position piece — good Intro framing citation) · JoBD-A6 Comprehensive review of AI in renewable energy systems (c86 — moved from selection, rev 1) · JoBD-A7 DL framework for large-scale plant disease detection using big data analytics (c14)

## Journal 4 — Artificial Intelligence Review (SCIE, IF 18.8; all OA; also our format target)

| # | Paper | Theme | Access | Verified |
|---|---|---|---|---|
| AIR-1 | Agentic AI: a comprehensive survey of architectures, applications, and future directions (2025) | Agentic AI | OA | ✓ |
| AIR-2 | AI advances in anomaly detection for telecom networks (2025) | Telecom anomaly detection | OA | ✓ |
| AIR-3 | From classical ML to emerging foundation models: multimodal data integration (2026) | Foundation models | OA | ✓ |
| AIR-4 | Review of generative AI for synthetic data generation: a healthcare perspective (2025) | Data quality & governance | OA | ✓ |
| AIR-5 | Survey of deep multivariate time-series models with an empirical reproducibility audit (2026) | Evaluation & reproducibility | OA | ✓ |

**Alternates:** AIR-A1 Agentic AI systems: architectures, cloud scalability (c23) · AIR-A2 Safeguarding LLMs survey (c72) · AIR-A3 GNN anomaly detection systematic review · AIR-A4 Blockchain+AI IoT security review · AIR-A5 AI for weather and climate survey

## Notes for the team

- **Rev 2 reselection (2026-09-15):** BDR-4 and JoBD-3 were swapped for stronger requirement evidence (see `../notes/selection-backing.md`, "Reselection changelog"); the other 18 were re-audited and kept.
- **Do not substitute silently.** If a paper must be swapped, use its vetted alternate from this file and note the swap in `writing-progress.md`.
- **Three BDR papers (BDR-3/4/5) have no indexed abstracts** — their first reading task is extracting problem/method/evaluation from the full text (BDR-4 is open access; BDR-3/5 need institutional access).
- Every selected paper has a pre-filled note in `sources/` (bibliography, access status, abstract, theme). Complete the Synthesis hooks section when you read it.
- Citation counts (OpenAlex, 2026-09-15) are recorded in `results/pool_selected.json` for the impact criterion justification.
