# Guia da 2ª codificação cega (codebook v0.2)

**Para:** Prof. Marcelo Magalhães Foohs  
**De:** Randerson O. M. Rebouças  
**Data:** 27 de julho de 2026  
**Material:** `codificacao_cega_v02.xlsx` (39 linhas) + `codebook_funcoes_mediacao.pdf` (v0.2)  
**Tempo estimado:** 1h30 a 2h, pode ser em duas sessões  

---

## Em uma frase

É a mesma tarefa da rodada de junho (marcar quais funções de mediação cada devolutiva
mobiliza), agora sobre um conjunto maior e com **uma coluna nova**, pedida pelos revisores
do JBCS.

## Como está a planilha

Uma devolutiva por linha, identificada só por código (`R01` a `R39`), em ordem
embaralhada. Colunas:

| Coluna | O que preencher |
|---|---|
| `Texto do aluno` | (só leitura) o texto fictício que originou a devolutiva |
| `Devolutiva` | (só leitura) a devolutiva a codificar |
| `FM01` a `FM08` | 1 (presente) ou 0 (ausente), como em junho |
| `MTL` | 1 ou 0, **coluna nova**, definida abaixo |
| `Observações` | livre, opcional (útil para casos-limite) |

São 39 × 9 = 351 decisões binárias. As células já têm validação para aceitar só 0 ou 1.

## Importante: duas passadas, não uma

**Preencha FM01 a FM08 nas 39 linhas primeiro. Só depois volte ao começo e preencha a
coluna MTL.**

O motivo é metodológico e vale o incômodo: FM02 ("nomear o problema") e MTL são vizinhos
conceituais, e decidir as duas na mesma leitura faz uma arrastar a outra. Como as duas
colunas alimentam análises diferentes, quero que sejam julgamentos independentes. Se puder
dar um intervalo entre as duas passadas, melhor ainda.

## As colunas FM01 a FM08

Nada mudou no procedimento: multirrótulo binário, unidade é a devolutiva inteira (não a
frase), **regra de evidência mínima, na dúvida marque 0**. As definições estão no codebook
anexo, versão **0.2**, que é a versão com FM02 e FM04 já ampliadas depois da rodada de
junho. Vale reler as duas, porque foram justamente as que ficaram com o menor κ (0,58 e
0,45) e as definições mudaram por causa disso.

## A coluna nova: MTL

**A pergunta:** esta devolutiva trata o **texto que o aluno escreveu** como objeto de
atenção, comentando alguma característica da sua construção? Ou fica no plano do
**conteúdo da obra literária** que o aluno citou, ou em elogio e pergunta genéricos que não
se ancoram em nada do texto produzido?

- **Marque 1** quando a devolutiva se refere a alguma propriedade da escrita do aluno: repetição, uso de conectivo, clareza de a quem um pronome se refere, encadeamento das ideias, organização, progressão, pontuação, escolha de palavra.
- **Marque 0** quando a devolutiva conversa sobre o enredo, os personagens ou o tema da obra, ou quando faz elogio ou pergunta que caberiam em qualquer texto.

**O ponto crítico, e é aqui que a coluna ganha valor:** *não* exija terminologia técnica.

- *"Você repetiu muito 'a cartomante'; dá para trocar por outra palavra?"* → **MTL = 1**, ainda que não apareça a palavra "coesão" nem "repetição lexical".
- *"Seu texto tem boa coesão e ótima estrutura."* → **MTL = 0** se o elogio for de fórmula e não apontar nada específico do texto. Usar o termo não basta.
- *"O que você acha que motivou a cartomante a mentir?"* → **MTL = 0**: é conversa sobre a obra, não sobre a escrita.

Vale para qualquer trecho da devolutiva, tanto na parte de elogio quanto nas perguntas.
Basta **um** trecho que satisfaça para marcar 1.

*(Os exemplos acima são inventados para o guia; não correspondem a nenhuma linha da
planilha.)*

## O que a tarefa não é

- **Não é avaliar a qualidade** da devolutiva, nem dar nota. É registrar presença ou ausência de funções.
- **Não é comparar** as devolutivas entre si, nem com um padrão-ouro. Não existe gabarito.
- **Não é procurar defeito.** Várias destas devolutivas vão parecer pobres. Isso não muda a tarefa: marcar o que está lá, não o que falta.

## Sobre a cegueira do procedimento

As 39 devolutivas são todas do mesmo modelo (`qwen2.5:3b-instruct`), então não há
procedência a esconder. O que você não recebe é a **codificação da primeira passada**, nem
a ordem original, nem a indicação de qual cenário e qual repetição cada linha é. O
embaralhamento é determinístico e auditável (`build_pacote_cego.py`, semente fixa), e a
chave de decegamento fica fora do material que você recebe.

Uma consequência do formato de saída do modelo, que vale ter em mente sem deixar que
influencie a codificação: o campo de elogio força um movimento de reconhecimento e as
perguntas abrem espaço para reflexão. Codifique pela regra de evidência mínima como
sempre; a interpretação desse viés de formato é problema meu na hora de escrever.

Se durante a tarefa você concluir que uma definição do codebook está frouxa, **anote em
`Observações` e siga com a definição como está**. Não ajuste o codebook no meio da
passada: um desacordo registrado vale mais para o artigo do que uma concordância obtida
por reconciliação, e foi exatamente assim que a v0.2 nasceu em junho.

## Devolução

Devolva o `.xlsx` preenchido. Eu rodo `src/cohen_kappa.py` e mando de volta o vetor de 8 κ
mais o κ da coluna MTL, com as bandas de Landis & Koch, antes de escrever a seção.

Qualquer dúvida em caso-limite, me chame; melhor resolver antes do que descobrir depois na
planilha.
