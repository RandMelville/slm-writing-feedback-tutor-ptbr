"""
Codificacao das 39 devolutivas do modelo conformante (qwen2.5:3b-instruct) segundo o
codebook de Funcoes de Mediacao (FM01-FM08) — a MESMA regua aplicada aos 5 especialistas
em fm_coding.py. Objetivo: comparar o repertorio de mediacao do modelo com o nucleo
operacional humano (FM02/FM04/FM06), respondendo "diante deste texto, o modelo mobilizou
FMs compativeis com a pratica dos especialistas?".

Fonte: data/results/round_1_main_models.json + round_2_complementary_models.json
       (39 registros qwen2.5:3b-instruct = 13 cenarios x 3 repeticoes).

Codificacao EMBUTIDA (anotador 1, Claude, codebook v0.2, regra de evidencia minima).
RESSALVA: passada unica; uma 2a passada cega e trabalho futuro, como ja registrado para a
recodificacao v0.2 do corpus humano. O formato de saida (pontos_fortes + perguntas_reflexivas)
PRE-CARREGA FM01 (reconhecer) e abre espaco a FM03/FM07 via as perguntas; por isso o sinal
informativo esta na AUSENCIA de FM02/FM04/FM06 (o nucleo humano), nao na presenca de FM01.

Saidas:
  analises/codificacao_fm_modelo.csv
  analises/fm_modelo_vs_humano.png
Uso: python analises/fm_coding_model.py
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]

FUNCS = {
    1: "FM01 Reconhecer competencia", 2: "FM02 Nomear o problema",
    3: "FM03 Provocar reflexao", 4: "FM04 Oferecer pista",
    5: "FM05 Modelar parcialmente", 6: "FM06 Propor revisao",
    7: "FM07 Desafiar ampliacao", 8: "FM08 Reforcar autonomia",
}

# (cenario, rep) -> [FMs presentes]. Justificativa de span resumida ao lado.
# Cenarios 11-13 sao casos-teto (textos bem desenvolvidos).
MODEL_CODING = {
    # S1: PF elogia estrutura (FM01); perguntas sao de enredo (nao FM03 estrito).
    (1, 1): [1], (1, 2): [1], (1, 3): [1],
    # S2: PF "bom entendimento" (FM01); perguntas interpretam a OBRA, nao o texto do aluno.
    (2, 1): [1], (2, 2): [1], (2, 3): [1],
    # S3: PF reconhece (FM01); r1 sonda a contradicao triste/riu (FM03) + enquadra sequencia (FM04);
    #     r2 pergunta sobre repeticao do PROPRIO texto (FM03); r3 reflexao sobre reescrita (FM03).
    (3, 1): [1, 3, 4], (3, 2): [1, 3], (3, 3): [1, 3],
    # S4: PF reconhece; perguntas pedem ampliar/detalhar (FM07); r3 nomeia "melhorar coesao" (FM02)
    #     + pista para conectar (FM04) + ampliacao (FM07).
    (4, 1): [1, 7], (4, 2): [1, 7], (4, 3): [1, 2, 4, 7],
    # S5: PF reconhece; perguntas de enredo (obra).
    (5, 1): [1], (5, 2): [1], (5, 3): [1],
    # S6: PF reconhece (e MISCREDITA repeticao/conectivo como qualidade); perguntas de enredo.
    (6, 1): [1], (6, 2): [1], (6, 3): [1],
    # S7: r1 sonda 'tava/estava' e excesso de 'ele' = metatextual (FM03); r2 amplia (FM07);
    #     r3 sugere dispositivos concretos = pista (FM04).
    (7, 1): [1, 3], (7, 2): [1, 7], (7, 3): [1, 4],
    # S8: PF reconhece; r2/r3 pedem analise/continuacao (FM07).
    (8, 1): [1], (8, 2): [1, 7], (8, 3): [1, 7],
    # S9: r1 pede proxima acao (FM07); r3 da pista (repetir/conectivos — orientacao concreta, FM04).
    (9, 1): [1, 7], (9, 2): [1], (9, 3): [1, 4],
    # S10: r1/r2 pedem aprofundar analise (FM07); r3 so reconhece.
    (10, 1): [1, 7], (10, 2): [1, 7], (10, 3): [1],
    # S11 (teto): r1 transfere tecnica de coesao = pista (FM04) + amplia (FM07); r2/r3 ampliam (FM07).
    (11, 1): [1, 4, 7], (11, 2): [1, 7], (11, 3): [1, 7],
    # S12 (teto): r1/r3 pedem aprofundar/analisar, inclui ponte com PC (FM07).
    (12, 1): [1, 7], (12, 2): [1], (12, 3): [1, 7],
    # S13 (teto): r1/r2 ampliam (FM07); r3 da pista de marcador temporal e substituicao lexical (FM04).
    (13, 1): [1, 7], (13, 2): [1, 7], (13, 3): [1, 4],
}

# Devolutivas em que o FM01 RECONHECE como qualidade um fenomeno que era o problema PLANTADO
# (anti-padrao: o modelo reforca o defeito em vez de nomea-lo). Cenarios problematicos S1-S10.
MISCREDIT = {(1, 2), (6, 1), (6, 3), (7, 1), (7, 3), (10, 1)}

rows = []
for (cen, rep), fms in MODEL_CODING.items():
    row = {"cenario": cen, "rep": rep, "teto": cen in (11, 12, 13),
           "miscredito_fm01": (cen, rep) in MISCREDIT}
    for k in FUNCS:
        row[f"FM{k:02d}"] = int(k in fms)
    row["n_funcoes"] = len(fms)
    rows.append(row)

df = pd.DataFrame(rows).sort_values(["cenario", "rep"]).reset_index(drop=True)
fm_cols = [f"FM{k:02d}" for k in FUNCS]
df.to_csv(ROOT / "analises" / "codificacao_fm_modelo.csv", index=False)

print("=== Prevalencia de cada FM no modelo (n=39 devolutivas) ===")
model_prev = {}
for k in FUNCS:
    c = f"FM{k:02d}"
    model_prev[c] = df[c].mean() * 100
    print(f"  {FUNCS[k]:32s}  {df[c].sum():2d}/39  ({df[c].mean()*100:4.0f}%)")
print(f"\nMedia de FMs por devolutiva (modelo): {df['n_funcoes'].mean():.1f}")
print(f"Devolutivas que MISCREDITAM o defeito plantado como qualidade (FM01): "
      f"{df['miscredito_fm01'].sum()} (em cenarios problematicos)")

# Referencia humana (do corpus de 65, fm_resultados.md / Tabela 2 do paper).
HUMAN_PREV = {"FM01": 69, "FM02": 80, "FM03": 34, "FM04": 69,
              "FM05": 9, "FM06": 57, "FM07": 32, "FM08": 32}
HUMAN_MEAN = 3.8

print("\n=== Modelo x nucleo humano (pontos percentuais) ===")
print(f"{'FM':6s} {'modelo%':>8s} {'humano%':>8s} {'gap':>6s}")
for k in FUNCS:
    c = f"FM{k:02d}"
    print(f"{c:6s} {model_prev[c]:8.0f} {HUMAN_PREV[c]:8d} {model_prev[c]-HUMAN_PREV[c]:6.0f}")

# --- Figura: barras agrupadas modelo vs humano ---
fig, ax = plt.subplots(figsize=(8, 3.4))
x = range(len(fm_cols))
w = 0.4
ax.bar([i - w/2 for i in x], [model_prev[c] for c in fm_cols], w,
       label="Model (qwen2.5:3b, n=39)", color="#d1495b")
ax.bar([i + w/2 for i in x], [HUMAN_PREV[c] for c in fm_cols], w,
       label="Specialists (n=65)", color="#30638e")
ax.set_xticks(list(x))
ax.set_xticklabels(fm_cols, fontsize=9)
ax.set_ylabel("% of feedback turns")
ax.set_ylim(0, 100)
ax.legend(fontsize=8)
for i, c in enumerate(fm_cols):
    ax.text(i - w/2, model_prev[c] + 1, f"{model_prev[c]:.0f}", ha="center", fontsize=7)
    ax.text(i + w/2, HUMAN_PREV[c] + 1, f"{HUMAN_PREV[c]:.0f}", ha="center", fontsize=7)
fig.tight_layout()
fig.savefig(ROOT / "analises" / "fm_modelo_vs_humano.png", dpi=140, bbox_inches="tight")
paper_dir = ROOT / "paper" / "jbcs"
if paper_dir.exists():
    fig.savefig(paper_dir / "fm_modelo_vs_humano.png", dpi=140, bbox_inches="tight")
print("\nCSV e figura salvos em analises/ (e copia em paper/jbcs/).")
