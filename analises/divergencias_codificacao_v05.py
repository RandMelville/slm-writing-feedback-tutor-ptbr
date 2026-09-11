"""Dossiê das divergências entre as duas codificações v0.5, para o exame qualitativo do §6.

Não reconcilia nada e não recalcula κ: só põe lado a lado, item a item, o que cada
codificadora marcou e a evidência que cada uma colou, para que a divergência possa ser
lida como divergência de definição, de limiar ou de descuido.

Para cada item com desacordo imprime:
  - a devolutiva (é o objeto codificado) e o texto do aluno abreviado;
  - as funções em desacordo, com a marca de cada codificadora;
  - a evidência de quem marcou 1;
  - candidatos a migração: funções que a outra codificadora marcou e a primeira não,
    no mesmo item, que é onde mora a confusão de fronteira (FM03 x FM07, FM02 x FM06).

Entrada: as capturas mais recentes em data/codificacao_v05_respostas/.
Saída: analises/divergencias_v05_<captura>.md

Uso: python3 analises/divergencias_codificacao_v05.py
"""
import importlib.util
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
CHAVE = ROOT / "data" / "segunda_codificacao_cega" / "chave_cega.csv"
ABA = "Codificação"
FMS = [f"FM{i:02d}" for i in range(1, 9)]
FPS = [f"FP{i:02d}" for i in range(1, 9)]

NOMES = {
    "FM01": "Reconhecer competência",
    "FM02": "Nomear o problema",
    "FM03": "Provocar reflexão",
    "FM04": "Oferecer pista",
    "FM05": "Modelar parcialmente",
    "FM06": "Propor revisão",
    "FM07": "Desafiar ampliação",
    "FM08": "Reforçar autonomia",
    "MTL": "Foco metalinguístico",
}


def _audita():
    caminho = ROOT / "analises" / "audita_codificacao_v05.py"
    spec = importlib.util.spec_from_file_location("audita_codificacao_v05", caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


AUD = _audita()


def carregar():
    arquivos = AUD.localiza()
    brutos = {}
    for rotulo, caminho in arquivos.items():
        df = pd.read_excel(caminho, sheet_name=ABA)
        df["ID"] = df["ID"].astype(str).str.strip()
        for col in FMS + FPS + ["MTL"]:
            df[col] = [AUD.celula(v) for v in df[col]]
        brutos[rotulo] = df.set_index("ID")
    chave = pd.read_csv(CHAVE).set_index("ID")[["cenario", "rep"]]
    return brutos, chave, {r: arquivos[r].name for r in arquivos}


def _kappa():
    caminho = ROOT / "analises" / "kappa_codificacao_v05.py"
    spec = importlib.util.spec_from_file_location("kappa_codificacao_v05", caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


KAP = _kappa()

PONT = str.maketrans({c: " " for c in ".,;:!?()[]{}\"'`-–—/\\*_"})


def tokens(v):
    """Vocábulos significativos de uma evidência, para medir se duas evidências cobrem o
    mesmo trecho. Descarta numeração de item, pontuação e palavras muito curtas."""
    if v is None or (isinstance(v, float) and pd.isna(v)):
        return set()
    t = str(v).lower().translate(PONT)
    return {w for w in t.split() if len(w) > 2 and not w.isdigit()}


def cobre(a, b, limite=0.8):
    """True se a evidência mais curta está contida na mais longa em 80% dos vocábulos."""
    if not a or not b:
        return False
    return len(a & b) / min(len(a), len(b)) >= limite


def trecho(v, limite=400):
    if v is None or (isinstance(v, float) and pd.isna(v)):
        return ""
    t = " ".join(str(v).split())
    return t if len(t) <= limite else t[:limite] + "..."


def main():
    brutos, chave, proc = carregar()
    A, B = brutos["A"], brutos["B"]
    captura = proc["A"].replace(".xlsx", "").split("_")[-1]
    colunas = FMS + ["MTL"]

    # divergências por item
    por_item = {}
    for rid in A.index:
        difs = [c for c in colunas if A.loc[rid, c] != B.loc[rid, c]]
        if difs:
            por_item[rid] = difs

    out = []

    def p(t=""):
        out.append(t)

    p(f"# Divergências entre as duas codificações v0.5 (captura de {captura})")
    p()
    p(f"Fonte: `{proc['A']}` e `{proc['B']}`. Nenhuma marcação foi alterada aqui.")
    p()
    total = sum(len(v) for v in por_item.values())
    p(f"{total} decisões em desacordo, distribuídas em {len(por_item)} das 39 devolutivas.")
    p()

    p("## Quadro por função")
    p()
    p("| Função | | A marca | B marca | em desacordo | A=1,B=0 | A=0,B=1 |")
    p("|---|---|---:|---:|---:|---:|---:|")
    for c in colunas:
        a1 = int(sum(1 for x in A[c] if x == 1))
        b1 = int(sum(1 for x in B[c] if x == 1))
        d = [r for r in A.index if A.loc[r, c] != B.loc[r, c]]
        so_a = sum(1 for r in d if A.loc[r, c] == 1)
        so_b = len(d) - so_a
        p(f"| {c} | {NOMES[c]} | {a1}/39 | {b1}/39 | {len(d)} | {so_a} | {so_b} |")
    p()

    p("## Coocorrência do desacordo: onde a marca de uma reaparece na outra")
    p()
    p("Para cada desacordo A=1/B=0 na função X, quais funções B marcou nesse mesmo item e A não.")
    p("É o rastro de confusão de fronteira: a leitura viu o movimento, mas o classificou em outra caixa.")
    p()
    migra = {}
    for rid, difs in por_item.items():
        for c in difs:
            if c == "MTL":
                continue
            origem, destino = ("A", "B") if A.loc[rid, c] == 1 else ("B", "A")
            outros = brutos[destino]
            candidatos = [
                d for d in FMS
                if d != c and outros.loc[rid, d] == 1 and brutos[origem].loc[rid, d] != 1
            ]
            for d in candidatos:
                migra[(c, d)] = migra.get((c, d), 0) + 1
    if migra:
        p("| perdida por uma | aparece na outra como | itens |")
        p("|---|---|---:|")
        for (c, d), n in sorted(migra.items(), key=lambda kv: -kv[1]):
            p(f"| {c} {NOMES[c]} | {d} {NOMES[d]} | {n} |")
    p()

    # ---------------------------------------------------------------- mesma evidência
    p("## Mesmo segmento, caixa diferente")
    p()
    p("Critério objetivo: em um desacordo sobre FMx, verifica-se se a outra codificadora marcou")
    p("alguma FMy no mesmo item cuja evidência colada cobre o mesmo trecho. 'Cobre' = 80% ou mais")
    p("dos vocábulos da evidência mais curta aparecem na mais longa, após normalização.")
    p()
    mesmos, outros_casos = [], []
    for rid, difs in por_item.items():
        for c in difs:
            if c == "MTL":
                continue
            origem, destino = ("A", "B") if A.loc[rid, c] == 1 else ("B", "A")
            ev = tokens(brutos[origem].loc[rid, f"Evidência {c}"])
            achou = None
            for d in FMS:
                if d == c or brutos[destino].loc[rid, d] != 1:
                    continue
                if cobre(ev, tokens(brutos[destino].loc[rid, f"Evidência {d}"])):
                    achou = d
                    break
            if achou:
                mesmos.append((rid, c, origem, achou, destino))
            else:
                outros_casos.append((rid, c, origem))
    n_fm = sum(len(v) for k, v in por_item.items() for _ in [0]) - 0
    n_fm = sum(1 for rid, difs in por_item.items() for c in difs if c != "MTL")
    p(f"**{len(mesmos)} dos {n_fm} desacordos sobre FM são o mesmo trecho classificado em outra "
      f"função.** Os outros {len(outros_casos)} são divergência sobre a existência do movimento.")
    p()
    p("| item | função de uma | quem marcou | função da outra |")
    p("|---|---|---|---|")
    for rid, c, origem, d, destino in sorted(mesmos):
        p(f"| {rid} | {c} {NOMES[c]} | {origem} | {d} {NOMES[d]} ({destino}) |")
    p()
    pares = {}
    for _, c, _, d, _ in mesmos:
        chave_par = tuple(sorted((c, d)))
        pares[chave_par] = pares.get(chave_par, 0) + 1
    p("Concentração por par de funções:")
    p()
    p("| par | desacordos |")
    p("|---|---:|")
    for (c, d), n in sorted(pares.items(), key=lambda kv: -kv[1]):
        p(f"| {c} x {d} ({NOMES[c]} x {NOMES[d]}) | {n} |")
    p()
    p("Desacordos sobre a existência do movimento, sem contrapartida na outra codificação:")
    p()
    for rid, c, origem in sorted(outros_casos):
        p(f"- {rid}, {c} ({NOMES[c]}): só {origem} marcou.")
    p()

    # ---------------------------------------------------------------- FP por devolutiva
    p("## Falso positivo no nível da devolutiva")
    p()
    p("Análise auxiliar, FORA do plano pré-registrado do §6, para separar duas coisas que o κ")
    p("por função mistura: discordar sobre *se há* movimento sem lastro, e discordar sobre *em")
    p("qual função* registrá-lo. Como o FP é preso à FM, quando a FM migra de caixa o FP migra")
    p("junto e conta como desacordo mesmo quando as duas apontaram o mesmo defeito.")
    p()
    lin_a = [int(any(A.loc[r, f] == 1 for f in FPS)) for r in A.index]
    lin_b = [int(any(B.loc[r, f] == 1 for f in FPS)) for r in A.index]
    k, po, pa, pb = KAP.kappa_binario(lin_a, lin_b)
    ks = "n/d" if k is None else f"{k:+.3f}"
    p(f"'a devolutiva tem ao menos um movimento sinalizado como sem lastro':")
    p(f"κ = {ks}, concordância bruta = {po*100:.1f}%, A = {sum(lin_a)}/39, B = {sum(lin_b)}/39, "
      f"banda {KAP.banda(k)}.")
    p()
    ambas = [r for r, x, y in zip(A.index, lin_a, lin_b) if x == 1 and y == 1]
    p(f"As duas sinalizaram problema de lastro nas mesmas {len(ambas)} devolutivas: "
      f"{', '.join(ambas)}.")
    p()

    p("## Item a item")
    p()
    for rid in sorted(por_item):
        difs = por_item[rid]
        cen, rep = int(chave.loc[rid, "cenario"]), int(chave.loc[rid, "rep"])
        p(f"### {rid} (cenário {cen}, execução {rep}) - em desacordo: {', '.join(difs)}")
        p()
        p(f"**Texto do aluno.** {trecho(A.loc[rid, 'Texto do aluno'], 300)}")
        p()
        p(f"**Devolutiva.** {trecho(A.loc[rid, 'Devolutiva'], 700)}")
        p()
        marcas_a = [c for c in FMS if A.loc[rid, c] == 1]
        marcas_b = [c for c in FMS if B.loc[rid, c] == 1]
        p(f"- A marcou: {', '.join(marcas_a) or 'nenhuma'} | MTL = {A.loc[rid, 'MTL']}")
        p(f"- B marcou: {', '.join(marcas_b) or 'nenhuma'} | MTL = {B.loc[rid, 'MTL']}")
        p()
        for c in difs:
            if c == "MTL":
                p(f"**MTL**: A = {A.loc[rid, 'MTL']}, B = {B.loc[rid, 'MTL']}")
                p()
                continue
            quem = "A" if A.loc[rid, c] == 1 else "B"
            fonte = brutos[quem]
            p(f"**{c} ({NOMES[c]})**: {quem} = 1, "
              f"{'B' if quem == 'A' else 'A'} = 0")
            p(f"  - evidência de {quem}: {trecho(fonte.loc[rid, f'Evidência {c}'], 350) or '(vazia)'}")
            fp = fonte.loc[rid, f"FP{c[2:]}"]
            if fp == 1:
                p(f"  - {quem} marcou também FP{c[2:]} = 1: "
                  f"{trecho(fonte.loc[rid, f'Justificativa FP{c[2:]}'], 300)}")
            p()
        obs_b = trecho(B.loc[rid, "Observações"], 900)
        if obs_b:
            p(f"**Observação de B neste item.** {obs_b}")
            p()

    # Observações de B em itens sem divergência de FM/MTL
    p("## Observações da codificadora B em itens sem divergência")
    p()
    sozinhas = [r for r in B.index
                if trecho(B.loc[r, "Observações"]) and r not in por_item]
    if not sozinhas:
        p("Nenhuma.")
    for rid in sozinhas:
        cen, rep = int(chave.loc[rid, "cenario"]), int(chave.loc[rid, "rep"])
        p(f"- **{rid}** (cenário {cen}, execução {rep}): {trecho(B.loc[rid, 'Observações'], 900)}")
    p()

    destino = ROOT / "analises" / f"divergencias_v05_{captura}.md"
    destino.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"{total} decisões em desacordo em {len(por_item)} devolutivas")
    print(f"[dossiê salvo em {destino.relative_to(ROOT)}]")


if __name__ == "__main__":
    main()
