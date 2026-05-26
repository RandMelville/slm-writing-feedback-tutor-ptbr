# A Diagnostic Evaluation of Small Language Models for Offline Socratic Tutoring in Brazilian Portuguese

[![paper](https://img.shields.io/badge/paper-preprint-blue)](paper/artigo_benchmark_slm.pdf)
[![python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org)
[![runtime](https://img.shields.io/badge/runtime-Ollama-purple)](https://ollama.com)
[![code license](https://img.shields.io/badge/code-MIT-green.svg)](LICENSE)
[![data license](https://img.shields.io/badge/data-CC--BY%204.0-green.svg)](LICENSE-DATA)
[![reproducible](https://img.shields.io/badge/runs-312%20%2B%2076-brightgreen)]()
[![inferential](https://img.shields.io/badge/stats-Fisher%20exact-orange)]()

> Diagnostic benchmark of 8 open Small Language Models (≤ 3.8 B parameters) for
> Socratic tutoring of writing in Brazilian Portuguese, evaluated strictly offline
> on CPU, against a metalinguistic rubric derived from Koch's Textual Linguistics.
> Includes a four-isolation falsification protocol that reclassifies the Llama 3.2
> family failure as a **reversible zero-shot bias** rather than compositional
> incapacity, supported by Fisher's exact tests on 2×2 conformance contingencies.

---

## Key findings

- **5 of 8 models** conform to the JSON output contract under zero-shot regime.
- The **Llama 3.2 family fails 78/78 zero-shot calls**, but recovers to **100 %
  conformance under one-shot in-context demonstration** (Fisher exact: *p* < 10⁻¹¹).
- Only one deployable model (≤ 3 B) combines structural conformance with latency
  below the 10 s HCI threshold: **`qwen2.5:3b-instruct`**.
- The conformant model still mobilizes Koch's metalinguistic terminology in only
  **46 % of scenarios**, evidencing a trade-off between structural and pedagogical
  competence that is independent of model size.

See the full preprint at [`paper/artigo_benchmark_slm.pdf`](paper/artigo_benchmark_slm.pdf).

---

## Reproduce in four commands

Requires Python 3.11+, [Ollama](https://ollama.com) installed locally, and ~8 GB of RAM
(plus disk space for model weights — about 30 GB for the full 8-model set).

```bash
# 1) Pull all eight models locally
ollama pull qwen2.5:1.5b-instruct qwen2.5:3b-instruct \
            llama3.2:1b llama3.2:3b \
            gemma2:2b gemma2:9b \
            llama3:8b phi3:mini

# 2) Install Python dependencies (only requests, pandas, matplotlib, scipy)
pip install -r requirements.txt

# 3) Run the main benchmark (8 models × 13 scenarios × 3 reps = 312 calls)
python src/benchmark_local.py

# 4) Reproduce the inferential analysis (Fisher exact on 7 contingencies)
python src/inferential_statistics.py
```

For the falsification protocol on the Llama 3.2 family (4 isolations, 80 calls):

```bash
python src/counter_experiment_llama32.py
```

---

## Repository layout

```
.
├── paper/                          # The article and PDF
│   ├── artigo_benchmark_slm.md
│   ├── artigo_benchmark_slm.pdf
│   ├── md_to_pdf.py                # PDF generator (reportlab)
│   └── references_inventory.txt    # Raw literature inventory
│
├── src/                            # All Python sources
│   ├── benchmark_local.py          # Main collection driver
│   ├── counter_experiment_llama32.py   # Falsification protocol (E1, E2, E2b)
│   ├── mine_benchmark.py           # Raw JSON → flat CSV extractor
│   ├── summarize_consolidated.py   # Aggregated table + figures
│   ├── generate_final_report.py    # Human-readable report
│   ├── inferential_statistics.py   # Fisher exact tests
│   └── prompts.py                  # Canonical SYSTEM_PROMPT (verbatim)
│
├── data/
│   ├── scenarios_canonical_koch.jsonl    # 13 canonical scenarios
│   ├── human_readable_report.txt         # English summary
│   └── results/
│       ├── round_1_main_models.json
│       ├── round_2_complementary_models.json
│       ├── counter_experiment_llama32.json
│       └── counter_experiment_llama32.log
│
└── analises/                       # Generated artifacts (figures, CSV, JSON)
    ├── benchmark_flat.csv
    ├── inferential_results.json
    ├── sumario_por_modelo.json
    ├── latencia_media.png
    └── throughput_tokens.png
```

---

## Methodology in one paragraph

Inference is conducted strictly locally and offline against an [Ollama](https://ollama.com)
server, over CPU with no GPU acceleration, in Q4_K_M quantization — emulating
the computational ceiling of typical Brazilian public-school computer labs.
Each model receives the same canonical SYSTEM_PROMPT and the same 13 canonical
scenarios drafted by a Textual Linguistics specialist. Conformance is decided
by a deterministic four-condition validator (`divergente()` in
[`src/mine_benchmark.py`](src/mine_benchmark.py)); categorical comparisons are
supported by Fisher's exact test. No grammar coercion, regex validation, or
constrained decoding is applied — only the model's native instruction-following
is measured. Full details are in Section 3 of the paper.

---

## A note on the SYSTEM_PROMPT identifier

The literal SYSTEM_PROMPT used across all 312 + 76 inference calls is preserved
verbatim in [`src/prompts.py`](src/prompts.py) for reproducibility. The prompt
opens with `"Você é o Bento..."` — *Bento* is the internal working identifier
of a future pedagogical fine-tuned model planned by the author, not part of the
public nomenclature of this benchmark. Renaming the prompt post-hoc would
invalidate reproducibility of the collected dataset, and a re-run would produce
a numerically different (though qualitatively identical) result. The choice
here, deliberate, is to preserve the historical artifact as it was.

---

## How to cite

If you use this benchmark, dataset, or methodology, please cite:

```bibtex
@article{rebocas2026benchmark,
  title   = {A Diagnostic Evaluation of Small Language Models for Offline
             Socratic Tutoring in Brazilian Portuguese: A Study on Structural
             and Pedagogical Adherence under Public-School Infrastructure Constraints},
  author  = {Reb{\'o}u{\c{c}}as, Randerson Melville},
  journal = {Preprint},
  year    = {2026},
  note    = {Available at: https://github.com/<USER>/<REPO>}
}
```

A machine-readable citation file is provided in [`CITATION.cff`](CITATION.cff).

---

## Licenses

- **Source code** (`src/`, `paper/md_to_pdf.py`): [MIT](LICENSE)
- **Article, dataset, figures** (`paper/`, `data/`, `analises/`): [CC-BY 4.0](LICENSE-DATA)

---

## Author

**Randerson Melville Rebouças**
Graduate Program in Informatics in Education (PPGIE)
Federal University of Rio Grande do Sul (UFRGS) — Brazil
`randerson.melville@gmail.com`

This work was conducted with institutional support from PPGIE/UFRGS and doctoral
funding from CAPES.
