"""Benchmark runner against local Ollama. n repetitions × M models × 13 canonical scenarios."""
import argparse, json, time, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import requests

from prompts import SYSTEM_PROMPT

ROOT = Path(__file__).resolve().parent.parent

# Modelos default: faixa deployável (≤3B) pro paper de benchmark.
# Sobrescreva com --models "a,b,c" pra rodar outro conjunto.
MODELOS_DEFAULT = [
    "llama3.2:1b",
    "llama3.2:3b",
    "gemma2:2b",
    "qwen2.5:1.5b-instruct",
    "qwen2.5:3b-instruct",
    "phi3:mini",
]

OLLAMA_URL = "http://localhost:11434/api/chat"


def carregar_cenarios(path: Path) -> list[dict]:
    """Lê JSONL no formato MLX (messages=[system,user,assistant]) e extrai o user content."""
    cenarios = []
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line:
            continue
        d = json.loads(line)
        user = next(m for m in d["messages"] if m["role"] == "user")["content"]
        cenarios.append({"cenario_id": i, "conteudo": user, "foco_teorico": ""})
    return cenarios


def chamar_ollama(modelo: str, conteudo: str, timeout: int) -> dict:
    payload = {
        "model": modelo,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": conteudo},
        ],
        "stream": False,
        "format": "json",
        "options": {"temperature": 0.2},
    }
    t0 = time.time()
    r = requests.post(OLLAMA_URL, json=payload, timeout=timeout)
    latencia_ms = int((time.time() - t0) * 1000)
    r.raise_for_status()
    data = r.json()
    return {
        "latencia_ms": latencia_ms,
        "tokens_input": data.get("prompt_eval_count", 0),
        "tokens_output": data.get("eval_count", 0),
        "resposta_ia": data["message"]["content"],
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", default=",".join(MODELOS_DEFAULT),
                    help="lista separada por vírgula (default: faixa ≤3B)")
    ap.add_argument("--reps", type=int, default=3, help="repetições por par modelo×cenário (default: 3)")
    ap.add_argument("--scenarios", type=Path, default=ROOT / "data" / "scenarios_canonical_koch.jsonl")
    ap.add_argument("--out", type=Path, default=ROOT / "data" / "results" / "round_1_main_models.json")
    ap.add_argument("--timeout", type=int, default=120)
    args = ap.parse_args()

    modelos = [m.strip() for m in args.models.split(",") if m.strip()]
    cenarios = carregar_cenarios(args.scenarios)
    total = len(modelos) * len(cenarios) * args.reps
    print(f"benchmark: {len(modelos)} modelos × {len(cenarios)} cenários × {args.reps} reps = {total} chamadas")
    print(f"saída: {args.out}\n")

    resultados = []
    feitas = 0
    for modelo in modelos:
        print(f"--- {modelo} ---")
        for cenario in cenarios:
            for rep in range(1, args.reps + 1):
                feitas += 1
                try:
                    r = chamar_ollama(modelo, cenario["conteudo"], args.timeout)
                    resultados.append({
                        "modelo_testado": modelo,
                        "cenario_id": cenario["cenario_id"],
                        "foco_teorico": cenario["foco_teorico"],
                        "rep": rep,
                        **r,
                    })
                    print(f"  [{feitas:>3}/{total}] cen={cenario['cenario_id']:>2} rep={rep} "
                          f"{r['latencia_ms']:>6}ms  tok_out={r['tokens_output']}")
                except Exception as e:
                    print(f"  [{feitas:>3}/{total}] cen={cenario['cenario_id']:>2} rep={rep} ❌ {e}")
                    resultados.append({
                        "modelo_testado": modelo,
                        "cenario_id": cenario["cenario_id"],
                        "foco_teorico": cenario["foco_teorico"],
                        "rep": rep,
                        "erro": str(e),
                    })

    args.out.write_text(json.dumps(resultados, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n✅ {len(resultados)} linhas salvas em {args.out}")


if __name__ == "__main__":
    main()
