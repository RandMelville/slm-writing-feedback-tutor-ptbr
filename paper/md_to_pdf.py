"""Converte paper Markdown -> PDF via reportlab. Sem deps nativas."""
import re, sys
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, Preformatted, Image
)
from reportlab.lib.utils import ImageReader

SRC = Path(sys.argv[1] if len(sys.argv) > 1 else "paper/artigo_benchmark_slm.md")
DST = Path(sys.argv[2] if len(sys.argv) > 2 else "paper/artigo_benchmark_slm.pdf")


_ITAL = re.compile(r"(?<!\*)\*([^*\n]+?)\*(?!\*)")

def _bold_with_italic(m: re.Match) -> str:
    inner = _ITAL.sub(r"<i>\1</i>", m.group(1))
    return f"<b>{inner}</b>"

def md_inline(s: str) -> str:
    """Inline markdown -> reportlab mini-HTML: ***bold-italic***, **bold**, *italic*, `code`.

    Backticks are processed first via a placeholder so asterisks inside `code`
    are NOT interpreted as bold/italic markers.
    """
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    # Stash backtick blocks to shield their content from asterisk rules
    code_blocks: list[str] = []
    def _stash(m: re.Match) -> str:
        code_blocks.append(m.group(1))
        return f"\x00CODE{len(code_blocks)-1}\x00"
    s = re.sub(r"`([^`]+?)`", _stash, s)
    # Process asterisk-based markup now
    s = re.sub(r"\*\*\*(.+?)\*\*\*", r"<b><i>\1</i></b>", s)
    s = re.sub(r"\*\*(.+?)\*\*", _bold_with_italic, s)
    s = _ITAL.sub(r"<i>\1</i>", s)
    # Restore code blocks
    def _restore(m: re.Match) -> str:
        return f'<font name="Courier" size="9">{code_blocks[int(m.group(1))]}</font>'
    s = re.sub(r"\x00CODE(\d+)\x00", _restore, s)
    # Links last
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<link href="\2" color="blue">\1</link>', s)
    return s


styles = getSampleStyleSheet()
S = {
    "title":   ParagraphStyle("title",   parent=styles["Title"],   fontSize=14, leading=18, alignment=TA_CENTER, spaceAfter=12, fontName="Helvetica-Bold"),
    "subtitle":ParagraphStyle("subtitle",parent=styles["Title"],   fontSize=11, leading=15, alignment=TA_CENTER, spaceAfter=12, fontName="Helvetica-Oblique", textColor=colors.grey),
    "author":  ParagraphStyle("author",  parent=styles["Normal"],  fontSize=10, leading=14, alignment=TA_CENTER, spaceAfter=14),
    "h1":      ParagraphStyle("h1",      parent=styles["Heading1"],fontSize=12, leading=15, spaceBefore=14, spaceAfter=8,  fontName="Helvetica-Bold"),
    "h2":      ParagraphStyle("h2",      parent=styles["Heading2"],fontSize=11, leading=14, spaceBefore=10, spaceAfter=6,  fontName="Helvetica-Bold"),
    "h3":      ParagraphStyle("h3",      parent=styles["Heading3"],fontSize=10, leading=13, spaceBefore=8,  spaceAfter=4,  fontName="Helvetica-Bold"),
    "body":    ParagraphStyle("body",    parent=styles["Normal"],  fontSize=10, leading=14, alignment=TA_JUSTIFY, spaceAfter=6, firstLineIndent=0),
    "abstract":ParagraphStyle("abstract",parent=styles["Normal"],  fontSize=9.5, leading=13, alignment=TA_JUSTIFY, spaceAfter=6, leftIndent=10, rightIndent=10),
    "kw":      ParagraphStyle("kw",      parent=styles["Normal"],  fontSize=9.5, leading=13, alignment=TA_JUSTIFY, spaceAfter=10, leftIndent=10, rightIndent=10, fontName="Helvetica-Oblique"),
    "caption": ParagraphStyle("caption", parent=styles["Normal"],  fontSize=9,  leading=12, alignment=TA_CENTER, spaceBefore=4, spaceAfter=6, fontName="Helvetica-Bold"),
    "ref":     ParagraphStyle("ref",     parent=styles["Normal"],  fontSize=9,  leading=12, alignment=TA_JUSTIFY, spaceAfter=5, leftIndent=14, firstLineIndent=-14),
    "code":    ParagraphStyle("code",    parent=styles["Code"],    fontSize=8,  leading=10, alignment=TA_LEFT, spaceBefore=4, spaceAfter=8, leftIndent=10, rightIndent=10, fontName="Courier", textColor=colors.HexColor("#1a1a1a"), backColor=colors.HexColor("#f3f3f3"), borderColor=colors.HexColor("#d0d0d0"), borderWidth=0.4, borderPadding=4),
    "quote":   ParagraphStyle("quote",   parent=styles["Normal"],  fontSize=9.5, leading=13, alignment=TA_JUSTIFY, spaceAfter=8, leftIndent=18, rightIndent=18, fontName="Helvetica-Oblique", textColor=colors.HexColor("#333333")),
}


def parse_table(lines: list[str], start: int) -> tuple[Table, int]:
    """Lê tabela markdown e devolve (Table, índice da próxima linha)."""
    rows = []
    i = start
    while i < len(lines) and lines[i].startswith("|"):
        cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
        rows.append(cells)
        i += 1
    if len(rows) >= 2 and all(re.match(r":?-+:?$", c) for c in rows[1]):
        rows = [rows[0]] + rows[2:]
    data = [[Paragraph(md_inline(c), S["body"]) for c in r] for r in rows]
    n_cols = len(data[0])
    col_w = [16*cm / n_cols] * n_cols
    if n_cols >= 5:
        col_w = [4.5*cm] + [(16-4.5)*cm/(n_cols-1)] * (n_cols-1)
    t = Table(data, colWidths=col_w, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#e8e8e8")),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("GRID", (0,0), (-1,-1), 0.4, colors.grey),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 4),
        ("RIGHTPADDING", (0,0), (-1,-1), 4),
        ("TOPPADDING", (0,0), (-1,-1), 3),
        ("BOTTOMPADDING", (0,0), (-1,-1), 3),
    ]))
    return t, i


def build(md_text: str) -> list:
    """Markdown -> lista de flowables."""
    lines = md_text.split("\n")
    flow = []
    i = 0
    n_title_lines = 0
    is_references = False
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1; continue

        # Horizontal rule
        if stripped == "---":
            flow.append(Spacer(1, 0.2*cm))
            i += 1; continue

        # Imagem ![caption](path) — escala para a largura do conteudo
        m_img = re.match(r"!\[([^\]]*)\]\(([^)]+)\)", stripped)
        if m_img:
            cap, path = m_img.group(1), m_img.group(2)
            img_path = (SRC.parent / path).resolve() if not Path(path).is_absolute() else Path(path)
            if img_path.exists():
                iw, ih = ImageReader(str(img_path)).getSize()
                max_w = 16 * cm
                w = min(max_w, iw)
                h = w * ih / iw
                blk = [Spacer(1, 0.2*cm), Image(str(img_path), width=w, height=h)]
                if cap:
                    blk.append(Paragraph(md_inline(cap), S["caption"]))
                blk.append(Spacer(1, 0.2*cm))
                flow.append(KeepTogether(blk))
            i += 1; continue

        # Fenced code block ``` ... ```
        if stripped.startswith("```"):
            i += 1
            code_lines = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            if i < len(lines):
                i += 1  # consome o ``` de fechamento
            code_text = "\n".join(code_lines)
            flow.append(Preformatted(code_text, S["code"]))
            continue

        # Blockquote
        if stripped.startswith("> "):
            quote_lines = []
            while i < len(lines) and lines[i].strip().startswith("> "):
                quote_lines.append(lines[i].strip()[2:])
                i += 1
            flow.append(Paragraph(md_inline(" ".join(quote_lines)), S["quote"]))
            continue

        # Heading 1 (título do paper)
        if stripped.startswith("# "):
            n_title_lines += 1
            style = S["title"] if n_title_lines == 1 else S["subtitle"]
            flow.append(Paragraph(md_inline(stripped[2:]), style))
            i += 1; continue

        # Heading 2 (seções)
        if stripped.startswith("## "):
            text = stripped[3:]
            is_references = text.lower().startswith("referências") or text.lower().startswith("referencias")
            flow.append(Paragraph(md_inline(text), S["h1"]))
            i += 1; continue

        # Heading 3 (subseções)
        if stripped.startswith("### "):
            flow.append(Paragraph(md_inline(stripped[4:]), S["h2"]))
            i += 1; continue

        # Heading 4
        if stripped.startswith("#### "):
            flow.append(Paragraph(md_inline(stripped[5:]), S["h3"]))
            i += 1; continue

        # Tabela
        if stripped.startswith("|"):
            tbl, i = parse_table(lines, i)
            flow.append(tbl)
            flow.append(Spacer(1, 0.15*cm))
            continue

        # Caption de tabela (negrito Tabela X.)
        if stripped.startswith("**Tabela ") or stripped.startswith("**Figura "):
            flow.append(Paragraph(md_inline(stripped), S["caption"]))
            i += 1; continue

        # Lista com hífen — concatena em parágrafo único com bullets
        if stripped.startswith("- "):
            items = []
            while i < len(lines) and lines[i].strip().startswith("- "):
                items.append(lines[i].strip()[2:])
                i += 1
            for item in items:
                flow.append(Paragraph(f"• {md_inline(item)}", S["body"]))
            continue

        # Email/affiliation simples
        if stripped.startswith("**") and stripped.endswith("**") and len(stripped) < 80:
            flow.append(Paragraph(md_inline(stripped), S["author"]))
            i += 1; continue

        # Parágrafo (acumula linhas até linha vazia)
        para_lines = []
        while i < len(lines) and lines[i].strip() and not lines[i].strip().startswith(("#", "|", "- ", "---")):
            para_lines.append(lines[i].strip())
            i += 1
        text = " ".join(para_lines)
        style = S["ref"] if is_references else S["body"]
        # Resumo / Abstract / Palavras-chave: heurística leve
        if text.startswith("**Palavras-chave:**") or text.startswith("**Keywords:**"):
            style = S["kw"]
        flow.append(Paragraph(md_inline(text), style))

    return flow


def main() -> None:
    md = SRC.read_text(encoding="utf-8")
    doc = SimpleDocTemplate(
        str(DST), pagesize=A4,
        leftMargin=2.5*cm, rightMargin=2.5*cm,
        topMargin=2*cm, bottomMargin=2*cm,
        title="Avaliação Diagnóstica de SLMs para Tutoria de Feedback de Escrita Offline em PT-BR",
        author="Randerson Melville Rebouças",
    )
    flow = build(md)
    doc.build(flow)
    size_kb = DST.stat().st_size / 1024
    print(f"{DST}  ({size_kb:.0f} KB)")


if __name__ == "__main__":
    main()
