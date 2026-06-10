"""Render the four paper tables as standalone PNG images.

Designed to be embedded in the DOCX sent for advisor review when the native
DOCX table rendering misbehaves. Each PNG carries caption above and note
below, so the image is self-contained.

Output: paper/tables/table_{1,2,3,4}.png
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib import rcParams


ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "paper" / "tables"
OUT_DIR.mkdir(parents=True, exist_ok=True)


rcParams["font.family"] = "DejaVu Sans"
rcParams["pdf.fonttype"] = 42


HEADER_FILL = "#e8e8e8"
ZEBRA_FILL = "#fafafa"
GRID_COLOR = "#888888"


def render(
    caption: str,
    headers: list[str],
    rows: list[list[str]],
    note: str,
    out_path: Path,
    col_widths: list[float] | None = None,
    figsize: tuple[float, float] = (10.0, None),  # height auto
) -> None:
    n_rows = len(rows) + 1  # + header
    row_h = 0.42
    header_h = 0.55
    caption_h = 0.55
    note_lines = max(1, (len(note) // 110) + note.count("\n") + 1)
    note_h = 0.30 * note_lines + 0.10
    total_h = caption_h + header_h + row_h * len(rows) + note_h + 0.4

    fig_w, _ = figsize
    fig, ax = plt.subplots(figsize=(fig_w, total_h))
    ax.set_axis_off()

    if col_widths is None:
        col_widths = [1.0 / len(headers)] * len(headers)
    else:
        s = sum(col_widths)
        col_widths = [w / s for w in col_widths]

    table = ax.table(
        cellText=[headers] + rows,
        colWidths=col_widths,
        cellLoc="center",
        loc="center",
    )
    table.auto_set_font_size(False)
    table.set_fontsize(9.5)
    table.scale(1.0, 1.45)

    for (r, c), cell in table.get_celld().items():
        cell.set_edgecolor(GRID_COLOR)
        cell.set_linewidth(0.6)
        if r == 0:
            cell.set_facecolor(HEADER_FILL)
            cell.set_text_props(weight="bold", color="#1a1a1a")
        else:
            if r % 2 == 0:
                cell.set_facecolor(ZEBRA_FILL)
            cell.set_text_props(color="#1a1a1a")

    fig.suptitle(caption, fontsize=11, fontweight="bold", y=0.985, ha="center")

    fig.text(
        0.02, 0.015, note,
        fontsize=8.5, style="italic", color="#333333",
        ha="left", va="bottom", wrap=True,
    )

    fig.subplots_adjust(top=0.93, bottom=note_h / total_h + 0.04, left=0.02, right=0.98)
    fig.savefig(out_path, dpi=220, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"{out_path}  ({out_path.stat().st_size // 1024} KB)")


# ---------------------------------------------------------------------------
# Table 1 — Efficiency metrics per model
# ---------------------------------------------------------------------------
render(
    caption="Table 1. Efficiency metrics per model (n = 39 calls per row, ordered by increasing mean latency).",
    headers=["Model", "Mean latency (ms)", "Std. dev. (ms)", "p95 (ms)", "CV", "Output tokens (mean)"],
    rows=[
        ["qwen2.5:1.5b-instruct", "2,299",  "474",    "3,234",  "20.6 %",  "118.8"],
        ["llama3.2:1b",           "2,389",  "1,423",  "6,391",  "59.6 %",  "119.5"],
        ["qwen2.5:3b-instruct",   "2,906",  "552",    "4,486",  "19.0 %",  "104.6"],
        ["llama3.2:3b",           "3,020",  "695",    "4,721",  "23.0 %",  "108.9"],
        ["gemma2:2b",             "3,744",  "720",    "5,080",  "19.2 %",  "121.8"],
        ["gemma2:9b",             "8,681",  "1,425",  "11,130", "16.4 %",  "126.9"],
        ["llama3:8b",            "10,523", "19,708", "19,326", "187.3 %", "144.7"],
        ["phi3:mini",            "14,769", "12,228", "43,717", "82.8 %",  "471.2"],
    ],
    note="Note. CV = coefficient of variation (σ/μ); p95 = 95th percentile of latency. Mean output tokens "
         "reported via Ollama native telemetry (eval_count).",
    out_path=OUT_DIR / "table_1.png",
    col_widths=[2.8, 1.5, 1.3, 1.2, 1.0, 1.6],
    figsize=(11.0, None),
)


# ---------------------------------------------------------------------------
# Table 2 — Structural conformance per model
# ---------------------------------------------------------------------------
render(
    caption="Table 2. Structural conformance per model, with Wilson 95 % CI and Fisher exact test against the reference model.",
    headers=["Model", "k / n", "Conf. rate", "Wilson 95 % CI", "Tier", "Fisher vs. Qwen 3B"],
    rows=[
        ["qwen2.5:3b-instruct",   "39 / 39", "100.0 %", "[91.0 %; 100.0 %]", "deployable", "reference"],
        ["gemma2:9b",             "39 / 39", "100.0 %", "[91.0 %; 100.0 %]", "ceiling",    "p = 1.000 n.s."],
        ["llama3:8b",             "39 / 39", "100.0 %", "[91.0 %; 100.0 %]", "ceiling",    "p = 1.000 n.s."],
        ["qwen2.5:1.5b-instruct", "38 / 39", "97.4 %",  "[86.8 %; 99.5 %]",  "deployable", "p = 1.000 n.s."],
        ["gemma2:2b",             "38 / 39", "97.4 %",  "[86.8 %; 99.5 %]",  "deployable", "p = 1.000 n.s."],
        ["llama3.2:1b",           "0 / 39",  "0.0 %",   "[0.0 %; 9.0 %]",    "deployable", "p < 0.001 ***"],
        ["llama3.2:3b",           "0 / 39",  "0.0 %",   "[0.0 %; 9.0 %]",    "deployable", "p < 0.001 ***"],
        ["phi3:mini",             "0 / 39",  "0.0 %",   "[0.0 %; 9.0 %]",    "deployable", "p < 0.001 ***"],
    ],
    note="Note. k = conformant responses; n = 39 calls per model. *** p < 0.001, two-sided Fisher exact, "
         "α = 0.05. When a cell of the contingency table is zero, the odds ratio is not finitely estimable; "
         "the reported p-value derives from the exact hypergeometric distribution with continuity correction. "
         "Wilson 95 % CIs computed without normal approximation.",
    out_path=OUT_DIR / "table_2.png",
    col_widths=[2.8, 1.1, 1.2, 2.0, 1.2, 1.8],
    figsize=(11.0, None),
)


# ---------------------------------------------------------------------------
# Table 3 — Falsification protocol on the Llama 3.2 family
# ---------------------------------------------------------------------------
render(
    caption="Table 3. Structural conformance of the Llama 3.2 family under falsification isolations.",
    headers=["Isolation", "Llama 3.2 1B", "Llama 3.2 3B", "Wilson 95 % CI (3B)", "Fisher vs. baseline"],
    rows=[
        ["Baseline (zero-shot, t = 0.2)", "0 / 39 (0.0 %)",       "0 / 39 (0.0 %)",       "[0.0 %; 9.0 %]",    "—"],
        ["E1 (zero-shot, t = 0.0)",       "0 / 13 (0.0 %)",       "0 / 13 (0.0 %)",       "[0.0 %; 22.8 %]",   "p = 1.000 n.s."],
        ["E2 (one-shot, t = 0.2)",        "11 / 12 (91.7 %)¹",    "12 / 12 (100.0 %)",    "[75.8 %; 100.0 %]", "p < 0.001 ***"],
        ["E2b (one-shot, t = 0.0)",       "9 / 12 (75.0 %)²",     "12 / 12 (100.0 %)",    "[75.8 %; 100.0 %]", "p < 0.001 ***"],
        ["E3 (curl, zero-shot)",          "failure reproduced",   "failure reproduced",   "—",                 "—"],
    ],
    note="Note. ¹ The single non-conformance of the 1B in E2 derives from HTTP timeout, not from a structural "
         "violation of the response actually returned. ² Idem for 3 of 12 of the 1B in E2b — timeouts associated "
         "with the context-budget increase introduced by the demonstrative pair of one-shot, with no implication "
         "on the typological conformance of the completed calls. *** p < 0.001, two-sided Fisher exact, α = 0.05. "
         "Fisher comparisons reported for the 3B variant against its own zero-shot baseline (0/39); the 1B variant "
         "exhibits the same direction of effect under the same conventional thresholds.",
    out_path=OUT_DIR / "table_3.png",
    col_widths=[2.6, 2.0, 2.0, 1.9, 1.6],
    figsize=(11.0, None),
)


# ---------------------------------------------------------------------------
# Table 4 — Metalinguistic adherence of qwen2.5:3b-instruct
# ---------------------------------------------------------------------------
render(
    caption="Table 4. Metalinguistic adherence of qwen2.5:3b-instruct (Wilson 95 % CI).",
    headers=["Metric", "Result"],
    rows=[
        ["Scenarios mobilizing Koch terminology", "6 / 13 (46.2 %)"],
        ["Wilson 95 % CI",                        "[23.2 %; 70.9 %]"],
        ["Upper bound (optimistic)",              "70.9 %: absence in ≥ 29 % of scenarios"],
        ["Lower bound (pessimistic)",             "23.2 %: absence in ≥ 77 % of scenarios"],
        ["Classification",                        "Partial and unstable adherence (sustained by CI)"],
    ],
    note="Note. The width of the CI ([23.2 %; 70.9 %]) reflects the small n of canonical scenarios (n = 13) and "
         "constitutes an acknowledged limitation of this analysis; nevertheless, even the upper bound of the "
         "interval implies absence of metalinguistic terminology in at least 29 % of scenarios, preserving the "
         "characterization of partial and unstable adherence regardless of where the true rate lies within the interval.",
    out_path=OUT_DIR / "table_4.png",
    col_widths=[2.8, 4.2],
    figsize=(9.5, None),
)
