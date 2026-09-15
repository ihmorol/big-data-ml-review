# Team plan — 8 members, deadline Sep 27, 2026

Fill in names in the Owner column. Every member is in a **journal pod** (Phase A) and takes a **writing/production role** (Phase B). No idle hands in either phase.

## Phase A — Journal pods (Sep 15–20): find, screen, read, extract

Each pod owns 5 locked papers from its journal (shortlist 8–10, lock the best 5) and writes the extraction notes in `sources/`.

| Pod | Journal | Members |
|---|---|---|
| Pod 1 | IEEE Transactions on Big Data | Member 1 (lead), Member 2 |
| Pod 2 | Big Data Research | Member 3 (lead), Member 4 |
| Pod 3 | Journal of Big Data | Member 5 (lead), Member 6 |
| Pod 4 | Artificial Intelligence Review | Member 7 (lead), Member 8 |

Pod work: search → screen against criteria → lock 5 in `trackers/papers-pool.md` → one `sources/<ID>.md` extraction note per paper (2 papers per member minimum).

## Phase B — Writing & production roles (Sep 20–26)

| Role | Owner | Deliverable |
|---|---|---|
| Integration editor | Member 1 | Owns the master document; resolves conflicts; final assembly; consistency of voice |
| Theme lead: scalable ML methods (§3.3) | Member 2 | LR subsection draft from pod 1 + 2 notes |
| Theme lead: platforms & pipelines (§3.4) | Member 3 | LR subsection draft from pod 2 + 3 notes |
| Theme lead: applications & domains (§3.5) | Member 5 | LR subsection draft from pod 3 + 4 notes |
| Tables & Figures lead | Member 6 | Table 1, Table 2, Figs 1–3 (data in `results/`, finals in `figures/`) |
| Cross-cutting analysis lead (§3.6–3.7) | Member 4 | Gaps + future directions subsection |
| Introduction & Conclusion lead | Member 7 | §1 Introduction, §5 Conclusion, taxonomy §3.2 text |
| Formatting & references lead | Member 8 | AIR/Springer Basic style pass, reference list, submission checklist, abstract |

Everyone drafts in Markdown under `paper/sections/`; the integration editor merges into `paper/manuscript.md`.

## Timeline (Sep 15 → Sep 27)

| Dates | Milestone | Owner check |
|---|---|---|
| Sep 15–16 | Pods shortlist candidates; **20 papers locked**; Table 1 skeleton started | pods |
| Sep 17–20 | All 20 extraction notes done; themes assigned; Table 1 data complete | pods + T&F lead |
| Sep 20–23 | Theme subsections drafted (§3.3–3.5, §3.6–3.7); Figs 1–3 built | theme leads + T&F |
| Sep 24 | Intro, Conclusion, §3.1–3.2 drafted; full assembly v1 | intro lead + editor |
| Sep 25 | Abstract written; references formatted; internal review pass | all |
| Sep 26 | Formatting pass vs AIR; submission checklist in `notes/requirements.md` ticked; freeze | formatting lead + editor |
| Sep 27 | **Submit** (aim to have it done on the 26th — the 27th is buffer) | — |

## Working agreements

- One drive/repo, one source of truth per artifact (this workspace's structure); no side copies.
- Deadline on the 26th, not the 27th — last-minute formatting fixes always take longer than expected.
- If a pod can't find 5 solid papers in its journal by Sep 16, escalate to the integration editor immediately — do not silently substitute papers from other journals.
