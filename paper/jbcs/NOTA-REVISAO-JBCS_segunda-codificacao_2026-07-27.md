# Revisão do artigo do benchmark (JBCS): a segunda codificação cega

**Para:** Prof. Marcelo Magalhães Foohs  
**De:** Randerson O. M. Rebouças  
**Data:** 27 de julho de 2026  

**Objetivo:** explicar o único item da revisão que depende de você, o que ele é na
prática e por que ele decide o destino do artigo. O restante da lista eu toco em
paralelo e não precisa da sua mão.

---

## A situação

O JBCS voltou hoje com **"a revised version is required for further review"**, prazo de
**45 dias** (vence por volta de 10/09). Dois pareceres, os dois construtivos. O Revisor A
escreve que o artigo é "promising and potentially publishable"; o Revisor C traz uma lista
majoritariamente editorial. **Nenhum dos dois pede coleta nova nem experimento novo de
inferência.** As 312 chamadas do benchmark e o contra-experimento continuam intactos.

Há doze itens de edição (roadmap da introdução, DOIs, densidade textual, related work,
uma tabela estourando margem) que são trabalho meu e já estão sendo feitos.

E há **um item, e só um, que depende de você**.

## O pedido, em uma frase

No §7.4 do artigo nós escrevemos, com todas as letras, que uma nova passada cega sobre o
codebook v0.2 era trabalho futuro. Os dois revisores leram essa frase e responderam a
mesma coisa: façam agora.

O Revisor C, literalmente:

> "Given that these figures are the most frequently cited in the article, I suggest the
> authors consider actually carrying out this second coding pass and reporting the
> corresponding κ, rather than merely flagging it as future work."

O Revisor A, por outro caminho:

> "the revised coding scheme would benefit from further reliability validation,
> particularly for the mediation functions that are central to the conclusions."

Como você foi o segundo anotador cego da primeira rodada (o κ = 0,83 das 20 devolutivas
humanas), a tarefa naturalmente volta para você: o codebook já está calibrado na sua
leitura, e trocar de anotador agora significaria recalibrar do zero dentro de 45 dias.

## Como seria a anotação, na prática

**Material:** as 39 saídas do modelo `qwen2.5:3b-instruct` (13 cenários × 3 repetições),
embaralhadas, sem a codificação do anotador 1 e sem indicação de cenário ou repetição. É
exatamente o escopo que o Revisor C nomeou. São devolutivas **curtas**, bem mais curtas que
as dos professores: mobilizam 1,7 funções em média, contra 3,8 das humanas.

**Duas colunas a preencher, na mesma leitura:**

1. **Funções de mediação (o que você já fez).** As oito colunas binárias FM01 a FM08,
   codebook v0.2, mesma regra de evidência mínima ("na dúvida, ausente"). Mesmo formato de
   planilha da rodada anterior.

2. **Uma coluna nova, binária, por devolutiva.** A pergunta: *esta devolutiva trata o
   texto do aluno como objeto linguístico (nomeia ou problematiza um fenômeno de
   textualidade), ou fica no plano temático da obra literária que o aluno citou?* O guia
   anexo detalha inclusão, exclusão e casos-limite. O ponto central da definição é que
   **não se exige terminologia técnica**: "você repetiu muito 'a cartomante'" conta, e um
   "seu texto tem boa coesão" de fórmula não conta. É justamente essa distinção que a régua
   de palavra-chave não consegue fazer, e é isso que o κ vai medir.

**Tempo estimado:** 1h30 a 2h, em uma ou duas sessões. São 39 × 9 = 351 decisões binárias.

**Saída:** dois coeficientes de concordância, que é o que os revisores querem ver.

**Uma ressalva estatística que fica comigo, não com você.** Na passada do anotador 1, FM01
está em 39/39 e FM05, FM06 e FM08 em 0/39. Sobre variável constante o κ degenera: fica
indefinido, ou perto de zero mesmo havendo concordância total. É o paradoxo do κ
(Feinstein e Cicchetti, 1990). Isso não se resolve aumentando o pacote, porque o κ que o
revisor pede é o da Tabela 9 e portanto tem de sair destas 39. Resolve-se no relato:
reporto κ onde ele é definido e, nas funções de base rara, acrescento a concordância bruta
e um coeficiente robusto a prevalência (PABAK, Byrt et al. 1993, ou AC1 de Gwet, 2008),
explicando a base rate. É tratamento padrão e citável. Só registro para você não estranhar
quando a tabela vier com mais de uma coluna de concordância.

**Duas varreduras, não uma.** O guia pede que você preencha FM01 a FM08 nas 39 linhas
primeiro e só depois volte para a coluna MTL. FM02 e MTL são vizinhas conceituais, e
julgá-las na mesma leitura faz uma puxar a outra. Como alimentam análises diferentes,
prefiro pagar o incômodo e ter dois julgamentos separados.

**Regra de relato fixada antes da coleta.** Escrevi um pré-registro curto
(`PRE-REGISTRO_analise.pdf`, anexo) dizendo o que vai para o artigo em cada faixa de
resultado, inclusive nos cenários ruins: se o κ da validação da RQ2 vier abaixo de 0,41, os
51,3% saem do *abstract* e a taxa passa a ser a do julgamento especialista. Fiz isso antes
de você anotar, de propósito. Sem a regra fixada, escolher a forma de relato depois de
conhecer o número é escolha conveniente, e é exatamente o tipo de coisa que um revisor
atento identifica. Se discordar de alguma das regras, é agora que dá para mudar.

## Por que cada uma das duas colunas importa

### A coluna 1 fecha o buraco de confiabilidade da tabela mais citada do artigo

A Tabela 9 (funções de mediação do modelo contra o repertório especialista) é a que
aparece no *abstract*, na §7.5 e na conclusão: FM02 em 3% contra 80%, FM04 em 15% contra
69%, FM06 em 0% contra 57%. É o número que sustenta a tese de que o modelo não entra no
núcleo corretivo.

Hoje essa tabela é **passada de codificador único, sem nenhuma medida de confiabilidade**.
Pior: das três funções que carregam a conclusão, duas são justamente as de **menor κ na
v0.1**, FM02 com 0,58 e FM04 com 0,45. Foi exatamente por causa desses dois números que
refinamos as definições para a v0.2. Ou seja, hoje a v0.2 conserta o problema por
argumento, mas não tem uma única medida que mostre que consertou. O Revisor A colocou o
dedo aí com precisão cirúrgica.

Sua segunda passada produz o κ por função sobre a v0.2 e resolve os dois lados de uma vez:
valida a codificação do modelo e, de quebra, mostra que o refino de FM02/FM04 elevou a
concordância.

### A coluna 2 destrava a palavra "superficialidade"

Esse é o passivo que já tínhamos mapeado desde junho, e é a crítica central do Revisor A:

> "Mentioning an appropriate term does not necessarily mean that the model correctly
> identifies the problem or helps the student revise it; conversely, a pedagogically useful
> response may not use the expected terminology. I therefore recommend either strengthening
> this analysis through independent human evaluation or clearly presenting the keyword
> analysis as exploratory evidence."

Os 51,3% da RQ2 saem hoje de uma **régua de palavra-chave**: a resposta cita algum termo da
taxonomia de Koch? Isso é uma triagem grosseira, e nós mesmos dizemos isso no artigo. A
coluna 2 é o julgamento especialista sobre o mesmo material. Cruzando as duas, sai o κ
heurística-versus-humano, que é precisamente a validação que o §8 do artigo declara como
"the immediate next step for this benchmark".

Note que o revisor ofereceu duas saídas, "either / or". A segunda (rebaixar tudo a
exploratório) já é o que o artigo faz hoje, e mesmo assim ele pediu mais. Achar que ele
aceita a mesma resposta escrita com outras palavras é uma aposta que eu não faria.

## O risco de não fazer

O Revisor C recomendou **"Resubmit for Review"**, o que significa que a versão revisada
volta para os mesmos olhos. Devolver com a mesma lacuna, só que melhor redigida, é apostar
que dois revisores que apontaram o item de forma independente vão aceitar a recusa na
segunda vez. Com 45 dias no relógio e uma tarefa de duas horas e meia na mesa, o cálculo de
risco não fecha a favor de não fazer.

## Isto não contradiz a nossa decisão de 1º de julho

Registro porque a semelhança superficial pode confundir. Em 01/07 você avaliou que **painel
de professores não é necessário** para a próxima etapa, e que a rubrica de qualidade do
feedback deve sair da literatura, com juiz sendo um *foundation model*. Isso continua
valendo integralmente, e é sobre a **avaliação do modelo em 2027**.

O que peço aqui é outra coisa: não há recrutamento, não há coleta, não há painel novo, não
há questão de CEP. O material já está coletado e codificado. Trata-se apenas de **medir a
confiabilidade de uma codificação que já existe**, com a pessoa que já a calibrou.

## Um ajuste de redação que vem junto

Você ser o anotador não é problema de método: dupla codificação por coautores é a prática
corrente em pesquisa qualitativa de Educação, e a independência que o κ exige é
**procedimental** (cegueira quanto à primeira codificação e quanto à origem de cada
devolutiva), não vínculo institucional. A melhor evidência é que o κ = 0,83 já está na
versão submetida e nenhum dos dois revisores objetou, inclusive o Revisor C, que conferiu
o checklist do JBCS item por item.

O que precisa mudar é como o texto **descreve** isso. Hoje o §7.4 diz "a second, blind, and
independent annotator (a specialist in Education)", e o CRediT te atribui apenas
Supervision, Validation e Writing. Um leitor entende "independent" como externo à equipe.
Enquanto esse κ era auxiliar, passou; quando ele virar peça central do argumento de
aceitação, vira flanco aberto na segunda rodada. Proponho:

- §7.4: "one of the authors, a specialist in Education, blind to the first coding and to
  the provenance of each turn". Declarar explicitamente fortalece, porque mostra que a
  cegueira é deliberada e construída.
- CRediT: acrescentar "Formal analysis (inter-annotator coding)" à sua entrada.

## O que preciso de você

1. **Confirmar se consegue reservar 1h30 a 2h nas próximas duas semanas.** Este é o caminho
   crítico; tudo o mais é paralelizável.
2. **Aval para os dois ajustes de redação acima.**

O material já está pronto e vai anexo, quatro arquivos: a planilha
`codificacao_cega_v02.xlsx` (39 linhas, embaralhada, com validação de 0/1 nas células), o
`GUIA_2a_CODIFICACAO.pdf`, o `PRE-REGISTRO_analise.pdf` e o `codebook_funcoes_mediacao.pdf`
(v0.2). Para anotar bastam a planilha, o guia e o codebook; o pré-registro é para você
conferir as regras de relato antes, se quiser.

## O que corre em paralelo, sem depender de você

Para você ter a foto inteira: estou tratando os doze itens editoriais, a análise em nível
de cenário que o Revisor A pediu (recálculo sobre dados
existentes, sem coleta), o abrandamento das afirmações causais sobre o *instruction tuning*
da Llama 3.2, e a ampliação do *related work* com a literatura brasileira de correção
automática de redação. Nada disso é bloqueante.

Um deles merece seu conhecimento porque toca o material publicado. O Revisor C notou que a
contagem de 80 chamadas do contra-experimento não fecha com o detalhamento (E1 26 + E2 24
+ E2b 24 = 74). Fui conferir: o arquivo de dados tem exatamente 74 registros, e o
isolamento E3 (as chamadas via `curl`) nunca foi persistido em arquivo, aparecendo no
artigo só de forma qualitativa. O número 80 também consta da seção **Data Availability** e,
portanto, do depósito no Zenodo. Vou rodar o E3 de novo salvando o JSON, reportar o k/n na
Tabela 4 e publicar uma nova versão do depósito. É o tipo de item que é melhor corrigir por
iniciativa nossa, com o registro completo, do que deixar como ajuste de aritmética.
