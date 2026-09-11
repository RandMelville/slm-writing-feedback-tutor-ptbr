# Protocolo revisado de codificação das Funções de Mediação e dos Falsos Positivos

**Estudo:** SLMs para tutoria de escrita offline em português do Brasil (artigo JBCS, revisão R1)\
**Versão:** 0.5, versão congelada\
**Data:** 26 de agosto de 2026\
**Redação original:** Randerson O. M. Rebouças\
**Revisão metodológica:** Marcelo Magalhães Foohs\
**Status:** versão congelada. Incorpora a revisão metodológica de 25/08/2026 e os quatro ajustes acordados na troca de 26/08/2026. Substitui integralmente o PROTOCOLO_v04. Nenhuma nova codificação começa antes do congelamento registrado na seção 9.

> **Documento interno.** Este protocolo registra as decisões metodológicas do estudo e poderá ser citado no artigo. Ele **não** é entregue aos codificadores. Cada codificador recebe apenas o Guia do Professor revisado, sua planilha individual revisada e as orientações operacionais necessárias.

Esta minuta alinha o registro metodológico ao Guia do Professor e às planilhas individuais revisadas. A principal mudança é a separação entre: (a) presença formal de uma Função de Mediação (FM); (b) ocorrência de falso positivo associado a essa função (FP); e (c) foco metalinguístico (MTL). O documento foi congelado após a manifestação expressa dos autores responsáveis, registrada na seção 9.

## 1. Histórico: o que aconteceu até aqui

### 1.1 As codificações já produzidas

+--------+------------+----------------------+----------------------------------------------------------+----------------------------+
| **\#** | **Quando** | **Quem codificou**   | **Material**                                             | **Instrumento**            |
+:=======+:===========+:=====================+:=========================================================+:===========================+
| 1      | jun/2026   | Randerson (leitura)  | as 65 devolutivas produzidas pelos especialistas         | codebook v0.1, depois v0.2 |
+--------+------------+----------------------+----------------------------------------------------------+----------------------------+
| 2      | jun/2026   | Marcelo, às cegas    | 20 das mesmas devolutivas produzidas pelos especialistas | codebook v0.1              |
+--------+------------+----------------------+----------------------------------------------------------+----------------------------+
| 3      | jun/2026   | **assistente de IA** | as 39 devolutivas do modelo (Qwen 2.5 3B)                | codebook v0.2              |
+--------+------------+----------------------+----------------------------------------------------------+----------------------------+
| 4      | jul/2026   | Marcelo, às cegas    | as mesmas 39 devolutivas do modelo                       | codebook v0.2-Q            |
+--------+------------+----------------------+----------------------------------------------------------+----------------------------+

O κ = 0,83 foi calculado sobre 20 devolutivas produzidas por especialistas e codificadas, de forma independente, por Randerson e Marcelo. Portanto, o coeficiente expressa a concordância entre esses dois codificadores quanto à identificação das Funções de Mediação nessa amostra. Não envolve comparação com IA nem constitui parâmetro-alvo de desempenho do modelo. O κ = 0,14, obtido posteriormente no exame das 39 devolutivas do modelo, não se sustenta como estimativa de confiabilidade interanotadores, pois uma das codificações foi produzida por assistente de IA e os instrumentos empregados não eram plenamente equivalentes.

### 1.2 Procedência da codificação nº 3

A primeira codificação das 39 devolutivas do modelo **não foi produzida por leitura humana**. Ela foi gerada por assistente de IA em sessão de trabalho e ficou embutida em `analises/fm_coding_model.py`, cujo cabeçalho registra a autoria desde junho. A implicação não foi percebida quando a comparação foi montada: um coeficiente de concordância entre uma codificação automatizada e uma codificação humana não é uma estimativa de confiabilidade interanotadores, independentemente de qualquer outro problema do instrumento.

A codificação nº 3 sai da cadeia de evidência do artigo. Ela permanece no material aberto, identificada pelo que é: uma triagem automatizada prévia, com data e procedência declaradas. Essa procedência aparece com a mesma clareza no texto do artigo, e não apenas neste protocolo.

### 1.3 O defeito de instrumento entre a nº 3 e a nº 4

A comparação campo a campo entre o codebook v0.2 (usado na nº 3) e o v0.2-Q (usado na nº 4) mostra que **as oito definições são substantivamente idênticas**. A única diferença de redação é uma troca de palavra na FM05 e a retirada dos códigos de origem das âncoras.

O único acréscimo substantivo é uma **"Nota específica deste corpus" na FM03**, determinando que pergunta sobre enredo, personagem ou tema da obra não conta como FM03. Essa nota não existia no instrumento da nº 3 e foi escrita **a partir dela**: os comentários da codificação automatizada já registravam esse mesmo julgamento. Uma decisão da primeira passada foi convertida em regra e entregue à segunda como instrumento.

Soma-se a isso o registro, no mesmo documento, da média de funções por devolutiva apurada na primeira passada (1,7 contra 3,8 das humanas). A nota metodológica 8 do segundo codificador descreve exatamente o efeito de ambos: ancoragem e inflação da concordância.

Direção do efeito, para o registro: a informação vazada apontava para menos funções e o segundo codificador marcou mais (2,77 contra 1,69); a nota da FM03 orientava a não marcar e ele marcou a função em 21 das 39 devolutivas, contra 4 da primeira passada. Ambas as contaminações operaram no sentido de **aumentar** a concordância aparente, o que faz do κ = 0,14 um limite superior.

**Alcance do defeito, com a inferência corrigida.** Retirando a FM03 do cálculo, o κ médio vai de 0,138 para 0,149. O que esse número mostra é que **a regra anterior da FM03 não explica, sozinha, a discrepância observada**. Não se conclui daí que o instrumento não tenha contribuído para ela. A permanência das divergências em outras funções, em especial a FM07, que apresenta o mesmo número de divergências, exige examinar os casos discrepantes e as respectivas regras operacionais antes de determinar a origem dessas diferenças.

A regra de validade mínima da seção 3.0 oferece uma hipótese explícita a examinar: a definição anterior da FM07 pode ter permitido contar como desafio de ampliação formulações apoiadas em informação inexistente, interpretação equivocada ou situação comunicativa incoerente. O exame dos casos discrepantes de FM07 entra no plano de análise (seção 6).

### 1.4 O que mudou da v0.3 para esta versão

+--------------------------------------------------------------------------------------------+----------------------------+
| **Mudança metodológica**                                                                   | **Onde foi incorporada**   |
+:===========================================================================================+:===========================+
| Separação entre presença da FM e falso positivo associado                                  | seções 2, 3.0 e 3.2        |
+--------------------------------------------------------------------------------------------+----------------------------+
| Evidência específica para cada FM e justificativa específica para cada FP                  | seções 3.0, 4 e 5          |
+--------------------------------------------------------------------------------------------+----------------------------+
| MTL mantida como eixo independente, preenchido em segunda passada                          | seções 3.3, 3.4 e 5        |
+--------------------------------------------------------------------------------------------+----------------------------+
| Codificação nº 4 excluída do cálculo final de concordância                                 | seções 1.5, 5 e 6          |
+--------------------------------------------------------------------------------------------+----------------------------+
| Dois novos codificadores independentes                                                     | seções 3.5 e 5             |
+--------------------------------------------------------------------------------------------+----------------------------+
| Codificadores recebem apenas o Guia do Professor revisado e a planilha individual revisada | seção 4                    |
+--------------------------------------------------------------------------------------------+----------------------------+
| Procedência da codificação automatizada declarada também no artigo                         | seção 1.2                  |
+--------------------------------------------------------------------------------------------+----------------------------+
| Exemplos do instrumento não extraídos das 39 devolutivas-alvo                              | seção 3.7                  |
+--------------------------------------------------------------------------------------------+----------------------------+

### 1.4.1 Ajustes acordados em 26 de agosto de 2026

Quatro pontos foram levantados na conferência do autor principal e aprovados pelo revisor metodológico na mesma data:

1.  A planilha passou a **impedir** a combinação `FM = 0` com `FP = 1`, por validação de dados com fórmula, e não apenas a sinalizá-la por realce condicional. A redação da seção 3.0 fica assim sustentada pelo instrumento.
2.  A linha de cabeçalho e as colunas A a C foram **congeladas** nas duas planilhas, de modo que o texto do aluno e a devolutiva permaneçam visíveis ao longo das 37 colunas.
3.  A relação entre VFM e a codificação de julho foi explicitada na seção 6.
4.  O `verifica_exemplos.py` foi atualizado para os textos exatos do Guia, do Anexo e deste Protocolo que integram o conjunto final, e reexecutado, com o registro preservado.

### 1.5 O estatuto da codificação nº 4

A codificação nº 4 não integra o cálculo final de concordância. Ela foi produzida antes da separação entre FM e FP e, portanto, não possui as mesmas variáveis da rodada final. Sua contribuição é histórica e metodológica: tornou visível que uma devolutiva pode apresentar formalmente uma função e, ao mesmo tempo, apoiar-se em leitura equivocada ou orientação inadequada.

Ela será preservada como parte do percurso do estudo. Qualquer comparação entre essa codificação e as duas novas será exploratória, realizada somente depois de concluídos e preservados os novos registros, sem ser apresentada como confiabilidade interanotadores.

## 2. O que este instrumento pede do codificador, em uma frase

Ler cada devolutiva e registrar separadamente: quais Funções de Mediação aparecem formalmente (FM), quais dessas ocorrências constituem falsos positivos (FP) e se a devolutiva toma a escrita do aluno como objeto de atenção (MTL).

## 3. Codebook revisado

### 3.0 Regra de validade mínima das FMs

> A presença formal de uma Função de Mediação e sua adequação são registradas em colunas diferentes. A coluna FM responde se o movimento aparece; a coluna FP responde se esse movimento, embora presente na forma, apoia-se em leitura incorreta, premissa falsa ou orientação tecnicamente inadequada.

Para cada par FMxx--FPxx:

1.  **FMxx = 0 e FPxx = 0:** o movimento não aparece na devolutiva.
2.  **FMxx = 1 e FPxx = 0:** o movimento aparece e não foi identificado falso positivo associado.
3.  **FMxx = 1 e FPxx = 1:** o movimento aparece formalmente, mas há pelo menos uma ocorrência falsa ou inadequada associada à função.
4.  **FMxx = 0 e FPxx = 1:** combinação inválida e proibida pela planilha.

O registro de FP não transforma a tarefa em uma avaliação global da devolutiva. O juízo permanece localizado: identifica-se apenas se uma ocorrência formal da função se apoia em interpretação comprovadamente ausente ou contrariada pelo texto, ou se a orientação proposta pode induzir o aluno ao erro.

**Evidência e justificativa.** Para cada FM marcada com 1, o codificador copia o trecho exato que fundamenta a marcação no campo `Evidência FMxx`. Se marcar FPxx = 1, registra no campo `Justificativa FPxx` por que aquela ocorrência é falsa ou inadequada. Um mesmo trecho pode fundamentar mais de uma FM e, nesse caso, deve ser repetido nos respectivos campos de evidência.

**Segmentos mistos.** Se a mesma devolutiva contiver, para uma função, um segmento adequado e outro falso, registra-se FMxx = 1 e FPxx = 1. A evidência identifica o movimento formal; a justificativa distingue o segmento problemático. Assim, o registro binário não apaga nenhuma das duas ocorrências.

**Princípio de prudência.** Na dúvida sobre a presença formal da função, marcar FM = 0. Na dúvida sobre o falso positivo, marcar FP = 0 e registrar a dúvida em `Observações`, sem presumir que toda interpretação alternativa seja erro.

### 3.1 Objeto, unidade e regra de evidência

**Objeto.** 39 devolutivas produzidas por um modelo de linguagem sobre textos sintéticos de aluno, escritos pela equipe de pesquisa para simular produções de 8º e 9º ano.

**Unidade de codificação.** A devolutiva integral. Cada linha recebe 17 decisões binárias: FM01 a FM08, FP01 a FP08 e MTL.

**Unidade de evidência.** A evidência é o segmento exato da devolutiva que sustenta cada FM. Basta um segmento para caracterizar a presença formal de uma função. Se houver segmentos adequados e falsos associados à mesma função, ambos são preservados por meio do par FM--FP e dos campos de evidência e justificativa.

**Independência entre funções.** Uma mesma devolutiva pode mobilizar várias funções, e o mesmo trecho pode sustentar mais de uma delas. Cada função é decidida separadamente.

### 3.2 As oito funções

**FM01. Reconhecer competência** - *Definição:* afirmar, de forma específica, algo que o aluno fez bem no texto (uma escolha, uma compreensão, um recurso bem empregado). - *Inclusão:* o elogio nomeia o que foi bem feito (compreensão do enredo, uso de conectivo, organização, vocabulário). - *Exclusão:* encorajamento genérico voltado ao futuro ("continue se dedicando", "está no caminho certo") sem nomear uma competência, isso é FM08. - *Falso positivo associado (marcar FM01 = 1 e FP01 = 1):* elogio que apresenta como competência uma inadequação, erro ou vício da produção, ou que atribui ao aluno uma competência não sustentada pelo texto. - *Âncora:* "Parabéns! Você identificou um dos acontecimentos mais importantes do conto: a confiança de Camilo nas palavras da cartomante e o desfecho inesperado da história." - *Caso-limite:* "Continue se dedicando, pois já demonstrou compreender a história." A segunda oração nomeia uma competência, logo FM01; o "continue se dedicando" isolado seria só FM08. - *Falso positivo, exemplo:* "Parabéns pelo uso variado de conectivos: 'e', 'e daí', 'e aí' deixaram o texto fluido." A repetição do mesmo conector é apresentada como qualidade. FM01 = 1 e FP01 = 1.

**FM02. Nomear o problema** - *Definição:* indicar ao aluno que o texto é inadequado em algum aspecto. - *Inclusão:* o problema é dito (repetição, pronome ambíguo, conector contraditório, ordem embaralhada, períodos curtos justapostos, buraco narrativo). Inclui apontar que algo está ausente, insuficiente ou não atende ao gênero, ainda que em tom de convite. - *Exclusão:* levar o aluno a descobrir o problema por pergunta, isso é FM03. Pedir reescrita sem indicar o que está inadequado, isso é FM06. Texto elogiado sem apontar insuficiência, não marcar. - *Falso positivo associado (marcar FM02 = 1 e FP02 = 1):* indicação de problema inexistente, ou caracterização de um recurso adequado como inadequação, quando isso puder levar o aluno a corrigir algo que não constitui problema. - *Âncora:* "Você usou 'ele' muitas vezes, sem deixar claro a quem se referia o pronome a cada vez." - *Caso-limite:* "A palavra 'portanto' não parece adequada. Por qual palavra você poderia substituí-la?" O primeiro trecho é FM02, o segundo é FM03. Mesma devolutiva, duas funções. - *Falso positivo, exemplo:* o aluno escreveu "Assim que abriu a porta, o bonde passou", e a devolutiva diz: "Cuidado, 'assim que' não é expressão adequada na escrita; troque sempre por 'quando'." O problema não existe e a regra é falsa. FM02 = 1 e FP02 = 1.

**FM03. Provocar reflexão** - *Definição:* marcar FM03 quando a pergunta estiver ancorada em um elemento identificável da produção do aluno e for construída de modo que uma resposta pertinente exija explicar, justificar, relacionar, reconsiderar ou desenvolver esse elemento, ainda que essa operação não seja solicitada explicitamente. A pergunta não deve fornecer antecipadamente a resposta. - *Inclusão:* pergunta ancorada em elemento identificável do texto do aluno, mesmo quando a operação reflexiva não é pedida em palavras. Pergunta sobre a obra citada conta, desde que leve o estudante a reexaminar uma escolha narrativa, interpretativa ou argumentativa presente no próprio texto. - *Exclusão:* pergunta retórica que já contém a correção dentro de si, conta como FM02. Pergunta que não se ancora em nenhum elemento identificável da produção do aluno. - *Falso positivo associado (marcar FM03 = 1 e FP03 = 1):* pergunta construída sobre informação inexistente, leitura equivocada ou premissa falsa, quando por essa razão a reflexão solicitada não possa ser sustentada pela produção do aluno. - *Âncora:* "O que exatamente te fez rir? Por que o final é chocante?" - *Caso-limite:* "(se era horrível, o natural seria ele querer sair, então o 'mas' não cabe aqui)". A resposta já está dada no parêntese, logo FM02 e não FM03. - *Falso positivo, exemplo:* "Por que você escolheu terminar o texto com a morte da personagem?", num texto em que ninguém morre. FM03 = 1 e FP03 = 1.

**FM04. Oferecer pista** - *Definição:* fornecer ajuda concreta em direção à solução sem reescrever o texto do aluno. - *Inclusão:* listar substituições possíveis, conectores, marcadores temporais como repertório a usar. Inclui indicar o aspecto ou conteúdo específico a desenvolver, ou a estratégia a seguir. - *Exclusão:* apresentar uma frase já reescrita do aluno, isso é FM05. Apenas mandar reescrever sem dar o caminho, isso é FM06. **Fronteira com FM03:** a mesma orientação dada como diretiva é FM04; dada como pergunta é FM03. - *Falso positivo associado (marcar FM04 = 1 e FP04 = 1):* pista incorreta, incompatível com o problema identificado, ou que oriente o aluno para uma solução capaz de introduzir ou agravar uma inadequação. - *Âncora:* "para evitar essa repetição, usar o nome da cartomante, ou usar 'ela' ou 'a mulher'." - *Caso-limite:* "Você pode utilizar marcadores temporais como: Primeiro... Depois... Mais tarde... Finalmente..." Oferece ferramentas, mas não monta a frase do aluno, logo FM04 e não FM05. - *Falso positivo, exemplo:* "Para ligar as duas ideias que se opõem, use 'portanto'." O conector indicado é conclusivo, não adversativo, e a pista conduz ao erro. FM04 = 1 e FP04 = 1.

**FM05. Modelar parcialmente** - *Definição:* demonstrar uma solução por meio de exemplo reescrito, idealmente a partir do próprio trecho do aluno. - *Inclusão:* apresenta frase montada que materializa a alteração. - *Exclusão:* apenas nomear palavras ou recursos a usar, sem montar a frase, corresponde à FM04. - *Falso positivo associado (marcar FM05 = 1 e FP05 = 1):* o modelo preserva o problema que deveria resolver ou introduz inadequação relevante. - *Âncora:* "Sugestão: 'Sem saída, desceu pelo elevador; logo depois, percebeu que a confusão só aumentava...'" - *Caso-limite:* uma lista de conectores é FM04; uma frase pronta empregando um conector é FM05. - *Falso positivo, exemplo:* diante de ambiguidade pronominal, oferecer "Ele saiu e ele voltou quando ele viu que ele tinha esquecido a chave." Há modelo formal, mas ele repete o problema: FM05 = 1 e FP05 = 1.

**FM06. Propor revisão** - *Definição:* propor ou solicitar explicitamente a reescrita ou correção do que já está no texto. - *Inclusão:* "vamos reescrever", "o texto precisa ser reescrito", "reorganize seguindo a ordem". - *Exclusão:* desafio de acrescentar conteúdo novo que não estava lá, isso é FM07. - *Falso positivo associado (marcar FM06 = 1 e FP06 = 1):* proposta de revisão fundamentada em problema inexistente, ou que oriente uma alteração capaz de tornar a produção menos adequada. - *Âncora:* "Vamos reescrever esse trecho a partir dessas dicas?!" - *Caso-limite:* "O texto precisa ser reescrito." FM06 puro, sem pista e sem modelo. - *Falso positivo, exemplo:* "Reescreva o trecho tirando as vírgulas entre as orações, porque vírgula antes de 'mas' é erro." A revisão proposta piora o texto. FM06 = 1 e FP06 = 1.

**FM07. Desafiar ampliação** - *Definição:* desafiar o aluno a ir além da correção, aprofundando ou acrescentando opinião, análise, detalhe ou reflexão que enriqueça o texto. - *Inclusão:* "acrescente sua opinião", "aprofunde sua análise", "desenvolva mais". - *Exclusão:* consertar conteúdo já existente corresponde à FM06; reescrever para o aluno corresponde à FM05. - *Falso positivo associado (marcar FM07 = 1 e FP07 = 1):* o desafio se apoia em elemento inexistente, premissa falsa ou interpretação contrariada pelo texto. - *Âncora:* "Acrescente uma frase avaliando a história." - *Caso-limite:* transformar dez frases em três ou quatro frases mais conectadas é FM06, pois reorganiza o que já existe; pedir opinião nova sobre o desfecho é FM07. - *Falso positivo, exemplo:* "Acrescente um parágrafo explicando por que o narrador escolheu o cachorro como confidente", num texto sem cachorro: FM07 = 1 e FP07 = 1. - *Caso que não basta para FP:* referir-se de modo pouco natural ao "autor deste texto" não prova, isoladamente, que o desafio seja falso. Se a ampliação se sustenta no texto, FM07 = 1 e FP07 = 0.

**FM08. Reforçar autonomia** - *Definição:* movimento de fechamento que afirma capacidade ou agência do aluno e projeta continuidade do trabalho. - *Inclusão:* "está no caminho certo", "vamos seguir em frente", "você consegue". - *Exclusão:* elogio que nomeia competência específica corresponde à FM01. - *Falso positivo associado (marcar FM08 = 1 e FP08 = 1):* a formulação tem aparência de encorajamento, mas reforça explicitamente a continuidade de orientação identificada como inadequada. - *Âncora:* "Você teve um ótimo começo! Vamos seguir em frente!" - *Caso-limite:* "Continue se dedicando, pois está no caminho certo" é FM08; não nomeia competência específica. - *Falso positivo, exemplo:* "Continue assim, trocando sempre as vírgulas por pontos como eu sugeri", quando a orientação é inadequada: FM08 = 1 e FP08 = 1.

### 3.3 A variável MTL

**Sigla:** MTL, contração de MeTaLinguístico. **Nome por extenso:** foco metalinguístico no texto do aluno. Binária, uma decisão por devolutiva, preenchida em passada separada.

> A devolutiva trata o texto que o aluno escreveu como objeto de atenção, comentando alguma característica da sua construção? Ou fica no plano do conteúdo da obra que o aluno citou, ou em elogio e pergunta genéricos que não se ancoram em nada do texto produzido?

- **Marcar 1** quando a devolutiva se refere a alguma propriedade da escrita do aluno: repetição, uso de conectivo, clareza referencial, encadeamento das ideias, organização, progressão, pontuação, escolha de palavra.
- **Marcar 0** quando a devolutiva conversa sobre o enredo, os personagens ou o tema da obra, ou quando faz elogio ou pergunta que caberiam em qualquer texto.

**Não exigir terminologia técnica.** "Você repetiu muito 'a cartomante'; dá para trocar por outra palavra?" é MTL = 1 mesmo sem a palavra "coesão". "Seu texto tem boa coesão" é MTL = 0 se o elogio for de fórmula e não apontar nada específico. Usar o termo não basta.

**A regra de validade mínima não se aplica à MTL.** A MTL registra o objeto de que a devolutiva fala, não a correção do que ela diz sobre esse objeto. Um comentário equivocado sobre a pontuação do aluno continua sendo um comentário sobre a escrita do aluno, logo MTL = 1. Se esse mesmo comentário for um falso positivo de FM02, isso é registrado no par FM02--FP02, não aqui.

**Esta definição não muda em relação à v0.2-Q e à v0.3.**

### 3.4 Fronteiras entre MTL e as FMs

As FMs perguntam *que movimento de mediação a devolutiva faz*. A MTL pergunta *sobre que objeto ela faz esse movimento*. São eixos ortogonais: nenhuma FM implica MTL = 1, e não existe regra aritmética ligando as duas colunas. Exemplos inventados para o instrumento:

+-------------------------------------------------------------------------------------------+--------+---------+
| **Exemplo**                                                                               | **FM** | **MTL** |
+:==========================================================================================+:=======+:========+
| "Você usou 'ele' várias vezes e nem sempre dá para saber de quem se trata."               | FM02   | 1       |
+-------------------------------------------------------------------------------------------+--------+---------+
| "Você trocou o nome do personagem: quem procurou a cartomante foi Camilo, não Vilela."    | FM02   | 0       |
+-------------------------------------------------------------------------------------------+--------+---------+
| "Você começou três frases seguidas com 'A Casa Verde'. Que efeito isso causa em quem lê?" | FM03   | 1       |
+-------------------------------------------------------------------------------------------+--------+---------+
| "Releia o capítulo em que a Casa Verde é esvaziada e anote o que acontece."               | FM04   | 0       |
+-------------------------------------------------------------------------------------------+--------+---------+
| "Seu texto ficou muito bom, parabéns!"                                                    | ---    | 0       |
+-------------------------------------------------------------------------------------------+--------+---------+

### 3.5 Independência da codificação

Os dois codificadores trabalham sem contato entre si durante a tarefa: não comparam decisões, não discutem casos-limite e não trocam planilhas. Também não recebem resultados agregados, frequências esperadas, codificações anteriores, o artigo ou o repositório do estudo.

Dúvidas são encaminhadas ao pesquisador responsável. Toda resposta que acrescente esclarecimento operacional é registrada e enviada, com a mesma redação e ao mesmo tempo, aos dois codificadores, sem revelar decisões ou dúvidas individuais. Não se altera o Guia nem o codebook durante a rodada.

Se alguma definição parecer inadequada, o codificador registra a observação e segue a regra vigente. A discussão e eventual revisão do instrumento somente ocorrem depois de concluídas e preservadas as duas codificações.

### 3.6 Escopo: presença funcional não é qualidade

O instrumento não atribui nota global à devolutiva nem avalia professores. Ele registra movimentos textualmente observáveis e, separadamente, falsos positivos localizados.

Para fins analíticos, denomina-se **realização sem falso positivo identificado** a combinação FMxx = 1 e FPxx = 0. A combinação FMxx = 1 e FPxx = 1 registra presença formal com problema associado. Essa distinção não permite concluir, por si só, se o aluno compreendeu a orientação, se houve aprendizagem ou se a mediação foi pedagogicamente eficaz; tais questões dependem de dados de interação e pertencem ao estudo piloto e a trabalhos posteriores.

### 3.7 Procedência dos exemplos

Nenhum exemplo, âncora ou caso-limite deste protocolo e do anexo de alinhamento conceitual sai das 39 devolutivas a codificar. Todos são construídos para o instrumento ou vêm do corpus humano de referência (as 65 devolutivas produzidas pelos especialistas), que não faz parte do material a codificar.

Isso é verificado por programa, e não por leitura: `verifica_exemplos.py`, neste mesmo diretório, normaliza acentuação e caixa e falha se qualquer trecho citado nos dois documentos aparecer nas 39 devolutivas.

## 4. O que cada codificador recebe

Cada codificador recebe somente:

- o Guia do Professor revisado, documento operacional com as definições de FM, FP e MTL, exemplos e regras de independência;
- uma planilha individual com as 39 devolutivas e as colunas `ID`, `Texto do aluno`, `Devolutiva`, oito conjuntos `FMxx`, `Evidência FMxx`, `FPxx`, `Justificativa FPxx`, além de `MTL` e `Observações`;
- prazo e canal para dúvidas operacionais.

Não recebe este protocolo, o anexo interno de alinhamento conceitual, codificações anteriores, resultados já apurados, chave de identificação de cenários, planilha do outro codificador ou qualquer gabarito.

Os dois recebem as mesmas 39 unidades e os mesmos identificadores `R01` a `R39`, condição necessária para o cálculo de concordância linha a linha. Se a ordem das linhas for diferente entre as planilhas, a correspondência é feita pelo identificador, nunca pela posição.

## 5. Procedimento

1.  Revisar e aprovar expressamente o Protocolo, o Guia do Professor e as planilhas individuais.
2.  Congelar os três elementos antes de compartilhar qualquer material com os codificadores.
3.  Entregar a cada codificador apenas o Guia do Professor revisado e sua planilha individual revisada.
4.  Realizar a **primeira passada**: FM, evidência correspondente, FP e justificativa correspondente, função por função.
5.  Realizar a **segunda passada**: MTL, sem reabrir as decisões de FM e FP.
6.  Preservar separadamente os dois arquivos datados antes de qualquer confronto.
7.  Calcular a concordância exclusivamente entre as duas novas codificações.
8.  Examinar divergências somente após a preservação dos registros originais.
9.  Consolidar resultados pelos 13 cenários, considerando as três execuções de cada um.
10. Revisar método, resultados, discussão, limitações e conclusões do artigo conforme os resultados.

**Comunicação durante a codificação.** Respostas metodológicas a dúvidas são encaminhadas simetricamente aos dois codificadores e arquivadas. Questões meramente técnicas de acesso ou preenchimento podem ser resolvidas individualmente, desde que não revelem conteúdo da outra codificação.

**Preservação do percurso.** Os instrumentos e registros anteriores permanecem no material aberto exatamente como foram usados, acompanhados de nota de transparência. Nenhum código original é alterado silenciosamente.

## 6. Plano de análise, fixado antes da anotação

Sobre o par **codificador A × codificador B**:

- concordância bruta e κ de Cohen por FM (FM01 a FM08) e para MTL, sempre acompanhados das prevalências observadas;
- para cada FPxx, frequência por codificador e concordância bruta. Como FPxx é condicionado à presença de FMxx, a concordância sobre FP será examinada no subconjunto de linhas em que pelo menos um codificador marcou FMxx = 1; κ será informado somente quando houver variação suficiente e com explicitação do denominador;
- PABAK poderá ser apresentado como análise complementar em categorias raras ou saturadas, nunca em substituição ao κ e sempre com sinalização do efeito da prevalência;
- matriz de divergências e exame qualitativo das evidências e justificativas, sem reconciliação retroativa dos arquivos originais;
- consolidação por cenário das três execuções de cada um dos 13 cenários, reportando estabilidade e variação de FM, FP e MTL;
- nenhuma categoria será omitida por produzir resultado desfavorável.

Para descrever a presença funcional sem falso positivo identificado, será usada a variável derivada `VFMxx = 1` quando `FMxx = 1` e `FPxx = 0`; nos demais casos, `VFMxx = 0`. Os resultados devem apresentar separadamente a presença formal (FM), os falsos positivos (FP) e a realização sem FP identificado (VFM), evitando tratar esses três indicadores como equivalentes.

**A VFM é uma medida derivada mais estrita do que a utilizada na codificação de julho.** Naquele instrumento, quando a mesma função reunia um segmento adequado e outro inadequado na mesma devolutiva, a coluna permanecia em 1. Sob a regra atual, esse mesmo caso produz `FM = 1` e `FP = 1`, logo `VFM = 0`. Portanto, qualquer comparação entre a VFM e a codificação de julho será exploratória e deverá reconhecer explicitamente que as duas medidas não são equivalentes.

Sobre a validade de construto da métrica da RQ2, a régua lexical executada por programa (`src/metalinguistic_adherence.py`) será confrontada com MTL de cada codificador, fornecendo duas leituras humanas independentes do mesmo construto.

Qualquer comparação com a codificação nº 4 será exploratória, posterior à preservação das novas codificações e relatada como percurso metodológico, não como confiabilidade.

## 7. O que vai para o artigo em cada cenário de resultado

O artigo informará, função por função, a concordância bruta, o κ, as prevalências e as frequências de FP. Não será usado um κ médio como critério único de decisão, pois funções com prevalências distintas não devem ser reduzidas a um único valor sem justificativa.

- Funções com concordância suficiente poderão sustentar descrições quantitativas, sempre acompanhadas de seus indicadores de confiabilidade.
- Funções com baixa concordância serão tratadas como resultados instáveis: as frequências poderão ser apresentadas por transparência, mas não sustentarão conclusões quantitativas fortes.
- Quando o κ for prejudicado por categoria rara ou saturada, a interpretação considerará conjuntamente concordância bruta, prevalência, PABAK complementar e exame dos desacordos.
- O percurso de revisão do instrumento, inclusive a procedência da codificação automatizada e a substituição da comparação anterior, será descrito no método e nas limitações.

## 8. Limitações já assumidas

- **Codificação binária.** FM, FP e MTL reduzem fenômenos graduais e contextuais a decisões binárias.
- **FP não é avaliação global.** O falso positivo identifica problema localizado em uma função; não mede a qualidade pedagógica total da devolutiva.
- **Dependência lógica.** FPxx somente existe quando FMxx = 1, o que exige análise específica de sua concordância.
- **Juízo individual por passada.** Cada codificação é produzida por uma pessoa, não por painel.
- **Viés de formato.** O esquema de saída do modelo pode favorecer determinadas funções, especialmente reconhecimento e pergunta.
- **Textos sintéticos.** O corpus não contém produção real de estudante, limitando a generalização.
- **Validade interacional não observada.** O benchmark não mostra se o aluno compreendeu, respondeu ou aprendeu com a devolutiva.

## 9. Congelamento e concordância dos autores

Esta versão está congelada. O congelamento ocorreu após a conferência conjunta de:

1.  Protocolo revisado;
2.  Guia do Professor revisado;
3.  planilhas individuais dos codificadores A e B.

Após o início da primeira codificação, nenhuma definição será alterada. Erro material eventualmente encontrado será registrado em errata datada; se afetar decisões de codificação, os autores decidirão de forma documentada se a rodada deve ser reiniciada.

+--------------------------+----------------------------------------------------------------------+------------------+
| **Autor**                | **Manifestação sobre esta versão**                                   | **Data**         |
+:=========================+:=====================================================================+:=================+
| Randerson O. M. Rebouças | de acordo, com os quatro ajustes da seção 1.4.1                      | 26/08/2026       |
+--------------------------+----------------------------------------------------------------------+------------------+
| Marcelo Magalhães Foohs  | de acordo com os quatro ajustes, por e-mail de 26/08/2026            | 26/08/2026       |
+--------------------------+----------------------------------------------------------------------+------------------+
| Rosa Maria Vicari        | não solicitada nesta etapa, em razão de indisponibilidade comunicada | ---              |
+--------------------------+----------------------------------------------------------------------+------------------+

Pareceres, mensagens ou concordâncias referentes a versões anteriores não equivalem à aprovação desta versão.

## Referências do plano de análise

- Byrt, T., Bishop, J., Carlin, J. B. (1993). Bias, prevalence and kappa. *Journal of Clinical Epidemiology*, 46(5), 423-429.
- Feinstein, A. R., Cicchetti, D. V. (1990). High agreement but low kappa: I. The problems of two paradoxes. *Journal of Clinical Epidemiology*, 43(6), 543-549.
- Landis, J. R., Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159-174.
