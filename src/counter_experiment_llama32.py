"""Contra-experimento para falsear a hipótese de viés de formato em Llama 3.2.

Três isolamentos:
  E1) temperature = 0 (determinismo total) — testa se a violação é estocástica.
  E2) few-shot pesado: 1 par user/assistant no contexto mostrando pontos_fortes
      como string monolítica — testa se o viés cede à demonstração explícita.
  E3) curl direto (fora do Python) — fora deste script; ver chamada separada.

Saída: logs/contra_experimento_llama32_resultados.json + sumário no stdout.
"""
import json, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import requests
from prompts import SYSTEM_PROMPT

ROOT = Path(__file__).resolve().parent.parent
OLLAMA = "http://localhost:11434/api/chat"
MODELOS = ["llama3.2:1b", "llama3.2:3b"]
SCENARIOS_PATH = ROOT / "data" / "scenarios_canonical_koch.jsonl"


def carregar_cenarios():
    cenarios = []
    for i, line in enumerate(SCENARIOS_PATH.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        d = json.loads(line)
        user = next(m for m in d["messages"] if m["role"] == "user")["content"]
        asst = next(m for m in d["messages"] if m["role"] == "assistant")["content"]
        cenarios.append({"id": i, "user": user, "assistant_gold": asst})
    return cenarios


def diagnosticar(resposta_bruta):
    try:
        p = json.loads(resposta_bruta)
    except json.JSONDecodeError as e:
        return {"conforme": False, "motivo": f"JSON inválido: {e.msg[:30]}", "pf_tipo": None}
    if not isinstance(p, dict):
        return {"conforme": False, "motivo": f"raiz={type(p).__name__}", "pf_tipo": None}
    pf = p.get("pontos_fortes")
    if isinstance(pf, str) and pf.strip():
        pf_tipo = "str_ok"
    elif isinstance(pf, list):
        pf_tipo = f"list[{len(pf)}]"
    elif pf is None:
        pf_tipo = "AUSENTE"
    else:
        pf_tipo = type(pf).__name__
    pr = p.get("perguntas_reflexivas")
    pr_ok = isinstance(pr, list) and len(pr) > 0 and all(isinstance(x, str) for x in pr)
    conforme = (pf_tipo == "str_ok") and pr_ok
    return {"conforme": conforme, "motivo": "OK" if conforme else f"pf={pf_tipo}", "pf_tipo": pf_tipo}


def chamar(modelo, messages, temperature):
    payload = {
        "model": modelo,
        "messages": messages,
        "stream": False,
        "format": "json",
        "options": {"temperature": temperature},
    }
    t0 = time.time()
    r = requests.post(OLLAMA, json=payload, timeout=120)
    r.raise_for_status()
    return {
        "latencia_ms": int((time.time() - t0) * 1000),
        "resposta_ia": r.json()["message"]["content"],
    }


def rodar_experimento(nome, modelo, cenarios, montar_messages, temperature):
    print(f"\n--- {nome} | {modelo} | temp={temperature} | n={len(cenarios)} ---")
    resultados = []
    for c in cenarios:
        try:
            r = chamar(modelo, montar_messages(c), temperature)
            d = diagnosticar(r["resposta_ia"])
            status = "✓" if d["conforme"] else "✗"
            print(f"  cen={c['id']:>2}  {r['latencia_ms']:>5}ms  {status} {d['motivo']}")
            resultados.append({"experimento": nome, "modelo": modelo, "cenario_id": c["id"],
                               **r, **d})
        except Exception as e:
            print(f"  cen={c['id']:>2}  ❌ {e}")
            resultados.append({"experimento": nome, "modelo": modelo, "cenario_id": c["id"], "erro": str(e)})
    n = len(resultados)
    conf = sum(1 for x in resultados if x.get("conforme"))
    print(f"  RESUMO: {conf}/{n} conformes ({100*conf/n:.1f}%)")
    return resultados


def main():
    cenarios = carregar_cenarios()
    cen_fewshot = cenarios[0]                 # cenário 1 vira exemplo few-shot
    cen_teste_fewshot = cenarios[1:]          # avalia nos 12 restantes
    cen_teste_full = cenarios                 # avalia nos 13 para temp=0

    todos = []

    # E1 — temperature=0 nos 13 cenários
    def msgs_baseline(c):
        return [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": c["user"]},
        ]
    for modelo in MODELOS:
        todos += rodar_experimento("E1_temp0", modelo, cen_teste_full, msgs_baseline, 0.0)

    # E2 — few-shot pesado (1 demo no histórico) com temperatura padrão 0.2
    def msgs_fewshot(c):
        return [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": cen_fewshot["user"]},
            {"role": "assistant", "content": cen_fewshot["assistant_gold"]},
            {"role": "user", "content": c["user"]},
        ]
    for modelo in MODELOS:
        todos += rodar_experimento("E2_fewshot", modelo, cen_teste_fewshot, msgs_fewshot, 0.2)

    # E2b — few-shot + temp=0 (combinação mais forte)
    for modelo in MODELOS:
        todos += rodar_experimento("E2b_fewshot_temp0", modelo, cen_teste_fewshot, msgs_fewshot, 0.0)

    out = ROOT / "data" / "results" / "counter_experiment_llama32.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(todos, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nsaved {out} ({len(todos)} calls)")


if __name__ == "__main__":
    main()
