# Codebook — Funções de Mediação em devolutivas de escrita (8º/9º ano)

> Versão 0.2 — Randerson Melville Rebouças, PPGIE/UFRGS, 24 de junho de 2026.
> Mudança v0.1→v0.2: FM02 e FM04 ampliadas após a rodada de concordância (κ) com o Prof. Marcelo —
> as duas funções de menor κ. Ver nota nas próprias definições e em `fm_resultados.md` §6.
> Taxonomia proposta pelo Prof. Marcelo (FM01–FM08), operacionalizada sobre o corpus de referência especializada.
> Corpus: 5 professores (P1–P5) × 13 cenários = 65 devolutivas. Fonte: `data/baseline_humano/respostas_professores.jsonl`.

---

## Propósito e enquadramento

Este codebook serve para **codificar quais funções de mediação cada especialista mobiliza** ao
devolver um texto a um aluno. Atende à reorientação registrada com o Prof. Marcelo: o valor do
corpus não está no problema identificado (FM02, induzido pelo desenho dos cenários, logo circular), mas
nas **estratégias de mediação não plantadas** — como o especialista formula, quando provoca,
quando modela, quanto andaime oferece.

A codificação é **descritiva**, em chave de mediação (Vygotsky/scaffolding). Não pontua qualidade,
não estabelece "padrão-ouro" e não compara devolutivas humanas com o modelo de linguagem.

## Protocolo de aplicação

- **Unidade de análise:** a devolutiva inteira (uma célula `respondente × cenario`). Não a frase.
- **Rotulagem:** multirrótulo binário — para cada uma das 8 funções, marcar **presente (1)** ou
  **ausente (0)**. Uma mesma devolutiva normalmente aciona várias funções.
- **Regra de evidência mínima (conservadora):** só marcar uma FM como presente quando houver
  trecho textual explícito que a sustente. **Na dúvida, marcar ausente.** Esta regra é o que
  protege a confiabilidade entre anotadores.
- **Span opcional:** ao codificar, anotar (quando viável) o trecho que evidencia cada FM marcada.
  Útil para auditoria; a unidade de decisão continua sendo a presença na devolutiva.
- **Política de texto:** erros de digitação dos professores são preservados verbatim e não
  influenciam a codificação.

## Confiabilidade (κ)

Duas passadas: (1) heurística textual transparente como triagem; (2) anotação humana de uma
amostra. Reporta-se **κ de Cohen por função** (8 valores, cada um binário presente/ausente),
mais média e faixa. Funções com κ baixo sinalizam definição frouxa e voltam para revisão do
codebook antes de qualquer contagem definitiva. Multirrótulo → não existe um κ global único;
o vetor de 8 κ é o resultado honesto.

---

## As oito funções

### FM01 — Reconhecer competência
- **Definição:** afirmar, de forma específica, algo que o aluno **fez bem no texto** (uma escolha,
  uma compreensão, um recurso bem empregado).
- **Inclusão:** o elogio nomeia o que foi bem feito (compreensão do enredo, uso de conectivo,
  organização, vocabulário).
- **Exclusão:** encorajamento genérico voltado ao futuro ("continue se dedicando", "estás no
  caminho certo") **sem** nomear uma competência → isso é FM08, não FM01.
- **Âncora (P5/C1):** *"Parabéns! Você identificou um dos acontecimentos mais importantes do conto:
  a confiança de Camilo nas palavras da cartomante e o desfecho inesperado da história."*
- **Caso-limite (P4/C1):** *"Continue se dedicando, pois já demonstraste compreender a história."* —
  a 2ª oração nomeia uma competência (compreensão) → FM01; o "continue se dedicando" isolado seria
  só FM08.

### FM02 — Nomear o problema
- **Definição:** indicar ao aluno que o texto é inadequado em algum aspecto.
- **Inclusão:** o problema é dito (repetição, pronome ambíguo, conector contraditório, ordem
  embaralhada, períodos curtos justapostos, buraco narrativo). **Inclui também apontar que algo está
  ausente, insuficiente ou não atende ao gênero** — ainda que em tom de convite ("como é uma resenha,
  falta sua opinião"; "as afirmações ficaram genéricas e sem justificativa"). *(Ampliado na v0.2 após
  a rodada de κ: nomear uma insuficiência conta, não só apontar um erro explícito.)*
- **Exclusão:** levar o aluno a *descobrir* o problema por uma pergunta aberta → FM03. Pedir
  reescrita sem indicar o que está inadequado → FM06. Texto-teto elogiado sem apontar insuficiência
  → não marcar.
- **Âncora (P2/C2):** *"Você usou \"ele\" muitas vezes, sem deixar claro a quem se referia o pronome
  a cada vez."*
- **Caso-limite (P1/C3):** *"A palavra \"portanto\" não parece adequada. Por qual palavra você
  poderia substituí-la?"* — "portanto não parece adequada" é FM02; "por qual palavra você poderia
  substituí-la?" é FM03. Mesma devolutiva, duas funções.

### FM03 — Provocar reflexão
- **Definição:** dirigir ao aluno uma pergunta que o leve a reexaminar uma escolha textual própria,
  **sem entregar a resposta**.
- **Inclusão:** pergunta genuinamente aberta sobre o texto do aluno ("O que exatamente te fez rir?",
  "A personagem estava realmente feliz?").
- **Exclusão:** pergunta retórica que já contém a correção dentro de si → conta como FM02 (o
  problema foi nomeado, só que em forma interrogativa).
- **Âncora (P2/C3):** *"O que exatamente te fez rir? Por que o final é chocante? Por que era óbvio
  que ia acontecer aquilo?"*
- **Caso-limite (P1/C10):** *"(se era horrível, o natural seria ele querer sair, então o \"mas\" não
  cabe aqui)"* — embora pareça reflexão, a resposta já está dada no parêntese → FM02, não FM03.

### FM04 — Oferecer pista
- **Definição:** fornecer ajuda concreta em direção à solução **sem reescrever** o texto do aluno.
- **Inclusão:** listar substituições possíveis, conectores, marcadores temporais como repertório a
  usar. **Inclui também indicar o aspecto/conteúdo específico a desenvolver ou a estratégia a seguir**
  ("explique o que você achou das atitudes de X", "retome os conectores", "reler o conto e anotar a
  sequência"). *(Ampliado na v0.2 após a rodada de κ — era a função de menor concordância.)*
- **Exclusão:** apresentar uma frase já reescrita do aluno → FM05. Apenas mandar reescrever sem dar
  o caminho → FM06. **Fronteira com FM03:** a mesma orientação dada **como diretiva** é FM04; dada
  **como pergunta aberta** ("o que você achou das atitudes de X?") é FM03.
- **Âncora (P1/C1):** *"para evitar essa repetição, usar o nome da cartomante, ou usar \"ela\" ou
  \"a mulher\"."*
- **Caso-limite (P5/C4):** *"Você pode utilizar marcadores temporais como: Primeiro... Depois...
  Mais tarde... Finalmente..."* — oferece ferramentas (pista), mas **não** monta a frase do aluno →
  FM04, não FM05.

### FM05 — Modelar parcialmente
- **Definição:** demonstrar a solução com um **exemplo reescrito** (uma frase-modelo, idealmente do
  próprio trecho do aluno).
- **Inclusão:** o especialista escreve um exemplo que materializa o conserto.
- **Exclusão:** apenas nomear palavras/recursos a usar, sem montar o exemplo → FM04.
- **Âncora (P5/C13):** *"Sugestão de ampliação: \"Sem saída, desceu pelo elevador; logo depois,
  percebeu que a confusão só aumentava, pois os moradores começaram a observá-lo com espanto...\""* —
  reescreve a frase do próprio aluno.
- **Caso-limite (P1/C7):** *"Tente usar palavras que indiquem o tempo para unir as frases, como por
  exemplo: \"Assim que abriu a porta, o bonde passou.\""* — é exemplo-modelo (FM05), ainda que não
  seja a frase exata do aluno; a fronteira com FM04 é a presença de uma frase pronta.

### FM06 — Propor revisão
- **Definição:** propor/solicitar explicitamente a **reescrita ou correção** do que já está no texto.
- **Inclusão:** "vamos reescrever", "o texto precisa ser reescrito", "reorganize seguindo a ordem".
- **Exclusão:** desafio de **acrescentar** conteúdo novo (opinião, análise, detalhe) que não estava
  lá → FM07.
- **Âncora (P1/C1):** *"Vamos reescrever esse trecho a partir dessas dicas?!"*
- **Caso-limite (P2/C2):** *"O texto precisa ser reescrito."* — FM06 puro (sem pista, sem modelo);
  útil para mostrar que FM06 pode ocorrer sozinho.

### FM07 — Desafiar ampliação
- **Definição:** desafiar o aluno a ir **além de corrigir** — aprofundar, acrescentar opinião,
  análise, detalhe, reflexão que enriqueçam o texto.
- **Inclusão:** "acrescente sua opinião", "aprofunde sua análise", "desenvolva mais", "desafio para
  a reescrita: acrescentar...".
- **Exclusão:** consertar um problema existente → FM06. Reescrever para o aluno → FM05.
- **Âncora (P5/C1):** *"Desafio para a reescrita: acrescentar uma frase avaliando a história e
  utilizar menos repetições."* (a 1ª metade é FM07; "menos repetições" é FM06.)
- **Caso-limite (P1/C9):** *"O desafio que vou te dar é transformar essas 10 frases em 3 ou 4 frases
  mais longas e conectadas."* — reestruturar o que existe → FM06; só seria FM07 se pedisse conteúdo
  novo. Fronteira a observar de perto na codificação.

### FM08 — Reforçar autonomia
- **Definição:** movimento de fechamento que afirma a **capacidade/agência do aluno** e projeta
  continuidade do trabalho.
- **Inclusão:** "estás no caminho certo", "vamos seguir em frente", "você consegue", convite à
  continuidade.
- **Exclusão:** elogio que nomeia uma competência específica demonstrada no texto → FM01.
- **Âncora (P5/C10):** *"Você teve um ótimo começo! Vamos seguir em frente!"*
- **Caso-limite (P4/C2):** *"Continues te dedicando, pois está no caminho certo."* — afirmação
  prospectiva da capacidade, sem nomear o que foi feito → FM08, não FM01.

---

## Sinalização de qualidade de dados (antes de qualquer contagem)

- **P4 / Cenário 10 — desalinhamento:** a devolutiva fala da "investigação realizada pelo detetive"
  (conteúdo do C9, *O Caso da Borboleta*), não de *Cemitério dos Vivos* (C10). Provável erro de
  cópia. **Isolar esta célula** e, se possível, confirmar com o respondente antes de contar por foco.
  A codificação de FMs pode prosseguir (as funções não dependem do conteúdo correto), mas a célula
  fica marcada.

## Próximos passos após validação deste rascunho

1. Marcelo revisa as definições e os casos-limite (ajustar fronteiras FM04/FM05 e FM06/FM07, que são
   as mais escorregadias).
2. Codificar as 65 devolutivas (heurística → matriz `respondente × cenario × FM`).
3. Anotar amostra à mão e reportar κ por função; refinar definições de baixo κ.
4. Saída descritiva: frequência de cada FM por professor; perfis de mediação; a variação como dado.
