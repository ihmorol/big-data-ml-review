"""Build the team paper tracker (one Notion-ready markdown file), references.bib, and a small CSV set.

Sources: results/pool_selected.json (pool rev 3: 20 selected + 29 alternates),
results/screen/*.csv and results/openalex_raw/ (counts for the Fig. 1 funnel),
sources/*.md (per-paper extraction notes), papers/**/*.pdf (downloaded full texts),
notes/landscape-report.md (branch taxonomy).

Outputs:
  trackers/paper-tracker.md        the tracker - one file, import it into Notion
  paper/references.bib             BibTeX for the 20 selected papers
  trackers/notion-import/*.csv     the same tables as CSVs, for anyone who wants Notion databases

Design rules:
  - one master table: one row per paper, every working column on that row;
  - the tracker carries the 20 papers' verified information and leaves the status and
    analysis columns empty for the team to fill;
  - no speculative values.

Re-running overwrites the markdown, the BibTeX and the CSVs, but the ten working columns the team
has filled in are carried over from the existing tracker/CSV; everything else is regenerated.
"""
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POOL = ROOT / "results" / "pool_selected.json"
SCREEN = ROOT / "results" / "screen"
RAW = ROOT / "results" / "openalex_raw"
SOURCES = ROOT / "sources"
PAPERS = ROOT / "papers"
TRACKER_OUT = ROOT / "trackers" / "paper-tracker.md"
BIB_OUT = ROOT / "paper" / "references.bib"
CSV_OUT = ROOT / "trackers" / "notion-import"

REPO = "https://github.com/ihmorol/big-data-ml-review"
GENERATED = "2026-09-15"

JOURNAL_SHORT = {
    "IEEE_TBD": "IEEE TBD",
    "BDR": "Big Data Research",
    "JoBD": "Journal of Big Data",
    "AIR": "AI Review",
}
# Publisher-form names (OpenAlex spells one of them "Journal Of Big Data").
JOURNAL_FULL = {
    "IEEE_TBD": "IEEE Transactions on Big Data",
    "BDR": "Big Data Research",
    "JoBD": "Journal of Big Data",
    "AIR": "Artificial Intelligence Review",
}
JOURNAL_ORDER = ["IEEE_TBD", "BDR", "JoBD", "AIR"]

# Branch taxonomy: notes/landscape-report.md Sect. 3. Papers are branch members there.
BRANCH = {
    "B1": "Scalable and interpretable learning methods",
    "B2": "Platforms, pipelines, and infrastructure",
    "B3": "Applications and domains",
    "B4": "Foundation models and LLMs",
    "B5": "Privacy, governance, and evaluation",
}
PAPER_BRANCH = {
    "TBD-1": "B1", "TBD-4": "B1", "TBD-5": "B1", "BDR-5": "B1", "JoBD-5": "B1",
    "BDR-3": "B2", "JoBD-4": "B2", "BDR-2": "B2",
    "BDR-1": "B3", "AIR-2": "B3", "BDR-4": "B3", "JoBD-3": "B3", "JoBD-1": "B3",
    "TBD-3": "B4", "AIR-1": "B4", "AIR-3": "B4", "TBD-2": "B4",
    "JoBD-2": "B5", "AIR-4": "B5", "AIR-5": "B5",
}

PODS = {
    "IEEE_TBD": "Pod 1 (Members 1-2)",
    "BDR": "Pod 2 (Members 3-4)",
    "JoBD": "Pod 3 (Members 5-6)",
    "AIR": "Pod 4 (Members 7-8)",
}

# Alternates: why each is held (trackers/papers-pool.md swap rules).
HELD_FOR = {
    "TBD-A5": "Designated swap for any TBD paywalled item (OA)",
    "TBD-A6": "Research-only backup for TBD",
    "BDR-A1": "Swap if BDR-3/BDR-5 access fails (OA)",
    "BDR-A2": "Swap if BDR-3/BDR-5 access fails (OA)",
    "AIR-A6": "Research-only insurance if the AIR review exception is rejected",
    "AIR-A7": "Research-only insurance if the AIR review exception is rejected",
    "AIR-A8": "Research-only insurance if the AIR review exception is rejected",
    "AIR-A9": "Research-only insurance if the AIR review exception is rejected",
    "AIR-A10": "Research-only insurance if the AIR review exception is rejected",
}
DEFAULT_HELD = "General hold (vetted alternate)"

# BibTeX keys: lastname + year + keyword. Hand-picked where the first title word is generic.
KEY_OVERRIDES = {
    "TBD-4": "xiao2025katn",
    "AIR-2": "edozie2025telecom",
    "AIR-4": "waseem2025synthetic",
    "AIR-5": "vats2026survey",
    "AIR-3": "muneer2026classical",
}

# Compound surnames: "Full Name" -> (bibtex "Last, First", last name for reference strings).
# Anything listed here is flagged in Appendix B for a spot-check against the publisher page.
SURNAME_OVERRIDES = {
    "Mohamad Abou Ali": ("Abou Ali, Mohamad", "Abou Ali"),
    "Diptendu Sinha Roy": ("Sinha Roy, Diptendu", "Sinha Roy"),
    "Züleyha Akusta Dağdevıren": ("Akusta Dağdevıren, Züleyha", "Akusta Dağdevıren"),
    "Saif ul Islam": ("ul Islam, Saif", "ul Islam"),
    "Marwa Salah Farhan": ("Salah Farhan, Marwa", "Salah Farhan"),
}
FLAGGED_SURNAMES = set(SURNAME_OVERRIDES)

MISSING_FIELD_NOTE = {
    "TBD-2": "volume/issue not indexed yet (early access) - verify at IEEE Xplore",
    "AIR-5": "volume/issue not indexed yet (online first) - verify at SpringerLink",
}
ARTICLE_NUMBER_NOTE = "article number not indexed - verify at the publisher"


def load_pool():
    records = json.loads(POOL.read_text(encoding="utf-8"))
    selected = [r for r in records if r.get("role") == "selected"]
    alternates = [r for r in records if r.get("role") != "selected"]

    # stable order: journal order, then numeric suffix
    def sort_key(r):
        num = re.sub(r"\D", "", r["id"].split("-")[1])
        return (JOURNAL_ORDER.index(r["journal_file"]), int(num))

    return sorted(selected, key=sort_key), sorted(alternates, key=sort_key)


def note_path(pid: str):
    hits = sorted(SOURCES.glob(f"{pid}_*.md"))
    return hits[0] if hits else None


def pdf_path(pid: str):
    """Full text downloaded by a pod: papers/<journal>/<ID>_<Author>_<Year>_<Title>.pdf"""
    hits = sorted(PAPERS.glob(f"**/{pid}_*.pdf"))
    return hits[0] if hits else None


def repo_url(path: Path):
    return f"{REPO}/blob/main/{path.relative_to(ROOT).as_posix()}"


def split_name(full: str):
    """Return (bibtex_author, last_name, initials). Default: last token is the surname."""
    if full in SURNAME_OVERRIDES:
        bib, last = SURNAME_OVERRIDES[full]
    else:
        parts = full.split()
        last = parts[-1]
        bib = full
    given = full[: len(full) - len(last)].strip()
    initials = "".join(t[0].upper() for t in re.split(r"[\s\-]+", given) if t)
    return bib, last, initials


def bibtex_key(pid, rec):
    if pid in KEY_OVERRIDES:
        return KEY_OVERRIDES[pid]
    last = re.sub(r"[^A-Za-z]", "", split_name(rec["authors"][0])[1]).lower()
    words = re.findall(r"[A-Za-z]{4,}", rec["title"])
    skip = {"with", "from", "using", "based", "toward", "towards", "through", "into"}
    word = next((w.lower() for w in words if w.lower() not in skip), "paper")
    return f"{last}{rec['year']}{word}"


def bibtex_entry(pid, rec):
    biblio = rec.get("biblio") or {}
    authors = [split_name(a)[0] for a in rec["authors"]]
    lines = [f"@article{{{bibtex_key(pid, rec)},"]
    lines.append("  author   = {" + " and ".join(authors) + "},")
    lines.append("  title    = {" + rec["title"] + "},")
    lines.append("  journal  = {" + JOURNAL_FULL[rec["journal_file"]] + "},")
    lines.append("  year     = {" + str(rec["year"]) + "},")
    if biblio.get("volume"):
        lines.append("  volume   = {" + biblio["volume"] + "},")
    if biblio.get("issue"):
        lines.append("  number   = {" + biblio["issue"] + "},")
    first, last = biblio.get("first_page"), biblio.get("last_page")
    # Pages without a volume are early-access placeholders (e.g. "1--14") - leave them out.
    if biblio.get("volume") and first and last and first != last:
        lines.append(f"  pages    = {{{first}--{last}}},")
    elif biblio.get("volume") and first:
        lines.append("  pages    = {" + first + "},")
    lines.append("  doi      = {" + rec["doi"] + "},")
    lines.append("  url      = {https://doi.org/" + rec["doi"] + "},")
    note = ("Review article" if is_review(rec) else "Research article") + f"; pool ID {pid}"
    lines.append("  note     = {" + note + "}")
    entry = "\n".join(lines) + "\n}"
    todo = []
    if pid in MISSING_FIELD_NOTE:
        todo.append(MISSING_FIELD_NOTE[pid])
    if rec["journal_file"] in ("JoBD", "AIR") and not (first or last):
        todo.append(ARTICLE_NUMBER_NOTE)
    if any(a in FLAGGED_SURNAMES for a in rec["authors"]):
        todo.append("compound surname(s) parsed mechanically - verify against the publisher page")
    if todo:
        entry = "\n".join("% TODO: " + t for t in todo) + "\n" + entry
    return entry


def is_review(rec):
    return rec["journal_file"] == "AIR"


def reference_string(pid, rec):
    """Springer Basic: Lastname FN (Year) Title. Journal Vol(Issue):pages. https://doi.org/..."""
    biblio = rec.get("biblio") or {}
    names = []
    for a in rec["authors"]:
        _, last, initials = split_name(a)
        names.append(f"{last} {initials}")
    authors = ", ".join(names)
    loc = ""
    if biblio.get("volume"):
        loc = biblio["volume"]
        if biblio.get("issue"):
            loc += f"({biblio['issue']})"
    first, last = biblio.get("first_page"), biblio.get("last_page")
    if biblio.get("volume") and first and last and first != last:
        loc += f":{first}\u2013{last}"
    elif biblio.get("volume") and first:
        loc += f":{first}"
    if not loc:
        loc = "[volume/pages to verify]"
    elif not (first or last):
        loc += " [article no. to verify]"
    return f"{authors} ({rec['year']}) {rec['title']}. {JOURNAL_FULL[rec['journal_file']]} {loc}. https://doi.org/{rec['doi']}"


def reference_flags(pid, rec):
    flags = []
    if pid in MISSING_FIELD_NOTE:
        flags.append("verify volume/pages (online first)")
    if rec["journal_file"] in ("JoBD", "AIR") and not (rec.get("biblio") or {}).get("first_page"):
        flags.append("verify article number")
    if any(a in FLAGGED_SURNAMES for a in rec["authors"]):
        flags.append("compound surname parsed mechanically - verify")
    if is_review(rec):
        flags.append("review article (AIR exception)")
    return "; ".join(flags) if flags else "\u2014"


def access_long(rec):
    return f"OA ({rec.get('oa_status','open')})" if rec.get("is_oa") else "PAID \u2014 institutional access"


def md_table(headers, rows):
    def cell(v):
        return " ".join(str(v).replace("|", "\\|").split())

    out = ["| " + " | ".join(cell(h) for h in headers) + " |",
           "|" + "|".join(["---"] * len(headers)) + "|"]
    for r in rows:
        out.append("| " + " | ".join(cell(c) for c in r) + " |")
    return out


def check_tables(lines):
    """Every markdown table must have a constant pipe count inside its block."""
    bad, i = [], 0
    while i < len(lines):
        if lines[i].startswith("|"):
            block = []
            while i < len(lines) and lines[i].startswith("|"):
                block.append(lines[i])
                i += 1
            if len({ln.count("|") for ln in block}) != 1:
                bad.append(block[0][:90])
        else:
            i += 1
    return bad


def check_blank_lines(lines):
    """A table must be followed by a blank line, or Notion folds the next paragraph into it."""
    return [f"{i + 1}: {ln[:70]}" for i, ln in enumerate(lines[:-1])
            if ln.startswith("|") and lines[i + 1].strip() and not lines[i + 1].startswith("|")]


def funnel_counts():
    rows = {}
    for jf in JOURNAL_ORDER:
        rows[jf] = {
            "retrieved": len(json.loads((RAW / f"{jf}.json").read_text(encoding="utf-8"))),
            "screened": len(list(csv.DictReader((SCREEN / f"{jf}.csv").open(encoding="utf-8-sig")))),
        }
    return rows


MASTER_HEADERS = ["ID", "Paper (DOI)", "Year", "Journal \u00b7 type", "Access", "PDF", "Reader",
                  "Read status", "Method / platform \u2020", "Dataset & scale", "Headline result",
                  "Limitations (theirs / ours)", "Draft \u00a7", "S2 \u00b7 S5", "Notes"]

# Columns after PDF are the team's to fill; a regeneration keeps what they wrote.
MD_WORKING = MASTER_HEADERS[6:]
CSV_WORKING = ["Reader", "Read status", "Method / platform (abstract)", "Dataset and scale",
               "Headline result", "Limitations (theirs / ours)", "Draft section", "S2", "S5", "Notes"]
EMPTY = "\u2014"


def load_prev_md():
    """ID -> filled working cells already in the tracker (the '—' placeholders are ignored)."""
    prev = {}
    if not TRACKER_OUT.exists():
        return prev
    for line in TRACKER_OUT.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| "):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != len(MASTER_HEADERS) or not re.match(r"^[A-Za-z]+-\d+$", cells[0]):
            continue
        filled = {MASTER_HEADERS[i]: cells[i] for i in range(6, len(MASTER_HEADERS))
                  if cells[i] and cells[i] != EMPTY}
        if filled:
            prev[cells[0]] = filled
    return prev


def load_prev_csv():
    """Same, for master.csv (its column names differ slightly from the markdown table)."""
    prev = {}
    path = CSV_OUT / "master.csv"
    if not path.exists():
        return prev
    with path.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            filled = {k: (row.get(k) or "").strip() for k in CSV_WORKING}
            filled = {k: v for k, v in filled.items() if v and v != EMPTY}
            if filled:
                prev[row.get("ID", "")] = filled
    return prev


def master_row(rec, pdf, note, prev=None):
    """One row per paper: metadata regenerated, working columns kept where the team filled them."""
    prev = prev or {}
    pid = rec["id"]
    journal = f"{JOURNAL_SHORT[rec['journal_file']]} \u00b7 {'review' if is_review(rec) else 'research'}"

    def keep(name, generated=EMPTY):
        return prev.get(name, generated)

    return [
        pid,
        f"[{rec['title']}](https://doi.org/{rec['doi']})",
        rec["year"],
        journal,
        access_long(rec),
        f"[PDF]({repo_url(pdf)})" if pdf else EMPTY,
        keep("Reader"),
        keep("Read status"),
        keep(MASTER_HEADERS[8], f"{rec.get('ml_methods','')} \u00b7 {rec.get('bd_context','')} \u2020"),
        keep("Dataset & scale"),
        keep("Headline result"),
        keep("Limitations (theirs / ours)"),
        keep("Draft \u00a7"),
        keep("S2 \u00b7 S5"),
        keep("Notes"),
    ]


def build():
    selected, alternates = load_pool()
    funnel = funnel_counts()
    oa = sum(1 for r in selected if r.get("is_oa"))
    paid = [r["id"] for r in selected if not r.get("is_oa")]
    years = {y: sum(1 for r in selected if r["year"] == y) for y in ("2025", "2026", "2027")}
    cites = sum(r.get("cited_by", 0) for r in selected)
    top = max(selected, key=lambda r: r.get("cited_by", 0))
    by_id = {r["id"]: r for r in selected}
    note = {r["id"]: note_path(r["id"]) for r in selected}
    pdf = {r["id"]: pdf_path(r["id"]) for r in selected}
    pdf_count = sum(1 for p in pdf.values() if p)
    prev_md = load_prev_md()
    prev_csv = load_prev_csv()

    L = []
    A = L.append

    # ---------- header ----------
    A("# Paper Tracker \u2014 Big Data with Machine Learning: A Review")
    A("")
    A("One table, 20 rows \u2014 one row per selected paper, everything the team needs on that row. "
      "Metadata (title, link, year, journal, access, PDF) is filled in; the working columns are empty for us to fill as we read "
      "and write. Same 20 IDs everywhere in the project: TBD-1 \u2026 TBD-5, BDR-1 \u2026 BDR-5, JoBD-1 \u2026 JoBD-5, AIR-1 \u2026 AIR-5.")
    A("")
    A(f"**Pool:** rev 3, locked {GENERATED} \u00b7 20 papers (5 per journal) + 29 vetted alternates \u00b7 review period 2025\u20132027 "
      f"(all items are 2025\u20132026; no 2027-dated item exists yet). {pdf_count} of 20 full texts are already in `papers/`.")
    A(f"**Repo:** {REPO} \u2014 the tracker is regenerated from it by `code/build_tracker.py`; re-run that script after a paper swap. "
      "Cells the team has already filled are carried over, so a regeneration only refreshes metadata.")
    A("")
    A("## How to use it")
    A("")
    A("- **Work in the master table.** Find your paper by ID, fill the empty cells in that row. Never delete a row; never guess a number.")
    A("- **Who fills what:** the reader fills `Reader`, `Read status`, `Dataset & scale`, `Headline result`, `Limitations` \u00b7 "
      "the theme leads fill `Draft \u00a7` and `Notes` (quotable line + page) \u00b7 `S2 \u00b7 S5` is the quick quality score (0\u20132 each) "
      "from the reader \u00b7 the integration editor keeps the board current.")
    A("- **Status vocabulary, exactly these words:** `Not started` \u00b7 `Skimmed` \u00b7 `Read` \u00b7 `Deep-read`. "
      "Draft \u00a7 uses the outline's codes: \u00a73.3 methods \u00b7 \u00a73.4 platforms \u00b7 \u00a73.5 applications \u00b7 \u00a73.6 cross-cutting \u00b7 \u00a73.7 future.")
    A("- **`\u2020`** marks values taken from the indexed abstract \u2014 verify them against the full text, then drop the marker.")
    A("- **Keep each cell on one line** (a line break inside a cell breaks the Notion import), and keep the `ID` values unchanged \u2014 "
      "they are the keys that tie this page to `sources/`, `papers/` and the rest of the repo.")
    A("")
    A("Supporting documents, all in the repo: "
      f"[papers-pool.md]({REPO}/blob/main/trackers/papers-pool.md) (selection record + swap rules) \u00b7 "
      f"[team-tasks.md]({REPO}/blob/main/trackers/team-tasks.md) (roles + timeline) \u00b7 "
      f"[writing-progress.md]({REPO}/blob/main/trackers/writing-progress.md) (marks + session log) \u00b7 "
      f"[sources/]({REPO}/tree/main/sources) (one extraction note per paper) \u00b7 "
      f"[paper/references.bib]({REPO}/blob/main/paper/references.bib) (the BibTeX below, as a file).")
    A("")

    # ---------- summary ----------
    A("## Summary")
    A("")
    A("### The corpus")
    A("")
    L.extend(md_table(["Metric", "Value"], [
        ["Papers", "20 \u2014 exactly 5 per journal (the assignment forces 5 \u00d7 4)"],
        ["Journals", "IEEE Transactions on Big Data \u00b7 Big Data Research \u00b7 Journal of Big Data \u00b7 Artificial Intelligence Review"],
        ["Years", f"2025: {years['2025']} \u00b7 2026: {years['2026']} \u00b7 2027: {years['2027']}"],
        ["Article type", "15 original research \u00b7 5 review articles (all AIR, kept as a documented exception per the supervisor clarification of 2026-09-15)"],
        ["Access", f"{oa} open access \u00b7 {len(paid)} paywalled ({', '.join(paid)} \u2014 institutional access needed)"],
        ["Citations (OpenAlex 2026-09-15)", f"{cites} across the pool \u00b7 most-cited {top['id']} ({top.get('cited_by')}) \u00b7 six papers at 0"],
        ["Verification", "20/20 selected papers verified against Crossref on 2026-09-15"],
        ["Deadline", "2026-09-27 \u2014 plan to have the paper done on the 26th"],
    ]))
    A("")
    A("### How the 20 papers were chosen (the numbers behind Fig. 1)")
    A("")
    L.extend(md_table(["Stage", "All four journals", "IEEE TBD", "BDR", "JoBD", "AIR", "Source file"],
                      [["Retrieved from OpenAlex (2025+)",
                        sum(funnel[j]["retrieved"] for j in JOURNAL_ORDER),
                        funnel["IEEE_TBD"]["retrieved"], funnel["BDR"]["retrieved"],
                        funnel["JoBD"]["retrieved"], funnel["AIR"]["retrieved"], "results/openalex_raw/*.json"],
                       ["Passed the keyword screen (ML + big-data hit)",
                        sum(funnel[j]["screened"] for j in JOURNAL_ORDER),
                        funnel["IEEE_TBD"]["screened"], funnel["BDR"]["screened"],
                        funnel["JoBD"]["screened"], funnel["AIR"]["screened"], "results/screen/*.csv"],
                       ["Candidates verified against Crossref",
                        len(selected) + len(alternates),
                        sum(1 for r in selected + alternates if r["journal_file"] == "IEEE_TBD"),
                        sum(1 for r in selected + alternates if r["journal_file"] == "BDR"),
                        sum(1 for r in selected + alternates if r["journal_file"] == "JoBD"),
                        sum(1 for r in selected + alternates if r["journal_file"] == "AIR"),
                        "results/pool_selected.json"],
                       ["Included in the review", len(selected), 5, 5, 5, 5, "the master table below"]]))
    A("")
    A("Recount from those files before drawing Fig. 1 \u2014 the screen counts come from the keyword rules in `code/screen_pool.py`.")
    A("")
    A("### What the 20 papers cover (the \u00a73.2 branches)")
    A("")
    A("Five branches from `notes/landscape-report.md`, used for Fig. 2. Every paper sits in exactly one branch; R2's Branch cell "
      "in the master table repeats it.")
    A("")
    rows = []
    for code, name in BRANCH.items():
        members = [p for p in PAPER_BRANCH if PAPER_BRANCH[p] == code]
        members.sort(key=lambda p: list(by_id).index(p))
        rows.append([code, name, ", ".join(members), len(members)])
    L.extend(md_table(["Branch", "Theme", "Papers", "Count"], rows))
    A("")
    A("- **Straddlers (visible, not hidden):** BDR-2 is federated learning as a privacy mechanism *and* as 6G infrastructure \u00b7 "
      "JoBD-2 is privacy machinery on a healthcare application \u00b7 JoBD-3 is a prompt-engineering method tested on affective computing \u00b7 "
      "TBD-2 is an LLM method paper running on industrial production data \u00b7 AIR-4 couples generative models to a governance problem \u00b7 "
      "TBD-5 is a methods contribution evaluated only on security data.")
    A("- **Empty cells in the taxonomy** \u2014 no reinforcement-learning-at-scale paper, no purely theoretical contribution, "
      "no 2027-dated item. These are findings for the cross-cutting section, not gaps in our search.")
    A("- **Theme labels:** the per-paper \"theme\" values in `trackers/papers-pool.md` are pod-specific (ten labels for twenty papers, "
      "some overlapping). The Branch list above is the authoritative grouping for Fig. 2.")
    A("")
    A("### Access, swaps and thin spots")
    A("")
    A(f"- **Paywalled ({len(paid)}):** {', '.join(paid)}. Try institutional access first; if a paper stays unobtainable, swap it rather "
      "than writing from the abstract: TBD-A5 (OA) for any TBD item \u00b7 BDR-A1 or BDR-A2 (both OA) for BDR-3/BDR-5 \u2014 see Appendix C.")
    A("- **Thin metadata:** BDR-3, BDR-4 and BDR-5 have no indexed abstracts, and evaluation specifics are missing from most abstracts "
      "across the pool \u2014 `Dataset & scale`, `Headline result` and `Limitations` must come from the full texts.")
    A("- **AIR exception:** if the supervisor rejects the five review articles, promote AIR-A6\u2026A10 (pre-verified research articles) "
      "from Appendix C and re-balance the branches.")
    A("")

    # ---------- master table ----------
    A("## R1 \u2014 Master table: the 20 papers")
    A("")
    A("- **Pods:** " + " \u00b7 ".join(f"{JOURNAL_SHORT[j]} = {PODS[j]}" for j in JOURNAL_ORDER) + ".")
    A("- **Column guide:** `PDF` and the paper title link to the file and the DOI \u00b7 `Method / platform` is the abstract-level value "
      "to verify \u00b7 `S2 \u00b7 S5` is 0\u20132 for rigor and for relevance to this review (medium appraisal: those two items are enough) \u00b7 "
      "`Notes` takes the quotable line with its page or section number.")
    A("- **Full texts** live in `papers/<journal>/<ID>_<Author>_<Year>_<ShortTitle>.pdf`; extraction notes in `sources/<ID>_*.md`.")
    A("")
    L.extend(md_table(MASTER_HEADERS, [master_row(r, pdf[r["id"]], note[r["id"]], prev_md.get(r["id"])) for r in selected]))
    A("")
    A("Cell rules: name datasets with their scale (rows, GB, nodes) \u2014 \"large-scale\" alone is not evidence \u00b7 list the baselines the "
      "authors compared against, since \"no baseline\" is itself a finding \u00b7 keep every number that produces the headline result.")
    A("")

    # ---------- ledger ----------
    A("## R2 \u2014 Claim-to-evidence ledger")
    A("")
    A("Append a row for every number, comparison or \"first/only\" claim in the manuscript: which paper backs it, where exactly, and who "
      "checked it. The row below is the format \u2014 replace it as real claims appear. Status flow: `Draft` \u2192 `Checked` (a second member "
      "opened the source and found the number) \u2192 `Frozen` (in the submitted text). Abstract-only backing is fine for a description, "
      "never for a number.")
    A("")
    L.extend(md_table(["Claim ID", "Claim (as written)", "Backing paper(s)", "Evidence (number + page/section)",
                       "Used in draft (\u00a7)", "Checked by", "Status"],
                      [["C-01", "one-sentence claim, exactly as it will appear in the draft", "TBD-1", "measured value + page",
                        "\u00a73.3", "reviewer name", "Draft"]]))
    A("")

    # ---------- Appendix A ----------
    A("## Appendix A \u2014 BibTeX (20 entries)")
    A("")
    A("Key rule: `firstauthorlastnameYYYYkeyword`. Fields come from the OpenAlex/Crossref records in `results/pool_selected.json`; "
      "`% TODO` lines mark what to verify at the publisher during the references pass. The same entries are in `paper/references.bib`, "
      "which a reference manager (Zotero, Mendeley, JabRef) imports in one step.")
    A("")
    for r in selected:
        A(f"#### {r['id']} \u00b7 {bibtex_key(r['id'], r)}")
        A("")
        A("```bibtex")
        for line in bibtex_entry(r["id"], r).split("\n"):
            A(line)
        A("```")
        A("")

    # ---------- Appendix B ----------
    A("## Appendix B \u2014 Reference strings, Springer Basic")
    A("")
    A("Generated in the style the assignment requires: `Lastname FN (Year) Title. Journal Vol(Issue):pages. https://doi.org/\u2026`. "
      "Don't retype these by hand \u2014 re-run the script after a swap. Clearing the Flags column is the references lead's checklist "
      "(author names are split mechanically, so compound surnames are flagged rather than guessed).")
    A("")
    L.extend(md_table(["ID", "Reference string (Springer Basic)", "Flags"],
                      [[r["id"], reference_string(r["id"], r), reference_flags(r["id"], r)] for r in selected]))
    A("")

    # ---------- Appendix C ----------
    A("## Appendix C \u2014 Alternates bench (29) and swap protocol")
    A("")
    A("All 29 are Crossref-verified and held in `results/pool_selected.json`. Nothing here is cited in the paper \u2014 they are insurance "
      "against access failures and against the AIR review-article exception being rejected.")
    A("")
    L.extend(md_table(["ID", "Title", "Access", "DOI", "Held for"],
                      [[r["id"], r["title"], "OA" if r.get("is_oa") else "PAID", f"[link](https://doi.org/{r['doi']})",
                        HELD_FOR.get(r["id"], DEFAULT_HELD)] for r in alternates]))
    A("")
    A("**Swap protocol** \u2014 only the integration editor approves a swap: use the alternate named for that journal in `Held for` first \u00b7 "
      "check it against the same criteria as the original in `notes/selection-backing.md` \u00b7 keep the branch balance above intact "
      "(like branch for like branch) \u00b7 re-run `python code/build_tracker.py` so this page, the BibTeX and the CSVs pick the swap up \u00b7 "
      "update `trackers/papers-pool.md` and the session log, then re-import this page into Notion.")
    A("")

    # ---------- Appendix D ----------
    A("## Appendix D \u2014 Column dictionary")
    A("")
    A("Who fills what, and with which words. Anything not listed here stays free text, one line per cell.")
    A("")
    L.extend(md_table(["Column", "Allowed values / format", "Owner"], [
        ["ID", "TBD-1 \u2026 TBD-5, BDR-1 \u2026 BDR-5, JoBD-1 \u2026 JoBD-5, AIR-1 \u2026 AIR-5 \u2014 never changes", "fixed"],
        ["Reader", "member name (pod leads assign, at least 2 papers per member)", "pod lead"],
        ["Read status", "Not started \u00b7 Skimmed \u00b7 Read \u00b7 Deep-read", "reader"],
        ["Method / platform", "what the paper builds and the platform it runs on (Spark, streaming, fog/cloud, cluster \u2026)", "reader"],
        ["Dataset & scale", "named datasets with scale: rows, GB, nodes, patients, streams", "reader"],
        ["Headline result", "the paper's main number, with the metric and the baseline it beats", "reader"],
        ["Limitations (theirs / ours)", "authors' admitted limits, then ours: weak baselines, no statistical tests, unevidenced scale claims", "reader"],
        ["Draft \u00a7", "\u00a73.3 methods \u00b7 \u00a73.4 platforms \u00b7 \u00a73.5 applications \u00b7 \u00a73.6 cross-cutting \u00b7 \u00a73.7 future (per `paper/outline.md`)", "theme lead"],
        ["S2 \u00b7 S5", "0 \u00b7 1 \u00b7 2 each: S2 method described well enough to reproduce, S5 relevance to this review", "reader"],
        ["Notes", "unique contribution, or the quotable line with page/section; agreement or contradiction with another pool ID", "theme lead"],
        ["Branch", "B1 scalable/interpretable methods \u00b7 B2 platforms/infrastructure \u00b7 B3 applications/domains \u00b7 B4 foundation models/LLMs \u00b7 B5 privacy/governance/evaluation", "taxonomy lead"],
        ["Dates", "ISO YYYY-MM-DD", "all"],
    ]))
    A("")
    A("`\u2020` marks abstract-level values \u2014 verify against the full text. `\u2014` means not yet filled: leave it empty rather than guessing.")
    A("")
    A("## Revision log")
    A("")
    A("Newest first. Add a row for every swap, import or structural change.")
    A("")
    L.extend(md_table(["Rev", "Date", "Change", "By"], [
        ["1", GENERATED, "Tracker created from pool rev 3 (20 selected + 29 alternates): single master table for the team, claim ledger, BibTeX, Springer Basic reference strings, alternates bench.", "workspace automation"],
    ]))
    A("")

    text = "\n".join(L) + "\n"
    bad = check_tables(L)
    blank = check_blank_lines(L)
    TRACKER_OUT.parent.mkdir(parents=True, exist_ok=True)
    TRACKER_OUT.write_text(text, encoding="utf-8")

    # ---------- references.bib ----------
    header = [
        "% references.bib - Big Data with Machine Learning: A Review",
        f"% 20 selected papers (pool rev 3, locked {GENERATED})",
        "% Generated by code/build_tracker.py from results/pool_selected.json.",
        "% Verify volume/issue/pages for the entries carrying a TODO before submission.",
        "",
    ]
    bib = "\n".join(header) + "\n\n".join(bibtex_entry(r["id"], r) for r in selected) + "\n"
    BIB_OUT.parent.mkdir(parents=True, exist_ok=True)
    BIB_OUT.write_text(bib, encoding="utf-8")

    # ---------- optional CSV set (same tables, for anyone who wants Notion databases) ----------
    CSV_OUT.mkdir(parents=True, exist_ok=True)
    for stale in ("registry.csv", "extraction.csv", "status.csv", "synthesis.csv", "appraisal.csv"):
        (CSV_OUT / stale).unlink(missing_ok=True)

    def write_csv(name, headers, rows):
        with (CSV_OUT / name).open("w", newline="", encoding="utf-8") as f:
            w = csv.writer(f, lineterminator="\n")
            w.writerow(headers)
            w.writerows(rows)

    csv_headers = ["ID", "Title", "DOI", "Year", "Journal", "Type", "Access", "PDF", "Note",
                   "Reader", "Read status", "Method / platform (abstract)", "Dataset and scale",
                   "Headline result", "Limitations (theirs / ours)", "Draft section", "S2", "S5", "Notes"]
    master_csv_rows = []
    for r in selected:
        filled = prev_csv.get(r["id"], {})
        defaults = {"Method / platform (abstract)": f"{r.get('ml_methods','')} / {r.get('bd_context','')}"}
        master_csv_rows.append([r["id"], r["title"], "https://doi.org/" + r["doi"], r["year"],
                                JOURNAL_FULL[r["journal_file"]],
                                "Review article" if is_review(r) else "Research article", access_long(r),
                                repo_url(pdf[r["id"]]) if pdf[r["id"]] else "",
                                repo_url(note[r["id"]]) if note[r["id"]] else ""]
                               + [filled.get(k) or defaults.get(k, "") for k in CSV_WORKING])
    write_csv("master.csv", csv_headers, master_csv_rows)
    write_csv("alternates.csv",
              ["ID", "Title", "Year", "Journal", "Access", "DOI", "Held for", "Status"],
              [[r["id"], r["title"], r["year"], JOURNAL_FULL[r["journal_file"]],
                "OA" if r.get("is_oa") else "PAID", "https://doi.org/" + r["doi"],
                HELD_FOR.get(r["id"], DEFAULT_HELD), "Verified (Crossref 2026-09-15)"] for r in alternates])
    write_csv("references.csv",
              ["ID", "Reference string (Springer Basic)", "Flags", "BibTeX key"],
              [[r["id"], reference_string(r["id"], r), reference_flags(r["id"], r), bibtex_key(r["id"], r)] for r in selected])

    print(f"wrote {TRACKER_OUT.relative_to(ROOT)} ({len(text.splitlines())} lines, {len(selected)} paper rows)")
    print(f"wrote {BIB_OUT.relative_to(ROOT)} ({len(selected)} entries)")
    print(f"wrote {CSV_OUT.relative_to(ROOT)}/ (3 CSVs, optional)")
    if bad:
        print("WARNING: inconsistent table widths in:", bad)
    if blank:
        print("WARNING: table not followed by a blank line at:", blank)


if __name__ == "__main__":
    build()
