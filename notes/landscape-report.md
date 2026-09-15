# Big Data with Machine Learning: A Review — verified pool and landscape report

*A working synthesis for the supervisor-assigned review. 20 papers, 5 from each of four journals, published 2025–2027 (all items 2025–2026; no 2027-dated items exist yet). Every reference was existence- and metadata-verified against Crossref on 2026-09-15. Content statements are abstract-level: paywalled papers (TBD-1, TBD-2, TBD-3, TBD-5, BDR-3, BDR-4, BDR-5) are described from titles/abstracts only until the team reads the full texts.*

Reference numbering in this report follows pool IDs ([1]–[20] = TBD-1…AIR-5; see `results/table1.csv`), not order of first appearance — deliberate, so `[n]`, `sources/`, and the pool tracker stay consistent while the team drafts. Convert to first-appearance numbering during submission formatting.

## Abstract

The 2025–2026 output of the four journals spans 1,519 works, from which this report selects and verifies 20 papers (5 per journal) to map the current state of big data with machine learning. The selected corpus shows the field's center of gravity shifting from *learning on big data* to *governing learning at scale*: privacy-preserving training, platform engineering, and trustworthiness account for two fifths of the corpus (8 of 20), while classic scalable-algorithm contributions persist at 5 of 20. Seven of the twenty works are survey or review articles (the five Artificial Intelligence Review articles by journal design, TBD-2's blockchain-FL survey, and JoBD-1's benchmark survey); the remaining thirteen are original research articles. Two tensions emerge: privacy-preserving and scale-maximizing research pull in opposite directions, and agentic/foundation-model work — the fastest-rising theme by citations — remains thin on big-data-grounded evaluation, with the corpus's single explicit reproducibility audit finding that evaluation practice in deep time-series work is fragmented. This report supplies the taxonomy, per-branch comparisons, and open problems for the review paper's Literature Review, Tables, and Conclusion.

## 1. Introduction

Data volume growth and machine learning's rise are the two defining developments in contemporary computing, and the literature at their intersection moves fast enough that even 18-month-old syntheses understate it. This report consolidates the 2025–2027 output of the four journals designated by the assignment — IEEE Transactions on Big Data, Big Data Research, Journal of Big Data, and Artificial Intelligence Review — into a 20-paper corpus that the team can defend line by line.

The report's scope is fixed by the assignment: at least 20 papers, approximately 3–5 per journal (met with exactly 5 each), 2025–2027 publication, relevance to both big data and machine learning, preference for Web of Science indexing and high-impact venues. All four journals are SCIE-indexed and Q1 by SJR; their current impact factors order Artificial Intelligence Review (18.8) > Journal of Big Data (10.8) > IEEE TBD (8.1) > Big Data Research (4.6).

The remainder is organized as: methodology (Sect. 2); the thematic taxonomy (Sect. 3); five thematic branches (Sect. 4–8); cross-branch synthesis (Sect. 9); open problems (Sect. 10); conclusion (Sect. 11).

## 2. Methodology

**Retrieval.** Rather than keyword-web searching, the full 2025+ output of each journal was pulled programmatically from the OpenAlex API by source ID (1,519 works: IEEE TBD 296, Big Data Research 101, Journal of Big Data 480, Artificial Intelligence Review 642), keeping titles, abstracts, authors, venue, publication date, open-access status, and citation counts. This removes venue-mismatch risk that web search invites. A keyword screen over titles/abstracts (machine-learning terms × big-data terms) ranked candidates per journal; the BDR shortlist was additionally reviewed title-by-title because OpenAlex lacks abstracts for many Elsevier records.

**Selection.** From the ranked candidates, 5 papers per journal were chosen to maximize (i) joint BD+ML relevance, (ii) theme diversity across the corpus as a whole, (iii) citation impact within the 2025–2026 window, and (iv) open accessibility where quality was comparable. Per the team's access constraint, paywalled selections were kept only where the paper's role in the synthesis was irreplaceable; 24 further vetted alternates are held in `results/pool_selected.json` for substitution. Because theme diversity was an explicit selection criterion, the corpus's theme proportions are curated, not raw field proportions — every branch comparison describes this corpus, not the journals' complete output.

**Verification.** Every selected paper (and every alternate) was verified in two steps per the citation protocol: existence and metadata identity against the Crossref record for its DOI (title, venue, year), with content claims restricted to title/abstract level. Result: 20/20 selected verified; three IEEE early-access items carry 2025 online / 2026 issue dates, both inside the review period.

**Access status.** Open access: all JoBD and AIR selections, plus TBD-4 and BDR-1, BDR-2, BDR-4. Paywalled (institutional access needed): TBD-1, TBD-2, TBD-3, TBD-5, BDR-3, BDR-5 (6 of 20). No indexed free copies or preprints were found for the paywalled set; if access cannot be obtained, the designated swaps are TBD-A5 (OA) for any TBD paywalled item and BDR-A1/BDR-A2 (OA) for BDR paywalled items. `notes/selection-backing.md` carries the per-paper requirement backing.

**Journal profile.**

| Journal | 2025+ works | WoS | IF (current) | SJR 2024 | Access |
|---|---|---|---|---|---|
| IEEE Transactions on Big Data | 296 | SCIE | 8.1 | 1.571 Q1 | hybrid |
| Big Data Research | 101 | SCIE | 4.6 | 0.914 Q1 | hybrid |
| Journal of Big Data | 480 | SCIE | 10.8 | 1.964 Q1 | full OA |
| Artificial Intelligence Review | 642 | SCIE | 18.8 | 3.01 Q1 | full OA |

*Note: SCIE status verified via secondary sources (Master Journal List is not machine-accessible); impact figures as published on journal pages, September 2026.*

## 3. Taxonomy

The corpus classifies along two axes. **Axis 1 — what is learned:** scalable/interpretable classical methods, deep learning at scale, graph learning, transformers/time-series, foundation models and agentic systems. **Axis 2 — what surrounds the learning:** platforms (batch/streaming/fog-cloud/edge), application domain (health, energy, security/telecom, general), and governance (privacy, explainability, reproducibility).

Five branches carry the corpus (paper counts in parentheses):

1. **Scalable and interpretable learning methods** (5) — [1] TBD-1, [4] TBD-4, [5] TBD-5, [10] BDR-5, [15] JoBD-5
2. **Platforms, pipelines, and infrastructure** (4) — [8] BDR-3, [14] JoBD-4, [11] JoBD-1, [7] BDR-2
3. **Applications and domains** (4) — [6] BDR-1, [17] AIR-2, [9] BDR-4, [13] JoBD-3
4. **Foundation models and agentic AI** (3) — [3] TBD-3, [16] AIR-1, [18] AIR-3
5. **Privacy, governance, and evaluation** (4) — [2] TBD-2, [12] JoBD-2, [19] AIR-4, [20] AIR-5

Full metadata for all 20 sits in `results/table1.csv`. **Straddlers** (identified, not hidden): [7] BDR-2 is federated learning as privacy mechanism *and* as 6G infrastructure; [12] JoBD-2 is privacy machinery instantiated on a healthcare application; [13] JoBD-3 is a prompt-engineering method paper tested on an affective-computing application (branches 6/7 straddler); [19] AIR-4 couples generative models to a governance problem; [5] TBD-5 is a methods contribution whose only evaluation is security data. **Empty cells:** no reinforcement-learning-at-scale method paper appears anywhere in the corpus; no purely theoretical/statistical-learning contribution; no 2027-dated item exists in any of the four journals to include (verified 2026-09-15).

## 4. Scalable and interpretable learning methods

This branch answers the oldest question in the field — how do learning methods themselves scale — and shows the 2025–2026 answer has become plumbing-heavy: parallelization, embedding tricks, and streaming constraints rather than new base algorithms.

The interpretability contribution [1] PEXP makes the branch's sharpest claim: model interpretation for models trained on large-scale data is itself a scalability problem, and a parallel tree-based explainer with distribution-aware perturbation and kernel similarity addresses fidelity and cost together; no other pool paper treats explanation cost as the bottleneck. Scaling classical regression instead of explaining it, [10] BDR-5 pairs fast spectral embedding with random Fourier features for large-scale least squares — a striking counterpoint to the deep-learning default of the rest of the corpus, and one of the few branch papers whose claims cannot be checked here (no abstract indexed; title-level only until accessed). Against both, [4] TBD-4's KATN takes the deep route for multivariate time series classification, aggregating four transformer blocks that fuse residual local features with multi-head global relations — the dual local/global tension is the pattern the branch's time-series work shares with [5] TBD-5, which instead argues *against* offline-trained detectors: its Gaussian Space Trees and Gaussian-weighted ADWIN autoencoder target streaming regimes directly, reporting 94%+ and 89%+ ROC-AUC respectively on three real streamed datasets — the branch's most concrete numbers, and a rare case of results stated per-method rather than an aggregate. [15] JoBD-5 completes the branch by attacking a structural constraint rather than a computational one: network anomaly detection suffers from high-dimensional sparse graphs with scarce labels, and hyperbolic-space embedding of graph distance features is its proposal for capturing hierarchical structure where Euclidean embeddings blur it. Notably, four of the five papers optimize a resource (computation [1, 10], latency [5], representation efficiency [15]) rather than an accuracy leaderboard — in this corpus, "scalable ML" has become mostly a systems constraint.

| Study | Method | Scale lever | Evaluation basis | Reported result |
|---|---|---|---|---|
| [1] TBD-1 PEXP | parallel tree-based explainer | parallelization of explanation | not stated in abstract | — |
| [4] TBD-4 KATN | aggregation transformers (local+global) | feature fusion efficiency | not stated in abstract | — |
| [5] TBD-5 GSTrees/GWAAE | Gaussian trees + autoencoder | streaming, no offline retraining | ECG5000, Credit Card Fraud, SMTP streams | >94% (GSTrees); >89% ROC-AUC (GWAAE) |
| [10] BDR-5 | spectral embedding + random Fourier features | large-scale least squares | not stated in abstract | — |
| [15] JoBD-5 | hyperbolic GNN | representation of sparse graphs | not stated in abstract | — |

*Table A: The branch optimizes resources as much as accuracy; three of five papers do not state evaluation specifics in the abstract, so the team should extract protocols from the full texts.*

## 5. Platforms, pipelines, and infrastructure

Where branch 4 optimizes models, this branch optimizes the machinery under them, and it is the branch that most literally embodies "big data."

[8] BDR-3 is the corpus's single unambiguous Spark contribution — fraud detection on massive datasets executed on Spark — and with no indexed abstract its specifics (dataset, scale, algorithm) must come from the full text; its value to the review is marking that classic cluster-computing stacks still anchor production workloads even in the LLM era. [14] JoBD-4 shows the modern hybrid: a fog/cloud real-time forecasting system for systolic blood pressure and heart rate built on Apache Spark, with an offline model-development phase (single- vs multi-task, multi-step temporal convolutional networks) feeding an online streaming pipeline — the clearest example in the corpus of the batch/streaming split being engineered rather than assumed. [11] JoBD-1 operates one level up: a multi-domain survey that benchmarks CNN, XGBoost, self-supervised learning, GNNs, ELM, KNN, and decision trees across IoT, social media, NLP, and information security on five metrics, concluding GNN and SSL are the strongest performers — the corpus's only head-to-head algorithm benchmark and therefore a load-bearing citation for the review's comparison table (its exact figures need extraction from the full text, which is open access). [7] BDR-2 asks the infrastructure question economically: across federated-learning variants in 6G settings it compares training time, communication overhead, and energy consumption, reporting that FL accelerates training and cuts transferred data but that outcomes depend on the specific FL approach — the branch's only paper that also belongs to the privacy story, since its subject is the federated paradigm itself. The four papers together delineate an infrastructure stack — cluster engine [8], fog/cloud streaming [14], cross-domain benchmark [11], distributed-training economics [7] — that no single application paper in this corpus deploys end-to-end.

## 6. Applications and domains

Four papers carry the application branch, and their domains could hardly be further apart: malware analysis, telecom operations, financial risk, and affective computing.

[6] BDR-1 attacks the opposite end of the visibility spectrum from [1]: malware detection where the data structure itself is the obstacle, pairing new graph-reduction techniques with GNN explainability so that control-flow and function-call graphs become tractable and their predictions legible to analysts — the only pool paper where explainability is inseparable from the application's workflow rather than a model-level add-on, and one of the corpus's two explainability threads alongside [1]. [17] AIR-2 charts a decade of transition in telecom network operations from rule-based anomaly detection to deep-learning systems, with case studies; it is the survey counterpart to [5] TBD-5's streaming method and [15] JoBD-5's graph method, giving the review a three-paper vertical on anomaly detection that no other theme matches. [9] BDR-4 moves the branch into finance: heterogeneous graph-based risk assessment for internet financial companies built on their company big data — the corpus's clearest case of graph learning deployed on natively relational business data; as an open-access article whose abstract is not indexed, its evaluation specifics are a first-reading extraction task. [13] JoBD-3 is the branch's method-flavored member and its only affective-computing entry: a multimodal emotion-recognition framework for big data environments that generates synthetic samples with GANs to counter class imbalance and extracts cross-modal features through dynamic prompt engineering across text, audio, video, and motion — the corpus's only applied prompt-engineering research article, bridging this branch to the generative-model work of Sect. 7.

The branch's pattern: domains with native graph structure ([6], [9], [15]) and domains with native streams ([14], [17]) attract the most method-building, while the remaining application domains mostly consume off-the-shelf deep learning.

## 7. Foundation models and agentic AI

This branch is small in count (3) and outsized in citation velocity — together its members hold 167 of the corpus's citations — and it is the branch most likely to look dated first, which is itself a finding.

[16] AIR-1 is the corpus's most-cited paper by a wide margin (134 citations within months) and its most ambitious synthesis: a dual-paradigm framework separating symbolic/classical from neural/generative agentic systems, built from a PRISMA-based review of 90 studies, and aimed squarely at the field's "conceptual retrofitting" problem — the conflation of modern neural agents with older symbolic architectures. [18] AIR-3 tracks the same transition at the model layer: a review of multimodal data-integration strategies in oncology moving from classical ML to foundation models pretrained on extensive data and adapted to downstream tasks (biomarker discovery, diagnosis, personalization) — the corpus's clearest statement that "big data + ML" now means heterogeneous modalities fused, not just volume. [3] TBD-3 is the branch's only method paper and the only IEEE TBD contribution to LLM work selected here: GraphLLM argues that the standard Graph2Text conversion is the bottleneck in LLM graph reasoning — a claim of direct consequence for big-data applications whose data is natively graph-structured (social networks, knowledge graphs, molecular databases) — and restructures graph reasoning accordingly. The honest observation for the review: none of the three evaluates under the platform constraints (streaming, cluster, memory) that branches 4–5 treat as first-class, and this branch's scale vocabulary is *training-set size*, not production workload. Agentic/foundation-model research in these four journals is currently ahead of its big-data grounding.

## 8. Privacy, governance, and evaluation

The corpus's governance concentration (4 papers) is about everything around the model: who can see the data, what can be published, what can be trusted. Its existence in these four journals, rather than only in policy venues, is a clear signal of where BD+ML research's center has moved.

Privacy splits into three mechanisms. Blockchain-augmented federated learning [2] TBD-2 surveys why blockchain is applied to FL (single-point-of-failure removal, incentives, security) and what it costs (network, computing, storage demands) — the branch's most infrastructure-aware privacy survey. Differential privacy receives an applied treatment in [12] JoBD-2, which combines federated learning with transfer learning (ResNet, VGG16) across three medical imaging datasets in a simulated multi-center environment, contributing an adaptive aggregation method — and opening from the corpus's starkest statistic, that over 30% of healthcare organizations suffered breaches in the past year. Synthetic data is the third mechanism: [19] AIR-4 reviews generative models (GANs and successors) producing high-fidelity synthetic data for imaging, EHRs, signals, and drug discovery under privacy regulation, filling what it identifies as the gap left by model-class-specific prior reviews with a unified comparative evaluation. The evaluative thread is carried alone by [20] AIR-5: a seven-task survey of deep multivariate time-series models that includes an *empirical reproducibility audit* — the only pool paper that measures the literature's methodological health, and the reason the review can write about evaluation practice with a citation rather than an assertion. Against this branch's maturity in privacy mechanisms, its accountability mechanisms (audits, benchmarks, reporting standards) are represented by a single paper — the corpus's most lopsided internals.

## 9. Cross-branch synthesis

Three cross-branch patterns are visible only when the branches are read together.

**Trends shared across branches.** First, resource-consciousness has become universal: papers optimize computation [1, 10], latency [5], representation cost [15], communication and energy [7], or explanation cost [1, 6] — accuracy-only contributions no longer anchor even the method branch. Second, heterogeneity is the new scale: the corpus's "big data" is multimodal [13, 18, 19], multi-source [12], graph-structured [3, 6, 9, 15], or streaming [5, 14] more often than merely voluminous — volume alone appears in no title. Third, both survey-heavy journals (AIR, JoBD) contribute syntheses and application breadth, while the two data-engineering journals (TBD, BDR) contribute mechanisms and systems; the review's comparison table can exploit this division of labor.

**Tensions.** The defining one: privacy-preserving research ([2], [7], [12], [19]) and scale-maximizing research ([16], [18], [3]) pull in opposite directions — the former's premise is that data cannot be centralized, the latter's that capability comes from pretraining on everything available. No pool paper addresses the contradiction; [7] BDR-2 comes closest by pricing federated training in communication and energy terms. A second tension is evaluative: the agentic/foundation-model branch's citation velocity ([16]: 134) vastly exceeds its reproducibility, while the one paper that audits reproducibility [20] has zero citations — the field rewards novelty faster than it rewards verification.

**Methodological problems common to the corpus.** Only [5] and [11] report per-method results with named datasets among the non-survey papers; several abstracts omit evaluation specifics entirely (visible as "not stated" in Table A). Caveat: abstract brevity can hide full-text detail, so this is weak evidence on its own — the stronger evidence is [20]'s reproducibility audit, whose finding that evaluation practice is fragmented the corpus's pattern is consistent with rather than independent proof of.

## 10. Open problems

- **Reinforcement learning at scale is absent.** No selected paper contributes an RL method for big-data regimes — the taxonomy's method axis has an empty RL cell, and against branch 4's pattern of resource-constrained learning, RL's sample inefficiency versus big data's abundance is an unaddressed intersection in this corpus.
- **Agentic systems lack big-data grounding.** No pool paper evaluates agentic architectures [16] under streaming, cluster, or memory constraints; the interface between agentic AI and the platform concerns of branch 5 is the taxonomy's most conspicuous empty cell.
- **The privacy–scale contradiction is unpriced.** Beyond [7]'s communication/energy accounting, no paper quantifies what decentralized training costs in model quality relative to centralized pretraining — the review can state this as a gap supported by the *absence* across 20 verified papers plus [7]'s partial treatment.
- **Accountability lags mechanism.** One reproducibility audit [20] against four privacy-focused works [2, 7, 12, 19]: no benchmark, audit, or reporting standard for privacy claims appears in the corpus.
- **Explanation at scale is single-sourced.** [1] alone treats interpretation cost as the bottleneck; [6]'s explainability is application-bound. Whether the two generalize to each other is untested.

## 11. Conclusion

The 20 verified papers from the four assignment journals describe a field in transition: the 2025–2026 literature at IEEE TBD, Big Data Research, Journal of Big Data, and AIR still builds scalable learning methods (branch 4, the largest at 5 of 20 papers), while platforms, applications, and the governance of learning at scale each carry four papers (branches 5, 6, 8), and its most visible individual work is the foundation-model/agentic wave (branch 7). Three takeaways for the review paper: (1) "big data" in this corpus means heterogeneity and constraint more than volume; (2) privacy-preserving and capability-maximizing research are on a collision course that no selected paper addresses; (3) evaluation and reproducibility practice is the corpus's weakest joint, documented by the corpus itself. The corpus's limits are the assignment's limits — four journals, 5 papers each, one snapshot year, English-language venues only — and the review should carry that as an explicit scope caveat. What the corpus contributes beyond a reading list is the taxonomy and the two tensions, which give the review a thesis: *big data with machine learning, 2025–2027, is less about learning from more data than about learning under constraints — privacy, platforms, and proof.*

## References

Numbering follows pool IDs (TBD-1=[1] … AIR-5=[20]); see `results/table1.csv` and `sources/` for DOIs and full metadata.

[1] S. S. et al. (TBD-1), "PEXP: A Scalable Parallel Tree-Based Framework for Interpreting Models on Big Data," IEEE Transactions on Big Data, 2026 (early access 2025).
[2] — (TBD-2), "Blockchain-Empowered Federated Learning: Benefits, Challenges, and Solutions," IEEE Transactions on Big Data, 2025.
[3] — (TBD-3), "GraphLLM: Boosting Graph Reasoning Ability of Large Language Model," IEEE Transactions on Big Data, 2025/2026.
[4] — (TBD-4), "Knowledge Aggregation Transformer Network for Multivariate Time Series Classification," IEEE Transactions on Big Data, 2025.
[5] — (TBD-5), "Enhanced Approaches for Anomaly Detection in Streaming Data," IEEE Transactions on Big Data, 2026.
[6] — (BDR-1), "Explainable malware detection through integrated graph reduction and learning techniques," Big Data Research, 2025.
[7] — (BDR-2), "Efficient training: Federated learning cost analysis," Big Data Research, 2025.
[8] — (BDR-3), "Opinion fraud detection on massive datasets by spark," Big Data Research, 2026.
[9] — (BDR-4), "Heterogeneous Graph-based Risk Assessment for Internet Financial Companies with Company Big Data," Big Data Research, 2026.
[10] — (BDR-5), "Large-scale least squares regression based on fast spectral embedding and random Fourier features," Big Data Research, 2026.
[11] — (JoBD-1), "Big Data Analytics in IoT, social media, NLP, and information security: trends, challenges, and potential," Journal of Big Data, 2025.
[12] — (JoBD-2), "A privacy-enhanced framework for collaborative Big Data analysis in healthcare," Journal of Big Data, 2025.
[13] — (JoBD-3), "Advancing multimodal emotion recognition in big data through prompt engineering and deep adaptive learning," Journal of Big Data, 2025.
[14] — (JoBD-4), "Cloud based real-time multivariate multi-step prediction of systolic blood pressure and heart rate," Journal of Big Data, 2025.
[15] — (JoBD-5), "Graph neural network approach with spatial structure to anomaly detection of network data," Journal of Big Data, 2025.
[16] M. Abou Ali et al. (AIR-1), "Agentic AI: a comprehensive survey of architectures, applications, and future directions," Artificial Intelligence Review, 2025.
[17] — (AIR-2), "Artificial intelligence advances in anomaly detection for telecom networks," Artificial Intelligence Review, 2025.
[18] — (AIR-3), "From classical machine learning to emerging foundation models: review on multimodal data integration," Artificial Intelligence Review, 2026.
[19] — (AIR-4), "Review of generative AI for synthetic data generation: a healthcare perspective," Artificial Intelligence Review, 2025.
[20] — (AIR-5), "A survey of deep multivariate time-series models with an empirical reproducibility audit," Artificial Intelligence Review, 2026.

*Full author lists, volume/issue/page data, and DOIs: `results/table1.csv`; per-paper reading notes: `sources/`.*
