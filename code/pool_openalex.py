"""Pull 2025+ articles for the four assignment journals from OpenAlex.

Outputs one JSON per journal in results/openalex_raw/ with the fields needed
for screening: doi, title, date, type, OA status, citations, authors, abstract.
"""
import json
import time
import urllib.request
import urllib.parse
from pathlib import Path

JOURNALS = {
    "IEEE_TBD": "S2491400915",   # IEEE Transactions on Big Data
    "BDR": "S2491565770",        # Big Data Research
    "JoBD": "S2737955091",       # Journal of Big Data
    "AIR": "S122814990",         # Artificial Intelligence Review
}
OUT = Path(__file__).resolve().parents[1] / "results" / "openalex_raw"
OUT.mkdir(parents=True, exist_ok=True)

SELECT = ",".join([
    "doi", "title", "publication_date", "type", "open_access",
    "cited_by_count", "authorships", "abstract_inverted_index",
    "primary_location", "biblio", "topics",
])
BASE = "https://api.openalex.org/works"


def fetch(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "bda-review-pool/1.0 (mailto:team8.bda@example.edu)"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def deinvert(inv: dict | None) -> str:
    if not inv:
        return ""
    pos = {}
    for word, idxs in inv.items():
        for i in idxs:
            pos[i] = word
    return " ".join(pos[i] for i in sorted(pos))


for name, sid in JOURNALS.items():
    cursor = "*"
    works = []
    while cursor:
        params = urllib.parse.urlencode({
            "filter": f"primary_location.source.id:{sid},from_publication_date:2025-01-01",
            "select": SELECT, "per-page": 200, "cursor": cursor,
        })
        data = fetch(f"{BASE}?{params}")
        works.extend(data.get("results", []))
        cursor = data.get("meta", {}).get("next_cursor")
        time.sleep(0.2)
    out = []
    for w in works:
        loc = (w.get("primary_location") or {}).get("source") or {}
        out.append({
            "doi": (w.get("doi") or "").replace("https://doi.org/", ""),
            "title": w.get("title") or "",
            "date": w.get("publication_date") or "",
            "type": w.get("type"),
            "is_oa": (w.get("open_access") or {}).get("is_oa"),
            "oa_status": (w.get("open_access") or {}).get("oa_status"),
            "cited_by": w.get("cited_by_count"),
            "authors": [a["author"]["display_name"] for a in (w.get("authorships") or [])][:6],
            "journal": loc.get("display_name"),
            "biblio": w.get("biblio"),
            "topics": [t.get("display_name") for t in (w.get("topics") or [])][:4],
            "abstract": deinvert(w.get("abstract_inverted_index")),
        })
    path = OUT / f"{name}.json"
    path.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{name}: {len(out)} works -> {path.name}")
