"""Variante de conformidade: o prompt EM USO NA PLATAFORMA vs o prompt do artigo.

Motivo. O artigo mede o `SYSTEM_PROMPT` canônico, cuja primeira linha nomeia a
persona ("Você é o Bento, um tutor socrático..."). A plataforma RemidiAção roda a
mesma instrução **sem a persona** (a orientação vetou o rótulo "socrático"), e a
ADR-0019 afirma que "o piloto roda o que foi medido". Estritamente, não roda: a
string difere. Este script fecha essa lacuna medindo as duas condições lado a
lado, na mesma máquina, no mesmo dia, sob os mesmos hiperparâmetros do Apêndice B
do artigo (`temperature = 0.2`, `stream = false`, `format = "json"`, sem coerção
de gramática).

Instrumentos reaproveitados do próprio artigo, e não reescritos:
- conformidade estrutural: o validador `divergente()` (C1–C4, §3.4);
- aderência metalinguística: os stems de Koch de `metalinguistic_adherence.py`.

O prompt da plataforma é **lido do arquivo-fonte dela**, nunca copiado para cá:
uma cópia divergiria em silêncio, que é exatamente o problema que este script
existe para detectar.

Uso:
    python3 src/variant_platform_prompt.py [--reps 3] [--model qwen2.5:3b-instruct]
"""

import argparse
import importlib.util
import json
import re
import time
import unicodedata
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
PLATAFORMA = (
    Path.home() / "Documents" / "doutorado" / "plataforma-remidiacao"
    / "backend" / "app" / "utils" / "prompts.py"
)
CENARIOS = ROOT / "data" / "scenarios_canonical_koch.jsonl"
SAIDA = ROOT / "data" / "results" / "variant_platform_prompt.json"
OLLAMA_URL = "http://localhost:11434/api/chat"


def carregar_prompt_do_artigo() -> str:
    spec = importlib.util.spec_from_file_location("bench_prompts", ROOT / "src" / "prompts.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.SYSTEM_PROMPT


def carregar_prompt_da_plataforma() -> str:
    spec = importlib.util.spec_from_file_location("plat_prompts", PLATAFORMA)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.KOCH_SYSTEM


def carregar_cenarios() -> list[str]:
    """Só o conteúdo do turno `user`, como faz `benchmark_local.py`."""
    saida = []
    for linha in CENARIOS.read_text(encoding="utf-8").splitlines():
        if not linha.strip():
            continue
        d = json.loads(linha)
        saida.append(next(m for m in d["messages"] if m["role"] == "user")["content"])
    return saida


def divergente(resp: str) -> bool:
    """Validador estrutural do artigo (§3.4), copiado de `summarize_consolidated.py`."""
    try:
        d = json.loads(resp or "")
    except Exception:
        return True
    if not isinstance(d, dict):
        return True
    pf, pr = d.get("pontos_fortes"), d.get("perguntas_reflexivas")
    if not (isinstance(pf, str) and pf.strip()):
        return True
    if not (
        isinstance(pr, list)
        and pr
        and all(isinstance(p, str) and p.strip() for p in pr)
    ):
        return True
    return False


def carregar_stems() -> dict:
    spec = importlib.util.spec_from_file_location(
        "adher", ROOT / "src" / "metalinguistic_adherence.py"
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.KOCH_STEMS


def normalizar(texto: str) -> str:
    sem_acento = unicodedata.normalize("NFKD", texto.lower())
    return "".join(c for c in sem_acento if not unicodedata.combining(c))


def mobiliza_rubrica(resp: str, stems: dict) -> bool:
    alvo = normalizar(resp or "")
    return any(s in alvo for s in stems)


def chamar(modelo: str, system: str, conteudo: str, timeout: int = 120) -> dict:
    payload = {
        "model": modelo,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": conteudo},
        ],
        "stream": False,
        "format": "json",
        "options": {"temperature": 0.2},
    }
    t0 = time.time()
    r = requests.post(OLLAMA_URL, json=payload, timeout=timeout)
    latencia = int((time.time() - t0) * 1000)
    r.raise_for_status()
    d = r.json()
    return {
        "latencia_ms": latencia,
        "tokens_output": d.get("eval_count", 0),
        "resposta_ia": d["message"]["content"],
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="qwen2.5:3b-instruct")
    ap.add_argument("--reps", type=int, default=3)
    args = ap.parse_args()

    condicoes = {
        "artigo": carregar_prompt_do_artigo(),
        "plataforma": carregar_prompt_da_plataforma(),
    }
    # A diferença precisa ficar no registro: é o objeto da medição.
    print("Diferença entre as duas strings:")
    a, p = condicoes["artigo"].splitlines()[0], condicoes["plataforma"].splitlines()[0]
    print(f"  artigo     : {a[:100]}")
    print(f"  plataforma : {p[:100]}")
    iguais_no_resto = condicoes["artigo"].split("\n", 1)[1:] == condicoes[
        "plataforma"
    ].split("\n", 1)[1:]
    print(f"  resto idêntico: {iguais_no_resto}\n")

    cenarios = carregar_cenarios()
    stems = carregar_stems()
    registros = []
    for nome, system in condicoes.items():
        for rep in range(1, args.reps + 1):
            for i, conteudo in enumerate(cenarios, 1):
                try:
                    r = chamar(args.model, system, conteudo)
                    r.update(condicao=nome, rep=rep, cenario_id=i, modelo=args.model)
                    r["divergente"] = divergente(r["resposta_ia"])
                    r["mobiliza_koch"] = mobiliza_rubrica(r["resposta_ia"], stems)
                except Exception as exc:  # noqa: BLE001
                    r = {
                        "condicao": nome, "rep": rep, "cenario_id": i,
                        "modelo": args.model, "erro": str(exc),
                        "divergente": True, "mobiliza_koch": False,
                    }
                registros.append(r)
            print(f"  {nome} rep {rep}: {len(cenarios)} chamadas concluídas", flush=True)

    SAIDA.parent.mkdir(parents=True, exist_ok=True)
    SAIDA.write_text(json.dumps(registros, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\n{'condição':<12} {'n':>4} {'conformes':>10} {'%':>7} {'Koch':>6} {'%':>7} {'lat.média':>11}")
    for nome in condicoes:
        rs = [r for r in registros if r["condicao"] == nome]
        conf = sum(1 for r in rs if not r["divergente"])
        koch = sum(1 for r in rs if r["mobiliza_koch"])
        lat = [r["latencia_ms"] for r in rs if "latencia_ms" in r]
        media = sum(lat) / len(lat) if lat else 0
        print(
            f"{nome:<12} {len(rs):>4} {conf:>10} {100*conf/len(rs):>6.1f}% "
            f"{koch:>6} {100*koch/len(rs):>6.1f}% {media:>10.0f}ms"
        )
    print(f"\nbruto em {SAIDA}")


if __name__ == "__main__":
    main()
