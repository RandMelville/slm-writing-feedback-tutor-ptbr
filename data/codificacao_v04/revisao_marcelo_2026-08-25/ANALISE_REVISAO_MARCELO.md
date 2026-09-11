# Revisão de Marcelo ao pacote de codificação v0.4

**Data do parecer:** 25 de agosto de 2026, 12h15 (e-mail "Documentos revisados")
**Analisado em:** 25 de agosto de 2026
**Situação da coautoria:** Rosa comunicou na manhã de 25/08 que está fora desta etapa (cirurgia de familiar, cerca de 3 semanas de recuperação). Marcelo respondeu que ele e Randerson seguem sozinhos nos dois artigos. **Há um parecer, não dois.**

## Arquivos recebidos (nesta pasta)

| Arquivo | Corresponde a |
|---|---|
| `01_PROTOCOLO_revisao_Marcelo.docx` | `PROTOCOLO_v04.docx` |
| `02_ANEXO_ALINHAMENTO_revisao_Marcelo.docx` | `ANEXO_CALIBRACAO.docx` (renomeado) |
| `03_GUIA_PROFESSOR_revisao_Marcelo.docx` | `GUIA_PROFESSOR.docx` |
| `04_Planilha_A_revisao_Marcelo.xlsx` | `pacote_v04_codificador_A.csv` |
| `05_Planilha_B_revisao_Marcelo.xlsx` | `pacote_v04_codificador_B.csv` |

Nada foi congelado. A seção 9 do protocolo revisado registra as duas manifestações como pendentes.

## A mudança

É uma só, e ela reorganiza o resto: **separar presença da FM de validade da FM.**

Na v0.4, a regra "parece, mas não é" (§3.0) mandava marcar 0 quando o movimento estava presente na forma mas se apoiava em leitura errada do texto do aluno. Elogio que trata a repetição de "e daí" como variedade de conectivos: FM01 = 0.

Na revisão, o mesmo caso vira **FM01 = 1 e FP01 = 1**. A presença fica numa coluna, a inadequação em outra.

### Efeitos

| | v0.4 (congelada em 22/08) | Revisão Marcelo |
|---|---|---|
| Decisões binárias por linha | 9 (FM01-08 + MTL) | **17** (FM01-08 + FP01-08 + MTL) |
| Colunas da planilha | 13 | **37** (evidência textual por FM, justificativa por FP) |
| MTL | objeto, com a validade embutida na regra geral | objeto puro; inadequação vai para o FP |
| Passadas | 2 (FM, depois MTL) | 2 (FM + evidência + FP, depois MTL) |
| Codificação nº 4 (Marcelo, julho) | fora do κ | fora do κ e explicitamente incomparável (§1.5) |
| Variável derivada | — | **VFM** = 1 quando FM = 1 e FP = 0 |
| Anexo | "de calibração" | "de alinhamento conceitual dos autores", 13 exemplos com vetor `FM \| FP \| MTL` |

### Plano de análise (§6 revisada)

- κ de Cohen e concordância bruta por FM e para MTL, sempre com as prevalências.
- FP: frequência por codificador e concordância bruta no subconjunto em que ao menos um codificador marcou FM = 1; κ só quando houver variação suficiente, com o denominador explicitado.
- PABAK como complemento em categorias raras ou saturadas, nunca em substituição ao κ.
- Reportar separadamente FM (presença formal), FP (falso positivo) e VFM (realização sem FP identificado), sem tratar os três como equivalentes.
- MTL de cada codificador confrontada com a régua lexical de `src/metalinguistic_adherence.py` (validade de construto da RQ2).
- Nenhum κ médio como critério único de decisão.

### Planilhas

Duas abas (LEIA-ME + Codificação). Validação de dados 0/1 nas 17 colunas binárias, realce condicional em todas, e regra de expressão que destaca `FP = 1` com `FM <> 1`. A e B seguem idênticas, R01–R39 na mesma ordem, sem embaralhamento.

## Parecer: aceitar

**1. Ele consertou a causa provável do κ = 0,14.** A regra antiga pedia duas decisões distintas dentro de uma coluna só: "o movimento está aqui?" e "o movimento se sustenta?". A primeira é quase objetiva, a segunda é interpretativa. Forçando as duas num binário, a variância da segunda contamina a primeira. Separadas, o κ das FMs deve subir, e é exatamente isso que o parecerista do JBCS pediu.

**2. O FP é um resultado melhor do que o que havia.** "O modelo produz a pergunta reflexiva, mas em X% dos casos a pergunta se apoia em premissa que não existe no texto do aluno" é um achado específico e publicável sobre SLMs ≤3B. A formulação antiga apagava esse achado dentro de um zero.

**3. Nada se perde.** O VFM reconstrói a leitura antiga como variável derivada. O esquema novo é estritamente mais informativo que o v0.4.

**Custo medido, não estimado:** na codificação nº 4 a média foi **2,77 FMs marcadas por devolutiva** (108 marcações em 39 linhas). Isso dá cerca de 108 colagens de evidência por codificador, mais as justificativas de FP, que são poucas. É trabalho a mais, mas a evidência é copiar e colar, não julgar. Não dobra o tempo.

## Quatro ajustes antes de congelar

1. **§3.0 afirma o que a planilha não faz.** O texto diz que `FM = 0` com `FP = 1` é "combinação inválida e proibida pela planilha". Na planilha é apenas realce condicional; a validação de dados aceita o valor. Ou trocar a validação por fórmula (`AND(OR(F2=0;F2=1);NÃO(E(F2=1;D2<>1)))`), ou corrigir a frase para "sinalizada". Como está, o protocolo promete uma trava inexistente.

2. **Congelar painéis em A:C.** São 37 colunas, com "Texto do aluno" em largura 58 e "Devolutiva" em 68. Ao chegar na evidência da FM05, o codificador perdeu de vista a devolutiva que está codificando. Correção de um minuto que evita erro de linha.

3. **VFM não é a régua antiga.** Na v0.4, segmento misto (um trecho vale, outro não) ficava 1. Na revisão vira FM = 1 e FP = 1, logo VFM = 0. VFM é portanto **mais estrito** que a "FM válida" de julho. Precisa estar dito no protocolo, senão alguém compara VFM com a codificação nº 4 supondo que é a mesma régua.

4. **Rodar `verifica_exemplos.py` sobre os textos novos.** Anexo e guia mudaram os exemplos, e o protocolo continua afirmando que a procedência é verificada por programa. O script aponta hoje para os `.md` antigos. Antes de congelar: reconstruir os três `.md` a partir dos `.docx` revisados e rodar de novo.

## Prazo

Prazo do JBCS: 10/09/2026. Restam 16 dias em 25/08.

Sequência: congelar com os quatro ajustes (2-3 dias) → fechar os dois codificadores (chamada do LinkedIn enviada a Marcelo em 25/08, sem inscritos confirmados) → codificação (cerca de 1 semana) → κ → reescrita de §7 e Tabela 9.

Cabe, sem folga. **Se em 5 dias não houver dois codificadores confirmados, o plano B precisa estar decidido antes, não depois.**

## Pendente

Segundo pacote de Marcelo, 25/08 às 17h09: quatro documentos reconstruídos da RSL (protocolo, strings de busca, verificação diagnóstica, nota de transparência). Analisado separadamente em `~/Documents/doutorado/rsl/`.

---

## Desfecho: aprovado em 26/08/2026

Resposta enviada a Marcelo em 26/08 às 00h15, com os quatro ajustes. Ele respondeu às 11h23 concordando com os quatro, e decidindo o que estava em aberto no primeiro:

1. **Validação da planilha:** prefere que a planilha **impeça** de fato a combinação `FM = 0` com `FP = 1`, mantendo a redação do Protocolo. Ou seja, muda o instrumento, não o texto.
2. **Congelar** a linha de cabeçalho e as colunas A a C nas duas planilhas.
3. **Incluir no Protocolo** que a VFM é medida derivada mais estrita do que a de julho, que em segmentos mistos a codificação anterior permanecia em 1 enquanto a VFM será 0, e que qualquer comparação será exploratória, reconhecendo que as medidas não são equivalentes.
4. **Executar o `verifica_exemplos.py`** sobre os textos exatos do Guia, do Anexo e do Protocolo que integram o conjunto final, atualizando o script para esses arquivos e preservando o registro.

### Duas correções de escopo que ele fez, e que procedem

> "A separação entre FM e FP permite testar empiricamente se a baixa concordância anterior decorria da mistura entre presença e sustentação do movimento. Entretanto, **não devemos antecipar que o κ das FMs necessariamente subirá**; isso será determinado pelas duas novas codificações."

> "A frequência de FP poderá constituir um resultado relevante **sobre o modelo e as condições avaliadas neste estudo**. A generalização para modelos pequenos em geral dependeria de evidência mais ampla."

As duas atingem afirmações desta análise e do e-mail enviado. A separação é uma **hipótese a testar**, não um resultado previsto, e o achado de FP é sobre `qwen2.5:3b-instruct` nas 39 devolutivas, não sobre SLMs ≤3B em geral. Ajustar a redação do artigo de acordo.

## Execução dos quatro ajustes, 26/08/2026

Feita. Artefatos em `data/codificacao_v04/`, sufixo `_v05`:

| Item | O que foi feito | Verificação |
|---|---|---|
| 1 | Validação de dados das oito colunas FP trocada de lista para fórmula: `AND(OR(F2=0,F2=1),NOT(AND(F2=1,D2<>1)))`, com mensagem de erro nomeando o par | 8 validações `custom` e 9 `list` (8 FM + MTL) em cada planilha |
| 2 | Painéis congelados em `D2`, ou seja, cabeçalho mais colunas A a C | `freeze_panes = D2` nas duas |
| 3 | Parágrafo novo na seção 6 do Protocolo, mais a seção 1.4.1 registrando os quatro ajustes | `PROTOCOLO_v05.md` linhas 74 e 237 |
| 4 | `verifica_exemplos.py` apontado para os três arquivos `_v05` e reexecutado | 103 trechos, 16 do corpus humano (permitido), **0 das 39**, saída 0. Registro em `verificacao_exemplos_2026-08-26.log` |

Os `.md` foram reconstruídos a partir dos `.docx` revisados por Marcelo (via pandoc), porque o repositório mantém o `.md` como fonte e o `verifica_exemplos.py` lê `.md`. Os `.docx` e o PDF do Guia foram regerados a partir deles.

O Protocolo passou de "minuta para aprovação" a **versão 0.5 congelada**, com a seção 9 registrando as duas manifestações de 26/08 e a de Rosa como não solicitada nesta etapa.

**Aos codificadores vai apenas `GUIA_PROFESSOR_v05.pdf` e a planilha individual.** Protocolo e Anexo seguem internos.

### Bug corrigido de passagem em `paper/md_to_pdf.py`

Ao gerar o PDF do Guia, o script travou em laço infinito. Causa: o acumulador de parágrafo em `build()` para de acumular ao encontrar uma linha iniciada por `---`, mas nenhum ramo anterior consome essa linha, então `i` nunca avança. Régua horizontal nunca havia aparecido nos `.md` escritos à mão; ela entra agora porque os `.md` do pacote vêm de conversão do `.docx` pelo pandoc, que emite `---` para linha horizontal.

Corrigido com um ramo explícito que trata `---`, `***` e `___` como `HRFlowable` e avança `i`. `paper/artigo_benchmark_slm.md` foi regerado sem regressão.
