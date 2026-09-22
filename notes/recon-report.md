# Reconnaissance report — "Big Data with Machine Learning: A Review"

*Read-only context-gathering pass for the paper-writing subtasks. Compiled 2026-09-22. This report only records what exists; it does not draft the paper. The single source of truth for requirements is `notes/Big Data Assignment.pdf`; the distilled brief is `notes/requirements.md`.*

**Correction to the tasking assumption:** the AIR journal LaTeX template **is inside the workspace** at `AIR_Journal_Template/` — it did not need a filesystem search. Details in §4.

---

## 1. Assignment theme + requirements (verbatim where possible)

### 1.1 Theme
- **Deliverable:** "a literature review paper" — an **Artificial Intelligence Review Paper** titled **"Big Data with Machine Learning: A Review"** (`notes/requirements.md` L7).
- **Review period:** **2025–2027**; **keywords:** *Machine Learning, Big Data* (`notes/requirements.md` L9).

### 1.2 Requirement list (quoted)

From `notes/requirements.md`:

> "An **Artificial Intelligence Review Paper** titled: **Big Data with Machine Learning: A Review** — review period **2025–2027**, keywords *Machine Learning, Big Data*." (L7–9)

> "It must be a **proper literature review**: synthesizing, comparing, and critically analyzing the selected papers — explicitly **not** a paper-by-paper summary." (L11)

> "At least **20 research papers** selected from exactly these four journals:" (L15)
> 1. **IEEE Transactions on Big Data** (IEEE Xplore)
> 2. **Big Data Research** (Elsevier ScienceDirect)
> 3. **Journal of Big Data** (SpringerOpen)
> 4. **Artificial Intelligence Review** (Springer)

> "≈3–5 papers per source. **Math note:** 4 journals × max 5 = 20, so hitting '≥20 papers from these four journals' forces **exactly 5 from each journal**. Plan 5 + 5 + 5 + 5." (L22)

> "**Supervisor clarification (2026-09-15):** 'research papers' means **original research articles**. Enforced for TBD/BDR/JoBD (15/15 selections are original research); AIR's five selections are review articles kept as a documented exception (AIR is review-designated, and the assignment names it as both source and format template). Ready-made swaps if the exception is rejected: AIR-A6…A10." (L24)

Selection criteria (L26–30):
- "Relevant to **Big Data and Machine Learning**"
- "Published during the **2025–2027** review period (note: as of Sep 2026 only 2025–2026 papers exist…)"
- "Preferably indexed in **Web of Science** (all four target journals are WoS-indexed…)"
- "Preferably **high-impact** venues (impact factor, citations)"

Fixed structure (L32–39):
> 1. Abstract
> 2. Introduction
> 3. Literature Review
> 4. Tables and Figures
> 5. Conclusion
> 6. References

Formatting requirement (L41–43):
> "Formatting, organization, citation style, and presentation must follow ***Artificial Intelligence Review*** (Springer, journal no. 10462):
> - Citation style: **Springer Basic (numeric, brackets)** — in text `[1]`, `[1, 2]`, `[1–3]`; reference list entries like `Lastname FN (Year) Article title. Journal Name Volume(Issue):page range`
> - Aim for an AIR-like review anatomy: motivation + scope in the Introduction; a thematic Literature Review that groups, compares, and critically analyzes; comparison tables; research gaps and future directions; Conclusion. No formal research questions required — the brief is a plain supervisor-assigned review."

Marks distribution (L45–58, total 25%):

| Component | Marks |
|---|---|
| Abstract | 2% |
| Introduction | 3% |
| Literature Review | 10% |
| Tables and Figures | 3% |
| Conclusion | 2% |
| Formatting | 2% |
| References | 3% |
| **Total** | **25%** |

> "Implication: the Literature Review carries 40% of the assignment's marks — invest there." (L58)

Logistics (L60–64):
- **"Deadline: September 27, 2026"** (12 days from Sep 15 setup)
- **"Group size: maximum 10 — we are 8 members"**
- **"Weight: 25% of the course"**

Submission checklist (L66–73):
- [ ] Exactly 5 papers per journal, all 2025+, all four journals represented
- [ ] Every selected paper has an extraction note in `sources/`
- [ ] Tables and figures are numbered, captioned, and referenced from the text
- [ ] All in-text citations appear in the reference list and vice versa (numbers match)
- [ ] Citation style = Springer Basic (numeric, brackets) throughout
- [ ] Reads as synthesis/comparison/critique — no paper-by-paper summary structure

From `README.md` (L19–31) — the "Assignment at a glance" table: Deliverable = Literature review paper **"Big Data with Machine Learning: A Review"**; Format = Publication style of *Artificial Intelligence Review* (Springer); Sources = **"≥ 20 papers, 2025–2027, from 4 journals (≈3–5 each → exactly 5 per journal)"**; Components = Abstract · Introduction · Literature Review · Tables & Figures · Conclusion · References; Deadline = **September 27, 2026**; Team = 8; Weight = 25%.

The one rule README highlights (L56): the Literature Review (10%) must **"synthesize, compare, and critically analyze"** the 20 papers — "themes, contrasts, gaps — not 20 mini-summaries."

`notes/selection-backing.md` §1 provides a clause-by-clause inventory **R1–R19** (quoted from the PDF). Key IDs: R1 type = AI Review Paper · R2 title verbatim · R3 keywords · R4 period 2025–2027 · R5 ≥20 papers · R6 four journals only · R7 3–5 per source (met at exactly 5) · R8 BD+ML relevance · R9 date window · R10 WoS · R11 high-impact · R12 AIR format · R13 synthesize/compare/critique · R14 six components · R15 AIR citation style · R16 marks · R17 deadline · R18 ≤10 members · R19 25% weight.

---

## 2. Tracker state

### 2.1 `trackers/paper-tracker.md` — the per-paper master registry (target for Notion import)

Structure: header prose + "How to use it" + **Summary** (corpus / selection numbers / branches / access) + then three tables:
- **R1 — Master table: the 20 papers** (20 rows)
- **R2 — Claim-to-evidence ledger** (empty template; 1 placeholder row `C-01`)
- **Appendix A — BibTeX (20 entries)**
- **Appendix B — Reference strings, Springer Basic** (20 rows)
- **Appendix C — Alternates bench (29) and swap protocol**
- **Appendix D — Column dictionary**
- Revision log (1 row: rev 1, 2026-09-15).

**R1 master-table columns (exact header):**
`ID | Paper (DOI) | Year | Journal · type | Access | PDF | Reader | Read status | Method / platform † | Dataset & scale | Headline result | Limitations (theirs / ours) | Draft § | S2 · S5 | Notes`

**Filled vs empty:** Metadata filled for all 20 rows (ID, title+DOI, year, journal·type, access, and abstract-level `Method / platform †`). **Working columns are empty for 15 of 20 rows** (`Reader`, `Read status`, `Dataset & scale`, `Headline result`, `Limitations`, `Draft §`, `S2 · S5`, `Notes` all `—`). **Only 3 rows are filled:** **AIR-1, AIR-2, AIR-3** (Reader = Ikramul Hasan; Read status = Read; full content columns + `Draft §` + S2·S5 + a quotable line). PDF column populated only for AIR-1…AIR-5.

**R2 ledger columns:** `Claim ID | Claim (as written) | Backing paper(s) | Evidence (number + page/section) | Used in draft (§) | Checked by | Status` — **empty (placeholder only)**.

**Appendix D column dictionary — allowed values / owners:** `ID` (fixed), `Reader` (member name), `Read status` (`Not started · Skimmed · Read · Deep-read`), `Method / platform`, `Dataset & scale`, `Headline result`, `Limitations (theirs / ours)`, `Draft §` (`§3.3 methods · §3.4 platforms · §3.5 applications · §3.6 cross-cutting · §3.7 future`), `S2 · S5` (0/1/2 each), `Notes`, `Branch` (`B1…B5`), `Dates` (ISO). `†` = abstract-level value to verify; `—` = unfilled.

**Branch map (authoritative, Fig. 2):** B1 Scalable/interpretable methods = TBD-1, TBD-4, TBD-5, BDR-5, JoBD-5 (5) · B2 Platforms/pipelines = BDR-2, BDR-3, JoBD-4 (3) · B3 Applications/domains = BDR-1, BDR-4, JoBD-1, JoBD-3, AIR-2 (5) · B4 Foundation models/LLMs = TBD-2, TBD-3, AIR-1, AIR-3 (4) · B5 Privacy/governance/evaluation = JoBD-2, AIR-4, AIR-5 (3).

**Summary facts:** 20 papers; years 2025:12 · 2026:8 · 2027:0; 15 research + 5 AIR reviews (exception); 14 OA / 6 paywalled (TBD-1, TBD-2, TBD-3, TBD-5, BDR-3, BDR-5); citations 393 total (most-cited AIR-1 = 134); 20/20 Crossref-verified 2026-09-15. Selection funnel: retrieved 1519 (TBD 296 · BDR 101 · JoBD 480 · AIR 642) → keyword screen 441 (70/10/177/184) → Crossref-verified 49 (11/11/12/15) → included 20 (5/5/5/5).

### 2.2 `trackers/papers-pool.md`
Locked **rev 3 (2026-09-15)**. Four journal tables (5 rows each) with columns `# | Paper | Theme | Access | Verified`, plus per-journal **alternates** lists (29 total) and notes. Article-type policy block at top (original-research-only; AIR exception; AIR-A6…A10 insurance).

### 2.3 `trackers/writing-progress.md`
Table columns: `Component | Marks | Status | Owner | Notes`. **All statuses = `not started`** (10 rows: pool, extraction notes, Abstract 2%, Introduction 3%, Literature Review 10%, Tables and Figures 3%, Conclusion 2%, Formatting 2%, References 3%; owners are Member 6/7/8, Members 2–5 pods). Session log has 3 entries (all 2026-09-15), newest first.

### 2.4 `trackers/team-tasks.md`
8 members; Phase A journal pods (Pod 1 IEEE TBD = Members 1–2; Pod 2 BDR = 3–4; Pod 3 JoBD = 5–6; Pod 4 AIR = 7–8). Phase B roles (integration editor = Member 1; theme leads 2/3/5; T&F = 6; cross-cutting = 4; intro+conclusion = 7; formatting+refs+abstract = 8). Timeline Sep 15 → Sep 27 (target freeze Sep 26).

### 2.5 `trackers/notion-import/`
README documents **3 CSVs, one per Notion database**:
- `master.csv` — **20 rows**; columns (exact header): `ID,Title,DOI,Year,Journal,Type,Access,PDF,Note,Reader,Read status,Method / platform (abstract),Dataset and scale,Headline result,Limitations (theirs / ours),Draft section,S2,S5,Notes`. Same filled/empty split as R1 (metadata populated; working columns empty except AIR-1/2/3).
- `alternates.csv` — **29 rows**; columns: `ID,Title,Year,Journal,Access,DOI,Held for,Status` (all Verified Crossref 2026-09-15).
- `references.csv` — **20 rows**; columns: `ID,Reference string (Springer Basic),Flags,BibTeX key`.
Import instructions: Year→Number; Access/Read status/Draft section→Select; DOI/PDF→URL; Relation on ID. Regenerate via `python code/build_tracker.py`.

---

## 3. `sources/` notes — filled vs stub

**Template** (`sources/_template.md`) expected structure: `# Extraction note — <ID> <short title>`; **## Bibliographic** (Pool ID, Full citation Springer Basic, Journal/year, WoS indexed, Citations at access date); **## Content** (Problem/domain, Big-data context, ML methods, Data, Key findings ≤3 bullets, Limitations the authors admit, Limitations we see); **## Synthesis hooks** (Theme placement, Agrees with, Contradicts, Extends/enables, Unique contribution, Quotable line with page).

**5 topic groups (one per primary journal "pod"), 5 papers each = 20 notes:**

| Group | Journal | Notes |
|---|---|---|
| **AIR** | Artificial Intelligence Review | AIR-1, AIR-2, AIR-3, AIR-4, AIR-5 |
| **BDR** | Big Data Research | BDR-1, BDR-2, BDR-3, BDR-4, BDR-5 |
| **JoBD** | Journal of Big Data | JoBD-1, JoBD-2, JoBD-3, JoBD-4, JoBD-5 |
| **TBD** | IEEE Transactions on Big Data | TBD-1, TBD-2, TBD-3, TBD-4, TBD-5 |
| (5th) | — | There is **no fifth group**; the folder holds exactly these 20 (4 groups × 5). The tasking note "one more?" — the 5th is only the **template file `_template.md`**, not a paper group. |

**Filled vs stub (verified by search for the placeholder tokens `fill from full text` / `fill with page number`):**
- **FILLED (5):** **AIR-1, AIR-2, AIR-3** (complete Bibliographic + Content + Synthesis hooks, with page-cited quotes) — and, per `git status`, **AIR-4** and **TBD-4/TBD-5** show as *modified* working-tree files (AIR-1/2/4 and TBD-4/5 modified, AIR-3 already committed). Note: AIR-4, TBD-4, TBD-5 are recorded as modified but were not confirmed fully populated in this pass.
- **STUB (15):** the remaining notes contain a pre-filled Bibliographic block + Content skeleton (title/theme/abstract where indexed) but **empty "Synthesis hooks"** with literal placeholders. Confirmed stubs: **TBD-1, TBD-2, TBD-3, TBD-4, TBD-5, BDR-1, BDR-2, BDR-3, BDR-4, BDR-5, JoBD-1, JoBD-2, JoBD-3, JoBD-4, JoBD-5, AIR-5** (16 files matched the placeholder search; TBD-4/TBD-5 counted here as their hooks still carry placeholders).

**Filenames (exact):** `AIR-1_agentic-ai-a-comprehensive.md` · `AIR-2_artificial-intelligence-advances-in.md` · `AIR-3_from-classical-machine-learning.md` · `AIR-4_review-of-generative-ai.md` · `AIR-5_a-survey-of-deep.md` · `BDR-1_explainable-malware-detection-through.md` · `BDR-2_efficient-training-federated-learning.md` · `BDR-3_opinion-fraud-detection-on.md` · `BDR-4_heterogeneous-graphbased-risk-assessment.md` · `BDR-5_largescale-least-squares-regression.md` · `JoBD-1_a-deep-learningbased-framework.md` · `JoBD-2_a-privacyenhanced-framework-for.md` · `JoBD-3_advancing-multimodal-emotion-recognition.md` · `JoBD-4_cloud-based-realtime-multivariate.md` · `JoBD-5_graph-neural-network-approach.md` · `TBD-1_pexp-a-scalable-parallel.md` · `TBD-2_tsmllm-a-multimodal-large.md` · `TBD-3_graphllm-boosting-graph-reasoning.md` · `TBD-4_knowledge-aggregation-transformer-network.md` · `TBD-5_enhanced-approaches-for-anomaly.md`.

---

## 4. AIR journal LaTeX template

**Location (in-workspace, not external):** `AIR_Journal_Template/sn-article-template/` (repo root → `AIR_Journal_Template/` → `sn-article-template/`).

**All files inside:**
- `sn-article.tex` — main template (Version 3.1, December 2024)
- `sn-jnl.cls` — the document class (`\ProvidesClass{sn-jnl}`, line 55)
- `sn-bibliography.bib` — sample bib (165 lines; entries `bib1`…`bib13`+ illustrating article/book/incollection/etc.)
- `bst/` — 9 bibliography styles: `sn-apacite.bst`, `sn-aps.bst`, `sn-basic.bst`, `sn-chicago.bst`, `sn-mathphys-ay.bst`, `sn-mathphys-num.bst`, `sn-nature.bst`, `sn-vancouver-ay.bst`, `sn-vancouver-num.bst`
- `sn-article.pdf` (compiled sample), `user-manual.pdf` (Springer Nature User Manual)
- `fig.eps`, `empty.eps` (sample graphics)

**Document class used in the shipped template (exact line 33):**
```latex
\documentclass[pdflatex,sn-mathphys-num]{sn-jnl}% Math and Physical Sciences Numbered Reference Style
```
(Commented alternatives in the file: `sn-basic`, `sn-nature`, `sn-mathphys-ay`, `sn-aps`, `sn-vancouver-num`, `sn-vancouver-ay`, `sn-apa`, `sn-chicago`, plus `referee`/`lineno` options. Class defines reference-style switches for `sn-basic`, `sn-mathphys` (num/ay), etc.)

**Discrepancy to resolve:** `notes/requirements.md` specifies **"Springer Basic (numeric, brackets)"** for citations, which corresponds to `\documentclass[...]{sn-jnl}` with option **`sn-basic`** (i.e. `\bibliographystyle{sn-basic}`). The template's default is **`sn-mathphys-num`**. For a big-data/ML review, either satisfies "numeric, brackets"; the assignment text names **Springer Basic**, so `sn-basic` is the safer literal match. **Decision needed before the LaTeX draft.**

**Required packages (from `sn-article.tex` L44–57):** `graphicx`, `multirow`, `amsmath`, `amssymb`, `amsfonts`, `amsthm`, `mathrsfs`, `[title]{appendix}`, `xcolor`, `textcomp`, `manyfoot`, `booktabs`, `algorithm`, `algorithmicx`, `algpseudocode`, `listings`.

**Required front-matter fields / commands:** `\title[Article Title]{Article Title}` · authors via `\author*[1,2]{\fnm{First} \sur{Author}}\email{...}` (with `\spfx{}` particle, `\sfx{}` suffix) · `\affil*[1]{\orgdiv{...}\orgname{...}\orgaddress{\street{} \city{} \postcode{} \state{} \country{}}}` · `\abstract{...}` (or structured `\abstract{\textbf{Purpose:}...}`) · `\keywords{k1, k2, ...}` · optional `\pacs[JEL/MSC]{}` · `\maketitle`.

**Structural / formatting rules to follow:**
- **One single `.tex` file** — "Please do not use `\input{...}` to include other tex files. Submit your LaTeX manuscript as one .tex document." (L6–7). Figures/files attached separately, not embedded.
- Sections: `\section{}` / `\subsection{}` / `\subsubsection{}`; Introduction **must not include subheadings** (L146).
- Backmatter: `\backmatter` then `\bmhead{Supplementary information}`, `\bmhead{Acknowledgements}`, `\section*{Declarations}` (Funding · Conflict of interest · Ethics approval · Consent for publication · Data availability · Materials availability · Code availability · Author contribution — write "Not applicable" where irrelevant). Appendices via `\begin{appendices}`.
- Bibliography: `\bibliography{sn-bibliography}` (class uses `natbib`; supports numeric + author-year). Tables use `booktabs` (`\toprule/\midrule/\botrule`); wide tables → `table*` or `sidewaystable`; figures eps for latex / pdf-jpg-png for pdflatex; equations via `equation`/`align`.
- The template is the generic **Springer Nature** class, not AIR-specific — the assignment maps AIR's style onto it.

---

## 5. Requested skills — availability + paths

Workspace has **no local skills dir**; skills live in the user profile. Directories checked: `C:\Users\User\.roo\skills` (**exists**), `C:\Users\User\.agents\skills` (**exists**), `C:\Users\User\.claude\skills` (**exists**), `C:\Users\User\.zcode\skills` (**exists**), `C:\Users\User\.agent` (**does NOT exist**).

Every requested skill **exists with a `SKILL.md`** in `.agents`, `.claude`, and `.zcode` (`.roo` does **not** carry the research-writing set). Full paths (`.agents` is the canonical one for this mode):

| Skill | `C:\Users\User\.agents\skills` | `.claude\skills` | `.zcode\skills` | `.roo\skills` |
|---|---|---|---|---|
| deep-research | ✅ `...\.agents\skills\deep-research\SKILL.md` | ✅ | ✅ | ❌ |
| idea-evaluator | ✅ `...\.agents\skills\idea-evaluator\SKILL.md` | ✅ | ✅ | ❌ |
| paper-writer | ✅ `...\.agents\skills\paper-writer\SKILL.md` | ✅ | ✅ | ❌ |
| intro-drafter | ✅ `...\.agents\skills\intro-drafter\SKILL.md` | ✅ | ✅ | ❌ |
| humanizer | ✅ `...\.agents\skills\humanizer\SKILL.md` | ✅ | ✅ | ❌ |
| figure-designer | ✅ `...\.agents\skills\figure-designer\SKILL.md` | ✅ | ✅ | ❌ |
| paper-polish | ✅ `...\.agents\skills\paper-polish\SKILL.md` | ✅ | ✅ | ❌ |
| pre-submission-reviewer | ✅ `...\.agents\skills\pre-submission-reviewer\SKILL.md` | ✅ | ✅ | ❌ |
| *(extra)* tech-paper-template | ✅ `...\.agents\skills\tech-paper-template\SKILL.md` | ✅ | ✅ | ❌ |

Related supporting skills also present in `.agents`: `research-paper-writing`, `rebuttal-guidance`, `benchmark-paper-template`, `latex-posters`, `doc-coauthoring`, `scientific-slides`, `make-pdf`, `paper-…` (all under `C:\Users\User\.agents\skills\`). `.roo` carries the engineering/design skills (brainstorming, writing-plans, verification-before-completion, etc.) but not the paper-writing suite.

---

## 6. Git state

- **Branch:** `main`; **"Your branch is ahead of 'origin/main' by 2 commits."**
- **Recent history (`git log --oneline -20`):**
  - `67ff332 docs(trackers): record AIR-3 extraction data and assign reader`
  - `4684a66 docs(sources): complete extraction note and synthesis hooks for AIR-3`
  - `aca07c5 rev 3: original-research-only enforcement per supervisor clarification`
  - `f21a999 README: add team getting-started section (clone, workflow, trackers)`
  - `f065bba Initial commit: Big Data + ML review workspace (20-paper verified pool, selection backing, synthesis, trackers)`
- **Uncommitted changes:** yes.
  - **Modified (tracked):** `README.md`, `sources/AIR-1_agentic-ai-a-comprehensive.md`, `sources/AIR-2_artificial-intelligence-advances-in.md`, `sources/AIR-4_review-of-generative-ai.md`, `sources/TBD-4_knowledge-aggregation-transformer-network.md`, `sources/TBD-5_enhanced-approaches-for-anomaly.md`.
  - **Untracked:** `AIR_Journal_Template/`, `code/build_tracker.py`, `notes/notion-field-values-air2-air3.md`, `notes/paper-breakdown-AIR-2-AIR-3.md`, `notes/relevance-and-readability-audit.md`, `paper/air-1-s10462-025-11422-4.pdf`, `paper/air-2-s10462-025-11108-x.pdf`, `paper/air-3-s10462-026-11522-9.pdf`, `paper/references.bib`, `papers/`, `trackers/notion-import/README.md`, `trackers/notion-import/alternates.csv`, `trackers/notion-import/references.csv`.
- **`.gitignore`:** `archive/` (unpublished old project), `__pycache__/`, `*.pyc`, `.venv/`, `venv/`, `.DS_Store`, `Thumbs.db`, `desktop.ini`, `*.swp`.
- **`.gitattributes`:** `* text=auto eol=lf`, `*.pdf -text`, `*.png binary`, `*.jpg binary`.

---

## 7. Other context worth carrying forward

- **`paper/outline.md`** fixes components 1–6 with section codes: §3.1 background · §3.2 taxonomy (Fig. 2) · §3.3 scalable ML methods · §3.4 platforms/pipelines · §3.5 applications/domains · §3.6 cross-cutting · §3.7 future directions. Tables 1–2 + Figs 1–3 minimum. Writing order: Table 1/Fig. 1 → §3.3–3.5 → §3.6–3.7 → §3.1–3.2 → Intro → Conclusion → Abstract → references → formatting.
- **`notes/landscape-report.md`** is the full pre-written synthesis (abstract, taxonomy, five branches with comparison tables, cross-branch synthesis, open problems, conclusion) using **pool-ID numbering [1]–[20] = TBD-1…AIR-5**. It also names branches as B1–B5.
- **`notes/paper-breakdown-AIR-2-AIR-3.md`** — deep defence dossiers for AIR-2/AIR-3 (page-cited quotes, numbers to memorise, supervisor Q&A, traps).
- **`notes/notion-field-values-air2-air3.md`** — ready-to-paste Notion cell values for AIR-2 (`Agrees with`, `Disagrees with` only) and the full AIR-3 row.
- **`notes/relevance-and-readability-audit.md`** — difficulty + big-data-substance audit; flags 6 paywalled papers and "too advanced" papers, with re-scored swap candidates (recommends TBD-3 → TBD-A5, etc.).
- **`paper/references.bib`** — **20 `@article` entries**, keys: `jiang2026pexp`, `wang2026mllm`, `chai2025graphllm`, `xiao2025katn`, `gunbilek2026enhanced`, `mohammadian2025explainable`, `teixeira2025efficient`, `ghodsi2026opinion`, `liu2026heterogeneous`, `li2026large`, `elfouly2025deep`, `haripriya2025privacy`, `wafa2025advancing`, `saleh2025cloud`, `zhang2025graph`, `abouali2025agentic`, `edozie2025telecom`, `muneer2026classical`, `waseem2025synthetic`, `vats2026survey`. Several carry `% TODO` flags (verify volume/issue/article number/compound surnames).
- **`paper/drafts/` and `paper/sections/` are empty** (no manuscript drafted yet). `figures/` and `code/src`, `code/tests` were not populated. `results/` holds `table1.csv`, `pool_selected.json`, `openalex_raw/*.json`, `screen/*.csv`.

---

## 8. Gaps / risks

1. **Tracker is 15/20 empty.** Only AIR-1/2/3 rows are complete; the other 17 working-column cells (Reader, Read status, Dataset & scale, Headline result, Limitations, Draft §, S2·S5, Notes) need filling. R2 claim ledger is entirely empty.
2. **15 of 20 source notes are stubs** with placeholder "Synthesis hooks" — the extraction work the assignment requires ("Every selected paper has an extraction note") is not yet done for TBD-1…5, BDR-1…5, JoBD-1…5, AIR-5.
3. **No manuscript exists yet** — `paper/sections/` and `paper/drafts/` are empty; only the outline and the landscape report (a synthesis, not the paper) exist.
4. **Template class mismatch to decide:** requirement says **Springer Basic (numeric brackets)** → `sn-basic`; template default is **`sn-mathphys-num`**. Pick one before drafting.
5. **Six paywalled papers** (TBD-1, TBD-2, TBD-3, TBD-5, BDR-3, BDR-5) — content extraction blocked without institutional access; designated OA swaps exist (TBD-A5; BDR-A1/A2).
6. **AIR review-article exception** is a live compliance risk; insurance swaps AIR-A6…A10 are pre-verified but must be recorded if used (never substitute silently).
7. **Citation-numbering convention conflict:** all existing notes/reports use pool-ID numbering (`[1]`=TBD-1 … `[20]`=AIR-5), but the final paper must number by **order of first appearance**. All `[n]` must be re-keyed at assembly.
8. **Uncommitted / untracked work** (incl. whole `AIR_Journal_Template/`, `papers/`, `references.bib`, several notes) — not yet pushed; branch is 2 commits ahead of origin.
9. **2027 papers do not exist** — period is satisfied as far as possible; the methodology must state the 2027-availability check.
10. **Thin metadata** for BDR-3/BDR-4/BDR-5 (no indexed abstracts) and most abstracts lack evaluation specifics — `Dataset & scale`, `Headline result`, `Limitations` must come from full texts.
