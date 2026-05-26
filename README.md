# A Diagnostic Evaluation of Small Language Models for Offline Socratic Tutoring in Brazilian Portuguese: A Study on Structural and Pedagogical Adherence under Public-School Infrastructure Constraints

[![Paper](https://img.shields.io/badge/paper-PDF-blue)](paper/artigo_benchmark_slm.pdf)
[![Report](https://img.shields.io/badge/interactive-report-purple)](https://randmelville.github.io/slm-socratic-tutor-ptbr/report/)
[![Python](https://img.shields.io/badge/python-3.11+-blue)](https://www.python.org)
[![Code](https://img.shields.io/badge/code-MIT-green)](LICENSE)
[![Data](https://img.shields.io/badge/data-CC--BY%204.0-green)](LICENSE-DATA)

Diagnostic benchmark of eight open Small Language Models (≤ 3.8 B parameters)
for Socratic tutoring of writing in Brazilian Portuguese, executed strictly
offline on CPU. Includes a four-isolation falsification protocol on the
Llama 3.2 family, supported by Fisher's exact tests on 2×2 conformance
contingencies with Wilson 95 % confidence intervals.

Language: [English](README.md) · [Português](README.pt-br.md)

## Overview

Eight SLMs are evaluated against a metalinguistic rubric derived from Koch's
Textual Linguistics (Koch, 2018, 2020), through 312 inference calls
(8 models × 13 canonical scenarios × 3 repetitions) plus 76 additional calls
across four falsification isolations.

### Selected base model

**`qwen2.5:3b-instruct`** is the recommended base model for downstream
pedagogical fine-tuning. Among the eight evaluated, it is the **only deployable
model (≤ 3 B parameters) that simultaneously satisfies all non-functional
requirements**: 100 % structural conformance to the JSON output contract
under zero-shot regime (39/39 calls; Wilson 95 % CI [91.0 %; 100.0 %]),
mean latency of 2,906 ms — comfortably below the 10 s threshold for synchronous
classroom UX — and CV of 19.0 % indicating stable behavior across repetitions.
Fisher's exact test confirms that its conformance is statistically
indistinguishable from the 7–9 B reference-ceiling models (*p* = 1.000 n.s.),
strengthening its selection as the operationally preferable base.

### Three findings

1. Five of eight models conform to the JSON output contract under zero-shot
   regime; three (Llama 3.2 1B, Llama 3.2 3B, Phi-3 Mini) fail at 100 %.
2. The Llama 3.2 failure is a **reversible zero-shot bias**: a single
   one-shot demonstration restores conformance to 100 %
   (Fisher exact: *p* < 0.001), reclassifying the family as deployable
   under prompt-engineering at higher context cost.
3. Even the conformant `qwen2.5:3b-instruct` mobilizes Koch's metalinguistic
   terminology in only 46.2 % of scenarios (Wilson 95 % CI [23.2 %; 70.9 %]),
   evidencing that structural conformance and pedagogical adequacy are
   logically independent dimensions.

Full methodology, tables, and references are in
[`paper/artigo_benchmark_slm.pdf`](paper/artigo_benchmark_slm.pdf) (also
available as [`DOCX`](paper/artigo_benchmark_slm.docx) and
[`Markdown`](paper/artigo_benchmark_slm.md)). An
[interactive HTML report](https://randmelville.github.io/slm-socratic-tutor-ptbr/report/)
is also available with the per-model results and the falsification protocol
in browsable form.

## Requirements

- Python 3.11 or later
- [Ollama](https://ollama.com) running locally
- ~ 8 GB RAM and ~ 30 GB free disk for the eight quantized model weights

## Installation

```bash
git clone https://github.com/RandMelville/slm-socratic-tutor-ptbr.git
cd slm-socratic-tutor-ptbr
pip install -r requirements.txt
```

## Reproduction

```bash
# Pull the eight evaluated models locally
ollama pull qwen2.5:1.5b-instruct qwen2.5:3b-instruct \
            llama3.2:1b llama3.2:3b \
            gemma2:2b gemma2:9b llama3:8b phi3:mini

# Main benchmark — 8 models × 13 scenarios × 3 repetitions = 312 calls
python src/benchmark_local.py

# Falsification protocol on the Llama 3.2 family — 4 isolations, 80 calls
python src/counter_experiment_llama32.py

# Fisher's exact tests and Wilson 95 % CIs
python src/inferential_statistics.py
```

## Repository structure

```
paper/      Article (Markdown, PDF, DOCX) and reference inventory
src/        Reproducible scripts (benchmark, validator, statistics)
data/       Canonical scenarios + raw inference results
analises/   Generated artifacts (CSV, JSON, figures)
report/     Self-contained interactive HTML report
```

## Citation

```bibtex
@article{reboucas2026slmsocratic,
  title   = {A Diagnostic Evaluation of Small Language Models for Offline
             Socratic Tutoring in Brazilian Portuguese: A Study on Structural
             and Pedagogical Adherence under Public-School Infrastructure
             Constraints},
  author  = {Reb{\'o}u{\c{c}}as, Randerson Oliveira Melville and Foohs, Marcelo Magalh{\~a}es},
  year    = {2026},
  note    = {Available at https://github.com/RandMelville/slm-socratic-tutor-ptbr}
}
```

A machine-readable citation file is provided in [`CITATION.cff`](CITATION.cff).

## License

Source code is released under the [MIT License](LICENSE). The article,
dataset, generated artifacts, and interactive report are released under
[Creative Commons Attribution 4.0 International (CC-BY 4.0)](LICENSE-DATA).

## Authors

**Randerson Oliveira Melville Rebouças** — `randerson.melville@gmail.com`
**Marcelo Magalhães Foohs** — `mmfoohs@gmail.com`

Graduate Program in Informatics in Education (PPGIE), Federal University of
Rio Grande do Sul (UFRGS), Porto Alegre, Brazil.

Co-advisor: Profa. Dra. Rosa Maria Vicari (PPGIE/UFRGS).

This work was conducted with institutional support from PPGIE/UFRGS.
