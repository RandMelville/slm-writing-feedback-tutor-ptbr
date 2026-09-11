"""Monta o documento de referência do pandoc usado em md_to_docx.py.

O reference.docx padrão do pandoc não justifica o texto e não põe borda nenhuma
nas tabelas: elas saem como colunas invisíveis. Este script parte do padrão e
ajusta só o que interessa para um documento profissional de leitura:

  - corpo em Calibri 11pt, justificado, com entrelinha 1,15;
  - tabela com borda em todas as células, cabeçalho em cinza claro e negrito;
  - títulos em Calibri, escala moderada, sem o azul do tema do Word;
  - citação recuada em itálico e cinza, para os trechos de parecer.

Uso: python3 paper/build_reference_docx.py
Saída: paper/reference.docx
"""
import re
import shutil
import subprocess
import zipfile
from pathlib import Path

AQUI = Path(__file__).resolve().parent
DESTINO = AQUI / "reference.docx"

TINTA = "1A1A19"
CINZA = "5C5C57"
BORDA = "9A9A95"
FUNDO_CABECALHO = "EFEEEA"


def borda(tipo):
    return f'<w:{tipo} w:val="single" w:sz="4" w:space="0" w:color="{BORDA}" />'


TBL_BORDAS = ("<w:tblBorders>" + "".join(borda(t) for t in
              ("top", "left", "bottom", "right", "insideH", "insideV")) + "</w:tblBorders>")


def troca_estilo(styles: str, style_id: str, novo: str) -> str:
    padrao = re.compile(r'<w:style [^>]*w:styleId="%s"[ >].*?</w:style>' % style_id, re.S)
    assert padrao.search(styles), f"estilo {style_id} não encontrado"
    return padrao.sub(novo, styles, count=1)


def main() -> None:
    base = AQUI / "_ref_pandoc.docx"
    with base.open("wb") as fh:
        subprocess.run(["pandoc", "--print-default-data-file", "reference.docx"],
                       stdout=fh, check=True)

    z = zipfile.ZipFile(base)
    conteudo = {n: z.read(n) for n in z.namelist()}
    z.close()
    styles = conteudo["word/styles.xml"].decode("utf-8")

    # corpo: Calibri 11pt, justificado, entrelinha 1,15
    styles = troca_estilo(styles, "Normal", (
        '<w:style w:type="paragraph" w:default="1" w:styleId="Normal">'
        '<w:name w:val="Normal" /><w:qFormat />'
        '<w:pPr><w:jc w:val="both" /><w:spacing w:line="264" w:lineRule="auto" /></w:pPr>'
        f'<w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:cs="Calibri" />'
        f'<w:color w:val="{TINTA}" /><w:sz w:val="22" /><w:szCs w:val="22" /></w:rPr>'
        '</w:style>'))

    # tabela: borda em todas as células e margem interna legível
    styles = troca_estilo(styles, "Table", (
        '<w:style w:type="table" w:default="1" w:styleId="Table">'
        '<w:name w:val="Table" /><w:basedOn w:val="TableNormal" /><w:qFormat />'
        '<w:tblPr><w:tblInd w:w="0" w:type="dxa" />' + TBL_BORDAS +
        '<w:tblCellMar>'
        '<w:top w:w="60" w:type="dxa" /><w:left w:w="108" w:type="dxa" />'
        '<w:bottom w:w="60" w:type="dxa" /><w:right w:w="108" w:type="dxa" />'
        '</w:tblCellMar></w:tblPr>'
        # o cabeçalho do pandoc é a primeira linha: fundo claro e negrito
        '<w:tblStylePr w:type="firstRow"><w:rPr><w:b /></w:rPr>'
        f'<w:tcPr><w:shd w:val="clear" w:color="auto" w:fill="{FUNDO_CABECALHO}" /></w:tcPr>'
        '</w:tblStylePr>'
        '</w:style>'))

    # célula de tabela não justifica: texto curto justificado abre buracos
    styles = troca_estilo(styles, "Compact", (
        '<w:style w:type="paragraph" w:customStyle="1" w:styleId="Compact">'
        '<w:name w:val="Compact" /><w:basedOn w:val="BodyText" /><w:qFormat />'
        '<w:pPr><w:jc w:val="left" /><w:spacing w:before="36" w:after="36" /></w:pPr>'
        '</w:style>'))

    # citação de parecer: recuada, itálica, cinza
    styles = troca_estilo(styles, "BlockText", (
        '<w:style w:type="paragraph" w:styleId="BlockText">'
        '<w:name w:val="Block Text" /><w:basedOn w:val="BodyText" />'
        '<w:next w:val="BodyText" /><w:qFormat />'
        '<w:pPr><w:spacing w:before="120" w:after="120" />'
        '<w:ind w:firstLine="0" w:left="480" w:right="480" /><w:jc w:val="left" /></w:pPr>'
        f'<w:rPr><w:i /><w:color w:val="{CINZA}" /></w:rPr>'
        '</w:style>'))

    # títulos: sem o azul do tema, tamanhos moderados
    for sid, nome, tamanho, antes in (("Heading1", "heading 1", 30, 320),
                                      ("Heading2", "heading 2", 24, 280),
                                      ("Heading3", "heading 3", 22, 240)):
        styles = troca_estilo(styles, sid, (
            f'<w:style w:type="paragraph" w:styleId="{sid}">'
            f'<w:name w:val="{nome}" /><w:basedOn w:val="Normal" />'
            f'<w:next w:val="BodyText" /><w:qFormat />'
            f'<w:pPr><w:keepNext /><w:jc w:val="left" />'
            f'<w:spacing w:before="{antes}" w:after="120" /></w:pPr>'
            f'<w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" /><w:b />'
            f'<w:color w:val="{TINTA}" /><w:sz w:val="{tamanho}" /></w:rPr>'
            '</w:style>'))

    conteudo["word/styles.xml"] = styles.encode("utf-8")
    with zipfile.ZipFile(DESTINO, "w", zipfile.ZIP_DEFLATED) as saida:
        for nome, dados in conteudo.items():
            saida.writestr(nome, dados)
    base.unlink()
    print(f"{DESTINO.relative_to(AQUI.parent)}  ({DESTINO.stat().st_size / 1024:.0f} KB)")


if __name__ == "__main__":
    main()
