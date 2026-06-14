# Processo do baseline humano (referência especializada)

Documento-guia da coleta do padrão-ouro humano para a RQ2. Resume perfil, base ética,
dados coletáveis, materiais e fluxo de ponta a ponta.

## 1. Por que e para quê

A RQ2 do paper precisa de um **teto comparativo humano**: como professores experientes
responderiam aos 13 cenários. Sem isso, a afirmação "a IA é pedagogicamente superficial
(51,3%)" não tem referência. As respostas humanas servem a dois fins:

1. **Teto da RQ2:** rodar a mesma heurística (`src/metalinguistic_adherence.py`) sobre as
   respostas humanas → esperado bem acima dos 51,3% do Qwen (Fisher exact).
2. **Validação da métrica (κ):** um anotador rotula uma amostra (~20%) das respostas dos
   *modelos* como aderente/não → Cohen's κ heurística-vs-humano → fecha *Threats to
   Validity*.

## 2. Base ética (sem CEP)

O orientador responsável avaliou (2026-06-14) que, **como referência especializada sobre
material sintético**, a atividade **não requer autorização do CEP**. Para permanecer
nesse enquadramento:

- Os professores são **colaboradores especialistas**, não sujeitos de pesquisa.
- Os 13 cenários são **fictícios** (sem aluno real, sem dado pessoal).
- Não se coleta dado pessoal/sensível como variável de pesquisa.
- Não se usa TCLE de pesquisa; usa-se a **carta-convite** (`carta_convite.md`).

## 3. Perfil exigido

- **Obrigatório:** professor(a) de **Língua Portuguesa**, atuando no **EFII (8º–9º ano)**.
- **Desejável:** experiência com redação/produção textual; familiaridade com feedback
  formativo.
- **Quantos:** 2 a 3. Dois é o mínimo (evita idiossincrasia de um só); três permite
  adjudicar divergências.
- A **autora dos cenários** (especialista em Linguística Textual) pode ser anotadora e/ou
  adjudicadora.
- **Por que não qualquer matéria:** a rubrica é metalinguística (Koch); só um especialista
  em língua produz uma referência defensável. Um revisor rejeitaria um painel genérico.

## 4. Dados coletáveis antes de começar (sem CEP)

Via `perfil_anotador.md`, somente **qualificação profissional**, para caracterizar o
painel de forma agregada e anônima no artigo:

- ✅ disciplina, séries em que atua, tempo de experiência, experiência com redação,
  familiaridade com feedback formativo, formação (opcional).
- ❌ NÃO coletar: idade, gênero, raça, opiniões sobre IA como variável, qualquer dado
  sensível.
- Respostas vão ao dataset como **Anotador A/B/C**. Nome (opcional) fica só para
  agradecimento, separado das respostas.

## 5. Materiais entregues (nesta pasta)

1. `carta_convite.md` — convite + termos de colaboração (não é TCLE).
2. `perfil_anotador.md` — ficha de perfil (preenche antes).
3. `INSTRUCOES_ANOTADOR.md` — folha explicativa (papel socrático, o que olhar, exemplo).
4. `template_coleta.md` — os 13 cenários com os dois campos para preencher.

> A folha **não revela** o fenômeno-alvo de cada cenário, de propósito: revelar
> enviesaria o julgamento e destruiria o valor do padrão-ouro.

## 6. Fluxo de ponta a ponta

1. **Recrutar** 2–3 candidatos via PIBID-Letras/UFRGS, escolas do piloto, ou rede da
   autora dos cenários.
2. **Convidar:** enviar `carta_convite.md`. Quem aceitar, preenche `perfil_anotador.md`
   (confirma elegibilidade).
3. **Entregar** `INSTRUCOES_ANOTADOR.md` + `template_coleta.md` (uma cópia por anotador).
   Prazo sugerido: ~1 semana.
4. **Receber** os templates preenchidos.
5. **Serializar** as respostas para JSON no formato `[{cenario_id, resposta_ia}, ...]`
   (uma vez por anotador), salvando como `anotador_A.json`, etc., nesta pasta.
6. **Rodar o teto:** `python3 src/metalinguistic_adherence.py --human data/human_baseline/anotador_A.json`
   para cada anotador; comparar com o Qwen via Fisher.
7. **Rodar o κ:** estender o script para Cohen's κ (a) entre anotadores e (b)
   heurística-vs-humano numa amostra das respostas dos modelos. *(extensão pendente)*
8. **Integrar** no `main.tex`: subseção/linha comparativa na RQ2 + κ na seção Threats to
   Validity; atualizar a descrição agregada do painel.

## 7. Adjudicação de divergências

Com 3 anotadores, usar maioria; empates resolvidos pela autora dos cenários. Com 2,
reportar ambos e, se necessário, uma rodada de discussão para consenso. Em qualquer caso,
o κ **entre** anotadores é reportado antes de qualquer consolidação (mede a confiabilidade
do próprio padrão-ouro).
