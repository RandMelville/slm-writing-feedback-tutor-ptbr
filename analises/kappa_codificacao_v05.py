"""Concordância entre as duas codificações v0.5, exatamente como o Protocolo v0.5 §6 fixou.

Roda DEPOIS de `analises/audita_codificacao_v05.py`. Não escreve nos arquivos congelados:
toda normalização acontece aqui, em memória.

O que o §6 pré-registrou, e que este script executa nesta ordem:

  1. FM01-FM08 e MTL: concordância bruta e κ de Cohen, sempre com as prevalências de cada
     codificadora, PABAK (Byrt et al., 1993) e a banda de Landis e Koch (1977). Nenhuma
     categoria é omitida.
  2. FP01-FP08: frequência por codificadora e concordância bruta no subconjunto em que ao
     menos uma marcou FMxx = 1, com o denominador explícito. κ só quando definido.
  3. VFMxx = 1 sse FMxx = 1 e FPxx = 0 (presença sem falso positivo identificado), tratada
     como terceiro indicador, nunca como sinônimo de FM.
  4. Matriz de divergências por item, sem reconciliação retroativa.
  5. Consolidação pelos 13 cenários (3 execuções cada): estabilidade dentro do cenário.
  6. RQ2: a régua lexical de `src/metalinguistic_adherence.py` confrontada com o MTL de cada
     codificadora, que são duas leituras humanas independentes do mesmo construto.

Entrada: os `codificacao_{A,B}_<AAAA-MM-DD>.xlsx` mais recentes em data/codificacao_v05_respostas/.
Saída: stdout e analises/kappa_codificacao_v05_<captura>.txt, nomeado pela data de captura
para que resultado de captura antiga nunca seja confundido com o final.

Uso: python3 analises/kappa_codificacao_v05.py
"""
import importlib.util
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
import metalinguistic_adherence as mla  # noqa: E402

CHAVE = ROOT / "data" / "segunda_codificacao_cega" / "chave_cega.csv"
ABA = "Codificação"
FMS = [f"FM{i:02d}" for i in range(1, 9)]
FPS = [f"FP{i:02d}" for i in range(1, 9)]

# A captura de 08/09 é anterior às correções que as duas codificadoras fizeram em 08 e 09/09.
# Ver data/codificacao_v05_respostas/PROCEDENCIA.md.
CAPTURA_DEFASADA = "2026-09-08"


def _audita():
    """Reaproveita localiza() e celula() da auditoria, em vez de reescrever o carregador."""
    caminho = ROOT / "analises" / "audita_codificacao_v05.py"
    spec = importlib.util.spec_from_file_location("audita_codificacao_v05", caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


AUD = _audita()


def banda(k):
    """Landis e Koch (1977)."""
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
    """κ de Cohen para duas listas binárias pareadas. None se pe == 1 (marginais degenerados)."""
    n = len(a)
    po = sum(1 for x, y in zip(a, b) if x == y) / n
    pa1, pb1 = sum(a) / n, sum(b) / n
    pe = pa1 * pb1 + (1 - pa1) * (1 - pb1)
    if abs(1 - pe) < 1e-12:
        return None, po, pa1, pb1
    return (po - pe) / (1 - pe), po, pa1, pb1


def carregar():
    """Devolve (df, procedência). Falha alto se houver célula vazia: a auditoria vem antes."""
    arquivos = AUD.localiza()
    quadros = {}
    for rotulo, caminho in arquivos.items():
        df = pd.read_excel(caminho, sheet_name=ABA)
        df["ID"] = df["ID"].astype(str).str.strip()
        for col in FMS + FPS + ["MTL"]:
            valores = [AUD.celula(v) for v in df[col]]
            vazias = [i for i, v in zip(df["ID"], valores) if v is None]
            invalidas = [f"{i}/{col}={v!r}" for i, v in zip(df["ID"], valores)
                         if v is not None and v not in (0, 1)]
            if vazias or invalidas:
                sys.exit(
                    f"ERRO em {caminho.name}, coluna {col}: "
                    f"{len(vazias)} vazia(s) {vazias[:5]}, {len(invalidas)} inválida(s) "
                    f"{invalidas[:5]}.\nRode analises/audita_codificacao_v05.py e resolva com a "
                    "codificadora antes de calcular concordância."
                )
            df[col] = valores
        quadros[rotulo] = df.set_index("ID")[FMS + FPS + ["MTL"]]

    a, b = quadros["A"], quadros["B"]
    if list(a.index) != list(b.index):
        a, b = a.sort_index(), b.sort_index()
    assert list(a.index) == list(b.index), "IDs não pareiam entre A e B"

    df = a.join(b, lsuffix="_A", rsuffix="_B")
    chave = pd.read_csv(CHAVE).set_index("ID")[["cenario", "rep"]]
    df = df.join(chave)
    assert df["cenario"].notna().all(), "ID sem correspondência na chave de decegamento"
    assert len(df) == 39, f"esperado 39 linhas, obtido {len(df)}"

    proc = {r: arquivos[r].name for r in ("A", "B")}
    return df, proc


def regua_lexical():
    """Flag binária da régua lexical de Koch, por (cenario, rep)."""
    recs = mla.load_records("qwen2.5:3b-instruct", "all")
    return {(r["cenario"], r["rep"]): int(r["adere"]) for r in mla.score(recs)}


def linha(p, nome, a, b, n_total=None):
    n = n_total if n_total is not None else len(a)
    k, po, pa, pb = kappa_binario(a, b)
    ks = "  n/d " if k is None else f"{k:+.3f}"
    p(f"{nome:<7} {ks}  {po*100:6.1f}%   {sum(a):>2}/{n:<3} {sum(b):>2}/{n:<3} "
      f"{2*po-1:+.3f}  {banda(k)}")
    return k, po


def cabecalho_tabela(p, rot_a="prev A", rot_b="prev B"):
    p(f"{'':<7} {'kappa':>6}  {'bruta':>6}   {rot_a:<6} {rot_b:<6} {'PABAK':>6}  banda")


def main():
    df, proc = carregar()
    saida = []

    def p(txt=""):
        print(txt)
        saida.append(txt)

    captura = proc["A"].replace(".xlsx", "").split("_")[-1]

    p("=" * 78)
    p("CONCORDÂNCIA ENTRE AS DUAS CODIFICAÇÕES v0.5 (Protocolo v0.5, §6)")
    p("=" * 78)
    p(f"codificadora A: {proc['A']}")
    p(f"codificadora B: {proc['B']}")
    if CAPTURA_DEFASADA in proc["A"] or CAPTURA_DEFASADA in proc["B"]:
        p("")
        p("!" * 78)
        p(f"AVISO: a captura de {CAPTURA_DEFASADA} é ANTERIOR às correções que as duas fizeram")
        p("em 08 e 09/09 (células que faltavam e a convenção de branco = 0 da codificadora B).")
        p("Estes números são ensaio de código, NÃO são o resultado do artigo. Recapture as duas")
        p("planilhas no Drive (Arquivo > Baixar > Microsoft Excel) antes de reportar qualquer coisa.")
        p("!" * 78)
    p("")

    # ------------------------------------------------------------------ 1. FM e MTL
    p("=" * 78)
    p("1. PRESENÇA DA FUNÇÃO (FM01-FM08) E METALINGUAGEM (MTL), n = 39")
    p("=" * 78)
    cabecalho_tabela(p)
    res_fm = {}
    for col in FMS + ["MTL"]:
        a = df[f"{col}_A"].tolist()
        b = df[f"{col}_B"].tolist()
        res_fm[col] = linha(p, col, a, b)
    p("")
    definidos = [v[0] for k, v in res_fm.items() if k in FMS and v[0] is not None]
    p(f"FMs com κ definido: {len(definidos)}/8")
    if definidos:
        p(f"κ mediano entre as FMs definidas: {sorted(definidos)[len(definidos)//2]:+.3f}")
    p("O §7 do Protocolo proíbe usar um κ médio como critério único de decisão: funções com")
    p("prevalências distintas não se reduzem a um número só.")
    p("")

    # ------------------------------------------------------------------ 2. FP condicional
    p("=" * 78)
    p("2. FALSO POSITIVO (FP01-FP08), no subconjunto em que ao menos uma marcou FM = 1")
    p("=" * 78)
    p("O denominador muda por função: FP só existe onde a FM existe (Protocolo §3.0).")
    p("")
    p(f"{'':<7} {'kappa':>6}  {'bruta':>6}   {'FP=1 A':<7} {'FP=1 B':<7} {'PABAK':>6}  "
      f"{'n':>3}  banda")
    for i in range(1, 9):
        fm, fp = f"FM{i:02d}", f"FP{i:02d}"
        sub = df[(df[f"{fm}_A"] == 1) | (df[f"{fm}_B"] == 1)]
        n = len(sub)
        tot_a, tot_b = int(df[f"{fp}_A"].sum()), int(df[f"{fp}_B"].sum())
        if n == 0:
            p(f"{fp:<7}   n/d       n/d    {tot_a:<7} {tot_b:<7}   n/d    0  "
              f"nenhuma linha com {fm} = 1")
            continue
        a, b = sub[f"{fp}_A"].tolist(), sub[f"{fp}_B"].tolist()
        k, po, _, _ = kappa_binario(a, b)
        ks = "  n/d " if k is None else f"{k:+.3f}"
        motivo = "" if k is not None else "  (marginais degenerados)"
        p(f"{fp:<7} {ks}  {po*100:6.1f}%   {sum(a):>2}/{n:<4} {sum(b):>2}/{n:<4} "
          f"{2*po-1:+.3f} {n:>3}  {banda(k)}{motivo}")
    p("")
    p("As colunas FP=1 contam dentro do subconjunto; os totais nas 39 linhas vão abaixo.")
    p(f"total de FP = 1 nas 39 linhas -- A: {int(df[[f'{c}_A' for c in FPS]].sum().sum())}  |  "
      f"B: {int(df[[f'{c}_B' for c in FPS]].sum().sum())}")
    p("")

    # ------------------------------------------------------------------ 3. VFM derivada
    p("=" * 78)
    p("3. PRESENÇA SEM FALSO POSITIVO IDENTIFICADO (VFMxx = 1 sse FMxx = 1 e FPxx = 0), n = 39")
    p("=" * 78)
    p("Indicador derivado, mais estrito que o de julho: o mesmo caso que lá ficava em 1 aqui")
    p("produz FM = 1 e FP = 1, logo VFM = 0 (Protocolo §6).")
    cabecalho_tabela(p)
    for i in range(1, 9):
        fm, fp = f"FM{i:02d}", f"FP{i:02d}"
        a = [int(x == 1 and y == 0) for x, y in zip(df[f"{fm}_A"], df[f"{fp}_A"])]
        b = [int(x == 1 and y == 0) for x, y in zip(df[f"{fm}_B"], df[f"{fp}_B"])]
        linha(p, f"VFM{i:02d}", a, b)
    p("")

    # ------------------------------------------------------------------ 4. divergências
    p("=" * 78)
    p("4. DIVERGÊNCIAS POR ITEM (entram no exame qualitativo, sem reconciliação retroativa)")
    p("=" * 78)
    for col in FMS + ["MTL"]:
        d = df[df[f"{col}_A"] != df[f"{col}_B"]]
        if len(d) == 0:
            p(f"{col}: nenhuma")
            continue
        itens = ", ".join(f"{i}(c{int(c)}r{int(r)}: A={x} B={y})" for i, c, r, x, y in
                          zip(d.index, d["cenario"], d["rep"], d[f"{col}_A"], d[f"{col}_B"]))
        p(f"{col} ({len(d)}): {itens}")
    p("")
    mais = sum(int(((df[f"{c}_A"] == 0) & (df[f"{c}_B"] == 1)).sum()) for c in FMS)
    menos = sum(int(((df[f"{c}_A"] == 1) & (df[f"{c}_B"] == 0)).sum()) for c in FMS)
    tot = mais + menos
    if tot:
        p(f"direção do desacordo em FM: B credita função que A não marcou em {mais}/{tot} "
          f"({100*mais/tot:.1f}%); B retira função que A marcou em {menos}/{tot} "
          f"({100*menos/tot:.1f}%).")
    n_a = df[[f"{c}_A" for c in FMS]].sum(axis=1)
    n_b = df[[f"{c}_B" for c in FMS]].sum(axis=1)
    p(f"FMs por devolutiva -- A: {n_a.mean():.2f}  |  B: {n_b.mean():.2f}")
    p("")

    # ------------------------------------------------------------------ 5. por cenário
    p("=" * 78)
    p("5. CONSOLIDAÇÃO PELOS 13 CENÁRIOS (3 execuções cada): estabilidade dentro do cenário")
    p("=" * 78)
    p("'estável' = as 3 execuções do cenário receberam a mesma marcação naquela coluna.")
    p("")
    p(f"{'':<7} {'estáveis A':>11} {'estáveis B':>11}   (de 13 cenários)")
    for col in FMS + FPS + ["MTL"]:
        est = {}
        for rot in ("A", "B"):
            est[rot] = sum(1 for _, g in df.groupby("cenario") if g[f"{col}_{rot}"].nunique() == 1)
        p(f"{col:<7} {est['A']:>11} {est['B']:>11}")
    p("")
    p(f"{'cenário':<9} {'FM=1 A':>7} {'FM=1 B':>7}  {'FP=1 A':>7} {'FP=1 B':>7}  "
      f"{'MTL A':>6} {'MTL B':>6}")
    for cen, g in df.groupby("cenario"):
        p(f"{int(cen):<9} {int(g[[f'{c}_A' for c in FMS]].sum().sum()):>7} "
          f"{int(g[[f'{c}_B' for c in FMS]].sum().sum()):>7}  "
          f"{int(g[[f'{c}_A' for c in FPS]].sum().sum()):>7} "
          f"{int(g[[f'{c}_B' for c in FPS]].sum().sum()):>7}  "
          f"{int(g['MTL_A'].sum()):>6} {int(g['MTL_B'].sum()):>6}")
    p("")

    # ------------------------------------------------------------------ 6. RQ2
    p("=" * 78)
    p("6. RQ2: régua lexical executada por programa vs. MTL de cada codificadora")
    p("=" * 78)
    lex = regua_lexical()
    df["regua"] = [lex[(int(c), int(r))] for c, r in zip(df["cenario"], df["rep"])]
    cabecalho_tabela(p, "régua ", "humano")
    for rot in ("A", "B"):
        linha(p, f"régua×{rot}", df["regua"].tolist(), df[f"MTL_{rot}"].tolist())
    linha(p, "MTL A×B", df["MTL_A"].tolist(), df["MTL_B"].tolist())
    p("")
    p(f"taxa da régua lexical: {df['regua'].mean()*100:.1f}% ({int(df['regua'].sum())}/39)")
    for rot in ("A", "B"):
        p(f"taxa MTL {rot}: {df[f'MTL_{rot}'].mean()*100:.1f}% "
          f"({int(df[f'MTL_{rot}'].sum())}/39)")
    for rot in ("A", "B"):
        ct = pd.crosstab(df["regua"], df[f"MTL_{rot}"],
                         rownames=["régua"], colnames=[f"MTL {rot}"])
        p("")
        p(f"matriz de confusão régua × MTL {rot}:")
        p(ct.to_string())

    destino = ROOT / "analises" / f"kappa_codificacao_v05_{captura}.txt"
    destino.write_text("\n".join(saida) + "\n", encoding="utf-8")
    print(f"\n[relatório salvo em {destino.relative_to(ROOT)}]")


if __name__ == "__main__":
    main()
