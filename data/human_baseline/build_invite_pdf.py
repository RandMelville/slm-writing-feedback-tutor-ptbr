#!/usr/bin/env python3
"""
build_invite_pdf.py — gera o convite formatado em PDF (com logo UFRGS/PPGIE e o
link do Google Form) a partir de carta_convite.md.

Uso:
    python3 build_invite_pdf.py --form-url "https://forms.gle/XXXX" \
        --logo ufrgs_ppgie_logo.png

Argumentos:
    --form-url   link público do Form (saída do build_form.gs). Obrigatório.
    --logo       caminho do logo (PNG/JPG). Opcional: se ausente, usa um
                 placeholder de texto e avisa para você inserir o logo oficial.
    --out        caminho de saída (padrão: Convite_Baseline_PPGIE.pdf).

Requer reportlab (já usado por paper/md_to_pdf.py). Se faltar:
    pip install reportlab
"""
import argparse
import html
import re
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, HRFlowable,
)

HERE = Path(__file__).resolve().parent
AZUL = HexColor("#1b3a6b")  # azul institucional sóbrio


def inline(text):
    """Escapa XML e converte **negrito** -> <b> para o Paragraph do reportlab."""
    text = html.escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    return text


def build_styles():
    ss = getSampleStyleSheet()
    return {
        "title": ParagraphStyle("title", parent=ss["Title"], fontSize=16,
                                textColor=AZUL, spaceAfter=4, alignment=TA_CENTER),
        "sub": ParagraphStyle("sub", parent=ss["Normal"], fontSize=9.5,
                              textColor=HexColor("#555555"), alignment=TA_CENTER,
                              spaceAfter=10),
        "h2": ParagraphStyle("h2", parent=ss["Heading2"], fontSize=11.5,
                             textColor=AZUL, spaceBefore=10, spaceAfter=4),
        "body": ParagraphStyle("body", parent=ss["Normal"], fontSize=10.3,
                               leading=15, alignment=TA_JUSTIFY, spaceAfter=6),
        "bullet": ParagraphStyle("bullet", parent=ss["Normal"], fontSize=10.3,
                                 leading=15, leftIndent=14, spaceAfter=3),
        "cta": ParagraphStyle("cta", parent=ss["Normal"], fontSize=11.5,
                              textColor=AZUL, alignment=TA_CENTER, leading=16),
    }


def render_md(md_text, styles):
    """Converte carta_convite.md em flowables, pulando o H1 (título virá no topo).

    Linhas de prosa consecutivas (markdown com quebra manual) são unidas num único
    parágrafo justificado; só blank lines, títulos e itens de lista separam blocos.
    """
    flow = []
    buf = []

    def flush():
        if buf:
            flow.append(Paragraph(inline(" ".join(buf)), styles["body"]))
            buf.clear()

    for raw in md_text.splitlines():
        line = raw.rstrip()
        s = line.strip()
        if not s:
            flush()
            continue
        if line.startswith("# "):
            flush()
            continue  # título tratado à parte
        if line.startswith("## "):
            flush()
            flow.append(Paragraph(inline(line[3:]), styles["h2"]))
        elif re.match(r"^\s*[-*]\s+", line):
            flush()
            flow.append(Paragraph("• " + inline(re.sub(r"^\s*[-*]\s+", "", line)),
                                  styles["bullet"]))
        elif re.match(r"^\s*\d+\.\s+", line):
            flush()
            flow.append(Paragraph(inline(s), styles["body"]))
        else:
            buf.append(s)
    flush()
    return flow


def cta_box(form_url, styles):
    """Caixa de chamada com o link do formulário."""
    p = Paragraph(
        f"<b>Para participar, acesse o formulário (~30 min):</b><br/>"
        f'<font color="#1b3a6b">{html.escape(form_url)}</font>', styles["cta"])
    t = Table([[p]], colWidths=[16 * cm])
    t.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 1, AZUL),
        ("BACKGROUND", (0, 0), (-1, -1), HexColor("#eef2f8")),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
    ]))
    return t


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--form-url", required=True, help="link público do Google Form")
    ap.add_argument("--logo-ufrgs", default=str(HERE / "logo-ufrgs.png"))
    ap.add_argument("--logo-ppgie", default=str(HERE / "ppgie-logo.png"))
    ap.add_argument("--out", default=str(HERE / "Convite_Baseline_PPGIE.pdf"))
    args = ap.parse_args()

    styles = build_styles()
    story = []

    # Logos no topo: UFRGS à esquerda, PPGIE à direita.
    def scaled_logo(path, max_h=1.7 * cm):
        img = Image(str(path))
        ratio = max_h / img.imageHeight
        img.drawHeight = max_h
        img.drawWidth = img.imageWidth * ratio
        return img

    ufrgs, ppgie = Path(args.logo_ufrgs), Path(args.logo_ppgie)
    if ufrgs.exists() and ppgie.exists():
        left, right = scaled_logo(ufrgs), scaled_logo(ppgie)
        t = Table([[left, right]], colWidths=[8 * cm, 8 * cm])
        t.setStyle(TableStyle([
            ("ALIGN", (0, 0), (0, 0), "LEFT"),
            ("ALIGN", (1, 0), (1, 0), "RIGHT"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ]))
        story += [t, Spacer(1, 10)]
    elif ufrgs.exists() or ppgie.exists():
        one = scaled_logo(ufrgs if ufrgs.exists() else ppgie, 2.0 * cm)
        one.hAlign = "CENTER"
        story += [one, Spacer(1, 10)]
    else:
        print(f"[aviso] logos não encontrados ({ufrgs.name}, {ppgie.name}) — placeholder.")
        story.append(Paragraph("[ logos UFRGS · PPGIE ]", styles["sub"]))

    story.append(Paragraph(
        "Universidade Federal do Rio Grande do Sul", styles["sub"]))
    story.append(Paragraph(
        "Programa de Pós-Graduação em Informática na Educação (PPGIE)", styles["sub"]))
    story.append(HRFlowable(width="100%", thickness=1, color=AZUL, spaceAfter=12))

    story.append(Paragraph("Convite para colaboração como referência especializada",
                           styles["title"]))
    story.append(Spacer(1, 10))

    story.append(cta_box(args.form_url, styles))
    story.append(Spacer(1, 12))

    carta = (HERE / "carta_convite.md").read_text(encoding="utf-8")
    story += render_md(carta, styles)

    doc = SimpleDocTemplate(args.out, pagesize=A4,
                            leftMargin=2.3 * cm, rightMargin=2.3 * cm,
                            topMargin=1.8 * cm, bottomMargin=1.8 * cm,
                            title="Convite — Baseline PPGIE/UFRGS")
    doc.build(story)
    print(f"[ok] PDF gerado em {args.out}")


if __name__ == "__main__":
    main()
