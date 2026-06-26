# A Diagnostic Evaluation of Small Language Models for Offline Socratic Tutoring in Brazilian Portuguese: A Study on Structural and Pedagogical Adherence under Public-School Infrastructure Constraints

---

**Randerson Oliveira Melville Rebouças**
Graduate Program in Informatics in Education (PPGIE)
Federal University of Rio Grande do Sul (UFRGS) — Porto Alegre, RS, Brazil
`randerson.melville@gmail.com`

**Marcelo Magalhães Foohs**
Graduate Program in Informatics in Education (PPGIE)
Federal University of Rio Grande do Sul (UFRGS) — Porto Alegre, RS, Brazil
`mmfoohs@gmail.com`

**Rosa Maria Vicari**
Graduate Program in Informatics in Education (PPGIE)
Federal University of Rio Grande do Sul (UFRGS) — Porto Alegre, RS, Brazil

DOI: [10.5281/zenodo.20388846](https://doi.org/10.5281/zenodo.20388846)
Code and data: [github.com/RandMelville/slm-socratic-tutor-ptbr](https://github.com/RandMelville/slm-socratic-tutor-ptbr)

---

## Abstract

The adoption of generative Artificial Intelligence in educational contexts has been predominantly anchored in proprietary models dependent on broadband connectivity, an assumption incompatible with the material reality of most Brazilian public schools. This work conducts a controlled diagnostic evaluation of eight open Small Language Models (SLMs), executed strictly in a local, offline environment, against a metalinguistic rubric derived from Ingedore Koch's Textual Linguistics. A total of 312 primary inference calls were performed (8 models × 13 canonical scenarios × 3 repetitions) without applying any external grammatical coercion mechanism, plus 80 additional calls across four falsification isolations directed at the most expressive architectural finding. Categorical comparisons are supported by Fisher's exact test (with odds ratio and 95 % CI). Results reveal two distinct failure regimes: (i) **zero-shot structural non-adherence**, manifested as 100 % typological divergence in the Llama 3.2 family (1 B and 3 B) and Phi-3 Mini — characterized, for the Llama 3.2 family, as a deterministic formatting bias inherited from instruction tuning for generalist commercial use, fully reversible by minimal in-context demonstration (*one-shot*), which distinguishes it from compositional incapacity of the model; and (ii) **pedagogical superficiality**, observed in Qwen 2.5 3B-Instruct — the only structurally conformant model in the deployable range under zero-shot — whose responses mobilize Koch's rubric terminology in only 46 % of scenarios. We conclude that contemporary off-the-shelf generalist models are insufficient for fine-grained Socratic tutoring in Brazilian Portuguese under zero-shot regime, justifying the development of specialized models through supervised fine-tuning on curated pedagogical corpora.

**Keywords:** Language Models; Basic Education; Brazilian Portuguese; Local Inference; Textual Linguistics; Diagnostic Evaluation.

---

## 1. Introduction

The incorporation of Large Language Models (LLMs) into educational contexts has constituted, over the past three years, one of the fastest-growing research fronts in Computers and Education. The specialized literature documents promising results in the use of proprietary models such as GPT-4, Claude, and Gemini for conversational tutoring, automated essay scoring, and formative *feedback* generation (Kasneci et al., 2023; Tlili et al., 2023). This production, however, has been predominantly anchored in infrastructural assumptions — stable broadband access, no budget restriction for Application Programming Interface (API) calls, and contractual stability of foreign vendors — that **do not correspond to the material reality of most of the Brazilian public-school network**.

The historical TIC Educação series, conducted by the Regional Center for Studies on the Development of the Information Society (CGI.br/NIC.br/Cetic.br, 2025), evidences the persistence of profound connectivity inequalities in Brazilian public schools. Although the 2024 edition of the survey reports that 96 % of Brazilian schools now have internet access, effective student use remains deeply unequal: while 67 % of students in state schools use the internet for pedagogical activities assigned by teachers, in municipal schools that proportion falls to only 27 % — confirming that institutional connectivity does not translate into effective pedagogical access at the student level. To this structural limit is added the issue of **student-data sovereignty**: the routine transmission of textual productions by underage students to commercial servers located in foreign jurisdictions configures a gray zone under the Brazilian General Data Protection Law (Brasil, 2018), particularly at its interface with the Brazilian Statute for Children and Adolescents in Digital Environments (Brasil, 2025).

This double encirclement — material connectivity precariousness and legal-ethical fragility of sensitive data traffic — imposes that the adoption of generative AI in the Brazilian public school contemplate, as an inescapable non-functional requirement, the **strictly local and offline** execution of inference models. The technical window for such an approach was opened by the recent proliferation of Small Language Models (SLMs) in the 1- to 4-billion parameter range, made viable by aggressive quantization (Q4, Q5) and by lightweight *runtimes* capable of executing inference over CPU on modest machines, without dependence on dedicated graphics acceleration (Abdin et al., 2024; Yang et al., 2024).

Recent literature on SLMs concentrates predominantly on general-purpose *benchmarks*, in English, and directed at mathematical reasoning or code generation tasks. It remains open, however, whether **open off-the-shelf models, executed locally under simulated public-school infrastructure conditions, are natively capable of operating as Socratic tutors of writing in Brazilian Portuguese**, respecting structured-output contracts and non-prescriptivist pedagogical principles. The present study addresses this gap through a controlled diagnostic evaluation of eight off-the-shelf SLMs against a rubric derived from the Textual Linguistics of Ingedore Koch (Koch, 2018; Koch, 2020), under a rigorously local inference environment and without any external grammatical coercion mechanism.

This work is guided by two related but distinct research questions — one structural-quantitative, the other pedagogical-qualitative:

- **RQ1.** To what extent do contemporary open SLMs, executed locally in an offline environment, adhere to the structural output contract declared in natural language?
- **RQ2.** Among the structurally conformant models, to what extent do their responses mobilize Koch's metalinguistic rubric beyond the thematic-surface layer?

The article is organized as follows: Section 2 reviews the relevant state of the art; Section 3 details the experimental methodology adopted, with a level of description sufficient for integral reproducibility of the study; Section 4 reports computational efficiency; Section 5 presents structural conformance, addressing **RQ1**; Section 6 conducts a qualitative analysis of pedagogical adherence in the best-classified model, addressing **RQ2**; and Section 7 synthesizes conclusions and outlines the subsequent agenda, returning explicitly to each research question.

## 2. Related Work

Systematic evaluation of language models for educational tasks articulates across three research fronts relevant to the present study. The first front comprises studies on the use of proprietary LLMs as tutors and formative evaluators. Kasneci et al. (2023) synthesize opportunities and challenges of ChatGPT in basic education, identifying significant potential but warning against systemic biases and infrastructural dependence. Tlili et al. (2023) conduct a longitudinal case study on the pedagogical use of *chatbots*, highlighting tensions between student engagement and conceptual fidelity. This literature, however, operates predominantly under an assumption of continuous connectivity — a gap the present work addresses directly.

The second front corresponds to technical literature on SLMs viable for local execution. Abdin et al. (2024), describing Phi-3, posit the thesis of "small and capable models" through intensive training-data curation; Yang et al. (2024) present the Qwen 2.5 family, with emphasis on multilingualism; Grattafiori et al. (2024) and the Gemma team (Gemma Team, 2024) describe, respectively, the Llama 3 and Gemma 2 families in their lightweight variants. These references configure the candidate universe of the present *benchmark*, but their technical reports evaluate performance predominantly on Anglocentric *benchmarks* and mathematical tasks, with no specific coverage of pedagogical tutoring in Brazilian Portuguese.

The third front involves the emerging literature on **format bias** in models post-trained by preference. Zheng et al. (2023) and Wu and Aji (2023) demonstrate that human and model-judge evaluators exhibit systematic preference for long, listed, and well-formatted responses regardless of content quality, and that this reward signal becomes internalized in finalized models as a dominant attractor in the generation space. This theoretical body is mobilized, in Section 5, for the interpretation of the architectural findings of this study.

The intersection of these three fronts — educational application, local viability in Brazilian Portuguese, and post-training failure patterns — remains, to the best of this investigation's knowledge, under-explored. The present article contributes to fill this gap through controlled empirical diagnosis.

## 3. Methodology

This section describes, with a level of detail directed at integral reproducibility, the experimental protocol adopted. The subsequent subsections document, in order: (i) the local *offline* inference stack that emulates the school computational ceiling; (ii) the corpus of canonical scenarios and the metalinguistic rubric that anchors it; (iii) the sample matrix and HTTP hyperparameters transmitted on each call; (iv) the deterministic structural-conformance validator; (v) the inferential statistical framework applied to categorical comparisons; (vi) the criteria for metalinguistic pedagogical adherence; (vii) canonical examples of inputs and outputs observed in the corpus; (viii) the secondary falsification protocol; and (ix) reproducibility guarantees. The full statistical rationale, the complete inference payload sent to the server, and the source code of the structural validator are reported, respectively, in Appendices A and B, in conformance with the convention that separates scientific argument in the body from implementation documentation in the appendices.

### 3.1 Computational Environment and Local Offline Inference Stack

The entirety of the 312 inference calls was conducted in a **strictly local and offline** environment, without any communication with remote services during the collection phase. The choice deliberately emulates the computational ceiling available in Brazilian public-school computer labs: execution over a Central Processing Unit (CPU), without dedicated Graphics Processing Unit (GPU) acceleration, and with a Random Access Memory (RAM) restriction compatible with the typical installed base of school machines (8 GB range).

The inference orchestrator adopted was **Ollama**, a local HTTP server running on the *loopback* interface (`localhost:11434`). Calls were made via synchronous POST requests to the `/api/chat` endpoint, with `Content-Type: application/json` header, in the client–server communication pattern natively exposed by the *runtime*. Models were instantiated in Ollama's default quantization — `Q4_K_M` for most architectural families evaluated — a format compatible with the 8 GB RAM limit and widely disseminated in modest-hardware local inference implementations. The client layer was developed in Python 3.11 using the `requests` library for HTTP transport and the `json` module of the standard library for serialization and deserialization of payloads.

### 3.2 Evaluation Instrument: Scenario Corpus and Metalinguistic Rubric

The evaluation rubric was derived from Koch's taxonomy of textual cohesion (Koch, 2018, 2020) and her work on the teaching of writing (Koch & Elias, 2016), operationalized in **thirteen canonical scenarios** drafted by a specialist in Textual Linguistics. Each scenario consists of a short writing text in the school discursive genre (review, summary, retelling, opinion piece, chronicle), attributed to a hypothetical lower-secondary student (8th and 9th grades), and deliberately conveys a target cohesive phenomenon to be identified and problematized by the automated tutor. The scenarios are deliberately **synthetic**: rather than authentic student essays — which typically superimpose several deviations and would make it impossible to attribute the model's response to a specific phenomenon — each text is engineered by the specialist to isolate a single target phenomenon in controlled, verifiable form, as required for diagnostic evaluation. The choice of school genres and of canonical literary sources well established in the lower-secondary curriculum — such as the review of Machado de Assis's *A Cartomante* in scenario 1 — is equally deliberate: it keeps each scenario **ecologically valid** for the 8th–9th grade Brazilian classroom, a text that could plausibly occur in that setting even though it is synthetically constructed. The taxonomy spans two axes:

- **Referential Cohesion**: ambiguity through inadequate pronominalization; excessive lexical repetition with suppression of ellipsis and substitution by hypernym or pro-form;
- **Sequential Cohesion**: contradictory use of argumentative operators; disorganization of temporal and spatial markers; extreme juxtaposition of clauses without establishment of logical-semantic relations.

Each model received a canonical *system prompt*, identical across all experiments — ensuring strict control of variable — that defines: (i) the model's role as Socratic tutor for 8th–9th grade students of the Brazilian public school; (ii) five non-negotiable pedagogical constraints (do not provide a ready answer; do not rewrite the corrected text; value linguistic varieties and orality marks without acting as a "grammar police"; focus on cohesion and coherence per Koch; bridge with Computational Thinking when appropriate); and (iii) the output format strictly specified as a JSON object with exactly two keys — `pontos_fortes` (type `string`, monolithic) and `perguntas_reflexivas` (type `array` of `string`, with a pair of elements exemplified in the canonical schema). Keys are preserved verbatim in Brazilian Portuguese since they constitute the literal contract sent on every API call.

### 3.3 Experimental Protocol: Sample Matrix and Inference Hyperparameters

The sample matrix comprised **eight distinct language models**, distributed across two ranges:

- **Deployable range (analytical center of the study):** `qwen2.5:1.5b-instruct`, `qwen2.5:3b-instruct`, `llama3.2:1b`, `llama3.2:3b`, `gemma2:2b`, and `phi3:mini` (3.8 B). The delimitation at up to 3.8 billion parameters corresponds to the memory envelope executable in Q4 quantization within the 8 GB RAM target.
- **Reference ceiling (upper *baseline*):** `llama3:8b` and `gemma2:9b`. These models are not deployment candidates, included as comparative references of attainable quality by the same architectural family at larger scales.

Each model × scenario pair was submitted to **three independent repetitions** (n = 3), totaling 8 × 13 × 3 = **312 inference calls**. Triple replication enables estimation of standard deviation and coefficient of variation (CV = σ/μ) intra-model — indispensable metrics to distinguish expected stochastic variability, deriving from the sampling parameter `temperature`, from systemic instruction instability.

The HTTP payload sent to the server was rigorously uniform across all calls, transporting the canonical *system prompt*, the scenario text in the `user` slot, and an options block configuring `temperature = 0.2`, `stream = false`, `format = "json"`, and a client-side `timeout = 120` seconds. The choice of `temperature = 0.2` establishes a compromise between contract adherence and the micro-variability necessary for meaningful CV estimation across repetitions; `stream = false` ensures a single, well-defined termination point for *wall-clock* latency measurement; and `format = "json"` activates Ollama's native syntactic nudging toward parseable JSON output without enforcing any field-typology or key-cardinality schema — a deliberate decision aimed at gauging each model's **native adherence** to the structural contract specified in natural language, under conditions representative of realistic school deployment. The complete payload and per-hyperparameter methodological rationale are reported in Appendix B.

### 3.4 Structural Validation: Deterministic Conformance Criteria

The binary conformance classification of each response was performed by a deterministic validator that decides, over the raw content returned by the model, whether the response integrally satisfies the contract declared in the *system prompt*. The validator operates through four disjoint criteria, applied in sequence, in which the violation of any one suffices for divergence classification. **C1 — JSON syntax**: the returned string must constitute a valid JSON document per the ECMA-404 specification, ensuring the decoder respected the syntactic regime induced by Ollama's `format = "json"` parameter. **C2 — Root is object**: the outer structure must be a JSON object (nominal *mapping*), since the declared contract prescribes two named keys; the typical violation at this level is the return of an *array* at the root, a pattern inherited from tabular output regimes and incompatible with the individual tutoring interface. **C3 — `pontos_fortes` is monolithic non-empty string**: the canonical schema exemplifies this field as continuous prose, oriented to Socratic welcoming through recognition of textual merits; substituting prose with enumeration shifts the register from welcoming feedback to corrective evaluation, in direct violation of the "do not act as grammar police" directive. **C4 — `perguntas_reflexivas` is non-empty list of strings**: the contract explicitly declares the `array` of `string` type with a minimum pair of items; the validator adopts the permissive cardinality criterion ≥ 1, with divergences at this level invariably manifesting as the appearance of types other than `string` (nested objects, `null` values).

The choice for a deterministic classifier, rather than evaluation by a judge model, was deliberate: structural conformance is a syntactic-typological property decidable in finite time by type inspection, with no room for interpretive subjectivity, and delegation to an LLM judge would introduce undesired variance precisely on the dimension where the study seeks maximal objectivity. The full source code of the `divergente()` function, in the exact order of execution applied over the 312-record corpus, is reported in Appendix B.

### 3.5 Inferential Statistical Framework

Categorical comparisons supporting the structural-conformance claims of this paper were operationalized through **Fisher's exact test** on 2×2 contingency tables, complemented by **Wilson 95 % confidence intervals** for each observed proportion; the full statistical rationale — including the four converging reasons for the choice of Fisher's exact test, the treatment of the odds ratio under zero-cell contingencies, and the APA-style significance thresholds — is detailed in Appendix A. Latency data, by contrast, are reported descriptively only (Section 4), as the empirical separation between model classes is evident at the order-of-magnitude scale and does not require inferential support for interpretation.

### 3.6 Analysis Criteria: Efficiency and Metalinguistic Pedagogical Adherence

**Computational efficiency.** Latency was measured in *wall-clock* via `time.time()` in Python, including the entire local I/O stack between client and Ollama server. For each model, the following were computed: mean, standard deviation, median (p50), 95th percentile (p95), minimum, and maximum, in milliseconds. The coefficient of variation (CV) operates as a dimensionless measure of stability across repetitions. Input and output token counters were obtained from Ollama's native telemetry (`prompt_eval_count` and `eval_count`), preserving fidelity of the measure relative to each model's specific tokenizer.

**Metalinguistic pedagogical adherence.** For the model best classified along the dimensions of efficiency and structural conformance, additional qualitative inspection was conducted, verifying the presence, in the response text, of terms from Koch's metalinguistic taxonomy — cohesion, connector, pronoun, referential, sequential, ambiguity, repetition, synonym, ellipsis, argumentative operator, temporal marker, juxtaposition. The presence of at least one rubric term was considered a minimum indication of metalinguistic adherence; its absence classifies the response as operating in an exclusively thematic-surface layer.

### 3.7 Anatomy of Outputs: Canonical Examples from the Corpus

To expose the nature of the contracts evaluated, this subsection illustrates, with literal material extracted from the corpus, the cohesive deviation embedded in a representative scenario, one conformant output, and two distinct modalities of divergent output.

**Input — scenario 1 (Referential Cohesion: excessive lexical repetition).** Synthetic text attributed to a hypothetical student, extracted literally from the canonical thirteen-scenario corpus (preserved in Brazilian Portuguese as the object of linguistic study):

> Resenha sobre A Cartomante: A cartomante falou pro Camilo que tava tudo bem. A cartomante leu as cartas. A cartomante sorriu pra ele. A cartomante deu certeza pra ele. Depois o Camilo foi pra casa do Vilela e morreu. A cartomante tinha errado tudo.

The embedded target phenomenon is the lexical repetition of the noun phrase *"a cartomante"* in four consecutive clauses — a paradigmatic case of referential cohesion through repetition, in which the tutor would be expected to induce the student toward substitution by pronominal pro-form or hypernym, leading them to reflect on the referential chain without providing the corrected form outright.

*Translation note for non-Lusophone readers (not part of the experiment): "Review of 'The Fortune-Teller'. The fortune-teller told Camilo everything was fine. The fortune-teller read the cards. The fortune-teller smiled at him. The fortune-teller gave him certainty. Then Camilo went to Vilela's house and died. The fortune-teller had got it all wrong."*

**Conformant output — `qwen2.5:3b-instruct`, repetition 1.** The model strictly respects the typology declared in the *system prompt*: `pontos_fortes` is returned as continuous prose and `perguntas_reflexivas` as a pair of questions in a list of *strings*.

```json
{
  "pontos_fortes": "O texto tem uma estrutura boa, com um início claro e uma conclusão que ressalta a importância da leitura.",
  "perguntas_reflexivas": [
    "Como você imagina o que aconteceria se a cartomante tivesse acertado tudo?",
    "Por que é importante ler entre as linhas nos livros?"
  ]
}
```

Note that structural adherence does not entail pedagogical adequacy: the conformant response above shifts to the thematic plane of the literary work (importance of reading), without mobilizing any metalinguistic terminology — a phenomenon discussed qualitatively in Section 6.

**Divergent output, modality A — `llama3.2:1b`, repetition 1 (typological violation of `pontos_fortes`).** The model emits syntactically valid, parseable JSON endowed with both expected keys; divergence manifests exclusively as substitution of the monolithic prose by itemized enumeration, in direct violation of C3 of the `divergente()` algorithm:

```json
{
  "pontos_fortes": [
    "A Cartomante falou pro Camilo que tava tudo bem.",
    "A Cartomante leu as cartas.",
    "A Cartomante sorriu pra ele.",
    "A Cartomante deu certeza pra ele."
  ],
  "perguntas_reflexivas": [
    "Ela falou, mas não disse nada.",
    "O que a Cartomante fez?",
    "Por que a Cartomante sorriu?"
  ]
}
```

**Divergent output, modality B — `phi3:mini`, repetition 1 (integral schema substitution and pedagogical inversion).** The model abandons the declared canonical schema and imposes a structure of its own built around nested objects with unsolicited keys (`erro`, `correção`, `texto_original`, `texto_proposto`), simultaneously violating C3 (type of `pontos_fortes`) and the anti-prescriptivist pedagogical directive of the *system prompt*. Illustrative excerpt:

```json
{
  "pontos_fortes": [
    {
      "erro": "A palavra 'tava' é uma forma coloquial da conjugação do verbo estar, que pode ser considerada informal e menos adequada para um texto acadêmico. A alternativa seria usar a forma correta 'estava'.",
      "correção": {
        "texto_original": "A cartomante falou pro Camilo que tava tudo bem.",
        "texto_proposto": "A cartomante falou para Camilo que estava tudo bem."
      }
    },
    {
      "erro": "O uso de 'leu' é um erro comum na conjugação do verbo ler no passado, pois a forma correta seria 'lera'.",
      "correção": { "texto_original": "A cartomante leu as cartas.", "...": "..." }
    }
  ]
}
```

Note the double anomaly: (i) the model classifies the legitimate colloquialism *"tava"* as an error to be corrected, in violation of the explicit directive to value linguistic varieties; and (ii) it **hallucinates a non-existent grammatical rule** by prescribing the form *"lera"* (pluperfect indicative) as replacement for the form *"leu"* (simple past), correctly employed by the student — confusing distinct verbal aspects and introducing an error into the original text under pretext of correction. This case confirms the multidimensional collapse pattern that will be discussed in Subsection 5.2.

### 3.8 Secondary Falsification Protocol via Counter-Experiment

In addition to the main protocol described in the previous subsections, a secondary falsification protocol was designed and executed, specifically directed at the most expressive architectural finding of the study — the systematic divergence observed in the Llama 3.2 family (1B and 3B). The methodological motivation is twofold: (a) rule out competing hypotheses that would reduce the finding to an instrumental artifact — configuration error, stochastic instability, interference of the Python client layer — and (b) characterize the precise nature of the observed bias, distinguishing *compositional incapacity* from *disobedience under zero-shot regime*. The protocol was operationalized in three disjoint isolations, conducted on the same canonical scenarios as the main protocol and under the same local Ollama inference stack:

1. **E1 — Stochasticity isolation.** Repetition of 26 calls (2 models × 13 scenarios × 1 repetition) with `temperature = 0.0`, a deterministic regime in which the decoder adopts strict greedy sampling. Eventual stability of the failure here rules out the hypothesis of sampling variability as cause.
2. **E2 — In-context demonstration isolation.** Repetition of 24 calls (2 models × 12 scenarios × 1 repetition) preceded, in the message sequence, by a `user`/`assistant` pair exhibiting scenario 1 and its canonical gold response in strict schematic format. Scenario 1 is consumed as demonstration; the remaining twelve are evaluated under minimal contextual anchoring (*one-shot in-context learning*). Eventual reversal of divergence here demonstrates that the compositional capacity of the model is intact and isolates the bias as an obedience phenomenon under zero-shot regime.
3. **E2b — Joint isolation.** Combination of E1 and E2: in-context demonstration under `temperature = 0.0`, across 24 calls, to verify whether the reversal observed in E2 is stable when all source of stochastic variability is suppressed.
4. **E3 — Client-layer isolation.** Repetition of the base calls via the `curl` command-line utility, with the same JSON payload sent directly to the Ollama endpoint, without mediation of the Python `requests` library. Eventual persistence of failure here rules out interference of the client transport layer as cause.

The two primary isolations (E1 and E2) operate on theoretically independent axes — sampling temperature and contextual anchoring — and their combination in E2b plus the instrumental isolation of E3 total 80 additional calls under the same canonical SYSTEM_PROMPT, under the same local Ollama, over the same scenarios of the main corpus. Results are reported in Subsection 5.3.

### 3.9 Reproducibility and Artifact Availability

The complete corpus of the 312 calls — including *prompts* sent, raw responses in `resposta_ia`, telemetry metrics (`tokens_input`, `tokens_output`, `latencia_ms`), and execution metadata (`modelo_testado`, `cenario_id`, `rep`) — was preserved in two structured JSON files of 312 homogeneous records, in long-matrix format. Collection, deterministic classification, and aggregation scripts were developed in Python 3.11, using only the standard library and the packages `requests`, `pandas`, `matplotlib`, and `scipy`. The full source code and raw data are publicly available in the authors' repository, in conformance with the Open Science practices recommended by the Brazilian Computer Society.

## 4. Computational Efficiency

Table 1 synthesizes the aggregated efficiency metrics per model (n = 39 calls per row), ordered by increasing mean latency.

**Table 1.** Efficiency metrics per model.

| Model | Mean latency (ms) | Std. dev. (ms) | p95 (ms) | CV | Output tokens (mean) |
|---|---:|---:|---:|---:|---:|
| `qwen2.5:1.5b-instruct` | 2,299 | 474 | 3,234 | 20.6 % | 118.8 |
| `llama3.2:1b` | 2,389 | 1,423 | 6,391 | 59.6 % | 119.5 |
| `qwen2.5:3b-instruct` | 2,906 | 552 | 4,486 | 19.0 % | 104.6 |
| `llama3.2:3b` | 3,020 | 695 | 4,721 | 23.0 % | 108.9 |
| `gemma2:2b` | 3,744 | 720 | 5,080 | 19.2 % | 121.8 |
| `gemma2:9b` | 8,681 | 1,425 | 11,130 | 16.4 % | 126.9 |
| `llama3:8b` | 10,523 | 19,708 | 19,326 | 187.3 % | 144.7 |
| `phi3:mini` | 14,769 | 12,228 | 43,717 | 82.8 % | 471.2 |

The classical Human–Computer Interaction literature establishes three system-response thresholds relevant to user experience: up to 100 ms for the sensation of instantaneity; up to 1 s for preservation of cognitive flow; and up to **10 s for maintenance of the user's directed attention in sequential tasks** (Nielsen, 1993; Card; Robertson; Mackinlay, 1991). This last threshold is the operational criterion adopted in this study for pedagogical viability in synchronous classroom use — above it, the student disengages from the task while waiting for the tutor's response, compromising the continuity of metalinguistic reflection.

In light of this criterion, it is observed that the **Qwen 2.5 family leads markedly on the efficiency dimension**, with mean latencies of 2.299 s (1.5 B variant) and 2.906 s (3 B variant). Both models sit at less than one third of the UX threshold, and their coefficients of variation (CV ≈ 19–21 %) indicate that the observed variability is predominantly stochastic — attributable to the `temperature = 0.2` parameter — rather than deriving from systemic instability. The 95th percentile of latency remains, in both cases, below 4.5 seconds, ensuring that even executions in the upper extreme of the distribution do not break the time contract with the user.

In contrast, the `phi3:mini` model configures a **paradigmatic case of computational infeasibility for the synchronous educational scenario**. Its mean latency of 14.769 s exceeds the HCI threshold by more than 47 %, and analysis of the distribution reveals that the problem is structural, not point-wise: the standard deviation of 12,228 ms (CV of 82.8 %) and p95 of 43,717 s evidence markedly bimodal behavior, with prolonged-generation episodes that can exceed three quarters of a minute in extreme cases. Compounding this temporal instability is a mean output verbosity of **471.2 tokens** — between 3.9 and 4.5 times higher than the other models evaluated, which oscillate between 104 and 145 tokens. Such verbosity itself configures a pedagogical failure: effective Socratic responses in educational context are recognized as brief and focal (Paul; Elder, 2007), and the textual inflation observed in Phi-3 indicates a misalignment between the model's generation regime and the communicational requirements of the task.

It is also worth registering anomalous behavior of the `llama3:8b` model at the upper extreme of the distribution, with CV of 187.3 % and absolute maximum of approximately 130 seconds in isolated execution. Although situated in the comparative-ceiling range of the study and therefore outside the candidate set for deployment, the finding recommends caution in the adoption of 7–8 billion parameter models in comparative research based on temporal metrics.

## 5. Structural Conformance and Architectural Findings

The dimension of conformance to the structural contract specified in natural language — requirement of a JSON object with keys `pontos_fortes` (type `string`) and `perguntas_reflexivas` (type `array` of `string`) — produces the most expressive finding of this study. Table 2 consolidates the conformance rates observed, accompanied by Wilson 95 % confidence intervals and the two-sided Fisher exact *p*-value for each model relative to `qwen2.5:3b-instruct` as the reference model.

**Table 2.** Structural conformance per model, with Wilson 95 % CI and Fisher exact test against the reference model.

| Model | k / n | Conf. rate | Wilson 95 % CI | Tier | Fisher vs. Qwen 3B |
|---|---:|---:|:---:|:---:|:---:|
| `qwen2.5:3b-instruct` | 39 / 39 | 100.0 % | [91.0 %; 100.0 %] | deployable | reference |
| `gemma2:9b` | 39 / 39 | 100.0 % | [91.0 %; 100.0 %] | ceiling | *p* = 1.000 n.s. |
| `llama3:8b` | 39 / 39 | 100.0 % | [91.0 %; 100.0 %] | ceiling | *p* = 1.000 n.s. |
| `qwen2.5:1.5b-instruct` | 38 / 39 | 97.4 % | [86.8 %; 99.5 %] | deployable | *p* = 1.000 n.s. |
| `gemma2:2b` | 38 / 39 | 97.4 % | [86.8 %; 99.5 %] | deployable | *p* = 1.000 n.s. |
| `llama3.2:1b` | 0 / 39 | 0.0 % | [0.0 %; 9.0 %] | deployable | ***p* < 0.001 \`**`* |
| `llama3.2:3b` | 0 / 39 | 0.0 % | [0.0 %; 9.0 %] | deployable | ***p* < 0.001 \`**`* |
| `phi3:mini` | 0 / 39 | 0.0 % | [0.0 %; 9.0 %] | deployable | ***p* < 0.001 \`**`* |

*Note. k = conformant responses; n = 39 calls per model. \`*`\`*`\`*` p < 0.001, two-sided Fisher exact, α = 0.05. When a cell of the contingency table is zero, the odds ratio is not finitely estimable; the reported p-value derives from the exact hypergeometric distribution with continuity correction. Wilson 95 % CIs computed without normal approximation.*

The distribution is clearly bimodal: five models exhibit integral or near-integral adherence (97.4–100.0 %, Wilson 95 % CI: [86.8 %; 100.0 %]), while three models collapse entirely (0.0 %, Wilson 95 % CI: [0.0 %; 9.0 %]), with no intermediate instances. Fisher's exact test confirms that the conformance rates of the Llama 3.2 family (both 1B and 3B variants) and of Phi-3 Mini differ from the reference model at *p* < 0.001 each, while the four other conformant models — including the 7–9 B reference-ceiling pair — are statistically indistinguishable from the reference (*p* = 1.000 n.s.). This last observation is methodologically important: the deployable model `qwen2.5:3b-instruct` is not detectably inferior in structural conformance to the larger reference-ceiling models, which strengthens its selection as the operationally preferable base. Such polarization suggests that conformance to the contract **is not a monotonic function of the parameter count**, but rather an architectural-behavioral property of the family and of the instruction-tuning regime.

### 5.1 The Family Failure of the Llama 3.2 Line

Qualitative inspection of the outputs of the two Llama 3.2 variants (1 B and 3 B) reveals a rigorously identical failure pattern: the emitted JSON is, across all 78 calls, syntactically valid and parseable; divergence manifests exclusively as a **typological violation** of the `pontos_fortes` field, returned consistently as an *array* of *strings* (typically enumerating two to four items) in place of the specified monolithic `string` type. The perfect symmetry between the two family sizes — in parallel with the full conformance of the Qwen 2.5 family at analogous sizes under identical *prompt* — rules out hypotheses of insufficient capacity or stochasticity and displaces the explanation toward post-training.

As reported in Table 2, the pairwise comparison of the Llama 3.2 family against the reference model `qwen2.5:3b-instruct` yields *p* < 0.001 \`*`\`*`\`*` for both variants (1B and 3B), while the matched-scale Qwen 2.5 family is statistically indistinguishable from the reference (*p* = 1.000 n.s.). The cross-family separation, at matched scale and under identical natural-language specification, is therefore not a borderline result subject to interpretation: it is one of the most categorical statistical contrasts observable in 2×2 categorical experimentation. As noted in the table caption, the odds ratio is not finitely estimable when one cell of the contingency table is zero; the exact *p*-value alone, derived from the hypergeometric distribution, suffices to falsify the null hypothesis of homogeneous conformance rates between families at any conventional significance threshold.

This pattern finds coherent interpretation in light of the literature on **format bias** in preference-post-trained models. Zheng et al. (2023) and Wu and Aji (2023) document that implicit format-based rewards — operating either through human evaluators or judge models — induce systematic inflation of stylistic markers such as lists, *bullet points*, bold headings, and enumerations, at the expense of *prompt* fidelity. The operational motivation of this bias is direct: responses structured as marked items are perceived as more professional and readable by human evaluators in general-purpose assistant interfaces, and the reward signal internalizes this preference as a dominant attractor in the generation space.

Liu et al. (2025), in the framework of **GuideEval**, offer the behavioral-theoretical complement necessary to the interpretation of the finding: the framework decomposes the tutorial competence of a model into three distinct phases — Perception of the student's cognitive state, Orchestration of the tutorial response, and Elicitation of reflection — and demonstrates that failures in the Orchestration phase typically manifest as rigidity toward format instruction, with the model retreating to output patterns strongly entrenched in post-training. In terms of Liu et al.'s scheme, the anomaly observed in the Llama 3.2 line is precisely an Orchestration failure: the model *perceives* the task correctly (assisting the student) and *would elicit* questions, but the intermediate stage of behavioral modulation of the response collapses to the enumeration attractor conditioned by its generalist post-training. The present study contributes to the literature on two aspects. **First**, it demonstrates that the formatting bias is **resistant to explicit counter-specification in natural language under zero-shot regime**: the *system prompt* univocally declares the expected type, and yet the enumeration attractor prevails in 100 % of the calls. **Second**, it evidences that the bias constitutes an **architectural signature consistent across scales** of the same family — a fact that suggests the origin of the phenomenon in the institutional post-training procedure adopted by the team responsible for the 3.2 line, rather than in particularities of an isolated *checkpoint*. The operational implication, however, requires the rigorous qualification provided by Subsection 5.3: in the absence of external syntactic coercion **and under pure zero-shot regime** — the standard conditions of most economically viable educational deployments —, the Llama 3.2 family is not deployable as structured-tutoring infrastructure in Brazilian Portuguese; under minimal contextual anchoring by demonstration (*one-shot*), however, conformance is fully recovered, which reclassifies the finding as a **reversible zero-shot bias** rather than as the model's categorial compositional incapacity.

### 5.2 The Multidimensional Collapse of Phi-3 Mini

The failure of `phi3:mini` is qualitatively distinct and more severe. Analysis of the outputs reveals that the model not only typologically violates the `pontos_fortes` field — emitted in 100 % of calls as an *array* —, but **entirely replaces the declared schema** with its own structure, built around unsolicited fields `erro`, `correção`, `texto_original`, and `texto_proposto`. Additionally, 20.5 % of calls present `perguntas_reflexivas` as `NoneType` or composed of nested non-*string* elements, configuring progressive deterioration of contract fidelity as generation advances. The Fisher exact comparison of Phi-3 Mini against the reference model (Table 2) yields *p* < 0.001 \`*`\`*`\`*`, of the same magnitude as the Llama 3.2 family contrasts, justifying its analytical bracketing in the same regime of zero-shot non-adherence.

More grave, however, is the **pedagogical inversion** of the *prompt*: the model, trained predominantly on English-language corpora for general-purpose assistant use cases, assumes a corrective-prescriptivist posture in flagrant violation of the explicit directive of the *system prompt* — "value linguistic varieties and orality marks" —, producing, for instance, outputs in which it classifies the legitimate colloquialism *"tava"* as an error to be corrected to *"estava"* and, in sequence, **hallucinates a non-existent grammatical rule** by prescribing the form *"lera"* (pluperfect) as replacement for the form *"leu"* (simple past), correctly employed by the student.

This double-violation pattern — structural and pedagogical — confirms the general hypothesis of Wu and Aji (2023) on the imperfect transferability of instruction habits across distinct linguistic-pragmatic domains. The model, optimized for an Anglocentric conversational regime in which explicit correction is virtuous, transports this habit into a pedagogical-linguistic context in Brazilian Portuguese in which it is harmful, and does so even under counter-instruction in natural language. The combination observed in Phi-3 — structural collapse, pedagogical inversion, temporal instability, and quadruple verbosity relative to peers — configures a testimonial case of the transferability limit of Anglocentric SLMs to educational tasks in Brazilian Portuguese, even when the model is nominally declared multilingual by its developers.

The phenomenon of Phi-3's inflated verbosity — 471 mean tokens against the 104 to 145 range of the other models — additionally finds echo in **MathTutorBench** by Macina et al. (2025), which systematizes, in an adjacent domain (mathematical tutoring), the finding that off-the-shelf models tend to superimpose thematic expertise over pedagogical competence, transforming the tutorial act into an extended expository monologue rather than brief oriented maieutics. Phi-3's verbal excess observed in this study is therefore not a particularity of tokenization or instance noise — it is a local manifestation of a systemic pattern of post-trained generalist models, which conflate output volume with tutorial quality, in direct prejudice of the focal and dialogic regime that defines Socratic maieutics (Paul; Elder, 2007).

### 5.3 Robustness Analysis of the Llama 3.2 Architectural Finding via Controlled Counter-Experiment

The perfect uniformity of divergence observed in the Llama 3.2 family — 78 calls, two architectural sizes, zero conformant responses in the main protocol — imposes, by sound scientific practice, deliberate examination of competing hypotheses that would reduce the finding to an instrumental artifact before sustaining it as a behavioral signature of the model. To this end, the secondary protocol described in Subsection 3.8 was integrally executed, totaling 80 additional calls under the same local inference stack. Table 3 synthesizes the outcomes, accompanied by Wilson 95 % CIs and the two-sided Fisher exact *p*-value of each isolation against the zero-shot baseline.

**Table 3.** Structural conformance of the Llama 3.2 family under falsification isolations.

| Isolation | Llama 3.2 1B | Llama 3.2 3B | Wilson 95 % CI (3B) | Fisher vs. baseline |
|---|:---:|:---:|:---:|:---:|
| Baseline (zero-shot, *t* = 0.2) | 0 / 39 (0.0 %) | 0 / 39 (0.0 %) | [0.0 %; 9.0 %] | — |
| **E1** (zero-shot, *t* = 0.0) | 0 / 13 (0.0 %) | 0 / 13 (0.0 %) | [0.0 %; 22.8 %] | *p* = 1.000 n.s. |
| **E2** (one-shot, *t* = 0.2) | **11 / 12 (91.7 %)**¹ | **12 / 12 (100.0 %)** | [75.8 %; 100.0 %] | ***p* < 0.001 \`**`* |
| **E2b** (one-shot, *t* = 0.0) | **9 / 12 (75.0 %)**² | **12 / 12 (100.0 %)** | [75.8 %; 100.0 %] | ***p* < 0.001 \`**`* |
| **E3** (curl, zero-shot) | failure reproduced | failure reproduced | — | — |

*Note. ¹ The single non-conformance of the 1B in E2 derives from HTTP timeout, not from a structural violation of the response actually returned. ² Idem for 3 of 12 of the 1B in E2b — timeouts associated with the context-budget increase introduced by the demonstrative pair of one-shot, with no implication on the typological conformance of the completed calls. \`*`\`*`\`*` p < 0.001, two-sided Fisher exact, α = 0.05. Fisher comparisons reported for the 3B variant against its own zero-shot baseline (0/39); the 1B variant exhibits the same direction of effect under the same conventional thresholds.*

The joint reading of the four isolations sustains three interlinked conclusions, of falsificationist nature, on the nature of the finding.

**First conclusion — the bias is deterministic, not stochastic.** In E1, the complete suppression of sampling variability by `temperature = 0.0` produces no conformance; on the contrary, the 3B model converges to the structural attractor `pontos_fortes = list[str], cardinality = 2` in 12 of the 13 scenarios, exhibiting the near-degeneration profile typical of bias encoded in the weight space. Hypotheses that would attribute divergence to sampling noise or instability across repetitions are therefore falsified.

**Second conclusion — the bias is in the model, not in the client stack.** In E3, transmission of the same JSON payload to the Ollama endpoint via `curl`, eliminating any mediation by the Python `requests` library, integrally reproduces the typological-divergence pattern observed in the main protocol — `pontos_fortes` returned as a list, JSON syntactically valid, other keys consistent. Hypotheses that would attribute divergence to interference of the client transport layer, HTTP headers, payload encoding, or `messages` array serialization are therefore falsified.

**Third conclusion — the bias is one of zero-shot obedience, not of compositional incapacity.** In E2, the precedence of a single `user`/`assistant` pair exhibiting the canonical gold response for scenario 1 produces total reversal of divergence: the 3B model reaches 12/12 conformance in the twelve subsequent scenarios, and the 1B model reaches 11/12 (with the single exception attributable to transport *timeout*, not format failure). The stability of this reversal is confirmed in E2b, in which the combination of *one-shot* with `temperature = 0.0` preserves 100 % conformance in the 3B. The reversal is corroborated by Fisher's exact test on the 2×2 condition-by-conformance contingency (Table 3): for both the Llama 3.2 3B variant (12/12 conformant under one-shot vs. 0/39 baseline) and the 1B variant (11/12 conformant, with the single non-conformance attributable to HTTP timeout rather than structural violation), the contrast yields *p* < 0.001 \`*`\`*`\`*`. By contrast, the determinism-isolation E1 (0/13 vs. 0/39 baseline) yields *p* = 1.000 n.s., confirming that the bias is invariant to sampling temperature. The epistemic inference is direct: the Llama 3.2 family models **possess the compositional capacity** to produce `pontos_fortes` as monolithic string respecting the declared schema; what is compromised is obedience to this specification when provided exclusively in natural language under zero-shot regime, without contextual demonstration. The enumeration attractor is dominant only in the absence of a contrary demonstrative anchor.

This set of conclusions repositions the Subsection 5.1 finding with added precision. The Llama 3.2 family does not exhibit categorial incapacity to operate as a structured tutor — it exhibits a **reversible zero-shot bias**, in the strict sense of Liu et al. (2025): failure in the Orchestration phase of the tutorial response when the operational regime does not provide a demonstrative reference, with full recovery when such reference is provided. This characterization has three implications:

1. **Methodological implication for the paper.** The choice of `qwen2.5:3b-instruct` as base model for subsequent pedagogical fine-tuning remains justified — among the models evaluated, it is the only one conformant under zero-shot, and zero-shot is the regime of lowest engineering cost in the classroom. But the justification is no longer "Llama 3.2 is not deployable" and becomes "Qwen 2.5 3B is the only one that dispenses additional prompting engineering to guarantee structural contract".
2. **Operational implication for alternative deployments.** A valid intermediate route is established for schools or municipal networks that, for pedagogical or technical-sovereignty reasons, prefer the Llama 3.2 family: the additional engineering cost consists of keeping a ~300-token demonstrative pair in the context per call, a moderate budget increase but with an observable latency penalty, as registered by the *timeouts* in E2/E2b over the 1B.
3. **Implication for the literature on format bias.** The present study contributes controlled experimental evidence that the bias documented by Zheng et al. (2023), Wu and Aji (2023), and Liu et al. (2025) **is not absolute**: it is a function of the operational regime adopted. This empirical refinement, derived from a directed falsification protocol, offers a basis for future studies on the computational economy of educational *prompt engineering* as a mitigator of post-training bias in off-the-shelf SLMs.

## 6. Qualitative Analysis: Pedagogical Adherence of the Conformant Model

The joint reading of Sections 4 and 5 isolates `qwen2.5:3b-instruct` as the unique configuration among the *deployable* models simultaneously satisfying all non-functional requirements: mean latency of 2.906 s (below the HCI threshold), controlled variability (CV = 19.0 %), and full adherence (0/39) to the JSON contract without recourse to external coercion. This result, however, **does not authorize optimistic inference about the model's pedagogical adequacy**, as demonstrated in the additional qualitative inspection below.

Applying the metalinguistic criterion described in Subsection 3.6 to the 13 responses of the first repetition of `qwen2.5:3b-instruct`, it is observed that only 6 of 13 responses (46.2 %; Wilson 95 % CI: [23.2 %; 70.9 %]) mobilize any terminology of the cohesion taxonomy — pronominalization, lexical repetition, connective, argumentative operator, temporal marker, juxtaposition. Table 4 reports the observed proportion alongside the interpretation of the confidence bounds.

**Table 4.** Metalinguistic adherence of `qwen2.5:3b-instruct` (Wilson 95 % CI).

| Metric | Result |
|---|---|
| Scenarios mobilizing Koch terminology | 6 / 13 (46.2 %) |
| Wilson 95 % CI | [23.2 %; 70.9 %] |
| Upper bound (optimistic) | 70.9 %: absence in ≥ 29 % of scenarios |
| Lower bound (pessimistic) | 23.2 %: absence in ≥ 77 % of scenarios |
| Classification | Partial and unstable adherence (sustained by CI) |

*Note. The width of the CI ([23.2 %; 70.9 %]) reflects the small n of canonical scenarios (n = 13) and constitutes an acknowledged limitation of this analysis; nevertheless, even the upper bound of the interval implies absence of metalinguistic terminology in at least 29 % of scenarios, preserving the characterization of partial and unstable adherence regardless of where the true rate lies within the interval.*

In the seven remaining scenarios (53.8 %), the model shifts the interlocution to the **thematic-narrative plane of the literary work cited** by the student (characters, plot, setting), commenting elements of the literary source rather than evaluating the textuality of the production. As an illustration, the response to the scenario on Referential Cohesion — in which the student text repeats eight times the noun phrase *"a cartomante"* across four consecutive sentences — merely observes "good structure, clear beginning, and conclusion that highlights the importance of reading", without any mention of the excessive lexical repetition that constituted the target phenomenon of the scenario.

This constitutes a **categorial task failure**: the model conflates *what the student wrote* with *what the student wrote about*, and loses the central pedagogical object of the Socratic intervention oriented by metalinguistic rubric. Even in scenarios in which some taxonomy term is evoked, the approach is predominantly declarative — the model *names* the linguistic phenomenon without leading the student to *reflect* on how it operates in the produced text, contradicting the dialogic Socratic structure prescribed by the rubric (Paul; Elder, 2007).

The reading of this finding finds direct theoretical support in **MathTutorBench** by Macina et al. (2025), which documents, in an adjacent educational domain, the existence of a **systematic trade-off between thematic expertise and pedagogical competence** in off-the-shelf models: the same model capable of correctly discussing the content of a literary work or problem tends to fail as a tutor when faced with the task of leading the student through progressive questioning, retreating to an expository-thematic regime. The behavior here observed in `qwen2.5:3b-instruct` is a local manifestation of this phenomenon: the model is proficient at conversing *about* "A Cartomante" as a literary work — produces reasonable commentary on structure, reading, and plot — but fails to sustain the metalinguistic-Socratic stance that would reposition the focus on the student's text as a linguistic artifact open to problematization in light of Koch's taxonomy. Complementarily, the GuideEval framework of Liu et al. (2025) categorizes this failure mode as joint deficiency in the Perception phases (the model does not detect the target cohesive phenomenon) and Elicitation (even when it detects, it does not conduct questioning that makes the student operate on the text itself), confirming that adherence to format and pedagogical adequacy constitute logically independent dimensions of a model's tutorial competence.

## 7. Conclusion

This study conducted a controlled diagnostic evaluation of eight open Small Language Models, executed locally under infrastructure restrictions compatible with the material reality of the Brazilian public school, against a metalinguistic rubric derived from the textual-cohesion taxonomy of Ingedore Koch. **With respect to RQ1 (native structural adherence)**, the structural-conformance dimension produced a sharp result: among models in the *deployable* range (up to 3.8 billion parameters), only **Qwen 2.5 3B-Instruct** combines integral adherence to the JSON contract declared in natural language, mean latency comfortably situated below the Human–Computer Interaction threshold for synchronous tasks, and low variability across repetitions — constituting the only evaluated configuration that simultaneously satisfies, without recourse to external grammatical coercion, all non-functional requirements for educational deployment.

**With respect to RQ2 (mobilization of the metalinguistic rubric)**, however, the reading of this result does not authorize optimistic inference about the model's pedagogical adequacy. Systematic qualitative inspection of responses evidences that, although structurally conformant, the model presents **partial and unstable adherence to Koch's metalinguistic rubric**, mobilizing it in only 46 % of scenarios and operating predominantly in a thematic-surface layer in the remaining 54 %.

This finding, articulated with the architectural findings discussed in Section 5 and the falsification protocol reported in Subsection 5.3, sustains the central conclusion of the study: **the open language models contemporaneously available off-the-shelf, within their range of computational viability for Brazilian public schools, are insufficient for the task of Socratic tutoring of writing in Brazilian Portuguese grounded in a fine metalinguistic rubric, under zero-shot regime**. The insufficiency manifests in two distinct regimes: (i) **regime of zero-shot structural non-adherence**, exhibited by the Llama 3.2 and Phi-3 families, in which the model violates the syntactic-typological contract even under explicit natural-language specification — characterized, in the case of the Llama 3.2 family, by an obedience bias demonstrably reversible via minimal contextual anchoring (*one-shot*), and therefore distinguishable from compositional incapacity; and (ii) **regime of structural adherence with pedagogical superficiality**, exemplified by Qwen 2.5 3B-Instruct, in which the model respects the format but operates predominantly in a thematic-surface layer, without systematically mobilizing the theoretical taxonomy required by the task.

The simultaneous persistence of these two failure regimes — across models from architecturally distinct families, trained by diverse institutions, and optimized for predominantly Anglophone markets — converges to the diagnosis that the task of Socratic tutoring in Brazilian Portuguese for basic education **is not addressed in zero-shot regime by off-the-shelf generalist models** and demands, as necessary scientific unfolding, the development of **specialized models through supervised fine-tuning on curated pedagogical corpora in Brazilian Portuguese**, aligned with the metalinguistic rubric specific to the school domain. The alternative route via *prompt engineering* with demonstrative anchoring, made viable by the reversibility documented in Subsection 5.3, remains technically available, but presupposes an operational regime whose costs in context budget and latency must be weighed against the savings obtained in training. Such unfolding, outside the scope of the present diagnosis, constitutes the subsequent research agenda of this investigation.

## Acknowledgments

The authors thank the Graduate Program in Informatics in Education (PPGIE) of the Federal University of Rio Grande do Sul (UFRGS) for institutional support.

---

## References

Abdin, M., Aneja, J., Awadalla, H., Awasthi, A., Awan, A., Bach, N., Bahree, A., Bakhtiari, A., Bao, J., Behl, H., et al. (2024). *Phi-3 technical report: A highly capable language model locally on your phone*. arXiv:2404.14219. https://arxiv.org/abs/2404.14219

Brasil. (2018). *Lei nº 13.709, de 14 de agosto de 2018: Lei Geral de Proteção de Dados Pessoais (LGPD)*. Presidência da República.

Brasil. (2025). *Lei nº 15.211, de 22 de setembro de 2025: Estatuto Digital da Criança e do Adolescente (ECA Digital)*. Presidência da República.

Card, S. K., Robertson, G. G., & Mackinlay, J. D. (1991). The information visualizer, an information workspace. In *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (CHI '91)* (pp. 181–186). ACM Press.

CGI.br, NIC.br, & Cetic.br. (2025). *Pesquisa sobre o uso das tecnologias de informação e comunicação nas escolas brasileiras: TIC Educação 2024*. Comitê Gestor da Internet no Brasil. https://cetic.br/pesquisa/educacao/

Gemma Team. (2024). *Gemma 2: Improving open language models at a practical size*. arXiv:2408.00118. https://arxiv.org/abs/2408.00118

Grattafiori, A., Dubey, A., Jauhri, A., Pandey, A., Kadian, A., Al-Dahle, A., Letman, A., Mathur, A., Schelten, A., Vaughan, A., et al. (2024). *The Llama 3 herd of models*. arXiv:2407.21783. https://arxiv.org/abs/2407.21783

Kasneci, E., Sessler, K., Küchemann, S., Bannert, M., Dementieva, D., Fischer, F., Gasser, U., Groh, G., Günnemann, S., Hüllermeier, E., et al. (2023). ChatGPT for good? On opportunities and challenges of large language models for education. *Learning and Individual Differences*, *103*, 102274. https://doi.org/10.1016/j.lindif.2023.102274

Koch, I. G. V. (2018). *A coesão textual* [Textual cohesion] (22nd ed.). Contexto. (Original work published 1989)

Koch, I. G. V. (2020). *Introdução à linguística textual: trajetória e grandes temas* [Introduction to textual linguistics: Trajectory and great themes] (2nd ed.). Contexto.

Koch, I. G. V., & Elias, V. M. (2016). *Escrever e argumentar* [Writing and arguing]. Contexto.

Liu, Y., Li, C., Zhang, T., Wang, M., Zhu, Q., Li, J., & Huang, H. (2025). *Discerning minds or generic tutors? Evaluating instructional guidance capabilities in Socratic LLMs*. arXiv:2508.06583. https://arxiv.org/abs/2508.06583

Macina, J., Daheim, N., Hakimi, I., Kapur, M., Gurevych, I., & Sachan, M. (2025). MathTutorBench: A benchmark for measuring open-ended pedagogical capabilities of LLM tutors. In *Proceedings of EMNLP 2025*. ACL. arXiv:2502.18940. https://arxiv.org/abs/2502.18940

Nielsen, J. (1993). *Usability engineering*. Morgan Kaufmann.

Paul, R., & Elder, L. (2007). Critical thinking: The art of Socratic questioning. *Journal of Developmental Education*, *31*(1), 36–37.

Tlili, A., Shehata, B., Adarkwah, M. A., Bozkurt, A., Hickey, D. T., Huang, R., & Agyemang, B. (2023). What if the devil is my guardian angel: ChatGPT as a case study of using chatbots in education. *Smart Learning Environments*, *10*(1), Article 15. https://doi.org/10.1186/s40561-023-00237-x

Wu, M., & Aji, A. F. (2023). *Style over substance: Evaluation biases for large language models*. arXiv:2307.03025. https://arxiv.org/abs/2307.03025

Yang, A., Yang, B., Hui, B., Zheng, B., Yu, B., Zhou, C., Li, C., Li, C., Liu, D., Huang, F., et al. (2024). *Qwen2.5 technical report*. arXiv:2412.15115. https://arxiv.org/abs/2412.15115

Zheng, L., Chiang, W.-L., Sheng, Y., Zhuang, S., Wu, Z., Zhuang, Y., Lin, Z., Li, Z., Li, D., Xing, E. P., Zhang, H., Gonzalez, J. E., & Stoica, I. (2023). Judging LLM-as-a-judge with MT-bench and Chatbot Arena. In *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*.

---

## Appendix A — Statistical Rationale

This appendix details the inferential framework summarized in Subsection 3.5. Categorical comparisons supporting the structural-conformance claims of the paper — that conformance rates differ from a reference model and that *one-shot* demonstration reverses the Llama 3.2 family bias — were operationalized through **Fisher's exact test** on 2×2 contingency tables, complemented by **Wilson 95 % confidence intervals** for each observed proportion. Fisher's exact test was selected for four converging reasons: (i) the structural-conformance data is intrinsically binary (conformant vs. divergent); (ii) cells with extreme proportions (0/39 and 39/39) are observed, in which the asymptotic χ² approximation is invalid (expected frequency below 5 in at least one cell); (iii) the test produces exact two-sided *p*-values by combinatorial enumeration of more extreme tables, with no distributional assumption; and (iv) when a cell of the contingency table is zero, the conditional maximum-likelihood odds ratio is not finitely estimable, but the *p*-value derived from the exact hypergeometric distribution remains valid as the reportable effect, in line with standard practice for categorical comparisons under extreme proportion regimes.

Wilson 95 % CIs supplement each rate with its uncertainty band, computed analytically without assuming normality of the proportion — a property especially relevant near the extremes of the unit interval, where the normal approximation underlying the Wald interval would produce bounds outside [0, 1]. All inferential computations were performed with `scipy.stats.fisher_exact` (two-sided alternative) and a closed-form Wilson interval implementation, both reported in `src/inferential_statistics.py`. Significance is reported in APA-style notation throughout the paper: *p* < 0.001 ``***``, *p* < 0.01 ``**``, *p* < 0.05 ``*``, *p* ≥ 0.05 n.s., with α = 0.05 as the conventional rejection threshold.

## Appendix B — Implementation Details

This appendix documents the implementation artifacts referenced in Subsections 3.3 and 3.4. The materials are provided to support integral reproducibility of the study; the executable form, together with the raw inference corpus, is available in the public repository indicated in Section 3.9.

**B.1 — HTTP payload sent to Ollama.** All 312 main-protocol calls and the 80 falsification-protocol calls transported to the server a JSON payload structured in rigorously uniform fashion across models, schematically reproduced below:

```python
payload = {
    "model": <model identifier>,
    "messages": [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user",   "content": <scenario text>},
    ],
    "stream":  False,
    "format":  "json",
    "options": {"temperature": 0.2},
}
```

Each hyperparameter was selected by explicit methodological motivation and acts on a distinct dimension of the generation process's stochasticity:

1. **`temperature = 0.2`.** The parameter scales logits prior to *softmax* sampling and governs the concentration of the probability distribution over the vocabulary. Values close to 0 collapse the distribution into a near-deterministic regime (quasi-greedy prediction); values above 1 flatten it, favoring lexical diversity. The choice of 0.2 establishes a compromise: rigorous enough to induce adherence to the structural contract declared in natural language by the *system prompt*, without suppressing the micro-variability necessary for meaningful estimation of intra-model CV across repetitions. Values near 0 would render infeasible the differentiation of systemic versus stochastic variance — the central axis of the instruction-stability analysis.
2. **`stream = false`.** Deactivates the progressive *token-by-token* transmission regime (*server-sent events*) and imposes synchronous mode, in which the server retains the entire response until stopping and returns it in a single HTTP body. The justification is metrological: the *wall-clock* latency meter based on `time.time()` requires well-defined start and end points, and reception in a single chunk eliminates ambiguity about the inference termination moment. The synchronous mode is also the regime expected in real school usage, in which the student awaits the complete response before proceeding.
3. **`format = "json"`.** Signals to Ollama the intent of JSON output. Operationally, the server restricts the decoder to a logit mask compatible with tokens structurally valid for JSON, exerting probabilistic *nudging* over the generation. Critical methodological decision: this parameter **does not enforce a schema** — it merely guarantees that the output will be syntactically parseable as JSON, but **imposes nothing on field typology, presence of required keys, or list cardinality**. The choice to keep it active, without complementation by strict grammatical coercion (BNF grammars, regex validation, or *constrained decoding*), reflects the intent to gauge the model's **native adherence** to the structural contract specified in natural language, under conditions representative of the realistic school-deployment scenario — in which there are no engineering resources to implement layers of syntactic coercion over every inference.
4. **`timeout = 120` seconds.** Client-side waiting limit, dimensioned to accommodate even the most prolonged generations of verbose models without masking genuine server failures.

**B.2 — Source code of the `divergente()` structural validator.** The binary conformance classification of each response was performed by the deterministic function below — operationalized in `src/mine_benchmark.py` — that decides, over the raw content returned in `message.content`, whether the response integrally satisfies the contract declared in the *system prompt*. The classifier logic is reproduced in pseudocode, in the exact order of execution adopted over the 312-record corpus:

```python
def divergente(raw_response: str) -> bool:
    # C1 — JSON syntax
    try:
        parsed = json.loads(raw_response)
    except json.JSONDecodeError:
        return True

    # C2 — Root type
    if not isinstance(parsed, dict):
        return True

    # C3 — Type and cardinality of `pontos_fortes`
    pf = parsed.get("pontos_fortes")
    if not (isinstance(pf, str) and pf.strip()):
        return True

    # C4 — Type and cardinality of `perguntas_reflexivas`
    pr = parsed.get("perguntas_reflexivas")
    if not isinstance(pr, list) or len(pr) == 0 \
       or any(not isinstance(x, str) for x in pr):
        return True

    return False
```

The function operates on the raw content preserved in the `resposta_ia` attribute of each of the 312 records of the collection corpus. The four conditions (C1–C4) are documented in narrative form in Subsection 3.4.
