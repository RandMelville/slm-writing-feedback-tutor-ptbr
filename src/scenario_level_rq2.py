"""Analise da RQ2 com o CENARIO como unidade de analise.

Motivacao (Revisor A, JBCS): "the 39 responses per model derive from only 13 scenarios
repeated three times. The repetitions are useful for assessing stability, but they do not
provide the same diversity as 39 independent scenarios. A scenario-level analysis would
strengthen the conclusions."

O ponto e estatistico e procede: as 39 respostas nao sao independentes. Sao 13 grupos de 3
respostas cada, e respostas do mesmo cenario se parecem mais entre si do que respostas de
cenarios diferentes. O IC de Wilson sobre n=39 trata as 39 como independentes e, por isso,
e anticonservador (estreito demais).

Este script produz tres leituras que respondem ao revisor sem coletar nada novo:

  (1) Tabela por cenario: quantas das 3 repeticoes aderem, por cenario.
  (2) Estatisticas com o cenario como unidade: media das proporcoes por cenario, e as
      duas leituras binarias extremas (adere em ao menos 1 rep; adere nas 3).
  (3) Correcao para o agrupamento: ICC (ANOVA one-way), efeito de desenho
      DEFF = 1 + (m-1)*ICC, n efetivo = n/DEFF, e IC de Wilson recalculado sobre o n
      efetivo. Complementado por um bootstrap de cluster (reamostra CENARIOS, nao
      respostas), que nao depende da suposicao de ICC constante.

Saidas: stdout + analises/scenario_level_rq2.json
Uso: python src/scenario_level_rq2.py
"""
import json
import math
import random
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from metalinguistic_adherence import load_records, score  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
MODELO = "qwen2.5:3b-instruct"
SEED = 20260727
B = 20000  # reamostragens do bootstrap de cluster


def wilson(k, n, z=1.959963985):
    """IC de Wilson 95% para uma proporcao. Aceita n nao inteiro (n efetivo)."""
    if n <= 0:
        return (0.0, 0.0)
    p = k / n
    d = 1 + z * z / n
    centro = (p + z * z / (2 * n)) / d
    margem = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, centro - margem), min(1.0, centro + margem))


def icc_anova(grupos):
    """ICC(1) por ANOVA one-way, tamanhos de cluster iguais (m repeticoes por cenario)."""
    k = len(grupos)
    m = len(next(iter(grupos.values())))
    assert all(len(v) == m for v in grupos.values()), "cluster sizes desiguais"
    todos = [x for v in grupos.values() for x in v]
    grande_media = sum(todos) / len(todos)

    ss_between = m * sum((sum(v) / m - grande_media) ** 2 for v in grupos.values())
    ss_within = sum((x - sum(v) / m) ** 2 for v in grupos.values() for x in v)
    ms_between = ss_between / (k - 1)
    ms_within = ss_within / (k * (m - 1))

    denom = ms_between + (m - 1) * ms_within
    if denom == 0:
        return 0.0, ms_between, ms_within
    return (ms_between - ms_within) / denom, ms_between, ms_within


def bootstrap_cluster(grupos, b=B, seed=SEED):
    """Reamostra CENARIOS com reposicao; devolve percentis 2.5 e 97.5 da proporcao."""
    rng = random.Random(seed)
    chaves = list(grupos)
    props = []
    for _ in range(b):
        amostra = [grupos[rng.choice(chaves)] for _ in chaves]
        planas = [x for v in amostra for x in v]
        props.append(sum(planas) / len(planas))
    props.sort()
    lo = props[int(0.025 * (b - 1))]
    hi = props[int(0.975 * (b - 1))]
    return lo, hi


def main():
    linhas = score(load_records(MODELO, "all"))
    grupos = defaultdict(list)
    for x in linhas:
        grupos[x["cenario"]].append(1 if x["adere"] else 0)
    grupos = dict(sorted(grupos.items()))

    n = sum(len(v) for v in grupos.values())
    k_ader = sum(sum(v) for v in grupos.values())
    m = len(next(iter(grupos.values())))
    n_cen = len(grupos)

    print("=== (1) por cenario (reps aderentes / 3) ===")
    for cen, v in grupos.items():
        print(f"  S{cen:02d}: {sum(v)}/{m}  {''.join('X' if x else '.' for x in v)}")

    sempre = sum(1 for v in grupos.values() if sum(v) == m)
    nunca = sum(1 for v in grupos.values() if sum(v) == 0)
    ao_menos_uma = sum(1 for v in grupos.values() if sum(v) >= 1)
    instaveis = n_cen - sempre - nunca

    print("\n=== (2) cenario como unidade ===")
    p_pool = k_ader / n
    props_cen = [sum(v) / m for v in grupos.values()]
    media_cen = sum(props_cen) / n_cen
    print(f"  proporcao agregada (resposta como unidade): {k_ader}/{n} = {100*p_pool:.1f}%")
    print(f"  media das proporcoes por cenario:           {100*media_cen:.1f}%")
    lo_s, hi_s = wilson(sempre, n_cen)
    lo_a, hi_a = wilson(ao_menos_uma, n_cen)
    print(f"  cenarios que aderem nas {m} reps:  {sempre}/{n_cen} ({100*sempre/n_cen:.1f}%)  Wilson [{100*lo_s:.1f}%; {100*hi_s:.1f}%]")
    print(f"  cenarios que aderem em >=1 rep:   {ao_menos_uma}/{n_cen} ({100*ao_menos_uma/n_cen:.1f}%)  Wilson [{100*lo_a:.1f}%; {100*hi_a:.1f}%]")
    print(f"  cenarios que nunca aderem:        {nunca}/{n_cen}")
    print(f"  cenarios instaveis (1 ou 2 de {m}): {instaveis}/{n_cen}")

    print("\n=== (3) correcao para o agrupamento ===")
    icc, msb, msw = icc_anova(grupos)
    deff = 1 + (m - 1) * icc
    n_eff = n / deff
    lo_naive, hi_naive = wilson(k_ader, n)
    lo_eff, hi_eff = wilson(p_pool * n_eff, n_eff)
    lo_boot, hi_boot = bootstrap_cluster(grupos)
    print(f"  ICC(1) = {icc:.3f}   (MSB={msb:.4f}, MSW={msw:.4f})")
    print(f"  DEFF   = {deff:.3f}   n efetivo = {n_eff:.1f} (de {n})")
    print(f"  Wilson ingenuo  (n={n}):      [{100*lo_naive:.1f}%; {100*hi_naive:.1f}%]  largura {100*(hi_naive-lo_naive):.1f} pp")
    print(f"  Wilson n efetivo ({n_eff:.1f}):    [{100*lo_eff:.1f}%; {100*hi_eff:.1f}%]  largura {100*(hi_eff-lo_eff):.1f} pp")
    print(f"  bootstrap de cluster (B={B}): [{100*lo_boot:.1f}%; {100*hi_boot:.1f}%]  largura {100*(hi_boot-lo_boot):.1f} pp")

    saida = {
        "modelo": MODELO,
        "por_cenario": {f"S{c}": v for c, v in grupos.items()},
        "n_respostas": n, "n_cenarios": n_cen, "reps_por_cenario": m,
        "aderentes": k_ader,
        "proporcao_agregada": p_pool,
        "media_proporcoes_por_cenario": media_cen,
        "cenarios_sempre": sempre, "cenarios_nunca": nunca,
        "cenarios_ao_menos_uma": ao_menos_uma, "cenarios_instaveis": instaveis,
        "icc": icc, "deff": deff, "n_efetivo": n_eff,
        "ic_wilson_ingenuo": [lo_naive, hi_naive],
        "ic_wilson_n_efetivo": [lo_eff, hi_eff],
        "ic_bootstrap_cluster": [lo_boot, hi_boot],
        "bootstrap_B": B, "seed": SEED,
    }
    destino = ROOT / "analises" / "scenario_level_rq2.json"
    destino.write_text(json.dumps(saida, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\ngravado: {destino.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
