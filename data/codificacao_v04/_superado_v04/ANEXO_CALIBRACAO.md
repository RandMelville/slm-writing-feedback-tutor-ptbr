# Anexo de calibração: treze exemplos resolvidos

**Acompanha:** protocolo v0.4 (versão congelada), 22 de agosto de 2026

> **Documento interno.** Este anexo resolve os casos-limite para os autores e é a fonte de onde
> saíram, reduzidos, os exemplos do `GUIA_PROFESSOR`. Ele **não** vai aos codificadores: treze
> vetores resolvidos funcionariam como gabarito e arrastariam a leitura dos dois na mesma direção.

Cada exemplo traz um texto de aluno, uma devolutiva, o vetor resolvido e a justificativa. Serve a
dois propósitos: fixar entre os autores como as fronteiras difíceis e a regra de validade mínima
se aplicam, e servir de fonte para os exemplos, muito mais enxutos, que vão no `GUIA_PROFESSOR`.

**Procedência.** Nenhum exemplo deste anexo sai das 39 devolutivas a codificar. Todos foram
construídos para o instrumento ou adaptados do corpus de devolutivas de professores, que não faz
parte do material a codificar. Isso é verificado por programa (`verifica_exemplos.py`).

Convenção do vetor: `FM01 FM02 FM03 FM04 FM05 FM06 FM07 FM08 | MTL`.

---

## Parte 1. Fronteiras entre funções

### Exemplo 1. FM01 e FM08 na mesma devolutiva

> **Texto do aluno:** *"O Camilo foi na cartomante. A cartomante falou que tava tudo bem. Aí ele foi na casa do Vilela e morreu."*
>
> **Devolutiva:** "Você entendeu bem o que acontece no conto e colocou os fatos na ordem em que aconteceram. Continue assim, você vai longe!"

**Vetor:** `1 0 0 0 0 0 0 1 | 1`

A primeira frase nomeia duas coisas que o aluno fez bem (compreendeu o enredo, ordenou os fatos),
logo **FM01 = 1**. A segunda não nomeia nada, afirma capacidade e projeta continuidade, logo
**FM08 = 1**. As duas convivem: a devolutiva reconhece uma competência e fecha reforçando
autonomia. **MTL = 1** porque "colocou os fatos na ordem em que aconteceram" comenta a construção
do texto, não o enredo da obra.

### Exemplo 2. Pergunta que já traz a resposta é FM02, não FM03

> **Devolutiva:** "Você escreveu que ele odiava o lugar, mas quis ficar. (Se era horrível, o natural seria querer sair, então o 'mas' não cabe aqui.) Percebeu?"

**Vetor:** `0 1 0 0 0 0 0 0 | 1`

A correção está dentro do parêntese. O aluno não precisa reconsiderar nada, só concordar. É o
problema sendo nomeado em forma de pergunta, logo **FM02 = 1** e **FM03 = 0**. **MTL = 1**: o
comentário é sobre o conector usado no texto do aluno.

### Exemplo 3. FM03 válida

> **Devolutiva:** "No final você escreveu que o personagem ficou aliviado. O que, no seu texto, mostra esse alívio para quem lê?"

**Vetor:** `0 0 1 0 0 0 0 0 | 1`

A pergunta está ancorada num elemento identificável do texto do aluno (o final, o alívio) e uma
resposta pertinente exige que ele releia e justifique. A resposta não está dada. **FM03 = 1**. Não
marque FM02: a devolutiva não afirma que existe um problema, ela pede o exame.

### Exemplo 4. Repertório é FM04, não FM05

> **Devolutiva:** "Para não repetir 'aí' no começo de cada frase, você pode usar 'em seguida', 'depois disso' ou 'quando'."

**Vetor:** `0 1 0 1 0 0 0 0 | 1`

**FM02 = 1** porque o problema é dito (a repetição de "aí"). **FM04 = 1** porque oferece
repertório concreto. **FM05 = 0** porque nenhuma frase do aluno foi reescrita. Repare que nomear o
problema e oferecer a pista na mesma frase é comum: as duas colunas vão a 1.

### Exemplo 5. Frase pronta é FM05

> **Devolutiva:** "Ficaria mais claro assim: 'Quando Camilo abriu o bilhete, entendeu que Vilela já sabia de tudo.' Repare como usar o nome resolve a dúvida sobre quem é 'ele'."

**Vetor:** `0 1 0 0 1 0 0 0 | 1`

Existe uma frase montada que materializa o conserto, logo **FM05 = 1**. **FM02 = 1**, porque a
segunda frase diz qual era o problema (a dúvida sobre o referente). **FM04 = 0**: aqui não há
repertório a escolher, há um modelo pronto. A fronteira entre FM04 e FM05 é a presença da frase.

### Exemplo 6. FM06 e FM07 juntas, e por que outras colunas sobem junto

> **Devolutiva:** "Reescreva o segundo parágrafo juntando as frases curtas em duas ou três frases mais longas. Depois, acrescente um trecho dizendo o que você achou do desfecho."

**Vetor:** `0 1 0 1 0 1 1 0 | 1`

**FM06 = 1**: pede a reescrita do que já está no texto. **FM07 = 1**: a segunda parte pede conteúdo
novo (a opinião sobre o desfecho), que não estava lá. **FM02 = 1**: ao mandar juntar as frases
curtas, a devolutiva diz que a justaposição é inadequada. **FM04 = 1**: "juntando em duas ou três
frases mais longas" é a estratégia a seguir, não apenas a ordem de reescrever.

Vetores com quatro funções não são erro. O instrumento é multirrótulo, e uma devolutiva densa
mobiliza vários movimentos.

---

## Parte 2. A coluna MTL

### Exemplo 7. MTL = 1 sem nenhum termo técnico

> **Devolutiva:** "Você começou quase todas as frases com 'aí'. Leia o parágrafo em voz alta e veja como soa."

**Vetor:** `0 1 0 1 0 0 0 0 | 1`

Nenhuma palavra de gramática aparece, e mesmo assim a devolutiva trata a escrita do aluno como
objeto: o início repetido das frases. **MTL = 1**. Também é **FM02** (o problema é dito) e
**FM04** (ler em voz alta é uma estratégia concreta).

### Exemplo 8. MTL = 0 com todos os termos técnicos no lugar

> **Devolutiva:** "Seu texto tem boa coesão e ótima estrutura. Parabéns!"

**Vetor:** `0 0 0 0 0 0 0 0 | 0`

Os termos estão lá, mas nada do texto é apontado: o elogio caberia em qualquer produção. **MTL =
0**. E **FM01 = 0** pela mesma razão: nenhuma competência específica é nomeada. Também não é
FM08, porque não afirma capacidade nem projeta continuidade do trabalho, é só uma fórmula de
fechamento. Vetor inteiramente zerado é um resultado possível e não deve ser evitado.

---

## Parte 3. A regra de validade mínima em ação

Nos exemplos a seguir, o movimento está na forma e mesmo assim vai a **0**, porque opera contra a
finalidade da função. Em todos eles o campo `Observações` é obrigatório.

### Exemplo 9. Elogio que transforma o problema em qualidade

> **Texto do aluno:** *"Eu fui na loja e comprei pão e daí eu voltei e aí minha mãe falou e eu respondi."*
>
> **Devolutiva:** "Parabéns pelo uso variado de conectivos: 'e', 'e daí', 'e aí' deixaram o texto fluido. Continue assim!"

**Vetor:** `0 0 0 0 0 0 0 0 | 1`

**FM01 = 0**: o que é elogiado como variedade é justamente a repetição que empobrece o texto.
Formalmente é um reconhecimento de competência, semanticamente reforça uma inadequação.

**FM08 = 0**: "Continue assim!" reforça explicitamente a continuidade de uma orientação
inadequada, e por isso não é realização válida de reforço de autonomia.

**MTL = 1**, e isso não é contradição. A regra de validade mínima vale para as FMs, não para a
MTL. A devolutiva fala dos conectores do texto do aluno, ainda que fale errado. A MTL registra o
objeto, não o acerto.

**Observações (obrigatório):** *"FM01 e FM08 a 0 pela regra de validade mínima: o elogio apresenta a repetição de conectores como qualidade e o fechamento manda continuar assim."*

### Exemplo 10. Pergunta sobre um elemento que não existe

> **Texto do aluno:** *(uma crônica em que ninguém morre)*
>
> **Devolutiva:** "Por que você escolheu terminar o texto com a morte da personagem? O que isso muda para o leitor?"

**Vetor:** `0 0 0 0 0 0 0 0 | 0`

A pergunta tem forma perfeita de FM03: é aberta, pede justificativa, projeta efeito de leitura.
Mas está construída sobre um acontecimento inexistente, e por isso a reflexão pedida não pode ser
sustentada pela produção do aluno. **FM03 = 0**. **MTL = 0**: o objeto de que a devolutiva fala
não está no texto.

### Exemplo 11. Problema inventado e pista que leva ao erro

> **Texto do aluno:** *"Ele abriu a porta, mas o bonde já tinha passado."*
>
> **Devolutiva:** "Cuidado: 'mas' não pode ser usado no meio da frase. Troque por 'portanto' para ligar as duas ideias."

**Vetor:** `0 0 0 0 0 0 0 0 | 1`

**FM02 = 0**: o problema não existe, e a regra apresentada é falsa. Marcar 1 aqui contaria como
mediação um movimento que leva o aluno a corrigir o que estava certo.

**FM04 = 0**: a pista é incorreta. O conector sugerido é conclusivo, e a relação entre as duas
ideias é de contraste. Seguir a orientação piora o texto.

**MTL = 1**: apesar de tudo, o comentário é sobre o conector empregado pelo aluno.

**Observações (obrigatório):** *"FM02 e FM04 a 0 pela regra de validade mínima: problema inexistente e substituição por conector de sentido incompatível."*

### Exemplo 12. Evidência segmentada: um segmento vale, outro não

> **Devolutiva:** "Uma forma de resolver a repetição é escrever assim: 'Quando Camilo leu o bilhete, entendeu tudo.' Outra opção é: 'Ele leu e ele entendeu e ele saiu.'"

**Vetor:** `0 1 0 0 1 0 0 0 | 1`

**FM05 = 1**, porque existe ao menos uma ocorrência válida: o primeiro modelo resolve de fato a
repetição. O segundo modelo preserva o problema que deveria resolver e, sozinho, seria falso
positivo. Como basta um segmento válido, a devolutiva recebe 1, e o falso positivo vai para as
`Observações`, para que o binário não o apague. **FM02 = 1**: a repetição é nomeada.

**Observações (obrigatório):** *"FM05 = 1 pelo primeiro modelo ('Quando Camilo leu o bilhete...'); o segundo modelo ('Ele leu e ele entendeu e ele saiu') é falso positivo, repete o problema."*

### Exemplo 13. Desafio que perde a situação comunicativa

> **Devolutiva:** "O autor deste texto poderia desenvolver melhor o argumento final. Comente o que ele quis dizer e proponha uma continuação."

**Vetor:** `0 1 0 0 0 0 0 0 | 1`

**FM07 = 0**: formalmente é um convite a ampliar, mas a devolutiva trata a produção como texto de
terceiro e devolve ao aluno a tarefa de comentar o próprio texto como se fosse de outra pessoa.
Perdida a situação comunicativa, o desafio não se realiza como mediação.

**FM02 = 1**: a insuficiência do argumento final é apontada, e essa indicação continua válida. A
perda da situação comunicativa invalida o desafio, não a nomeação do problema. Decida sempre
função a função, nunca pela devolutiva inteira.

**Observações (obrigatório):** *"FM07 a 0 pela regra de validade mínima: a devolutiva se dirige ao 'autor deste texto' em terceira pessoa e pede ao aluno que comente a própria produção como se fosse alheia."*

---

## Resumo de bolso

| Se... | então |
|---|---|
| a pergunta já contém a correção | FM02, não FM03 |
| há repertório sem frase montada | FM04, não FM05 |
| há frase montada | FM05 |
| pede consertar o que existe | FM06 |
| pede conteúdo novo | FM07 |
| elogia nomeando o que foi feito | FM01 |
| afirma capacidade e projeta continuidade, sem nomear | FM08 |
| o movimento está na forma mas induz ao erro, reforça inadequação ou piora o texto | 0, e escreva nas Observações |
| há um segmento válido e outro falso para a mesma função | 1, e escreva os dois nas Observações |
| a devolutiva fala da escrita do aluno, mesmo sem termo técnico | MTL = 1 |
| a devolutiva fala da obra, ou faz elogio de fórmula | MTL = 0 |
| a devolutiva fala da escrita do aluno, mas fala errado | MTL = 1 mesmo assim |
| na dúvida sobre a presença do movimento | não marcar |
