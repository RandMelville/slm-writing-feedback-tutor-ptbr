"""
Verifica, por programa, a exigencia do parecer de 10/08/2026: nenhum exemplo entregue aos novos
codificadores pode sair das 39 devolutivas que eles vao recodificar.

Ler os dois documentos e confiar na memoria nao serve. O script extrai todo trecho citado do
PROTOCOLO_v04.md, do ANEXO_CALIBRACAO.md e do GUIA_PROFESSOR.md, que e o documento que vai
de fato as maos dos codificadores (texto entre aspas e linhas de citacao), normaliza
acentuacao, caixa e pontuacao, e procura cada janela de 6 palavras dentro do corpus das 39
devolutivas. Qualquer coincidencia e falha.

O corpus humano de referencia (65 devolutivas de professores) e fonte permitida, entao
coincidencia com ele e apenas informada.

Uso: python3 data/codificacao_v04/verifica_exemplos.py
Saida: codigo 0 e "nenhum exemplo vem das 39" quando esta limpo; codigo 1 e a lista de trechos
em caso contrario.
"""
import csv
import json
import re
import sys
import unicodedata
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ROOT = AQUI.parents[1]
DOCS = [AQUI / "PROTOCOLO_v05.md", AQUI / "ANEXO_ALINHAMENTO_v05.md", AQUI / "GUIA_PROFESSOR_v05.md"]
PACOTE = ROOT / "data" / "segunda_codificacao_cega" / "codificacao_cega_v02.csv"
HUMANO = ROOT / "data" / "baseline_humano" / "respostas_professores.jsonl"

JANELA = 6  # palavras


def normalizar(texto):
    texto = unicodedata.normalize("NFKD", texto.lower())
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    return " ".join(re.sub(r"[^a-z0-9 ]+", " ", texto).split())


def trechos_citados(caminho):
    """Todo texto entre aspas (retas ou curvas) e toda linha de citacao markdown."""
    bruto = caminho.read_text(encoding="utf-8")
    achados = []
    for padrao in [r'"([^"\n]{10,})"', r'“([^”\n]{10,})”', r"'([^'\n]{10,})'"]:
        achados += re.findall(padrao, bruto)
    for linha in bruto.splitlines():
        if linha.lstrip().startswith(">"):
            achados.append(linha.lstrip("> ").strip())
    return [t for t in achados if len(normalizar(t).split()) >= JANELA]


def corpus_39():
    with PACOTE.open(encoding="utf-8") as fh:
        linhas = list(csv.DictReader(fh))
    assert len(linhas) == 39, f"esperado 39 devolutivas, obtido {len(linhas)}"
    return normalizar(" || ".join(l["Devolutiva"] for l in linhas))


def corpus_humano():
    if not HUMANO.exists():
        return ""
    devolutivas = []
    with HUMANO.open(encoding="utf-8") as fh:
        for linha in fh:
            if linha.strip():
                devolutivas.append(json.loads(linha)["devolutiva"])
    return normalizar(" || ".join(devolutivas))


def janelas(texto_normalizado):
    palavras = texto_normalizado.split()
    return {" ".join(palavras[i:i + JANELA]) for i in range(len(palavras) - JANELA + 1)}


def main():
    alvo = corpus_39()
    referencia = corpus_humano()

    falhas, vindos_do_humano, total = [], 0, 0
    for doc in DOCS:
        for trecho in trechos_citados(doc):
            total += 1
            js = janelas(normalizar(trecho))
            if any(j in alvo for j in js):
                falhas.append((doc.name, trecho))
            elif referencia and any(j in referencia for j in js):
                vindos_do_humano += 1

    print(f"trechos citados verificados: {total}")
    print(f"trechos com origem no corpus humano de referencia (permitido): {vindos_do_humano}")

    if falhas:
        print("\nFALHA: os trechos abaixo aparecem nas 39 devolutivas a codificar\n")
        for nome, trecho in falhas:
            print(f"  [{nome}] {trecho[:120]}")
        return 1

    print("nenhum exemplo vem das 39")
    return 0


if __name__ == "__main__":
    sys.exit(main())
