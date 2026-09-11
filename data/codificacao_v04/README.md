# Pacote de codificação das Funções de Mediação

**Versão corrente: v0.5, congelada em 26 de agosto de 2026.**

Incorpora a revisão metodológica de Marcelo Magalhães Foohs de 25/08/2026, que separou presença da Função de Mediação (FM) de falso positivo associado (FP), e os quatro ajustes acordados por e-mail em 26/08/2026.

## O que vai a quem

| Arquivo | Quem recebe |
|---|---|
| `para_drive/GUIA_PROFESSOR_v05.pdf` | os dois codificadores, um anexo por pessoa |
| `para_drive/pacote_v05_codificador_A.xlsx` | codificador A, via Google Sheets |
| `para_drive/pacote_v05_codificador_B.xlsx` | codificador B, via Google Sheets |
| `PROTOCOLO_v05.{md,docx,pdf}` | **interno.** É o documento de método citado no artigo |
| `ANEXO_ALINHAMENTO_v05.{md,docx,pdf}` | **interno.** Treze exemplos resolvidos; funcionaria como gabarito |

Instruções de importação e as quatro checagens pós-conversão estão em `para_drive/LEIA_ANTES_DE_IMPORTAR.md`.

## Fonte e geração

O `.md` é a fonte. Os `.md` da v0.5 foram reconstruídos por pandoc a partir dos `.docx` revisados por Marcelo, preservados em `revisao_marcelo_2026-08-25/`.

```
.docx:  pandoc X.md -o X.docx --standalone --reference-doc=../../paper/referencia_tabelas.docx
        python3 ../../paper/docx_tabelas.py X.docx
.pdf:   python3 ../../paper/md_to_pdf.py X.md X.pdf
```

## Verificação de procedência dos exemplos

`verifica_exemplos.py` confere que nenhum exemplo do Protocolo, do Anexo ou do Guia sai das 39 devolutivas a codificar. Exigência do parecer de 10/08/2026.

Última execução, 26/08/2026: **103 trechos verificados, 16 com origem no corpus de devolutivas de professores (fonte permitida), 0 vindos das 39.** Registro em `verificacao_exemplos_2026-08-26.log`.

Rodar de novo a cada alteração nos três documentos:

```
python3 data/codificacao_v04/verifica_exemplos.py
```

## O que mudou da v0.4 para a v0.5

| | v0.4 | v0.5 |
|---|---|---|
| Decisões binárias por linha | 9 (FM01-08 + MTL) | 17 (FM01-08 + FP01-08 + MTL) |
| Colunas da planilha | 13 | 37, com evidência por FM e justificativa por FP |
| Movimento presente mas infundado | FM = 0 | FM = 1 e FP = 1 |
| MTL | objeto, com validade embutida | objeto puro; a inadequação vai para o FP |
| Derivada | — | VFM = 1 quando FM = 1 e FP = 0 |

A VFM é **mais estrita** que a régua de julho: segmento misto era 1 e agora produz VFM = 0. Comparações com a codificação de julho são exploratórias, e as medidas não são equivalentes (Protocolo §6).

## Análise da revisão

`revisao_marcelo_2026-08-25/ANALISE_REVISAO_MARCELO.md` traz os arquivos originais dele, o parecer sobre a mudança, os quatro ajustes, o desfecho e as duas ressalvas de escopo que ele fez e que precisam entrar na redação do artigo.

## Superado

`_superado_v04/` guarda o pacote v0.4 (protocolo, anexo de calibração, guia e os dois CSV). Preservado como percurso metodológico, não deve ser distribuído.
