# bento_train_data/

Dados de treino para o LoRA do Bento via MLX-LM.

## Estado atual (2026-05-22)

- `train.jsonl` — 13 cenários padrão-ouro (mesmos do `../bento8b_dataset_final.jsonl`).
- `valid.jsonl` — **intencionalmente vazio**.

## Por que valid.jsonl está vazio

Anteriormente `valid.jsonl` era cópia byte-a-byte de `train.jsonl` — vazamento de dados clássico: a loss de validação reportada pelo MLX-LM não mede generalização, mede memorização. Isso silenciosamente invalida qualquer comparação entre rodadas de FT.

Com apenas 13 seeds, qualquer split holdout (ex.: 10 train + 3 valid) também seria estatisticamente inútil — 3 amostras não dão sinal de generalização, e perderíamos ~23% do já-pequeno conjunto de treino.

Solução temporária: deixar `valid.jsonl` vazio e rodar MLX-LM com `--val-batches 0` (sem validação automática) até termos dataset expandido. O smoke test atual em `../adapters/` foi feito sem val real na prática — não há perda.

## Quando esse arquivo voltará a ter conteúdo

Quando o dataset for expandido (Track D do plano em `~/.claude/plans/`) para 200+ exemplos, o split estratificado em `../data_pipeline/06_final_splits/` substituirá este diretório como fonte canônica de treino. Aí `valid.jsonl` terá dados disjuntos de `train.jsonl`, estratificados por `foco_koch`.

**Antes da expansão**: NÃO reativar `valid.jsonl` com cópia de `train.jsonl` — isso reintroduz o vazamento que estamos corrigindo.

## Conceito aprendido aqui

*Data leakage* entre train e valid é um dos erros mais comuns e mais silenciosos em ML aplicado. A loss baixa mente — o modelo está sendo testado nos mesmos exemplos que viu no treino. O sintoma típico é "loss de valid empata com loss de train e cai junto" em vez de divergir. Sempre que valid e train tiverem origem suspeita, rodar `diff` (ou hash) antes de confiar nas métricas.
