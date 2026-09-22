# Polish Log — CLARITY / EDITING-POLISH pass on `paper/manuscript.tex`

*Produced 2026-09-22 by a CLARITY / EDITING-POLISH subtask. Method: `humanizer` (AI-tone removal) + `paper-polish` (grammar, flow, and tone calibration while preserving the author's meaning and evidence strength) applied in combination.*

**Scope actually edited:** `paper/manuscript.tex` only (plus this log and the rebuilt `paper/manuscript.pdf`). No change to `sources/`, `trackers/`, `paper/references.bib`, `paper/figures/`, or `paper/sn-*.{cls,bst}`. Section structure/names, `\documentclass`, all `\cite`/`\citep` keys, all `\label`/`\ref`, table contents, figure includes, the declarations, and the abstract's factual content were left untouched.

---

## 1. Summary of the corpus state and what was removed

The manuscript arrived **already unusually clean** of the heavy AI-tone lexicon. A pre-pass scan confirmed **zero** occurrences of: delve, leverage, seamless/seamlessly, robust (as filler), cutting-edge, paradigm shift, groundbreaking, revolutionize, testament to, realm, underscores, paves the way, plays a crucial role, it is important to note, in today's world, rapidly evolving, ever-growing, unlocks, harness, holistic, synergy, navigate the complexities, at the forefront, game-changer, tapestry, moreover/furthermore chains. There were **no em-dashes (`---`)** in prose at all.

So the pass targeted the lower-frequency tells that were actually present, and the clearer win — sentence-level flow and a handful of colon-and-comma chains that read as machine-assembled.

### Patterns removed (with counts)

| Pattern | Count removed | Notes |
|---|---|---|
| "landscape" used as a metaphor | **2** | §2.5 ("telecom landscape"); §3 ("the corpus landscape"). One further instance (figure 1 caption title "Corpus landscape") was **kept deliberately** — see §4. |
| "not just X, but Y" / negative-parallelism construction | **1** | §2.5: "a training recipe, not just an architecture, drives results" → "the training recipe, not the architecture alone, drives results". |
| "the real X" / "a real X" emphasis-and-filler adjective | **2** | §2.3: "the real obstacle" → "the main obstacle"; §2.4: "a real platform layer or a real cost" → "a specific platform layer or cost". |
| Informal register: "pitch" | **1** | §2.3: "The paper's pitch is…" → "The paper's central claim is…". |
| Overlong sentences split into single-idea sentences | **5** | §2.3 (KATN audit link); §2.4 (forecasting-model clause); §2.5 (telecom "catalogues…reports" chain); §2.5 (ten-phase pipeline, split into three sentences); §2.5 (agentic "sorts…argues" chain). |
| Comma splices (independent clauses joined by "and" + comma) | **3** | Same five sentences above; three were fixed as comma splices specifically. |
| Redundant construction ("cross-cutting patterns cut across") | **1** | §2.6 topic sentence. |
| Vague rhetorical aside ("which is itself telling") | **1** | §2.6. |
| Redundant relative clause ("which is the premise behind…") | **1** | §2.6. |
| Awkward nominal/prepositional phrase ("at the crossing of") | **1** | §1 Introduction. |

**Total: 15 line-level edits** across 13 paragraphs.

---

## 2. Before / after — representative edits (13 shown)

1. **§2.5 — metaphor + comma splice**
   - Before: `Its framing is blunt: rule-based detection is no longer effective in a fast-evolving telecom landscape. It catalogues classical methods, deep methods, and emerging techniques, and it reports that deep models reach roughly 85 to 97\%…`
   - After: `Its framing is blunt: rule-based detection is no longer effective on fast-moving telecom networks. It catalogues classical methods, deep methods, and emerging techniques. It reports that deep models reach roughly 85 to 97\%…`
   - Why: removes the "landscape" metaphor; splits the two-verb chain into short, single-idea sentences. Meaning unchanged.

2. **§3 — metaphor**
   - Before: `Fig.~\ref{fig1} plots the corpus landscape.`
   - After: `Fig.~\ref{fig1} plots the corpus.`
   - Why: "landscape" as a metaphor removed; "plots the corpus" loses nothing (the axes are described in the next sentence).

3. **§2.5 — negative parallelism**
   - Before: `…which is the corpus's clearest evidence that a training recipe, not just an architecture, drives results.`
   - After: `…which is the corpus's clearest evidence that the training recipe, not the architecture alone, drives results.`
   - Why: the "not just X" construction is a listed AI tell; the rewrite keeps the same contrast (recipe matters, architecture is not sufficient on its own).

4. **§2.3 — "the real" trope + informal "pitch"**
   - Before: `The paper's pitch is that computational inefficiency is the real obstacle to explaining large models…`
   - After: `The paper's central claim is that computational inefficiency is the main obstacle to explaining large models…`
   - Why: "pitch" is marketing register; "the real obstacle" is an emphasis trope. "main obstacle" preserves the paper's own framing (from C-03/TBD-1: computational inefficiency is the bottleneck).

5. **§2.4 — "a real X" filler**
   - Before: `Each names a real platform layer or a real cost, and together they outline an infrastructure stack.`
   - After: `Each names a specific platform layer or cost, and together they outline an infrastructure stack.`
   - Why: "real" is filler; "specific" is concrete and keeps the point (each paper names something actual).

6. **§2.3 — long sentence split**
   - Before: `That reporting style is exactly what the corpus's reproducibility audit later finds under-specified, and it links this paper to the evaluation thread in Section~2.6.`
   - After: `That reporting style is exactly what the corpus's reproducibility audit later finds under-specified. It links this paper to the evaluation thread in Section~2.6.`
   - Why: comma splice; two ideas separated. The KATN→§2.6 cross-reference is preserved verbatim.

7. **§2.5 — long sentence split (three sentences)**
   - Before: `It fuses text, audio, video, and motion through a ten-phase pipeline that uses a Mistral-7B text encoder, HuBERT for audio, a LLaVA and TimeSformer pair for video, and a pose model for motion, then combines them through adaptive graph networks, a cross-modality transformer, and prototypical contrastive learning.`
   - After: `It fuses text, audio, video, and motion through a ten-phase pipeline. The pipeline uses a Mistral-7B text encoder, HuBERT for audio, a LLaVA and TimeSformer pair for video, and a pose model for motion. It combines them through adaptive graph networks, a cross-modality transformer, and prototypical contrastive learning.`
   - Why: one 62-word sentence with two stacked participial clauses broken into three short ones. Every model name and every component is retained.

8. **§2.5 — long sentence split**
   - Before: `It sorts the field into symbolic architectures, which rely on planners and persistent state, and neural architectures, which rely on stochastic generation and prompt-driven orchestration, and it argues that conflating the two obscures how modern agents work.`
   - After: `It sorts the field into symbolic architectures, which rely on planners and persistent state, and neural architectures, which rely on stochastic generation and prompt-driven orchestration. It argues that conflating the two obscures how modern agents work.`
   - Why: the "and it argues" chain is a comma splice; split. The dual-paradigm description (AIR-1) is preserved word-for-word.

9. **§2.6 — redundancy + comma splice**
   - Before: `Three cross-cutting patterns cut across the branches, and they carry the review's analytical weight.`
   - After: `Three patterns cross the branches, and they carry the review's analytical weight.`
   - Why: "cross-cutting…cut across" is redundant; the sentence no longer repeats "cross-cutting" (the subsection heading already says it).

10. **§2.6 — rhetorical aside**
    - Before: `The requirement appears in every branch, which is itself telling.`
    - After: `The requirement appears in every branch.`
    - Why: "which is itself telling" adds an evaluative nudge without content. The substantive claim (it appears in every branch) is untouched; the point is carried by the supporting citations in the next sentence.

11. **§2.6 — redundant relative clause**
    - Before: `One program of work assumes that capability comes from centralizing and pretraining on everything available, which is the premise behind the foundation-model items…`
    - After: `One program of work assumes that capability comes from centralizing and pretraining on everything available. That premise sits behind the foundation-model items…`
    - Why: comma splice + relative clause; split into two direct sentences. Both citations (`wang2026mllm,chai2025graphllm`, `muneer2026classical`) preserved.

12. **§2.4 — long sentence split**
    - Before: `The forecasting model is a temporal convolutional network, chosen over LSTM, GRU, and sequence-to-sequence alternatives, and the multi-task variant predicts both vital signs jointly.`
    - After: `The forecasting model is a temporal convolutional network, chosen over LSTM, GRU, and sequence-to-sequence alternatives. The multi-task variant predicts both vital signs jointly.`
    - Why: separates the model-choice fact from the multi-task fact; the baselines list is kept.

13. **§1 — awkward possessive/prepositional phrase**
    - Before: `Big-data machine learning sits at the crossing of two fast-moving fields.`
    - After: `Big-data machine learning sits at the intersection of two fast-moving fields.`
    - Why: "the crossing of" is a non-idiomatic nominal; "the intersection of" is the standard usage. Meaning identical.

---

## 3. Sentences deliberately NOT changed, and why

- **`\abstract{…}`** — verbatim `We synthesize them thematically rather than paper by paper.` and the surrounding abstract. The abstract is accurate and already written in short, plain sentences; per the task rules the abstract's factual content must stay fixed. Only clarity-improving changes were in scope, and none was needed without risking drift from the paper's actual findings. Abstract word count re-checked: **185 words** (≤ ~200). Kept unchanged.
- **§2.5 — `Its most transferable finding is that fidelity metrics do not track usefulness.`** — this is a precise, well-calibrated claim (from AIR-4 / C-19) and already short. No edit.
- **§2.6 — `The patterns… is not that explainability is ignored; it is that explainability is required everywhere and standardized nowhere.`** — this resembles a negative-parallelism construction, but here the contrast is the substantive finding itself (a genuine antithesis, not rhythmic padding). The `paper-polish` faithfulness rule says do not flatten a real argument for style, so it was **kept**. Flagging it here for the author to confirm.
- **§2.3 — `Where KATN assumes a static archive, the streaming approach assumes the opposite.`** — "assumes the opposite" is a mild ellipsis, but it is crisp and the antecedent is unambiguous; changing it would only lengthen the sentence. Kept.
- **§2.7 — `Reinforcement learning at scale is absent from the taxonomy, and that absence is a method cell waiting to be filled.`** — "a method cell waiting to be filled" is mildly figurative, but it is the section's own framing device (it maps to the taxonomy's empty cells — C-21) and is used consistently. Kept.
- **Figure 1 caption title: `Corpus landscape.`** — see §5.
- **All table cells in `Table~\ref{tab1}` and `Table~\ref{tab2}`** — not touched. Table contents are explicitly out of scope and carry the numeric evidence.

---

## 4. Tone calibration against evidence (paper-polish)

No claim was strengthened and none was weakened. Spot-checks against the R2 ledger (`trackers/paper-tracker.md`) confirmed that every claim kept still matches its evidence:

- **KATN rank protocol / no per-dataset accuracy** (§2.3) — matches TBD-4 / C-12; kept as "rank-based rather than accuracy-based".
- **Streaming thresholds** (§2.3) — matches TBD-5 / C-09 ("threshold statements taken from the indexed abstract, not precise measurements"); the qualifier was preserved, not removed.
- **PEXP unquantified claims** (§2.3) — matches TBD-1 / C-03 / C-13; the "no dataset, no platform, no metric, and no named baseline… unquantified here" sentence was left intact.
- **Federated cost (no figures)** (§2.3/§2.4) — matches BDR-2 / C-04 ("the claim stands as a direction rather than a quantified result"); retained.
- **Abstract-only / unavailable items (BDR-3, BDR-4, BDR-5; TBD-1..3, TBD-5)** — the manuscript's own hedges ("describable only at title level", "Not available; abstract not indexed", "the review can record the cluster setting… but cannot describe the algorithm") were **preserved exactly**; the polish pass added no new hedging and removed none.
- **JoBD-3 99.82%/99.81%** (§2.5) — still framed as "reporting-practice evidence", not capability; the anomalously-high flag was preserved.

The one meaning-adjacent edit is edit #3 (§2.5, "not just an architecture" → "not the architecture alone"). The underlying finding (JoBD-1 / C-20: the training recipe drives the 97.33% result, and the ViT baseline is weak) is unchanged: "not the architecture alone" carries the identical claim that recipe and architecture both matter. Noted for the author's confirmation, but no change to the scientific content.

---

## 5. What was preserved unchanged (explicit statement)

- **All citations:** every `\citep{…}`/`\cite{…}` key is byte-identical to the pre-pass file. No key added, removed, or reordered. The manuscript still renders **20 numbered references, [1]..[20]**.
- **All numbers:** every percentage, RMSE, MAE, F1, threshold, count, dataset size, and record total is unchanged. No value was added, guessed, or altered.
- **All cross-references:** every `\ref{}`/`\label{}` is unchanged; no new label introduced, none removed.
- **Section structure and names:** unchanged (Introduction, Literature Review with subsections 2.1–2.7, Tables and Figures, Conclusion, Declarations).
- **`\documentclass` line, declarations block, keywords, title/author block:** unchanged.
- **Figure includes and both tables:** unchanged (5 figures, 2 tables).
- **Figure 1 caption title "Corpus landscape":** kept. This is a figure *title* tied to the image filename `fig1_corpus_landscape.pdf`, and it is descriptive rather than metaphorical in that position; changing it would desynchronise the caption from the artefact and the `figures/fig-data-source.md` record. Flagged here as the single deliberate exception to the "remove 'landscape'" rule.
- **The abstract:** factual content unchanged (185 words).

---

## 6. Verification

Recompiled from `paper/` with the standard sequence (`pdflatex → bibtex → pdflatex → pdflatex`). See the task completion note for the compiled PDF status, the final citation/reference/figure/table counts, and the abstract word count.
