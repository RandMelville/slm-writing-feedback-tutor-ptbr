# O que subir para o Drive, e o que conferir depois

Estes três arquivos são **tudo** o que sai daqui para fora. Protocolo e Anexo de alinhamento são internos e não vão ao Drive compartilhado com codificadores.

| Arquivo | Destino |
|---|---|
| `GUIA_PROFESSOR_v05.pdf` | anexo do convite, um para cada codificador |
| `pacote_v05_codificador_A.xlsx` | importar como Google Sheets, compartilhar com **uma** pessoa |
| `pacote_v05_codificador_B.xlsx` | importar como Google Sheets, compartilhar com a **outra** |

## Importação

Subir cada `.xlsx` e usar **Abrir com → Planilhas Google**, o que cria uma cópia nativa. Compartilhar essa cópia, não o `.xlsx`.

Compartilhar como **Editor**, com uma pessoa por planilha, sem cópia entre elas. Desmarcar "Notificar pessoas" não é necessário, mas o link não deve ser público.

## Conferir depois de importar (4 checagens, 2 minutos)

A conversão do Excel para Planilhas Google não é perfeita. Antes de compartilhar, abrir a planilha convertida e verificar:

1. **Duas abas:** `LEIA-ME` e `Codificação`.
2. **Painéis congelados.** Rolar para a direita até a coluna `Evidência FM05`. O texto do aluno e a devolutiva precisam continuar visíveis à esquerda. Se não estiverem: Exibir → Congelar → 1 linha, e Exibir → Congelar → 3 colunas.
3. **Trava do falso positivo.** Numa linha qualquer, deixar `FM01` vazio ou em 0 e tentar digitar `1` em `FP01`. Tem que **recusar** o valor, não só avisar. Se aceitar, a validação virou aviso na conversão: Dados → Validação de dados, na coluna FP, mudar para "Rejeitar entrada".
4. **Colunas 0/1.** Tentar digitar `2` em `FM01`. Tem que recusar.

A checagem 3 é a que importa mais, porque é a regra que o Protocolo afirma na seção 3.0.

## Estrutura da planilha

37 colunas por linha, 39 linhas de dados (R01 a R39):

```
ID | Texto do aluno | Devolutiva
FM01 | Evidência FM01 | FP01 | Justificativa FP01
... (idem para FM02 a FM08)
MTL | Observações
```

As duas planilhas são idênticas em conteúdo e ordem. A correspondência entre codificadores é feita pelo `ID`, nunca pela posição da linha.

## Duas passadas

1ª: FM01 a FM08, com evidência de cada FM = 1 e o FP correspondente.
2ª: voltar ao início e preencher só MTL.
