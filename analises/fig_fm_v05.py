"""Figura das Funções de Mediação sob as duas codificações v0.5.

Substitui fm_modelo_vs_humano.png, que plotava a codificação de procedência
retirada. A forma mudou de barras agrupadas para intervalo entre as duas
codificadoras: o ponto do modelo não é estimativa pontual, e a figura tem de
mostrar isso em vez de escondê-lo atrás de uma barra só.

Azul = codificadora A, laranja = codificadora B, marca cinza = corpus de
referência dos cinco professores (n = 65), que é distribuição descritiva e não
uma terceira medida da mesma coisa.

Uso: python3 analises/fig_fm_v05.py
"""
import importlib.util
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
FMS = [f"FM{i:02d}" for i in range(1, 9)]

# Corpus de referência dos 5 professores (65 devolutivas), Tabela tab:fm-freq do artigo.
REFERENCIA = {"FM01": 69, "FM02": 80, "FM03": 34, "FM04": 69,
              "FM05": 9, "FM06": 57, "FM07": 32, "FM08": 32}

AZUL, LARANJA, CINZA = "#2a78d6", "#eb6834", "#8a8a85"
TINTA, TINTA2 = "#1a1a19", "#5c5c57"


def carregar():
    spec = importlib.util.spec_from_file_location(
        "kappa_codificacao_v05", ROOT / "analises" / "kappa_codificacao_v05.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    df, _ = mod.carregar()
    return {c: (df[f"{c}_A"].mean() * 100, df[f"{c}_B"].mean() * 100) for c in FMS}


NOMES = {
    "FM01": "Recognize competence", "FM02": "Name the problem",
    "FM03": "Provoke reflection", "FM04": "Offer a cue",
    "FM05": "Partially model", "FM06": "Propose revision",
    "FM07": "Challenge expansion", "FM08": "Reinforce autonomy",
}


def main():
    prev = carregar()
    # O conversor renderiza a figura a 6,3 polegadas de largura, sempre. Desenhar
    # nesse tamanho evita que ela seja ampliada e que a tipografia dela fique maior
    # que a do corpo do artigo. Por isso tambem nao ha tight_layout nem
    # bbox_inches="tight": a moldura e posta a mao, para a largura final ser exata.
    fig = plt.figure(figsize=(6.3, 2.55))
    ax = fig.add_axes([0.295, 0.19, 0.672, 0.69])
    y = list(range(len(FMS)))[::-1]

    from matplotlib.markers import MarkerStyle

    for i, fm in zip(y, FMS):
        a, b = prev[fm]
        junto = abs(a - b) <= 1.5
        if not junto:
            ax.plot([a, b], [i, i], color=CINZA, linewidth=1.2, zorder=1,
                    solid_capstyle="round")
        ax.scatter([REFERENCIA[fm]], [i], marker="D", s=20, facecolor="white",
                   edgecolor=TINTA2, linewidth=0.9, zorder=2)
        if junto:
            # As duas coincidem: marca partida, para nenhuma sumir sob a outra.
            ax.scatter([a], [i], s=30, color=AZUL, zorder=3, linewidth=0.3,
                       marker=MarkerStyle("o", fillstyle="left"), edgecolor="white")
            ax.scatter([b], [i], s=30, color=LARANJA, zorder=3, linewidth=0.3,
                       marker=MarkerStyle("o", fillstyle="right"), edgecolor="white")
        else:
            ax.scatter([a], [i], s=26, color=AZUL, zorder=3,
                       edgecolor="white", linewidth=0.7)
            ax.scatter([b], [i], s=26, color=LARANJA, zorder=3,
                       edgecolor="white", linewidth=0.7)

    # Rotulos numa coluna alinhada a esquerda, fora da area de dados. O tick label
    # do matplotlib e alinhado a direita e deixaria a borda esquerda serrilhada.
    ax.set_yticks(y)
    ax.set_yticklabels([])
    for i, fm in zip(y, FMS):
        eixo = ax.get_yaxis_transform()
        ax.text(-0.42, i, fm, transform=eixo, ha="left", va="center",
                fontsize=8, color=TINTA)
        ax.text(-0.335, i, NOMES[fm], transform=eixo, ha="left", va="center",
                fontsize=8, color=TINTA)

    ax.set_ylim(-0.6, len(FMS) - 0.4)
    ax.set_xlim(-2.5, 100)
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.set_xticklabels(["0", "25", "50", "75", "100%"], fontsize=7.5, color=TINTA2)
    ax.set_xlabel("turns in which the function is coded", fontsize=8, color=TINTA2,
                  labelpad=3)
    ax.grid(axis="x", color="#eceae6", linewidth=0.6)
    ax.set_axisbelow(True)
    for lado in ("top", "right", "left"):
        ax.spines[lado].set_visible(False)
    ax.spines["bottom"].set_color("#d5d4d0")
    ax.spines["bottom"].set_linewidth(0.6)
    ax.tick_params(length=0, pad=2)

    manuais = [
        plt.Line2D([], [], marker="o", linestyle="", color=AZUL, markersize=4.5,
                   label="Coder A"),
        plt.Line2D([], [], marker="o", linestyle="", color=LARANJA, markersize=4.5,
                   label="Coder B"),
        plt.Line2D([], [], marker="D", linestyle="", markerfacecolor="white",
                   markeredgecolor=TINTA2, markersize=4.5, label="Specialists (n=65)"),
    ]
    ax.legend(handles=manuais, fontsize=7.5, frameon=False, ncol=3,
              loc="lower right", bbox_to_anchor=(1.0, 1.01), handletextpad=0.3,
              columnspacing=1.4, labelcolor=TINTA, borderpad=0)

    for destino in (ROOT / "analises" / "fm_modelo_v05.png",
                    ROOT / "paper" / "jbcs" / "fm_modelo_v05.png"):
        fig.savefig(destino, dpi=300, facecolor="white")
        print(f"[{destino.relative_to(ROOT)}]")


if __name__ == "__main__":
    main()
