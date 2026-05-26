# Avaliação Diagnóstica de Modelos de Linguagem de Pequeno Porte para Tutoria Socrática Offline em Língua Portuguesa: um Estudo de Aderência Estrutural e Pedagógica sob Restrições de Infraestrutura Escolar Pública

[![Paper](https://img.shields.io/badge/paper-PDF-blue)](paper/artigo_benchmark_slm.pdf)
[![Relatório](https://img.shields.io/badge/relat%C3%B3rio-interativo-purple)](https://randmelville.github.io/slm-socratic-tutor-ptbr/report/)
[![Python](https://img.shields.io/badge/python-3.11+-blue)](https://www.python.org)
[![Código](https://img.shields.io/badge/c%C3%B3digo-MIT-green)](LICENSE)
[![Dados](https://img.shields.io/badge/dados-CC--BY%204.0-green)](LICENSE-DATA)

Benchmark diagnóstico de oito Modelos de Linguagem de Pequeno Porte abertos
(≤ 3,8 B parâmetros) para tutoria socrática de escrita em Português do Brasil,
executados estritamente offline em CPU. Inclui protocolo de falsificação em
quatro isolamentos sobre a família Llama 3.2, com suporte de testes exatos
de Fisher em contingências 2×2 e intervalos de confiança de Wilson 95 %.

Idioma: [English](README.md) · [Português](README.pt-br.md)

## Visão geral

Oito SLMs são avaliados contra uma rubrica metalinguística derivada da
Linguística Textual de Koch (Koch, 2018, 2020), por meio de 312 chamadas
de inferência (8 modelos × 13 cenários canônicos × 3 repetições) e 76
chamadas adicionais distribuídas em quatro isolamentos de falsificação.

Três achados:

1. Cinco dos oito modelos respeitam o contrato JSON em regime zero-shot;
   três (Llama 3.2 1B, Llama 3.2 3B, Phi-3 Mini) falham em 100 %.
2. A falha da família Llama 3.2 é **viés zero-shot reversível**: uma única
   demonstração one-shot restaura a conformidade para 100 %
   (Fisher exato: *p* < 0,001).
3. Entre os modelos deployáveis, apenas o `qwen2.5:3b-instruct` combina
   conformidade estrutural com latência abaixo do limiar de 10 s da IHC.

Metodologia, tabelas e referências completas em
[`paper/artigo_benchmark_slm.pdf`](paper/artigo_benchmark_slm.pdf) (também
disponível em [`DOCX`](paper/artigo_benchmark_slm.docx) e
[`Markdown`](paper/artigo_benchmark_slm.md)). Um
[relatório HTML interativo](https://randmelville.github.io/slm-socratic-tutor-ptbr/report/)
também está disponível, com os resultados por modelo e o protocolo de
falsificação em formato navegável.

## Requisitos

- Python 3.11 ou superior
- [Ollama](https://ollama.com) executando localmente
- ~ 8 GB de RAM e ~ 30 GB de disco livre para os oito modelos quantizados

## Instalação

```bash
git clone https://github.com/RandMelville/slm-socratic-tutor-ptbr.git
cd slm-socratic-tutor-ptbr
pip install -r requirements.txt
```

## Reprodução

```bash
# Baixa os oito modelos avaliados localmente
ollama pull qwen2.5:1.5b-instruct qwen2.5:3b-instruct \
            llama3.2:1b llama3.2:3b \
            gemma2:2b gemma2:9b llama3:8b phi3:mini

# Benchmark principal — 8 modelos × 13 cenários × 3 repetições = 312 chamadas
python src/benchmark_local.py

# Protocolo de falsificação para a família Llama 3.2 — 4 isolamentos, 80 chamadas
python src/counter_experiment_llama32.py

# Testes exatos de Fisher e IC Wilson 95 %
python src/inferential_statistics.py
```

## Estrutura do repositório

```
paper/      Artigo (Markdown, PDF, DOCX) e inventário de referências
src/        Scripts reprodutíveis (benchmark, validador, estatística)
data/       Cenários canônicos + resultados brutos de inferência
analises/   Artefatos gerados (CSV, JSON, figuras)
report/     Relatório HTML interativo auto-contido
```

## Como citar

```bibtex
@article{reboucas2026slmsocratic,
  title   = {A Diagnostic Evaluation of Small Language Models for Offline
             Socratic Tutoring in Brazilian Portuguese: A Study on Structural
             and Pedagogical Adherence under Public-School Infrastructure
             Constraints},
  author  = {Reb{\'o}u{\c{c}}as, Randerson Oliveira Melville and Foohs, Marcelo Magalh{\~a}es},
  year    = {2026},
  note    = {Disponível em https://github.com/RandMelville/slm-socratic-tutor-ptbr}
}
```

Um arquivo de citação legível por máquina está disponível em
[`CITATION.cff`](CITATION.cff).

## Licenças

O código-fonte é distribuído sob a [Licença MIT](LICENSE). O artigo, dataset,
artefatos gerados e relatório interativo são distribuídos sob
[Creative Commons Attribution 4.0 International (CC-BY 4.0)](LICENSE-DATA).

## Autores

**Randerson Oliveira Melville Rebouças** — `randerson.melville@gmail.com`
**Marcelo Magalhães Foohs** — `mmfoohs@gmail.com`

Programa de Pós-Graduação em Informática na Educação (PPGIE), Universidade
Federal do Rio Grande do Sul (UFRGS), Porto Alegre, Brasil.

Coorientadora: Profa. Dra. Rosa Maria Vicari (PPGIE/UFRGS).

Este trabalho foi conduzido com apoio institucional do PPGIE/UFRGS.
