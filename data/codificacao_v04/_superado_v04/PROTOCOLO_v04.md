# Protocolo de codificação das Funções de Mediação (v0.4, versão congelada)

**Estudo:** SLMs para tutoria de escrita offline em português do Brasil (artigo JBCS, revisão R1)
**Versão:** 0.4
**Data:** 22 de agosto de 2026
**Redação:** Randerson O. M. Rebouças
**Status:** versão final para congelamento. Substitui integralmente o `PROTOCOLO_REVISADO_v03.md`
e o `codebook_respostas_modelo.md` (v0.2-Q). Nenhuma nova codificação começa antes do
congelamento registrado na seção 9.

> **Documento interno.** Este protocolo é o registro metodológico do estudo, citado no artigo.
> Ele **não** é o material entregue aos codificadores: eles recebem o `GUIA_PROFESSOR` e a
> planilha. O guia é a versão operacional deste documento, em linguagem de professor, sem
> nenhuma alteração de definição.

Esta versão incorpora o parecer do Prof. Marcelo Magalhães Foohs de 10 de agosto de 2026
(`Observacoes_Protocolo_Revisado_v03.docx`) e a leitura técnica da Profa. Rosa Maria Vicari de 11
de agosto de 2026. É o instrumento congelado da rodada final, e chega aos dois novos
codificadores traduzido no `GUIA_PROFESSOR`, sem alteração de definição.

---

## 1. Histórico: o que aconteceu até aqui

### 1.1 As codificações já produzidas

| # | Quando | Quem codificou | Material | Instrumento |
|---|---|---|---|---|
| 1 | jun/2026 | Randerson (leitura) | as 65 devolutivas dos cinco professores | codebook v0.1, depois v0.2 |
| 2 | jun/2026 | Marcelo, às cegas | 20 das mesmas devolutivas de professores | codebook v0.1 |
| 3 | jun/2026 | **assistente de IA** | as 39 devolutivas do modelo (Qwen 2.5 3B) | codebook v0.2 |
| 4 | jul/2026 | Marcelo, às cegas | as mesmas 39 devolutivas do modelo | codebook v0.2-Q |

O par 1 × 2 produziu o κ = 0,83 do corpus humano, que não é afetado por nada deste documento. O
par 3 × 4 produziu o κ = 0,14 que motivou esta revisão e que não se sustenta como estimativa de
confiabilidade interanotadores.

### 1.2 Procedência da codificação nº 3

A primeira codificação das 39 devolutivas do modelo **não foi produzida por leitura humana**. Ela
foi gerada por assistente de IA em sessão de trabalho e ficou embutida em
`analises/fm_coding_model.py`, cujo cabeçalho registra a autoria desde junho. A implicação não foi
percebida quando a comparação foi montada: um coeficiente de concordância entre uma codificação
automatizada e uma codificação humana não é uma estimativa de confiabilidade interanotadores,
independentemente de qualquer outro problema do instrumento.

A codificação nº 3 sai da cadeia de evidência do artigo. Ela permanece no material aberto,
identificada pelo que é: uma triagem automatizada prévia, com data e procedência declaradas. Essa
procedência aparece com a mesma clareza no texto do artigo, e não apenas neste protocolo.

### 1.3 O defeito de instrumento entre a nº 3 e a nº 4

A comparação campo a campo entre o codebook v0.2 (usado na nº 3) e o v0.2-Q (usado na nº 4)
mostra que **as oito definições são substantivamente idênticas**. A única diferença de redação é
uma troca de palavra na FM05 e a retirada dos códigos de origem das âncoras.

O único acréscimo substantivo é uma **"Nota específica deste corpus" na FM03**, determinando que
pergunta sobre enredo, personagem ou tema da obra não conta como FM03. Essa nota não existia no
instrumento da nº 3 e foi escrita **a partir dela**: os comentários da codificação automatizada já
registravam esse mesmo julgamento. Uma decisão da primeira passada foi convertida em regra e
entregue à segunda como instrumento.

Soma-se a isso o registro, no mesmo documento, da média de funções por devolutiva apurada na
primeira passada (1,7 contra 3,8 das humanas). A nota metodológica 8 do segundo codificador
descreve exatamente o efeito de ambos: ancoragem e inflação da concordância.

Direção do efeito, para o registro: a informação vazada apontava para menos funções e o segundo
codificador marcou mais (2,77 contra 1,69); a nota da FM03 orientava a não marcar e ele marcou a
função em 21 das 39 devolutivas, contra 4 da primeira passada. Ambas as contaminações operaram no
sentido de **aumentar** a concordância aparente, o que faz do κ = 0,14 um limite superior.

**Alcance do defeito, com a inferência corrigida.** Retirando a FM03 do cálculo, o κ médio vai de
0,138 para 0,149. O que esse número mostra é que **a regra anterior da FM03 não explica, sozinha,
a discrepância observada**. Não se conclui daí que o instrumento não tenha contribuído para ela. A
permanência das divergências em outras funções, em especial a FM07, que apresenta o mesmo número
de divergências, exige examinar os casos discrepantes e as respectivas regras operacionais antes
de determinar a origem dessas diferenças.

A regra de validade mínima da seção 3.0 oferece uma hipótese explícita a examinar: a definição
anterior da FM07 pode ter permitido contar como desafio de ampliação formulações apoiadas em
informação inexistente, interpretação equivocada ou situação comunicativa incoerente. O exame dos
casos discrepantes de FM07 entra no plano de análise (seção 6).

### 1.4 O que mudou da v0.3 para esta versão

| Ponto do parecer de 10/08 | Onde entrou |
|---|---|
| Regra de validade mínima das FMs | seção 3.0, e um item novo em cada uma das oito funções |
| Registro de evidência segmentada com os dois segmentos nas Observações | seção 3.0 |
| A codificação nº 4 sai do cálculo de κ | seções 1.5 e 5 |
| Dois novos codificadores, κ só entre eles | seção 5 |
| Correção da inferência sobre FM03 e FM07 | seção 1.3 |
| Procedência da codificação por IA também no texto do artigo | seção 1.2 |
| Exemplos aos codificadores não podem sair das 39 | seção 3.7, com verificação por programa |

### 1.5 O estatuto da codificação nº 4

A regra de validade mínima altera o instrumento de forma substantiva e pode mudar códigos já
atribuídos na codificação nº 4. Na planilha consolidada existem linhas com uma FM marcada como
presente e a Observação registrando que a devolutiva elogia característica inexistente, converte
um problema em qualidade ou fornece orientação tecnicamente inadequada.

Por isso a codificação nº 4 **não integra o cálculo final de concordância**. Ela é preservada como
parte do percurso metodológico, e com razão: foi a aplicação detalhada dela que tornou visíveis os
limites do instrumento e permitiu chegar a esta versão. Qualquer confronto entre ela e as novas
codificações é exploratório, acontece depois de as duas novas estarem concluídas e preservadas, e
é relatado como tal.

---

## 2. O que este instrumento pede do codificador, em uma frase

Ler cada devolutiva e registrar quais movimentos de mediação ela realiza de fato, marcando 1
apenas quando o movimento existe na forma **e** é compatível com a finalidade que define aquela
função.

---

## 3. Codebook v0.4

### 3.0 Regra de validade mínima das FMs

> Uma ocorrência somente deve ser codificada como 1 quando, além de apresentar as características
> formais da função, for semanticamente compatível com sua finalidade mediadora. Movimentos que se
> apresentem formalmente como uma FM, mas induzam o aluno ao erro, reforcem uma inadequação ou
> proponham uma alteração que possa piorar a produção, devem ser considerados falsos positivos e
> codificados como 0.

Esta é a única mudança conceitual em relação à versão anterior, e vale para as oito funções. A
operacionalização de cada uma está no item *Falso positivo* de cada função, na seção 3.2.

**O que a regra não é.** Ela não é uma avaliação da qualidade da devolutiva. Não se pergunta se o
movimento foi bem realizado, se seria a melhor escolha pedagógica ou se o aluno vai aprender com
ele. Pergunta-se apenas se aquilo que está sendo contado como ocorrência da função é uma
realização válida dela, ou se opera contra a própria finalidade que a define. Uma devolutiva pode
ter todas as funções válidas e ainda assim ser pedagogicamente pobre: isso não é assunto deste
instrumento.

**Registro de evidência segmentada.** Se uma devolutiva contiver, para a mesma FM, um segmento que
a realize validamente e outro que apenas aparente realizá-la, mas seja falso positivo, a função é
codificada como **1** para a devolutiva, porque existe ao menos uma ocorrência válida. Nesse caso
o campo `Observações` é **obrigatório**: identifique o segmento que sustenta o 1 e o segmento
considerado 0, com a justificativa. Assim o resultado binário não apaga o falso positivo
identificado durante a análise.

O mesmo campo é obrigatório sempre que uma função for para 0 **por aplicação da regra de validade
mínima**, e não por ausência do movimento. Escreva, em uma linha, qual é o segmento e por que ele
não vale.

### 3.1 Objeto, unidade e regra de evidência

**Objeto.** 39 devolutivas produzidas por um modelo de linguagem sobre textos de aluno. Os textos
de aluno são sintéticos, escritos pela equipe de pesquisa, e simulam produções de 8º e 9º ano.

**Unidade de codificação.** A devolutiva integral. Cada devolutiva recebe um vetor binário de nove
decisões (FM01 a FM08 e MTL).

**Evidência segmentada.** As evidências de cada função aparecem em segmentos específicos da
devolutiva. Basta um segmento válido para marcar a função, e um problema localizado em um segmento
não anula uma função adequadamente realizada em outro. A recíproca também vale e fica registrada
para evitar leitura indevida do vetor: a presença de uma função não torna adequada a devolutiva
inteira.

**Regra de evidência mínima.** Na dúvida sobre a presença do movimento, não marcar.

### 3.2 As oito funções

**FM01. Reconhecer competência**
- *Definição:* afirmar, de forma específica, algo que o aluno fez bem no texto (uma escolha, uma compreensão, um recurso bem empregado).
- *Inclusão:* o elogio nomeia o que foi bem feito (compreensão do enredo, uso de conectivo, organização, vocabulário).
- *Exclusão:* encorajamento genérico voltado ao futuro ("continue se dedicando", "está no caminho certo") sem nomear uma competência, isso é FM08.
- *Falso positivo (marcar 0):* elogio que apresenta como competência uma inadequação, erro ou vício da produção, ou que atribui ao aluno uma competência não sustentada pelo texto.
- *Âncora:* "Parabéns! Você identificou um dos acontecimentos mais importantes do conto: a confiança de Camilo nas palavras da cartomante e o desfecho inesperado da história."
- *Caso-limite:* "Continue se dedicando, pois já demonstrou compreender a história." A segunda oração nomeia uma competência, logo FM01; o "continue se dedicando" isolado seria só FM08.
- *Falso positivo, exemplo:* "Parabéns pelo uso variado de conectivos: 'e', 'e daí', 'e aí' deixaram o texto fluido." A repetição do mesmo conector é apresentada como qualidade. FM01 = 0.

**FM02. Nomear o problema**
- *Definição:* indicar ao aluno que o texto é inadequado em algum aspecto.
- *Inclusão:* o problema é dito (repetição, pronome ambíguo, conector contraditório, ordem embaralhada, períodos curtos justapostos, buraco narrativo). Inclui apontar que algo está ausente, insuficiente ou não atende ao gênero, ainda que em tom de convite.
- *Exclusão:* levar o aluno a descobrir o problema por pergunta, isso é FM03. Pedir reescrita sem indicar o que está inadequado, isso é FM06. Texto elogiado sem apontar insuficiência, não marcar.
- *Falso positivo (marcar 0):* indicação de problema inexistente, ou caracterização de um recurso adequado como inadequação, quando isso puder levar o aluno a corrigir algo que não constitui problema.
- *Âncora:* "Você usou 'ele' muitas vezes, sem deixar claro a quem se referia o pronome a cada vez."
- *Caso-limite:* "A palavra 'portanto' não parece adequada. Por qual palavra você poderia substituí-la?" O primeiro trecho é FM02, o segundo é FM03. Mesma devolutiva, duas funções.
- *Falso positivo, exemplo:* o aluno escreveu "Assim que abriu a porta, o bonde passou", e a devolutiva diz: "Cuidado, 'assim que' não é expressão adequada na escrita; troque sempre por 'quando'." O problema não existe e a regra é falsa. FM02 = 0.

**FM03. Provocar reflexão**
- *Definição:* marcar FM03 quando a pergunta estiver ancorada em um elemento identificável da produção do aluno e for construída de modo que uma resposta pertinente exija explicar, justificar, relacionar, reconsiderar ou desenvolver esse elemento, ainda que essa operação não seja solicitada explicitamente. A pergunta não deve fornecer antecipadamente a resposta.
- *Inclusão:* pergunta ancorada em elemento identificável do texto do aluno, mesmo quando a operação reflexiva não é pedida em palavras. Pergunta sobre a obra citada conta, desde que leve o estudante a reexaminar uma escolha narrativa, interpretativa ou argumentativa presente no próprio texto.
- *Exclusão:* pergunta retórica que já contém a correção dentro de si, conta como FM02. Pergunta que não se ancora em nenhum elemento identificável da produção do aluno.
- *Falso positivo (marcar 0):* pergunta construída sobre informação inexistente, leitura equivocada ou premissa falsa, quando por essa razão a reflexão solicitada não possa ser sustentada pela produção do aluno.
- *Âncora:* "O que exatamente te fez rir? Por que o final é chocante?"
- *Caso-limite:* "(se era horrível, o natural seria ele querer sair, então o 'mas' não cabe aqui)". A resposta já está dada no parêntese, logo FM02 e não FM03.
- *Falso positivo, exemplo:* "Por que você escolheu terminar o texto com a morte da personagem?", num texto em que ninguém morre. FM03 = 0.

**FM04. Oferecer pista**
- *Definição:* fornecer ajuda concreta em direção à solução sem reescrever o texto do aluno.
- *Inclusão:* listar substituições possíveis, conectores, marcadores temporais como repertório a usar. Inclui indicar o aspecto ou conteúdo específico a desenvolver, ou a estratégia a seguir.
- *Exclusão:* apresentar uma frase já reescrita do aluno, isso é FM05. Apenas mandar reescrever sem dar o caminho, isso é FM06. **Fronteira com FM03:** a mesma orientação dada como diretiva é FM04; dada como pergunta é FM03.
- *Falso positivo (marcar 0):* pista incorreta, incompatível com o problema identificado, ou que oriente o aluno para uma solução capaz de introduzir ou agravar uma inadequação.
- *Âncora:* "para evitar essa repetição, usar o nome da cartomante, ou usar 'ela' ou 'a mulher'."
- *Caso-limite:* "Você pode utilizar marcadores temporais como: Primeiro... Depois... Mais tarde... Finalmente..." Oferece ferramentas, mas não monta a frase do aluno, logo FM04 e não FM05.
- *Falso positivo, exemplo:* "Para ligar as duas ideias que se opõem, use 'portanto'." O conector indicado é conclusivo, não adversativo, e a pista conduz ao erro. FM04 = 0.

**FM05. Modelar parcialmente**
- *Definição:* demonstrar a solução com um exemplo reescrito, idealmente do próprio trecho do aluno.
- *Inclusão:* o interlocutor escreve um exemplo que materializa o conserto.
- *Exclusão:* apenas nomear palavras ou recursos a usar, sem montar o exemplo, isso é FM04.
- *Falso positivo (marcar 0):* modelo que não realiza adequadamente a solução proposta, que preserva o problema que deveria ajudar a resolver, ou que introduz nova inadequação relevante.
- *Âncora:* "Sugestão de ampliação: 'Sem saída, desceu pelo elevador; logo depois, percebeu que a confusão só aumentava, pois os moradores começaram a observá-lo com espanto...'"
- *Caso-limite:* "Tente usar palavras que indiquem o tempo para unir as frases, como por exemplo: 'Assim que abriu a porta, o bonde passou.'" É exemplo-modelo, ainda que não seja a frase exata do aluno; a fronteira com FM04 é a presença de uma frase pronta.
- *Falso positivo, exemplo:* o problema é a ambiguidade do pronome, e o modelo oferecido é "Ele saiu e ele voltou depois, quando ele viu que ele tinha esquecido a chave." O exemplo repete o problema que deveria resolver. FM05 = 0.

**FM06. Propor revisão**
- *Definição:* propor ou solicitar explicitamente a reescrita ou correção do que já está no texto.
- *Inclusão:* "vamos reescrever", "o texto precisa ser reescrito", "reorganize seguindo a ordem".
- *Exclusão:* desafio de acrescentar conteúdo novo que não estava lá, isso é FM07.
- *Falso positivo (marcar 0):* proposta de revisão fundamentada em problema inexistente, ou que oriente uma alteração capaz de tornar a produção menos adequada.
- *Âncora:* "Vamos reescrever esse trecho a partir dessas dicas?!"
- *Caso-limite:* "O texto precisa ser reescrito." FM06 puro, sem pista e sem modelo.
- *Falso positivo, exemplo:* "Reescreva o trecho tirando as vírgulas entre as orações, porque vírgula antes de 'mas' é erro." A revisão proposta piora o texto. FM06 = 0.

**FM07. Desafiar ampliação**
- *Definição:* desafiar o aluno a ir além de corrigir: aprofundar, acrescentar opinião, análise, detalhe, reflexão que enriqueçam o texto.
- *Inclusão:* "acrescente sua opinião", "aprofunde sua análise", "desenvolva mais".
- *Exclusão:* consertar um problema existente, isso é FM06. Reescrever para o aluno, isso é FM05.
- *Falso positivo (marcar 0):* desafio apoiado em elementos inexistentes, premissas falsas ou interpretações fabricadas pela devolutiva, quando a ampliação proposta conduzir o aluno a desenvolver algo que não encontra sustentação no texto ou na situação comunicativa. Uma formulação pode ter superficialmente a aparência de desafio de ampliação e ainda assim não realizar validamente a FM07: é o caso da pergunta que inventa um acontecimento e pede ao aluno que o interprete, e é o caso da formulação que perde a situação comunicativa e se refere à produção analisada como se não fosse o texto do próprio aluno.
- *Âncora:* "Desafio para a reescrita: acrescentar uma frase avaliando a história e utilizar menos repetições." A primeira metade é FM07; "menos repetições" é FM06.
- *Caso-limite:* "O desafio que vou te dar é transformar essas 10 frases em 3 ou 4 frases mais longas e conectadas." Reestruturar o que existe é FM06; só seria FM07 se pedisse conteúdo novo.
- *Falso positivo, exemplo 1:* "Agora acrescente um parágrafo explicando por que o narrador escolheu o cachorro como confidente", num texto sem cachorro e sem confidente. FM07 = 0.
- *Falso positivo, exemplo 2:* "Comente o que o autor deste texto quis dizer e proponha uma continuação." O texto é do próprio aluno, e a formulação o trata como texto de terceiro. FM07 = 0.

**FM08. Reforçar autonomia**
- *Definição:* movimento de fechamento que afirma a capacidade ou agência do aluno e projeta continuidade do trabalho.
- *Inclusão:* "está no caminho certo", "vamos seguir em frente", "você consegue", convite à continuidade.
- *Exclusão:* elogio que nomeia uma competência específica demonstrada no texto, isso é FM01.
- *Falso positivo (marcar 0):* formulação que tem apenas aparência de encorajamento, sem afirmar capacidade ou agência do aluno nem projetar continuidade do trabalho. Também não é realização válida o encorajamento que reforça explicitamente a continuidade de uma orientação identificada como inadequada.
- *Âncora:* "Você teve um ótimo começo! Vamos seguir em frente!"
- *Caso-limite:* "Continue se dedicando, pois está no caminho certo." Afirmação prospectiva da capacidade, sem nomear o que foi feito, logo FM08.
- *Falso positivo, exemplo:* "Continue assim, trocando sempre as vírgulas por pontos como eu sugeri." Reforça a continuidade de uma orientação inadequada. FM08 = 0.

### 3.3 A variável MTL

**Sigla:** MTL, contração de MeTaLinguístico. **Nome por extenso:** foco metalinguístico no texto
do aluno. Binária, uma decisão por devolutiva, preenchida em passada separada.

> A devolutiva trata o texto que o aluno escreveu como objeto de atenção, comentando alguma
> característica da sua construção? Ou fica no plano do conteúdo da obra que o aluno citou, ou em
> elogio e pergunta genéricos que não se ancoram em nada do texto produzido?

- **Marcar 1** quando a devolutiva se refere a alguma propriedade da escrita do aluno: repetição, uso de conectivo, clareza referencial, encadeamento das ideias, organização, progressão, pontuação, escolha de palavra.
- **Marcar 0** quando a devolutiva conversa sobre o enredo, os personagens ou o tema da obra, ou quando faz elogio ou pergunta que caberiam em qualquer texto.

**Não exigir terminologia técnica.** "Você repetiu muito 'a cartomante'; dá para trocar por outra
palavra?" é MTL = 1 mesmo sem a palavra "coesão". "Seu texto tem boa coesão" é MTL = 0 se o elogio
for de fórmula e não apontar nada específico. Usar o termo não basta.

**A regra de validade mínima não se aplica à MTL.** A MTL registra o objeto de que a devolutiva
fala, não a correção do que ela diz sobre esse objeto. Um comentário equivocado sobre a pontuação
do aluno continua sendo um comentário sobre a escrita do aluno, logo MTL = 1. Se esse mesmo
comentário for um falso positivo de FM02, isso é decidido na coluna FM02, não aqui.

**Esta definição não muda em relação à v0.2-Q e à v0.3.**

### 3.4 Fronteiras entre MTL e as FMs

As FMs perguntam *que movimento de mediação a devolutiva faz*. A MTL pergunta *sobre que objeto
ela faz esse movimento*. São eixos ortogonais: nenhuma FM implica MTL = 1, e não existe regra
aritmética ligando as duas colunas. Exemplos inventados para o instrumento:

| Exemplo | FM | MTL |
|---|:---:|:---:|
| "Você usou 'ele' várias vezes e nem sempre dá para saber de quem se trata." | FM02 | 1 |
| "Você trocou o nome do personagem: quem procurou a cartomante foi Camilo, não Vilela." | FM02 | 0 |
| "Você começou três frases seguidas com 'A Casa Verde'. Que efeito isso causa em quem lê?" | FM03 | 1 |
| "Releia o capítulo em que a Casa Verde é esvaziada e anote o que acontece." | FM04 | 0 |
| "Seu texto ficou muito bom, parabéns!" | nenhuma | 0 |

### 3.5 Independência da codificação

Este protocolo **não informa** ao codificador nenhum resultado agregado de passadas anteriores,
nem frequência esperada de funções, nem qual configuração é comum neste corpus. Nenhuma regra
deste codebook foi derivada de ocorrências observadas no material a codificar.

Os dois codificadores trabalham **sem contato entre si** durante a tarefa: não comparam decisões,
não discutem casos-limite um com o outro e não trocam as planilhas. Dúvidas de interpretação vão
para o pesquisador responsável, que responde apenas com o que já está escrito neste documento, e
registra a pergunta.

Também não consultar o artigo, o repositório público do estudo nem qualquer material anterior
sobre estas devolutivas. Se você já conhece esse material por outra via, avise antes de começar.

**Desacordo com o codebook.** Se alguma definição parecer inadequada durante a tarefa, registrar
em `Observações` e seguir com a definição como está. Não ajustar o codebook no meio da passada. Um
desacordo registrado vale mais para o estudo do que uma concordância obtida por reconciliação.

### 3.6 Escopo: presença funcional não é qualidade

Este instrumento registra **se** um movimento de mediação ocorre, com a validade mínima definida
na seção 3.0, e é silencioso sobre **o quão bem** ele é realizado. Duas devolutivas podem receber
o mesmo vetor binário e ter qualidades pedagógicas muito diferentes.

A distinção que sustenta o recorte: a devolutiva é o produto textual observável, e a mediação é o
processo que ocorre na interação. Saber se o aluno compreendeu a orientação, se ela provocou
reflexão, se foi apropriada durante a revisão e como interferiu na autoria exige dados da
interação, e fica para o estudo piloto e trabalhos posteriores.

### 3.7 Procedência dos exemplos

Nenhum exemplo, âncora ou caso-limite deste protocolo e do anexo de calibração sai das 39
devolutivas a codificar. Todos são construídos para o instrumento ou vêm do corpus humano de
referência (as 65 devolutivas dos cinco professores), que não faz parte do material a codificar.

Isso é verificado por programa, e não por leitura: `verifica_exemplos.py`, neste mesmo diretório,
normaliza acentuação e caixa e falha se qualquer trecho citado nos dois documentos aparecer nas 39
devolutivas.

---

## 4. O que cada codificador recebe

- `GUIA_PROFESSOR`, documento único de trabalho: as oito definições e a da MTL em linguagem de professor, um exemplo por função, três exemplos da regra de validade mínima, as regras de independência e o prazo. É a versão operacional deste protocolo, sem alteração de definição.
- Uma planilha individual no Google Sheets, com as 39 devolutivas embaralhadas, sem indicação de cenário, repetição ou ordem original, com as colunas `ID`, `Texto do aluno`, `Devolutiva`, `FM01` a `FM08`, `MTL` e `Observações`.

Não recebe: este protocolo, o anexo de calibração, nenhuma codificação anterior, a chave de
decegamento, os resultados já apurados, nem a planilha do outro codificador. O protocolo e o anexo
são documentos internos, escritos para os autores e para o relato no artigo; entregá-los à tarefa
acrescentaria histórico do estudo e plano de análise, que são justamente o tipo de informação que
pode ancorar a leitura.

Os dois recebem exatamente o mesmo material e os mesmos identificadores `R01` a `R39`, o que é
condição para o cálculo de concordância linha a linha.

---

## 5. Procedimento

1. Discutir e aprovar entre os autores esta versão do protocolo.
2. Congelar a versão antes de qualquer nova codificação (seção 9).
3. Entregar o mesmo protocolo aos **dois** novos codificadores independentes, sem acesso às codificações anteriores.
4. Preservar separadamente as duas codificações, em arquivos datados, antes de qualquer confronto entre elas.
5. Calcular a concordância **exclusivamente entre as duas novas codificações**.
6. Consolidar os resultados pelos 13 cenários, considerando as três execuções de cada.
7. Revisar método, resultados, discussão, limitações e conclusões do artigo conforme os resultados.
8. Relatar aos avaliadores, com transparência, o percurso que levou à revisão do instrumento e à realização das novas codificações.

**Como codificar.** Duas varreduras separadas sobre o mesmo material: primeiro as oito FMs nas 39
linhas, depois a MTL nas 39 linhas. A separação existe para reduzir o arrasto de um eixo sobre o
outro, sobretudo entre FM02 e MTL, que são vizinhos conceituais.

**Quando o confronto acontece.** As justificativas e observações qualitativas de cada codificação
permanecem independentes. A discussão das divergências ocorre somente depois de concluídos e
preservados os dois registros.

**Preservação e errata.** O codebook v0.2-Q vai para o material aberto como foi usado, acompanhado
de errata que identifica as três passagens defeituosas: o registro da média da passada anterior, a
nota específica da FM03 e o reforço dela na seção de fronteiras. Nenhum código original é alterado
silenciosamente. As codificações nº 3 e nº 4 são preservadas como foram entregues.

---

## 6. Plano de análise, fixado antes da anotação

Sobre o par **codificador A × codificador B**:

- κ de Cohen por função (FM01 a FM08) e para a MTL, com bandas de Landis e Koch (1977).
- Concordância bruta ao lado de cada κ, sempre.
- Prevalência observada em cada codificador.
- PABAK (Byrt et al., 1993) nas categorias de base rara ou saturada, ao lado do κ e nunca no lugar dele, com sinalização explícita do paradoxo do κ (Feinstein e Cicchetti, 1990).
- **Consolidação por cenário:** as três execuções de cada um dos 13 cenários agrupadas, reportando estabilidade e variação das FMs e da MTL entre execuções do mesmo cenário.
- **Exame dos casos discrepantes de FM07**, conforme a seção 1.3, verificando se a divergência se concentra em formulações apoiadas em elemento inexistente ou em perda da situação comunicativa.
- Nenhuma categoria é omitida por ter resultado desfavorável.

Sobre a **validade de construto da métrica da RQ2**: a régua lexical executada por programa
(`src/metalinguistic_adherence.py`) é confrontada com a coluna MTL de cada um dos dois
codificadores, o que fornece duas leituras especialistas independentes do mesmo construto.

Sobre a **codificação nº 4**: qualquer comparação com ela é exploratória, feita depois de as duas
novas codificações estarem preservadas, e relatada como percurso, não como confiabilidade.

---

## 7. O que vai para o artigo em cada cenário de resultado

| Resultado do κ médio das FMs | O que é escrito |
|---|---|
| ≥ 0,61 | A distribuição por função é reportada como medida, com o vetor de κ ao lado. |
| 0,41 a 0,60 | A distribuição é mantida com ressalva explícita de que a leitura função a função é indicativa; a conclusão se apoia no padrão agregado. |
| < 0,41, ou κ < 0,40 em FM02, FM04 ou FM06 | As funções que sustentam a conclusão perdem estatuto de evidência quantitativa; a tabela é rebaixada a ilustração qualitativa e o achado é reformulado como padrão, não como medida. |

Em qualquer dos três casos os números são publicados, e o histórico da seção 1 deste documento é
narrado no método, incluindo a procedência da codificação nº 3.

---

## 8. Limitações já assumidas

- **Codificação binária.** O instrumento reduz a devolutiva a presenças e ausências. Fenômenos de mediação são contextuais e não lineares, e o vetor binário não os captura. As `Observações` existem em parte para guardar o que o binário perde.
- **Validade mínima não é qualidade.** A regra da seção 3.0 examina apenas a compatibilidade semântica entre o movimento e a finalidade da função. As dimensões de qualidade que dependem de aluno real em interação ficam para o piloto.
- **Juízo especialista único por passada.** Cada codificação é de uma pessoa, não de um painel.
- **Viés de formato.** O esquema de saída do modelo força um movimento de reconhecimento e abre espaço para pergunta, de modo que FM01 e FM03 podem estar presentes por imposição do formato. Isso é problema da interpretação no artigo, não da codificação.
- **Textos de aluno sintéticos.** O corpus não contém produção real de estudante, o que limita a generalização e é declarado no artigo.

---

## 9. Congelamento e concordância dos autores

Esta versão precisa da concordância explícita dos três autores antes de qualquer nova codificação.
Registrada a concordância, o documento é congelado: nenhuma alteração de definição entra depois
que a primeira codificação começar. Se um erro material for encontrado durante a tarefa, ele vira
errata datada, anexada ao protocolo, e não edição silenciosa.

| Autor | Concordância | Data |
|---|---|---|
| Randerson O. M. Rebouças | sim, redação desta versão | 22/08/2026 |
| Marcelo Magalhães Foohs | parecer de 10/08/2026, incorporado integralmente nesta versão | 10/08/2026 |
| Rosa Maria Vicari | "concordo totalmente" (leitura técnica do v0.3 e do parecer) | 11/08/2026 |

---

## Referências do plano de análise

- Byrt, T., Bishop, J., Carlin, J. B. (1993). Bias, prevalence and kappa. *Journal of Clinical Epidemiology*, 46(5), 423-429.
- Feinstein, A. R., Cicchetti, D. V. (1990). High agreement but low kappa: I. The problems of two paradoxes. *Journal of Clinical Epidemiology*, 43(6), 543-549.
- Landis, J. R., Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159-174.
