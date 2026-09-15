# Selection backing — the 20 papers against every assignment requirement

Re-analysis of `Big Data Assignment.pdf` performed 2026-09-15 (raw + layout extraction, marks table and page metadata re-checked). Companion documents: pool tracker `../trackers/papers-pool.md`, synthesis `./landscape-report.md`, machine-readable metadata `../results/pool_selected.json`, Table 1 data `../results/table1.csv`, reading notes `../sources/`.

## 1. Requirement inventory (clause by clause)

| ID | Requirement (as written in the PDF) | Status | How satisfied |
|---|---|---|---|
| R1 | Assignment type: Artificial Intelligence Review Paper | satisfied | Whole workspace is scoped to this; no experimental component required |
| R2 | Proposed title: "Big Data with Machine Learning: A Review" | satisfied | Title used verbatim in outline/report; final paper keeps it |
| R3 | Keywords: Machine Learning, Big Data | satisfied | Fixed keyword list carried in outline; must appear on the final title page |
| R4 | Review period: 2025–2027 | satisfied | All 20 papers published 2025–2026; zero 2027-dated items exist in any of the four journals (verified against full journal pulls, 2026-09-15) |
| R5 | At least 20 research papers | satisfied | Exactly 20 selected; 15/15 selections from TBD, BDR, and JoBD are original research articles; AIR's 5 review articles are a documented exception (interpretation 2) |
| R6 | Selected from the four designated journals only | satisfied | Pool built by pulling each journal's *complete* 2025+ output by source ID, not by open web search — venue drift is structurally impossible |
| R7 | Approximately 3–5 papers per source | satisfied | Exactly 5 per journal |
| R8 | Criterion: relevance to Big Data **and** Machine Learning | satisfied | Per-paper evidence in Sect. 4; both dimensions evidenced for every paper (title/abstract for 17; title-level for 3, flagged with extraction tasks) |
| R9 | Criterion: published during 2025–2027 | satisfied | See R4 |
| R10 | Preferably indexed in Web of Science | satisfied | All four journals are SCIE-indexed (verified via wos-journal.info + publisher pages; all Q1 by SJR) |
| R11 | Preferably published in high-impact journals | satisfied | IFs: AIR 18.8 > JoBD 10.8 > IEEE TBD 8.1 > BDR 4.6; paper-level citations recorded as secondary evidence |
| R12 | Follow AIR publication format and structure | in progress | `../paper/outline.md` follows AIR section anatomy; final formatting pass Sep 25–26 |
| R13 | Proper literature review: synthesize, compare, critically analyze — not summaries | in progress | Landscape report delivers the synthesis (branches, comparison tables, tensions, gaps); drafting follows it |
| R14 | Components: Abstract, Introduction, Literature Review, Tables and Figures, Conclusion, References | in progress | All six mapped in outline + traceability (Sect. 3) |
| R15 | Formatting, organization, citation style, presentation aligned with AIR | in progress | Springer Basic (numeric, brackets) confirmed for AIR; reference style rules recorded in `./requirements.md` |
| R16 | Marks: Abstract 2, Intro 3, LR 10, T&F 3, Conclusion 2, Formatting 2, References 3 (= 25) | tracked | Per-component owners + status in `../trackers/writing-progress.md` |
| R17 | Deadline: September 27, 2026 | tracked | Timeline in `../trackers/team-tasks.md`; internal freeze Sep 26 |
| R18 | Group size: maximum 10 members | satisfied | Team of 8 |
| R19 | Assignment weight: 25% | noted | No action; informs effort allocation (LR = 40% of marks) |

### Interpretation notes (decisions taken where the PDF is not fully explicit)

1. **R5 + R7 arithmetic.** "At least 20" from four journals at "3–5 each" is satisfiable only at 5+5+5+5=20. Getting more than 20 would require papers from outside the four journals, which R6 forbids. Hence exactly 5 per journal is forced, and this pool is maximal.
2. **"Research papers" (R5) — supervisor clarification.** The supervisor clarified (relayed by the team, 2026-09-15) that "research papers" means **original research articles**, not reviews or surveys. Enforcement: all fifteen selections from IEEE TBD, Big Data Research, and Journal of Big Data are original research articles — the rev-2 survey selections (TBD-2 blockchain-FL survey, JoBD-1 multi-domain benchmark survey) were replaced in rev 3. The five Artificial Intelligence Review selections remain review articles as an **approved, documented exception**: AIR is a review-designated journal (294 of its 549 articles in the 2025+ window are review-type), the assignment designates AIR both as a source and as the format template, and the team decided to keep them. Insurance: five original-research AIR articles are pre-verified in the alternate pool (AIR-A6…A10) as ready drop-in replacements if the exception is rejected.
3. **R9 and 2027.** As of the submission date no 2027-dated article exists in any of the four journals (all four publishers' complete 2025+ output was pulled and dated: zero 2027 items). The period is therefore satisfied as far as physically possible; add one sentence to the paper's methodology stating this (already drafted in the landscape report).
4. **R10 at article level.** WoS indexing is verified at journal level (Master Journal List is not machine-accessible; secondary sources + publisher pages used). Individual articles in SCIE journals inherit indexing; IEEE early-access items (TBD-1, TBD-3, TBD-5) are indexed upon issue assignment (Crossref confirms issue-year 2026).
5. **R11 evidence tiers.** "High-impact" is primarily a journal property (R11 says "journals"); paper-level citation counts (OpenAlex, 2026-09-15) are recorded as supporting signal only, never as the selection driver.

## 2. Compliance summary

### 2.1 Per journal

| Journal | Selected | Years | Types | OA | SCIE | IF |
|---|---|---|---|---|---|---|
| IEEE Transactions on Big Data | 5 (TBD-1…5) | 2025 ×2, 2026 ×3 | 5 original research | 1/5 | yes | 8.1 |
| Big Data Research | 5 (BDR-1…5) | 2025 ×2, 2026 ×3 | 5 research | 3/5 | yes | 4.6 |
| Journal of Big Data | 5 (JoBD-1…5) | 2025 ×5 | 5 original research | 5/5 | yes | 10.8 |
| Artificial Intelligence Review | 5 (AIR-1…5) | 2025 ×3, 2026 ×2 | 5 review articles (approved exception — interpretation 2) | 5/5 | yes | 18.8 |

### 2.2 Corpus composition

- 15 original research articles; 5 review articles (all AIR, approved exception — interpretation 2).
- Publication window: 2025-01 → 2026-09; 12 papers from 2025, 8 from 2026.
- Access: 14 open access, 6 paywalled (TBD-1, TBD-2, TBD-3, TBD-5, BDR-3, BDR-5) with designated OA swaps.
- Theme spread (landscape-report branches): scalable methods 5 · applications 5 · foundation models/LLM 4 · platforms 3 · privacy/governance/evaluation 3.
- Domain spread: healthcare (2), security/anomaly detection (4), finance (1), affective computing (1), agriculture (1), industrial systems (1), plus methods/infrastructure (10).

## 3. Requirement → paper-component traceability

What each required section must carry and where it is maintained in this workspace.

| Paper component (marks) | Requirements it must carry | How maintained | Artifact |
|---|---|---|---|
| Abstract (2%) | R1–R4, R8, R13 | Review framing; scope = 20 papers/4 journals/period; keywords list "Machine Learning, Big Data" on title page | outline, landscape-report abstract |
| Introduction (3%) | R4, R6, R8–R11, R13 | Context; scope + selection criteria statement (four journals, 5 each, WoS, impact); organization preview; 2027-availability note | outline §2; landscape-report Sect. 2 |
| Literature Review (10%) | R13 (core), R8, R14 | Thematic synthesis: taxonomy, five branches with in-sentence comparison, comparison tables, tensions, gaps — never per-paper summaries | landscape-report Sects. 3–9 |
| Tables and Figures (3%) | R14, R5–R7, R8 | Table 1 = all 20 with venue/year/theme/methods/scale columns; Table 2 = theme×paper matrix; Fig. 1 selection flow demonstrates R6/R9/R10; Fig. 2 taxonomy; Fig. 3 distributions | results/table1.csv; figures/ |
| Conclusion (2%) | R13, R12 | Synthesis answers (state of methods/platforms/applications/challenges), takeaways, review-scope limits | outline §5; landscape-report Sect. 10–11 |
| References (3%) | R5, R6, R10, R15 | 20 primary references, Springer Basic numeric-bracket style, every entry Crossref-verified, in-text/extract consistency | results/pool_selected.json; sources/ |
| Formatting (2%) | R12, R15 | AIR structure, Springer Basic citation style, section anatomy, figure/table captions | trackers/writing-progress.md checklist |

## 4. Per-paper backing

Format per entry: citation (type | access | verification) → R8 relevance (Big Data / Machine Learning evidence) → R9 date → R10/R11 venue facts → role in the review → action/risk.

### IEEE Transactions on Big Data — 5/5 compliant (5 original research; 1 OA)

**[1] TBD-1** — Jiang W, et al (2026) PEXP: A Scalable Parallel Tree-Based Framework for Interpreting Models on Big Data. IEEE Trans Big Data 12. DOI 10.1109/tbdata.2026.3668673. (research | paid | Crossref ✓)
- **R8 — BD:** "big data" is in the title; abstract frames the problem as interpretation "applied to models trained on large-scale datasets". **ML:** interpretable machine learning for (deep) learning models; parallel tree-based explainer.
- **R9:** 2026 (early access 2025). **R10:** IEEE TBD, SCIE. **R11:** journal IF 8.1; 3 citations to date.
- **Role:** branch 4 anchor for scalable *interpretability* — the corpus's only paper treating explanation cost as the bottleneck. **Action:** paywalled — access request; content runs abstract-level until then.

**[2] TBD-2** — Wang H, et al (2026) TS-MLLM: A Multi-Modal Large Language Model-based Framework for Industrial Time-Series Big Data Analysis. IEEE Trans Big Data. DOI 10.1109/tbdata.2026.3695338. (original research | paid | Crossref ✓)
- **R8 — BD:** "Industrial Time-Series Big Data" in the title; the abstract frames equipment prognostics and health management as the task. **ML:** a unified multimodal LLM jointly modeling temporal signals, frequency-domain visual representations, and textual knowledge — per the abstract, the first to model all three jointly.
- **R9:** 2026. **R10:** SCIE. **R11:** journal IF 8.1 (recent; citations pending).
- **Role:** branch 7's industrial-systems method paper — the corpus's only LLM-augmented industrial big-data framework. Replaced the rev-2 blockchain-FL survey for the original-research-only clarification. **Action:** paywalled — access request; content runs abstract-level until then.

**[3] TBD-3** — Chai Z, et al (2025) GraphLLM: Boosting Graph Reasoning Ability of Large Language Model. IEEE Trans Big Data 12. DOI 10.1109/tbdata.2025.3627488. (research | paid | Crossref ✓)
- **R8 — BD:** abstract states graph data is "ubiquitous in Big Data applications such as social networks, knowledge graphs, and molecular databases". **ML:** LLM reasoning; Graph2Text bottleneck identified and restructured.
- **R9:** 2025 (issue 2026). **R10:** SCIE. **R11:** 17 citations.
- **Role:** branch 7's only method paper (LLM × graph-structured big data). **Action:** paywalled — access request.

**[4] TBD-4** — Xiao Z, et al (2025) Knowledge Aggregation Transformer Network for Multivariate Time Series Classification. IEEE Trans Big Data 11. DOI 10.1109/tbdata.2025.3594294. (research | **OA** | Crossref ✓)
- **R8 — BD:** venue-designated (IEEE TBD); subject is multivariate time-series analytics — a core big-data workload class; abstract does not use the phrase "big data" (noted). **ML:** four aggregation transformer blocks; residual + multi-head attention fusion.
- **R9:** 2025. **R10:** SCIE. **R11:** 27 citations — highest in the TBD selection.
- **Role:** branch 4 deep-learning method anchor; the only OA TBD paper. **Risk/mitigation:** weakest literal "big data" wording in the TBD set — if the supervisor requires explicit BD wording in every paper, designated compliance swap is TBD-A6 (TS-MLLM, "Industrial Time-Series Big Data" in title) or TBD-A3.

**[5] TBD-5** — Gunbilek E, et al (2026) Enhanced Approaches for Anomaly Detection in Streaming Data: Coupling Gaussian Distributions With Space Trees and Adaptive AutoEncoders. IEEE Trans Big Data 12. DOI 10.1109/tbdata.2026.3679567. (research | paid | Crossref ✓)
- **R8 — BD:** abstract: "processing, analyzing and continuously monitoring big data streams in real time". **ML:** GSTrees and GWAAE stream-learning methods; per-dataset results (>94%; ROC-AUC >89%).
- **R9:** 2026. **R10:** SCIE. **R11:** recent (0 citations) — journal IF carries R11.
- **Role:** branch 4's streaming-constraint anchor with the corpus's most concrete numbers. **Action:** paywalled — access request.

### Big Data Research — 5/5 compliant (5 research; 3 OA)

**[6] BDR-1** — Mohammadian H, et al (2025) Explainable malware detection through integrated graph reduction and learning techniques. Big Data Res 41. DOI 10.1016/j.bdr.2025.100555. (research | **OA** | Crossref ✓)
- **R8 — BD:** the obstacle named in the abstract is data scale — "the sheer size and complexity of these graph representations". **ML:** GNNs + graph reduction + explainability.
- **R9:** 2025. **R10:** SCIE. **R11:** 12 citations; journal IF 4.6.
- **Role:** branch 6 anchor for explainability-inside-workflow; pairs with TBD-1.

**[7] BDR-2** — Teixeira R, et al (2025) Efficient training: Federated learning cost analysis. Big Data Res 40. DOI 10.1016/j.bdr.2025.100510. (research | **OA** | Crossref ✓)
- **R8 — BD:** distributed AI at 6G network scale; compares training time, communication overhead, energy. **ML:** federated learning variants.
- **R9:** 2025. **R10:** SCIE. **R11:** 9 citations.
- **Role:** branch 5/8 straddler — prices federated training, the corpus's only cost accounting.

**[8] BDR-3** — Ghodsi S, et al (2026) Opinion fraud detection on massive datasets by spark. Big Data Res 43. DOI 10.1016/j.bdr.2026.100590. (research | paid | Crossref ✓)
- **R8 — BD:** "massive datasets" + Apache Spark in the title — explicit platform-scale framing. **ML:** detection of opinion fraud (title-level; abstract not indexed).
- **R9:** 2026. **R10:** SCIE. **R11:** recent; journal IF carries R11.
- **Role:** branch 5's Spark anchor. **Action:** paywalled AND abstract not indexed — first-reading extraction task; if ML evidence proves thin at full text, designated swap BDR-A1 (OA, deep NN financial time series).

**[9] BDR-4** — Liu Q, et al (2026) Heterogeneous Graph-based Risk Assessment for Internet Financial Companies with Company Big Data. Big Data Res 45. DOI 10.1016/j.bdr.2026.100620. (research | **OA** | Crossref ✓)
- **R8 — BD:** "Company Big Data" in the title. **ML:** heterogeneous graph-based (graph learning) risk assessment (title-level; abstract not indexed).
- **R9:** 2026. **R10:** SCIE. **R11:** recent; journal IF carries R11.
- **Role:** branch 6 finance domain anchor — graph learning on natively relational business data. **Action:** abstract not indexed — first-reading extraction task (OA, so immediate).

**[10] BDR-5** — Li X, et al (2026) Large-scale least squares regression based on fast spectral embedding and random Fourier feature mapping. Big Data Res 43. DOI 10.1016/j.bdr.2026.100589. (research | paid | Crossref ✓)
- **R8 — BD:** "large-scale" in the title; the entire contribution is scale. **ML:** spectral embedding + random Fourier features for regression (title-level; abstract not indexed).
- **R9:** 2026. **R10:** SCIE. **R11:** recent; journal IF carries R11.
- **Role:** branch 4's classical-scaling counterpoint to the deep-learning default. **Action:** paywalled — access request; extraction task.

### Journal of Big Data — 5/5 compliant (5 original research; 5 OA)

**[11] JoBD-1** — Elfouly MK, et al (2025) A deep learning-based framework for large-scale plant disease detection using big data analytics in precision agriculture. J Big Data 12. DOI 10.1186/s40537-025-01265-9. (original research | **OA** | Crossref ✓)
- **R8 — BD:** "large-scale ... using big data analytics" in the title; the abstract frames prior methods as deficient because they "rely on small datasets" — scale is the stated gap. **ML:** a deep learning framework for severity-aware disease detection spanning crops.
- **R9:** 2025. **R10:** SCIE. **R11:** 14 citations.
- **Role:** branch 6's agriculture domain anchor; replaced the rev-2 multi-domain benchmark survey for the original-research-only clarification (its benchmark role passes to the paper's own comparison table).

**[12] JoBD-2** — Haripriya R, et al (2025) A privacy-enhanced framework for collaborative Big Data analysis in healthcare using adaptive federated learning aggregation. J Big Data 12. DOI 10.1186/s40537-025-01169-8. (research | **OA** | Crossref ✓)
- **R8 — BD:** "Big Data analysis in healthcare" in the title; breach statistic (30%+ organizations) motivates scale-appropriate privacy. **ML:** FL + transfer learning (ResNet, VGG16), adaptive aggregation, three medical imaging datasets.
- **R9:** 2025. **R10:** SCIE. **R11:** 19 citations.
- **Role:** branch 8's applied privacy anchor; bridges healthcare and governance.

**[13] JoBD-3** — Wafa AA, et al (2025) Advancing multimodal emotion recognition in big data through prompt engineering and deep adaptive learning. J Big Data 12. DOI 10.1186/s40537-025-01264-w. (research | **OA** | Crossref ✓)
- **R8 — BD:** "in big data" in the title. **ML:** multimodal deep learning (text/audio/video/motion), GANs for class-imbalance sampling, dynamic prompt engineering.
- **R9:** 2025. **R10:** SCIE. **R11:** 22 citations — highest in the JoBD selection (resel. rev 2).
- **Role:** branch 6's affective-computing member; corpus's only applied prompt-engineering research article; bridges to the generative-methods branch.

**[14] JoBD-4** — Saleh H, et al (2025) Cloud based real-time multivariate multi-step prediction of systolic blood pressure and heart rate using temporal convolutional network and Apache Spark. J Big Data 12. DOI 10.1186/s40537-025-01207-5. (research | **OA** | Crossref ✓)
- **R8 — BD:** the engine is explicit — Apache Spark, fog/cloud streaming pipeline, offline/online split. **ML:** temporal convolutional networks, single-/multi-task multi-step forecasting.
- **R9:** 2025. **R10:** SCIE. **R11:** 8 citations.
- **Role:** branch 5's pipeline exemplar — one of two Spark-based papers (with [8]).

**[15] JoBD-5** — Zhang H, et al (2025) Graph neural network approach with spatial structure to anomaly detection of network data. J Big Data 12. DOI 10.1186/s40537-025-01149-y. (research | **OA** | Crossref ✓)
- **R8 — BD:** high-dimensional, sparse network data at scale with scarce labels is the stated constraint. **ML:** hyperbolic-space graph embedding for anomaly detection.
- **R9:** 2025. **R10:** SCIE. **R11:** 19 citations.
- **Role:** branch 4 graph-efficiency contribution; vertical with [5] and [17] on anomaly detection.

### Artificial Intelligence Review — 5/5 compliant (5 review articles — approved exception, interpretation 2; 5 OA)

Note: AIR is the assignment's designated source *and* its format template; these five review articles are retained as the team-approved exception recorded in interpretation 2, with a pre-verified original-research AIR replacement set in the alternates pool. Zero AIR 2025+ articles carry "big data" in the title — AIR is an AI journal, so relevance is established through each paper's scale/data-heterogeneity engagement, quoted below.

**[16] AIR-1** — Abou Ali M, et al (2025) Agentic AI: a comprehensive survey of architectures, applications, and future directions. Artif Intell Rev 59. DOI 10.1007/s10462-025-11422-4. (review | **OA** | Crossref ✓)
- **R8 — BD:** large-scale generative systems and their architectures/orchestration. **ML:** the defining 2025 agentic-AI synthesis; PRISMA-based review of 90 studies; dual-paradigm framework.
- **R9:** 2025. **R10:** SCIE. **R11:** 134 citations — the corpus's single strongest impact signal.
- **Role:** branch 7 anchor; the review's window onto the field's fastest-moving theme.

**[17] AIR-2** — Edozie E, et al (2025) Artificial intelligence advances in anomaly detection for telecom networks. Artif Intell Rev 58. DOI 10.1007/s10462-025-11108-x. (review | **OA** | Crossref ✓)
- **R8 — BD:** abstract opens on networks "becoming increasingly dynamic and complex due to the massive amounts of data they process". **ML:** evolution of deep-learning anomaly detection with case studies.
- **R9:** 2025. **R10:** SCIE. **R11:** 86 citations.
- **Role:** branch 6 telecom anchor; the survey side of the anomaly-detection vertical.

**[18] AIR-3** — Muneer A, et al (2026) From classical machine learning to emerging foundation models: review on multimodal data integration for cancer research. Artif Intell Rev 59. DOI 10.1007/s10462-026-11522-9. (review | **OA** | Crossref ✓)
- **R8 — BD:** "vast and heterogeneous datasets" spanning genomics, proteomics, imaging, clinical data — heterogeneity-as-scale. **ML:** classical ML → foundation models; integration strategies, validation.
- **R9:** 2026. **R10:** SCIE. **R11:** 16 citations.
- **Role:** branch 7's heterogeneity statement; highest-impact journal in the corpus.

**[19] AIR-4** — Waseem HM, et al (2025) Review of generative AI for synthetic data generation: a healthcare perspective. Artif Intell Rev 59. DOI 10.1007/s10462-025-11440-2. (review | **OA** | Crossref ✓)
- **R8 — BD:** the paper's premise is that ML "necessitates large-scale, high-quality datasets" while acquisition is constrained — data-supply-side big data. **ML:** unified comparative evaluation of generative model classes (GANs and successors).
- **R9:** 2025. **R10:** SCIE. **R11:** 7 citations.
- **Role:** branch 8 governance/synthetic-data mechanism; pairs with [12] on privacy constraints.

**[20] AIR-5** — Vats V, et al (2026) A survey of deep multivariate time-series models with an empirical reproducibility audit. Artif Intell Rev. DOI 10.1007/s10462-026-11674-8. (review | **OA** | Crossref ✓)
- **R8 — BD:** multivariate interdependent temporal data at scale across healthcare/finance/industrial monitoring; the audit component measures literature-wide evaluation practice. **ML:** seven-task taxonomy of deep MTS methods (transformers, contrastive, generative).
- **R9:** 2026. **R10:** SCIE. **R11:** recent (0 citations); journal IF 18.8 carries R11 — accepted deliberately for role, not impact.
- **Role:** the corpus's only reproducibility audit — the review's evidence for its evaluation-practice claim.

## 5. Reselection changelog (rev 1 → rev 3, 2026-09-15)

**Swapped out → in:**

1. **BDR-4:** *Optimization of differential privacy mechanism for big data privacy protection* → *Heterogeneous Graph-based Risk Assessment for Internet Financial Companies with Company Big Data*.
   Why: the DP-optimization paper's ML evidence was indirect even at title level (a privacy mechanism, not a learning method), and it carried no indexed abstract — weak on R8, the assignment's first criterion. The replacement states both dimensions in its title (graph-based learning + Company Big Data), is open access, and adds a finance domain to branch 6. Cost: the DP mechanism anchor moves to the alternate pool (BDR-A6); the privacy branch keeps four papers.
2. **JoBD-3:** *Comprehensive review of AI applications in renewable energy systems* (86 citations) → *Advancing multimodal emotion recognition in big data through prompt engineering and deep adaptive learning* (22 citations).
   Why: the energy review's Big Data relevance was contextual (energy-system data) rather than explicit, and it was a pure review in a journal where the corpus already carries four other review-type texts. The replacement has "big data" in its title, is an original research article, and adds the corpus's only prompt-engineering method application. Cost: energy/sustainability domain drops from the corpus; the review becomes 7 surveys instead of 8 (see interpretation 2); the high citation count is recorded here as the paper's R11 evidence, and it remains JoBD-A6 as the designated swap if the supervisor prefers it.

**Kept (18):** re-audited against R1–R11 with no violations; notes recorded above where evidence is title-level only (BDR-3/4/5) or where BD wording is implicit (TBD-4 KATN).

**Alternates expanded 20 → 24:** added TBD-A6 (TS-MLLM — explicit "Industrial Time-Series Big Data" title, compliance-swap candidate), JoBD-A6 (energy review, moved), JoBD-A7 (large-scale plant disease detection using big data analytics, c14, OA), BDR-A6 (DP optimization, moved).

**Metadata enrichment:** JoBD-4's full title confirms Apache Spark in the pipeline (platforms branch strengthened; extraction note regenerated).

**rev 2 → rev 3 (2026-09-15, supervisor clarification: original-research-only):**

- **Enforcement:** all fifteen TBD/BDR/JoBD selections are now original research articles. **AIR exception:** the five AIR review articles are kept as an approved, documented exception (AIR is review-designated; the assignment names it as a source and as the format template; team decision 2026-09-15). **Insurance:** five original-research AIR articles are pre-verified as drop-in replacements in the alternate pool — AIR-A6 physics-informed ML medical imaging (c46) · AIR-A7 privacy mechanisms and metrics in federated learning (c48) · AIR-A8 scaling transformers for time-series forecasting (c4) · AIR-A9 XAI-HD heart-disease explainability (c31) · AIR-A10 cloud-edge-end collaborative caching (c3).
- **TBD-2:** *Blockchain-Empowered Federated Learning survey* (25 cites) → *TS-MLLM: Multi-Modal LLM for Industrial Time-Series Big Data Analysis* (2026, original research). Why: original-research compliance plus explicit "Big Data" and LLM in the title. Cost: the blockchain-FL survey anchor is dropped (it fails the clarified constraint); the privacy cluster keeps [7], [12], [19].
- **JoBD-1:** *Big Data Analytics in IoT/social/NLP/security benchmark survey* (18 cites) → *Large-scale plant disease detection using big data analytics* (2025, original research, 14 cites). Why: original-research compliance with explicit dual-evidence title; adds precision agriculture. Cost: the corpus loses its multi-domain benchmark (landscape report Sect. 9 updated); IoT-healthcare research becomes the new JoBD-A7 alternate.
- **Alternates refresh:** TBD-A6 now HMGRL — large-scale drug-drug interaction graph learning (15 cites, original research); AIR-A6…A10 added (above); JoBD-A7 = IoT-healthcare hybrid framework (c10).

## 6. Compliance risks and mitigations

| Risk | Severity | Mitigation in place |
|---|---|---|
| Supervisor rejects the AIR review-article exception | medium | Documented exception (interpretation 2); five pre-verified original-research AIR articles (AIR-A6…A10) are ready drop-in swaps; all other fifteen selections are already original research |
| 2027 papers do not exist yet | low (factual) | One methodology sentence stating the 2027-availability check; keep the sentence in the final paper |
| 6 papers paywalled (TBD-1/2/3/5, BDR-3/5) | medium | Access requests are a team action; every paywalled paper has a designated OA swap; no workarounds found (green-OA and preprint checks performed 2026-09-15) |
| BDR-3/4/5 abstract-less in OpenAlex | low | First-reading extraction task; BDR-4 is OA and immediate; BDR-3/5 after access arrives; BDR-3 has swap BDR-A1 if its ML basis proves thin |
| TBD-4's implicit big-data wording | low | Documented in-paper relevance reasoning (venue + MTS workload); compliance swap TBD-A6 available |
| WoS verified at journal level only | low | All four journals SCIE Q1; per-article notes in `../results/pool_selected.json` |

## 7. Team sign-off checklist

- [ ] Request institutional access for the 6 paywalled papers (or trigger designated swaps)
- [ ] Read all 20 and complete the Synthesis hooks in `../sources/`
- [ ] If the supervisor rejects the AIR exception: promote AIR-A6…A10 (pre-verified original-research articles) — decisions already documented in Sect. 5; keep the 2027-availability note in the paper's methodology either way
- [ ] Keep every citation numbered per final-first-appearance in the paper and re-verify against `../results/table1.csv` before submission
