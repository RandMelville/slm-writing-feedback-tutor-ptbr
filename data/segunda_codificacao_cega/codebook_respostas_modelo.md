# Codebook da codificação das respostas do modelo

**Funções de mediação (FM01 a FM08) e foco metalinguístico (MTL) nas devolutivas do `qwen2.5:3b-instruct`**

> **Versão 0.2-Q**, 29 de julho de 2026. Randerson Oliveira Melville Rebouças, PPGIE/UFRGS.
> Taxonomia FM01 a FM08 proposta pelo Prof. Marcelo Magalhães Foohs.
> Objeto desta rodada: **39 devolutivas geradas pelo modelo `qwen2.5:3b-instruct`** (13 cenários canônicos, 3 repetições cada).
> Instrumento de acompanhamento: `GUIA_2a_CODIFICACAO.pdf` (procedimento) e `codificacao_cega_v02.xlsx` (planilha).

---

## 0. O que este documento é

Este é o instrumento conceitual da **segunda codificação cega**, aquela pedida pelos revisores A e C do JBCS. Ele **substitui**, para esta rodada, o `codebook_funcoes_mediacao.pdf` (v0.2), que foi escrito em junho para o corpus dos cinco professores e circulou junto com o Guia de 27 de julho.

O que mudou em relação àquele documento:

| | v0.2 (junho) | v0.2-Q (este) |
|---|---|---|
| Objeto codificado | 65 devolutivas de 5 professores humanos | 39 devolutivas do modelo `qwen2.5:3b-instruct` |
| Variáveis | FM01 a FM08 | FM01 a FM08 **e MTL** |
| Definições das 8 FMs | (originais) | **idênticas, sem alteração de substância** |
| Referências à rodada humana | E1 a E5, sinalização E4/C10, próximos passos | removidas |

As **definições, inclusões, exclusões e casos-limite das oito funções são as mesmas da v0.2**, preservadas deliberadamente: é sobre elas que o κ desta rodada será calculado, e alterá-las agora invalidaria a comparação com a rodada de junho. Os ajustes são de enquadramento (qual é o objeto, qual é a unidade) e de escopo (entra a variável MTL). Onde a redação foi tocada, foi só pontuação.

As **âncoras e casos-limite continuam vindo do corpus dos professores**, e isso é intencional: foram esses exemplos que calibraram as definições na rodada de junho, e trocá-los por exemplos novos descalibraria o instrumento no meio da série. Eles aparecem aqui apenas como fixadores de sentido, sem identificação de respondente, e **não fazem parte do material a codificar**.

---

## 1. Objeto e corpus

O material a codificar são as saídas do modelo `qwen2.5:3b-instruct`, o único modelo da faixa implantável (até 3,8 bilhões de parâmetros) que cumpriu integralmente o contrato estrutural do benchmark em regime *zero-shot*.

**O corpus tem 13 cenários, cada um submetido ao modelo três vezes, totalizando 39 respostas.**

Isso precisa ficar explícito porque tem consequência direta sobre a codificação:

- **Não são 39 cenários independentes.** São 13 observações repetidas três vezes cada. A planilha traz uma resposta por linha exatamente porque a decisão de codificação é por resposta, mas a unidade amostral da análise é o cenário, e o tratamento estatístico disso (intervalo de Wilson, correlação intraclasse, *bootstrap* por cluster) fica comigo, não com o anotador.
- **Respostas parecidas vão aparecer.** Três execuções do mesmo cenário podem produzir devolutivas próximas, às vezes quase idênticas em algum trecho. Isso é esperado e é o próprio dado.
- **Cada linha é codificada por si.** Não se deve tentar identificar quais linhas são repetições de um mesmo cenário, nem harmonizar a codificação entre elas. A (in)consistência entre repetições é justamente um dos resultados a medir; forçá-la na codificação destruiria a medida.
- **A ordem está embaralhada** por procedimento determinístico e auditável (`build_pacote_cego.py`, semente fixa). A chave de decegamento e a codificação da primeira passada ficam fora do material entregue.

Uma característica do corpus que vale conhecer de antemão: estas devolutivas são **curtas**, bem mais curtas que as dos professores. Na primeira passada, mobilizam 1,7 funções em média, contra 3,8 das humanas. Linhas com poucas funções marcadas, ou com apenas uma, são normais aqui.

---

## 2. Unidade de análise e regras de decisão

- **Unidade de análise: a devolutiva integral do modelo.** Ou seja, todo o conteúdo da coluna `Devolutiva` de uma linha, tomado como um objeto único: o parágrafo de reconhecimento e as perguntas reflexivas juntos. Não a frase, não o campo isolado, não a pergunta isolada.
- **Rotulagem: multirrótulo binário.** Para cada uma das oito funções e para a MTL, marcar **presente (1)** ou **ausente (0)**. Uma mesma devolutiva pode acionar várias funções, e frequentemente aciona.
- **Regra de evidência mínima (conservadora):** só marcar uma variável como presente quando houver trecho textual explícito que a sustente. **Na dúvida, marcar ausente.** Esta regra é o que protege a confiabilidade entre anotadores, e vale igualmente para as FMs e para a MTL.
- **Basta um trecho.** Se qualquer parte da devolutiva satisfaz o critério, a variável é 1. Não se exige que a devolutiva inteira faça aquilo.
- **Span opcional:** quando viável, anotar em `Observações` o trecho que evidencia a marcação. Útil para auditoria; a unidade de decisão continua sendo a presença na devolutiva.
- **Política de texto:** o texto do modelo é preservado *verbatim*. Eventuais erros, truncamentos ou estranhezas de formatação não influenciam a codificação.
- **O texto do aluno é contexto, não é codificado.** Ele está na planilha para que a devolutiva possa ser interpretada (por exemplo, para saber se um elogio se refere a algo que de fato está no texto), mas as marcações descrevem apenas a devolutiva.
- **A codificação é descritiva.** Não pontua qualidade, não estabelece padrão-ouro, não compara a devolutiva do modelo com a de nenhum professor. Marcar o que está lá, não o que falta.

### Duas passadas, não uma

**Preencher FM01 a FM08 nas 39 linhas primeiro. Só depois voltar ao começo e preencher a coluna MTL.**

FM02 e MTL são vizinhas conceituais, e decidir as duas na mesma leitura faz uma arrastar a outra. Como as duas colunas alimentam análises diferentes (confiabilidade da codificação das FMs, de um lado; validade de construto da métrica da RQ2, de outro), os julgamentos precisam ser independentes. Um intervalo entre as duas passadas melhora a independência.

---

## 3. As oito funções de mediação

Definições idênticas às da v0.2. As âncoras e casos-limite vêm do corpus de referência especializada (as 65 devolutivas dos professores), e servem só para fixar o sentido da definição.

### FM01. Reconhecer competência

- **Definição:** afirmar, de forma específica, algo que o aluno **fez bem no texto** (uma escolha, uma compreensão, um recurso bem empregado).
- **Inclusão:** o elogio nomeia o que foi bem feito (compreensão do enredo, uso de conectivo, organização, vocabulário).
- **Exclusão:** encorajamento genérico voltado ao futuro ("continue se dedicando", "estás no caminho certo") **sem** nomear uma competência, isso é FM08 e não FM01.
- **Âncora:** *"Parabéns! Você identificou um dos acontecimentos mais importantes do conto: a confiança de Camilo nas palavras da cartomante e o desfecho inesperado da história."*
- **Caso-limite:** *"Continue se dedicando, pois já demonstraste compreender a história."* A segunda oração nomeia uma competência (compreensão), logo FM01; o "continue se dedicando" isolado seria só FM08.

### FM02. Nomear o problema

- **Definição:** indicar ao aluno que o texto é inadequado em algum aspecto.
- **Inclusão:** o problema é dito (repetição, pronome ambíguo, conector contraditório, ordem embaralhada, períodos curtos justapostos, buraco narrativo). **Inclui também apontar que algo está ausente, insuficiente ou não atende ao gênero**, ainda que em tom de convite ("como é uma resenha, falta sua opinião"; "as afirmações ficaram genéricas e sem justificativa"). *(Ampliado na v0.2 após a rodada de κ: nomear uma insuficiência conta, não só apontar um erro explícito.)*
- **Exclusão:** levar o aluno a *descobrir* o problema por uma pergunta aberta, isso é FM03. Pedir reescrita sem indicar o que está inadequado, isso é FM06. Texto elogiado sem apontar insuficiência, não marcar.
- **Âncora:** *"Você usou 'ele' muitas vezes, sem deixar claro a quem se referia o pronome a cada vez."*
- **Caso-limite:** *"A palavra 'portanto' não parece adequada. Por qual palavra você poderia substituí-la?"* O trecho "portanto não parece adequada" é FM02; "por qual palavra você poderia substituí-la?" é FM03. Mesma devolutiva, duas funções.

### FM03. Provocar reflexão

- **Definição:** dirigir ao aluno uma pergunta que o leve a reexaminar uma escolha textual própria, **sem entregar a resposta**.
- **Inclusão:** pergunta genuinamente aberta sobre o texto do aluno ("O que exatamente te fez rir?", "A personagem estava realmente feliz?").
- **Exclusão:** pergunta retórica que já contém a correção dentro de si, conta como FM02 (o problema foi nomeado, só que em forma interrogativa).
- **Âncora:** *"O que exatamente te fez rir? Por que o final é chocante? Por que era óbvio que ia acontecer aquilo?"*
- **Caso-limite:** *"(se era horrível, o natural seria ele querer sair, então o 'mas' não cabe aqui)"*. Embora pareça reflexão, a resposta já está dada no parêntese, logo FM02 e não FM03.
- **Nota específica deste corpus:** pergunta sobre o **enredo, os personagens ou o tema da obra literária** citada pelo aluno não é FM03, porque não devolve ao aluno nenhuma escolha textual própria para reexaminar. Este é o caso mais frequente nas devolutivas do modelo e merece atenção redobrada na passada das FMs.

### FM04. Oferecer pista

- **Definição:** fornecer ajuda concreta em direção à solução **sem reescrever** o texto do aluno.
- **Inclusão:** listar substituições possíveis, conectores, marcadores temporais como repertório a usar. **Inclui também indicar o aspecto ou conteúdo específico a desenvolver, ou a estratégia a seguir** ("explique o que você achou das atitudes de X", "retome os conectores", "reler o conto e anotar a sequência"). *(Ampliado na v0.2 após a rodada de κ, era a função de menor concordância.)*
- **Exclusão:** apresentar uma frase já reescrita do aluno, isso é FM05. Apenas mandar reescrever sem dar o caminho, isso é FM06. **Fronteira com FM03:** a mesma orientação dada **como diretiva** é FM04; dada **como pergunta aberta** ("o que você achou das atitudes de X?") é FM03.
- **Âncora:** *"para evitar essa repetição, usar o nome da cartomante, ou usar 'ela' ou 'a mulher'."*
- **Caso-limite:** *"Você pode utilizar marcadores temporais como: Primeiro... Depois... Mais tarde... Finalmente..."* Oferece ferramentas (pista), mas **não** monta a frase do aluno, logo FM04 e não FM05.

### FM05. Modelar parcialmente

- **Definição:** demonstrar a solução com um **exemplo reescrito** (uma frase-modelo, idealmente do próprio trecho do aluno).
- **Inclusão:** o interlocutor escreve um exemplo que materializa o conserto.
- **Exclusão:** apenas nomear palavras ou recursos a usar, sem montar o exemplo, isso é FM04.
- **Âncora:** *"Sugestão de ampliação: 'Sem saída, desceu pelo elevador; logo depois, percebeu que a confusão só aumentava, pois os moradores começaram a observá-lo com espanto...'"*, que reescreve a frase do próprio aluno.
- **Caso-limite:** *"Tente usar palavras que indiquem o tempo para unir as frases, como por exemplo: 'Assim que abriu a porta, o bonde passou.'"* É exemplo-modelo (FM05), ainda que não seja a frase exata do aluno; a fronteira com FM04 é a presença de uma frase pronta.

### FM06. Propor revisão

- **Definição:** propor ou solicitar explicitamente a **reescrita ou correção** do que já está no texto.
- **Inclusão:** "vamos reescrever", "o texto precisa ser reescrito", "reorganize seguindo a ordem".
- **Exclusão:** desafio de **acrescentar** conteúdo novo (opinião, análise, detalhe) que não estava lá, isso é FM07.
- **Âncora:** *"Vamos reescrever esse trecho a partir dessas dicas?!"*
- **Caso-limite:** *"O texto precisa ser reescrito."* FM06 puro, sem pista e sem modelo, o que mostra que FM06 pode ocorrer sozinho.

### FM07. Desafiar ampliação

- **Definição:** desafiar o aluno a ir **além de corrigir**: aprofundar, acrescentar opinião, análise, detalhe, reflexão que enriqueçam o texto.
- **Inclusão:** "acrescente sua opinião", "aprofunde sua análise", "desenvolva mais", "desafio para a reescrita: acrescentar...".
- **Exclusão:** consertar um problema existente, isso é FM06. Reescrever para o aluno, isso é FM05.
- **Âncora:** *"Desafio para a reescrita: acrescentar uma frase avaliando a história e utilizar menos repetições."* A primeira metade é FM07; "menos repetições" é FM06.
- **Caso-limite:** *"O desafio que vou te dar é transformar essas 10 frases em 3 ou 4 frases mais longas e conectadas."* Reestruturar o que existe é FM06; só seria FM07 se pedisse conteúdo novo. Fronteira a observar de perto.

### FM08. Reforçar autonomia

- **Definição:** movimento de fechamento que afirma a **capacidade ou agência do aluno** e projeta continuidade do trabalho.
- **Inclusão:** "estás no caminho certo", "vamos seguir em frente", "você consegue", convite à continuidade.
- **Exclusão:** elogio que nomeia uma competência específica demonstrada no texto, isso é FM01.
- **Âncora:** *"Você teve um ótimo começo! Vamos seguir em frente!"*
- **Caso-limite:** *"Continues te dedicando, pois está no caminho certo."* Afirmação prospectiva da capacidade, sem nomear o que foi feito, logo FM08 e não FM01.

---

## 4. A variável MTL

**Sigla:** MTL, contração de **MeTaLinguístico**.
**Nome por extenso da variável:** *foco metalinguístico no texto do aluno*.
**Tipo:** binária, uma decisão por devolutiva, preenchida na segunda passada.

Ela existe para dar um julgamento especialista ao mesmo construto que hoje é medido por uma régua lexical de palavra-chave (`src/metalinguistic_adherence.py`), que apenas verifica se a resposta cita algum dos termos da taxonomia de Koch. O cruzamento entre as duas produz o κ heurística-versus-humano que valida (ou invalida) a métrica da RQ2. A régua não consegue distinguir o uso vazio do termo técnico do apontamento genuíno feito em linguagem comum, e é exatamente essa distinção que a MTL mede.

### Definição

> A devolutiva trata o **texto que o aluno escreveu** como objeto de atenção, comentando alguma característica da sua construção? Ou fica no plano do **conteúdo da obra literária** que o aluno citou, ou em elogio e pergunta genéricos que não se ancoram em nada do texto produzido?

- **Marcar 1** quando a devolutiva se refere a alguma propriedade da escrita do aluno: repetição, uso de conectivo, clareza de a quem um pronome se refere, encadeamento das ideias, organização, progressão, pontuação, escolha de palavra.
- **Marcar 0** quando a devolutiva conversa sobre o enredo, os personagens ou o tema da obra, ou quando faz elogio ou pergunta que caberiam em qualquer texto.

### O ponto crítico: não exigir terminologia técnica

É aqui que a variável ganha valor, e é aqui que ela se separa da régua lexical.

- *"Você repetiu muito 'a cartomante'; dá para trocar por outra palavra?"* → **MTL = 1**, ainda que não apareça a palavra "coesão" nem "repetição lexical".
- *"Seu texto tem boa coesão e ótima estrutura."* → **MTL = 0** se o elogio for de fórmula e não apontar nada específico do texto. Usar o termo não basta.
- *"O que você acha que motivou a cartomante a mentir?"* → **MTL = 0**, é conversa sobre a obra, não sobre a escrita.

*(Os três exemplos acima são inventados para o instrumento e não correspondem a nenhuma linha da planilha.)*

Vale para qualquer trecho da devolutiva, tanto na parte de elogio quanto nas perguntas. **Basta um** trecho que satisfaça para marcar 1.

### Congelamento da definição

Esta definição é **idêntica em substância à do `GUIA_2a_CODIFICACAO`, de 27 de julho de 2026**, e está congelada pelo pré-registro da análise: ela não será ajustada depois de vistos os resultados. Se se mostrar mal formulada, isso é reportado como limitação, não corrigido retroativamente. A explicitação de fronteiras da seção 5 foi redigida em 29 de julho de 2026, **antes de qualquer anotação**, e não altera o critério: apenas o desdobra em relação às FMs vizinhas.

---

## 5. Fronteiras entre MTL e as FMs vizinhas

### O princípio geral

As duas dimensões respondem a perguntas diferentes sobre a mesma devolutiva:

- **As FMs perguntam:** *que movimento de mediação a devolutiva faz?* (reconhece, nomeia, pergunta, dá pista, modela, manda revisar, desafia, encoraja)
- **A MTL pergunta:** *sobre que objeto ela faz esse movimento?* (o texto que o aluno escreveu, ou a obra sobre a qual ele escreveu)

São eixos **ortogonais**. Nenhuma FM implica MTL = 1, e MTL = 1 não implica nenhuma FM em particular. **Não existe regra aritmética ligando as duas colunas**: a MTL não é soma, união nem consequência das FMs, e não deve ser derivada delas. É por isso que as duas passadas são separadas.

As três fronteiras que mais exigem cuidado são com FM02, FM03 e FM04, porque são as funções que podem se dirigir tanto ao texto do aluno quanto ao conteúdo da obra. Os exemplos abaixo são **inventados** e não correspondem a nenhuma linha da planilha.

### 5.1. MTL e FM02 (nomear o problema)

FM02 é sobre **declarar uma inadequação**. MTL é sobre **em que a inadequação incide**. Um problema pode ser nomeado no plano da obra, e uma propriedade da escrita pode ser comentada sem que nada seja declarado inadequado.

| Exemplo | FM02 | MTL | Por quê |
|---|:---:|:---:|---|
| "Você usou 'ele' várias vezes e nem sempre dá para saber de quem se trata." | 1 | 1 | Nomeia a inadequação e ela incide sobre uma propriedade da escrita (clareza referencial). |
| "Você trocou o nome do personagem: quem procurou a cartomante foi Camilo, não Vilela." | 1 | 0 | Nomeia uma inadequação, mas ela é de conteúdo da obra, não de construção do texto. |
| "Você usou bem os marcadores de tempo para ligar uma cena à outra." | 0 | 1 | Comenta uma propriedade da escrita sem declarar nada inadequado (é FM01). |
| "Seu texto ficou muito bom, parabéns!" | 0 | 0 | Elogio de fórmula, não aponta nada, nem problema nem propriedade. |

**Regra prática:** perguntar primeiro *"alguma coisa foi dita como inadequada?"* (FM02) e, só na segunda passada, *"sobre o que se falou?"* (MTL).

### 5.2. MTL e FM03 (provocar reflexão)

FM03 exige pergunta aberta que devolva ao aluno **uma escolha textual própria**. MTL exige que **alguma propriedade da escrita** seja apontada. As duas coincidem com frequência, mas não sempre, e o corpus do modelo é rico justamente nas linhas em que não coincidem.

| Exemplo | FM03 | MTL | Por quê |
|---|:---:|:---:|---|
| "Você começou três frases seguidas com 'A Casa Verde'. Que efeito isso causa em quem lê?" | 1 | 1 | Pergunta aberta sobre uma escolha do próprio texto, e a propriedade está nomeada. |
| "O que você poderia melhorar no seu texto?" | 1 | 0 | Devolve ao aluno o próprio texto (FM03), mas nenhuma propriedade da escrita é apontada. |
| "Como você acha que o medo dos habitantes afetou a história do livro?" | 0 | 0 | Pergunta sobre o enredo da obra: não é reflexão sobre escolha textual do aluno nem foco metalinguístico. |
| "Há repetições demais neste parágrafo." | 0 | 1 | Aponta propriedade da escrita, mas em forma declarativa (é FM02), não pergunta. |

**Atenção, é o caso mais frequente deste corpus:** o modelo faz muitas perguntas sobre a obra. Essas linhas costumam ser **FM03 = 0 e MTL = 0**, e a tentação de marcá-las como reflexão pelo simples fato de serem perguntas é o principal risco de arrasto nesta rodada.

### 5.3. MTL e FM04 (oferecer pista)

FM04 é sobre **dar um caminho concreto**. MTL é sobre **para onde o caminho aponta**. A ampliação da FM04 na v0.2, que passou a incluir "indicar o aspecto ou conteúdo específico a desenvolver", tornou possível uma pista inteiramente temática.

| Exemplo | FM04 | MTL | Por quê |
|---|:---:|:---:|---|
| "Para ligar as cenas, você pode usar 'primeiro', 'depois', 'finalmente'." | 1 | 1 | Pista concreta que incide sobre a construção do texto. |
| "Releia o capítulo em que a Casa Verde é esvaziada e anote o que acontece." | 1 | 0 | Estratégia concreta (FM04), mas dirigida ao conteúdo da obra. |
| "Há muita repetição de 'Casa Verde' no texto." | 0 | 1 | Aponta a propriedade sem oferecer caminho (é FM02). |
| "Capriche mais na próxima." | 0 | 0 | Nem caminho concreto nem propriedade apontada (é FM08). |

**Regra prática:** uma pista é MTL = 1 quando o que ela oferece é um recurso de escrita ou uma operação sobre o texto; é MTL = 0 quando o que ela oferece é leitura, informação ou conteúdo da obra.

---

## 6. Notas de aplicação

**Viés de formato, a conhecer sem deixar influenciar.** O esquema de saída do modelo tem um campo de reconhecimento e um bloco de perguntas, o que força um movimento de elogio e abre espaço para pergunta. Isso significa que FM01 e FM03 podem estar presentes por imposição do formato, não por decisão pedagógica. A leitura desse viés é problema da escrita do artigo, não da codificação: **codificar pela regra de evidência mínima como sempre**, marcando o que está no texto.

**Devolutiva desalinhada do texto do aluno.** Se uma devolutiva comentar algo que não está no texto do aluno correspondente, codificar as funções normalmente (elas não dependem da correção do conteúdo) e registrar a observação. A MTL, nesse caso, segue a mesma regra: o que importa é se a devolutiva se dirige à construção do texto, ainda que erre o alvo.

**Desacordo com o codebook.** Se durante a tarefa alguma definição parecer frouxa, **registrar em `Observações` e seguir com a definição como está**. Não ajustar o codebook no meio da passada: um desacordo registrado vale mais para o artigo do que uma concordância obtida por reconciliação, e foi exatamente assim que a v0.2 nasceu em junho.

**Casos-limite genuínos.** Melhor perguntar antes do que descobrir depois na planilha.

---

## 7. Quadro-resumo (referência rápida)

| Variável | Pergunta de decisão |
|---|---|
| **FM01** Reconhecer competência | Nomeia especificamente algo que o aluno fez bem no texto? |
| **FM02** Nomear o problema | Diz que algo no texto está inadequado, insuficiente ou ausente? |
| **FM03** Provocar reflexão | Faz pergunta aberta que devolve ao aluno uma escolha textual própria, sem entregar a resposta? |
| **FM04** Oferecer pista | Dá ajuda concreta em direção à solução, sem reescrever o texto? |
| **FM05** Modelar parcialmente | Apresenta um exemplo já reescrito, uma frase pronta? |
| **FM06** Propor revisão | Pede explicitamente a reescrita ou correção do que já está no texto? |
| **FM07** Desafiar ampliação | Pede conteúdo novo, indo além de corrigir o que existe? |
| **FM08** Reforçar autonomia | Afirma a capacidade do aluno e projeta continuidade, sem nomear competência específica? |
| **MTL** Foco metalinguístico | Comenta alguma propriedade da escrita do aluno, ou fica no plano da obra e do elogio genérico? |

Em todas: **na dúvida, 0**. Basta um trecho para marcar 1. A unidade é sempre a devolutiva inteira.

---

## 8. Procedência das definições

- **FM01 a FM08:** taxonomia do Prof. Marcelo Magalhães Foohs, operacionalizada sobre o corpus de referência especializada em junho de 2026 (v0.1) e revista após a primeira rodada de concordância (v0.2, ampliação de FM02 e FM04, as duas funções de menor κ, respectivamente 0,58 e 0,45). **Sem alteração de substância nesta versão.**
- **MTL:** definida em 27 de julho de 2026 no `GUIA_2a_CODIFICACAO`, em resposta ao Revisor A do JBCS, e congelada pelo `PRE-REGISTRO_analise` da mesma data.
- **Fronteiras da seção 5:** redigidas em 29 de julho de 2026, antes de qualquer anotação desta rodada, como desdobramento das definições existentes.
