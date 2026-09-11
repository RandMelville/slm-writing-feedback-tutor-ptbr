# Sobre o codebook da segunda codificação

**Para:** Prof. Marcelo Magalhães Foohs
**De:** Randerson Oliveira Melville Rebouças
**Data:** 29 de julho de 2026
**Anexo:** `codebook_respostas_modelo.pdf` (v0.2-Q)

---

Marcelo, você tem razão e o reparo é justo. Mandei o codebook de junho junto com um guia de julho, e o resultado é um instrumento que fala de E1 a E5, sinaliza o problema de E4/C10 e termina propondo como "próximos passos" quatro coisas que já fizemos. Para uma rodada que vai justamente sustentar a confiabilidade diante dos pareceristas, o instrumento não podia estar assim.

Segue o codebook novo, escrito para esta rodada. Os seis pontos que você pediu, um a um:

**1. Objeto identificado.** O documento diz na capa e na seção 1 que o material são as 39 devolutivas do `qwen2.5:3b-instruct`. Some qualquer coisa que sugira corpus humano.

**2. Unidade de análise.** Seção 2: a devolutiva integral do modelo, isto é, todo o conteúdo da coluna `Devolutiva` de uma linha, o parágrafo de reconhecimento e as perguntas tomados como um objeto só. Não a frase, não o campo isolado, não a pergunta isolada.

**3. Referências da rodada anterior removidas.** Saíram E1 a E5, a sinalização de qualidade de E4/C10, a descrição do corpus de 65 devolutivas e a lista de próximos passos.

**4. MTL incorporada formalmente.** Seção 4, com a sigla expandida: MTL é contração de **MeTaLinguístico**, e o nome por extenso da variável é *foco metalinguístico no texto do aluno*. A definição operacional é a mesma do Guia, palavra por palavra no que decide, porque o pré-registro a congelou e eu não quero mexer nela depois de escrita.

**5. Fronteiras com FM02, FM03 e FM04.** Seção 5, com um princípio explícito antes dos casos: as FMs perguntam *que movimento de mediação a devolutiva faz*; a MTL pergunta *sobre que objeto ela faz esse movimento*. São eixos ortogonais, e não existe regra aritmética ligando as colunas: a MTL não é soma nem consequência das FMs. Cada fronteira vem com uma tabela cobrindo as quatro combinações (1/1, 1/0, 0/1, 0/0), com exemplos inventados, nenhum deles tirado da planilha.

Aproveitei para registrar ali um padrão que é específico deste corpus e que me parece o principal risco de arrasto: o modelo faz muitas perguntas sobre o enredo da obra. Pergunta sobre enredo, personagem ou tema não é FM03 (não devolve ao aluno nenhuma escolha textual própria) nem MTL. Como são perguntas, e o formato de saída do modelo força perguntas, a tentação de marcá-las como reflexão é real.

**6. Estrutura do corpus registrada.** Seção 1: 13 cenários, cada um submetido três vezes, 39 respostas. Está dito com todas as letras que não são 39 cenários independentes, e estão listadas as três consequências práticas: respostas parecidas vão aparecer, cada linha se codifica por si, e não se deve tentar harmonizar entre repetições nem identificar quais linhas são do mesmo cenário. A inconsistência entre repetições é um dos resultados a medir, então forçá-la na codificação destruiria a medida. O tratamento estatístico do agrupamento (cenário como unidade amostral, ICC, bootstrap por cluster) fica comigo.

---

**Duas coisas que mantive de propósito, e por quê.**

**As definições das oito FMs estão intocadas.** Só mexi em pontuação. É deliberado: o κ desta rodada é sobre a v0.2, e é a comparação com o vetor de junho que mostra que a ampliação de FM02 e FM04 fez efeito. Se eu reescrevesse as definições agora, mesmo para melhor, perderia exatamente a medida que os revisores pediram. Por isso a versão se chama **0.2-Q**, e não 0.3: a taxonomia é a mesma, o que mudou é o objeto e a entrada da MTL.

**As âncoras e os casos-limite continuam vindo do corpus dos professores.** Foram esses exemplos que calibraram as definições em junho, na sua leitura, e trocá-los por exemplos novos descalibraria o instrumento no meio da série. Tirei os códigos de respondente e cenário, e o documento diz explicitamente que eles são fixadores de sentido e não fazem parte do material a codificar.

**Um detalhe de versionamento.** Não editei o Guia nem o pré-registro no que eles decidem, porque os dois estão declarados congelados e já estão com você. O Guia ainda cita `codebook_funcoes_mediacao.pdf` na linha de material; a seção 0 do codebook novo registra que o substitui nesta rodada. Para anotar, use este.

A explicitação das fronteiras foi escrita hoje, **antes de qualquer anotação**, e está datada dentro do próprio documento. Faço questão do registro: se ela aparecesse depois de eu ver os números, seria outra coisa.

Se alguma fronteira ainda parecer frouxa, me diga antes de começar. Depois que a passada começar, a regra continua sendo a de junho: anota em `Observações` e segue com a definição como está.
