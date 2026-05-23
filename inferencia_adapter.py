#!/usr/bin/env python3
"""Inferência do adapter LoRA atual contra o Qwen2.5-7B-Instruct.

Dois modos:

    # (a) Query única com texto arbitrário do aluno
    python inferencia_adapter.py --query "Texto do aluno aqui..."

    # (b) Sanity check: itera os 13 seeds e compara com label esperado
    python inferencia_adapter.py --sanity-check

Flags úteis para diagnóstico:

    --no-adapter      Carrega só o modelo base (sem o LoRA), pra comparar
                      lado a lado com a versão fine-tuned.
    --prompt-legado   Força o SYSTEM_PROMPT antigo (que o LoRA viu no
                      treino) em qualquer caso. Útil quando se quer
                      isolar o efeito do FT do efeito do prompt.

Por padrão, o sanity check COM adapter usa o prompt legado (foi o que o
LoRA viu), e SEM adapter usa o prompt canônico de prompts.py. Cada
execução imprime no stderr qual prompt foi usado.
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE_MODEL = "Qwen/Qwen2.5-7B-Instruct"
ADAPTER_PATH = str(ROOT / "adapters")
TRAIN_FILE = ROOT / "bento_train_data" / "train.jsonl"

# SYSTEM_PROMPT que o LoRA atual viu no treino. Preservado APENAS para
# sanity check honesto do adapter salvo em adapters/, que foi treinado
# antes da unificação de prompt (2026-05-22). Não usar em produção — o
# canônico vive em prompts.py.
SYSTEM_PROMPT_LEGADO = (
    "Você é o Bento-8B, um modelo especializado em tutoria socrática "
    "para alunos de escolas públicas (11 a 14 anos). Você nunca dá a "
    "resposta pronta e nunca reescreve o texto corrigido do aluno. "
    "Use linguagem acolhedora, simples e direta. Valorize as variedades "
    "linguísticas e as marcas de oralidade do aluno, sem agir como "
    "policial gramatical. Quando fizer sentido, faça pontes discretas "
    "com o Pensamento Computacional (lógica, sequência, condições). "
    "Responda estritamente em JSON com as chaves 'pontos_fortes' e "
    "'perguntas_reflexivas'."
)


def carregar_modelo(usar_adapter: bool):
    """Importa mlx_lm tardiamente — o load é pesado (vários GB)."""
    from mlx_lm import load
    if usar_adapter:
        print(f"[load] base={BASE_MODEL} + adapter={ADAPTER_PATH}", file=sys.stderr)
        return load(BASE_MODEL, adapter_path=ADAPTER_PATH)
    print(f"[load] base={BASE_MODEL} (sem adapter)", file=sys.stderr)
    return load(BASE_MODEL)


def gerar(model, tokenizer, system_prompt: str, user_text: str,
          max_tokens: int = 400) -> str:
    from mlx_lm import generate
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_text},
    ]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    return generate(
        model, tokenizer, prompt=prompt, max_tokens=max_tokens, verbose=False
    )


def sobreposicao_lexical(label: str, output: str) -> float:
    """Fração das palavras únicas do label que aparecem no output.

    Heurística rasa, só para triagem visual no sanity check. Não substitui
    avaliação semântica (κ humano, embeddings) que entra no Track A.
    """
    tokens_label = set(re.findall(r"\w+", label.lower()))
    tokens_output = set(re.findall(r"\w+", output.lower()))
    if not tokens_label:
        return 0.0
    return len(tokens_label & tokens_output) / len(tokens_label)


def json_parseavel(texto: str) -> bool:
    try:
        json.loads(texto)
        return True
    except (json.JSONDecodeError, TypeError):
        return False


def sanity_check(model, tokenizer, system_prompt: str):
    """Itera os 13 seeds, gera output e compara com label esperado."""
    exemplos = [
        json.loads(linha)
        for linha in TRAIN_FILE.read_text(encoding="utf-8").splitlines()
        if linha.strip()
    ]

    sumario = []
    for i, ex in enumerate(exemplos, 1):
        user_text = ex["messages"][1]["content"]
        label = ex["messages"][2]["content"]
        print(f"\n=== Cenário {i}/{len(exemplos)} ===")
        snippet_user = user_text[:140] + ("..." if len(user_text) > 140 else "")
        print(f"USER: {snippet_user}")

        output = gerar(model, tokenizer, system_prompt, user_text)
        overlap = sobreposicao_lexical(label, output)
        ok_json = json_parseavel(output)
        sumario.append({
            "cenario": i,
            "overlap_lexical": overlap,
            "json_parseavel": ok_json,
        })

        snippet_label = label[:400] + ("..." if len(label) > 400 else "")
        snippet_output = output[:400] + ("..." if len(output) > 400 else "")
        print(f"\nLABEL (esperado, do train.jsonl):\n{snippet_label}")
        print(f"\nOUTPUT (gerado):\n{snippet_output}")
        marca_json = "✓" if ok_json else "✗"
        print(f"\n[overlap_lexical={overlap:.0%}  json_parseavel={marca_json}]")

    print("\n" + "=" * 60)
    print("=== SUMÁRIO SANITY CHECK ===")
    print("=" * 60)
    n = len(sumario)
    parseaveis = sum(1 for s in sumario if s["json_parseavel"])
    overlap_medio = sum(s["overlap_lexical"] for s in sumario) / n
    print(f"Cenários processados: {n}")
    print(f"JSON parseável:       {parseaveis}/{n}")
    print(f"Overlap lexical médio: {overlap_medio:.0%}")
    print()
    print("Como ler esses números:")
    print("  - Overlap alto  (>60%) → LoRA memorizou os seeds. No smoke test")
    print("                            isso é DIAGNÓSTICO (pipeline funciona),")
    print("                            não objetivo de qualidade.")
    print("  - Overlap baixo (<20%) → LoRA mal mexeu nos pesos. Algo na rota")
    print("                            de treino pode ter falhado.")
    print("  - Overlap médio        → Influência parcial. Esperado para 20")
    print("                            iters com rank=8 num modelo 7B.")
    print("  - JSON parseável <100% → Modelo ainda quebra formato em alguns")
    print("                            cenários. Indica que estamos longe da")
    print("                            convergência de formato.")
    print()
    print("Compare rodando o mesmo comando com --no-adapter para ver o que o")
    print("modelo base produz sozinho. Diferença visível = LoRA está fazendo")
    print("algo. Diferença invisível = LoRA inerte (apesar do .safetensors).")


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("--sanity-check", action="store_true",
                    help="Itera os 13 seeds e compara com label esperado")
    ap.add_argument("--query", type=str, default=None,
                    help="Texto do aluno para uma query única")
    ap.add_argument("--no-adapter", action="store_true",
                    help="Carregar só o modelo base (sem o LoRA), para comparar")
    ap.add_argument("--prompt-legado", action="store_true",
                    help="Forçar o SYSTEM_PROMPT antigo em vez do canônico")
    ap.add_argument("--max-tokens", type=int, default=400,
                    help="Limite de tokens gerados por resposta (default 400)")
    args = ap.parse_args()

    if not args.sanity_check and not args.query:
        ap.print_help()
        return 1

    # Decisão de qual prompt usar (impressa pra ficar explícito)
    from prompts import SYSTEM_PROMPT
    if args.prompt_legado:
        system_prompt = SYSTEM_PROMPT_LEGADO
        rotulo = "LEGADO (forçado por --prompt-legado)"
    elif args.sanity_check and not args.no_adapter:
        system_prompt = SYSTEM_PROMPT_LEGADO
        rotulo = "LEGADO (adapter foi treinado com este — sanity check honesto)"
    else:
        system_prompt = SYSTEM_PROMPT
        rotulo = "CANÔNICO (prompts.py)"
    print(f"[prompt] usando: {rotulo}", file=sys.stderr)

    model, tokenizer = carregar_modelo(usar_adapter=not args.no_adapter)

    if args.sanity_check:
        sanity_check(model, tokenizer, system_prompt)
    else:
        print(gerar(model, tokenizer, system_prompt, args.query,
                    max_tokens=args.max_tokens))
    return 0


if __name__ == "__main__":
    sys.exit(main())
