#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Renderiza paper/jbcs/main.tex (fonte de verdade, classe sbc2023) para um PDF
usando reportlab (platypus). Reaproveita exatamente o mesmo parsing de LaTeX do
conversor irmao tex_to_docx.py (secoes, listas, tabelas/table*, lstlisting,
quotation, figuras, \\citep/\\citet, \\ref, \\href, \\textbf/\\textit/\\texttt,
math como $\\kappa$/$\\times$, \\multicolumn, Declarations e References).

Uso: python3 paper/jbcs/tex_to_pdf.py
Saida: paper/jbcs/benchmark_slm_jbcs.pdf
"""
import re, os

# --- reaproveita o parsing conhecido-bom do conversor .docx ---------------
# tex_to_docx.py guarda toda execucao/IO sob `if __name__ == "__main__":`,
# entao importar nao dispara conversao alguma; so traz dicts + helpers.
from tex_to_docx import (
    CITE, REF, REFERENCES, DECL_TITLES,
    first_braced, render_cite, math_sub, preprocess,
    fmt, plain, strip_multicolumn, strip_comments,
    HERE, TEX,
)

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image,
    Preformatted, KeepTogether,
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas as _canvas  # noqa: F401 (garante import valido)

OUT = os.path.join(HERE, "benchmark_slm_jbcs.pdf")

# --- fontes: Times New Roman tem cobertura grega/unicode (kappa, sigma...) -
SYS = "/System/Library/Fonts/Supplemental"
SERIF, SERIF_B, SERIF_I, SERIF_BI = "TNR", "TNR-Bold", "TNR-Italic", "TNR-BoldItalic"
MONO = "Courier"  # built-in (ASCII suficiente para codigo)


def register_fonts():
    """Registra Times New Roman (4 variantes) se disponivel; senao usa Times-Roman."""
    global SERIF, SERIF_B, SERIF_I, SERIF_BI
    fam = {
        SERIF: "Times New Roman.ttf",
        SERIF_B: "Times New Roman Bold.ttf",
        SERIF_I: "Times New Roman Italic.ttf",
        SERIF_BI: "Times New Roman Bold Italic.ttf",
    }
    try:
        for name, fn in fam.items():
            pdfmetrics.registerFont(TTFont(name, os.path.join(SYS, fn)))
        pdfmetrics.registerFontFamily(
            SERIF, normal=SERIF, bold=SERIF_B, italic=SERIF_I, boldItalic=SERIF_BI)
    except Exception:
        # fallback para os Type1 embutidos (sem grego, mas nao quebra)
        SERIF, SERIF_B, SERIF_I, SERIF_BI = (
            "Times-Roman", "Times-Bold", "Times-Italic", "Times-BoldItalic")


# --- estilos --------------------------------------------------------------
def make_styles():
    ss = getSampleStyleSheet()
    s = {}
    s["title"] = ParagraphStyle("p_title", parent=ss["Title"], fontName=SERIF_B,
                                fontSize=15, leading=18, alignment=TA_CENTER,
                                spaceAfter=8)
    s["author"] = ParagraphStyle("p_author", parent=ss["Normal"], fontName=SERIF,
                                 fontSize=10.5, leading=13, alignment=TA_CENTER,
                                 spaceAfter=2)
    s["affil"] = ParagraphStyle("p_affil", parent=ss["Normal"], fontName=SERIF_I,
                                fontSize=9.5, leading=12, alignment=TA_CENTER,
                                spaceAfter=10)
    s["body"] = ParagraphStyle("p_body", parent=ss["Normal"], fontName=SERIF,
                               fontSize=10.5, leading=14, alignment=TA_JUSTIFY,
                               spaceAfter=6)
    s["abstract"] = ParagraphStyle("p_abstract", parent=s["body"], fontSize=9.8,
                                   leading=13, leftIndent=0.6 * cm,
                                   rightIndent=0.6 * cm)
    s["h1"] = ParagraphStyle("p_h1", parent=ss["Heading1"], fontName=SERIF_B,
                             fontSize=13, leading=16, spaceBefore=12, spaceAfter=5,
                             textColor=colors.black)
    s["h2"] = ParagraphStyle("p_h2", parent=ss["Heading2"], fontName=SERIF_B,
                             fontSize=11.5, leading=14, spaceBefore=9, spaceAfter=4,
                             textColor=colors.black)
    s["h3"] = ParagraphStyle("p_h3", parent=ss["Heading3"], fontName=SERIF_BI,
                             fontSize=10.5, leading=13, spaceBefore=7, spaceAfter=3,
                             textColor=colors.black)
    s["list"] = ParagraphStyle("p_list", parent=s["body"], leftIndent=0.8 * cm,
                               bulletIndent=0.3 * cm, spaceAfter=3)
    s["caption"] = ParagraphStyle("p_caption", parent=s["body"], fontSize=9.2,
                                  leading=12, alignment=TA_LEFT, spaceBefore=4,
                                  spaceAfter=3)
    s["cell"] = ParagraphStyle("p_cell", parent=ss["Normal"], fontName=SERIF,
                               fontSize=8, leading=9.5, alignment=TA_LEFT)
    s["cellh"] = ParagraphStyle("p_cellh", parent=s["cell"], fontName=SERIF_B)
    s["quote"] = ParagraphStyle("p_quote", parent=s["body"], fontName=SERIF_I,
                                leftIndent=0.9 * cm, rightIndent=0.6 * cm,
                                fontSize=10, leading=13)
    s["code"] = ParagraphStyle("p_code", parent=ss["Code"], fontName=MONO,
                               fontSize=7.2, leading=8.6, textColor=colors.black)
    s["ref"] = ParagraphStyle("p_ref", parent=s["body"], fontSize=9.5, leading=12,
                              leftIndent=0.7 * cm, firstLineIndent=-0.7 * cm,
                              spaceAfter=4, alignment=TA_LEFT)
    return s


# --- inline: runs do fmt() -> markup do reportlab -------------------------
def esc(t):
    """Escapa &,<,> ANTES de injetar tags de markup do reportlab."""
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def runs_to_markup(runs):
    out = []
    for txt, b, ital, mono in runs:
        t = esc(txt)
        if mono:
            t = '<font face="%s">%s</font>' % (MONO, t)
        if ital:
            t = "<i>%s</i>" % t
        if b:
            t = "<b>%s</b>" % t
        out.append(t)
    return "".join(out)


def P(text, style):
    """Paragraph defensivo: se o markup quebrar, cai para texto plano escapado."""
    try:
        return Paragraph(runs_to_markup(fmt(text)), style)
    except Exception:
        try:
            return Paragraph(esc(plain(text)), style)
        except Exception:
            return Paragraph("", style)


def P_markup(markup, style):
    try:
        return Paragraph(markup, style)
    except Exception:
        return Paragraph(esc(re.sub(r"<[^>]+>", "", markup)), style)


AVAIL_W = A4[0] - 4 * cm  # margens de 2cm de cada lado


# --- montagem do documento ------------------------------------------------
def build():
    register_fonts()
    S = make_styles()
    src = open(TEX, encoding="utf-8").read()
    flow = []

    # titulo
    m = re.search(r"\\title(?:\[[^\]]*\])?\{(.+?)\}\s*\n", src, re.S)
    title = plain(m.group(1)) if m else "Paper"
    flow.append(P_markup(esc(title), S["title"]))

    # autores (simplificado: nomes + afiliacao unica)
    authors = re.findall(r"\\affil\{\\textbf\{([^}]+)\}", src)
    if authors:
        flow.append(P_markup("; ".join(esc(plain(a)) for a in authors), S["author"]))
    flow.append(P_markup(
        "Graduate Program in Informatics in Education (PPGIE), "
        "Federal University of Rio Grande do Sul (UFRGS), Porto Alegre, RS, Brazil",
        S["affil"]))

    # abstract
    ma = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", src, re.S)
    if ma:
        body = ma.group(1).replace(r"\textbf{Abstract.~}", "").strip()
        flow.append(P_markup("<b>Abstract</b>", S["h2"]))
        flow.append(P(body, S["abstract"]))
    mk = re.search(r"\\begin\{keywords\}(.*?)\\end\{keywords\}", src, re.S)
    if mk:
        flow.append(P_markup("<b>Keywords:</b> " + esc(plain(mk.group(1).strip())),
                             S["abstract"]))
    flow.append(Spacer(1, 6))

    # corpo
    bstart = src.index(r"\section{Introduction}")
    bend = src.index(r"\section*{Declarations}")
    process_body(flow, src[bstart:bend], S)

    # declaracoes
    flow.append(P_markup("Declarations", S["h1"]))
    for env, label in DECL_TITLES.items():
        md = re.search(r"\\begin\{" + env + r"\}(.*?)\\end\{" + env + r"\}", src, re.S)
        if md:
            flow.append(P_markup("<b>%s</b>" % esc(label), S["h2"]))
            flow.append(P(strip_comments(md.group(1)).strip(), S["body"]))

    # referencias
    flow.append(P_markup("References", S["h1"]))
    for ref in REFERENCES:
        flow.append(P_markup(esc(ref), S["ref"]))

    doc = SimpleDocTemplate(
        OUT, pagesize=A4,
        leftMargin=2 * cm, rightMargin=2 * cm,
        topMargin=2 * cm, bottomMargin=2 * cm,
        title=title, author="; ".join(plain(a) for a in authors))
    doc.build(flow)
    print("OK ->", OUT)


def process_body(flow, body, S):
    lines = body.split("\n")
    mode = "normal"
    tbuf, caption, cbuf, qbuf, fbuf = [], "", [], [], []
    list_mode = None
    item_n = [0]
    tcount = [0]
    fcount = [0]
    # numeracao de secoes
    sec = [0]
    sub = [0]
    subsub = [0]
    appendix = [False]
    app_letter = [0]

    def cur_sec_label():
        if appendix[0]:
            return chr(ord("A") + app_letter[0] - 1) if app_letter[0] > 0 else "A"
        return str(sec[0])

    def flush_figure():
        img, cap = None, ""
        for ln in fbuf:
            mi = re.search(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}", ln)
            if mi:
                img = mi.group(1)
            ls = ln.strip()
            if ls.startswith(r"\caption{"):
                cap, _ = first_braced(ls, ls.index("{"))
        fcount[0] += 1
        block = []
        if img:
            path = os.path.join(HERE, img)
            if os.path.exists(path):
                try:
                    iw, ih = _img_size(path)
                    maxw = min(6.3 * inch, AVAIL_W)
                    w = maxw
                    h = ih * (w / iw)
                    block.append(Image(path, width=w, height=h))
                except Exception:
                    pass
        if cap:
            block.append(P_markup("<b>Figure %d.</b> " % fcount[0] +
                                  runs_to_markup(fmt(cap)), S["caption"]))
        if block:
            flow.append(KeepTogether(block))

    def flush_table():
        rows = []
        for ln in tbuf:
            s = ln.strip()
            if not s or s.startswith(r"\hline") or s.startswith("%"):
                continue
            s = s.rstrip("\\").strip()
            rows.append([strip_multicolumn(c) for c in s.split("&")])
        if not rows:
            return
        tcount[0] += 1
        if caption:
            flow.append(P_markup("<b>Table %d.</b> " % tcount[0] +
                                 runs_to_markup(fmt(caption)), S["caption"]))
        ncol = max(len(r) for r in rows)
        data = []
        for ri, row in enumerate(rows):
            cells = []
            for ci in range(ncol):
                txt = row[ci] if ci < len(row) else ""
                st = S["cellh"] if ri == 0 else S["cell"]
                try:
                    cells.append(Paragraph(runs_to_markup(fmt(txt)), st))
                except Exception:
                    cells.append(Paragraph(esc(plain(txt)), st))
            data.append(cells)
        colw = [AVAIL_W / ncol] * ncol
        try:
            t = Table(data, colWidths=colw, repeatRows=1)
            t.setStyle(TableStyle([
                ("GRID", (0, 0), (-1, -1), 0.4, colors.grey),
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e8e8e8")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 3),
                ("RIGHTPADDING", (0, 0), (-1, -1), 3),
                ("TOPPADDING", (0, 0), (-1, -1), 2),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
            ]))
            flow.append(t)
            flow.append(Spacer(1, 6))
        except Exception:
            pass

    def flush_code():
        text = "\n".join(cbuf)
        try:
            pre = Preformatted(text, S["code"], maxLineLength=1000)
        except Exception:
            pre = Paragraph(esc(text).replace("\n", "<br/>"), S["code"])
        box = Table([[pre]], colWidths=[AVAIL_W])
        box.setStyle(TableStyle([
            ("BOX", (0, 0), (-1, -1), 0.5, colors.grey),
            ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f6f6f6")),
            ("LEFTPADDING", (0, 0), (-1, -1), 5),
            ("RIGHTPADDING", (0, 0), (-1, -1), 5),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ]))
        flow.append(box)
        flow.append(Spacer(1, 6))

    for raw in lines:
        raw = re.sub(r"(?<!\\)%.*$", "", raw)
        s = raw.strip()
        if mode == "code":
            if s.startswith(r"\end{lstlisting"):
                flush_code(); cbuf = []; mode = "normal"
            else:
                cbuf.append(raw)
            continue
        if mode == "table":
            if r"\end{tabular" in s:
                flush_table(); tbuf = []; caption = ""; mode = "normal"
            else:
                tbuf.append(raw)
            continue
        if mode == "figure":
            if r"\end{figure" in s:
                flush_figure(); fbuf = []; mode = "normal"
            else:
                fbuf.append(raw)
            continue
        if mode == "quote":
            if r"\end{quotation" in s:
                flow.append(P(" ".join(qbuf), S["quote"]))
                qbuf = []; mode = "normal"
            else:
                if s:
                    qbuf.append(s)
            continue
        # normal
        if s.startswith(r"\begin{lstlisting"):
            mode = "code"; cbuf = []; continue
        if s.startswith(r"\begin{tabular"):
            mode = "table"; tbuf = []; continue
        if s.startswith(r"\begin{quotation"):
            mode = "quote"; qbuf = []; continue
        if s.startswith(r"\begin{figure"):
            mode = "figure"; fbuf = []; continue
        if s.startswith(r"\caption{"):
            caption, _ = first_braced(s, s.index("{")); continue
        if s == r"\appendix":
            appendix[0] = True; continue
        if s.startswith(r"\begin{itemize"):
            list_mode = "bullet"; continue
        if s.startswith(r"\begin{enumerate"):
            list_mode = "number"; item_n[0] = 0; continue
        if s.startswith(r"\end{itemize}") or s.startswith(r"\end{enumerate}"):
            list_mode = None; continue
        if (not s or s.startswith(r"\label{") or s == r"\centering"
                or s.startswith(r"\hline")
                or s.startswith(r"\begin{table") or s.startswith(r"\end{table")
                or s.startswith(r"\begin{figure") or s.startswith(r"\end{figure")):
            continue
        if s.startswith(r"\section{") or s.startswith(r"\section*{"):
            c, _ = first_braced(s, s.index("{"))
            if appendix[0]:
                app_letter[0] += 1
            else:
                sec[0] += 1
            sub[0] = 0; subsub[0] = 0
            num = cur_sec_label()
            flow.append(P_markup("%s  %s" % (num, runs_to_markup(fmt(c))), S["h1"]))
            continue
        if s.startswith(r"\subsection{"):
            c, _ = first_braced(s, s.index("{"))
            sub[0] += 1; subsub[0] = 0
            num = "%s.%d" % (cur_sec_label(), sub[0])
            flow.append(P_markup("%s  %s" % (num, runs_to_markup(fmt(c))), S["h2"]))
            continue
        if s.startswith(r"\subsubsection{"):
            c, _ = first_braced(s, s.index("{"))
            subsub[0] += 1
            num = "%s.%d.%d" % (cur_sec_label(), sub[0], subsub[0])
            flow.append(P_markup("%s  %s" % (num, runs_to_markup(fmt(c))), S["h3"]))
            continue
        if s.startswith(r"\paragraph{"):
            lead, end = first_braced(s, s.index("{"))
            rest = s[end:].strip()
            markup = "<b>%s</b>" % runs_to_markup(fmt(lead))
            if rest:
                markup += " " + runs_to_markup(fmt(rest))
            flow.append(P_markup(markup, S["body"]))
            continue
        if s.startswith(r"\item"):
            content = s[len(r"\item"):].strip()
            if list_mode == "number":
                item_n[0] += 1
                bullet = "%d." % item_n[0]
            else:
                bullet = "•"
            try:
                p = Paragraph(runs_to_markup(fmt(content)), S["list"],
                              bulletText=bullet)
            except Exception:
                p = Paragraph(esc(plain(content)), S["list"], bulletText=bullet)
            flow.append(p)
            continue
        flow.append(P(s, S["body"]))


def _img_size(path):
    """Dimensoes (w,h) em px da imagem, sem PIL (le header PNG)."""
    try:
        from reportlab.lib.utils import ImageReader
        return ImageReader(path).getSize()
    except Exception:
        return (1000.0, 600.0)


if __name__ == "__main__":
    build()
