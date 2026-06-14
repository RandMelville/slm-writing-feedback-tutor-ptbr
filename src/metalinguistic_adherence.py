"""Scorer da aderência metalinguística (RQ2).

Detecta a presença de termos da taxonomia de coesão/coerência de Koch no texto da
resposta de um modelo (ou de um anotador humano). Reconstrução do script perdido na
reorganização de 2026-05-25.

IMPORTANTE (documentar no paper): isto é uma TRIAGEM de limite inferior, não uma
medida. A presença de um termo não garante adequação pedagógica, nem a ausência
garante falha. Por isso o número produzido aqui deve ser validado contra julgamento
humano via Cohen's kappa (ver data/human_baseline/).

Critério: uma resposta "mobiliza a rubrica" se o texto contém >= 1 termo da taxonomia.
A varredura cobre TODO o texto produzido pelo modelo (pontos_fortes + perguntas), e
tolera respostas malformadas (ex.: pontos_fortes como lista) varrendo o texto bruto.

Uso:
    python3 src/metalinguistic_adherence.py                 # qwen2.5:3b-instruct, rep 1 (reproduz o paper)
    python3 src/metalinguistic_adherence.py --model qwen2.5:3b-instruct --reps all   # n=39
    python3 src/metalinguistic_adherence.py --human data/human_baseline/anotador_A.json
"""
import argparse
import json
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESULT_FILES = [
    ROOT / "data" / "results" / "round_1_main_models.json",
    ROOT / "data" / "results" / "round_2_complementary_models.json",
]

# Stems da taxonomia metalinguística de Koch usada na rubrica (§3.6 do paper).
# Chave = stem normalizado (sem acento, minúsculo); valor = rótulo legível.
# Casamento por substring após normalizar o texto. Lista deliberadamente fiel aos
# 12 termos do paper; ampliá-la mudaria o número e exigiria nova validação.
KOCH_STEMS = {
    "coes": "coesão",                 # cohesion
    "conect": "conectivo/conector",   # connector
    "conjun": "conjunção",            # connector (variante)
    "pronom": "pronome/pronominalização",  # pronoun
    "referenc": "referencial/referenciação",  # referential
    "retomad": "retomada referencial",        # referential (variante)
    "sequenci": "sequenciação/sequencial",    # sequential
    "ambigu": "ambiguidade",          # ambiguity
    "repet": "repetição",             # repetition
    "sinon": "sinonímia/sinônimo",    # synonym
    "elipse": "elipse",               # ellipsis
    "elipt": "elíptico",              # ellipsis (variante)
    "argument": "operador argumentativo",  # argumentative operator
    "marcador": "marcador",           # (temporal) marker
    "temporal": "marcador temporal",  # temporal marker
    "justapos": "justaposição",       # juxtaposition
}


def normalize(text: str) -> str:
    """Minúsculas + remoção de acentos, para casamento robusto de stems."""
    text = text.lower()
    nfkd = unicodedata.normalize("NFKD", text)
    return "".join(c for c in nfkd if not unicodedata.combining(c))


def response_text(raw: str) -> str:
    """Extrai todo o texto gerado, tolerando JSON malformado."""
    try:
        parsed = json.loads(raw)
    except (json.JSONDecodeError, TypeError):
        return raw or ""
    if not isinstance(parsed, dict):
        return raw or ""
    parts = []
    pf = parsed.get("pontos_fortes")
    pr = parsed.get("perguntas_reflexivas")
    for chunk in (pf, pr):
        if isinstance(chunk, str):
            parts.append(chunk)
        elif isinstance(chunk, list):
            parts.extend(str(x) for x in chunk)
    # fallback: se as chaves esperadas não vieram, varre o JSON inteiro como texto
    return " ".join(parts) if parts else (raw or "")


def matched_terms(text: str) -> list:
    norm = normalize(text)
    return sorted({label for stem, label in KOCH_STEMS.items() if stem in norm})


def load_records(model: str, reps):
    records = []
    for f in RESULT_FILES:
        if not f.exists():
            continue
        for r in json.loads(f.read_text(encoding="utf-8")):
            if r.get("modelo_testado") != model:
                continue
            if reps != "all" and r.get("rep") not in reps:
                continue
            records.append(r)
    return records


def score(records):
    rows = []
    for r in records:
        text = response_text(r.get("resposta_ia", ""))
        terms = matched_terms(text)
        rows.append({
            "cenario": r.get("cenario_id"),
            "rep": r.get("rep"),
            "adere": bool(terms),
            "termos": terms,
        })
    return rows


def report(rows, title):
    n = len(rows)
    adere = sum(1 for x in rows if x["adere"])
    print(f"\n=== {title} ===")
    print(f"Aderência metalinguística: {adere}/{n} ({100*adere/max(n,1):.1f}%)")
    print(f"{'cen':>3} {'rep':>3}  {'adere':<6} termos")
    for x in sorted(rows, key=lambda d: (d["cenario"] or 0, d["rep"] or 0)):
        flag = "SIM" if x["adere"] else "—"
        print(f"{x['cenario']:>3} {x['rep']:>3}  {flag:<6} {', '.join(x['termos'])}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="qwen2.5:3b-instruct")
    ap.add_argument("--reps", default="1", help="'1', '1,2,3' ou 'all'")
    ap.add_argument("--human", help="JSON de respostas humanas [{cenario_id, resposta_ia}]")
    args = ap.parse_args()

    if args.human:
        recs = json.loads(Path(args.human).read_text(encoding="utf-8"))
        report(score(recs), f"Humano: {Path(args.human).name}")
        return

    reps = "all" if args.reps == "all" else [int(x) for x in args.reps.split(",")]
    recs = load_records(args.model, reps)
    if not recs:
        print(f"Nenhum registro para modelo={args.model} reps={args.reps}")
        return
    report(score(recs), f"{args.model} (reps={args.reps}, n={len(recs)})")


if __name__ == "__main__":
    main()
