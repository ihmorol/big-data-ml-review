# Relevance & Readability Audit — the 20 selected papers

Independent audit run 2026-09-18. Question asked: *are these 20 actually research related to big data and machine learning, and which are too advanced for the team to all read?*

Method: every DOI re-resolved against **Crossref** and **OpenAlex** (independent of our own `pool_selected.json`); page/word/equation counts measured from full text where we have it (AIR-1/2/3 local PDFs, TBD-4 green-OA copy); everything else judged from the verified indexed abstract + method stack. OA status checked via OpenAlex + Unpaywall. Raw outputs: `../../tmp/verify20.json`, `../../tmp/oa_abstracts.json`, `../../tmp/verify_alternates.json`.

## 1. Bottom line

- **All 20 exist and are real.** 20/20 resolve in Crossref and OpenAlex, all `journal-article`, none retracted. Titles, journals and years match the tracker. This is not a hallucinated list.
- **All 20 are machine-learning papers.** Every one is either an ML method, an ML application, or an ML review.
- **Big-data relevance varies a lot.** ~8 are core big-data (platform, streaming, parallel scale), ~9 use "big data" as framing only, and **TBD-3 and AIR-1 are the two with essentially no big-data substance** (see §2).
- **The real compliance risk is article type, not relevance:** 15 are original research, **5 are reviews** (all of AIR). If the supervisor enforces "research paper = original research article", all five AIR slots need the insurance swaps.
- **Six papers are paywalled** (TBD-1, TBD-2, TBD-3, TBD-5, BDR-3, BDR-5) — an accessibility problem for 8 readers, and the same papers skew hardest.

## 2. Per-paper verdict

Big-data score: **core** = scale/velocity/platform is central · **framing** = large-data claims are asserted but not measured or used · **weak** = big-data mention is decoration only.
Difficulty: judged on method-stack breadth + math density (`eq/1k words` measured where full text was available).

| ID | Journal (year) | Type | ML | Big-data | Difficulty | Note |
|---|---|---|---|---|---|---|
| TBD-1 PEXP | IEEE TBD 2026 | research | yes | **core** (parallel XAI for big data) | moderate | paywalled; concept (LIME-like) readable |
| TBD-2 TS-MLLM | IEEE TBD 2026 | research | yes | core (title) | **hard** | paywalled, no OA copy; multimodal LLM internals |
| TBD-3 GraphLLM | IEEE TBD 2025 | research | yes | **weak** | **hard** | paywalled; "Big Data applications" = one framing clause; graph-reasoning benchmarks only |
| TBD-4 KATN | IEEE TBD 2025 | research | yes | framing | hard (1.89 eq/1k words, measured) | green OA copy downloaded 2026-09-18 |
| TBD-5 GSTrees/GWAAE | IEEE TBD 2026 | research | yes | **core** (streaming) | moderate | paywalled; no OA copy anywhere |
| BDR-1 malware | BDR 2025 | research | yes | core-ish (graph scale, efficiency) | moderate | OA hybrid |
| BDR-2 FL cost | BDR 2025 | research | yes | framing (distributed/edge) | **easy** | OA hybrid; simple metrics (time, energy, bytes) |
| BDR-3 opinion fraud | BDR 2026 | research | yes | **core** (massive data + Spark) | unknown | paywalled, no indexed abstract — must be read to judge |
| BDR-4 financial risk | BDR 2026 | research | yes | **core** (title) | moderate | green OA |
| BDR-5 least squares | BDR 2026 | research | yes | framing (large-scale algorithm) | **hard (math)** | paywalled; spectral embedding + RFF theory |
| JoBD-1 plant disease | JoBD 2025 | research | yes | **framing** (datasets are standard image sets) | **easy** | OA gold; CNN transfer learning, familiar |
| JoBD-2 healthcare FL | JoBD 2025 | research | yes | core-ish (multi-center FL) | easy-moderate | OA gold; ResNet/VGG16 + FL |
| JoBD-3 emotion | JoBD 2025 | research | yes | framing ("in big data" = title) | **hard** | OA gold but 7-model stack (GAN, Mistral-7B, HuBERT, TimeSformer, LLaVA, HAN-GNN, XMTF) |
| JoBD-4 SBP/HR Spark | JoBD 2025 | research | yes | **core** (Spark streaming) | easy-moderate | OA gold; TCN = 1-D CNN |
| JoBD-5 GNN anomaly | JoBD 2025 | research | yes | framing | hard-moderate | OA gold; hyperbolic-space math |
| AIR-1 Agentic AI | AIR 2025 | **review** | yes | **weak** | easy to read, long (37 pp, 2 eq, measured) | labelled "Systematic Review" p.1 of PDF |
| AIR-2 telecom anomaly | AIR 2025 | **review** | yes | framing (65 scale mentions, no numbers) | easy to read (40 pp, 0 eq, measured) | Hadoop/Spark named once, historically |
| AIR-3 cancer multimodal | AIR 2026 | **review** | yes | framing | moderate (69 pp, 1.40 eq/1k words, measured) | long; useful as a methods catalogue |
| AIR-4 synthetic data | AIR 2025 | **review** | yes | framing | moderate | OA |
| AIR-5 MTS survey+audit | AIR 2026 | **review** | yes | framing | moderate | OA |

**Weakest on big-data substance:** TBD-3 (graph-reasoning benchmark paper wearing a big-data title), AIR-1 (survey; zero volume/velocity/platform content), then JoBD-1 / JoBD-3 / TBD-4, where "big data" is title-level.

## 3. The "too advanced" problem

Hardest papers for a mixed-ability group of 8, hardest first:

1. **TBD-2 TS-MLLM** — multimodal LLM + spectrum-aware VLM adaptation + PHM. Paywalled, no preprint.
2. **TBD-3 GraphLLM** — LLM graph reasoning internals (Graph2Text bottleneck, graph encoders). Paywalled; also the weakest big-data fit.
3. **JoBD-3 multimodal emotion** — GAN + Mistral-7B + HuBERT + TimeSformer + LLaVA + HAN-GNN + XMTF in one pipeline. OA, but the densest stack in the pool.
4. **BDR-5 least-squares/RFF** — numerical-linear-algebra math. Paywalled.
5. **TBD-4 KATN** — transformer internals, ablation-heavy (measured 1.89 eq/1k words, the highest of the accessible set).
6. **JoBD-5 hyperbolic GNN** — non-Euclidean geometry.

Note the correlation: 4 of the 6 hardest are also paywalled, so the team cannot even read them freely.

## 4. Alternatives, re-scored for big-data substance

This is a Big Data course, so the swap test is *both* "easier to read" **and** "actually about big data", not just readability. Column 4 gives the new big-data grade (core = platform/scale/velocity is the subject; framing = large data asserted but not central).

All candidates re-verified 2026-09-18 (Crossref + OpenAlex): correct journal, 2025+, journal-article, not retracted; OA from OpenAlex/Unpaywall.

| Swap out | Suggested in | Journal | Big-data | OA | Difficulty | Why |
|---|---|---|---|---|---|---|
| **TBD-3 GraphLLM** | **TBD-A5 SARF** (10.1109/tbdata.2025.3639968) | IEEE TBD | **core** (data quality for large-scale IoT/mobile data) | **yes CC-BY** | easy-mod | Wins on every axis: fixes the pool's weakest big-data link, OA, no LLM math, designated swap already. |
| TBD-3 GraphLLM | TBD-A3 stream ensembles (10.1109/tbdata.2025.3570072) | IEEE TBD | **core** (data streams, concept drift, label scarcity) | no (closed) | mod | Classic hard-big-data problem (streaming + no labels); needs institutional access. |
| TBD-3 GraphLLM | TBD-A4 graph clustering (10.1109/tbdata.2025.3639917) | IEEE TBD | **core** (scalability/complexity for big graphs) | no (closed) | mod-hard | Method paper whose whole point is scaling to large, high-dim data. Math present. |
| **JoBD-3 emotion** | **JoBD-A4 BlueEdge** (10.1186/s40537-025-01262-y) | JoBD | **core** (big-data cleaning, edge vs cloud/Hadoop) | yes gold | easy-mod | Most squarely "big data infrastructure" of the JoBD swaps; small evaluation (146 cases) — usable as an "ours" limitation. |
| JoBD-3 emotion | JoBD-A7 IoT healthcare (10.1186/s40537-025-01243-1) | JoBD | **core** (explicit large-scale, high-dim IoT medical data) | yes gold | easy-mod | Best explicit "big data + ML classification" match; 8 000 records, 200+ attributes. |
| JoBD-3 emotion | JoBD-A1 FinTech fraud (10.1186/s40537-026-01506-5) | JoBD | moderate (real-time large-scale transactions) | yes gold | **easiest** | Single GRU + blockchain; the most readable option, big-data framing is real-time scale. |
| **BDR-5 least squares** | **BDR-A4 ImDMI** (10.1016/j.bdr.2025.100519) | BDR | **core** (continuous big-data publishing on **Apache Spark**) | no (closed) | mod | The only BDR alternate with an explicit big-data platform; no indexed abstract, so read before committing. |
| BDR-5 least squares | BDR-A2 job matching (10.1016/j.bdr.2025.100509) | BDR | moderate ("millions of offers/resumes") | yes CC-BY | easy-mod | OA and readable, but it is an NLP recommender — weaker big-data than BDR-A4. |
| AIR-1 Agentic AI | **AIR-A5 weather/climate** (10.1007/s10462-026-11690-8) | AIR | **core** (petabyte-scale spatiotemporal data) | yes | mod | Fixes AIR-1's zero big-data content while staying a legit AIR review. |
| AIR-1 Agentic AI | AIR-A3 GNN anomaly SLR (10.1007/s10462-026-11532-7) | AIR | moderate (graph scale, scalability barriers) | yes | easy-mod | Readable SLR; overlaps JoBD-5/TBD-5 thematically. |

**Revised recommendation (big-data first):**
1. **TBD-3 → TBD-A5** — the one swap that improves big-data fit, readability and access simultaneously. Do this one regardless of which "too advanced" papers you meant.
2. **JoBD-3 → JoBD-A4** for big-data substance (edge/cloud data cleaning), or **JoBD-A1** if readability matters more (single model, OA). Both keep 5-per-journal and original-research rules.
3. Optional: **BDR-5 → BDR-A4** if you want a Spark/platform paper in the BDR slot — note BDR-4's abstract is not indexed, so read it first and be ready to fall back to **BDR-A2**.
4. If the supervisor rejects the review exception, prefer AIR-A8/A9/A10 (original research) over AIR-A6/A7 (they read as reviews).

**Correcting the earlier read:** BDR-5's "scalable algorithm" is a legitimate big-data branch (scalable ML), so it is *not* the weakest big-data paper — the two genuinely weak ones are **TBD-3 and AIR-1**. Swapping TBD-3 is justified on big-data grounds alone; swapping AIR-1 → AIR-A5 is justified if you want no weak links in the AIR column.

## 5. Caveats

- Do not substitute silently — the repo rule. Swaps must be recorded in `trackers/writing-progress.md` and the tracker/`references.bib` regenerated (`code/build_tracker.py`).
- Theme balance: the §3.2 branch map (B1–B5) and Fig. 2 counts need a refresh after any swap (TBD-A5 lands in B1/B2; JoBD-A1 lands in B3/B2; BDR-A1 in B3).
- Citation impact: swaps trade citations for readability (TBD-A5 = 0 cites vs TBD-3 = 17; JoBD-A1 = 0 vs JoBD-3 = 22). Defensible since the impact criterion is "preferably".
- The AIR research-only insurance set is not uniform: AIR-A8/A9/A10 are clearly original research; AIR-A6/A7 read as reviews, so verify their article type before promoting them.
- Full-text verification was possible only for AIR-1/2/3 and TBD-4; Springer and ScienceDirect block automated full-text access, so BDR-3/BDR-4/BDR-5 and the JoBD papers beyond their abstracts still need the members' own reading (or institutional access) before citing specifics.
