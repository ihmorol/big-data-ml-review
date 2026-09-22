#!/usr/bin/env python3
"""
make_figures.py - original, print-ready figures for the review
"Big Data with Machine Learning: A Review".

Design method follows the `figure-designer` skill (SKILL.md +
references/design-rules.md, motivated-example.md, solution-overview.md,
experimental-results.md):

  * Fig. 1  Motivated example  -> problem/landscape map (the corpus makes the
            review's problem visible: "learning on more data" vs
            "learning under constraints").
  * Fig. 2  Solution overview  -> taxonomy map (the organising scheme).
  * Fig. 3  Experimental results -> grouped/point anchors for reported results
            with an explicit "not available" band (honest axis; no zero-as-missing).
  * Fig. 4  Supporting trend figure -> stacked bar (method-generation shift).
  * Fig. 5  Selection flow -> PRISMA-style retrieval/screening/inclusion funnel
            (required by notes/writing-plan.md for the Introduction).

Every plotted value is traceable to a source note in `sources/*.md`
(and, for the full-text papers, to the paper PDF). The complete
value -> paper ID -> source-note mapping is in `fig-data-source.md`.

Outputs (written next to this script):
  fig1_corpus_landscape.{pdf,png}   two-column  (figure*)
  fig2_taxonomy.{pdf,png}           two-column  (figure*)
  fig3_evidence_anchors.{pdf,png}   two-column  (figure*)
  fig4_method_shift.{pdf,png}       single-column (figure)
  fig5_selection_flow.{pdf,png}     single-column (figure)

Reproduce:  python paper/figures/make_figures.py
Requires:   matplotlib, numpy
"""

from pathlib import Path
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
from matplotlib.lines import Line2D

FIGDIR = Path(__file__).resolve().parent

# ---------------------------------------------------------------------------
# Shared style  (print-friendly, colour-blind-safe, no chartjunk)
# ---------------------------------------------------------------------------
plt.rcParams.update(
    {
        "font.family": "serif",
        "font.serif": ["DejaVu Serif"],
        "font.size": 8.5,
        "axes.titlesize": 9.5,
        "axes.labelsize": 9,
        "xtick.labelsize": 8,
        "ytick.labelsize": 8,
        "legend.fontsize": 7.5,
        "axes.linewidth": 0.8,
        "axes.edgecolor": "#444444",
        "grid.color": "#DDDDDD",
        "grid.linewidth": 0.6,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.02,
        "figure.dpi": 120,
    }
)

# Okabe-Ito colour-blind-safe palette
OI = {
    "blue": "#0072B2",
    "orange": "#E69F00",
    "green": "#009E73",
    "vermillion": "#D55E00",
    "pink": "#CC79A7",
    "sky": "#56B4E9",
    "grey": "#BBBBBB",
    "darkgrey": "#666666",
}

JOURNAL_COLOR = {
    "TBD": OI["blue"],          # IEEE Transactions on Big Data
    "BDR": OI["green"],         # Big Data Research
    "JoBD": OI["vermillion"],   # Journal of Big Data
    "AIR": OI["pink"],          # Artificial Intelligence Review
}
JOURNAL_LABEL = {
    "TBD": "IEEE Trans. Big Data",
    "BDR": "Big Data Research",
    "JoBD": "J. Big Data",
    "AIR": "Artif. Intell. Rev.",
}

# Canonical citation number per paper (notes/writing-plan.md §3.2). Pool IDs
# (TBD-x / AIR-x) are internal keys only and must NOT appear in the figures;
# the manuscript cites papers by these bracketed numbers.
CIT = {
    "TBD-4": 1, "TBD-5": 2, "JoBD-5": 3, "BDR-5": 4, "TBD-1": 5, "AIR-3": 6,
    "BDR-2": 7, "BDR-3": 8, "JoBD-4": 9, "BDR-1": 10, "AIR-2": 11,
    "BDR-4": 12, "JoBD-1": 13, "JoBD-3": 14, "TBD-2": 15, "TBD-3": 16,
    "AIR-1": 17, "JoBD-2": 18, "AIR-4": 19, "AIR-5": 20,
}


def cite(pid):
    """Pool ID -> manuscript citation label, e.g. 'TBD-5' -> '[2]'."""
    return f"[{CIT[pid]}]"

# Evidence-tier -> colour (Fig. 3)
TIER_COLOR = {
    "full": OI["blue"],        # full-text verified
    "abstract": OI["orange"],  # abstract-only, threshold values
    "review": OI["pink"],      # review / second-hand range
    "na": OI["grey"],          # not available / qualitative only
}

# Method generation -> colour (Fig. 4)
GEN_COLOR = {
    "Classical": OI["grey"],
    "Deep": OI["blue"],
    "LLM / FM": OI["vermillion"],
    "Not specified": OI["darkgrey"],
}


def save(fig, name):
    """Save one figure as vector PDF (for pdflatex) and 300-dpi PNG (preview)."""
    pdf = FIGDIR / f"{name}.pdf"
    png = FIGDIR / f"{name}.png"
    fig.savefig(pdf, format="pdf")
    fig.savefig(png, format="png", dpi=300)
    plt.close(fig)
    print(f"wrote {pdf.name} and {png.name}")


# ---------------------------------------------------------------------------
# Shared corpus data
# ---------------------------------------------------------------------------
# journal: TBD | BDR | JoBD | AIR ; kind: research | review
PAPERS = {
    "TBD-1": dict(journal="TBD", kind="research"),
    "TBD-2": dict(journal="TBD", kind="research"),
    "TBD-3": dict(journal="TBD", kind="research"),
    "TBD-4": dict(journal="TBD", kind="research"),
    "TBD-5": dict(journal="TBD", kind="research"),
    "BDR-1": dict(journal="BDR", kind="research"),
    "BDR-2": dict(journal="BDR", kind="research"),
    "BDR-3": dict(journal="BDR", kind="research"),
    "BDR-4": dict(journal="BDR", kind="research"),
    "BDR-5": dict(journal="BDR", kind="research"),
    "JoBD-1": dict(journal="JoBD", kind="research"),
    "JoBD-2": dict(journal="JoBD", kind="research"),
    "JoBD-3": dict(journal="JoBD", kind="research"),
    "JoBD-4": dict(journal="JoBD", kind="research"),
    "JoBD-5": dict(journal="JoBD", kind="research"),
    "AIR-1": dict(journal="AIR", kind="review"),
    "AIR-2": dict(journal="AIR", kind="review"),
    "AIR-3": dict(journal="AIR", kind="review"),
    "AIR-4": dict(journal="AIR", kind="review"),
    "AIR-5": dict(journal="AIR", kind="review"),
}

BRANCHES = {
    "B1": dict(label="Scalable &\ninterpretable methods",
               papers=["TBD-1", "TBD-4", "TBD-5", "BDR-5", "JoBD-5"], section="§3.3"),
    "B2": dict(label="Platforms, pipelines\n& infrastructure",
               papers=["BDR-2", "BDR-3", "JoBD-4"], section="§3.4"),
    "B3": dict(label="Applications\n& domains",
               papers=["BDR-1", "BDR-4", "JoBD-1", "JoBD-3", "AIR-2"], section="§3.5"),
    "B4": dict(label="Foundation models\n& LLMs",
               papers=["TBD-2", "TBD-3", "AIR-1", "AIR-3"], section="§3.3 / §3.5"),
    "B5": dict(label="Privacy, governance\n& evaluation",
               papers=["JoBD-2", "AIR-4", "AIR-5"], section="§3.6"),
}


# ===========================================================================
# FIGURE 1 - Corpus landscape (motivated example / problem map)
# ===========================================================================
def fig1_corpus_landscape():
    X_LEVELS = [
        "Curated benchmarks\n(no primary scale)",
        "Moderate /\nsingle-GPU",
        "Large-scale\nframing",
        "Institution /\ndistributed",
        "Streaming\nvelocity",
        "Distributed\nplatform",
    ]
    Y_LEVELS = [
        "None\n(accuracy)",
        "Explain-\nability",
        "Reproduci-\nbility",
        "Platform /\nstreaming",
        "Privacy",
        "Compute /\nrepresent.",
    ]
    # Curated design mapping (methodological judgement; documented in README +
    # fig-data-source.md). x = data scale / kind, y = binding constraint.
    # Slight fractional offsets keep coincident categories legible.
    POS = {
        "AIR-3": (-0.10, 0.03), "AIR-1": (0.16, 0.25), "TBD-4": (0.34, -0.04),
        "JoBD-1": (0.80, 0.00), "TBD-3": (1.18, 0.20), "TBD-2": (1.30, -0.20),
        "TBD-1": (2.00, -0.02), "BDR-4": (2.30, 0.18),
        "BDR-1": (2.00, 1.00),
        "AIR-2": (0.00, 2.00), "AIR-5": (0.42, 2.20),
        "TBD-5": (4.00, 3.02), "JoBD-4": (4.40, 3.22), "BDR-3": (5.00, 3.00),
        "BDR-2": (3.00, 4.00), "JoBD-2": (3.42, 4.20), "AIR-4": (0.00, 4.00),
        "BDR-5": (2.00, 5.00), "JoBD-5": (2.34, 5.16), "JoBD-3": (1.20, 5.00),
    }

    fig, ax = plt.subplots(figsize=(7.0, 4.7))

    ax.set_xticks(range(len(X_LEVELS)))
    ax.set_yticks(range(len(Y_LEVELS)))
    ax.set_xticklabels(X_LEVELS, fontsize=7.4)
    ax.set_yticklabels(Y_LEVELS, fontsize=7.6)
    ax.set_xlim(-0.5, len(X_LEVELS) - 0.5)
    ax.set_ylim(-0.5, len(Y_LEVELS) - 0.5)
    ax.grid(True, which="major", zorder=0)
    ax.set_axisbelow(True)

    for pid, (x, y) in POS.items():
        p = PAPERS[pid]
        marker = "o" if p["kind"] == "research" else "s"
        ax.scatter(
            x, y,
            s=150 if p["kind"] == "research" else 115,
            c=JOURNAL_COLOR[p["journal"]], marker=marker,
            edgecolors="white", linewidths=0.9, zorder=4,
        )
        dy = -14 if y >= 4.6 else 9
        ax.annotate(
            cite(pid), (x, y), textcoords="offset points", xytext=(0, dy),
            ha="center", fontsize=6.6, color="#222222", zorder=5,
        )

    # Constraint thesis framing
    ax.axhspan(0.55, 5.5, color=OI["orange"], alpha=0.05, zorder=1)
    ax.annotate("Learning under constraints\n(privacy / platform / proof)",
                xy=(4.55, 5.42), ha="center", va="top", fontsize=7.2,
                color="#8a5a00", style="italic")
    ax.annotate("Learning on more data\n(accuracy-led)",
                xy=(4.30, -0.42), ha="center", va="bottom", fontsize=7.2,
                color="#8a0000", style="italic")

    ax.set_xlabel("Data scale / kind  (from curated benchmarks to distributed engines)",
                  fontsize=8.4)
    ax.set_ylabel("Binding constraint  (what the paper optimises)", fontsize=8.4)

    jhandles = [
        Line2D([], [], marker="o", linestyle="", markersize=7,
               markerfacecolor=JOURNAL_COLOR[j], markeredgecolor="white",
               label=JOURNAL_LABEL[j])
        for j in ["TBD", "BDR", "JoBD", "AIR"]
    ]
    khandles = [
        Line2D([], [], marker="o", linestyle="", markersize=6.5,
               markerfacecolor="#777777", markeredgecolor="white",
               label="original research (15)"),
        Line2D([], [], marker="s", linestyle="", markersize=6.5,
               markerfacecolor="#777777", markeredgecolor="white",
               label="review article (5, AIR)"),
    ]
    fig.legend(handles=jhandles + khandles, loc="lower center", ncol=3,
               frameon=False, bbox_to_anchor=(0.5, -0.02),
               handletextpad=0.4, columnspacing=1.3)
    fig.tight_layout(rect=(0, 0.11, 1, 1))
    save(fig, "fig1_corpus_landscape")


# ===========================================================================
# FIGURE 2 - Taxonomy / solution overview (the map)
# ===========================================================================
def _chips(ax, x0, y_bottom, w, papers):
    cols = 3
    gap = 0.006
    chip_w = (w - 2 * gap) / cols
    chip_h = 0.030
    for i, pid in enumerate(papers):
        r, c = divmod(i, cols)
        cx = x0 + c * (chip_w + gap)
        cy = y_bottom - (r + 1) * (chip_h + 0.008)
        ax.add_patch(
            FancyBboxPatch(
                (cx, cy), chip_w, chip_h,
                boxstyle="round,pad=0.001,rounding_size=0.007",
                linewidth=0.6, edgecolor="#999999",
                facecolor=JOURNAL_COLOR[PAPERS[pid]["journal"]],
                alpha=0.9, zorder=3,
            )
        )
        ax.text(cx + chip_w / 2, cy + chip_h / 2, cite(pid), ha="center",
                va="center", fontsize=6.4, color="white", zorder=4)


def fig2_taxonomy():
    fig, ax = plt.subplots(figsize=(7.0, 4.8))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    def strip(y0, h, line1, line2):
        ax.add_patch(Rectangle((0.02, y0), 0.96, h,
                               facecolor="#EEF3F8", edgecolor="#B9CBDA", lw=0.8))
        ax.text(0.035, y0 + h * 0.66, line1, fontsize=8.2, fontweight="bold",
                va="center", color="#1f4e70")
        ax.text(0.035, y0 + h * 0.26, line2, fontsize=7.8, va="center",
                color="#1f4e70")

    # Axis strips (title + content on separate lines -> no overlap)
    strip(0.895, 0.10, "Axis 1 — what is learned",
          "classical / statistical    →    deep & purpose-built    →    LLM / foundation models")
    strip(0.020, 0.11, "Axis 2 — what surrounds the learning",
          "platform (B2)    ·    domain (B3)    ·    governance (B5)")

    xs = [0.02, 0.345, 0.67]
    w = 0.31
    row1_y, row2_y, bh = 0.525, 0.155, 0.330

    boxes = [("B1", xs[0], row1_y), ("B2", xs[1], row1_y), ("B3", xs[2], row1_y),
             ("B4", xs[0], row2_y), ("B5", xs[1], row2_y)]
    for key, bx, by in boxes:
        b = BRANCHES[key]
        ax.add_patch(
            FancyBboxPatch(
                (bx, by), w, bh,
                boxstyle="round,pad=0.004,rounding_size=0.02",
                linewidth=1.0, edgecolor="#5a6672", facecolor="#FBFBFB", zorder=2,
            )
        )
        ax.text(bx + 0.012, by + bh - 0.014, b["label"], fontsize=7.4,
                fontweight="bold", va="top", ha="left", color="#243038", zorder=3)
        ax.text(bx + 0.012, by + bh - 0.078, f"{len(b['papers'])} papers",
                fontsize=6.5, va="top", ha="left", color="#7a8794", zorder=3)
        ax.text(bx + w - 0.012, by + 0.014, b["section"], fontsize=6.6,
                va="bottom", ha="right", color="#7a8794", style="italic", zorder=3)
        _chips(ax, bx + 0.012, by + 0.105, w - 0.024, b["papers"])

    # Empty-cells findings box
    ex, ey = xs[2], row2_y
    ax.add_patch(
        FancyBboxPatch(
            (ex, ey), w, bh,
            boxstyle="round,pad=0.004,rounding_size=0.02",
            linewidth=1.0, edgecolor="#B0885a", facecolor="#FBF6EE",
            linestyle="--", zorder=2,
        )
    )
    ax.text(ex + 0.014, ey + bh - 0.014, "Empty cells (findings)", fontsize=7.4,
            fontweight="bold", va="top", ha="left", color="#8a5a00", zorder=3)
    ax.text(ex + 0.014, ey + bh - 0.062,
            "• no reinforcement-learning-at-scale paper\n"
            "• no purely theoretical contribution\n"
            "• no 2027-dated item",
            fontsize=6.1, va="top", ha="left", color="#5a4527", zorder=3,
            linespacing=1.7)

    # branch-flow arrow in the inter-row gap
    ax.annotate("", xy=(0.985, 0.495), xytext=(0.015, 0.495),
                arrowprops=dict(arrowstyle="-|>", color="#9AA7B4", lw=1.0), zorder=1)
    ax.text(0.5, 0.495, "  every paper sits in exactly one branch  ",
            fontsize=6.5, ha="center", va="center", color="#7a8794",
            backgroundcolor="#FFFFFF", style="italic", zorder=3)

    save(fig, "fig2_taxonomy")


# ===========================================================================
# FIGURE 3 - Reported-result anchors (results figure)
# ===========================================================================
def fig3_evidence_anchors():
    acc = [
        ("JoBD-5", "CampusNet F1", 99.13, "full"),
        ("JoBD-3", "IEMOCAP acc.", 99.82, "full"),
        ("JoBD-3", "MELD acc.", 99.81, "full"),
        ("JoBD-1", "12-class acc.", 97.33, "full"),
        ("JoBD-2", "adaptive agg. acc.", 96.30, "full"),
        ("JoBD-2", "centralised+DP (σ²=1.0)", 94.50, "full"),
        ("TBD-5", "ECG GSTrees >94%", 94.00, "abstract"),
        ("TBD-5", "fraud ROC-AUC >94%", 94.00, "abstract"),
        ("JoBD-5", "UNSW F1", 93.41, "full"),
        ("TBD-5", "ECG GWAAE ROC-AUC >89%", 89.00, "abstract"),
        ("JoBD-5", "CICIDS F1", 83.66, "full"),
        ("TBD-5", "fraud recall >82%", 82.00, "abstract"),
        ("TBD-5", "SMTP ROC-AUC >80%", 80.00, "abstract"),
    ]
    acc.sort(key=lambda r: r[2])

    fig, (axA, axB) = plt.subplots(
        1, 2, figsize=(7.0, 4.6), gridspec_kw={"width_ratios": [1.95, 1.0]}
    )

    # ---- Panel A : percent anchors ----
    for i, (pid, lab, val, tier) in enumerate(acc):
        hatch = "//" if tier == "abstract" else None
        axA.barh(i, val, color=TIER_COLOR[tier], edgecolor="white",
                 linewidth=0.6, hatch=hatch, height=0.66, zorder=3)
        axA.text(val + 1.2, i, f"{val:g}", va="center", ha="left",
                 fontsize=6.6, color="#333333", zorder=4)
    axA.set_yticks(range(len(acc)))
    axA.set_yticklabels([f"{cite(p)} · {l}" for p, l, v, t in acc], fontsize=6.8)
    axA.set_xlim(0, 108)
    axA.set_ylim(-3.9, len(acc) - 0.35)
    axA.set_xlabel("Reported headline score  (%)", fontsize=8.2)
    axA.set_title("(a) Classification / detection anchors", fontsize=8.6)
    axA.grid(True, axis="x", zorder=0)
    axA.set_axisbelow(True)
    axA.axhline(-0.5, color="#999999", lw=0.7, ls=":")

    # review / second-hand band, placed left of its value so it stays in-frame
    axA.errorbar(88, -1.3, xerr=[[6], [6]], fmt="o", color=TIER_COLOR["review"],
                 ecolor=TIER_COLOR["review"], elinewidth=1.6, capsize=3, zorder=4)
    axA.text(79, -1.3, "[11] review band\n85–97", va="center", ha="right",
             fontsize=6.4, color=TIER_COLOR["review"])
    # honest "not available" note, left-anchored so it cannot overflow
    axA.text(0, -2.00,
             "No comparable metric available:  [4], [5], [8], [12], [15], [16]\n"
             "Qualitative claims only:  [6], [7], [10], [17], [19]\n"
             "Reproducibility audit (panel b):  [20]",
             va="top", ha="left", fontsize=6.2, color="#555555", linespacing=1.45)

    # ---- Panel B : regression-error anchors ----
    rmse = [
        ("JoBD-4", "HR", 1.54),
        ("JoBD-4", "SBP", 4.14),
        ("AIR-5", "as published", 11.62),
        ("AIR-5", "audit re-run", 12.39),
    ]
    for i, (pid, lab, val) in enumerate(rmse):
        col = "#7a9db8" if "reproduced" in lab else TIER_COLOR["full"]
        axB.bar(i, val, color=col, edgecolor="white", linewidth=0.6,
                width=0.6, zorder=3)
        axB.text(i, val + 0.3, f"{val:.2f}", ha="center", va="bottom",
                 fontsize=6.6, color="#333333", zorder=4)
    axB.annotate("", xy=(3, 12.05), xytext=(2, 11.28),
                 arrowprops=dict(arrowstyle="-|>", color="#7a9db8", lw=1.0,
                                 connectionstyle="arc3,rad=-0.3"), zorder=5)
    axB.set_xticks(range(len(rmse)))
    axB.set_xticklabels(
        ["[9]\nHR", "[9]\nSBP", "[20]\nas\npubl.", "[20]\naudit\nre-run"],
        fontsize=5.7,
    )
    axB.set_xlim(-0.6, 3.6)
    axB.set_ylabel("RMSE  (lower is better)", fontsize=8.2)
    axB.set_ylim(0, 14.8)
    axB.set_title("(b) Regression-error anchors", fontsize=8.6)
    axB.grid(True, axis="y", zorder=0)
    axB.set_axisbelow(True)

    handles = [
        Line2D([], [], marker="s", linestyle="", markersize=7,
               markerfacecolor=TIER_COLOR["full"], markeredgecolor="white",
               label="full-text verified"),
        Line2D([], [], marker="s", linestyle="", markersize=7,
               markerfacecolor=TIER_COLOR["abstract"], markeredgecolor="white",
               label="abstract-only (threshold values)"),
        Line2D([], [], marker="s", linestyle="", markersize=7,
               markerfacecolor=TIER_COLOR["review"], markeredgecolor="white",
               label="review / second-hand range"),
        Line2D([], [], marker="s", linestyle="", markersize=7,
               markerfacecolor=TIER_COLOR["na"], markeredgecolor="#999999",
               label="no metric / qualitative only"),
    ]
    fig.legend(handles=handles, loc="lower center", ncol=4, frameon=False,
               bbox_to_anchor=(0.5, -0.02), columnspacing=1.4, handletextpad=0.4)
    fig.tight_layout(rect=(0, 0.05, 1, 1))
    save(fig, "fig3_evidence_anchors")


# ===========================================================================
# FIGURE 4 - Method-generation shift across the corpus
# ===========================================================================
def fig4_method_shift():
    gen = {
        "TBD-1": "Deep", "TBD-2": "LLM / FM", "TBD-3": "LLM / FM",
        "TBD-4": "Deep", "TBD-5": "Deep",
        "BDR-1": "Deep", "BDR-2": "Deep", "BDR-3": "Not specified",
        "BDR-4": "Deep", "BDR-5": "Classical",
        "JoBD-1": "Deep", "JoBD-2": "Deep", "JoBD-3": "LLM / FM",
        "JoBD-4": "Deep", "JoBD-5": "Deep",
        "AIR-1": "LLM / FM", "AIR-2": "Deep", "AIR-3": "LLM / FM",
        "AIR-4": "Deep", "AIR-5": "Deep",
    }
    order = ["Classical", "Deep", "LLM / FM", "Not specified"]
    journals = ["TBD", "BDR", "JoBD", "AIR"]

    fig, ax = plt.subplots(figsize=(3.5, 2.7))
    left = [0] * len(journals)
    for g in order:
        counts = [sum(1 for pid, gg in gen.items()
                      if gg == g and PAPERS[pid]["journal"] == j)
                  for j in journals]
        ax.barh(range(len(journals)), counts, left=left, color=GEN_COLOR[g],
                edgecolor="white", linewidth=0.6, height=0.6, label=g, zorder=3)
        for i, c in enumerate(counts):
            if c:
                ax.text(left[i] + c / 2, i, str(c), ha="center", va="center",
                        fontsize=6.6, color="white", zorder=4)
        left = [l + c for l, c in zip(left, counts)]

    ax.set_yticks(range(len(journals)))
    ax.set_yticklabels([JOURNAL_LABEL[j] for j in journals], fontsize=6.8)
    ax.set_xlabel("Papers (n = 20)", fontsize=8.2)
    ax.set_xlim(0, 5.6)
    ax.set_xticks(range(0, 6))
    ax.grid(True, axis="x", zorder=0)
    ax.set_axisbelow(True)
    ax.invert_yaxis()
    ax.legend(title="Method generation", ncol=2, frameon=False, fontsize=6.3,
              title_fontsize=6.5, loc="upper center", bbox_to_anchor=(0.5, -0.24))
    fig.tight_layout()
    save(fig, "fig4_method_shift")


# ===========================================================================
# FIGURE 5 - Selection flow (PRISMA-style funnel)
# ===========================================================================
def fig5_selection_flow():
    # Exact counts from trackers/paper-tracker.md
    # "How the 20 papers were chosen (the numbers behind Fig. 1)".
    stages = [
        ("Retrieved from OpenAlex (2025+)",
         {"TBD": 296, "BDR": 101, "JoBD": 480, "AIR": 642}, 1519),
        ("Passed keyword screen (ML + big data)",
         {"TBD": 70, "BDR": 10, "JoBD": 177, "AIR": 184}, 441),
        ("Verified against Crossref",
         {"TBD": 11, "BDR": 11, "JoBD": 12, "AIR": 15}, 49),
        ("Included in the review",
         {"TBD": 5, "BDR": 5, "JoBD": 5, "AIR": 5}, 20),
    ]
    journals = ["TBD", "BDR", "JoBD", "AIR"]

    fig, ax = plt.subplots(figsize=(3.6, 3.0))
    for i, (name, split, total) in enumerate(stages):
        left = 1e-9  # avoid log(0) at the axis
        for j in journals:
            v = split[j]
            ax.barh(i, v, left=left, color=JOURNAL_COLOR[j], edgecolor="white",
                    linewidth=0.6, height=0.62, zorder=3)
            left += v
        ax.text(total * 1.18, i, f"n = {total}", va="center", ha="left",
                fontsize=6.8, color="#333333", fontweight="bold", zorder=4)
    ax.set_yticks(range(len(stages)))
    ax.set_yticklabels([s[0] for s in stages], fontsize=6.5)
    ax.set_xscale("log")
    ax.set_xlim(3, 9000)
    ax.set_xlabel("Papers  (log scale)", fontsize=8.2)
    ax.grid(True, axis="x", zorder=0)
    ax.set_axisbelow(True)
    ax.invert_yaxis()

    handles = [
        Line2D([], [], marker="s", linestyle="", markersize=7,
               markerfacecolor=JOURNAL_COLOR[j], markeredgecolor="white",
               label=JOURNAL_LABEL[j])
        for j in journals
    ]
    ax.legend(handles=handles, ncol=2, frameon=False, fontsize=6.2,
              loc="upper center", bbox_to_anchor=(0.5, -0.26))
    fig.tight_layout()
    save(fig, "fig5_selection_flow")


def main():
    FIGDIR.mkdir(parents=True, exist_ok=True)
    fig1_corpus_landscape()
    fig2_taxonomy()
    fig3_evidence_anchors()
    fig4_method_shift()
    fig5_selection_flow()


if __name__ == "__main__":
    main()
