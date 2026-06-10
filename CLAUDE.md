# CLAUDE.md — Projeto Bento (Benchmark + Modelo)

> Memória de trabalho para assistentes Claude operando neste diretório.
> Pesquisador: Randerson Melville Rebouças (UFRGS) — randerson.melville@gmail.com
> Última revisão: 2026-05-25 — benchmark concluído, paper em EN, contra-experimento Llama 3.2 executado e integrado (§5.3 do paper), Fisher exact rodado (§5.4 do paper), reorganização do repo para padrão de publicação aberta concluída. Estrutura pública atual em §2.

---

## 1. Separação de escopo: Tese vs. Bento

Há **dois projetos distintos** que se alimentam, mas não se misturam:

| | **Tese — Plataforma Criativa** | **Bento (este diretório)** |
|---|---|---|
| Onde | Programa de doutorado UFRGS | `/Users/randersonmelville/Documents/doutorado/slm-socratic-tutor-ptbr/` (pasta renomeada de `bento/` em 2026-06-10 p/ casar com o repo GitHub; "Bento" permanece o codinome do modelo fine-tuned futuro) |
| Entregável | Plataforma educacional + tese acadêmica | Benchmark + modelo no Hugging Face (apoio do piloto) |
| Foco | Pedagogia, Linguística Textual (Koch), Pensamento Computacional, design da plataforma | Engenharia de LLM: benchmark de open-source + fine-tuning de tutor socrático |
| Público | Banca + comunidade educacional | Comunidade ML/NLP + escolas-piloto |
| Status | CEP aprovado, protótipo + RSL em construção, piloto 2026.2, aplicação 2027 | Smoke test do LoRA OK; benchmark parcial; dataset em 13 seeds |

Quando o usuário falar em "artigo", "modelo", "fine-tuning", "dataset", "benchmark", "adapter" → escopo **Bento**.
Quando falar em "tese", "plataforma", "aluno", "professora", "andaime cognitivo" no plano conceitual → escopo **Tese** (este diretório só guarda o que vira insumo para o Bento).

### Restrições não-negociáveis do Bento

- **Bento é apoio da tese**, não fim em si. Não pode consumir 100% do tempo do pesquisador, que tem RSL + protótipo + piloto da tese em paralelo.
- **Hardware-alvo: escola pública brasileira** (CPU ou GPU modesta, ~8 GB RAM). Modelos 7B-9B estão fora do deploy final. Mirar 1B-3B.
- **Deadline real: piloto 2º semestre de 2026.** Aplicação em sala em 2027.
- **CEP da tese já aprovado** — coleta de redações reais de alunos via UFRGS não está bloqueada por ética.
- **Dois papers, dois tempos:**
  - **(1) Benchmark de modelos open-source ≤3B em PT-BR para tutoria socrática (Koch)** — escrito em 2026; duplo propósito de **publicação** (workshop PROPOR/STIL/BEA) E **decisão empírica** do modelo-base do piloto 2026.2.
  - **(2) Bento paper** — apresentação do modelo fine-tuned em redações reais coletadas pelo piloto, 2027+.
  - O Bento (2027) cita o benchmark (2026); o benchmark NÃO depende do Bento. ~80% do texto do paper vira capítulo de metodologia da tese — esforço amortizado.

---

## 2. Estado atual dos artefatos (pós-reorganização 2026-05-25)

A pasta foi reorganizada em **dois espaços disjuntos**:

### 2.1 Repo público do benchmark (raiz)

Estrutura adequada para git público + reprodução em quatro comandos. Tudo aqui é citável e licenciável (código MIT, dados+paper CC-BY 4.0).

```
README.md, LICENSE, LICENSE-DATA, CITATION.cff, requirements.txt, .gitignore
CLAUDE.md (este arquivo, fica em PT-BR para uso interno)

paper/
  artigo_benchmark_slm.md   # paper em EN, 380+ linhas, §§3-7 com inferencial
  artigo_benchmark_slm.pdf  # regenerado via md_to_pdf.py
  md_to_pdf.py
  references_inventory.txt  # ex-referencias_literatura_escola.txt

src/                        # todos os scripts em src/, paths via ROOT
  benchmark_local.py        # driver da coleta (CLI argparse)
  counter_experiment_llama32.py  # protocolo E1/E2/E2b
  mine_benchmark.py         # JSON bruto → CSV plano
  summarize_consolidated.py # tabela + 2 PNGs
  generate_final_report.py  # human_readable_report.txt (EN)
  inferential_statistics.py # Fisher exact em 7 contingências 2×2
  prompts.py                # SYSTEM_PROMPT canônico (Bento preservado, doc no README)

data/
  scenarios_canonical_koch.jsonl   # ex-bento8b_dataset_final.jsonl
  human_readable_report.txt        # regenerado em EN
  results/
    round_1_main_models.json       # ex-resultados_benchmark_consolidado.json
    round_2_complementary_models.json   # ex-resultados_modelos_restantes.json
    counter_experiment_llama32.json     # 74 chamadas do contra-experimento
    counter_experiment_llama32.log

analises/
  benchmark_flat.csv
  inferential_results.json
  latencia_media.png
  throughput_tokens.png
```

### 2.2 `_privado_modelo_futuro/` (ignorado pelo .gitignore, fica fora do repo)

Tudo que pertence ao projeto-modelo (Bento pós-FT), não ao benchmark:
- `adapters/` (LoRA smoke test, 11 MB)
- `bento_train_data/`
- `inferencia_adapter.py`, `expand_dataset.py`
- `Diario_Bento8B_Framework_MLX.txt`, `data_pipeline/`
- `logs/sanity_check_2026_05_22.md`, `logs/track_a_2026_05_22.md`
- `proxima_sessao_pesquisa.md`

Quando retomar o trabalho de fine-tuning depois do piloto, esse espaço vira o repo separado do modelo Bento.

### 2.3 Decisões registradas nesta reorganização

- **Idioma:** paper, README e código em EN; CLAUDE.md e dossiês internos em PT-BR.
- **"Bento" no SYSTEM_PROMPT** (`src/prompts.py`): preservado verbatim — escolha b1, documentada no README, honra reprodutibilidade dos 388 registros.
- **Estatística inferencial:** somente Fisher exact 2×2, 7 testes (F1-F7), reportados nas §§5.1, 5.2, 5.3 e Tabela 4 (§5.4).
- **Dossiê do orientador:** apagado (incorporado integralmente ao paper como §5.3).
- **Arquivos órfãos** (analise_erros_benchmark.py, resultados_benchmark_brutos.json, contexto_bento.txt, teste_fumaça.json, PNGs antigos de analises/graficos/): descartados.
- **Overleaf:** `.tex` ainda não gerado — requer `brew install pandoc` antes de `pandoc paper/artigo_benchmark_slm.md -o paper/artigo_benchmark_slm.tex --standalone --listings`.

### ⚠️ Lacunas restantes
1. ~~Não existe script de inferência~~ — **resolvido em 2026-05-22** (Track B). Ver `inferencia_adapter.py` + `logs/sanity_check_2026_05_22.md`.
2. ~~**Benchmark cobre 5/13 cenários e modelos do tamanho errado.**~~ — **resolvido em 2026-05-24** (Track E). 8 modelos × 13 cenários × 3 reps = 312 chamadas. Ver §5.0.
3. **Sem logs de treino preservados** — próxima rodada do MLX-LM precisa redirecionar stdout para `logs/run_YYYYMMDD_HHMM.log`.
4. **`SYSTEM_PROMPT` canônico pode precisar de regra 6:** *"Não opine sobre a obra que o aluno cita; foque no texto do aluno."* Achado do sanity check — modelo confundiu "alienista" (título) com personagem grande no cenário 5.

---

## 3. Meta 1 — Paper de Benchmark (deliverable autônomo de 2026)

**Tese empírica do paper:** *modelos open-source ≤3B falham de modos sistemáticos e mensuráveis na rubrica socrática de Koch em PT-BR; entre eles, o modelo X é o menos pior segundo critérios definidos e portanto é o escolhido para rodar no piloto 2026.2.* Modelos 7B-9B (Llama 3 8B, Gemma 2 9B) e proprietários (GPT-4o-mini, Claude Haiku) entram como teto de referência.

**Duplo propósito** — o mesmo trabalho produz (a) paper de workshop e (b) decisão empírica do modelo do piloto. Sem conflito, reforço mútuo.

**Venue alvo:** workshop PROPOR 2026, STIL 2026, ou BEA (NAACL/EMNLP). PT-BR aceito nos brasileiros, EN obrigatório no BEA.

**Componentes do paper:**
1. `analise_erros_benchmark.py` — heurísticas + agregações (estrutura abaixo).
2. Matriz: ~6 modelos ≤3B + 2-4 tetos de referência × 13 cenários × n=3.
3. **Baseline humano** — 2-3 professores de Português EFII respondendo os 13 cenários em formato JSON. Sem isso o paper não passa.
4. Anotação humana de amostra (~20%) → κ de Cohen heurística-vs-humano.
5. Escrita: ~30-60h distribuídas em 2-3 meses.

### Script a criar: `analise_erros_benchmark.py`

```
ENTRADA: resultados_benchmark_brutos.json (e depois resultados_benchmark_hardware_escolar.json)
SAÍDA:   - analises/relatorio_erros.csv     (uma linha por resposta com flags)
         - analises/sumario_por_modelo.json (agregados)
         - analises/graficos/               (PNG: barras, heatmap, boxplot)
```

**Pipeline por resposta (cada item do JSON):**
1. **Validação estrutural** — `resposta_ia` é JSON parseável? Tem `pontos_fortes` e `perguntas_reflexivas`? Esta última é lista com ≥1 item?
2. **Distanciamento pedagógico (falha do Llama 3 no Diário)** — 3ª pessoa ("o aluno") em vez de 2ª ("você") → flag `pessoa_errada`. Tom acadêmico ("demonstra", "habilidade") vs. acolhedor ("legal", "que tal").
3. **Genericidade (falha do Gemma no Diário)** — pergunta reflexiva contém qualquer termo do `foco_teorico`? Se não, flag `nao_aborda_foco_koch`.
4. **Ponte com Pensamento Computacional** — a 2ª pergunta menciona "bloco", "lógica", "Scratch", "fluxo", "comando"? Sem isso, o modelo violou o System Prompt.
5. **Prescritivismo** — verifica linguagem corretiva ("incorreto", "errado", "deveria"): viola "valorize variedades linguísticas".

**Agregação:** taxa de cada flag por modelo; taxa por foco Koch; matriz modelo × foco_koch; latência p50/p95; % de respostas JSON-válidas.

**Validação humana obrigatória:** as heurísticas são *triagem*, não verdade. Anotar manualmente ~20% das respostas e calcular Cohen's κ (concordância inter-anotador heurística-vs-humano). Isso vira "Threats to Validity" no artigo.

---

## 4. Meta 2 (Modelo) — Esteira de expansão do dataset

**Objetivo:** sair de 13 seeds para 200–500 exemplos auditados para um LoRA defensável no modelo-base ≤3B escolhido pelo benchmark.

### Estrutura de pastas proposta

```
bento/
├── data_pipeline/
│   ├── 01_seed/                  # bento8b_dataset_final.jsonl (os 13 originais)
│   ├── 02_synthetic_raw/         # gerados via API (Claude/GPT-4) sem revisão
│   ├── 03_real_raw/              # redações reais coletadas (TXT/PDF/digitalizado)
│   ├── 04_curated/               # após revisão humana + validação JSON
│   ├── 05_augmented/             # paráfrases controladas
│   └── 06_final_splits/          # train/valid/test estratificados (substitui bento_train_data/)
├── scripts/
│   ├── gerar_sinteticos.py       # API → 02_synthetic_raw
│   ├── normalizar_reais.py       # OCR/limpeza → 03_real_raw
│   ├── validar_dataset.py        # JSON schema + checks de Koch
│   ├── augmentar.py              # paráfrase + injeção de erros
│   └── split_estratificado.py    # → 06_final_splits
└── docs/
    ├── DATASETS_PT_BR.md         # mapeamento de datasets públicos
    └── DATASET_CARD.md           # exigido pelo Hugging Face
```

### Fluxo (4 frentes paralelas)

**Frente A — Síntese controlada por API:**
- Gerar 30–50 cenários *por categoria* da taxonomia (incluir além dos 5 focos atuais: coesão lexical por sinonímia/hiperonímia, conectores específicos, coerência local).
- Prompt do gerador recebe: foco teórico, faixa etária (8º-9º ano), tema rotativo, exemplo few-shot de um dos 13 seeds.
- Marcar como `origem: sintetico_claude` no metadado.

**Frente B — Redações reais de estudantes (CEP já aprovado):**
- Dois fluxos em paralelo:
  - **B1 (imediato, sem coleta nova):** Olimpíada "Escrevendo o Futuro" (Cenpec/Itaú), Essay-BR (ENEM, UFMG). Públicos, faixa adequada (B1) ou adjacente (Essay-BR). Ver Track C.
  - **B2 (médio prazo):** coleta via UFRGS/PIBID/escolas do piloto. CEP já aprovado pela tese — destrava o caminho.
- Anonimizar (nomes/escolas), manter erros linguísticos intocados.
- Anotar respostas socráticas com você como ground truth humano — é o que diferencia o Bento de um destilado de Claude.

**Frente C — Augmentation controlado:**
- Paráfrase do `input` (texto do aluno) mantendo o erro de Koch.
- Variação de nomes/contextos (preservar faixa etária e tema escolar).
- NÃO parafrasear o `output` socrático sem revisão — degrada a rubrica.

**Frente D — Split limpo (substitui `bento_train_data/`):**
- Estratificar por `foco_teorico` para valid/test conter todas as categorias.
- **Test set 100% real** (B1 + B2) — congelado, nunca tocado, é a régua oficial.
- Valid set: misto sintético+real.
- Train set: o grosso.

### Formato canônico (manter compatibilidade MLX-LM)

```json
{
  "messages": [
    {"role": "system", "content": "<SYSTEM_PROMPT canônico em prompts.py>"},
    {"role": "user", "content": "<texto do aluno>"},
    {"role": "assistant", "content": "<JSON socrático estrito>"}
  ],
  "_meta": {
    "origem": "sintetico_claude | real_anonimizado | augmentado",
    "foco_koch": "...",
    "ano_escolar": "8|9",
    "revisado_humano": true
  }
}
```
> O `_meta` é descartado no FT mas usado pelos scripts de split/auditoria.

---

## 5. Modelos do benchmark — alvo hardware escolar

### 5.0 Resultados consolidados (2026-05-24) — BENCHMARK CONCLUÍDO

**Pipeline executado com sucesso.** 8 modelos × 13 cenários × 3 reps = 312 chamadas, 0 erros de conexão. Outputs em `resultados_benchmark_consolidado.json` + `resultados_modelos_restantes.json`; relatório fechado em `relatorio_final_benchmark.txt`.

**Tabela unificada (ordenada por latência crescente):**

| Modelo | Latência média (ms) | Tokens out médios | Divergência estrutural |
|---|---:|---:|---:|
| `qwen2.5:1.5b-instruct` | 2.299 | 118,8 | 2,6% (1/39) |
| `llama3.2:1b` | 2.389 | 119,5 | **100% (39/39)** |
| `qwen2.5:3b-instruct` | **2.906** | 104,6 | **0% (0/39)** |
| `llama3.2:3b` | 3.020 | 108,9 | **100% (39/39)** |
| `gemma2:2b` | 3.744 | 121,8 | 2,6% (1/39) |
| `gemma2:9b` | 8.681 | 126,9 | 0% (0/39) |
| `llama3:8b` | 10.523 | 144,7 | 0% (0/39) |
| `phi3:mini` | 14.769 | 471,2 | **100% (39/39)** |

**Achados sistemáticos publicáveis:**

1. **Família Llama 3.2 inteira falha o contrato JSON (100% nos dois tamanhos).** Tanto 1B quanto 3B emitem JSON sintaticamente válido mas retornam `pontos_fortes` como **lista** em vez de **string**. Não é problema de capacidade — é falha arquitetural/tuning de família. Sem grammar coercion (BNF no Ollama) ou few-shot pesado, ambos são não-deployáveis como tutor estruturado.
2. **Phi-3 Mini colapsa em três frentes simultâneas:** 100% divergência + latência 14,7s (5× pior que Qwen 3B, **acima** do limite de 10s pra UX em sala) + verbosidade 4× maior (471 vs ~110-145 tokens). Reforça o argumento de que "instruct-tuning forte em EN" não transfere automaticamente pra PT-BR. Outlier útil pra boxplot do paper.
3. **Surpresa positiva:** `qwen2.5:1.5b-instruct` é o **mais rápido** (2,3s) e quase limpo (2,6%, 1/39). Alternativa secundária pra escolas com hardware ainda mais modesto.

**Modelo-base do piloto 2026.2 decidido empiricamente: `qwen2.5:3b-instruct`.** Justificativa em 4 critérios:
- **Velocidade compatível com sala:** 2,9s médios, ~5× mais rápido que o pior outlier, folgadamente abaixo de 10s.
- **Obediência total ao schema:** 0/39 divergências — único modelo ≤3B com adesão perfeita ao SYSTEM_PROMPT; dispensa grammar coercion no inference.
- **Hardware compatível:** 3B em Q4 ≈ 2 GB RAM. 8-9B viram apenas teto de referência no paper.
- **Margem pro LoRA pedagógico:** com o formato já garantido pelo modelo-base, o adapter pode focar 100% da capacidade na rubrica socrática de Koch (foco teórico, 2ª pessoa, ponte com PC) em vez de gastar parâmetros consertando estrutura — crítico dado dataset ainda enxuto.

---

### 5.1 Planejamento original (preservado para histórico)

A matriz original do `benchmark_local.py` (`llama3:8b`, `gemma2:9b`) era boa pra primeira foto, mas esses tamanhos não são deployáveis em escola pública. Para o artigo/capítulo e para escolher o modelo-base do FT, o benchmark precisa cobrir:

**Faixa deployável (centro do benchmark):**
- `phi3:mini` (3.8B)
- `llama3.2:1b` e `llama3.2:3b`
- `gemma2:2b`
- `qwen2.5:1.5b-instruct` e `qwen2.5:3b-instruct`

**Teto de referência (apenas comparativo):**
- `llama3:8b`, `gemma2:9b` (já testados)
- Opcional: `mistral:7b-instruct`, `qwen2.5:7b-instruct`

**Boas práticas a aplicar:**
1. Rodar **13 cenários** (hoje só 5).
2. **n=3 a 5 execuções por par** modelo×cenário, com temperatura ≥ 0.2, para reportar variância.
3. Salvar como `resultados_benchmark_hardware_escolar.json` separado dos brutos atuais.
4. **Baseline humano**: 2-3 professores respondendo os mesmos cenários no formato JSON. Sem isso, "Bento é melhor que Llama" não tem teto comparativo.
5. **Resultado central:** matriz `modelo × foco_koch` publicável + decisão empírica do modelo do piloto. Bento (fine-tuned em dados reais do piloto, 2027+) é deliverable separado — entra em v2 do paper ou em paper sucessor.

---

## 6. Análise honesta: você está no caminho certo?

**Sim, na espinha dorsal.** O que está bem feito:

- **Benchmarkou antes de treinar.** A maioria dos AI engineers iniciantes pula essa etapa. Você tem `resultados_benchmark_brutos.json` como linha de base.
- **Tem um quadro teórico (Koch) ancorando a avaliação.** A taxonomia vira sua rubrica, e a rubrica vira métrica.
- **Validou o pipeline com smoke test antes do treino real.** Subir tensor, alocar memória unificada, calcular loss sem quebrar — é o que economiza dias depois.
- **Escolheu MLX-LM no Apple Silicon em vez de brigar com CUDA num cluster.** Decisão pragmática.

**O que precisa endurecer (em ordem de impacto):**
1. ~~Vazamento train/valid~~ — corrigido em 2026-05-22.
2. **Dataset de 13 é brinquedo.** Mesmo com LoRA, o modelo memoriza e não generaliza. Frente A+B+C é requisito.
3. **Falta baseline humano** (§5.4). Sem isso, não há teto pra comparar.
4. **Falta script de inferência** — sem ele o adapter atual é inverificável (Track B do plano).
5. **Heurísticas do §3 são frágeis** — use como triagem, mas anote amostra com humano (Cohen's κ).
6. **Documentação científica em paralelo** — `DATASET_CARD.md` + `MODEL_CARD.md` no Hugging Face.

**Próximo salto como AI engineer — três disciplinas a internalizar:**
- **Disciplina de eval** — toda mudança (dataset, hiperparâmetro, modelo-base) medida no mesmo test set congelado. Crie o test set agora e não toque mais nele.
- **Disciplina de versionamento de dados** — `dataset_v1_seed_13.jsonl`, `dataset_v2_synthetic_300.jsonl`. Sem isso, você não consegue responder "esse ganho veio dos dados ou do hiperparâmetro?".
- **Disciplina de reprodutibilidade** — `seed` fixado, `requirements.txt` travado, comando exato do MLX-LM num `Makefile`/`justfile`, logs de treino salvos.

Resumo: fundação boa, restrição de hardware reorienta a escolha de modelo-base, próximo gargalo real é dataset (não modelo).

---

## 7. Tarefas imediatas (ordem do plano aprovado em 2026-05-22)

Ver plano completo em `~/.claude/plans/antes-de-prossugir-para-delegated-metcalfe.md`.

### Mapa dos deliverables (cronograma vivo)

| Deliverable | Quando | Depende de | Status |
|---|---|---|---|
| **Paper de Benchmark** | 2026 (workshop) | Tracks A + E + baseline humano + escrita | Dados completos (Track E ✅); falta baseline humano + escrita |
| **Modelo do piloto** (open-source ≤3B, escolhido pelo benchmark) | 2026.2 | Conclusão da Track E | ✅ Decidido em 2026-05-24: `qwen2.5:3b-instruct` (§5.0) |
| **Bento (modelo fine-tuned)** | 2027+ | Redações reais do piloto + Track D + FT (Track F) | Dataset 13 → 200-500 ainda pendente |
| **Bento paper** | 2027+ | Bento treinado + avaliado em test set congelado | — |

**Track 0 (bloqueante, em execução):** higiene + memória + correção valid.jsonl + este CLAUDE.md.

**Tracks paralelos após T0:**
- **A** — `analise_erros_benchmark.py` → primeiros números pro artigo/capítulo.
- **B** — `prompts.py` + `inferencia_adapter.py` → verificar o adapter atual end-to-end (lacuna nova).
- **C** — `docs/DATASETS_PT_BR.md` → mapear datasets PT-BR públicos antes de construir esteira.

**Sequenciais após paralelos:**
- **D** (depende de C.3) — estrutura `data_pipeline/` + esqueletos + `validar_dataset.py`.
- **E** ~~(depende de A) — rebenchmark com modelos ≤3B + n=3 + 13/13 cenários.~~ ✅ **Concluída em 2026-05-24.** Ver §5.0.

**Fase 2 (NÃO executar agora):**
- **F** — FT real em modelo deployable. Pré-requisitos: dataset ≥200 linhas auditadas (D), modelo-base escolhido por evidência (E), test set 100% real congelado.

**Critério de "pronto para o piloto 2026.2":**
1. Modelo-base ≤3B identificado com evidência do benchmark.
2. Adapter LoRA com inferência reproduzível em ≤8 GB RAM.
3. Test set 100% real congelado, com baseline humano.
4. `DATASET_CARD.md` e `MODEL_CARD.md` mínimos preenchidos.

---

## 8. Convenções de sessão

**Pedagogia (importante — afeta TODO trabalho neste diretório):**
- Antes de cada track/feature/script, gastar 3-5 frases explicando o **porquê** — qual conceito de AI engineering está em jogo, por que essa decisão e não outra.
- Implementar em pedaços auditáveis (não dump de 500 linhas).
- Cada entrega termina com verificação observável que o usuário consegue rodar.
- Iteração curta vence sessão longa: uma coisa, valida, próxima.
- Fechar com 1 frase de "o que se aprendeu de transferível".

**Operação:**
- Idioma de trabalho: português (código em inglês quando padrão da comunidade ML pedir; comentários e docs em PT-BR).
- Não rodar fine-tuning real sem confirmação explícita (consome bateria/tempo).
- Não chamar APIs pagas (Claude/GPT-4) sem confirmação — o usuário decide quando "queimar" tokens.
- Preferir stdlib + `pandas`/`matplotlib` para análise; reservar dependências pesadas (`sentence-transformers`, `datasets`) para quando justificado.
- Logs de treino do MLX-LM: sempre redirecionar para arquivo (`tee logs/run_YYYYMMDD_HHMM.log`).
