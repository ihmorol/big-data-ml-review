# Paper outline — "Big Data with Machine Learning: A Review"

Target format: *Artificial Intelligence Review* (Springer). Citations: numeric brackets `[n]`. This outline maps 1:1 onto the six assignment components (Abstract, Introduction, Literature Review, Tables and Figures, Conclusion, References) — nothing outside them.

## Component 1 — Abstract (~200–250 words, write LAST)

One paragraph: why BD+ML needs a current synthesis → what we reviewed (20 papers, 4 journals, 2025–2027, selection method) → the taxonomy/themes found → 2–3 cross-cutting insights and gaps → future directions. No citations in the abstract (AIR convention).

## Component 2 — Introduction (~1.5–2 pages, worth 3%)

1. **Context:** explosive data growth; ML as the primary lens for extracting value; why the 2025+ literature needs consolidating.
2. **Scope:** the four journals, 2025–2027, 20 papers, selection criteria (relevance, period, WoS, impact) — with a PRISMA-style selection flow figure (Fig. 1).
3. **Organization of the paper.**

No formal research questions — the supervisor's brief is a plain literature review. The Introduction sets scope and preview; the analytical weight lives in the Literature Review.

## Component 3 — Literature Review (~60% of the paper, worth 10%)

Organized **thematically** — zero paper-by-paper structure. Draft themes (finalize after reading; expect 3–5):

- **3.1 Background & concepts** (brief): the BD "V"s, the ML pipeline at scale — only what the synthesis needs.
- **3.2 Taxonomy of BD+ML research** (Fig. 2): our classification of the 20 papers along axes like ML paradigm × data modality × platform × domain. Every paper gets placed; the taxonomy drives 3.3–3.5.
- **3.3 Theme — Scalable ML methods & architectures:** what algorithms/architectures the papers use, how they handle volume/velocity; compare design choices head-to-head.
- **3.4 Theme — Platforms, pipelines & data engineering:** batch vs streaming vs hybrid; infrastructures reported; interoperability and bottleneck patterns.
- **3.5 Theme — Applications & domains:** where the work lands (health, security, IoT, finance, …), datasets and evaluation practice; what the benchmarks reveal about maturity.
- **3.6 Cross-cutting analysis:** contrasts between journals/approaches; recurring limitations authors admit; methodological weaknesses *we* see (e.g., weak baselines, scale claims without evidence); explicit research gaps.
- **3.7 Future research directions:** derived from 3.6, not generic.

## Component 4 — Tables and Figures (worth 3%; Tables 1–2 + Figs 1–3 minimum)

- **Table 1 — Master comparison of the 20 papers:** ref, journal, year, domain, ML technique(s), big-data platform/tech, dataset & scale, key contribution. (The backbone table — build it in `results/table1.csv` early and regenerate.)
- **Table 2 — Theme × paper matrix** (or taxonomy mapping).
- **Fig. 1 — Paper selection flow** (identification → screening → inclusion, PRISMA-style).
- **Fig. 2 — Taxonomy diagram.**
- **Fig. 3 — Distribution chart:** papers per journal/year/theme or per ML paradigm.
- Every figure/table numbered, captioned, cited in text ("as shown in Table 1").

## Component 5 — Conclusion (~1 page, worth 2%)

Recap what the synthesis showed (state of methods, platforms, applications, challenges); 2–3 takeaways; limitations of our review (scope: 4 journals, 20 papers); future outlook. No new citations.

## Component 6 — References (worth 3%)

- Springer Basic (numeric, brackets): `Lastname FN (Year) Title. Journal Vol(Issue):pages`. DOI where available.
- All 20 primary papers + a small number of supporting/background references (kept minimal — the assignment grades the 20).
- Every `[n]` resolves; numbering by order of first appearance; no uncited entries.

## Writing order (given 12 days)

Table 1 & Fig. 1 data → themes 3.3–3.5 → 3.6–3.7 → 3.1–3.2 → Introduction → Conclusion → Abstract → references pass → formatting pass.
