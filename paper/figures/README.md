# Figures — "Big Data with Machine Learning: A Review"

Publication-quality, original figures for the review (`sn-jnl`, compiled with
**pdflatex**). Generated reproducibly from [`make_figures.py`](make_figures.py);
every plotted value is traceable to a source note via
[`fig-data-source.md`](fig-data-source.md).

Reproduce all figures:

```
python paper/figures/make_figures.py
```

Requires `matplotlib` and `numpy`. Each figure is written as **`.pdf`** (vector,
for pdflatex) and **`.png`** (300 dpi, for preview).

> **Important — citation numbers, not pool IDs.** Figures label papers with the
> manuscript's bracketed citation numbers `[1]`–`[20]`
> (`notes/writing-plan.md` §3.2), because the manuscript cites by number.
> Internal pool IDs (TBD-x / AIR-x) are never shown in a figure. The mapping
> `[n] ↔ pool ID` is in [`fig-data-source.md`](fig-data-source.md).

---

## Figure inventory

| Fig | File | Type (figure-designer) | Paradigm | Intended section | Width | R2 claims supported |
|---|---|---|---|---|---|---|
| 1 | `fig1_corpus_landscape.pdf/.png` | Motivated example | Scatter-map (Existing-vs-Ours variant) | Introduction (problem framing) / §3.5 | two-column `figure*` (~7 in) | C-07, C-13, C-15, C-16 |
| 2 | `fig2_taxonomy.pdf/.png` | Solution overview | Taxonomy / map | §3.2 | two-column `figure*` (~7 in) | C-01, C-02, C-21 |
| 3 | `fig3_evidence_anchors.pdf/.png` | Experimental results | Grouped-bar + point-anchor with NA band | §3.3 / §3.6 | two-column `figure*` (~7 in) | C-03, C-06, C-09, C-19 |
| 4 | `fig4_method_shift.pdf/.png` | Supporting (experimental-results base) | Stacked bar | §3.3 (method arc) | single-column `figure` (~3.5 in) | C-01, C-02 |
| 5 | `fig5_selection_flow.pdf/.png` | Supporting (motivated-example base) | PRISMA-style funnel | Introduction (selection method) | single-column `figure` (~3.6 in) | (methodology; no R2 numeric claim) |

All five are cited from the running text (`Figure~\ref{figN}`) per
`notes/air-format-spec.md` §3.7/§4.

---

## Per-figure design notes and limitations

### Fig. 1 — Corpus landscape (motivated example)
- **Job:** make the review's problem visible in one glance — the corpus splits
  into "learning on more data" (accuracy-led, bottom band) and "learning under
  constraints" (privacy / platform / proof, shaded upper band).
- **Encoding:** colour = journal; marker = research (circle) vs review (square);
  x = data scale/kind; y = binding constraint. Journal identity and article
  type are exact; the two axis positions are **curated design coordinates**
  justified point-by-point in `fig-data-source.md`.
- **Limitations:** axis positions are a defensible *interpretation* of the
  notes, not measured values — the figure is a framing device, and the
  coordinates are documented so a reviewer can challenge them. Some categories
  are deliberately coarse.

### Fig. 2 — Taxonomy (solution overview / the map)
- **Job:** the organising scheme. Two axes (Axis 1 what is learned; Axis 2 what
  surrounds the learning) and five branches B1–B5, with all 20 papers placed
  exactly once, plus the documented empty cells.
- **Encoding:** branch boxes with journal-coloured chips; each chip is a
  citation number. Total = 5+3+5+4+3 = 20.
- **Limitations:** the branch assignment is *our* classification of *this*
  curated corpus (landscape §2 curation caveat), not raw field proportions.
  Branch labels are thematic, not measured.

### Fig. 3 — Reported-result anchors (experimental results)
- **Job:** put the corpus's headline numbers side by side **without hiding the
  evidence gap**. Panel (a) = classification/detection percentages; panel (b) =
  regression RMSE, with the only reported→reproduced pair.
- **Honest-missing treatment:** papers with no comparable metric are shown as an
  explicit text band ("No comparable metric available: [4], [5], [8], [12],
  [15], [16]") and "Qualitative claims only: …" — **never plotted as zero**.
- **Encoding:** colour+hatch = evidence tier; 300-dpi legible; axis starts at 0
  with value labels (no truncated exaggeration).
- **Limitations:** values come from **different datasets and metrics** and are
  therefore *anchors, not a like-for-like leaderboard* — this is stated on the
  figure and is the honest reading. Abstract-only values are threshold values
  (e.g. ">94%") plotted at the threshold and hatched to mark them as
  non-precise. JoBD-3's [14] 99.8% is plotted at face value but is flagged
  (C-09) as anomalously high; the caption should note this.

### Fig. 4 — Method-generation shift (supporting trend)
- **Job:** visualise the classical → deep → LLM/foundation-model shift across
  the corpus, broken down by journal.
- **Encoding:** stacked bars per journal; "Not specified" kept visible rather
  than guessed.
- **Limitations:** the generation label is a **curated classification** per
  paper (documented in `fig-data-source.md`); BDR-3 is "Not specified" because
  its abstract is not indexed (C-14). Small n per journal (5) — read counts,
  not proportions with false precision.

### Fig. 5 — Selection flow (PRISMA-style funnel)
- **Job:** the Introduction's selection-method paragraph, showing
  1,519 → 441 → 49 → 20 with a per-journal split.
- **Encoding:** log-scaled x (labelled on the axis, honest-axis rule); counts
  printed as `n = …`.
- **Limitations:** shows retrieval/screening/inclusion only — the detailed
  inclusion/exclusion *reasons* live in the tracker, not in the figure. Purely
  descriptive; carries no performance claim.

---

## figure-designer quality-control audit

Universal rules (`figure-designer/references/design-rules.md`) applied to every
figure. `[inspection]` = verified from the generated output; `[user-verify]` =
needs confirmation against paper context.

| Rule | Fig.1 | Fig.2 | Fig.3 | Fig.4 | Fig.5 |
|---|---|---|---|---|---|
| Vector format (PDF) **and** 300-dpi PNG | pass | pass | pass | pass | pass |
| Font ≥ 8 pt post-scaling (labels) | pass | pass | pass | pass | pass |
| Small canvas, proportional fonts | pass | pass | pass | pass | pass |
| Colour-blind-safe palette (Okabe-Ito) | pass | pass | pass | pass | pass |
| Dual encoding (colour **+** shape/hatch) | pass | pass | pass | pass (labels) | pass |
| Self-contained caption (finding first) | pass* | pass* | pass* | pass* | pass* |
| Honest axes / no zero-as-missing | pass | n/a | pass | pass | pass (log labelled) |
| No 3D / no chartjunk / no gradients | pass | pass | pass | pass | pass |
| Labels are real entities (no placeholders) | pass | pass | pass | pass | pass |
| No pool IDs leaked into the figure | pass | pass | pass | pass | pass |

\* Captions are drafted at manuscript-assembly time (out of this subtask's
scope); the required finding-first caption text is specified per figure above.

**Integrity-gate result (skill Step 7):** all seven checks pass for figures
1–3 and 5; figure 4 passes with the noted small-n caveat. No CRITICAL
violation remains.

**Severity summary: 0 CRITICAL, 1 MAJOR, 2 MINOR.**
- **MAJOR (Fig. 3):** the cross-paper comparison mixes datasets/metrics by
  design. **Action:** the manuscript caption must state "values are not
  like-for-like; they are reported anchors" and must flag [14] (JoBD-3) as
  anomalously high (C-09). Do **not** quote Fig. 3 as a SOTA ranking.
- **MINOR (Fig. 1):** axis coordinates are curated. **Action:** keep
  `fig-data-source.md` with the submission so the placement is auditable.
- **MINOR (Fig. 4):** n = 5 per journal. **Action:** read as counts.

### Items the team must confirm before submission `[user-verify]`
1. Fig. 1's curated axis placements match how §3.5 describes the "big-data label
   loosens" finding (C-07).
2. Fig. 3's "not available" lists match the final full-text-access state — if
   BDR-3/BDR-5/TBD-1/2/3 later gain full text, values must be added and the
   tier recoloured.
3. The five figures are each referenced at least once in the running text
   (consistency check, writing-plan §4).

---

## Files

| File | Role |
|---|---|
| `make_figures.py` | Reproducible generator (matplotlib, no external data files). |
| `fig-data-source.md` | Full value → citation number → pool ID → source-note traceability. |
| `fig{1..5}_*.pdf` | Vector figures for pdflatex. |
| `fig{1..5}_*.png` | 300-dpi previews. |
| `README.md` | This file (inventory + QC audit). |
