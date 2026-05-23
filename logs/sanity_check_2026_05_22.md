# Sanity Check do LoRA smoke test — 2026-05-22

## Contexto

Primeira verificação end-to-end do adapter salvo em `adapters/` desde o smoke test do MLX-LM. Objetivo: confirmar se o LoRA está agindo (memorizou ou influenciou os pesos) ou se ficou inerte apesar do `.safetensors` salvo.

## Configuração

- **Modelo base:** `Qwen/Qwen2.5-7B-Instruct`
- **Adapter:** `adapters/adapters.safetensors` — LoRA `rank=8, scale=20, dropout=0, 4 layers, lr=1e-5, 20 iters`
- **Prompt usado no sanity check com adapter:** `SYSTEM_PROMPT_LEGADO` (versão curta antiga, foi a que o LoRA viu no treino — comparação honesta exige o mesmo prompt).
- **Prompt usado no sanity check sem adapter:** `SYSTEM_PROMPT` canônico (versão unificada em `prompts.py`).
- **Cenários:** 13 seeds do `bento_train_data/train.jsonl`.
- **Métrica heurística:** overlap lexical (fração de palavras únicas do label que aparecem no output) + validade do JSON.
- **Script:** `inferencia_adapter.py --sanity-check` e `--sanity-check --no-adapter`.

## Resultados quantitativos

| Variante | Overlap lexical médio | JSON parseável | Observação |
|---|---|---|---|
| **Com adapter** (LoRA) | 23% | 13/13 | Influência sutil mas detectável |
| **Sem adapter** (Qwen 7B puro) | 19% | 13/13 | Já entrega JSON válido |
| **Δ (LoRA − base)** | +4 pp | 0 | LoRA age, com intensidade baixa |

Overlap individual por cenário com adapter: 26, 26, 26, 32, 25, 22, 24, 18, 22, 22, 20, 25, 17 — todos na faixa 17-32%, sem outliers.

## Diferenças qualitativas observadas

### Onde o LoRA mudou claramente o output

**Cenário 13 (O Homem Nu):**
- COM adapter: *"A frase 'Sem saída, desceu pelo elevador' é uma ponte acertada com o Pensamento Computacional, pois dá a ideia de sequência e condição..."*
- SEM adapter: *"Você fez um reconto bem interessante! A descrição do café passando ajuda a criar um cenário familiar."*

→ O LoRA aprendeu a forçar a ponte com Pensamento Computacional (regra 5 do prompt legado). Sinal claro de fine-tuning agindo.

**Cenário 4 (crônica do Camilo):**
- COM: *"...várias marcas de oralidade..."*
- SEM: *"...mencionou vários elementos importantes..."*

→ Termo "marcas de oralidade" (vocabulário decorado dos seeds) aparece no LoRA, não no base.

### Onde o LoRA piorou em relação ao base

**Cenário 10 (Cemitério dos Vivos):**
- SEM adapter: *"O uso de conectivos como 'portanto', 'mas', 'embora' e 'assim' ajuda a criar uma narrativa fluída."*
- COM adapter: *"Você fez um esboço da resenha com marcas de oralidade, o que é ótimo."*

→ O base puro fez observação técnica mais alinhada com Koch (nomeou os conectivos!) do que o LoRA, que puxou pro vocabulário decorado.

**Cenário 12 (texto bem-escrito de O Alienista):**
- SEM: *"...como sua abordagem mudou ao longo do tempo."*
- COM: *"Você trouxe uma visão rica sobre a história do Alienista."*

→ Base detecta progressão temporal; LoRA generaliza.

### Achado bônus — modelo opina sobre a obra

No cenário 5 do output COM adapter: *"Pensa no tamanho do alienista. Ele poderia ser uma metáfora..."* — o modelo confundiu **"alienista"** (título da obra) com personagem fisicamente grande. Sintoma de que o base Qwen tem conhecimento limitado de literatura brasileira e improvisa.

## Achados relevantes para o paper de Benchmark (2026)

1. **LoRA com 13 exemplos + 20 iters faz *style transfer* parcial**, não internalização da rubrica de Koch. Aprende formato, tom, vocabulário recorrente; não aprende análise específica de coesão.

2. **O base Qwen 2.5 7B já entrega JSON 100% válido e respostas razoáveis em PT-BR.** Para o piloto, um modelo de prateleira não-fine-tuned já é minimamente utilizável. Reduz urgência de FT antes da hora.

3. **FT precoce pode piorar em algumas dimensões.** O LoRA atual *atrapalha* em cenários onde o base fazia análise técnica (conectivos, marcadores temporais). Argumento publicável: *"fine-tune com pouco dado e poucas iterações pode prejudicar a análise técnica que o base ofereceria gratuitamente"*.

4. **Modelo opina sobre a obra literária e às vezes erra.** Sugere instrução adicional no `SYSTEM_PROMPT` canônico: *"Não opine sobre a obra que o aluno cita; foque no texto do aluno."*

## Conclusão para o pipeline

Pipeline MLX-LM end-to-end validado:
- Adapter carrega ✓
- Mudança detectável em relação ao base ✓
- JSON estável ✓

Smoke test cumpriu seu papel diagnóstico. Próximo LoRA (Track F, 2027+) precisa de:
- Dataset 10-50× maior (200-500 exemplos auditados).
- 200-500 iterações (não 20).
- Modelo-base ≤3B (escolhido pelo benchmark, Track E).
- Dados reais coletados no piloto 2026.2 — não sintéticos.
- Redirecionar stdout do MLX-LM para `logs/run_YYYYMMDD_HHMM.log` durante o treino.
