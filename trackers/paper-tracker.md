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
| TBD-1 | [PEXP: A Scalable Parallel Tree-Based Framework for Interpreting Models on Big Data](https://doi.org/10.1109/tbdata.2026.3668673) | 2026 | IEEE TBD · research | PAID — institutional access | — | — | — | tree-based parallel model interpretation · big data; parallel framework † | — | — | — | — | — | — |
| TBD-2 | [TS-MLLM: A Multi-Modal Large Language Model-based Framework for Industrial Time-Series Big Data Analysis](https://doi.org/10.1109/tbdata.2026.3695338) | 2026 | IEEE TBD · research | PAID — institutional access | — | — | — | multimodal LLM framework for industrial time-series analysis (PHM) · industrial time-series big data (explicit in title) † | — | — | — | — | — | — |
| TBD-3 | [GraphLLM: Boosting Graph Reasoning Ability of Large Language Model](https://doi.org/10.1109/tbdata.2025.3627488) | 2025 | IEEE TBD · research | PAID — institutional access | — | — | — | LLM for graph reasoning · graph-structured large data † | — | — | — | — | — | — |
| TBD-4 | [Knowledge Aggregation Transformer Network for Multivariate Time Series Classification](https://doi.org/10.1109/tbdata.2025.3594294) | 2025 | IEEE TBD · research | OA (green) | — | — | — | transformer for multivariate time series classification · high-volume sensor/time-series data † | — | — | — | — | — | — |
| TBD-5 | [Enhanced Approaches for Anomaly Detection in Streaming Data: Coupling Gaussian Distributions With Space Trees and Adaptive AutoEncoders](https://doi.org/10.1109/tbdata.2026.3679567) | 2026 | IEEE TBD · research | PAID — institutional access | — | — | — | statistical + ML anomaly detection · data streams (velocity) † | — | — | — | — | — | — |
| BDR-1 | [Explainable malware detection through integrated graph reduction and learning techniques](https://doi.org/10.1016/j.bdr.2025.100555) | 2025 | Big Data Research · research | OA (hybrid) | — | — | — | graph reduction + learning, explainable malware detection · large malware corpora † | — | — | — | — | — | — |
| BDR-2 | [Efficient training: Federated learning cost analysis](https://doi.org/10.1016/j.bdr.2025.100510) | 2025 | Big Data Research · research | OA (hybrid) | — | — | — | federated learning training-cost analysis · distributed/edge training † | — | — | — | — | — | — |
| BDR-3 | [Opinion fraud detection on massive datasets by spark](https://doi.org/10.1016/j.bdr.2026.100590) | 2026 | Big Data Research · research | PAID — institutional access | — | — | — | fraud detection ML on Spark · massive datasets; Spark cluster † | — | — | — | — | — | — |
| BDR-4 | [Heterogeneous Graph-based Risk Assessment for Internet Financial Companies with Company Big Data](https://doi.org/10.1016/j.bdr.2026.100620) | 2026 | Big Data Research · research | OA (green) | — | — | — | heterogeneous graph-based risk assessment · company big data (explicit in title) † | — | — | — | — | — | — |
| BDR-5 | [Large-scale least squares regression based on fast spectral embedding and random Fourier feature mapping](https://doi.org/10.1016/j.bdr.2026.100589) | 2026 | Big Data Research · research | PAID — institutional access | — | — | — | fast spectral embedding + random Fourier features regression · large-scale data † | — | — | — | — | — | — |
| JoBD-1 | [A deep learning-based framework for large-scale plant disease detection using big data analytics in precision agriculture](https://doi.org/10.1186/s40537-025-01265-9) | 2025 | Journal of Big Data · research | OA (gold) | — | — | — | deep learning framework for large-scale plant disease detection · big data analytics in precision agriculture (explicit in title) † | — | — | — | — | — | — |
| JoBD-2 | [A privacy-enhanced framework for collaborative Big Data analysis in healthcare using adaptive federated learning aggregation](https://doi.org/10.1186/s40537-025-01169-8) | 2025 | Journal of Big Data · research | OA (gold) | — | — | — | adaptive privacy-preserving collaborative analytics · healthcare big data † | — | — | — | — | — | — |
| JoBD-3 | [Advancing multimodal emotion recognition in big data through prompt engineering and deep adaptive learning](https://doi.org/10.1186/s40537-025-01264-w) | 2025 | Journal of Big Data · research | OA (gold) | — | — | — | GAN + dynamic prompt engineering, multimodal deep learning · multimodal big data (explicit in title) † | — | — | — | — | — | — |
| JoBD-4 | [Cloud based real-time multivariate multi-step prediction of systolic blood pressure and heart rate using temporal convolutional network and Apache Spark](https://doi.org/10.1186/s40537-025-01207-5) | 2025 | Journal of Big Data · research | OA (gold) | — | — | — | temporal convolutional network (TCN) multi-step forecasting · fog/cloud streaming pipeline with Apache Spark (explicit in title) † | — | — | — | — | — | — |
| JoBD-5 | [Graph neural network approach with spatial structure to anomaly detection of network data](https://doi.org/10.1186/s40537-025-01149-y) | 2025 | Journal of Big Data · research | OA (gold) | — | — | — | GNN anomaly detection · network traffic data † | — | — | — | — | — | — |
| AIR-1 | [Agentic AI: a comprehensive survey of architectures, applications, and future directions](https://doi.org/10.1007/s10462-025-11422-4) | 2025 | AI Review · review | OA (hybrid) | [PDF](https://github.com/ihmorol/big-data-ml-review/blob/main/papers/AIR/AIR-1_AbouAli_2025_AgenticAI.pdf) | Ikramul Hasan | Read | symbolic agents (MDP/POMDP, BDI, SOAR) vs neural agents (LLM orchestration — LangChain, AutoGen, CrewAI, RAG) · no platform — conceptual survey, but flags the cloud-compute bill | No datasets — survey. Evidence base: 90 papers (78 core + 12 seminal), Jan 2018–Mar 2025, PRISMA 2020 | Two paradigms, not one: symbolic (planners, BDI/SOAR) vs neural/generative (LLM orchestration). Domain decides the pick — symbolic/hybrid in safety-critical work (healthcare, legal), neural in data-rich fields (finance, education); neuro-symbolic is the proposed way forward | Theirs: search stops Mar 2025 · 12 of 90 studies added outside the PRISMA flow · proprietary systems under-documented / Ours: taxonomy asserted, not tested · "all 90 studies fit" is self-reported · no cost numbers behind the compute warning | §3.5 · §3.7 | 1 · 2 | "symbolic and hybrid architectures dominate safety-critical applications like healthcare and robotics, while pure neural systems thrive in data-rich, adaptive domains such as finance and education." (p. 24) |
| AIR-2 | [Artificial intelligence advances in anomaly detection for telecom networks](https://doi.org/10.1007/s10462-025-11108-x) | 2025 | AI Review · review | OA (hybrid) | [PDF](https://github.com/ihmorol/big-data-ml-review/blob/main/papers/AIR/AIR-2_Edozie_2025_TelecomAnomalyDetection.pdf) | Ikramul Hasan | Read | classical ML (Isolation Forest, k-NN, LOF, XGBoost) → deep learning (LSTM, autoencoders, VAE, MSCRED, DeepAnT, Telemanom) → GNNs, transformers, federated learning, XAI · no platform used; Hadoop/Spark mentioned as history only | No datasets of their own (stated p. 33): 3,084 screened → 160 included. Five dataset categories described (5G streams, sensor telemetry, security logs, traffic logs, synthetic) — no benchmark named, no sizes | Rule-based detection is obsolete; deep learning reports 85–97% accuracy but pays in latency (autoencoders 2,000–7,000 ms vs Isolation Forest 100–400 ms). The real blocker is deployment — compute cost, edge latency, model drift — not accuracy | Theirs: no data of their own · label scarcity and class imbalance · model drift and retraining cost · edge latency vs model size / Ours: accuracy ranges tied to no named dataset · no baselines · no volume numbers behind the "big data" framing · no LLM coverage · reference years contain typos | §3.5 · §3.6 | 1 · 2 | "Traditional methods of anomaly detection, which rely on rule-based systems, are no longer effective in today's fast-evolving telecom landscape." (p. 1) |
| AIR-3 | [From classical machine learning to emerging foundation models: review on multimodal data integration for cancer research](https://doi.org/10.1007/s10462-026-11522-9) | 2026 | AI Review · review | OA (hybrid) | [PDF](https://github.com/ihmorol/big-data-ml-review/blob/main/papers/AIR/AIR-3_Muneer_2026_MultimodalFoundationModelsCancer.pdf) | Ikramul Hasan | Read | classical ML (SVM/RF) → deep latent fusion (CNN/VAE/GNN) → foundation models (scGPT, OmniCLIP, Nicheformer) · multimodal cancer big data (omics, WSIs, radiology, EHR) | No primary data — review. Evidence base: 54 core studies (PRISMA: 3,280 screened → 54 included) + taxonomy of FMs (scGPT >33M cells, Nicheformer 110M cells, OmniCLIP 2.2M paired tissue images) | Intermediate and attention-based latent fusions significantly outperform early/late fusion in survival and metastasis prediction; foundation models enable few-shot learning for rare cancers; severe translational gap (>90% retrospective; near-zero prospective trials/approvals) | Theirs: extreme data heterogeneity and missing modalities in real clinics · high compute/GPU cost · lack of mechanistic interpretability · near-zero prospective trials or FDA clearances / Ours: 69-page secondary survey with no standardized experimental baselines · unharmonized metrics · oncology-specific framing | §3.3 · §3.5 | 1 · 2 | "The performance, reliability, and ultimate clinical utility of any AI model are inextricably bound to the fidelity, structure, and integrity of the data upon which it is trained." (p. 46) |
| AIR-4 | [Review of generative AI for synthetic data generation: a healthcare perspective](https://doi.org/10.1007/s10462-025-11440-2) | 2025 | AI Review · review | OA (hybrid) | [PDF](https://github.com/ihmorol/big-data-ml-review/blob/main/papers/AIR/AIR-4_Waseem_2025_SyntheticDataHealthcare.pdf) | — | — | generative AI synthetic data (review) · healthcare data scarcity/privacy † | — | — | — | — | — | — |
| AIR-5 | [A survey of deep multivariate time-series models with an empirical reproducibility audit](https://doi.org/10.1007/s10462-026-11674-8) | 2026 | AI Review · review | OA (hybrid) | [PDF](https://github.com/ihmorol/big-data-ml-review/blob/main/papers/AIR/AIR-5_Vats_2026_DeepMultivariateTimeSeriesSurvey.pdf) | — | — | deep multivariate TS models + reproducibility audit · multivariate time series at scale † | — | — | — | — | — | — |

Cell rules: name datasets with their scale (rows, GB, nodes) — "large-scale" alone is not evidence · list the baselines the authors compared against, since "no baseline" is itself a finding · keep every number that produces the headline result.

## R2 — Claim-to-evidence ledger

Append a row for every number, comparison or "first/only" claim in the manuscript: which paper backs it, where exactly, and who checked it. The row below is the format — replace it as real claims appear. Status flow: `Draft` → `Checked` (a second member opened the source and found the number) → `Frozen` (in the submitted text). Abstract-only backing is fine for a description, never for a number.

| Claim ID | Claim (as written) | Backing paper(s) | Evidence (number + page/section) | Used in draft (§) | Checked by | Status |
|---|---|---|---|---|---|---|
| C-01 | one-sentence claim, exactly as it will appear in the draft | TBD-1 | measured value + page | §3.3 | reviewer name | Draft |

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
| 1 | 2026-09-15 | Tracker created from pool rev 3 (20 selected + 29 alternates): single master table for the team, claim ledger, BibTeX, Springer Basic reference strings, alternates bench. | workspace automation |

