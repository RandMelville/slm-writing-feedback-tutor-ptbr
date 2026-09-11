"""Análise pré-registrada da 2ª codificação cega (39 saídas do qwen2.5:3b-instruct).

Executa o que foi fixado em data/segunda_codificacao_cega/PRE-REGISTRO_analise.md
ANTES de a anotação existir:

  (A) Confiabilidade FM01-FM08: κ de Cohen entre anotador 1 (codificação embutida em
      analises/fm_coding_model.py, via analises/codificacao_fm_modelo.csv) e anotador 2
      (passada cega do Marcelo, planilha consolidada).
  (B) Validade de construto da métrica da RQ2: κ entre a régua lexical
      (src/metalinguistic_adherence.py) e a coluna MTL do julgamento especialista.

Para cada categoria reporta: κ, concordância bruta, prevalência de cada anotador,
PABAK (Byrt et al., 1993) e a banda de Landis & Koch (1977). Nenhuma categoria é
omitida, conforme §2 do pré-registro.

Uso: python3 analises/kappa_2a_codificacao.py
"""
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
import metalinguistic_adherence as mla  # noqa: E402

XLSX = ROOT / "codificacao_cega_QWEN_marcelo_consolidada_por_cenario.xlsx"
CHAVE = ROOT / "data" / "segunda_codificacao_cega" / "chave_cega.csv"
COD1 = ROOT / "analises" / "codificacao_fm_modelo.csv"
FMS = [f"FM{i:02d}" for i in range(1, 9)]


def landis_koch(k):
    if k is None:
        return "indefinido (marginais degenerados)"
    for limite, rotulo in [(0.0, "poor"), (0.20, "slight"), (0.40, "fair"),
                           (0.60, "moderate"), (0.80, "substantial")]:
        if k <= limite:
            return rotulo if limite == 0.0 else rotulo
    return "almost perfect"


def banda(k):
    if k is None:
        return "indefinido"
    if k < 0.00:
        return "poor"
    if k <= 0.20:
        return "slight"
    if k <= 0.40:
        return "fair"
    if k <= 0.60:
        return "moderate"
    if k <= 0.80:
        return "substantial"
    return "almost perfect"


def kappa_binario(a, b):
    """κ de Cohen para duas listas binárias pareadas. None se pe == 1 (degenerado)."""
    n = len(a)
    po = sum(1 for x, y in zip(a, b) if x == y) / n
    pa1, pb1 = sum(a) / n, sum(b) / n
    pe = pa1 * pb1 + (1 - pa1) * (1 - pb1)
    if abs(1 - pe) < 1e-12:
        return None, po, pa1, pb1
    return (po - pe) / (1 - pe), po, pa1, pb1


def carregar():
    cod2 = pd.read_excel(XLSX, sheet_name="Codificação")
    chave = pd.read_csv(CHAVE)
    cod2 = cod2.merge(chave[["ID", "cenario", "rep"]], on="ID", how="left")
    assert cod2["cenario"].notna().all(), "ID sem correspondência na chave cega"

    cod1 = pd.read_csv(COD1)
    df = cod1.merge(cod2, on=["cenario", "rep"], suffixes=("_a1", "_a2"), how="inner")
    assert len(df) == 39, f"esperado 39 pares, obtido {len(df)}"
    return df


def regua_lexical():
    """Flag binária da régua lexical de Koch, por (cenario, rep)."""
    recs = mla.load_records("qwen2.5:3b-instruct", "all")
    return {(r["cenario"], r["rep"]): int(r["adere"]) for r in mla.score(recs)}


def linha(nome, a, b, rotulo_a="anot.1", rotulo_b="anot.2"):
    k, po, pa, pb = kappa_binario(a, b)
    pabak = 2 * po - 1
    ks = "  n/d " if k is None else f"{k:+.3f}"
    print(f"{nome:<6} {ks}  {po*100:6.1f}%   {sum(a):>2}/39  {sum(b):>2}/39  "
          f"{pabak:+.3f}  {banda(k)}")
    return k, po, pabak


def main():
    df = carregar()
    print("=" * 78)
    print("ANÁLISE (A) — Confiabilidade da codificação das FMs (Tabela 9 do artigo)")
    print("anotador 1: fm_coding_model.py (codebook v0.2) | anotador 2: passada cega v0.2-Q")
    print("=" * 78)
    print(f"{'FM':<6} {'kappa':>6}  {'bruta':>6}   {'prev1':>5}  {'prev2':>5}  "
          f"{'PABAK':>6}  banda")
    resultados = {}
    for fm in FMS:
        a = df[f"{fm}_a1"].astype(int).tolist()
        b = df[f"{fm}_a2"].astype(int).tolist()
        resultados[fm] = linha(fm, a, b)

    definidos = {k: v[0] for k, v in resultados.items() if v[0] is not None}
    print()
    print(f"κ médio (só categorias definidas, n={len(definidos)}): "
          f"{sum(definidos.values())/len(definidos):+.3f}")
    print(f"κ médio (indefinidos tratados como 0, n=8): "
          f"{sum(v[0] or 0.0 for v in resultados.values())/8:+.3f}")
    nucleo = [resultados[f][0] for f in ("FM02", "FM04", "FM06")]
    print("núcleo corretivo humano (FM02/FM04/FM06): "
          + ", ".join(f"{f}={'n/d' if k is None else f'{k:+.3f}'}"
                      for f, k in zip(("FM02", "FM04", "FM06"), nucleo)))
    print("concordância bruta média: "
          f"{sum(v[1] for v in resultados.values())/8*100:.1f}%")

    print()
    print("=" * 78)
    print("ANÁLISE (B) — Validade de construto da métrica da RQ2")
    print("régua lexical (metalinguistic_adherence.py) vs. coluna MTL (juízo especialista)")
    print("=" * 78)
    lex = regua_lexical()
    df["regua"] = [lex[(c, r)] for c, r in zip(df["cenario"], df["rep"])]
    print(f"{'':<6} {'kappa':>6}  {'bruta':>6}   {'régua':>5}  {'MTL':>5}  "
          f"{'PABAK':>6}  banda")
    linha("RQ2", df["regua"].astype(int).tolist(), df["MTL"].astype(int).tolist())
    tx_lex = df["regua"].mean() * 100
    tx_mtl = df["MTL"].mean() * 100
    print(f"\ntaxa régua lexical: {tx_lex:.1f}% ({df['regua'].sum()}/39)")
    print(f"taxa juízo especialista (MTL): {tx_mtl:.1f}% ({df['MTL'].sum()}/39)")

    # matriz de confusão
    ct = pd.crosstab(df["regua"], df["MTL"], rownames=["régua"], colnames=["MTL"])
    print("\nmatriz de confusão régua × MTL:")
    print(ct.to_string())

    print()
    print("=" * 78)
    print("DISCORDÂNCIAS POR ITEM (para o confronto qualitativo)")
    print("=" * 78)
    for fm in FMS:
        d = df[df[f"{fm}_a1"] != df[f"{fm}_a2"]]
        if len(d):
            itens = ", ".join(f"{i}(c{c}r{r}: a1={x}→a2={y})" for i, c, r, x, y in
                              zip(d["ID"], d["cenario"], d["rep"],
                                  d[f"{fm}_a1"], d[f"{fm}_a2"]))
            print(f"{fm} ({len(d)}): {itens}")
    d = df[df["regua"] != df["MTL"]]
    print(f"\nRQ2 régua×MTL ({len(d)}): "
          + ", ".join(f"{i}(c{c}r{r}: régua={x}→MTL={y})" for i, c, r, x, y in
                      zip(d["ID"], d["cenario"], d["rep"], d["regua"], d["MTL"])))

    print()
    print("=" * 78)
    print("DIRECIONALIDADE DO DESACORDO")
    print("=" * 78)
    mais = menos = 0
    for fm in FMS:
        a, b = df[f"{fm}_a1"].astype(int), df[f"{fm}_a2"].astype(int)
        mais += int(((a == 0) & (b == 1)).sum())
        menos += int(((a == 1) & (b == 0)).sum())
    tot = mais + menos
    print(f"anotador 2 CREDITA função que o anotador 1 não marcou: {mais}/{tot} "
          f"({100*mais/tot:.1f}%)")
    print(f"anotador 2 RETIRA função que o anotador 1 marcou:      {menos}/{tot} "
          f"({100*menos/tot:.1f}%)")
    n1 = df[[f"{f}_a1" for f in FMS]].sum(axis=1)
    n2 = df[[f"{f}_a2" for f in FMS]].sum(axis=1)
    print(f"FMs por devolutiva — anotador 1: {n1.mean():.2f}  |  "
          f"anotador 2: {n2.mean():.2f}  (humanos, ref.: 3.8)")

    print()
    print("=" * 78)
    print("ROBUSTEZ DA CONCLUSÃO: núcleo corretivo sob as DUAS codificações")
    print("=" * 78)
    # Tabela tab:fm-freq do artigo (corpus de 65 devolutivas dos 5 especialistas).
    humano = {"FM01": 69, "FM02": 80, "FM03": 34, "FM04": 69,
              "FM05": 9, "FM06": 57, "FM07": 32, "FM08": 32}
    print(f"{'FM':<6} {'anot.1':>7} {'anot.2':>7} {'humano':>7}  "
          f"{'gap a1':>7} {'gap a2':>7}")
    for fm in FMS:
        p1 = df[f"{fm}_a1"].mean() * 100
        p2 = df[f"{fm}_a2"].mean() * 100
        h = humano[fm]
        marca = "  <-- núcleo" if fm in ("FM02", "FM04", "FM06") else ""
        print(f"{fm:<6} {p1:6.0f}% {p2:6.0f}% {h:6.0f}%  "
              f"{p1-h:+6.0f} {p2-h:+6.0f}{marca}")


if __name__ == "__main__":
    main()
