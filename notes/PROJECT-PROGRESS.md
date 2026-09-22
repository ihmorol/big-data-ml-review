# Project Progress — "Big Data with Machine Learning: A Review"

*Project tracking document. Produced 2026-09-22 by the FINAL RECONCILIATION + DOCUMENTATION subtask.*

This document is the single place to see what was produced, where every artifact lives, how the work was sequenced, and what still needs a human decision before submission.

---

## 0. AI-assistance disclosure

**This project was produced with AI assistance.** It is a research draft — a literature review of 20 papers — assembled by AI agents working from the team's own source notes, and it is **intended to be reviewed and rewritten by the human team** before it is submitted for assessment.

Concretely:

- The literature review prose, taxonomy, figures, tables, and LaTeX were generated with AI assistance under human-authored planning documents (`notes/requirements.md`, `notes/thesis-and-structure.md`, `notes/writing-plan.md`).
- Every load-bearing number in the manuscript traces to the team's per-paper extraction notes in `sources/`, which record values from indexed abstracts and full texts. The AI did not invent datasets, metrics, results, or citations.
- The **assignment bans AI use.** Under that policy this draft cannot be submitted as-is: the team must (a) disclose the AI assistance per the course's stated process, and (b) rewrite the content in the team's own words so the submitted work is the team's. See §4.
- Treat the manuscript as a scaffold and evidence base, not as a finished submission.

---

## 1. Pipeline checklist

The full pipeline, in order, with status and the artifact each step produced. Every step below is **done** as of 2026-09-22.

| # | Step | Status | Artifact |
|---|---|---|---|
| 1 | Recon of the assignment, requirements, and journal expectations | done | [`notes/recon-report.md`](notes/recon-report.md), [`notes/requirements.md`](notes/requirements.md), [`notes/landscape-report.md`](notes/landscape-report.md) |
| 2 | AIR format spec (class line, reference style, section/table/figure rules) | done | [`notes/air-format-spec.md`](notes/air-format-spec.md), [`notes/paper-breakdown-AIR-2-AIR-3.md`](notes/paper-breakdown-AIR-2-AIR-3.md) |
| 3 | Deep research of all 20 papers → per-journal/per-paper notes | done | [`sources/`](sources/) (AIR×5, BDR×5, JoBD×5, TBD×5) |
| 4 | Tracker population (master table, claim ledger, pool, team tasks) | done | [`trackers/paper-tracker.md`](trackers/paper-tracker.md), [`trackers/papers-pool.md`](trackers/papers-pool.md), [`trackers/team-tasks.md`](trackers/team-tasks.md) |
| 5 | Thesis and structure (organizing claim, MECE outline, branch map) | done | [`notes/thesis-and-structure.md`](notes/thesis-and-structure.md) |
| 6 | Writing plan (sequence, per-section specs, citation order) | done | [`notes/writing-plan.md`](notes/writing-plan.md), [`paper/outline.md`](paper/outline.md) |
| 7 | References file (20 Springer Basic entries, first-appearance order) | done | [`paper/references.bib`](paper/references.bib) |
| 8 | Figures (corpus landscape, taxonomy, evidence anchors, method shift, selection flow) | done | [`paper/figures/`](paper/figures/) + [`paper/figures/fig-data-source.md`](paper/figures/fig-data-source.md) |
| 9 | Manuscript draft (single-file LaTeX, six fixed components) | done | [`paper/manuscript.tex`](paper/manuscript.tex) |
| 10 | Compile (pdflatex → bibtex → pdflatex ×2) | done | [`paper/manuscript.pdf`](paper/manuscript.pdf), [`paper/manuscript.bbl`](paper/manuscript.bbl) |
| 11 | Polish (humanizer + paper-polish clarity pass) | done | [`notes/polish-log.md`](notes/polish-log.md) |
| 12 | Compliance review (30-item checklist + pre-submission findings) | done | [`notes/compliance-review.md`](notes/compliance-review.md) |
| 13 | Reconciliation (fix two internal count inconsistencies) | done | this run — edits in [`paper/manuscript.tex`](paper/manuscript.tex) |
| 14 | Documentation (this progress document + writing tracker) | done | [`notes/PROJECT-PROGRESS.md`](notes/PROJECT-PROGRESS.md), [`trackers/writing-progress.md`](trackers/writing-progress.md) |

---

## 2. Where things live

| What | Path |
|---|---|
| Manuscript (LaTeX source) | [`paper/manuscript.tex`](paper/manuscript.tex) |
| Manuscript (compiled PDF) | [`paper/manuscript.pdf`](paper/manuscript.pdf) |
| Compiled bibliography | [`paper/manuscript.bbl`](paper/manuscript.bbl) |
| BibTeX references | [`paper/references.bib`](paper/references.bib) |
| Figures (PDF + PNG + generator script) | [`paper/figures/`](paper/figures/) — see [`make_figures.py`](paper/figures/make_figures.py) and [`fig-data-source.md`](paper/figures/fig-data-source.md) |
| Source notes (20 papers, per-paper extraction) | [`sources/`](sources/) |
| Trackers (pool, paper tracker, team tasks, writing progress) | [`trackers/`](trackers/) |
| Planning and review notes | [`notes/`](notes/) — includes `requirements.md`, `recon-report.md`, `landscape-report.md`, `air-format-spec.md`, `thesis-and-structure.md`, `writing-plan.md`, `polish-log.md`, `compliance-review.md`, and this file |
| Selection/analysis code | [`code/`](code/), [`results/`](results/) |
| AIR template + class/bst files | [`AIR_Journal_Template/`](AIR_Journal_Template/); class/bst also copied alongside the manuscript in `paper/` |
| Locked corpus PDFs | [`papers/AIR/`](papers/AIR/), [`papers/TBD/`](papers/TBD/) |

---

## 3. Git history

`git log --oneline`, newest first (as of this run):

```
f26a517 review(paper): AIR/Springer compliance verification + pre-submission review; fixes
5aa1d9b style(paper): humanizer + paper-polish clarity pass; recompiled
257bb26 feat(paper): draft full manuscript (sn-jnl, Springer Basic numeric) + compiled PDF
61c3feb docs(figs): add figures 1-3 (corpus landscape, taxonomy, results) from 20-paper evidence
b2b1802 docs(refs): populate references.bib with 20 Springer Basic entries (ordered by first appearance)
7698107 docs(plan): organizing thesis, MECE outline, writing plan + citation order
842964b docs(trackers): populate paper-tracker working columns + R2 claim-evidence ledger from 20 source notes
82dc1a4 docs(sources): complete AIR-4/AIR-5 notes; verify all 20 source notes
e97d548 docs(sources): complete JoBD-1..5 source notes (grounded in indexed abstracts)
fad4464 docs(sources): complete BDR-1..5 source notes (grounded in indexed abstracts)
37b11eb docs(sources): complete TBD-1..5 source notes (grounded in indexed abstracts)
81fe286 docs: recon report + AIR journal format spec (sn-basic) baseline
67ff332 docs(trackers): record AIR-3 extraction data and assign reader
4684a66 docs(sources): complete extraction note and synthesis hooks for AIR-3
aca07c5 rev 3: original-research-only enforcement per supervisor clarification
f21a999 README: add team getting-started section (clone, workflow, trackers)
f065bba Initial commit: Big Data + ML review workspace (20-paper verified pool, selection backing, synthesis, trackers)
```

The **reconciliation + documentation commit** for this run is listed in the completion report (it is the newest commit after this document was written).

---

## 4. Remaining work / human decisions

These items require a human decision and are **not** resolved by the AI draft.

1. **Replace the placeholder author/affiliation block.** `paper/manuscript.tex` lines ~40–49 carry placeholder authors ("Author One" … "Author Eight") with `author.*@example.edu`, and a placeholder affiliation. These must be replaced with the real author list, emails, and affiliation before submission. (The AI did not fill these in, since inventing names would fabricate authorship.)
2. **Confirm the AIR review-article exception with the supervisor.** The corpus contains five Artificial Intelligence Review items that are *review articles*, kept as a **documented exception** to the "research papers = original research articles" clarification. If the exception is not accepted, a re-anchoring of the affected sections is required (insurance swaps AIR-A6…A10 exist). Confirm before submission.
3. **Retrieve full texts for the abstract-level items.** BDR-3, BDR-4, BDR-5 have no indexed abstract, and several TBD/AIR items are paywalled and described at abstract level only. Retrieving the full texts would let the team remove the "abstract-level" caveats and strengthen the reported evidence. Until then, those items are described at the level their available evidence supports, with no unverified numbers.
4. **Disclose AI use and rewrite in the team's own words.** **The assignment bans AI use.** The team must follow the course's disclosure policy and rewrite the manuscript content in their own words so the submitted work is the team's own. See §0.

Optional (non-blocking, from the compliance review): the single `yet` at line ~59 (below the banned-vocabulary threshold) and cosmetic residual table/PDF-outline warnings.
