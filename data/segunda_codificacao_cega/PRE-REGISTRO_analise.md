# Pré-registro da análise da 2ª codificação cega

**Escrito em:** 27 de julho de 2026, **antes** de a anotação ser executada.
**Autor:** Randerson O. M. Rebouças
**Propósito:** fixar, antes de ver qualquer número, o que será reportado no artigo em cada
cenário de resultado. Sem isso, escolher a forma de relato depois de conhecer o κ é
escolha conveniente, e é o tipo de coisa que um revisor atento identifica.

Este documento é citável na *response letter* e vai junto com o material aberto do estudo.

---

## 1. O que está sendo medido

Duas análises independentes sobre as mesmas 39 saídas do `qwen2.5:3b-instruct`:

**(A) Confiabilidade da codificação das funções de mediação (Tabela 9 do artigo).**
Concordância entre o anotador 1 (codificação embutida em `analises/fm_coding_model.py`,
codebook v0.2) e o anotador 2 (passada cega), por função FM01 a FM08.

**(B) Validade de construto da métrica da RQ2.** Concordância entre a régua lexical de
palavra-chave (`src/metalinguistic_adherence.py`) e o julgamento especialista registrado na
coluna MTL.

## 2. Estatísticas a reportar (decidido antes da coleta)

Para as duas análises:

- **κ de Cohen por categoria**, com bandas de Landis & Koch (1977).
- **Concordância bruta (%)** ao lado de cada κ, sempre, não só quando conveniente.
- **Prevalência observada em cada anotador**, para o leitor julgar por si.
- Nas categorias com base rara ou saturada (na passada do anotador 1: FM01 em 39/39,
  FM05, FM06 e FM08 em 0/39), acrescentar **PABAK** (Byrt et al., 1993) e sinalizar
  explicitamente que o κ é degenerado ali, citando o paradoxo do κ (Feinstein & Cicchetti,
  1990). **Não** substituir o κ pelo PABAK: reportar os dois lado a lado.

Nenhuma categoria será omitida da tabela por ter resultado ruim.

## 3. Regra de relato da análise (A), confiabilidade das FMs

| Resultado | O que vai para o artigo |
|---|---|
| κ médio ≥ 0,61 (substantial ou acima) | Tabela 9 mantida como está, agora com o vetor de κ da v0.2 reportado ao lado. |
| κ médio entre 0,41 e 0,60 | Tabela 9 mantida, com a confiabilidade reportada e uma ressalva explícita de que a leitura função-a-função é indicativa; a conclusão passa a se apoiar no padrão agregado (ausência do núcleo corretivo), não nos percentuais individuais. |
| κ médio < 0,41, ou κ < 0,40 em FM02, FM04 ou FM06 | As três funções que sustentam a conclusão perdem o estatuto de evidência quantitativa. A Tabela 9 é rebaixada a ilustração qualitativa, os percentuais saem do *abstract* e da conclusão, e o achado é reformulado como observação de padrão, não como medida. |

Em qualquer um dos três casos os números são publicados.

## 4. Regra de relato da análise (B), validade da métrica da RQ2

| Resultado | O que vai para o artigo |
|---|---|
| κ ≥ 0,61 | A régua lexical é reportada como **proxy validado** do construto. A taxa de 51,3% deixa de ser "triagem indicativa" e passa a medida com validade de construto estabelecida, sempre acompanhada do κ. |
| κ entre 0,41 e 0,60 | A régua permanece **sonda corroborativa**, exatamente como o artigo já a trata hoje, agora com a limitação quantificada em vez de declarada. Reporto lado a lado a taxa da régua (51,3%) e a taxa do julgamento humano, e discuto a diferença. |
| κ < 0,41 | A régua lexical é declarada **inadequada como medida do construto**. A taxa de 51,3% sai do *abstract* e da conclusão. Em seu lugar entra a taxa obtida pelo julgamento especialista sobre as 39, que passa a ser a evidência da RQ2, com n e intervalo de Wilson. O achado da RQ2 não desaparece: muda de instrumento. |

**Compromisso explícito:** a definição da coluna MTL está congelada no
`GUIA_2a_CODIFICACAO.md` desta mesma data e **não será ajustada depois de ver os
resultados**. Se ela se mostrar mal formulada, isso é reportado como limitação, não
corrigido retroativamente.

## 5. Limitações já assumidas, a declarar no artigo

- **Juiz único.** A análise (B) confronta a régua com o julgamento de um especialista, não
  de um painel. O Revisor A pediu "independent human evaluation", não painel, mas a
  limitação é registrada.
- **Anotador coautor.** O segundo anotador é um dos autores, especialista em Educação,
  cego à codificação anterior e à ordem original. Isso passa a ser dito explicitamente no
  §7.4, no lugar da formulação atual ("a second, blind, and independent annotator"), e
  acrescentado ao CRediT.
- **Duas passadas separadas.** As colunas FM e MTL são preenchidas em varreduras
  distintas, para reduzir o arrasto de uma sobre a outra, mas pelo mesmo anotador. A
  independência entre os dois julgamentos é, portanto, parcial.
- **Viés de formato.** O esquema de saída do modelo força um movimento de reconhecimento
  (FM01) e abre espaço para reflexão e ampliação, o que já está discutido no §7.5 e
  continua valendo na leitura dos novos números.

## 6. Adendo de instrumento (29 de julho de 2026, antes da anotação)

O instrumento conceitual desta rodada passa a ser o `codebook_respostas_modelo.pdf`
(v0.2-Q), que substitui o `codebook_funcoes_mediacao.pdf` (v0.2) enviado no pacote de 27 de
julho. O motivo é documental: aquele documento fora escrito para o corpus dos cinco
professores e mantinha referências operacionais exclusivas daquela rodada.

O que o adendo **não** altera: as definições, inclusões, exclusões e casos-limite das oito
funções de mediação são idênticos aos da v0.2, e a definição operacional da coluna MTL é a
do `GUIA_2a_CODIFICACAO`, congelada na seção 4 acima. O que a v0.2-Q acrescenta é o
enquadramento do objeto (as 39 saídas do modelo, 13 cenários por 3 repetições), a unidade de
análise (a devolutiva integral do modelo), a formalização da variável MTL com a sigla
expandida, e a explicitação das fronteiras entre MTL e FM02, FM03 e FM04.

Esse desdobramento das fronteiras foi redigido nesta data, **antes de qualquer anotação da
segunda passada**, e é registrado aqui para que a cronologia fique auditável junto ao
material aberto do estudo.

## 7. O que não muda

As análises acima tocam apenas a RQ2 e a seção de referência especialista. Os achados
estruturais da RQ1 (312 chamadas primárias, o contraste 39/39 contra 0/39 na família Llama
3.2, o protocolo de falsificação e os testes de Fisher) são independentes desta codificação
e não são afetados por nenhum dos cenários acima.
