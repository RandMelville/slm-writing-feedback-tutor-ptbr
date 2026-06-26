"""
Codificacao das 65 devolutivas segundo o codebook de Funcoes de Mediacao (FM01-FM08).

Primeira passada (anotador 1: leitura atenta aplicando o codebook v0.1).
A codificacao fica EMBUTIDA aqui para ser auditavel; o calculo de kappa vira
quando um segundo anotador humano codificar uma amostra de forma independente.

Saidas:
  analises/codificacao_fm.csv      matriz respondente x cenario x FM (binaria)
  analises/fm_frequencia.png       heatmap professor x funcao
Uso: python analises/fm_coding.py
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]

FUNCS = {
    1: "FM01 Reconhecer competencia",
    2: "FM02 Nomear o problema",
    3: "FM03 Provocar reflexao",
    4: "FM04 Oferecer pista",
    5: "FM05 Modelar parcialmente",
    6: "FM06 Propor revisao",
    7: "FM07 Desafiar ampliacao",
    8: "FM08 Reforcar autonomia",
}

# (respondente -> {cenario: [FMs presentes]}). Cenarios 11-13 sao casos-teto.
CODING = {
    # FM02/FM04 ampliadas na v0.2 (pos-kappa): "nomear insuficiencia" e "indicar
    # o que desenvolver / estrategia" passam a contar; "explicar como pergunta" segue FM03.
    "E1": {
        1: [1, 2, 4, 6], 2: [1, 2, 4, 6], 3: [1, 2, 3, 4, 6], 4: [1, 2, 4, 6],
        5: [1, 2, 4, 5, 6], 6: [1, 2, 4, 6], 7: [1, 2, 4, 5, 6], 8: [1, 2, 3],
        9: [1, 2, 4, 6], 10: [1, 2, 3, 4, 6], 11: [1], 12: [1], 13: [1],
    },
    # E2 recodificado apos correcao do Prof. Marcelo (2026-06-24):
    # perguntas austeras = FM03 (nao FM02); estrategias "reler/anotar/substituir" e
    # orientacao de o-que-especificar-para-o-leitor = FM04. Registro sem afeto, mas
    # com forte reflexao e andaime procedimental — nao "puramente diagnostico".
    "E2": {
        1: [2, 4, 6], 2: [2, 6], 3: [2, 3], 4: [2, 4, 6], 5: [2, 3, 6], 6: [2, 3],
        7: [2, 4, 6], 8: [2, 3, 4, 6], 9: [2, 3], 10: [2, 3, 4, 6], 11: [2, 4],
        12: [1, 2, 3], 13: [2, 3, 6],
    },
    "E3": {
        1: [2, 4, 6], 2: [2, 4, 6], 3: [2, 4, 6], 4: [2, 4, 6], 5: [2, 4, 6],
        6: [2, 4, 6], 7: [2, 4, 6], 8: [1], 9: [2, 4, 6], 10: [1, 2, 4, 6], 11: [1],
        12: [1], 13: [1],
    },
    "E4": {
        1: [1, 2, 4, 7, 8], 2: [1, 2, 4, 6, 7, 8], 3: [1, 2, 4, 7, 8], 4: [1, 2, 4, 6, 8],
        5: [1, 2, 4, 7, 8], 6: [1, 2, 4, 6, 8], 7: [1, 2, 4, 6, 7, 8], 8: [1, 2, 4, 7, 8],
        9: [1, 2, 4, 7, 8], 10: [1, 2, 4, 7, 8], 11: [1, 2, 4, 7], 12: [1], 13: [1],
    },
    "E5": {
        1: [1, 2, 3, 4, 6, 7, 8], 2: [1, 2, 3, 4, 6, 7, 8], 3: [1, 2, 3, 4, 6, 7, 8],
        4: [1, 2, 3, 4], 5: [1, 2, 3, 4, 7, 8], 6: [1, 2, 4, 6, 7, 8], 7: [1, 4, 5, 7, 8],
        8: [1, 2, 3, 4, 7, 8], 9: [1, 2, 3, 4, 5, 6, 7, 8], 10: [1, 2, 3, 4, 5, 6, 7, 8],
        11: [1, 3, 7], 12: [1, 3, 7, 8], 13: [1, 3, 5, 6, 7, 8],
    },
}

MISALIGNED = {("E4", 10)}  # devolutiva fala do C9; isolar em contagens por foco

rows = []
for prof, cens in CODING.items():
    for cen, fms in cens.items():
        row = {"respondente": prof, "cenario": cen,
               "teto": cen in (11, 12, 13),
               "desalinhada": (prof, cen) in MISALIGNED}
        for k in FUNCS:
            row[f"FM{k:02d}"] = int(k in fms)
        row["n_funcoes"] = len(fms)
        rows.append(row)

df = pd.DataFrame(rows)
fm_cols = [f"FM{k:02d}" for k in FUNCS]
df.to_csv(ROOT / "analises" / "codificacao_fm.csv", index=False)

# --- Frequencia global (proporcao das 65 devolutivas) ---
print("=== Frequencia de cada funcao (n=65 devolutivas) ===")
for k in FUNCS:
    c = f"FM{k:02d}"
    print(f"  {FUNCS[k]:32s}  {df[c].sum():2d}/65  ({df[c].mean()*100:4.0f}%)")

print(f"\nMedia de funcoes por devolutiva: {df['n_funcoes'].mean():.1f} "
      f"(min {df['n_funcoes'].min()}, max {df['n_funcoes'].max()})")

# --- Perfil por professor (proporcao dos 13 cenarios) ---
print("\n=== Perfil por professor (proporcao dos 13 cenarios) ===")
prof_profile = df.groupby("respondente")[fm_cols].mean()
print((prof_profile * 100).round(0).astype(int).to_string())
print("\nMedia de funcoes por devolutiva, por professor:")
print(df.groupby("respondente")["n_funcoes"].mean().round(1).to_string())

# --- Combinacoes mais comuns ---
print("\n=== Combinacoes (assinaturas de FM) mais frequentes ===")
df["assinatura"] = df[fm_cols].apply(
    lambda r: "+".join(f"FM{k:02d}" for k in FUNCS if r[f"FM{k:02d}"]), axis=1)
for sig, n in df["assinatura"].value_counts().head(8).items():
    print(f"  {n:2d}x  {sig or '(vazio)'}")

# --- Heatmap professor x funcao ---
fig, ax = plt.subplots(figsize=(8, 3.2))
data = prof_profile.values * 100
im = ax.imshow(data, cmap="YlGnBu", vmin=0, vmax=100, aspect="auto")
ax.set_xticks(range(len(fm_cols)))
ax.set_xticklabels([f"FM{k:02d}" for k in FUNCS], fontsize=9)
ax.set_yticks(range(len(prof_profile.index)))
ax.set_yticklabels(prof_profile.index, fontsize=9)
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        ax.text(j, i, f"{data[i, j]:.0f}", ha="center", va="center",
                fontsize=8, color="black" if data[i, j] < 60 else "white")
ax.set_title("Funcoes de mediacao por professor (% dos 13 cenarios)", fontsize=10)
fig.colorbar(im, ax=ax, fraction=0.025, pad=0.02, label="%")
fig.tight_layout()
fig.savefig(ROOT / "analises" / "fm_frequencia.png", dpi=140)
print("\nFiguras e CSV salvos em analises/.")
