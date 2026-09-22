# notion-import/ — optional: the same tables as Notion databases

The team's tracker is the single file `../paper-tracker.md`. These CSVs are only for anyone who wants the same data as a Notion **database** (filterable, sortable, rollups) instead of a plain table — Notion imports markdown tables as static tables, and CSVs as databases.

| CSV | Rows | Notes |
|---|---|---|
| `master.csv` | 20 | Same columns as the master table in the tracker (metadata filled, working columns empty) |
| `alternates.csv` | 29 | The swap bench |
| `references.csv` | 20 | Springer Basic reference strings, flags, BibTeX keys |

Import: Notion → **Import → CSV**, one file at a time, then set the property types (`Year` → Number; `Access`, `Read status`, `Draft section` → Select; `DOI`, `PDF` → URL). Add a Relation on `ID` if you want the three databases linked.

Regenerate all three with `python code/build_tracker.py` after a paper swap or after new PDFs land in `papers/`.
