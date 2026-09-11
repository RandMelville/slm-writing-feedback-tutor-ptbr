# Anexo de alinhamento conceitual dos autores: treze exemplos resolvidos

**Acompanha:** Protocolo revisado de codificação, minuta para aprovação, 25 de agosto de 2026

> **Documento interno.** Este anexo explicita decisões conceituais dos autores e registra a origem de exemplos reduzidos no Guia do Professor revisado. Ele **não** constitui calibração dos codificadores e não lhes é entregue, pois os vetores resolvidos funcionariam como gabarito e poderiam ancorar as duas leituras na mesma direção.

Cada exemplo traz um texto de aluno, uma devolutiva, o vetor resolvido e a justificativa. Serve a dois propósitos: fixar entre os autores como as fronteiras difíceis e a regra de validade mínima se aplicam, e servir de fonte para os exemplos, muito mais enxutos, que vão no Guia do Professor revisado.

**Procedência.** Nenhum exemplo deste anexo sai das 39 devolutivas a codificar. Todos foram construídos para o instrumento ou adaptados do corpus de devolutivas de professores, que não faz parte do material a codificar. Isso é verificado por programa (`verifica_exemplos.py`).

Convenção do vetor: `FM01…FM08 | FP01…FP08 | MTL`. FPxx somente pode ser 1 quando a FMxx correspondente também for 1.

## Parte 1. Fronteiras entre funções

### Exemplo 1. FM01 e FM08 na mesma devolutiva

> **Texto do aluno:** *"O Camilo foi na cartomante. A cartomante falou que tava tudo bem. Aí ele foi na casa do Vilela e morreu."*
>
> **Devolutiva:** "Você entendeu bem o que acontece no conto e colocou os fatos na ordem em que aconteceram. Continue assim, você vai longe!"

**Vetor:** `1 0 0 0 0 0 0 1 | 0 0 0 0 0 0 0 0 | 1`

A primeira frase nomeia duas coisas que o aluno fez bem (compreendeu o enredo, ordenou os fatos), logo **FM01 = 1**. A segunda não nomeia nada, afirma capacidade e projeta continuidade, logo **FM08 = 1**. As duas convivem: a devolutiva reconhece uma competência e fecha reforçando autonomia. **MTL = 1** porque "colocou os fatos na ordem em que aconteceram" comenta a construção do texto, não o enredo da obra.

### Exemplo 2. Pergunta que já traz a resposta é FM02, não FM03

> **Texto do aluno:** *"Ele adorava o lugar, mas quis ficar."*
>
> **Devolutiva:** "Se ele adorava o lugar, o natural seria querer ficar; então o 'mas' não estabelece contraste aqui. Percebeu?"

**Vetor:** `0 1 0 0 0 0 0 0 | 0 0 0 0 0 0 0 0 | 1`

A correção está dentro do parêntese. O aluno não precisa reconsiderar nada, só concordar. É o problema sendo nomeado em forma de pergunta, logo **FM02 = 1** e **FM03 = 0**. **MTL = 1**: o comentário é sobre o conector usado no texto do aluno.

### Exemplo 3. FM03 válida

> **Devolutiva:** "No final você escreveu que o personagem ficou aliviado. O que, no seu texto, mostra esse alívio para quem lê?"

**Vetor:** `0 0 1 0 0 0 0 0 | 0 0 0 0 0 0 0 0 | 1`

A pergunta está ancorada num elemento identificável do texto do aluno (o final, o alívio) e uma resposta pertinente exige que ele releia e justifique. A resposta não está dada. **FM03 = 1**. Não marque FM02: a devolutiva não afirma que existe um problema, ela pede o exame.

### Exemplo 4. Repertório é FM04, não FM05

> **Devolutiva:** "Para não repetir 'aí' no começo de cada frase, você pode usar 'em seguida', 'depois disso' ou 'quando'."

**Vetor:** `0 1 0 1 0 0 0 0 | 0 0 0 0 0 0 0 0 | 1`

**FM02 = 1** porque o problema é dito (a repetição de "aí"). **FM04 = 1** porque oferece repertório concreto. **FM05 = 0** porque nenhuma frase do aluno foi reescrita. Repare que nomear o problema e oferecer a pista na mesma frase é comum: as duas colunas vão a 1.

### Exemplo 5. Frase pronta é FM05

> **Devolutiva:** "Ficaria mais claro assim: 'Quando Camilo abriu o bilhete, entendeu que Vilela já sabia de tudo.' Repare como usar o nome resolve a dúvida sobre quem é 'ele'."

**Vetor:** `0 1 0 0 1 0 0 0 | 0 0 0 0 0 0 0 0 | 1`

Existe uma frase montada que materializa o conserto, logo **FM05 = 1 e FP05 = 0**. **FM02 = 1**, porque a segunda frase nomeia o problema referencial. **FM04 = 0**: não há repertório entre alternativas, mas um modelo pronto. A fronteira entre FM04 e FM05 é a presença da frase montada.

### Exemplo 6. FM06 e FM07 juntas, e por que outras colunas sobem junto

> **Texto do aluno:** *segundo parágrafo composto por várias frases curtas justapostas e sem opinião sobre o desfecho.*
>
> **Devolutiva:** "Reescreva o segundo parágrafo juntando as frases curtas em duas ou três frases mais longas. Depois, acrescente um trecho dizendo o que você achou do desfecho."

**Vetor:** `0 1 0 1 0 1 1 0 | 0 0 0 0 0 0 0 0 | 1`

**FM06 = 1**: pede a reescrita do que já está no texto. **FM07 = 1**: a segunda parte pede conteúdo novo (a opinião sobre o desfecho), que não estava lá. **FM02 = 1**: ao mandar juntar as frases curtas, a devolutiva diz que a justaposição é inadequada. **FM04 = 1**: "juntando em duas ou três frases mais longas" é a estratégia a seguir, não apenas a ordem de reescrever.

Vetores com quatro funções não são erro. O instrumento é multirrótulo, e uma devolutiva densa mobiliza vários movimentos.

## Parte 2. A coluna MTL

### Exemplo 7. MTL = 1 sem nenhum termo técnico

> **Devolutiva:** "Você começou quase todas as frases com 'aí'. Leia o parágrafo em voz alta e veja como soa."

**Vetor:** `0 1 0 1 0 0 0 0 | 0 0 0 0 0 0 0 0 | 1`

Nenhuma palavra de gramática aparece, e mesmo assim a devolutiva trata a escrita do aluno como objeto: o início repetido das frases. **MTL = 1**. Também é **FM02** (o problema é dito) e **FM04** (ler em voz alta é uma estratégia concreta).

### Exemplo 8. MTL = 0 com todos os termos técnicos no lugar

> **Devolutiva:** "Seu texto tem boa coesão e ótima estrutura. Parabéns!"

**Vetor:** `0 0 0 0 0 0 0 0 | 0 0 0 0 0 0 0 0 | 0`

Os termos técnicos estão presentes, mas nada específico do texto é apontado: o elogio caberia em qualquer produção. **MTL = 0**. **FM01 = 0** porque nenhuma competência específica é nomeada. Também não é FM08, pois não afirma capacidade nem projeta continuidade. Um vetor inteiramente zerado é resultado possível.

## Parte 3. Presença formal e falso positivo

Nos exemplos a seguir, o movimento está formalmente presente e por isso a FM correspondente recebe 1. Quando a ocorrência se apoia em premissa falsa, leitura contrariada ou orientação inadequada, o FP correspondente também recebe 1, com justificativa obrigatória.

### Exemplo 9. Elogio que transforma o problema em qualidade

> **Texto do aluno:** *"Eu fui na loja e comprei pão e daí eu voltei e aí minha mãe falou e eu respondi."*
>
> **Devolutiva:** "Parabéns pelo uso variado de conectivos: 'e', 'e daí', 'e aí' deixaram o texto fluido. Continue assim!"

**Vetor:** `1 0 0 0 0 0 0 1 | 1 0 0 0 0 0 0 1 | 1`

**FM01 = 1 e FP01 = 1**: o que é elogiado como variedade é justamente a repetição que empobrece o texto. Formalmente é um reconhecimento de competência, semanticamente reforça uma inadequação.

**FM08 = 1 e FP08 = 1**: "Continue assim!" reforça explicitamente a continuidade de uma orientação inadequada, e por isso não é realização válida de reforço de autonomia.

**MTL = 1**, e isso não é contradição. A regra de validade mínima vale para as FMs, não para a MTL. A devolutiva fala dos conectores do texto do aluno, ainda que fale errado. A MTL registra o objeto, não o acerto.

**Justificativas de FP (obrigatórias):** *"FP01 e FP08 = 1: o elogio apresenta a repetição de conectores como qualidade e o fechamento manda continuar assim."*

### Exemplo 10. Pergunta sobre um elemento que não existe

> **Texto do aluno:** *(uma crônica em que ninguém morre)*
>
> **Devolutiva:** "Por que você escolheu terminar o texto com a morte da personagem? O que isso muda para o leitor?"

**Vetor:** `0 0 1 0 0 0 0 0 | 0 0 1 0 0 0 0 0 | 0`

A pergunta apresenta formalmente FM03: é aberta, pede justificativa e projeta efeito de leitura. Por isso **FM03 = 1**. Entretanto, está construída sobre acontecimento inexistente; assim, **FP03 = 1**. **MTL = 0**, pois a devolutiva não comenta uma característica efetivamente presente na escrita do aluno.

**Justificativa FP03:** *"A pergunta pressupõe a morte de uma personagem, acontecimento ausente no texto."*

### Exemplo 11. Problema inventado e pista que leva ao erro

> **Texto do aluno:** *"Ele abriu a porta, mas o bonde já tinha passado."*
>
> **Devolutiva:** "Cuidado: 'mas' não pode ser usado no meio da frase. Troque por 'portanto' para ligar as duas ideias."

**Vetor:** `0 1 0 1 0 0 0 0 | 0 1 0 1 0 0 0 0 | 1`

**FM02 = 1 e FP02 = 1**: o problema não existe, e a regra apresentada é falsa. Marcar 1 aqui contaria como mediação um movimento que leva o aluno a corrigir o que estava certo.

**FM04 = 1 e FP04 = 1**: a pista aparece formalmente, mas é incorreta. O conector sugerido é conclusivo, e a relação entre as duas ideias é de contraste. Seguir a orientação piora o texto.

**MTL = 1**: apesar de tudo, o comentário é sobre o conector empregado pelo aluno.

**Justificativas de FP (obrigatórias):** *"FP02 e FP04 = 1: problema inexistente e substituição por conector de sentido incompatível."*

### Exemplo 12. Evidência segmentada: um segmento vale, outro não

> **Devolutiva:** "Uma forma de resolver a repetição é escrever assim: 'Quando Camilo leu o bilhete, entendeu tudo.' Outra opção é: 'Ele leu e ele entendeu e ele saiu.'"

**Vetor:** `0 1 0 0 1 0 0 0 | 0 0 0 0 1 0 0 0 | 1`

**FM05 = 1 e FP05 = 1**. Existe ao menos uma ocorrência formal válida: o primeiro modelo resolve de fato a repetição. O segundo modelo preserva o problema que deveria resolver e, sozinho, seria falso positivo. A presença do primeiro segmento sustenta FM05 = 1, enquanto o segundo exige FP05 = 1 e justificativa própria. **FM02 = 1**: a repetição é nomeada.

**Justificativa FP05 (obrigatória):** *"O primeiro modelo ('Quando Camilo leu o bilhete...'); o segundo modelo ('Ele leu e ele entendeu e ele saiu') é falso positivo, repete o problema."*

### Exemplo 13. Estranheza de formulação não basta para FP

> **Texto do aluno:** *texto argumentativo cujo argumento final está apenas enunciado, sem desenvolvimento.*
>
> **Devolutiva:** "O autor deste texto poderia desenvolver melhor o argumento final. Comente o que ele quis dizer e proponha uma continuação."

**Vetor:** `0 1 0 0 0 0 1 0 | 0 0 0 0 0 0 0 0 | 1`

**FM02 = 1:** a insuficiência do argumento final é apontada. **FM07 = 1 e FP07 = 0:** há convite para desenvolver conteúdo novo sustentado pelo texto. A expressão "o autor deste texto" é pouco natural quando o destinatário é o próprio aluno, mas essa inadequação pragmática, isoladamente, não prova que a função seja falsa. FP exige premissa comprovadamente ausente, leitura contrariada pelo texto ou orientação capaz de induzir ao erro.

**MTL = 1:** a devolutiva comenta o desenvolvimento do argumento no texto do aluno.

Este exemplo impede o uso excessivo de FP: estranheza de formulação ou existência de interpretação alternativa não bastam para marcar falso positivo.

## Resumo de bolso

+---------------------------------------------------------------------------------------------------+------------------------------------------------------+
| **Se...**                                                                                         | **então**                                            |
+:==================================================================================================+:=====================================================+
| o movimento não aparece                                                                           | FM = 0 e FP = 0                                      |
+---------------------------------------------------------------------------------------------------+------------------------------------------------------+
| o movimento aparece e não há falso positivo identificado                                          | FM = 1 e FP = 0                                      |
+---------------------------------------------------------------------------------------------------+------------------------------------------------------+
| o movimento aparece, mas se apoia em premissa falsa, leitura contrariada ou orientação inadequada | FM = 1 e FP = 1                                      |
+---------------------------------------------------------------------------------------------------+------------------------------------------------------+
| FP = 1 com FM = 0                                                                                 | combinação inválida                                  |
+---------------------------------------------------------------------------------------------------+------------------------------------------------------+
| a pergunta já contém a correção                                                                   | FM02, não FM03                                       |
+---------------------------------------------------------------------------------------------------+------------------------------------------------------+
| há repertório sem frase montada                                                                   | FM04, não FM05                                       |
+---------------------------------------------------------------------------------------------------+------------------------------------------------------+
| há frase montada                                                                                  | FM05                                                 |
+---------------------------------------------------------------------------------------------------+------------------------------------------------------+
| pede consertar o que existe                                                                       | FM06                                                 |
+---------------------------------------------------------------------------------------------------+------------------------------------------------------+
| pede conteúdo novo                                                                                | FM07                                                 |
+---------------------------------------------------------------------------------------------------+------------------------------------------------------+
| elogia nomeando o que foi feito                                                                   | FM01                                                 |
+---------------------------------------------------------------------------------------------------+------------------------------------------------------+
| afirma capacidade e projeta continuidade, sem nomear competência                                  | FM08                                                 |
+---------------------------------------------------------------------------------------------------+------------------------------------------------------+
| um mesmo trecho sustenta várias funções                                                           | repetir o trecho em cada campo de evidência          |
+---------------------------------------------------------------------------------------------------+------------------------------------------------------+
| há segmento adequado e segmento falso para a mesma função                                         | FM = 1 e FP = 1; registrar evidência e justificativa |
+---------------------------------------------------------------------------------------------------+------------------------------------------------------+
| fala da escrita do aluno, mesmo de modo equivocado                                                | MTL = 1                                              |
+---------------------------------------------------------------------------------------------------+------------------------------------------------------+
| fala apenas da obra ou usa fórmula genérica                                                       | MTL = 0                                              |
+---------------------------------------------------------------------------------------------------+------------------------------------------------------+
| há interpretação alternativa plausível                                                            | não presumir FP; registrar dúvida em Observações     |
+---------------------------------------------------------------------------------------------------+------------------------------------------------------+
