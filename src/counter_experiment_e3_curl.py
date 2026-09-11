"""Isolamento E3 do contra-experimento: camada cliente (curl, fora do Python).

Contexto. O paper descreve quatro isolamentos (E1, E2, E2b, E3) e reporta um total de
80 chamadas. O arquivo `data/results/counter_experiment_llama32.json` contém 74 registros
(E1=26, E2=24, E2b=24): o E3 havia sido executado ad hoc na linha de comando, reportado
apenas de forma qualitativa na Tabela 4 e nunca persistido. Este script reexecuta o E3 de
forma completa e auditável, com os mesmos cenários e o mesmo payload do protocolo
principal, e grava o resultado.

Desenho: 2 modelos x 13 cenarios x 1 repeticao = 26 chamadas, zero-shot,
temperature = 0.2 (o valor do protocolo principal), `format: json`, `stream: false`.
O transporte e o utilitario `curl` invocado via subprocess, sem a biblioteca `requests`
em nenhum ponto do caminho: se a divergencia persistir aqui, a hipotese de interferencia
da camada cliente Python fica falseada.

Saidas:
  data/results/counter_experiment_e3_curl.json
  data/results/counter_experiment_e3_curl.log

Uso: python src/counter_experiment_e3_curl.py
"""
import json
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from counter_experiment_llama32 import carregar_cenarios, diagnosticar  # noqa: E402
from prompts import SYSTEM_PROMPT  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OLLAMA = "http://localhost:11434/api/chat"
MODELOS = ["llama3.2:1b", "llama3.2:3b"]
TEMPERATURA = 0.2
DESTINO = ROOT / "data" / "results" / "counter_experiment_e3_curl.json"
LOG = ROOT / "data" / "results" / "counter_experiment_e3_curl.log"


def chamar_via_curl(modelo, user):
    """POST identico ao do protocolo principal, transportado por curl."""
    payload = {
        "model": modelo,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user},
        ],
        "stream": False,
        "format": "json",
        "options": {"temperature": TEMPERATURA},
    }
    comando = [
        "curl", "--silent", "--show-error", "--max-time", "120",
        "-X", "POST", OLLAMA,
        "-H", "Content-Type: application/json",
        "--data-binary", "@-",
    ]
    t0 = time.time()
    proc = subprocess.run(
        comando,
        input=json.dumps(payload).encode("utf-8"),
        capture_output=True,
        check=True,
    )
    latencia = int((time.time() - t0) * 1000)
    corpo = json.loads(proc.stdout.decode("utf-8"))
    return latencia, corpo["message"]["content"]


def main():
    cenarios = carregar_cenarios()
    registros, linhas_log = [], []

    for modelo in MODELOS:
        for c in cenarios:
            latencia, resposta = chamar_via_curl(modelo, c["user"])
            diag = diagnosticar(resposta)
            registros.append({
                "experimento": "E3_curl",
                "modelo": modelo,
                "cenario_id": c["id"],
                "rep": 1,
                "temperatura": TEMPERATURA,
                "transporte": "curl",
                "latencia_ms": latencia,
                "resposta_ia": resposta,
                "conforme": diag["conforme"],
                "motivo": diag["motivo"],
                "pf_tipo": diag["pf_tipo"],
            })
            linha = f"{modelo:14s} c{c['id']:02d}  conforme={str(diag['conforme']):5s}  {diag['motivo']}"
            print(linha)
            linhas_log.append(linha)

    DESTINO.write_text(json.dumps(registros, ensure_ascii=False, indent=2), encoding="utf-8")

    resumo = ["", "=== resumo E3 (curl) ==="]
    for modelo in MODELOS:
        do_modelo = [r for r in registros if r["modelo"] == modelo]
        divergentes = sum(1 for r in do_modelo if not r["conforme"])
        tipos = sorted({r["pf_tipo"] for r in do_modelo})
        resumo.append(f"{modelo}: divergencia {divergentes}/{len(do_modelo)}  pontos_fortes -> {tipos}")
    resumo.append(f"total de chamadas E3: {len(registros)}")
    for linha in resumo:
        print(linha)

    LOG.write_text("\n".join(linhas_log + resumo) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
