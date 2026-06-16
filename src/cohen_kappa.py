"""Cohen's kappa entre dois codificadores, por dimensão (RQ2 / baseline humano).

Operacionaliza o que o codebook descreve (data/human_baseline/CODEBOOK_kappa.md):
concordância entre dois codificadores humanos nas dimensões A (foco) e B (mediação),
e, à parte, heurística-vs-humano na dimensão A colapsada em binário (A1 vs não-A1).

Só stdlib. Cohen (1960); banda de interpretação de Landis & Koch (1977); IC 95%
pela aproximação assintótica do erro-padrão (reportar com cautela em n pequeno).

Formato de entrada (JSON, lista de objetos), uma linha por unidade codificada:
    [{"unidade": "qwen_c01_r1", "A": "A1", "B": "B2"}, ...]
"unidade" é a chave de pareamento (mesma em ambos os arquivos). Campos A/B opcionais
por dimensão; pares sem o campo nos dois arquivos são ignorados naquela dimensão.

Uso:
    python3 src/cohen_kappa.py codificador_A.json codificador_B.json
    python3 src/cohen_kappa.py heuristica.json consenso.json --dims A --binary-a
    python3 src/cohen_kappa.py --demo
"""
import argparse
import json
import math
from pathlib import Path


def load(path):
    rows = json.loads(Path(path).read_text(encoding="utf-8"))
    return {r["unidade"]: r for r in rows}


def paired(a, b, dim):
    """Pares (cod_a, cod_b) das unidades presentes nos dois arquivos com o campo dim."""
    out = []
    for key in a.keys() & b.keys():
        va, vb = a[key].get(dim), b[key].get(dim)
        if va is not None and vb is not None:
            out.append((str(va), str(vb)))
    return out


def cohen_kappa(pairs):
    n = len(pairs)
    if n == 0:
        return None
    cats = sorted({c for pair in pairs for c in pair})
    po = sum(1 for x, y in pairs if x == y) / n
    # marginais
    pa = {c: sum(1 for x, _ in pairs if x == c) / n for c in cats}
    pb = {c: sum(1 for _, y in pairs if y == c) / n for c in cats}
    pe = sum(pa[c] * pb[c] for c in cats)
    if pe == 1.0:
        kappa = 1.0  # concordância perfeita e degenerada
    else:
        kappa = (po - pe) / (1 - pe)
    # erro-padrão assintótico (Fleiss/Cohen) e IC 95%
    se = math.sqrt(po * (1 - po) / (n * (1 - pe) ** 2)) if pe != 1.0 else 0.0
    # kappa pertence a [-1, 1]; o IC assintótico pode estourar com n pequeno -> aparar
    lo = max(-1.0, kappa - 1.96 * se)
    hi = min(1.0, kappa + 1.96 * se)
    return {"n": n, "cats": cats, "po": po, "pe": pe, "kappa": kappa,
            "se": se, "ci95": (lo, hi)}


def band(k):
    # Landis & Koch (1977)
    if k < 0:    return "poor (<0)"
    if k <= .20: return "slight (0.00-0.20)"
    if k <= .40: return "fair (0.21-0.40)"
    if k <= .60: return "moderate (0.41-0.60)"
    if k <= .80: return "substantial (0.61-0.80)"
    return "almost perfect (0.81-1.00)"


def collapse_a1(pairs):
    """A1 vs não-A1 (binário), para a validação heurística-vs-humano da dimensão A."""
    m = lambda v: "A1" if v == "A1" else "nao-A1"
    return [(m(x), m(y)) for x, y in pairs]


def report(pairs, title):
    res = cohen_kappa(pairs)
    print(f"\n=== {title} ===")
    if not res:
        print("  (sem pares válidos)")
        return
    lo, hi = res["ci95"]
    print(f"  n={res['n']}  categorias={res['cats']}")
    print(f"  concordância observada Po = {res['po']:.3f}")
    print(f"  concordância esperada  Pe = {res['pe']:.3f}")
    print(f"  Cohen's kappa = {res['kappa']:.3f}  (IC95% {lo:.3f} a {hi:.3f})")
    print(f"  interpretação (Landis & Koch): {band(res['kappa'])}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file_a", nargs="?", help="JSON do codificador A (ou heurística)")
    ap.add_argument("file_b", nargs="?", help="JSON do codificador B (ou consenso)")
    ap.add_argument("--dims", default="A,B", help="dimensões a avaliar (ex.: A ou A,B)")
    ap.add_argument("--binary-a", action="store_true",
                    help="colapsa a dimensão A em A1 vs não-A1 (heurística-vs-humano)")
    ap.add_argument("--demo", action="store_true", help="roda um exemplo sintético")
    args = ap.parse_args()

    if args.demo:
        a = {f"u{i}": {"A": x, "B": y} for i, (x, y) in enumerate(
            [("A1","B1"),("A1","B2"),("A2","B3"),("A1","B1"),("A3","B2"),
             ("A2","B1"),("A1","B2"),("A1","B1"),("A2","B3"),("A1","B1")])}
        b = {f"u{i}": {"A": x, "B": y} for i, (x, y) in enumerate(
            [("A1","B1"),("A1","B1"),("A2","B3"),("A1","B1"),("A2","B2"),
             ("A2","B1"),("A1","B2"),("A1","B2"),("A2","B3"),("A1","B1")])}
        report(paired(a, b, "A"), "DEMO dimensão A (foco)")
        report(paired(a, b, "B"), "DEMO dimensão B (mediação)")
        report(collapse_a1(paired(a, b, "A")), "DEMO dimensão A binária (A1 vs não-A1)")
        return

    if not args.file_a or not args.file_b:
        ap.error("forneça file_a e file_b (ou use --demo)")
    a, b = load(args.file_a), load(args.file_b)
    for dim in [d.strip() for d in args.dims.split(",") if d.strip()]:
        pairs = paired(a, b, dim)
        if args.binary_a and dim == "A":
            report(collapse_a1(pairs), f"Dimensão A binária (A1 vs não-A1) — {len(pairs)} pares")
        else:
            report(pairs, f"Dimensão {dim} — {len(pairs)} pares")


if __name__ == "__main__":
    main()
