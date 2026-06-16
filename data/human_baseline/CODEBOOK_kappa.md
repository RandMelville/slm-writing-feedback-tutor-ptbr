# Codebook — codificação para o cálculo de concordância (Cohen's κ)

Manual de codificação das respostas de tutoria (humanas ou de modelos) usado para
estimar a confiabilidade entre codificadores e validar a métrica automática da RQ2.
Responde aos quatro pontos solicitados: categorias (a), derivação teórica (b),
unidade de análise (c) e avaliadores (d).

---

## 1. Unidade de análise (c)

A unidade é a **devolutiva completa de um avaliador a um cenário** — a resposta
inteira (pontos fortes + perguntas/comentários), tomada como um todo. Não se
fragmenta a resposta em sentenças ou fenômenos isolados.

**Justificativa teórica:** na Linguística Textual (Koch), os fatores de textualidade
não operam isoladamente; a produção de sentido resulta da interação entre eles.
Atomizar a devolutiva contrariaria esse pressuposto. Além disso, a devolutiva
completa é a unidade real de uso na plataforma (um retorno por texto de aluno).

Cada unidade recebe **um código em cada uma das duas dimensões** abaixo. As
dimensões são independentes.

---

## 2. Categorias analíticas (a) e sua derivação (b)

### Dimensão A — Foco do retorno  *(derivada de Koch / Linguística Textual)*

O que a devolutiva toma como **objeto** principal.

| Código | Rótulo | Definição |
|---|---|---|
| **A1** | Textual-metalinguístico | Trata um fenômeno de **textualidade tal como opera no texto do aluno**: coesão (repetição, retomada pronominal, conectivos, elipse, substituição lexical), coerência/progressão (sequência temporal ou lógica, contradição), referenciação. O texto do aluno é tratado como **objeto linguístico**. |
| **A2** | Temático-conteudístico | Engaja com o **conteúdo / a obra / o tema**: comenta o enredo, a interpretação, acrescenta informação sobre a obra — sem tratar de como o texto está construído. |
| **A3** | Normativo-pontual | Foca em **ortografia, acentuação, pontuação ou morfologia isoladas**, na superfície, sem tratar de textualidade. |

*Derivação (b):* A1 operacionaliza a rubrica metalinguística de Koch no nível do
fenômeno (não da mera ocorrência de um vocábulo). A separação A1/A2 é exatamente o
achado da RQ2: aderência estrutural com **superfície temática** versus tratamento
metalinguístico.

**Regra de decisão:** classifique pelo foco **predominante** (por extensão/peso).
Empate genuíno é registrado e resolvido pela adjudicação (ver §4).

### Dimensão B — Natureza da mediação  *(derivada de Vygotsky / scaffolding)*

**Como** a devolutiva intervém. **Agnóstica à forma**: uma pergunta não é, por si,
"melhor" que uma afirmação.

| Código | Rótulo | Definição |
|---|---|---|
| **B1** | Mediadora | Oferece **apoio orientado ao avanço do aluno**: pergunta que leva à descoberta, pista, modelagem de estratégia, explicitação de um padrão/convenção, orientação de gênero ou de norma. **Inclui** instrução direta quando ela apoia o desenvolvimento (ex.: *"em textos formais costuma-se evitar repetir o nome usando pronomes — veja onde isso caberia no seu texto"*). |
| **B2** | Avaliativa-terminal | Apenas **julga** ou **entrega a correção pronta**, sem habilitar o aluno a avançar (ex.: *"está repetitivo"*, *"troque X por Y"*, *"seu texto está bom"*). Veredito ou solução fechada, sem andaime. |
| **B3** | Ausente | Não há intervenção pedagógica acionável: só reformula/elogia genericamente, não aponta caminho, ou foge da tarefa. |

*Derivação (b):* o critério vygotskiano é a contribuição para o avanço na Zona de
Desenvolvimento Proximal, **não a forma** da intervenção. Por isso B1 abarca pergunta
*e* instrução direta; e uma pergunta vazia/retórica pode ser B3.

**Regra de decisão:** classifique pela **função predominante** da resposta inteira.
Não conte "tem pergunta logo é B1": avalie se a intervenção habilita o avanço.

> **Independência das dimensões (intencional):** uma resposta pode ser A1+B2 (fala de
> coesão mas só entrega a correção) ou A2+B1 (medeia bem, mas sobre o conteúdo, não a
> textualidade). É essa independência que separa *aderência de formato* de *adequação
> pedagógica*.

---

## 3. Métrica automática como proxy (limite da heurística)

O *scorer* automático (`src/metalinguistic_adherence.py`) detecta apenas a presença
de termos da taxonomia de Koch. Ele é, portanto, um **proxy de triagem somente da
Dimensão A** (aproximadamente A1 vs. não-A1) e **não diz nada sobre a Dimensão B**.
Isso é declarado explicitamente no paper.

---

## 4. Avaliadores e procedimento (d)

- **Dois codificadores humanos** especialistas em Língua Portuguesa (EFII),
  **independentes** e **cegos** quanto à origem de cada resposta (humana ou qual
  modelo) e quanto à codificação um do outro.
- Ambos aplicam **este codebook** às mesmas unidades.
- A **especialista que elaborou os cenários** atua como **adjudicadora** (terceira
  decisão) em caso de divergência — **não** como um dos dois codificadores primários,
  para evitar circularidade.
- Dado o corpus reduzido (13 cenários), codifica-se **100% das respostas** do(s)
  modelo(s) validado(s), não uma amostra.

### O que se reporta

1. **κ humano–humano**, por dimensão (Cohen's κ, nominal de 3 categorias, não
   ponderado), com concordância observada, IC 95% e banda de Landis & Koch (1977).
2. **Concordância heurística–consenso humano**, apenas na Dimensão A colapsada em
   binário (A1 vs. não-A1) — validação do critério de triagem automático.

Referências de interpretação: Landis & Koch (1977); Cohen (1960); Artstein & Poesio
(2008). Reportar a convenção de cobertura como convenção, não como regra.
