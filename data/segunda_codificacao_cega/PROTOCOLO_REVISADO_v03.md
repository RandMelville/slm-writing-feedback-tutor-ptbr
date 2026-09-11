# Protocolo revisado da codificação das Funções de Mediação (v0.3)

**Estudo:** SLMs para tutoria de escrita offline em português do Brasil (artigo JBCS, revisão R1)
**Versão:** 0.3
**Data:** 5 de agosto de 2026
**Redação:** Randerson O. M. Rebouças
**Status:** aguardando concordância explícita dos três autores. Nenhuma nova codificação
começa antes disso.

Este documento revisa o protocolo de codificação a partir das notas metodológicas
registradas pelo segundo codificador na planilha consolidada de 30 de julho de 2026. Ele é
o passo 1 da sequência proposta pelo Prof. Marcelo e substitui integralmente o
`codebook_respostas_modelo.md` (v0.2-Q).

---

## 1. Histórico: o que aconteceu até aqui

### 1.1 As codificações já produzidas

| # | Quando | Quem codificou | Material | Instrumento |
|---|---|---|---|---|
| 1 | jun/2026 | Randerson (leitura) | as 65 devolutivas dos cinco professores | codebook v0.1, depois v0.2 |
| 2 | jun/2026 | Marcelo, às cegas | 20 das mesmas devolutivas de professores | codebook v0.1 |
| 3 | jun/2026 | **assistente de IA** | as 39 devolutivas do modelo (Qwen 2.5 3B) | codebook v0.2 |
| 4 | jul/2026 | Marcelo, às cegas | as mesmas 39 devolutivas do modelo | codebook v0.2-Q |

O par 1 × 2 produziu o κ = 0,83 do corpus humano, que não é afetado por nada deste
documento. O par 3 × 4 produziu o κ = 0,14 que motivou esta revisão.

### 1.2 Procedência da codificação nº 3

A primeira codificação das 39 devolutivas do modelo **não foi produzida por leitura
humana**. Ela foi gerada por assistente de IA em sessão de trabalho e ficou embutida em
`analises/fm_coding_model.py`, cujo cabeçalho registra a autoria desde junho. A implicação
não foi percebida quando a comparação foi montada: um coeficiente de concordância entre uma
codificação automatizada e uma codificação humana **não é uma estimativa de confiabilidade
interanotadores**, independentemente de qualquer outro problema do instrumento.

Isso é registrado aqui porque o passo 6 da sequência acordada exige narrar com transparência
o que motivou a recodificação, e porque a codificação nº 3 sai da cadeia de evidência do
artigo. Ela permanece no material aberto, identificada pelo que é: uma triagem automatizada
prévia, com data e procedência declaradas.

### 1.3 O defeito de instrumento entre a nº 3 e a nº 4

A comparação campo a campo entre o codebook v0.2 (usado na nº 3) e o v0.2-Q (usado na nº 4)
mostra que **as oito definições são substantivamente idênticas**. A única diferença de
redação é uma troca de palavra na FM05 e a retirada dos códigos de origem das âncoras.

O único acréscimo substantivo é uma **"Nota específica deste corpus" na FM03**, com reforço
na seção de fronteiras, determinando que pergunta sobre enredo, personagem ou tema da obra
não conta como FM03. Essa nota não existia no instrumento da nº 3 e foi escrita **a partir
dela**: os comentários da codificação automatizada já registravam esse mesmo julgamento.
Uma decisão da primeira passada foi convertida em regra e entregue à segunda como
instrumento.

Soma-se a isso o registro, no mesmo documento, da média de funções por devolutiva apurada na
primeira passada (1,7 contra 3,8 das humanas). A nota metodológica 8 do segundo codificador
descreve exatamente o efeito de ambos: ancoragem e inflação da concordância.

Verificação da direção do efeito, para o registro: a informação vazada apontava para menos
funções e o segundo codificador marcou mais (2,77 contra 1,69); a nota da FM03 orientava a
não marcar e ele marcou a função em 21 das 39 devolutivas, contra 4 da primeira passada.
Ambas as contaminações operaram no sentido de **aumentar** a concordância aparente, o que
faz do κ = 0,14 um limite superior.

Verificação do alcance: retirando a FM03 do cálculo, o κ médio vai de 0,138 para 0,149. O
defeito de instrumento, portanto, **não explica** o resultado. A FM07, cuja definição é
idêntica nos dois instrumentos, apresenta o mesmo número de divergências que a FM03.

---

## 2. O que muda neste protocolo, nota a nota

| Nota | Registro do segundo codificador | O que muda aqui |
|---|---|---|
| 5 | Nova redação da FM03 | Substitui integralmente a definição e a nota da FM03 (seção 3.2) |
| 6 | Unidade integral e evidência segmentada | Regra de unidade reescrita (seção 3.1) |
| 8 | Independência da segunda codificação | Retirados o agregado da passada anterior e toda orientação derivada de ocorrências frequentes do corpus (seção 3.5) |
| 9 | Confronto entre codificadores | Fixado o momento do confronto (seção 4.4) |
| 10 | Congelamento do codebook | Política de preservação e errata (seção 4.5) |
| 11 | O binário e o complexo | Declarado como limitação do instrumento (seção 7) |
| 2, 3, 7 | Presença funcional não é qualidade | Delimitação de escopo (seção 3.6) |
| 1, 4, 12, 13 | Definição de qualidade e agenda futura | Fora do escopo desta rodada, registrado na seção 7 |

---

## 3. Codebook v0.3

### 3.1 Objeto, unidade e regra de evidência

**Objeto.** As 39 saídas do modelo `qwen2.5:3b-instruct`, correspondentes a 13 cenários com
3 execuções cada. Os textos de aluno são sintéticos, escritos pela equipe de pesquisa.

**Unidade de codificação.** A devolutiva integral. Cada devolutiva recebe um vetor binário
de nove decisões (FM01 a FM08 e MTL).

**Evidência segmentada (nota 6).** As evidências de cada função aparecem em segmentos
específicos da devolutiva. Basta um segmento que satisfaça a definição para marcar a função,
e um problema localizado em um segmento não anula uma função adequadamente realizada em
outro. A recíproca também vale e é registrada aqui para evitar leitura indevida do vetor: a
presença de uma função não torna adequada a devolutiva inteira.

**Regra de evidência mínima.** Na dúvida, não marcar.

### 3.2 As oito funções

**FM01. Reconhecer competência**
- *Definição:* afirmar, de forma específica, algo que o aluno fez bem no texto (uma escolha, uma compreensão, um recurso bem empregado).
- *Inclusão:* o elogio nomeia o que foi bem feito (compreensão do enredo, uso de conectivo, organização, vocabulário).
- *Exclusão:* encorajamento genérico voltado ao futuro ("continue se dedicando", "está no caminho certo") sem nomear uma competência, isso é FM08.
- *Âncora:* "Parabéns! Você identificou um dos acontecimentos mais importantes do conto: a confiança de Camilo nas palavras da cartomante e o desfecho inesperado da história."
- *Caso-limite:* "Continue se dedicando, pois já demonstrou compreender a história." A segunda oração nomeia uma competência, logo FM01; o "continue se dedicando" isolado seria só FM08.

**FM02. Nomear o problema**
- *Definição:* indicar ao aluno que o texto é inadequado em algum aspecto.
- *Inclusão:* o problema é dito (repetição, pronome ambíguo, conector contraditório, ordem embaralhada, períodos curtos justapostos, buraco narrativo). Inclui apontar que algo está ausente, insuficiente ou não atende ao gênero, ainda que em tom de convite.
- *Exclusão:* levar o aluno a descobrir o problema por pergunta, isso é FM03. Pedir reescrita sem indicar o que está inadequado, isso é FM06. Texto elogiado sem apontar insuficiência, não marcar.
- *Âncora:* "Você usou 'ele' muitas vezes, sem deixar claro a quem se referia o pronome a cada vez."
- *Caso-limite:* "A palavra 'portanto' não parece adequada. Por qual palavra você poderia substituí-la?" O primeiro trecho é FM02, o segundo é FM03. Mesma devolutiva, duas funções.

**FM03. Provocar reflexão** *(redação integral da nota metodológica 5)*
- *Definição:* marcar FM03 quando a pergunta estiver ancorada em um elemento identificável da produção do aluno e for construída de modo que uma resposta pertinente exija explicar, justificar, relacionar, reconsiderar ou desenvolver esse elemento, ainda que essa operação não seja solicitada explicitamente. A pergunta não deve fornecer antecipadamente a resposta.
- *Inclusão:* pergunta ancorada em elemento identificável do texto do aluno, mesmo quando a operação reflexiva não é pedida em palavras.
- *Exclusão:* pergunta retórica que já contém a correção dentro de si, conta como FM02. Pergunta que não se ancora em nenhum elemento identificável da produção do aluno.
- *Âncora:* "O que exatamente te fez rir? Por que o final é chocante?"
- *Caso-limite:* "(se era horrível, o natural seria ele querer sair, então o 'mas' não cabe aqui)". A resposta já está dada no parêntese, logo FM02 e não FM03.
- *Mudança em relação à v0.2-Q, registrada:* a versão anterior excluía da FM03 toda pergunta sobre enredo, personagem ou tema da obra. Essa exclusão **cai**. Uma pergunta sobre a obra pode levar o estudante a reexaminar uma escolha narrativa, interpretativa ou argumentativa presente no próprio texto, e nesse caso é FM03. O critério passa a ser a ancoragem em elemento identificável da produção do aluno, não o assunto da pergunta.

**FM04. Oferecer pista**
- *Definição:* fornecer ajuda concreta em direção à solução sem reescrever o texto do aluno.
- *Inclusão:* listar substituições possíveis, conectores, marcadores temporais como repertório a usar. Inclui indicar o aspecto ou conteúdo específico a desenvolver, ou a estratégia a seguir.
- *Exclusão:* apresentar uma frase já reescrita do aluno, isso é FM05. Apenas mandar reescrever sem dar o caminho, isso é FM06. **Fronteira com FM03:** a mesma orientação dada como diretiva é FM04; dada como pergunta é FM03.
- *Âncora:* "para evitar essa repetição, usar o nome da cartomante, ou usar 'ela' ou 'a mulher'."
- *Caso-limite:* "Você pode utilizar marcadores temporais como: Primeiro... Depois... Mais tarde... Finalmente..." Oferece ferramentas, mas não monta a frase do aluno, logo FM04 e não FM05.

**FM05. Modelar parcialmente**
- *Definição:* demonstrar a solução com um exemplo reescrito, idealmente do próprio trecho do aluno.
- *Inclusão:* o interlocutor escreve um exemplo que materializa o conserto.
- *Exclusão:* apenas nomear palavras ou recursos a usar, sem montar o exemplo, isso é FM04.
- *Âncora:* "Sugestão de ampliação: 'Sem saída, desceu pelo elevador; logo depois, percebeu que a confusão só aumentava, pois os moradores começaram a observá-lo com espanto...'"
- *Caso-limite:* "Tente usar palavras que indiquem o tempo para unir as frases, como por exemplo: 'Assim que abriu a porta, o bonde passou.'" É exemplo-modelo, ainda que não seja a frase exata do aluno; a fronteira com FM04 é a presença de uma frase pronta.

**FM06. Propor revisão**
- *Definição:* propor ou solicitar explicitamente a reescrita ou correção do que já está no texto.
- *Inclusão:* "vamos reescrever", "o texto precisa ser reescrito", "reorganize seguindo a ordem".
- *Exclusão:* desafio de acrescentar conteúdo novo que não estava lá, isso é FM07.
- *Âncora:* "Vamos reescrever esse trecho a partir dessas dicas?!"
- *Caso-limite:* "O texto precisa ser reescrito." FM06 puro, sem pista e sem modelo.

**FM07. Desafiar ampliação**
- *Definição:* desafiar o aluno a ir além de corrigir: aprofundar, acrescentar opinião, análise, detalhe, reflexão que enriqueçam o texto.
- *Inclusão:* "acrescente sua opinião", "aprofunde sua análise", "desenvolva mais".
- *Exclusão:* consertar um problema existente, isso é FM06. Reescrever para o aluno, isso é FM05.
- *Âncora:* "Desafio para a reescrita: acrescentar uma frase avaliando a história e utilizar menos repetições." A primeira metade é FM07; "menos repetições" é FM06.
- *Caso-limite:* "O desafio que vou te dar é transformar essas 10 frases em 3 ou 4 frases mais longas e conectadas." Reestruturar o que existe é FM06; só seria FM07 se pedisse conteúdo novo.

**FM08. Reforçar autonomia**
- *Definição:* movimento de fechamento que afirma a capacidade ou agência do aluno e projeta continuidade do trabalho.
- *Inclusão:* "está no caminho certo", "vamos seguir em frente", "você consegue", convite à continuidade.
- *Exclusão:* elogio que nomeia uma competência específica demonstrada no texto, isso é FM01.
- *Âncora:* "Você teve um ótimo começo! Vamos seguir em frente!"
- *Caso-limite:* "Continue se dedicando, pois está no caminho certo." Afirmação prospectiva da capacidade, sem nomear o que foi feito, logo FM08.

### 3.3 A variável MTL

**Sigla:** MTL, contração de MeTaLinguístico. **Nome por extenso:** foco metalinguístico no
texto do aluno. Binária, uma decisão por devolutiva, preenchida em passada separada.

> A devolutiva trata o texto que o aluno escreveu como objeto de atenção, comentando alguma
> característica da sua construção? Ou fica no plano do conteúdo da obra que o aluno citou,
> ou em elogio e pergunta genéricos que não se ancoram em nada do texto produzido?

- **Marcar 1** quando a devolutiva se refere a alguma propriedade da escrita do aluno: repetição, uso de conectivo, clareza referencial, encadeamento das ideias, organização, progressão, pontuação, escolha de palavra.
- **Marcar 0** quando a devolutiva conversa sobre o enredo, os personagens ou o tema da obra, ou quando faz elogio ou pergunta que caberiam em qualquer texto.

**Não exigir terminologia técnica.** "Você repetiu muito 'a cartomante'; dá para trocar por
outra palavra?" é MTL = 1 mesmo sem a palavra "coesão". "Seu texto tem boa coesão" é MTL = 0
se o elogio for de fórmula e não apontar nada específico. Usar o termo não basta.

**Esta definição não muda em relação à v0.2-Q.** Ela é a mesma congelada em 27 de julho de
2026 e é a que foi usada na codificação nº 4.

### 3.4 Fronteiras entre MTL e as FMs

As FMs perguntam *que movimento de mediação a devolutiva faz*. A MTL pergunta *sobre que
objeto ela faz esse movimento*. São eixos ortogonais: nenhuma FM implica MTL = 1, e não
existe regra aritmética ligando as duas colunas. Exemplos inventados para o instrumento, sem
correspondência com nenhuma linha da planilha:

| Exemplo | FM | MTL |
|---|:---:|:---:|
| "Você usou 'ele' várias vezes e nem sempre dá para saber de quem se trata." | FM02 | 1 |
| "Você trocou o nome do personagem: quem procurou a cartomante foi Camilo, não Vilela." | FM02 | 0 |
| "Você começou três frases seguidas com 'A Casa Verde'. Que efeito isso causa em quem lê?" | FM03 | 1 |
| "Releia o capítulo em que a Casa Verde é esvaziada e anote o que acontece." | FM04 | 0 |
| "Seu texto ficou muito bom, parabéns!" | nenhuma | 0 |

### 3.5 Independência da codificação (nota 8)

Este protocolo **não informa** ao codificador nenhum resultado agregado de passadas
anteriores, nem frequência esperada de funções, nem qual configuração é comum neste corpus.
Nenhuma regra deste codebook foi derivada de ocorrências observadas no material a codificar.
Toda orientação vem das definições e de exemplos inventados ou do corpus humano de
referência, que não faz parte do material a codificar.

**Desacordo com o codebook.** Se alguma definição parecer inadequada durante a tarefa,
registrar em `Observações` e seguir com a definição como está. Não ajustar o codebook no
meio da passada. Um desacordo registrado vale mais para o estudo do que uma concordância
obtida por reconciliação.

### 3.6 Escopo: presença funcional não é qualidade (notas 2, 3, 7)

Este instrumento registra **se** um movimento de mediação ocorre, e é silencioso sobre **o
quão bem** ele é realizado. Duas devolutivas podem receber o mesmo vetor binário e ter
qualidades pedagógicas muito diferentes. A definição de qualidade da devolutiva formulada na
nota metodológica 1 é uma proposição analítica emergente, a ser operacionalizada e validada
em etapa posterior, e **não é aplicada retroativamente a este corpus**.

---

## 4. Procedimento da nova codificação

### 4.1 Quem codifica

Um novo codificador, especialista em Letras ou Educação, **de fora da autoria do artigo**.
Recebe apenas este protocolo e o pacote de anotação. Não tem acesso a nenhuma codificação
anterior, nem à chave de cenários, nem aos resultados já apurados.

### 4.2 O que recebe

- Este documento (protocolo v0.3), na versão aprovada pelos três autores.
- Planilha com as 39 devolutivas embaralhadas, sem indicação de cenário, repetição ou ordem original, com as colunas `ID`, `Texto do aluno`, `Devolutiva`, `FM01`–`FM08`, `MTL`, `Observações`.

### 4.3 Como codifica

Duas varreduras separadas sobre o mesmo material: primeiro as oito FMs, depois a MTL. A
separação existe para reduzir o arrasto de um eixo sobre o outro.

### 4.4 Quando o confronto acontece (nota 9)

As justificativas e observações qualitativas da nova codificação permanecem independentes.
O confronto com a codificação nº 4 e a discussão das divergências ocorrem **somente depois**
de concluídos e preservados os dois registros, em arquivos separados e datados.

### 4.5 Preservação e errata (nota 10)

O codebook v0.2-Q vai para o material aberto **como foi usado**, acompanhado de errata que
identifica as três passagens defeituosas: o registro da média da passada anterior, a nota
específica da FM03 e o reforço dela na seção de fronteiras. Nenhum código original é
alterado silenciosamente. A codificação nº 4 é preservada como foi entregue.

---

## 5. Plano de análise, fixado antes da anotação

Sobre o par **nova codificação × codificação nº 4**:

- κ de Cohen por função (FM01 a FM08) e para a MTL, com bandas de Landis e Koch (1977).
- Concordância bruta ao lado de cada κ, sempre.
- Prevalência observada em cada codificador.
- PABAK (Byrt et al., 1993) nas categorias de base rara ou saturada, ao lado do κ e nunca no lugar dele, com sinalização explícita do paradoxo do κ (Feinstein e Cicchetti, 1990).
- **Consolidação por cenário:** as três execuções de cada um dos 13 cenários agrupadas, reportando estabilidade e variação das FMs e da MTL entre execuções do mesmo cenário.
- Nenhuma categoria é omitida por ter resultado desfavorável.

Sobre a **validade de construto da métrica da RQ2**: a régua lexical executada por programa
é confrontada com a coluna MTL do novo codificador, o que passa a fornecer também uma
segunda leitura especialista do mesmo construto.

---

## 6. O que vai para o artigo em cada cenário de resultado

| Resultado do κ médio das FMs | O que é escrito |
|---|---|
| ≥ 0,61 | A distribuição por função é reportada como medida, com o vetor de κ ao lado. |
| 0,41 a 0,60 | A distribuição é mantida com ressalva explícita de que a leitura função a função é indicativa; a conclusão se apoia no padrão agregado. |
| < 0,41, ou κ < 0,40 em FM02, FM04 ou FM06 | As funções que sustentam a conclusão perdem estatuto de evidência quantitativa; a tabela é rebaixada a ilustração qualitativa e o achado é reformulado como padrão, não como medida. |

Em qualquer dos três casos os números são publicados, e o histórico da seção 1 deste
documento é narrado no método, incluindo a procedência da codificação nº 3.

---

## 7. Limitações já assumidas

- **Codificação binária (nota 11).** O instrumento reduz a devolutiva a presenças e ausências. Fenômenos de mediação são contextuais e não lineares, e o vetor binário não os captura.
- **Assimetria residual entre as duas passadas.** A codificação nº 4 foi produzida sob a v0.2-Q, que continha o agregado da passada anterior. O novo codificador não recebe essa informação. As definições operativas são as mesmas, inclusive na FM03, cuja redação atual é a que o segundo codificador de fato aplicou e registrou na nota 5, mas a assimetria de ancoragem existe e é declarada no artigo.
- **Juízo especialista único por passada.** Cada codificação é de uma pessoa, não de um painel.
- **Viés de formato.** O esquema de saída do modelo força um movimento de reconhecimento e abre espaço para pergunta, de modo que FM01 e FM03 podem estar presentes por imposição do formato. Isso é problema da interpretação no artigo, não da codificação.
- **Fora de escopo nesta rodada:** a definição de qualidade da devolutiva (nota 1), suas dimensões futuras (nota 4), a mediação humana como repertório comprimido (nota 12) e as implicações para a entrega de devolutivas na plataforma (nota 13). São material do próximo artigo e do desenho do piloto.

---

## 8. Concordância dos autores

Conforme o passo 2 da sequência acordada, esta versão precisa da concordância explícita dos
três autores antes de qualquer nova codificação.

| Autor | Concordância | Data |
|---|---|---|
| Randerson O. M. Rebouças | | |
| Marcelo Magalhães Foohs | | |
| Rosa Maria Vicari | | |
