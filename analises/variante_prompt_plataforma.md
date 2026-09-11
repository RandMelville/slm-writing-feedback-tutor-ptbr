# A string em uso na plataforma mantém a conformidade medida no artigo

**Data:** 22/08/2026 · **Autor:** Randerson Oliveira Melville Rebouças
**Script:** `src/variant_platform_prompt.py` · **Bruto:** `data/results/variant_platform_prompt.json`

## A lacuna

O artigo mede o `SYSTEM_PROMPT` canônico, cuja primeira linha nomeia a persona: *"Você é o
Bento, um tutor socrático de Linguística Textual (Koch)…"*. A plataforma RemidiAção roda a
mesma instrução **sem a persona**, porque a orientação vetou o rótulo "socrático" por falta de
fundamentação. O resto das duas strings é idêntico, linha a linha (verificado pelo script).

A ADR-0019 da plataforma afirma que "o piloto roda o que foi medido". Estritamente, não rodava:
a string difere, e o próprio `src/prompts.py` do benchmark registra no cabeçalho que a instrução
é mantida verbatim **porque foi exatamente ela que gerou os 388 registros**, e alterá-la quebra a
reprodutibilidade. Duas saídas eram possíveis: restaurar a persona na plataforma, o que a
orientação já recusou, ou **medir a variante**. Este documento faz a segunda.

## Desenho

Mesma máquina, mesmo dia, mesmo servidor Ollama, mesmo modelo, e os hiperparâmetros do
Apêndice B do artigo: `temperature = 0.2`, `stream = false`, `format = "json"`, sem qualquer
coerção de gramática. Os 13 cenários canônicos, 3 repetições por condição, **n = 39 por
condição**, 78 chamadas no total.

Os instrumentos são os do próprio artigo, reaproveitados e não reescritos: o validador
estrutural `divergente()` (critérios C1 a C4 da §3.4) e os stems da taxonomia de Koch de
`metalinguistic_adherence.py`. O prompt da plataforma é **lido do arquivo-fonte dela**, nunca
copiado, para que uma divergência futura apareça na medição em vez de passar em silêncio.

## Resultado

| condição | n | conformes | % | IC 95% (Wilson) | mobiliza Koch | % | IC 95% (Wilson) | latência média |
|---|---|---|---|---|---|---|---|---|
| prompt do artigo | 39 | 39 | **100,0%** | [91,0%; 100,0%] | 22 | 56,4% | [41,0%; 70,7%] | 2.201 ms |
| prompt da plataforma | 39 | 39 | **100,0%** | [91,0%; 100,0%] | 26 | 66,7% | [51,0%; 79,4%] | 2.141 ms |

**Conformidade estrutural: idêntica e total nas duas condições**, reproduzindo o intervalo
publicado no artigo para o `qwen2.5:3b-instruct`.

**Aderência metalinguística:** 26/39 contra 22/39, OR = 1,55, **Fisher exato p = 0,485**. A
diferença **não é significativa**. A leitura correta é que remover a persona **não degradou** a
propriedade medida, e não que a tenha melhorado. Vale a ressalva já declarada no próprio scorer:
esta é uma **triagem de limite inferior**, presença de termo da taxonomia, não uma medida de
adequação pedagógica.

## Consequência

A afirmação da ADR-0019 passa a ser sustentada por medição, e não por suposição: a plataforma
roda uma condição **de conformidade equivalente** à publicada. A divergência de string continua
existindo e continua declarada; o que deixou de existir é a incerteza sobre o efeito dela.

## O que este resultado não responde

Nada sobre **validade**: se o feedback fala do texto que o aluno de fato escreveu. Essa dimensão
(G2 da rubrica de qualidade) não é medida por nenhum instrumento existente, e é justamente onde
os dados de campo do ciclo 2 da plataforma mostram falha (o modelo atribuiu nome de personagem a
um adjetivo do texto, e inventou uma relação de parentesco que não existia). Conformidade
estrutural e presença de terminologia podem ser perfeitas num feedback que fala de um texto
inexistente. É o próximo instrumento a construir.
