"""Convert paper Markdown -> DOCX via Python markdown + macOS textutil.

Pipeline:
  1) markdown -> HTML (with tables, fenced code, footnotes extensions)
  2) HTML -> DOCX (via macOS native `textutil`)

Designed for advisor review in Microsoft Word — preserves headings, tables,
code blocks, italics/bold, and footnotes. Math and complex layouts are not
preserved at publication quality, but readability is.
"""
import shutil, subprocess, sys, tempfile
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
SRC = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "paper" / "artigo_benchmark_slm.md"
DST = Path(sys.argv[2]) if len(sys.argv) > 2 else SRC.with_suffix(".docx")


# Os tamanhos do CSS ja vem divididos por 4/3: o textutil multiplica os pt por
# esse fator ao converter para .docx, e sem isso o corpo saia a 14,5pt.
CSS = """
<style>
  body { font-family: 'Calibri', 'Helvetica', sans-serif; font-size: 8.25pt;
         line-height: 1.4; max-width: 720px; margin: 2em auto; color: #222; }
  h1 { font-size: 13.5pt; margin-top: 1.6em; color: #1a1a1a; }
  h2 { font-size: 10.5pt; margin-top: 1.4em; color: #1a1a1a; border-bottom: 1px solid #ccc; padding-bottom: 0.2em; }
  h3 { font-size: 9pt; margin-top: 1.2em; color: #333; }
  h4 { font-size: 8.25pt; font-weight: bold; margin-top: 1em; }
  p  { text-align: justify; margin: 0.6em 0; }
  code { font-family: 'Consolas', 'Courier New', monospace; font-size: 7.1pt;
         background: #f3f3f3; padding: 1px 4px; border-radius: 2px; }
  pre  { background: #f3f3f3; padding: 8px; border: 1px solid #ddd;
         border-radius: 3px; overflow-x: auto; font-size: 6.75pt; }
  pre code { background: none; padding: 0; }
  blockquote { border-left: 3px solid #888; padding-left: 12px; margin-left: 8px;
               color: #444; font-style: italic; }
  table { border-collapse: collapse; margin: 0.8em 0; width: 100%; font-size: 7.5pt; }
  th, td { border: 1px solid #888; padding: 4px 8px; vertical-align: top; }
  th { background: #e8e8e8; font-weight: bold; text-align: left; }
  hr { border: none; border-top: 1px solid #ccc; margin: 1.4em 0; }
  strong { font-weight: bold; }
  em { font-style: italic; }
  a  { color: #0645ad; text-decoration: underline; }
</style>
"""


def md_to_html(md_text: str) -> str:
    body = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "footnotes", "sane_lists"],
    )
    return f"<!DOCTYPE html><html><head><meta charset='utf-8'>{CSS}</head><body>{body}</body></html>"


def html_to_docx(html_path: Path, docx_path: Path) -> None:
    subprocess.run(
        ["textutil", "-convert", "docx", str(html_path), "-output", str(docx_path)],
        check=True,
    )


def pandoc_docx(src: Path, dst: Path) -> bool:
    """Converte com pandoc, quando disponivel. Preferido porque o caminho por
    textutil descarta a estrutura das tabelas: as celulas saem como texto corrido,
    sem linha nem coluna. Devolve False se o pandoc nao estiver instalado."""
    if not shutil.which("pandoc"):
        return False
    cmd = ["pandoc", str(src), "-o", str(dst), "--standalone"]
    referencia = Path(__file__).resolve().parent / "reference.docx"
    if referencia.exists():
        # Sem isso o pandoc usa o reference.docx dele, que nao justifica o texto e
        # deixa as tabelas sem borda nenhuma. Gerado por build_reference_docx.py.
        cmd += ["--reference-doc", str(referencia)]
    subprocess.run(cmd, check=True)
    return True


def main() -> None:
    if pandoc_docx(SRC, DST):
        print(f"{DST}  ({DST.stat().st_size / 1024:.0f} KB, via pandoc)")
        return
    md = SRC.read_text(encoding="utf-8")
    html = md_to_html(md)
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(html)
        tmp_html = Path(f.name)
    try:
        html_to_docx(tmp_html, DST)
    finally:
        tmp_html.unlink(missing_ok=True)
    size_kb = DST.stat().st_size / 1024
    print(f"{DST}  ({size_kb:.0f} KB)")


if __name__ == "__main__":
    main()
