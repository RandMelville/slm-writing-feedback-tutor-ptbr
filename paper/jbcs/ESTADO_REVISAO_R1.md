# Estado da revisão R1 (JBCS), atualizado em 11/09/2026

> **➡️ O estado atual está na §13 (11/09): pareceres em mãos, carta fechada ponto a ponto, aval dos dois coautores. Falta: compilar no Overleaf, limpar o histórico local e dar push, release v1.6.0 (Zenodo), submeter. Prazo ~10/10/2026.** A §12 registra a codificação e o κ; as §§1 a 11 são histórico e devem
> ser lidas como tal: a §8 explica o que caiu em agosto e a §11 registra o pacote v0.5 e o
> recrutamento.

> **⚠️ LEIA A §8 ANTES DE QUALQUER COISA.** Em 30/07 o Marcelo apontou que as duas
> codificações comparadas no κ das FMs foram produzidas sob protocolos diferentes, o que
> invalida aquele κ como estimativa de confiabilidade. A investigação de 04–05/08 confirmou
> a objeção e encontrou um problema maior: **a 1ª codificação das 39 devolutivas do modelo
> foi produzida por assistente de IA, não por leitura humana.** O κ = 0,14 e a §7.6 do
> artigo, tais como estão, não se sustentam. Protocolo v0.3 escrito e enviado aos autores.
> **Tudo abaixo desta linha, até a §8, é o estado congelado de 30/07 e está superado no que
> toca à codificação do lado do modelo.**

## Histórico da própria revisão (30/07/2026)

> A 2ª codificação cega voltou do Marcelo, a análise pré-registrada
> foi executada e o artigo foi editado conforme as regras congeladas. O κ das FMs deu
> **0,14** e disparou a linha 3 do pré-registro (rebaixamento da Tabela 9); o κ da RQ2 deu
> **0,54** e disparou a linha 2 (régua mantida como sonda, limitação quantificada).
> Detalhe em §5 deste documento. Rascunho da resposta em `RESPOSTA_REVISORES_R1.md`.

## Histórico (congelado em 27/07/2026)

Decisão editorial de **27/07/2026**: *"a revised version is required for further review"*.
Prazo de **45 dias**, vence por volta de **10/09/2026**. Dois pareceres: Revisor A
("Revisions Required") e Revisor C ("Resubmit for Review"), ambos construtivos, nenhum
pedindo coleta nova nem experimento de inferência adicional.

**O trabalho está parado aguardando uma única coisa: a 2ª codificação cega do Prof.
Marcelo.** Todo o resto que não depende dela está feito.

---

## 1. Bloqueado no Marcelo

Enviados por e-mail em 27/07: `codificacao_cega_v02.xlsx` e `GUIA_2a_CODIFICACAO.pdf`.

**Pendência conhecida (27/07):** o codebook v0.2 (`codebook_funcoes_mediacao.pdf`) **não**
foi no mesmo e-mail, e o guia o referencia como anexo. Ele nunca viu a v0.2 (a passada de
junho foi contra a v0.1; a v0.2 nasceu depois, ampliando FM02 e FM04). Precisa ir numa
mensagem de seguimento, senão ele codifica de memória pela v0.1 e o κ mede a coisa errada.

Também não foram enviados a nota de encaminhamento nem o pré-registro, então ele não sabe
que isso veio de revisor nem que há prazo.

### Atualização de 29/07: codebook próprio da rodada da Qwen

Ele leu o guia, entendeu a tarefa e travou no codebook: o v0.2 é o documento de junho,
enquadrado no corpus dos cinco professores (E1–E5, o flag de E4/C10, "próximos passos" que
já executamos). Pediu um instrumento coerente com esta rodada antes de começar a codificar.

Entregue: **`data/segunda_codificacao_cega/codebook_respostas_modelo.{md,pdf}` (v0.2-Q)**.
Objeto identificado (as 39 saídas da Qwen), unidade de análise (a devolutiva integral do
modelo), referências da rodada humana removidas, MTL formalizada com a sigla expandida
(contração de *MeTaLinguístico*; nome por extenso "foco metalinguístico no texto do aluno"),
fronteiras MTL × FM02/FM03/FM04 com tabelas 2×2 de exemplos inventados, e o corpus
registrado como 13 cenários × 3 repetições.

Duas escolhas deliberadas, ambas justificadas no documento e na resposta a ele:
- **As oito definições estão intocadas** (só pontuação). O κ desta rodada é sobre a v0.2 e é
  a comparação com o vetor de junho que mostra que a ampliação de FM02/FM04 funcionou. Por
  isso a versão é 0.2-Q, não 0.3.
- **As âncoras seguem vindo do corpus humano**, sem os códigos E#/C# e com nota de que não
  fazem parte do material a codificar. Foram elas que calibraram as definições na leitura
  dele; trocá-las descalibraria o instrumento no meio da série.

Acompanham: `RESPOSTA_marcelo_codebook.{md,pdf}` (rascunho da mensagem, item a item) e uma
§6 de adendo no `PRE-REGISTRO_analise.md`, datada de 29/07, registrando a substituição de
instrumento e que a explicitação das fronteiras é anterior a qualquer anotação.

O `GUIA_2a_CODIFICACAO` **não** foi editado (está declarado congelado e já está com ele);
ainda cita o codebook antigo na linha "Material", e a §0 do codebook novo registra que o
substitui.

Quando a planilha voltar:
1. Rodar `src/cohen_kappa.py` sobre as colunas FM01–FM08 e sobre a coluna MTL.
2. Seguir **à risca** as regras de relato de `data/segunda_codificacao_cega/PRE-REGISTRO_analise.md`,
   escritas e datadas antes da anotação. Elas são vinculantes, inclusive nos cenários ruins
   (κ < 0,41 na RQ2 tira os 51,3% do abstract).
3. Escrever a §7.4 e a §8 com os números, e só então a *response letter*.

## 2. Feito nesta rodada

**Isolamento E3 executado e persistido.** `src/counter_experiment_e3_curl.py`, 26 chamadas
via `curl` em subprocess (2 modelos × 13 cenários), temperatura 0.2. Divergência **26/26**,
`pontos_fortes` como lista em todos os casos. Dados em
`data/results/counter_experiment_e3_curl.json`.

**A contagem de 80 corrigida para 100** nas seis ocorrências, incluindo duas que o revisor
não viu: o *abstract* e a seção **Data Availability**. Detalhamento explícito no §3.8
(E1 26, E2 24, E2b 24, E3 26). A Tabela 4 deixou de trazer "failure reproduced" e traz
0/13 e 0/13 com Wilson e Fisher, homogênea com as demais linhas.

**Análise em nível de cenário** (pedido do Revisor A). `src/scenario_level_rq2.py` →
`analises/scenario_level_rq2.json`. Resultado que responde pelo avesso: ICC(1) = −0,11,
DEFF = 0,79, n efetivo 49,5; bootstrap de cluster (B = 20.000) devolve [38,5%; 64,1%],
mais estreito que o Wilson ingênuo. O agrupamento **não** infla a precisão dos 51,3%.
Mantivemos o Wilson mais largo como leitura de referência, de propósito. O ICC não positivo
é substantivo: é a forma quantitativa da instabilidade.

**Afirmações causais abrandadas.** O *abstract* não diz mais "inherited from instruction
tuning"; diz o que o protocolo de fato mostra (invariância a temperatura e à camada de
transporte). Parágrafo novo no §5.2 delimitando que o desenho é comportamental e caixa-preta
e não atribui o comportamento a nenhuma etapa do pipeline.

**Fronteira de generalização** amarrada no *abstract* e na conclusão ao regime avaliado
(zero-shot, CPU-only, Q4, sem coerção, as oito famílias do §3.3).

**Related work ampliado** com quatro referências, metadados conferidos na fonte:
Essay-BR (Marinho et al., JIDM 2022), Barbosa & Mauá (PROPOR 2026), TutorBench
(Srinivasa et al., 2025) e Chan et al. (Applied Sciences 2026). O contraste somativo vs.
formativo está escrito, não só citado. TutorBench dá o parâmetro que o Revisor C pediu
(fronteira não passa de 56%, subtarefa de feedback ~51%), com ressalva explícita de que
não é comparação direta.

**Ressalva da RQ2 promovida** no *abstract* a sentença própria, antes dos números.

**Tabela 9 reenquadrada:** "Gap" → "Difference (pp)", "Experts" → "Specialist corpus",
legenda declarando distribuição descritiva de referência, não nota-alvo.

**Densidade:** o trio 3%/15%/0% contra 80%/69%/57% caiu de quatro ocorrências para uma
(o *abstract*) mais a tabela.

**DOIs.** Diagnóstico do Revisor C estava errado: as oito entradas **já tinham** campo
`doi`. O estilo imprime DOI para `@article` e `@inproceedings` mas não para `@misc`, que é
o tipo dos preprints do arXiv. Acrescentado `note = {DOI: ...}` nas oito. Isso vira uma
resposta melhor do que "adicionamos os DOIs".

**Tabela 5** com colunas de largura fixa + `\footnotesize`.

**Roadmap da Introdução** agora menciona a Seção 8.

## 3. Não verificado, e precisa ser

**Compilar no Overleaf.** O `sbc2023.cls` e o `apalike-sol.bst` não estão no repositório, e
não há LaTeX completo na máquina, então nada disto foi compilado. Conferir na primeira
compilação:
- a Tabela 5 cabe na coluna;
- os DOIs aparecem nas oito entradas `@misc`;
- as quatro referências novas renderizam.

**Nova versão do Zenodo** com o `counter_experiment_e3_curl.json`. O DOI conceitual
(10.5281/zenodo.20388846) permanece; a Data Availability agora declara 100 registros de
falsificação, então o depósito precisa bater.

## 4. Observações soltas

- `paulelder2007socratic` está na bib sem ser citada em lugar nenhum. Inócua com bibtex,
  mas talvez fosse para estar citada.
- Colisão de rótulos: **E1–E5** designa tanto os isolamentos do contra-experimento (§3.8,
  §5.3) quanto as cinco professoras (§7.3, Tabela 8). Nenhum revisor pegou, mas agrava a
  densidade de leitura de que o Revisor C reclamou. Renomear as professoras para P1–P5
  é barato.
- A `chave_cega.csv` está no `.gitignore`, seguindo a política do commit e679470, que
  retirou a chave de κ da primeira rodada do repositório público.

---

## 5. Execução da 2ª codificação (30/07/2026)

Planilhas recebidas: `codificacao_cega_QWEN_marcelo_consolidada.xlsx` e
`..._por_cenario.xlsx`. A segunda é superset estrito (abas "Codificação" e "Notas
metodológicas" idênticas byte a byte); usar só ela como fonte.

Análise: `analises/kappa_2a_codificacao.py` → `analises/kappa_2a_codificacao_resultados.txt`.

### Resultado (A) — confiabilidade das FMs

κ médio **0,138** sobre as 6 categorias definidas (FM05 e FM08 são 0/39 nos dois
codificadores, κ indefinido). Bruta média 76,1% (6 cat.) / 82,1% (8 cat.).

| FM | κ | bruta | anot.1 | anot.2 | PABAK |
|---|---|---|---|---|---|
| FM01 | 0,000 † | 92,3% | 39/39 | 36/39 | 0,85 |
| FM02 | 0,374 | 92,3% | 1/39 | 4/39 | 0,85 |
| FM03 | 0,082 ‡ | 51,3% | 4/39 | 21/39 | 0,03 |
| FM04 | 0,226 | 74,4% | 6/39 | 10/39 | 0,49 |
| FM05 | n/d | 100% | 0/39 | 0/39 | 1,00 |
| FM06 | 0,000 † | 94,9% | 0/39 | 2/39 | 0,90 |
| FM07 | 0,147 ‡ | 51,3% | 16/39 | 35/39 | 0,03 |
| FM08 | n/d | 100% | 0/39 | 0/39 | 1,00 |

† zero degenerado (anotador 1 constante). ‡ confundido com deriva de instrumento (FM03).

**Linha 3 do pré-registro disparou**, por dois caminhos: κ médio < 0,41 **e** FM02 (0,374) e
FM04 (0,226) abaixo de 0,40 por si sós. O zero da FM06 é degenerado e não conta; a regra
dispara sem ele.

Três leituras que sustentam o texto novo:
- **Direcionalidade:** 49/56 (87,5%) das divergências são o anotador 2 creditando função a
  mais. Replica o offset de 100% da 1ª rodada. Médias: 1,69 vs. 2,77 FMs por devolutiva.
  Como o argumento é sobre função **ausente**, o codificador mais generoso é o caso
  adversarial, e o padrão sobrevive a ele.
- **Deriva de instrumento:** FM03+FM07 concentram 38/56 divergências. A nota metodológica 5
  do Marcelo registra critério de FM03 mais inclusivo, que o anotador 1 não aplicou. **Não
  recalcular** com definição harmonizada: o pré-registro veda.
- **Conclusão sobrevive:** núcleo corretivo sob anot.2 é 10%/26%/5% contra 80%/69%/57% dos
  especialistas. FM05 e FM08 são 0/39 nos dois. É padrão replicado, não medida.

### Resultado (B) — validade de construto da RQ2

κ = **0,538**, bruta 76,9%. **Linha 2 do pré-registro.** Régua 51,3% (20/39) vs. juízo
especialista 53,8% (21/39); 9 divergências quase simétricas (4 sobre-crédito da régua, 5
falsos negativos). Os 51,3% ficam, agora sempre acompanhados do κ.

### Bônus não planejado

O agrupamento por cenário que o Marcelo fez às cegas acertou **13/13**. Reconstruiu a matriz
inteira só pelo texto do aluno. Entrou na §7.6 sem alegação estatística.

## 6. Edições aplicadas ao `main.tex` (30/07)

1. **Abstract:** trio 3%/15%/0% × 80%/69%/57% removido, virou padrão; κ=0,54 e 53,8%
   acrescentados ao lado dos 51,3%; κ=0,14 declarado.
2. **§6:** parágrafo novo "Construct validity of the lexical screen" com a análise (B).
3. **§7.4:** anotador descrito como coautor, não "independente"; frase final sobre "open
   item" substituída por ponteiro à §7.6.
4. **§7.5:** ressalva de codificador único reescrita; Tabela 9 declarada ilustração
   qualitativa; parágrafo de leitura reescrito para só afirmar o que sobrevive às duas
   codificações.
5. **Tabela 9:** coluna "Difference (pp)" removida, coluna "Coder 2 (blind)" acrescentada,
   legenda em negrito declarando que não é medida.
6. **§7.6 nova** (`sec:fm-blind`): tabela de κ/PABAK + 4 qualificações + achado 13/13.
7. **§8 Threats:** de cinco para seis limitações; item da RQ2 reescrito com κ=0,54; item novo
   sobre confiabilidade da codificação do modelo; limitações do pré-registro §5 (juiz único,
   anotador coautor, independência parcial) e a nota 11 do Marcelo (binário ≠ qualidade).
8. **§9 Conclusão:** percentuais fora, padrão dentro, κ das duas análises declarados.
9. **CRediT:** contribuição de codificação cega do Marcelo registrada.
10. **Materials:** pacote de confiabilidade + plano de análise datado declarados como
    material aberto.
11. **`references.bib`:** `byrt1993bias` (PABAK) e `feinstein1990high` (paradoxo do κ).
12. **Abstract cortado de 661 → 401 palavras** (a versão submetida tinha 551). Decisão do
    Randerson em 30/07 depois de ver que ocupava a página 1 inteira. Preservados: ressalva
    da RQ2 como sentença própria antes dos números, 51,3% + κ=0,54 + 53,8%, κ=0,83, κ=0,14,
    312+100 chamadas, reversibilidade one-shot, fronteira do regime. Comprimidos: o núcleo
    corretivo soletrado por extenso e a frase "used descriptively rather than as a
    performance yardstick". Responde de passagem à queixa de densidade do Revisor C.
13. **Tabelas 9 e 10 para `table*`.** A 1ª compilação no Overleaf mostrou as duas
    transbordando a coluna (a 9 derramava "Specialist corpus" por cima do texto; a 10 cortava
    "Coder 2" e PABAK na margem). Passaram a `\begin{table*}[!t]`, mesmo padrão das outras
    cinco tabelas largas. A nota de rodapé da Tabela 10 (símbolos † e ‡) foi **para dentro**
    do float, numa `minipage{\textwidth}`, senão flutuaria para longe da tabela que explica;
    por isso o "discussed below" virou "discussed among the qualifications in Subsection 7.6".
14. **Conversores atualizados** (`tex_to_docx.py`, `tex_to_pdf.py`): CITE + REFERENCES com as
    duas entradas novas, mapa REF com `sec:fm-blind`=7.6, `sec:fm-role`=7.7 e
    `tab:fm-kappa-model`=10, e `split_row()` novo expandindo `\multicolumn` para N células.
    Esse último consertou também as linhas de média das Tabelas 6 e 8, que vinham
    deslocadas uma célula desde sempre. Só afeta os artefatos de leitura, não o Overleaf.

## 7. Situação ao encerrar a sessão de 30/07/2026

**Compilação no Overleaf: OK.** Segunda compilação, depois do fix de `table*`, saiu limpa
(23 páginas). O PDF foi salvo na raiz do repo como
`SLMs_for_Offline_Writing_Feedback_Tutoring_in_Brazilian_Portuguese.pdf` e **enviado ao
Marcelo em 30/07**. Os artefatos de leitura `paper/jbcs/benchmark_slm_jbcs.{pdf,docx}` foram
regerados a partir do mesmo `main.tex` final, caso ele peça o Word.

**O `main.tex` está fechado para esta rodada.** Fonte de verdade, como sempre.

### O que falta

1. **Pareceres completos, bloqueante para enviar.** `RESPOSTA_REVISORES_R1.md` cobre a fundo
   os quatro itens desta rodada (2ª codificação, validade da RQ2, estatuto do anotador,
   achado 13/13). O resto está listado no fim do arquivo mas precisa ser pareado com o texto
   verbatim dos revisores, que **não está no repositório**. Colar os dois relatórios num
   arquivo aqui é o primeiro passo da próxima sessão.
2. **Zenodo.** A seção Materials agora declara publicamente o pacote da 2ª codificação e o
   pré-registro datado. O depósito precisa passar a incluí-los, senão a declaração fica falsa.
   O DOI conceitual (10.5281/zenodo.20388846) permanece.
3. **Planilhas do Marcelo soltas na raiz.** `codificacao_cega_QWEN_marcelo_consolidada.xlsx`
   e `..._por_cenario.xlsx`. A segunda é superset estrito da primeira. Mover para
   `data/segunda_codificacao_cega/` e decidir se as observações qualitativas dele vão
   públicas (o artigo já cita as notas metodológicas dele na §8).
4. **Prazo:** vence por volta de **10/09/2026**.

### Não urgente, mas anotado

- Colisão de rótulos E1–E5 (isolamentos do contra-experimento × as cinco professoras)
  continua. Renomear as professoras para P1–P5 é barato e ataca a densidade que o Revisor C
  criticou.
- `paulelder2007socratic` segue na bib sem ser citada.
- As notas metodológicas 1 (definição emergente de qualidade) e 13 (presença formal de FM não
  autoriza entrega direta ao aluno) do Marcelo **não** entraram nesta revisão, para não abrir
  escopo. São material do paper de 2027. A nota 11 (binário ≠ qualidade) entrou na §8.

---

## 8. Ruptura do protocolo de codificação (04–05/08/2026)

### 8.1 O que o Marcelo apontou

Em quatro mensagens entre 29 e 30/07, mais a planilha consolidada:

1. **Vazamento de ancoragem.** O codebook v0.2-Q informava ao 2º codificador a média de FMs
   da 1ª passada (1,7 contra 3,8 das humanas). Nota metodológica 8 dele.
2. **A nota da FM03 induz viés.** A exclusão de perguntas sobre enredo/personagem/tema não é
   sempre verdadeira: pergunta sobre a obra pode levar a reexaminar escolha do próprio texto.
   Redação substituta na nota metodológica 5.
3. **Presença de FM não é qualidade** (notas 2, 7, 11), e a devolutiva integral como unidade
   não corresponde ao corpus: evidências aparecem em segmentos (nota 6).
4. **Bloqueante:** "as duas codificações que seriam comparadas foram produzidas com
   protocolos diferentes. Nessas condições, não se pode calcular concordância entre elas."

### 8.2 O que a investigação de 04–05/08 verificou

Tudo abaixo foi conferido nos arquivos, não inferido.

- **Os números do artigo estão corretos.** κ recomputado do zero a partir da planilha do
  Marcelo cruzada com `chave_cega.csv`: idêntico em todas as células (κ médio 0,1383,
  bruta 82,1%, 49/7 divergências, 1,69 vs 2,77, RQ2 κ=0,5375, 20/39 vs 21/39). O achado
  13/13 confere contra a chave: 13 trios puros, 39 IDs únicos.
- **O defeito de instrumento é estreito.** Diff campo a campo v0.2 × v0.2-Q: as oito
  definições são substantivamente idênticas (única troca de palavra na FM05). O ÚNICO
  acréscimo substantivo é a "Nota específica deste corpus" da FM03 (0 ocorrências na v0.2).
  A "Fronteira com FM03" da FM04 já existia na v0.2. O vazamento está na linha 44 do
  codebook e também foi enviado em mensagem.
- **A contaminação toda empurra para concordância.** O vazamento apontava para menos funções
  e ele marcou mais; a nota da FM03 mandava não marcar e ele marcou 21/39. **κ=0,14 é limite
  superior.** É o que a nota 8 dele já dizia ("inflar a concordância").
- **O defeito não explica o resultado.** κ sem FM03 = 0,149 contra 0,138 com. A FM07, de
  definição idêntica nos dois instrumentos, tem as mesmas 19 divergências da FM03.
- **A 1ª codificação das 39 foi produzida por assistente de IA.** Registrado no docstring de
  `analises/fm_coding_model.py` ("anotador 1, Claude"); commit `ce2ca08` com Co-Authored-By.
  Contraste: `fm_coding.py` (65 humanas) não tem essa marca, commit `20d2e05` não tem
  Co-Authored-By, e o gabarito removido tinha coluna `minhas_FMs`. **Confirmado pelo
  Randerson em 04/08.** Logo o κ=0,14 nunca foi concordância entre anotadores.
- **`main.tex` linha 602 está factualmente errada:** diz "coded independently under codebook
  v0.2"; o 2º codificador usou v0.2-Q.
- **A §7.6 usa as notas 5 e 11 do Marcelo e ignora as notas 8, 9 e 10**, que são as que
  atingem a validade do κ. Elas estavam na planilha desde 30/07.

### 8.3 Data Availability declara três coisas falsas

| Declarado na §Materials | Situação real |
|---|---|
| codebook v0.2-Q, pacote de anotação, plano de análise | versionados ✔ |
| codificação completa das 39 com justificativas e notas | **não versionada** (xlsx soltas na raiz) |
| script de análise que produz a Tabela 10 | **não versionado** (`analises/kappa_2a_codificacao.py`) |
| arquivo permanente no Zenodo | **só a v1.5.0 de 29/06**, um zip de 1,9 MB; não tem o pré-registro (27/07), o codebook v0.2-Q (29/07), a codificação (30/07) nem o `counter_experiment_e3_curl.json` (27/07) que sustenta as "100 falsification calls" |

### 8.4 A sequência acordada com o Marcelo

Ele passou o passo a passo e o Randerson concordou:

1. Revisar o protocolo com base nas notas metodológicas. ✔ **feito** (`data/segunda_codificacao_cega/PROTOCOLO_REVISADO_v03.{md,pdf}`)
2. Enviar o protocolo revisado para concordância explícita dos três autores. ← **estado atual, aguardando**
3. Entregar a um novo codificador, sem acesso às codificações anteriores.
4. Comparar com a codificação do Marcelo, ambas sob o mesmo protocolo.
5. Recalcular a concordância e consolidar por cenário (3 execuções × 13 cenários).
6. Reescrever método, resultados e discussão narrando com transparência o que motivou a recodificação.
7. Atualizar a resposta ponto a ponto aos avaliadores.

Os dois revisores pediram o κ das FMs com todas as letras (Revisor C: *"carrying out this
second coding pass and reporting the corresponding κ"*; Revisor A: *"further reliability
validation, particularly for the mediation functions"*), então abrir mão do κ não era opção.

### 8.5 O que o protocolo v0.3 muda

FM03 com a redação da nota 5 (cai a exclusão das perguntas sobre a obra); unidade com
evidência segmentada (nota 6); nenhum agregado de passada anterior nem regra derivada do
corpus (nota 8); momento do confronto fixado (nota 9); preservação com errata (nota 10);
binário ≠ qualidade como limitação declarada (nota 11); consolidação por cenário no plano
de análise. Seção 1.2 do protocolo registra a procedência da codificação por IA. Seção 7
declara a assimetria residual: a passada do Marcelo carregou a ancoragem de densidade, a
nova não.

### 8.6 O que NÃO é atingido

- **A escolha do modelo do piloto.** Vem de conformidade estrutural, latência e Fisher sobre
  412 chamadas, tudo verificado por programa. ADR-0001 e ADR-0019 da plataforma seguem válidas.
- **κ = 0,83 do corpus humano** (par: Randerson × Marcelo, junho, devolutivas de professores,
  codebook v0.1). Outro corpus, outro instrumento.
- **κ = 0,54 da RQ2.** Ali a comparação é entre régua executada por programa e o juízo MTL,
  não entre dois codificadores. Ressalva a acrescentar: a nota da §5.2 do v0.2-Q pode tê-lo
  inflado, então é limite superior também.
- **O achado 13/13** dos cenários, verificado.

### 8.7 Pendências

1. **Aguardando** aprovação do protocolo v0.3 pelos três autores.
2. Depois: pacote cego novo, recrutar o codificador externo, recodificar, recalcular.
3. Reescrever §7.4, §7.5, §7.6, §8, abstract, conclusão e Data Availability.
4. Versionar `analises/kappa_2a_codificacao.py`. **Decisão pendente do Randerson:** as duas
   `.xlsx` do Marcelo vão para o repositório público com as observações qualitativas dele?
5. Nova versão do Zenodo com tudo da R1.
6. **Prazo: ~10/09/2026.**

---

## 9. Parecer do Marcelo sobre o v0.3 (10/08/2026)

`Observacoes_Protocolo_Revisado_v03.docx`, na raiz do repositório. Ele aprova o que o v0.3
incorporou (FM03 revista, evidência segmentada, retirada da ancoragem, separação FM×MTL,
preservação dos registros, consolidação por cenário) e levanta cinco pontos que **mudam o
plano acordado em 05/08**.

### 9.1 Regra de validade mínima das FMs (o ponto principal)

> Uma ocorrência somente deve ser codificada como 1 quando, além de apresentar as
> características formais da função, for semanticamente compatível com sua finalidade
> mediadora. Movimentos que se apresentem formalmente como uma FM, mas induzam o aluno ao
> erro, reforcem uma inadequação ou proponham alteração que possa piorar a produção devem ser
> considerados falsos positivos e codificados como 0.

Operacionalizada função a função, FM01 a FM08, no parecer. Justificativa dele: o artigo já
assume uma dimensão qualitativa (a RQ2 é "pedagogical-qualitative", e o texto registra que o
modelo elogia como qualidade o fenômeno plantado como problema, chegando a dizer que
"positively reinforces it"). Não é a qualidade plena, que depende de aluno real em interação
e fica para o piloto; é a validade mínima necessária para decidir se a FM ocorreu.

**Registro de evidência segmentada:** havendo um segmento válido e outro falso para a mesma
FM, codifica 1, e as Observações identificam os dois segmentos com justificativa, para que o
binário não apague o falso 1.

### 9.2 A codificação nº 4 sai do cálculo

A regra de validade mínima altera o instrumento de forma substantiva e pode mudar códigos que
ele já atribuiu. Na planilha há linhas com FM marcada como presente e Observação registrando
que a devolutiva elogia característica inexistente ou dá orientação tecnicamente inadequada.
A codificação dele é **preservada como percurso metodológico**, não como dado do κ.

### 9.3 Dois novos codificadores, não um

Sequência revista:
1. Discutir e aprovar entre os autores a versão final do protocolo.
2. Congelar antes de qualquer codificação.
3. Entregar o mesmo protocolo a **dois** novos codificadores independentes, sem acesso às codificações anteriores.
4. Preservar as duas separadamente antes de qualquer confronto.
5. Calcular a concordância **exclusivamente entre as duas novas codificações**.
6. Consolidar pelos 13 cenários, com as três execuções de cada.
7. Revisar método, resultados, discussão, limitações e conclusões.
8. Relatar aos avaliadores o percurso que levou à revisão do instrumento.

### 9.4 Correção de inferência no v0.3

O v0.3 escreveu: *"retirando a FM03 do cálculo, o κ médio vai de 0,138 para 0,149. O defeito
de instrumento, portanto, não explica o resultado."* **A segunda frase não decorre da
primeira.** O que o número mostra é que a regra antiga da FM03 não explica a discrepância
sozinha, não que o instrumento não contribua. A FM07 tem o mesmo número de divergências e
precisa ser investigada antes de afastar a hipótese, e a própria regra de validade mínima
oferece a hipótese: a definição da FM07 pode estar contando como desafio de ampliação
formulações apoiadas em informação inexistente ou situação comunicativa incoerente.
**Corrigir no v0.4.**

### 9.5 Outras exigências

- A procedência da codificação por IA precisa aparecer **no texto do artigo** com a mesma clareza que está no protocolo. Hoje o artigo diz "we coded the 39 outputs" e "a single-coder pass", o que permite ler como pessoa.
- Os exemplos dados aos novos codificadores **não podem** sair das 39 devolutivas que serão recodificadas. Só exemplos construídos ou do corpus humano.

### 9.6 Estado e esforço

- Enviado à Profa. Rosa em 10/08, com o Marcelo em cópia, o parecer + o `PROTOCOLO_REVISADO_v03.docx` (gerado com pandoc; o `paper/md_to_docx.py` usa `textutil`, ignora argumentos de linha de comando e sobrescreve o `.docx` do artigo, não usar).
- **Aguardando a leitura técnica da Rosa** para escrever o v0.4.
- **Esforço de referência: a codificação das 39 levou ~10 h.** Com dois codificadores, são ~20 h de trabalho de terceiros.
- **Os dois codificadores já estão garantidos** (Randerson, 10/08).
- Prazo da revista: ~10/09/2026.

---

## 10. Protocolo v0.4 e pacote dos codificadores (22/08/2026)

### 10.1 A Rosa respondeu em 11/08

Duas mensagens, na thread "Artigo JBCS - Benchmark de modelos - Protocolo revisado de codificação":

> "Randerson, concordo com encaminhar os dois documentos. Eu já tive uma situação semelhante ao
> analisar ressonâncias Magneticas (para um colega da área médica): as ressonâncias eram produzidas
> por máquinas diferentes. Mas a revista não colocou problemas, apenas apontamos estas diferenças.
> Como se tratava de medir um espaço do cérebro humano, cada conjunto de RMI foi analisado em
> função das características de cada máquina. A conclusão final juntou os resultados e foi única."

> "Prezado Randerson, concordo totalmente."

Vale para a carta-resposta: é um precedente de co-autora para declarar a diferença de procedência
em vez de escondê-la, com a conclusão final juntando os resultados.

### 10.2 O que foi produzido

Tudo em `data/codificacao_v04/`:

**Vai aos codificadores:** só o `GUIA_PROFESSOR` e a planilha. O material foi simplificado em
22/08 porque quem codifica são professores, não metodologistas: protocolo com histórico do estudo,
plano de análise e limitações é documento de artigo, não de tarefa, e treze vetores resolvidos
funcionariam como gabarito.

| Arquivo | O que é |
|---|---|
| `GUIA_PROFESSOR.md/.pdf/.docx` | **único documento entregue.** 3 páginas, ~1.150 palavras, sem jargão de método: oito definições em linguagem de professor com um exemplo cada, a coluna MTL, a regra do "parece mas não é" com três exemplos, quando escrever em Observações, três combinados de independência, prazo. Abre com o contexto da tese (PPGIE/UFRGS, devolutiva como 1ª passada com a professora conduzindo) e declara que os textos de aluno são fictícios; fecha dizendo o que acontece com a leitura, o crédito nos agradecimentos e que o pagamento não depende do resultado. Não diz a procedência das devolutivas, que é contada depois da entrega |
| `PROTOCOLO_v04.md/.pdf/.docx` | **interno.** Instrumento congelado e registro metodológico citado no artigo; regra de validade mínima na §3.0, item de falso positivo em cada FM, inferência da FM03/FM07 corrigida na §1.3, codificação nº 4 fora do κ na §1.5 |
| `ANEXO_CALIBRACAO.md/.pdf/.docx` | **interno.** Treze exemplos resolvidos, cinco de falso positivo, um de evidência segmentada; fonte de onde saíram, reduzidos, os exemplos do guia |
| `build_pacote_v04.py` | reconstrói as 39 da fonte e afirma, por assert, que são idênticas às de julho; gera os dois pacotes |
| `verifica_exemplos.py` | confere por programa que nenhum exemplo dos três documentos sai das 39 (102 trechos, 19 do corpus humano, 0 das 39) |
| `pacote_v04_codificador_{A,B}.csv` | material de anotação, mesmos IDs R01–R39 para os dois |
| `RECRUTAMENTO.*` | **fora do versionamento**, só no diretório local (está no `.gitignore`, porque traz valores e dados de contato). Perfil exigido dos codificadores e impedimentos (não pode ser autor nem um dos cinco professores do corpus humano), condições de remuneração, mensagens de recrutamento e o rascunho em inglês da frase de qualificação dos codificadores para a seção de confiabilidade |
| `EMAIL_convite_codificador.md` | texto do convite. Não há e-mail de congelamento: o parecer de 10/08 e o aceite da Rosa de 11/08 já fecharam a decisão, e o v0.4 é a execução dela |

Planilhas no Google Sheets, criadas e **ainda não compartilhadas** (faltam os e-mails dos dois
codificadores):

- Codificador A: `1wIGoRDItjZiRW-duak_gKpmzJEpBbE8MYHpO7nSv4gg`
- Codificador B: `1gjRHxW-Uh9UpiiFJS6HY7CltzckbK8pCM0nhEuhu3T0`

Três rascunhos no Gmail: um na thread dos autores (congelamento) e um por codificador, sem
destinatário. Os anexos precisam ser arrastados na hora de enviar, a API de rascunho não os aceita
a partir do repositório.

### 10.3 Recrutamento dos dois codificadores

Decidido em 22/08: os codificadores são recrutados **por chamada pública no LinkedIn**, com
formulário de inscrição (nome, Lattes, formação, tempo de sala de aula, rede, prática de devolutiva,
disponibilidade e a pergunta de contato prévio com o estudo). Material em `RECRUTAMENTO.*`, que
fica fora do versionamento por conter valores e dados de contato.

Perfil exigido: licenciatura em Letras (Português), 3 anos ou mais de Ensino Fundamental II com
experiência em 8º ou 9º ano, prática atual de corrigir produção textual com devolutiva escrita.
Impedidos: autores, integrantes do grupo de pesquisa, os cinco professores do corpus humano e quem
já teve contato com o material do estudo.

O recrutamento aberto **melhora o artigo**, e não só resolve a logística: a seção de confiabilidade
passa a poder declarar quem codificou, com que qualificação, o que garantiu a independência e que a
remuneração foi fechada antes e não depende do resultado. O rascunho dessa frase, em inglês, está
no `RECRUTAMENTO.md` §6.

Esforço informado aos candidatos: ~10 h, que é o registro do próprio Marcelo ao codificar as mesmas
39 devolutivas. É o único dado real de esforço que existe sobre esta tarefa.

### 10.4 Cronograma até o prazo

| Quando | O quê |
|---|---|
| 22/08 | publicar a chamada e abrir o formulário |
| até 26/08 | inscrições |
| 27/08 | escolha das duas pessoas, combinação do valor, compartilhamento das planilhas e envio dos convites |
| até 05/09 | as duas codificações, ~10 h cada |
| 05–09/09 | κ(A,B), consolidação por cenário, exame da FM07, reescrita de método, resultados, discussão, limitações e conclusão |
| 10/09 | prazo da revista |

**Sem folga.** Se em 27/08 o formulário não tiver dois nomes de perfil adequado, o plano B é convite
direto a contatos com o mesmo perfil e o mesmo valor, decidido no mesmo dia.

### 10.5 Pendências que não dependem de terceiros

- `analises/kappa_v04.py`: adaptar `kappa_2a_codificacao.py` para o par A × B; dá para escrever e testar com dados sintéticos enquanto a codificação acontece.
- Zenodo: só a v1.5.0 de 29/06 está depositada, sem nada da R1. A Data Availability declara material que não está lá.
- Decisão em aberto: as `.xlsx` do Marcelo, com as observações qualitativas linha a linha, vão para o repositório público?
- A procedência da codificação por IA ainda precisa entrar no **texto do artigo** (§ método), não só no protocolo.

---

## 11. Revisão de Marcelo, pacote v0.5 e codificadoras (25 e 26/08/2026)

### 11.1 Rosa fora desta etapa

Rosa comunicou em 25/08 pela manhã que não conseguiria ler o material no tempo necessário, por cirurgia de familiar e cerca de três semanas de acompanhamento. Marcelo respondeu que ele e Randerson seguem sozinhos nos dois artigos. **Há um parecer, não dois.** O protocolo registra a manifestação dela como "não solicitada nesta etapa, em razão de indisponibilidade comunicada".

### 11.2 A revisão: separar presença da FM de falso positivo

Marcelo devolveu em 25/08 às 12h15 os cinco arquivos do benchmark revisados. A mudança é uma só e reorganiza o resto.

Na v0.4, a regra "parece, mas não é" mandava marcar 0 quando o movimento estava presente na forma mas se apoiava em leitura errada do texto do aluno. Na revisão, o mesmo caso vira `FM = 1` e `FP = 1`: a presença fica numa coluna, a inadequação em outra.

| | v0.4 | v0.5 |
|---|---|---|
| Decisões binárias por linha | 9 (FM01-08 + MTL) | **17** (FM01-08 + FP01-08 + MTL) |
| Colunas da planilha | 13 | **37**, com evidência por FM e justificativa por FP |
| MTL | objeto, com validade embutida | objeto puro; a inadequação vai para o FP |
| Derivada | — | **VFM** = 1 quando FM = 1 e FP = 0 |
| Codificação nº 4 | fora do κ | fora do κ e explicitamente incomparável |

**Por que aceitar:** a regra antiga pedia duas decisões de naturezas diferentes dentro de um binário só, "o movimento está aqui?" e "o movimento se sustenta?". A primeira é quase objetiva, a segunda é interpretativa. Separadas, a hipótese de que a mistura explicava o κ = 0,14 passa a ser testável. E o FP vira achado por si.

**Custo medido:** 2,77 FMs marcadas por devolutiva na codificação de julho, logo cerca de 108 colagens de evidência por codificador. Evidência é copiar e colar, não julgar.

### 11.3 Os quatro ajustes, aprovados em 26/08 às 11h23

1. A planilha passou a **impedir** `FM = 0` com `FP = 1`, por validação com fórmula, não só a sinalizar. Preferência dele: mudar o instrumento, não o texto do Protocolo.
2. Linha de cabeçalho e colunas A a C congeladas nas duas planilhas.
3. Parágrafo na §6 do Protocolo dizendo que a VFM é medida derivada **mais estrita** que a de julho: segmento misto ficava 1 e agora produz VFM = 0, logo comparações são exploratórias e as medidas não são equivalentes.
4. `verifica_exemplos.py` reapontado para os arquivos do conjunto final e reexecutado, com o registro preservado.

Todos executados. Resultado da verificação: **103 trechos, 16 do corpus humano (fonte permitida), 0 vindos das 39**, em `verificacao_exemplos_2026-08-26.log`.

### 11.4 Duas ressalvas dele que precisam entrar na redação

> "não devemos antecipar que o κ das FMs necessariamente subirá; isso será determinado pelas duas novas codificações"

> "A frequência de FP poderá constituir um resultado relevante sobre o modelo e as condições avaliadas neste estudo. A generalização para modelos pequenos em geral dependeria de evidência mais ampla."

As duas procedem e corrigem afirmações que estavam sendo feitas. A separação FM×FP é **hipótese a testar**, não resultado previsto. E o achado de FP é sobre `qwen2.5:3b-instruct` nas 39 devolutivas, não sobre SLMs ≤3B em geral. **Ajustar §7 e a discussão de acordo.**

### 11.5 Onde está o pacote

`data/codificacao_v04/`, sufixo `_v05`, com `README.md` próprio. A v0.4 foi movida para `_superado_v04/`. Os `.md` foram reconstruídos por pandoc a partir dos `.docx` revisados por Marcelo, preservados em `revisao_marcelo_2026-08-25/` junto da análise completa da revisão.

`para_drive/` reúne só o que sai daqui: as duas planilhas, o guia em PDF e o `LEIA_ANTES_DE_IMPORTAR.md` com as quatro checagens pós-conversão no Google Sheets, onde a validação de recusa pode virar simples aviso.

Commits: `c6ddba1` (pacote) e `43ce809` (correção de um laço infinito em `paper/md_to_pdf.py` diante de linha horizontal, que aparecia agora porque os `.md` vêm de conversão de `.docx`).

### 11.6 Codificadoras escolhidas

Três candidatas no formulário. **Escolhidas: as codificadoras A e B.** A terceira candidata fica como reserva. Randerson envia os convites. (Os nomes ficam fora deste arquivo, que é público: a Declaration do artigo as identifica só como *coder A* e *coder B*.)

Perfil que entra no método do artigo, sem nome:

- Licenciatura em Letras e mestrado em Linguística Aplicada; 6 a 10 anos de Ensino Fundamental II; atua hoje em 8º e 9º; rede pública municipal; corrige produção textual com devolutiva escrita; pesquisou avaliação textual na Olimpíada de Língua Portuguesa e faz o curso de avaliadores de redação do ENEM.
- Licenciatura em Letras e mestrado em Linguística Aplicada; mais de 10 anos de Ensino Fundamental II; rede pública municipal; experiência de correção de redação em vestibulares e no ENEM.

Critério do desempate: o §1 do `RECRUTAMENTO.md` exige perfil equivalente entre as duas na experiência com produção textual. A reserva tem mais tempo de sala mas nenhuma experiência com rubrica, e pareá-la com a segunda produziria divergência por diferença de calibragem, não por defeito do instrumento.

Verificado: nenhuma das três está entre os professores do corpus humano.

### 11.7 Riscos abertos no recrutamento

1. **O formulário publicado perdeu os campos 13 e 14 do `RECRUTAMENTO.md` §8.** Ninguém declarou disponibilidade, e ninguém respondeu à pergunta de contato prévio com o estudo, que o documento marca como "o filtro de independência e não pode faltar" e que é o que sustenta a afirmação de independência no artigo. Precisa ir na mensagem de convite.
2. **Os links do Sheets em `EMAIL_convite_codificador.md` são de 22/08 e apontam para a v0.4**, com 13 colunas e sem FP. Substituir pela importação das planilhas v0.5.
3. **Valor contraditório dentro do `RECRUTAMENTO.md`:** §2 sugere R$ 700 por pessoa, §7 traz tabela de R$ 300 a R$ 500. E a v0.5 aumentou o trabalho de 9 para 17 decisões por linha. Fechar um número antes de escrever.
4. O convite foi reescrito para a tarefa nova, com as horas e o prazo marcados como `[X]` e `[DATA]`, à espera dessas decisões.

### 11.8 O que continua valendo da §10

`analises/kappa_v04.py` ainda não existe e precisa ser adaptado para o par A × B, agora com FP e VFM além de FM e MTL. O depósito no Zenodo continua sem nada da R1. E a procedência da codificação por IA ainda precisa entrar no texto do artigo, não só no protocolo.

---

## 12. Codificação concluída, κ calculado e §7 reescrita (04–10/09/2026)

**Esta é a seção de retomada. As §§1 a 11 são histórico.**

### 12.1 As duas codificações

A codificadora A entregou em 04/09, a B em 07/09. A auditoria de 08/09 achou
pendências nas duas, cada uma foi consultada por escrito apenas sobre as próprias células, sem
que nenhuma classificação alheia fosse revelada e sem pedido de revisão de julgamento, e as
duas editaram a própria planilha em 08 e 09/09.

**A dúvida que decidia o κ foi resolvida por escrito**, não por suposição. B: *"Eram realmente 0,
entendi que FP eu apenas preencheria quando 1. Mas já consertei, colocando zero nas faltantes."*

Há duas capturas em `data/codificacao_v05_respostas/`, e **a de 10/09 é a que vale**: passa na
auditoria sem célula vazia, sem valor fora de `{0,1}` e sem violação da regra 3.0 nas duas
planilhas. A de 08/09 fica preservada como registro do estado anterior. `PROCEDENCIA.md`
explica as duas e por quê. Os scripts sempre usam a captura mais recente, e o relatório de
concordância leva a data da captura no nome.

### 12.2 Contratos e pagamento

Contrato de uma página que serve também de recibo, gerado por
`data/codificacao_v05_respostas/contratos/gera_contrato.py` (pasta no `.gitignore`, tem CPF e
chave Pix). R$ 300 por pessoa, valor fechado, preso à entrega e não a resultado, do bolso do
pesquisador. **A: paga em 10/09**, contrato e comprovante enviados. **B: pendente**,
esperando os dados para o contrato e o Pix; há rascunho no Gmail pedindo isso.

### 12.3 Resultado (`analises/kappa_codificacao_v05.py`, relatório de 10/09)

Sem média de κ, por pré-registro. Três camadas:

| | funções | leitura |
|---|---|---|
| Confiável | FM01 κ=0,64; FM03 κ=0,57; MTL κ=0,72 | sustentam descrição quantitativa |
| Não estimável | FM02, FM04, FM06 | 1 a 5 ocorrências em 39; bruta 87–92%, PABAK 0,74–0,85, κ desaba |
| Ausente | FM05, FM08 | 0 de 39 nas duas |

FM07 é o caso à parte: κ=0,34 com A marcando 24 e B marcando 12.

**Falso positivo não converge e nenhuma taxa sai dele.** FP01, o maior denominador, dá κ=0,21.
Testado no nível da devolutiva, ignorando em qual função o FP foi registrado: κ=0,18, com A
sinalizando 13 e B 27. É diferença de severidade, não de arrumação. Só o piso é publicável: as
duas concordam em 11 das 39.

**RQ2:** as duas humanas concordam entre si em 0,72 e com a régua lexical em 0,28 e 0,43. A
régua credita 51,3% onde elas creditam 66,7% e 64,1%, ou seja, **subdetecta**. O juízo humano
passa a ser a medida da RQ2 e a régua vira piso.

### 12.4 O achado que organiza a §7 (`analises/divergencias_codificacao_v05.py`)

**31 dos 35 desacordos sobre FM são o mesmo trecho classificado em outra função**, por critério
objetivo (80% dos vocábulos da evidência mais curta contidos na mais longa). Só 4 são divergência
sobre a existência do movimento, e em 2 deles B registrou na hora não saber classificar.

Concentram-se em três fronteiras: FM03×FM07 (14), FM04×FM07 (5), FM02×FM06 (4). A dominante tem
mecanismo identificável e **replicou**: a rodada de julho já a tinha apontado, a v0.5 consertou a
fronteira vizinha adotando o critério ampliado de FM03, o conserto pegou (as duas registram FM03
em 30/39 cada) e a fronteira ao lado quebrou. Não se recalcula κ com as categorias fundidas.

### 12.5 Edições no `main.tex`

- **§7.5 reescrita**, agora com as duas codificadoras externas, e **Tabela 9** com prevalência de
  cada uma no lugar da dupla retirada.
- **§7.6 nova**, "Independent Double Coding by Two External Teachers", declarando a retirada do
  κ=0,14 com o motivo técnico, o desenho da rodada, o recrutamento, os quatro impedimentos, os
  perfis das duas e o regime de pagamento. **Tabela 10 nova**: κ, bruta, prevalência A e B,
  PABAK e banda, por FM01–08 e MTL.
- **Figura 2 refeita** (`fig_fm_v05.py` → `fm_modelo_v05.png`): intervalo entre as duas
  codificadoras em vez de barra única, marca partida onde coincidem, losango cinza para a
  referência dos especialistas.
- **§5** (validade de construto da régua) reescrita com os números novos e a admissão de que a
  régua subdetecta.
- **Abstract, conclusão e ameaças à validade** ajustados; `κ=0,14` e `κ=0,54` não existem mais
  no arquivo.
- **Declarations:** parágrafo de ética sobre as duas codificadoras, agradecimento, financiamento
  (honorários do bolso do primeiro autor) e material liberado. **CRediT corrigido**: a
  contribuição do Marcelo era descrita como cobrindo as duas rodadas e a validação da RQ2, o que
  deixou de ser verdade.

### 12.6 Response letter

`RESPOSTA_REVISORES_R1.md`, `.docx` e `.pdf`. Reescrita em quatro seções, objetiva, sem citar
arquivo interno nenhum. A lista final de itens pendentes de casamento com o texto verbatim dos
pareceres **foi removida a pedido**, e com ela saíram do documento oito mudanças reais desta
rodada (isolamento E3, contagem 80→100, reanálise por cenário da RQ2, abrandamento causal,
fronteira de generalização, quatro referências novas, DOIs, Tabela 5). Elas continuam no artigo
e vão precisar reaparecer quando os pareceres forem colados.

### 12.7 Defeitos de conversão corrigidos, que não eram de conteúdo

1. A nota da Tabela 10 saía como texto solto (`vspace4pt`, `beginminipagetextwidth`): o
   conversor não entende `minipage`. **O mesmo defeito estava nos arquivos enviados em julho.**
2. **O bloco "Ethics and consent" nunca apareceu no `.docx` nem no `.pdf`**: os conversores só
   processavam os cinco ambientes nomeados das Declarations. Corrigido em `tex_to_docx.py` e
   `tex_to_pdf.py`, que agora percorrem a seção em ordem de documento.
3. `md_to_docx.py` convertia por `textutil`, que **descarta a estrutura das tabelas** e inflava
   a fonte em 4/3. Passou a usar pandoc com documento de referência próprio
   (`paper/build_reference_docx.py` → `paper/reference.docx`): corpo Calibri 11pt justificado,
   tabela com grade cinza e cabeçalho sombreado.
4. `tex_to_docx.py` ganhou a mesma identidade visual, no lugar de Times sem justificação com
   títulos no azul do Word.

Ressalva: o `.docx` foi conferido no XML, não em tela, porque não há Word nem LibreOffice na
máquina. O `textutil` não serve de conferência, porque não lê estilo de parágrafo.

### 12.8 O que falta

1. **Dados da codificadora B**, para contrato e pagamento, e o perfil dela já entrou no artigo pelo
   formulário de inscrição.
2. ~~Os pareceres verbatim~~ **Chegaram em 11/09** (encaminhados da caixa da UFRGS); ver §13.
3. **Prazo**: prorrogação de 30 dias pedida em 08/09, nova data ~10/10/2026.
4. Depósito no Zenodo do material da R1: sai sozinho da release `v1.6.0` no GitHub (integração
   ativa desde a v1.2.0; as versões v1.2.0 a v1.5.0 estão no registro conceitual).

## 13. Pareceres em mãos, carta fechada, aval dos coautores (11/09/2026)

**Esta é a seção de retomada.**

- **Os coautores aprovaram.** Rosa (11/09, manhã): "as respostas estão boas". Marcelo (11/09,
  tarde): "Concordo com a Rosa", com a ressalva, correta, de que a nova rodada fortalece a
  resposta mas não garante aceitação. Os dois perguntaram se a revista exige página/linha das
  alterações: **não exige**. A carta de decisão pede "a detailed response letter outlining the
  changes made" e as diretrizes de submissão da JBCS não falam em linha numerada nem em versão
  marcada. A diretriz de DOI diz "unless when unavailable", o que cobre o Barbosa e Mauá (PROPOR
  2026, sem DOI na ACL Anthology).
- **Pareceres verbatim** em `PARECERES_R1_verbatim.md` (local, no `.gitignore`). Decisão de
  27/07/2026 assinada pelos Editors-in-Chief; *reply-to* Altigran Soares da Silva. Revisor A:
  "Revisions Required", seis pontos. Revisor C: "Resubmit for Review", dez pontos.
- **Response letter refeita ponto a ponto** (`RESPOSTA_REVISORES_R1.{md,docx,pdf}`): cada
  comentário citado verbatim, resposta e localização na versão revisada (A1–A6, C1–C10), mais os
  três ajustes não pedidos (independência do anotador, ética e material, Figura 2) e uma tabela de
  resumo. Todas as afirmações da carta foram conferidas no `main.tex` antes de escrever. Admite
  que o artigo ficou mais longo e oferece mover parte da §7.6 para apêndice se o editor preferir.
- **Checagem estática do `main.tex`**: nenhum `\ref` sem `\label`, nenhuma citação sem entrada,
  ambientes e chaves balanceados, `0.14` e `0.54` ausentes, "80 calls" ausente. Só
  `paulelder2007socratic` segue na bib sem citação (inócuo). Compilação real só no Overleaf: o
  template da JBCS não é baixável sem login e a classe não está na máquina.
- **Pacote para o Overleaf**: `overleaf_R1_2026-09-11.zip` (main.tex, references.bib,
  fm_frequencia.png, fm_modelo_v05.png; `.gitignore`). A revista compila em XeLaTeX.
- **Repositório**: os READMEs (EN e PT) ganharam a seção que mapeia o material de confiabilidade
  liberado e a contagem de 100 chamadas. Os `.xlsx` de `para_drive` foram commitados com o rótulo
  "guia v0.5", que é o que as codificadoras receberam em 02/09. Varredura de PII nos arquivos
  rastreados: limpa (nenhum nome, e-mail ou metadado de autor de codificadora). **Os nomes só
  existiam neste arquivo**, em três commits locais nunca enviados ao GitHub; foram removidos do
  texto, mas **o histórico local ainda os carrega** (commits `abc9e05`, `69912dc`, `bfdc04f`).
  Antes do push, reescrever esses commits ou esmagar os locais num só.
- **Sequência de envio**: (1) subir o zip no Overleaf e compilar, conferir Tabela 5, os DOIs dos
  oito `@misc` e as quatro referências novas; (2) limpar o histórico e dar push do branch;
  (3) merge em `main`, release `v1.6.0` (o Zenodo versiona sozinho); (4) submeter no OJS o PDF do
  Overleaf e a response letter em PDF.
