"""Summary table + 2 figures (latency, throughput) from both round JSONs."""
import json, sys
from pathlib import Path
from statistics import mean

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent

# No args: read both round JSONs. With args: use the given paths.
SRCS = [Path(p) for p in sys.argv[1:]] or [
    ROOT / "data" / "results" / "round_1_main_models.json",
    ROOT / "data" / "results" / "round_2_complementary_models.json",
]
OUT_DIR = ROOT / "analises"
OUT_DIR.mkdir(exist_ok=True)

rows = []
for src in SRCS:
    if src.exists():
        rows.extend(json.loads(src.read_text(encoding="utf-8")))
    else:
        print(f"aviso: {src} não encontrado, pulando")


def divergente(resp: str) -> bool:
    """True se a resposta não bate o padrão estruturado esperado."""
    try:
        d = json.loads(resp or "")
    except Exception:
        return True
    if not isinstance(d, dict):
        return True
    pf, pr = d.get("pontos_fortes"), d.get("perguntas_reflexivas")
    if not (isinstance(pf, str) and pf.strip()):
        return True
    if not (isinstance(pr, list) and pr and all(isinstance(p, str) and p.strip() for p in pr)):
        return True
    return False


by_model = {}
for r in rows:
    if "erro" in r:
        continue
    by_model.setdefault(r["modelo_testado"], []).append(r)

print(f"{'modelo':<24} {'n':>4} {'lat_media_ms':>13} {'tok_out_media':>14} {'divergentes':>12}")
print("-" * 72)
agg = {}
for m, rs in sorted(by_model.items()):
    lats = [r["latencia_ms"] for r in rs]
    toks = [r["tokens_output"] for r in rs]
    div = sum(1 for r in rs if divergente(r["resposta_ia"]))
    agg[m] = {
        "n": len(rs),
        "lat_media": mean(lats),
        "tok_media": mean(toks),
        "throughput": mean(toks) / (mean(lats) / 1000),
        "divergentes": div,
    }
    print(f"{m:<24} {len(rs):>4} {mean(lats):>13.0f} {mean(toks):>14.1f} {div:>5}/{len(rs):<6}")

# Ordena por latência crescente — leitura mais útil pro paper
modelos = sorted(agg.keys(), key=lambda m: agg[m]["lat_media"])

# Cor por taxa de divergência: limpo (verde) / parcial (amarelo) / colapso (vermelho)
def cor(m: str) -> str:
    rate = agg[m]["divergentes"] / agg[m]["n"]
    if rate >= 0.5: return "#c0392b"
    if rate > 0:    return "#f1c40f"
    return "#2980b9"

cores = [cor(m) for m in modelos]

# Gráfico 1 — latência média (8 modelos)
fig, ax = plt.subplots(figsize=(10, 5.5), dpi=150)
barras = ax.bar(modelos, [agg[m]["lat_media"] for m in modelos], color=cores)
ax.set_ylabel("Latência média (ms)")
ax.set_title(f"Latência média por modelo — {len(modelos)} modelos × 13 cenários × 3 reps")
ax.axhline(10000, color="red", linestyle="--", linewidth=1, alpha=0.6, label="10s (limite UX sala)")
for b, m in zip(barras, modelos):
    ax.text(b.get_x() + b.get_width()/2, b.get_height(), f"{agg[m]['lat_media']:.0f}",
            ha="center", va="bottom", fontsize=8)
# Legenda manual das cores
from matplotlib.patches import Patch
legenda_cores = [
    Patch(facecolor="#2980b9", label="JSON OK (0% divergência)"),
    Patch(facecolor="#f1c40f", label="Divergência parcial"),
    Patch(facecolor="#c0392b", label="Colapso (≥50% divergência)"),
]
ax.legend(handles=legenda_cores + [plt.Line2D([0],[0], color="red", linestyle="--", label="10s")],
          loc="upper left", fontsize=8)
ax.grid(axis="y", linestyle=":", alpha=0.5)
plt.xticks(rotation=20, ha="right")
fig.tight_layout()
fig.savefig(OUT_DIR / "latencia_media.png")
plt.close(fig)

# Gráfico 2 — throughput tokens/s (8 modelos)
fig, ax = plt.subplots(figsize=(10, 5.5), dpi=150)
barras = ax.bar(modelos, [agg[m]["throughput"] for m in modelos], color=cores)
ax.set_ylabel("Throughput médio (tokens/s)")
ax.set_title(f"Throughput de saída por modelo — {len(modelos)} modelos")
for b, m in zip(barras, modelos):
    ax.text(b.get_x() + b.get_width()/2, b.get_height(), f"{agg[m]['throughput']:.1f}",
            ha="center", va="bottom", fontsize=8)
ax.legend(handles=legenda_cores, loc="upper right", fontsize=8)
ax.grid(axis="y", linestyle=":", alpha=0.5)
plt.xticks(rotation=20, ha="right")
fig.tight_layout()
fig.savefig(OUT_DIR / "throughput_tokens.png")
plt.close(fig)

print(f"\ngráficos: {OUT_DIR/'latencia_media.png'}, {OUT_DIR/'throughput_tokens.png'}")
