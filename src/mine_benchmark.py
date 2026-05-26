"""Extracts latency, tokens, and structural divergence flags from raw benchmark JSON to flat CSV."""
import csv, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = Path(sys.argv[1] if len(sys.argv) > 1 else ROOT / "data" / "results" / "round_1_main_models.json")
DST = Path(sys.argv[2] if len(sys.argv) > 2 else ROOT / "analises" / "benchmark_flat.csv")

rows = json.loads(SRC.read_text(encoding="utf-8"))
DST.parent.mkdir(parents=True, exist_ok=True)

out = []
for r in rows:
    raw = r.get("resposta_ia", "") or ""
    parsed, err = None, ""
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as e:
        err = f"json: {e.msg}"

    pf = parsed.get("pontos_fortes") if isinstance(parsed, dict) else None
    pr = parsed.get("perguntas_reflexivas") if isinstance(parsed, dict) else None
    pr_list = pr if isinstance(pr, list) else []

    out.append({
        "modelo": r.get("modelo_testado"),
        "cenario": r.get("cenario_id"),
        "foco": r.get("foco_teorico"),
        "latencia_ms": r.get("latencia_ms"),
        "tokens_in": r.get("tokens_input"),
        "tokens_out": r.get("tokens_output"),
        "tok_per_s": round(1000 * (r.get("tokens_output") or 0) / max(r.get("latencia_ms") or 1, 1), 2),
        "json_ok": parsed is not None,
        "tem_pontos_fortes": bool(isinstance(pf, str) and pf.strip()),
        "n_perguntas": len(pr_list),
        "len_resposta": len(raw),
        "erro_parse": err,
    })

with DST.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0].keys()))
    w.writeheader()
    w.writerows(out)

n = len(out)
ok = sum(1 for r in out if r["json_ok"])
print(f"{DST}  ({n} linhas, {ok}/{n} JSON ok)")
print("\nlatência por modelo (média / max ms):")
by_model = {}
for r in out:
    by_model.setdefault(r["modelo"], []).append(r["latencia_ms"])
for m, lats in sorted(by_model.items()):
    print(f"  {m:<15} média={sum(lats)//len(lats):>6} max={max(lats):>6}")
