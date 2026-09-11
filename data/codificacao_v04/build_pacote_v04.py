"""
Monta o pacote de anotacao da rodada final (protocolo v0.4), para DOIS codificadores.

Regra do parecer de 10/08/2026: o kappa sai exclusivamente entre as duas codificacoes novas.
Para isso os dois recebem exatamente o mesmo material e os mesmos identificadores R01-R39, o
que permite alinhar linha a linha na hora do calculo.

Os IDs e a ordem embaralhada sao os mesmos de julho (semente 20260727, em
data/segunda_codificacao_cega/build_pacote_cego.py). Nao e comodismo: mantem as unidades
alinhadas com a codificacao n.4, que sai do kappa mas continua servindo de comparacao
exploratoria depois que as duas novas estiverem preservadas.

O script reconstroi as 39 devolutivas a partir da fonte (data/results/round_1_main_models.json)
reaproveitando as funcoes do pacote de julho, e so entao afirma, por assert, que o texto e
identico ao que foi entregue naquela rodada. Se um dia a fonte mudar, o script quebra em vez de
gerar um pacote silenciosamente diferente.

Saidas (o mesmo conteudo nos dois arquivos, um por codificador):
  data/codificacao_v04/pacote_v04_codificador_A.csv
  data/codificacao_v04/pacote_v04_codificador_B.csv

A chave de decegamento continua sendo data/segunda_codificacao_cega/chave_cega.csv e NAO vai
com o pacote.

Uso: python3 data/codificacao_v04/build_pacote_v04.py
"""
import csv
import importlib.util
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ROOT = AQUI.parents[1]
PACOTE_JULHO = ROOT / "data" / "segunda_codificacao_cega" / "codificacao_cega_v02.csv"
BUILD_JULHO = ROOT / "data" / "segunda_codificacao_cega" / "build_pacote_cego.py"

FM_COLS = [f"FM0{i}" for i in range(1, 9)]
CAMPOS = ["ID", "Texto do aluno", "Devolutiva"] + FM_COLS + ["MTL", "Observações"]
CODIFICADORES = ["A", "B"]


def carregar_modulo_julho():
    """Importa o gerador de julho pelo caminho, para reaproveitar as funcoes de leitura."""
    spec = importlib.util.spec_from_file_location("build_pacote_cego", BUILD_JULHO)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def reconstruir_da_fonte(mod):
    """(cenario, rep) -> (texto do aluno, devolutiva), direto do JSON do benchmark."""
    textos = mod.carregar_cenarios()
    itens = {}
    for it in mod.carregar_modelo():
        itens[(it["cenario"], it["rep"])] = (textos[it["cenario"]], it["devolutiva"])
    return itens


def ler_pacote_julho():
    with PACOTE_JULHO.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def ler_chave():
    caminho = ROOT / "data" / "segunda_codificacao_cega" / "chave_cega.csv"
    with caminho.open(encoding="utf-8") as fh:
        return {r["ID"]: (int(r["cenario"]), int(r["rep"])) for r in csv.DictReader(fh)}


def main():
    mod = carregar_modulo_julho()
    fonte = reconstruir_da_fonte(mod)
    julho = ler_pacote_julho()
    chave = ler_chave()

    assert len(julho) == 39, f"esperado 39 linhas no pacote de julho, obtido {len(julho)}"

    linhas = []
    for linha in julho:
        rid = linha["ID"]
        texto_fonte, devolutiva_fonte = fonte[chave[rid]]
        assert linha["Devolutiva"] == devolutiva_fonte, f"{rid}: devolutiva divergente da fonte"
        assert linha["Texto do aluno"] == texto_fonte, f"{rid}: texto do aluno divergente da fonte"
        linhas.append({
            "ID": rid,
            "Texto do aluno": texto_fonte,
            "Devolutiva": devolutiva_fonte,
            **{c: "" for c in FM_COLS},
            "MTL": "",
            "Observações": "",
        })

    for cod in CODIFICADORES:
        saida = AQUI / f"pacote_v04_codificador_{cod}.csv"
        with saida.open("w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=CAMPOS)
            w.writeheader()
            w.writerows(linhas)
        print(f"{saida.name}: {len(linhas)} devolutivas, {len(linhas) * 9} decisoes a preencher")

    print("IDs identicos aos de julho e devolutivas conferidas contra a fonte: ok")


if __name__ == "__main__":
    main()
