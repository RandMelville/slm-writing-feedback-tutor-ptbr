# Codificação das Funções de Mediação — 65 devolutivas (codebook v0.2)

> Codificação por dois anotadores; concordância (κ) reportada na §6. Codebook v0.2 incorpora o
> refino de FM02/FM04 saído dessa rodada.
> Dados: `analises/codificacao_fm.csv` · script auditável: `analises/fm_coding.py` · figura: `analises/fm_frequencia.png`.
> Enquadramento (Prof. Marcelo): descritivo, emergente do corpus; sem comparação com o SLM.

## 1. As oito funções aparecem — a taxonomia é do corpus

Nenhuma FM ficou vazia; todas emergem das devolutivas reais. Frequência sobre as 65:

| Função | Presença | Função | Presença |
|---|---:|---|---:|
| FM01 Reconhecer competência | 69% | FM05 Modelar parcialmente | **9%** |
| FM02 Nomear o problema | 80% | FM06 Propor revisão | 57% |
| FM03 Provocar reflexão | 34% | FM07 Desafiar ampliação | 32% |
| FM04 Oferecer pista | 69% | FM08 Reforçar autonomia | 32% |

Média de **3,8 funções por devolutiva** (de 1 a 8). Nomear o problema (FM02), oferecer pista (FM04)
e propor revisão (FM06) são o **núcleo operacional** quase universal; **modelar (FM05) é raro** — só
E1 e E5 chegam a reescrever um trecho do aluno.

## 2. Há perfis distintos de mediação (a variação vira dado)

% dos 13 cenários em que cada professor aciona cada função:

| Prof | FM01 | FM02 | FM03 | FM04 | FM05 | FM06 | FM07 | FM08 | FM/dev |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| E1 | 100 | 77 | 23 | 69 | 15 | 69 | **0** | **0** | 3,5 |
| E2 | **8** | 100 | 62 | 46 | 0 | 62 | **0** | **0** | 2,8 |
| E3 | 38 | 69 | **0** | 69 | 0 | 69 | **0** | **0** | 2,5 |
| E4 | 100 | 85 | **0** | 85 | 0 | 31 | 69 | 77 | 4,5 |
| E5 | 100 | 69 | 85 | 77 | 31 | 54 | **92** | **85** | 5,9 |

![Figura 1. Funções de mediação por professor (% dos 13 cenários). O núcleo operacional (FM02 nomear, FM04 pista, FM06 revisar) é quase universal; o que distingue os perfis são FM01 (ausente em E2), FM03 (só E2 e E5), FM05 (só E1 e E5) e a camada FM07/FM08 (só E4 e E5).](fm_frequencia.png)

Lendo as linhas:

- **E2 — austero e reflexivo, sem afeto.** FM02 em 100% e **FM03 em 62%** (devolve o
  problema em forma de pergunta: *"Por que, de repente, ela desfez o marido?"*), com estratégia
  concreta (FM04 46%: *"reler o conto e anotar a sequência"*, *"substituir pelo pronome objeto"*).
  O que ele *não* faz é a camada afetiva: quase nenhum elogio (8%), nunca desafia ampliação nem
  reforça autonomia. Registro seco e centrado no leitor. 2,8 funções/devolutiva.
- **E3 — telegráfico.** Só o núcleo operacional (FM02/FM04/FM06, todos 69%), sem reflexão, sem
  modelagem, sem camada afetivo-expansiva. O mais enxuto, 2,5.
- **E1 — núcleo + reconhecimento + modelagem, sem expansão.** Reconhece (100%), nomeia, dá pista,
  propõe revisão, e é um dos dois que modelam (FM05) — porém **FM07=FM08=0**: nunca empurra o aluno
  a ir além nem fecha afirmando autonomia. 3,5.
- **E4 — afetivo-expansivo.** Forte em FM01 (100%), FM07 (69%) e FM08 (77%); também nomeia e aponta
  caminho (FM02/FM04 85%), mas **não usa pergunta reflexiva (FM03=0) nem modela (FM05=0)**, e propõe
  revisão pouco (31%). 4,5.
- **E5 — andaime completo.** Alto em tudo; único que combina reflexão (85%), modelagem (31%) e a
  camada expansiva (FM07 92%, FM08 85%). 5,9 funções/devolutiva.

## 3. Um núcleo comum e quatro diferenciadores

As assinaturas mais frequentes confirmam a estrutura: o combo dominante é `FM02+FM04+FM06` (11×) —
o **núcleo operacional**: nomear o problema, apontar o caminho, propor a revisão. Quase toda
devolutiva (fora os textos-teto puramente elogiados) passa por ele.

O que **distingue** os perfis não é esse núcleo — é a presença/ausência de quatro coisas:

- **FM01 reconhecer** — comum, mas **ausente no E2**.
- **FM03 reflexão** — só **E2 e E5** (provocação seca no primeiro, andaime no segundo); E3/E4 não usam.
- **FM05 modelar** — só **E1 e E5**.
- **FM07/FM08 ampliar + autonomia** — só **E4 e E5**.

Daí os perfis: E5 tem tudo; E2 = núcleo + reflexão, sem afeto; E4 = núcleo + afeto + expansão, sem
reflexão/modelagem; E1 = núcleo + reconhecimento + modelagem, sem expansão; E3 = núcleo nu.

Isso aterrissa a pergunta do Marcelo ("quais funções queremos que o sistema reproduza?"): o
repertório completo só aparece no perfil E5; os demais são recortes. Qual perfil a plataforma deve
espelhar, em complementaridade à professora, passa a ser uma decisão empírica e explícita.

## 4. A fronteira diretiva × pergunta

Quando o professor quer que o aluno acrescente opinião ou aprofunde, ele faz isso de dois modos, e
o modo decide a função: **como diretiva** ("acrescente uma breve opinião sobre Camilo") conta como
apontar caminho (FM04) sobre uma lacuna nomeada (FM02); **como pergunta** ("o final foi
surpreendente?") conta como provocar reflexão (FM03). É o que separa, num mesmo texto-teto, o E4
(diretiva → FM02+FM04) do E5 (pergunta → FM03). Essa distinção foi a principal lição da rodada de
κ e está fixada no codebook v0.2.

## 5. Honestidade metodológica

1. **Correções incorporadas (Prof. Marcelo, 2026-06-24).** (a) Terminologia: saiu a palavra
   "diagnóstico" (não consta em nenhuma FM); a análise usa só o vocabulário das funções. (b) O E2,
   antes lido como "puramente diagnóstico", foi recodificado (FM03 23→62%, FM04 8→46%) após viés
   sistemático meu de subler perguntas e estratégias austeras.
2. **E4/C10 desalinhada** (conteúdo do C9) segue marcada; codificável por função, mas isolada em
   qualquer contagem por foco.
3. **FM02/FM04 retêm subjetividade.** Foram as funções de menor κ (§6); a v0.2 as tornou mais
   inclusivas. Mesmo o especialista mostrou inconsistência residual em itens quase idênticos — a
   fronteira FM02/FM04/FM07 é genuinamente difusa e deve ser declarada como limitação.

## 6. Confiabilidade entre anotadores (κ)

Segunda codificação **cega e independente** pelo Prof. Marcelo (especialista em educação) sobre
amostra estratificada de 20 devolutivas (4 cenários × 5 professores; 160 decisões binárias), contra
a 1ª codificação. κ de Cohen por função:

| Função | κ | Função | κ |
|---|---:|---|---:|
| FM01 Reconhecer | **1,00** | FM05 Modelar | 1,00\* |
| FM02 Nomear | 0,58 | FM06 Propor revisão | **0,90** |
| FM03 Provocar reflexão | **1,00** | FM07 Desafiar ampliação | **0,90** |
| FM04 Oferecer pista | 0,45 | FM08 Reforçar autonomia | **0,78** |

**κ médio = 0,83** (concordância "quase perfeita", Landis & Koch); 12 das 20 devolutivas idênticas
nas 8 funções. \*FM05 testado em 1 único caso positivo — concordância trivial, pouco informativa.

**Achado direcional.** Em 100% das discordâncias foi o especialista marcando uma função **a mais** —
nunca o contrário —, concentrado em FM04 (+6) e FM02 (+4). Não é ruído aleatório, é um deslocamento
sistemático: o 1º anotador subcodificava *nomear insuficiência* e *apontar caminho*. Por isso a
correção foi refinar essas duas definições (codebook v0.2) na direção do especialista e recodificar
**só** FM02/FM04 nas 65 — o que elevou FM04 de 38→69% e FM02 de 66→80% e produziu os perfis acima.

**Ressalva (o que fica para uma rodada futura).** O κ=0,83 mede o codebook **v0.1**. A recodificação
inclusiva de FM02/FM04 (v0.2) **não** foi reavaliada com uma nova passada cega — fazê-lo sobre a
mesma amostra seria ajustar ao teste. Portanto: reporta-se κ=0,83 como a confiabilidade medida; uma
confirmação do v0.2 com novo anotador é trabalho futuro, não pré-requisito para esta análise.
