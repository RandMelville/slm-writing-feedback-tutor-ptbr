# Procedência das duas codificações v0.5

Registro exigido pelo Protocolo v0.5, seção 5, item 6: *"preservar separadamente os dois
arquivos datados antes de qualquer confronto"*.

Os arquivos desta pasta são o **registro original** das duas codificações. Não são editados
depois de capturados, nem para normalizar célula vazia em zero. Toda normalização acontece em
memória, no script de análise.

## Origem

| Arquivo | Planilha no Drive | ID do arquivo | Última modificação pela codificadora |
|---|---|---|---|
| `codificacao_A_2026-09-08.xlsx` | `pacote_v05_codificador_A` | `1D0VmmRypsvmP6E-_ztq0n6z7SulN-sSfipIEi7KAPHs` | 2026-09-04 20:51:34 UTC |
| `codificacao_B_2026-09-08.xlsx` | `pacote_v05_codificador_B` | `1MDqaPGQqE4bZEKvR1pI-VVEbhTulrfeh2NAnGNqxInY` | 2026-09-08 00:50:26 UTC |
| `codificacao_A_2026-09-10.xlsx` | `pacote_v05_codificador_A` | `1D0VmmRypsvmP6E-_ztq0n6z7SulN-sSfipIEi7KAPHs` | 2026-09-08 23:27:17 UTC |
| `codificacao_B_2026-09-10.xlsx` | `pacote_v05_codificador_B` | `1MDqaPGQqE4bZEKvR1pI-VVEbhTulrfeh2NAnGNqxInY` | 2026-09-09 12:32:16 UTC |

Ambas as planilhas foram criadas a partir de `data/codificacao_v04/para_drive/pacote_v05_codificador_{A,B}.xlsx`
(pacote v0.5, congelado em 26/08/2026) e compartilhadas em 02/09/2026, uma por pessoa,
sem acesso cruzado. A correspondência entre codificadoras é feita pelo `ID`, nunca pela
posição da linha.

## Duas capturas, e qual delas vale

**A captura de 08/09/2026 não é a codificação final.** A auditoria daquele dia encontrou uma
célula vazia em A (`FP08/R23`) e, em B, três FM vazias, um MTL vazio, uma evidência faltante e
282 células de FP em branco. Cada codificadora foi consultada por escrito sobre as suas
pendências, sem que nenhuma classificação alheia lhe fosse revelada e sem pedido de revisão de
julgamento. As duas responderam editando a própria planilha no Drive, em 08 e 09/09.

**A captura de 10/09/2026 é a que entra na análise de concordância.** Ela passa na auditoria sem
nenhuma célula vazia, nenhum valor fora de `{0, 1}` e nenhuma violação da regra 3.0 nas duas
planilhas. A codificadora B confirmou por e-mail, em 09/09, a convenção que estava por trás dos
brancos: *"Eram realmente 0, entendi que FP eu apenas preencheria quando 1. Mas já consertei,
colocando zero nas faltantes."* Os zeros passaram a estar escritos na planilha, então nenhuma
suposição de preenchimento entra no cálculo.

A captura de 08/09 fica preservada nesta pasta como registro do estado anterior, não como dado
descartado. `analises/audita_codificacao_v05.py` e `analises/kappa_codificacao_v05.py` usam
sempre a captura mais recente de cada codificadora, e o relatório de concordância é gravado com
a data da captura no nome do arquivo.

## Como capturar de novo

Na planilha aberta no Drive: `Arquivo > Baixar > Microsoft Excel (.xlsx)`, e salvar aqui com o
nome `codificacao_<A|B>_<AAAA-MM-DD>.xlsx`. O download direto por URL de export e o download
por automação de navegador não funcionam neste ambiente.

## Verificação

```
python3 analises/audita_codificacao_v05.py
```

Relatório em `analises/auditoria_codificacao_v05.txt`.
