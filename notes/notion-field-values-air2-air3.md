# Notion field values — AIR-2 and AIR-3 (simple wording)

Ready-to-paste values for the team tracker, in the tracker's own field names. One line per cell (the Notion import rule). Written in plain words so everyone on the team can follow it. All of it comes from our reading notes, so it can be defended if asked.

Source of detail: [`../sources/AIR-2_artificial-intelligence-advances-in.md`](../sources/AIR-2_artificial-intelligence-advances-in.md), [`../sources/AIR-3_from-classical-machine-learning.md`](../sources/AIR-3_from-classical-machine-learning.md).

---

## AIR-2 — AI advances in anomaly detection for telecom networks

Most fields in this row are already filled in Notion. Only `Agrees with` and `Disagrees with` are empty. Paste these two.

| Field | Value |
|---|---|
| **Agrees with** | TBD-5: when correct labels are rare, it is better to learn what normal looks like and flag anything different. JoBD-5: knowing how points connect helps spot network problems. BDR-2 and JoBD-2: training across many devices without moving the data is the private way to learn. BDR-1: giving reasons for a decision matters. AIR-5: deep learning models are now the main tools for finding odd patterns in time-series data. TBD-1: tree-based models are both accurate and fast. |
| **Disagrees with** | No paper here argues against its main story. But it is weaker on proof than the others. AIR-5 actually tests its results, and TBD-5, JoBD-5, BDR-3 and BDR-5 all give real numbers on named data. AIR-2 says it ran no data of its own (p. 33) and gives no sizes. It also claims tree models work well on huge live data (p. 14) but shows no proof, which is exactly what TBD-1 and BDR-5 test. |

---

## AIR-3 — From old machine learning to foundation models: mixing cancer data

| Field | Value |
|---|---|
| Access | Open |
| Agrees with | AIR-1: big foundation models cost a lot to run, and numbers alone are not enough (pp. 31, 50). AIR-2: the real problem is putting models to use, not their accuracy (pp. 30, 57). AIR-4: healthcare data is scarce and private, so fake data or shared training helps (pp. 48, 51). JoBD-2: sharing training across hospitals without moving the data keeps it private. TBD-4: attention helps models catch patterns that are far apart. |
| Data used | No data of its own, it is a review. It looked at 54 main studies (started with 3,280, ended with 54) and listed cancer foundation models with their sizes (scGPT over 33M cells, Nicheformer 110M cells, OmniCLIP 2.2M tissue image pairs). Data sets named: TCGA, GEO, METABRIC, CPTAC, ICGC, SEER, MIMIC. |
| Disagrees with | Goes against the idea in JoBD-3 that piling up more models means better real-world results. AIR-3 shows that adding many models often makes results harder to repeat and fails forward testing (pp. 29-31). |
| Future work | Test models in real forward-looking hospital trials and use them in decision-support tools. Standard ways to prepare data and measure results. Lower the GPU cost so hospitals can run them. Make models explain the biology behind their answers. Study the cost and benefit. Use few-shot learning for rare cancers. |
| ID | AIR-3 |
| Journal | Artificial Intelligence Review |
| Link | doi.org/10.1007/s10462-026-11522-9 |
| Main result | Mixing the data in the middle, not at the start or the end, with attention works best for predicting survival and how far cancer spreads. Foundation models need only a few examples for rare cancers. Big gap to real use: over 90% of studies look back at old records from one hospital, and almost none do forward trials or get approved. |
| Method | Shows the move from old ML (SVM, Random Forest, XGBoost) to deep learning (CNN, VAE, GNN, attention) to foundation models (scGPT, Nicheformer, OmniCLIP). Gives a two-part way to group fusion: when the data is combined (early, middle, late) and how it is combined (step-by-step, graph, attention, contrastive, correlation). |
| Reader | Ikramul Hasan |
| Status | Read |
| Tools | PRISMA 2020 plus a simpler extra search for preprints. Databases: PubMed, Google Scholar, arXiv, bioRxiv. Models named: SVM, Random Forest, XGBoost, CCA, CNN (ResNet/DenseNet), VAE, GNN, attention; scGPT, Nicheformer, OmniCLIP, GET, MolFM. No platform used; talks about GPU clusters and privacy. |
| Topic | B4 Foundation models and LLMs (also B3 Applications and domains) |
| Weak points | A long 69-page summary, not a test of its own. It reports other papers' numbers without checking they were measured the same way. Hard to apply outside cancer. No data or experiments of its own. |
| What is new | The only paper here that gives a clear two-part way to group fusion methods, plus a full list of cancer foundation models and their sizes. The only one that shows how far the field is from real hospital use (over 90% look back at old records). |
| Year | 2026 |

---

## Notes

- **AIR-2** only needs the two values above. The rest of that row is already written.
- **AIR-3** above is the full row, ready to paste if it is still empty.
- `Agrees with` and `Disagrees with` name other papers by their IDs (TBD-1, JoBD-5, and so on). If those are linked fields in Notion, keep the IDs as written so the links work.
- AIR-2's `Disagrees with` says plainly that no paper argues against it. That is the honest answer, not a made-up one.
