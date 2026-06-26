# Processo de análise — Funções de Mediação (2ª leva)

Complemento de `PROCESSO.md`. Aquele documento descreve a **coleta** da referência
especializada; este descreve a **análise** das 65 devolutivas, do corpus bruto até os
resultados do paper (§7, "Specialist Human Reference: A Repertoire of Mediation Functions").

Reorientação de base (Prof. Marcelo, 2026-06-24): o valor do corpus não está na
convergência sobre o erro plantado (circular, por desenho), mas nas **estratégias de
mediação** que os especialistas mobilizam. Daí a taxonomia FM01–FM08.

## 1. Recrutamento e corpus

- **Painel:** 5 professores de Língua Portuguesa (EFII), >10 anos de experiência; dois
  atuam no 8º–9º ano; um é referência nacional em Linguística. Recrutados por carta-convite
  (`carta_convite.md`), enquadramento ético sem CEP (`PROCESSO.md` §2).
- **Tarefa:** cada um respondeu aos mesmos 13 cenários sintéticos → 65 devolutivas, sem
  células faltantes.
- **Consentimento:** uso anônimo sob licença Creative Commons. Quem autorizou identificação
  é nomeado apenas nos *Acknowledgements* do paper; os demais permanecem anônimos.

## 2. Anonimização e rastreabilidade

- Respostas brutas do Google Forms (com a coluna opcional "Nome") **contêm PII** e ficam
  **fora do repositório** (gitignored; arquivadas em `_privado_modelo_futuro/baseline_raw_PII/`).
- O corpus publicável é `data/baseline_humano/respostas_professores.jsonl`, anonimizado por
  código **E1–E5** ("E" de Especialista; mapeamento código↔nome só existe no arquivo PII fora
  do git). Códigos consistentes com o paper.
- Uma célula (E4, cenário 10) está desalinhada (conteúdo do cenário 9, provável erro de
  cópia): sinalizada e isolada de contagens por foco; codificável para FMs.

## 3. Codebook e codificação

- Codebook `analises/codebook_funcoes_mediacao.md` (v0.2). Oito funções FM01–FM08,
  multirrótulo binário por devolutiva, regra de evidência mínima (na dúvida, ausente).
- 1ª passada (anotador 1) embutida e auditável em `analises/fm_coding.py` →
  `analises/codificacao_fm.csv`, `analises/fm_frequencia.png`, `analises/fm_resultados.md`.

## 4. Validação cega e confiabilidade (κ)

- 2º anotador independente e **cego** (Prof. Marcelo, especialista em Educação) codificou
  uma amostra estratificada de 20 devolutivas (4 cenários × 5 professores = 160 decisões
  binárias). Planilha: `analises/codificacao_cega_marcelo.xlsx` (IDs D01–D21, sem nomes).
- **κ de Cohen médio = 0,83** ("almost perfect", Landis & Koch 1977); vetor por função
  reportado. Funções de menor κ: FM02 (0,58) e FM04 (0,45).
- Desacordos **direcionais** (em 100% foi o especialista que marcou função *adicional*),
  concentrados em FM04 (+6) e FM02 (+4) → motivou refino inclusivo dessas duas definições
  na **v0.2** e recodificação de FM02/FM04 sobre as 65 devolutivas.
- Ressalva registrada: κ=0,83 mede a v0.1; o recode v0.2 **não** foi re-cegado na mesma
  amostra (faria *overfit* do teste) → nova passada cega v0.2 é trabalho futuro, não
  pré-requisito para a leitura descritiva.

## 5. Codificação do modelo (modelo × funções de mediação)

- A mesma régua (codebook v0.2, mesma regra) aplicada às **39 saídas do modelo conformante**
  (`qwen2.5:3b-instruct`, 13 cenários × 3 reps), em `analises/fm_coding_model.py` →
  `analises/codificacao_fm_modelo.csv`, `analises/fm_modelo_vs_humano.png`.
- Enquadramento **descritivo**: modelo × funções derivadas da prática (não modelo × professor).
  Sinal informativo está na **ausência** do núcleo corretivo humano (FM02/FM04/FM06), já que
  o formato de saída pré-carrega FM01/FM03.
- Ressalva: passada de codificador único (paralela à v0.2 humana); 2ª passada cega no modelo
  é trabalho futuro.

## 6. Saídas no paper

- §7.2/§7.3: frequência e perfis de mediação por especialista (Tabelas 6 e 7, Figura 1).
- §7.4: confiabilidade κ (Tabela 8).
- §7.5: funções mobilizadas pelo modelo vs. repertório humano (Tabela 9, Figura 2).
- §7.6: papel no estudo e questão editorial em aberto (split A/B resolvido como seção única).
