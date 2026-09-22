# Writing progress — mapped to assignment components and marks

Marks in brackets. Update the status table at the end of every work session.

| Component | Marks | Status | Owner | Notes |
|---|---|---|---|---|
| Paper pool: 20 locked (5/journal) | — | complete (2026-09-22) | pods | 20/20 Crossref-verified, 5 per journal (`trackers/papers-pool.md`) |
| Extraction notes ×20 | — | complete (2026-09-22) | pods | 20 per-paper notes in `sources/` (AIR×5, BDR×5, JoBD×5, TBD×5) |
| Abstract | 2% | complete (2026-09-22) | Member 8 | accurate, 185 words; no citations/equations; written last |
| Introduction | 3% | complete (2026-09-22) | Member 7 | context + scope + selection funnel + AIR exception + organization (no formal RQs) |
| Literature Review | **10%** | complete (2026-09-22) | Members 2, 3, 4, 5 | all 20 papers; 7 subsections (§2.1–§2.7) |
| Tables and Figures | 3% | complete (2026-09-22) | Member 6 | Table 1 (20-paper corpus summary); Table 2 (taxonomy mapping); 5 figures (all cited) |
| Conclusion | 2% | complete (2026-09-22) | Member 7 | recap + 3 takeaways + scope limits; no new citations |
| Formatting (AIR style) | 2% | complete (2026-09-22) | Member 8 | `sn-jnl` class, `sn-basic` numeric, Springer Basic compliant |
| References | 3% | complete (2026-09-22) | Member 8 | 20 Springer Basic entries; 20/20 resolve both ways |
| Supporting artifacts | — | complete (2026-09-22) | team | source notes, tracker, thesis/structure, writing plan, figures, polish log, compliance review |

## Session log (append, newest first)

- 2026-09-22 — **reconciliation + documentation.** Fixed the two internal count inconsistencies found by the compliance review: the B3 "largest, with eight papers" claim (line ~118) is now "one of the corpus's two largest branches, with five papers"; the B1 "A sixth item" sentence (line ~90) now treats the multimodal review as cross-referenced from B4 rather than counted as a sixth B1 member. Counts were re-derived from Table 2 (B1 5 / B2 3 / B3 5 / B4 4 / B5 3 = 20). Recompiled clean (23 pages, 20 references, 5 figures, 2 tables, 0 undefined refs). Added `notes/PROJECT-PROGRESS.md` (pipeline checklist, artifact map, git history, remaining human decisions, AI-assistance disclosure).
- 2026-09-22 — **compliance review + pre-submission fixes.** pre-submission-reviewer checklist (30 items) run; fixed CRITICAL Table 1 clipping and MAJOR Table 2 overflow by converting both to page-breaking `xltabular`; recorded two unfixed count inconsistencies (B3 count, B1 member count) as content decisions. See `notes/compliance-review.md`.
- 2026-09-22 — **polish pass.** humanizer + paper-polish clarity pass over the draft; recompiled. See `notes/polish-log.md`.
- 2026-09-22 — **manuscript drafted + compiled.** Full single-file `paper/manuscript.tex` written to `sn-jnl`/`sn-basic` (numeric); sections assembled per `notes/writing-plan.md`; compiled to PDF.
- 2026-09-22 — **figures + references + plan.** Figures 1–5 generated from the 20-paper evidence (`paper/figures/`); `paper/references.bib` populated with 20 Springer Basic entries in first-appearance order; organizing thesis, MECE outline, writing plan, and citation order recorded (`notes/thesis-and-structure.md`, `notes/writing-plan.md`).
- 2026-09-15 — **rev 3: original-research-only enforcement.** Supervisor clarified "research papers" = original research articles. TBD-2 (blockchain-FL survey) → TS-MLLM (LLM for industrial time-series big data, original research); JoBD-1 (multi-domain benchmark survey) → large-scale plant-disease detection (original research). AIR's five review articles kept as documented exception + AIR-A6…A10 research-only insurance swaps prepared. 20/20 re-verified; dossier, report, pool tracker updated; workspace pushed to GitHub.
- 2026-09-15 — **requirements re-analysis + pool rev 2**: PDF re-audited clause-by-clause (R1–R19 inventory in `notes/selection-backing.md`); 2 swaps for stronger requirement evidence (BDR-4 → heterogeneous-graph finance/Company Big Data; JoBD-3 → multimodal emotion recognition in big data); 20/20 re-verified via Crossref; alternates 24; per-paper requirement backing written; landscape report updated to rev 2.
- 2026-09-15 — **deep-research run complete**: 1,519 works pulled from the four journals (2025+), screened; 20 papers selected, 5/journal, 20/20 Crossref-verified. Landscape report written (`notes/landscape-report.md`), pool locked (`trackers/papers-pool.md`), Table 1 data (`results/table1.csv`), 20 extraction notes pre-filled (`sources/`). 6 papers need institutional access (swap rules in pool tracker).
