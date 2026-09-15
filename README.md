# Workspace — Big Data with Machine Learning: A Review

**The single source of truth for this workspace is [`notes/Big Data Assignment.pdf`](notes/Big%20Data%20Assignment.pdf).** Everything here exists to produce that assignment. A distilled copy of its requirements lives in [`notes/requirements.md`](notes/requirements.md) — read that first.

## Getting started (team members)

```bash
git clone https://github.com/ihmorol/big-data-ml-review.git
cd big-data-ml-review
```

Repo: **https://github.com/ihmorol/big-data-ml-review**

- Pull before you start editing; push when you finish a work session.
- Keep the trackers updated — they are the coordination point (`trackers/papers-pool.md`, `trackers/team-tasks.md`, `trackers/writing-progress.md`).
- Reading a paper? Open its note in `sources/` and complete the "Synthesis hooks" section.
- The local `archive/` folder (an unrelated old project) is intentionally not published to this repo.

## Assignment at a glance

| Item | Value |
|---|---|
| Deliverable | Literature review paper: **"Big Data with Machine Learning: A Review"** |
| Format | Publication style of *Artificial Intelligence Review* (Springer) |
| Sources | ≥ 20 papers, 2025–2027, from 4 journals (≈3–5 each → **exactly 5 per journal**) |
| Components | Abstract · Introduction · Literature Review · Tables & Figures · Conclusion · References |
| Deadline | **September 27, 2026** |
| Team | 8 members (assignment allows max 10) |
| Weight | 25% of course grade |

Marks: Abstract 2 · Introduction 3 · **Literature Review 10** · Tables & Figures 3 · Conclusion 2 · Formatting 2 · References 3.

## Workspace layout

```
notes/            requirements.md (distilled brief) + the assignment PDF itself
paper/            outline.md, then the actual sections as they are drafted
sources/          per-paper extraction notes (one file per selected paper)
trackers/         papers-pool.md · team-tasks.md · writing-progress.md
figures/          final figures (PNG/PDF, 300 dpi)
code/             optional scripts used to generate tables/figures from extracted data
results/          intermediate data behind tables/figures (counts, matrices)
archive/          previous project that used this workspace (DT–NB hybrid) — kept, not active
```

## How this runs (see trackers/ for detail)

1. **Paper pool (Sep 15–16):** 4 journal pods (2 members each) fill `trackers/papers-pool.md` → 20 papers locked.
2. **Read & extract (Sep 17–20):** every paper gets an extraction note in `sources/` using the shared template.
3. **Synthesize & write (Sep 20–24):** thematic Literature Review sections + tables/figures.
4. **Assemble & format (Sep 25–26):** intro, conclusion, abstract, references in Springer Basic (numeric, brackets) style, AIR formatting pass.
5. **Submit Sep 27.**

The one rule that matters: the Literature Review (10%) must **synthesize, compare, and critically analyze** the 20 papers — themes, contrasts, gaps — not 20 mini-summaries.
