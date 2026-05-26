# A Diagnostic Evaluation of Small Language Models for Offline Socratic Tutoring in Brazilian Portuguese: A Study on Structural and Pedagogical Adherence under Public-School Infrastructure Constraints

---

**Randerson Oliveira Melville Rebouças** [ORCID: 0009-0005-3056-5074](https://orcid.org/0009-0005-3056-5074)

PhD Candidate, Graduate Program in Informatics in Education (PPGIE)
Federal University of Rio Grande do Sul (UFRGS) — Porto Alegre, RS, Brazil
`randerson.melville@gmail.com`

Advisor: Prof. Dr. Marcelo Magalhães Foohs (PPGIE/UFRGS) [ORCID: 0000-0002-4735-0732](https://orcid.org/0000-0002-4735-0732)
Co-advisor: Profa. Dra. Rosa Maria Vicari (PPGIE/UFRGS) [ORCID: 0000-0002-6909-6405](https://orcid.org/0000-0002-6909-6405)

---

## Abstract

The adoption of generative Artificial Intelligence in educational contexts has been predominantly anchored in proprietary models dependent on broadband connectivity, an assumption incompatible with the material reality of most Brazilian public schools. This work conducts a controlled diagnostic evaluation of eight open Small Language Models (SLMs), executed strictly in a local, offline environment, against a metalinguistic rubric derived from Ingedore Koch's Textual Linguistics. A total of 312 primary inference calls were performed (8 models × 13 canonical scenarios × 3 repetitions) without applying any external grammatical coercion mechanism, plus 80 additional calls across four falsification isolations directed at the most expressive architectural finding. Categorical comparisons are supported by Fisher's exact test (with odds ratio and 95 % CI). Results reveal two distinct failure regimes: (i) **zero-shot structural non-adherence**, manifested as 100 % typological divergence in the Llama 3.2 family (1 B and 3 B) and Phi-3 Mini — characterized, for the Llama 3.2 family, as a deterministic formatting bias inherited from instruction tuning for generalist commercial use, fully reversible by minimal in-context demonstration (*one-shot*), which distinguishes it from compositional incapacity of the model; and (ii) **pedagogical superficiality**, observed in Qwen 2.5 3B-Instruct — the only structurally conformant model in the deployable range under zero-shot — whose responses mobilize Koch's rubric terminology in only 46 % of scenarios. We conclude that contemporary off-the-shelf generalist models are insufficient for fine-grained Socratic tutoring in Brazilian Portuguese under zero-shot regime, justifying the development of specialized models through supervised fine-tuning on curated pedagogical corpora.

**Keywords:** Language Models; Basic Education; Brazilian Portuguese; Local Inference; Textual Linguistics; Diagnostic Evaluation.

---

## 1. Introduction

The incorporation of Large Language Models (LLMs) into educational contexts has constituted, over the past three years, one of the fastest-growing research fronts in Informatics in Education. The specialized literature documents promising results in the use of proprietary models such as GPT-4, Claude, and Gemini for conversational tutoring, automated essay scoring, and formative *feedback* generation (Kasneci et al., 2023; Tlili et al., 2023). This production, however, has been predominantly anchored in infrastructural assumptions — stable broadband access, no budget restriction for Application Programming Interface (API) calls, and contractual stability of foreign vendors — that **do not correspond to the material reality of most of the Brazilian public-school network**.

The historical TIC Educação series, conducted by the Regional Center for Studies on the Development of the Information Society (CGI.br/NIC.br/Cetic.br, 2024), evidences the persistence of profound connectivity inequalities between urban and rural Brazilian public schools, with a significant proportion of units operating without internet access adequate for synchronous pedagogical use. To this structural limit is added the issue of **student-data sovereignty**: the routine transmission of textual productions by underage students to commercial servers located in foreign jurisdictions configures a gray zone under the Brazilian General Data Protection Law (Brasil, 2018), particularly at its interface with the legal framework for child and adolescent protection.

This double encirclement — material connectivity precariousness and legal-ethical fragility of sensitive data traffic — imposes that the adoption of generative AI in the Brazilian public school contemplate, as an inescapable non-functional requirement, the **strictly local and offline** execution of inference models. The technical window for such an approach was opened by the recent proliferation of Small Language Models (SLMs) in the 1- to 4-billion parameter range, made viable by aggressive quantization (Q4, Q5) and by lightweight *runtimes* capable of executing inference over CPU on modest machines, without dependence on dedicated graphics acceleration (Abdin et al., 2024; Yang et al., 2024).

Recent literature on SLMs concentrates predominantly on general-purpose *benchmarks*, in English, and directed at mathematical reasoning or code generation tasks. It remains open, however, whether **open off-the-shelf models, executed locally under simulated public-school infrastructure conditions, are natively capable of operating as Socratic tutors of writing in Brazilian Portuguese**, respecting structured-output contracts and non-prescriptivist pedagogical principles. The present study addresses this gap through a controlled diagnostic evaluation of eight off-the-shelf SLMs against a rubric derived from the Textual Linguistics of Ingedore Koch (Koch, 2018; Koch, 2020), under a rigorously local inference environment and without any external grammatical coercion mechanism.

The central research question guiding this work is: *what is the degree of native adherence of contemporary open SLMs to a pedagogical-structural contract specified in natural language, and what failure patterns manifest at a statistically publishable scale?* The article is organized as follows: Section 2 reviews the relevant state of the art; Section 3 details the experimental methodology adopted, with a level of description sufficient for integral reproducibility of the study; Sections 4 and 5 present, respectively, results along the dimensions of efficiency and structural conformance; Section 6 conducts a qualitative analysis of pedagogical adherence in the best-classified model; and Section 7 synthesizes conclusions and outlines the subsequent agenda.

## 2. Related Work

Systematic evaluation of language models for educational tasks articulates across three research fronts relevant to the present study. The first front comprises studies on the use of proprietary LLMs as tutors and formative evaluators. Kasneci et al. (2023) synthesize opportunities and challenges of ChatGPT in basic education, identifying significant potential but warning against systemic biases and infrastructural dependence. Tlili et al. (2023) conduct a longitudinal case study on the pedagogical use of *chatbots*, highlighting tensions between student engagement and conceptual fidelity. This literature, however, operates predominantly under an assumption of continuous connectivity — a gap the present work addresses directly.

The second front corresponds to technical literature on SLMs viable for local execution. Abdin et al. (2024), describing Phi-3, posit the thesis of "small and capable models" through intensive training-data curation; Yang et al. (2024) present the Qwen 2.5 family, with emphasis on multilingualism; Grattafiori et al. (2024) and the Gemma team (Gemma Team, 2024) describe, respectively, the Llama 3 and Gemma 2 families in their lightweight variants. These references configure the candidate universe of the present *benchmark*, but their technical reports evaluate performance predominantly on Anglocentric *benchmarks* and mathematical tasks, with no specific coverage of pedagogical tutoring in Brazilian Portuguese.

The third front involves the emerging literature on **format bias** in models post-trained by preference. Zheng et al. (2023) and Wu and Aji (2023) demonstrate that human and model-judge evaluators exhibit systematic preference for long, listed, and well-formatted responses regardless of content quality, and that this reward signal becomes internalized in finalized models as a dominant attractor in the generation space. This theoretical body is mobilized, in Section 5, for the interpretation of the architectural findings of this study.

The intersection of these three fronts — educational application, local viability in Brazilian Portuguese, and post-training failure patterns — remains, to the best of this investigation's knowledge, under-explored. The present article contributes to fill this gap through controlled empirical diagnosis.

## 3. Methodology

This section describes, with a level of detail directed at integral reproducibility, the experimental protocol adopted. The subsequent subsections document, in order: (i) the local *offline* inference stack that emulates the school computational ceiling; (ii) the corpus of canonical scenarios and the metalinguistic rubric that anchors it; (iii) the sample matrix and HTTP hyperparameters transmitted on each call; (iv) the algorithmic architecture of the deterministic structural-conformance validator; (v) the inferential statistical framework applied to categorical comparisons; (vi) the criteria for metalinguistic pedagogical adherence; (vii) canonical examples of inputs and outputs observed in the corpus; (viii) the secondary falsification protocol; and (ix) reproducibility guarantees.

### 3.1 Computational Environment and Local Offline Inference Stack

The entirety of the 312 inference calls was conducted in a **strictly local and offline** environment, without any communication with remote services during the collection phase. The choice deliberately emulates the computational ceiling available in Brazilian public-school computer labs: execution over a Central Processing Unit (CPU), without dedicated Graphics Processing Unit (GPU) acceleration, and with a Random Access Memory (RAM) restriction compatible with the typical installed base of school machines (8 GB range).

The inference orchestrator adopted was **Ollama**, a local HTTP server running on the *loopback* interface (`localhost:11434`). Calls were made via synchronous POST requests to the `/api/chat` endpoint, with `Content-Type: application/json` header, in the client–server communication pattern natively exposed by the *runtime*. Models were instantiated in Ollama's default quantization — `Q4_K_M` for most architectural families evaluated — a format compatible with the 8 GB RAM limit and widely disseminated in modest-hardware local inference implementations. The client layer was developed in Python 3.11 using the `requests` library for HTTP transport and the `json` module of the standard library for serialization and deserialization of payloads.

### 3.2 Evaluation Instrument: Scenario Corpus and Metalinguistic Rubric

The evaluation rubric was derived from Koch's (2018, 2020) taxonomy of textual cohesion, operationalized in **thirteen canonical scenarios** drafted by a specialist in Textual Linguistics. Each scenario consists of a short writing text in the school discursive genre (review, summary, retelling, opinion piece, chronicle), attributed to a hypothetical lower-secondary student (8th and 9th grades), and deliberately conveys a target cohesive phenomenon to be identified and problematized by the automated tutor. The taxonomy spans two axes:

- **Referential Cohesion**: ambiguity through inadequate pronominalization; excessive lexical repetition with suppression of ellipsis and substitution by hypernym or pro-form;
- **Sequential Cohesion**: contradictory use of argumentative operators; disorganization of temporal and spatial markers; extreme juxtaposition of clauses without establishment of logical-semantic relations.

Each model received a canonical *system prompt*, identical across all experiments — ensuring strict control of variable — that defines: (i) the model's role as Socratic tutor for 8th–9th grade students of the Brazilian public school; (ii) five non-negotiable pedagogical constraints (do not provide a ready answer; do not rewrite the corrected text; value linguistic varieties and orality marks without acting as a "grammar police"; focus on cohesion and coherence per Koch; bridge with Computational Thinking when appropriate); and (iii) the output format strictly specified as a JSON object with exactly two keys — `pontos_fortes` (type `string`, monolithic) and `perguntas_reflexivas` (type `array` of `string`, with a pair of elements exemplified in the canonical schema). Keys are preserved verbatim in Brazilian Portuguese since they constitute the literal contract sent on every API call.

### 3.3 Experimental Protocol: Sample Matrix and Inference Hyperparameters

The sample matrix comprised **eight distinct language models**, distributed across two ranges:

- **Deployable range (analytical center of the study):** `qwen2.5:1.5b-instruct`, `qwen2.5:3b-instruct`, `llama3.2:1b`, `llama3.2:3b`, `gemma2:2b`, and `phi3:mini` (3.8 B). The delimitation at up to 3.8 billion parameters corresponds to the memory envelope executable in Q4 quantization within the 8 GB RAM target.
- **Reference ceiling (upper *baseline*):** `llama3:8b` and `gemma2:9b`. These models are not deployment candidates, included as comparative references of attainable quality by the same architectural family at larger scales.

Each model × scenario pair was submitted to **three independent repetitions** (n = 3), totaling 8 × 13 × 3 = **312 inference calls**. Triple replication enables estimation of standard deviation and coefficient of variation (CV = σ/μ) intra-model — indispensable metrics to distinguish expected stochastic variability, deriving from the sampling parameter `temperature`, from systemic instruction instability.

**HTTP payload sent to Ollama.** The entirety of the calls transported to the server a JSON payload structured in rigorously uniform fashion across models, described schematically below:

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

### 3.4 Structural Validation Architecture: The `divergente()` Algorithm

The binary conformance classification of each response was performed by a deterministic function — operationalized in `mine_benchmark.py` — that decides, over the raw content returned in `message.content`, whether the response integrally satisfies the contract declared in the *system prompt*. The classifier logic is reproduced in pseudocode below, in the exact order of execution adopted over the corpus:

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

The four deterministic conditions operate as disjoint filters — violation of any one suffices for the divergence classification. The typological rationale of each condition is detailed below:

- **C1 — JSON syntax.** The first barrier ensures the returned string constitutes a valid JSON document per the ECMA-404 specification. Failures at this level indicate that the model's decoder did not respect even the tokenized regime induced by Ollama's `format = "json"` parameter — a rare occurrence, but registered in extreme cases.
- **C2 — Root is object.** Restricts the outer structure to a nominal *mapping* (JSON object). The declared contract prescribes an object with two named keys, and the typical violation at this level would occur via return of an *array* at the root (list of objects), a pattern inherited from tabular or batch output regimes — incompatible with the individual tutoring interface.
- **C3 — `pontos_fortes` is monolithic non-empty string.** The canonical schema declared in the *system prompt* exemplifies `pontos_fortes` as continuous prose, oriented to Socratic welcoming of the student through recognition of the merits of the text produced. Any typological deviation — particularly return as a *bullet* list — is flagged as divergent. The pedagogical rationale is direct: substituting prose with enumeration shifts the register from welcoming feedback to corrective evaluation, transforming the tutor into a test grader, in direct violation of the "do not act as grammar police" directive.
- **C4 — `perguntas_reflexivas` is non-empty list of strings.** The contract explicitly declares the `array` of `string` type and exemplifies a minimum pair of items. The implemented validator adopts the permissive criterion of cardinality ≥ 1, granting the benefit of the doubt to the model in cases of degeneration to a single item; in all cases where divergence manifested here, it involved the appearance of a type distinct from `string` (nested objects, `null` values), rather than merely the count of elements.

The function operates on the raw content preserved in `resposta_ia`, an attribute of each of the 312 records of the collection corpus. The choice for a deterministic classifier, rather than evaluation by a judge model, was deliberate: structural conformance is a syntactic-typological property decidable in finite time by type inspection, with no room for interpretive subjectivity, and delegation to an LLM judge would introduce undesired variance precisely on the dimension where the study seeks maximal objectivity.

### 3.5 Inferential Statistical Framework

To support the three categorical claims of the paper — that conformance rates differ between models, that intra-family divergence patterns are non-random, and that one-shot demonstration reverses the Llama 3.2 family bias — comparisons were operationalized through **Fisher's exact test** on 2×2 contingency tables. Fisher's exact test was selected as the workhorse inferential procedure for four converging reasons: (i) the structural-conformance data is intrinsically binary (conformant vs. divergent); (ii) cells with extreme proportions (0/39 and 39/39) are observed, in which the asymptotic χ² approximation is invalid (expected frequency below 5 in at least one cell); (iii) the test produces exact two-sided *p*-values by combinatorial enumeration of more extreme tables, with no distributional assumption; and (iv) it admits a natural effect-size measure — the conditional maximum-likelihood odds ratio (OR) with 95 % confidence interval by the Cornfield method — directly publishable alongside the *p*-value. All categorical comparisons reported in Sections 5.1, 5.2, and 5.3 of this article follow this framework, computed via the `scipy.stats.fisher_exact` implementation. Latency data, by contrast, are reported descriptively only (Section 4), as the empirical separation between model classes is evident at the order-of-magnitude scale and does not require inferential support for interpretation.

### 3.6 Analysis Criteria: Efficiency and Metalinguistic Pedagogical Adherence

**Computational efficiency.** Latency was measured in *wall-clock* via `time.time()` in Python, including the entire local I/O stack between client and Ollama server. For each model, the following were computed: mean, standard deviation, median (p50), 95th percentile (p95), minimum, and maximum, in milliseconds. The coefficient of variation (CV) operates as a dimensionless measure of stability across repetitions. Input and output token counters were obtained from Ollama's native telemetry (`prompt_eval_count` and `eval_count`), preserving fidelity of the measure relative to each model's specific tokenizer.

**Metalinguistic pedagogical adherence.** For the model best classified along the dimensions of efficiency and structural conformance, additional qualitative inspection was conducted, verifying the presence, in the response text, of terms from Koch's metalinguistic taxonomy — cohesion, connector, pronoun, referential, sequential, ambiguity, repetition, synonym, ellipsis, argumentative operator, temporal marker, juxtaposition. The presence of at least one rubric term was considered a minimum indication of metalinguistic adherence; its absence classifies the response as operating in an exclusively thematic-surface layer.

### 3.7 Anatomy of Outputs: Canonical Examples from the Corpus

To expose the nature of the contracts evaluated, this subsection illustrates, with literal material extracted from the corpus, the cohesive deviation embedded in a representative scenario, one conformant output, and two distinct modalities of divergent output.

**Input — scenario 1 (Referential Cohesion: excessive lexical repetition).** Synthetic text attributed to a hypothetical student, extracted literally from the canonical thirteen-scenario corpus (preserved in Brazilian Portuguese as the object of linguistic study):

> Resenha sobre A Cartomante: A cartomante falou pro Camilo que tava tudo bem. A cartomante leu as cartas. A cartomante sorriu pra ele. A cartomante deu certeza pra ele. Depois o Camilo foi pra casa do Vilela e morreu. A cartomante tinha errado tudo.

*English gloss (provided for non-Lusophone readers; not part of the experiment):* Review of "The Fortune-Teller": The fortune-teller told Camilo everything was fine. The fortune-teller read the cards. The fortune-teller smiled at him. The fortune-teller gave him certainty. Then Camilo went to Vilela's house and died. The fortune-teller had got it all wrong.

The embedded target phenomenon is the lexical repetition of the noun phrase *"a cartomante"* in four consecutive clauses — a paradigmatic case of referential cohesion through repetition, in which the tutor would be expected to induce the student toward substitution by pronominal pro-form or hypernym, leading them to reflect on the referential chain without providing the corrected form outright.

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

## 4. Results of Computational Efficiency

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

## 5. Results of Structural Conformance and Architectural Findings

The dimension of conformance to the structural contract specified in natural language — requirement of a JSON object with keys `pontos_fortes` (type `string`) and `perguntas_reflexivas` (type `array` of `string`) — produces the most expressive finding of this study. Table 2 consolidates the divergence rates observed.

**Table 2.** Structural divergence rate per model (n = 39 calls).

| Model | Divergence |
|---|---:|
| `qwen2.5:3b-instruct` | 0 % (0/39) |
| `gemma2:9b` | 0 % (0/39) |
| `llama3:8b` | 0 % (0/39) |
| `qwen2.5:1.5b-instruct` | 2.6 % (1/39) |
| `gemma2:2b` | 2.6 % (1/39) |
| `llama3.2:1b` | **100 % (39/39)** |
| `llama3.2:3b` | **100 % (39/39)** |
| `phi3:mini` | **100 % (39/39)** |

The distribution is clearly bimodal: five models exhibit integral or near-integral adherence (0–2.6 %), while three models collapse entirely (100 %), with no intermediate instances. Such polarization suggests that conformance to the contract **is not a monotonic function of the parameter count**, but rather an architectural-behavioral property of the family and of the instruction-tuning regime.

### 5.1 The Family Failure of the Llama 3.2 Line

Qualitative inspection of the outputs of the two Llama 3.2 variants (1 B and 3 B) reveals a rigorously identical failure pattern: the emitted JSON is, across all 78 calls, syntactically valid and parseable; divergence manifests exclusively as a **typological violation** of the `pontos_fortes` field, returned consistently as an *array* of *strings* (typically enumerating two to four items) in place of the specified monolithic `string` type. The perfect symmetry between the two family sizes — in parallel with the full conformance of the Qwen 2.5 family at analogous sizes under identical *prompt* — rules out hypotheses of insufficient capacity or stochasticity and displaces the explanation toward post-training.

The pairwise comparison between families under matched scale, by Fisher's exact test, yields statistical separations of extreme magnitude: Llama 3.2 1B vs. Qwen 2.5 1.5B (0/39 vs. 38/39 conformant; Fisher exact two-sided *p* < 10⁻¹⁵); Llama 3.2 3B vs. Qwen 2.5 3B (0/39 vs. 39/39 conformant; *p* < 10⁻¹⁵); Llama 3.2 3B vs. Gemma 2 2B (0/39 vs. 38/39 conformant; *p* < 10⁻¹⁵). The cross-family separation, at matched scale, is therefore not a borderline result subject to interpretation: it is one of the most categorical statistical contrasts observable in 2×2 categorical experimentation. The odds ratio is formally degenerate due to zero cells — the conditional maximum-likelihood estimate is undefined when conformance frequency reaches an extreme of the support — but the *p*-value alone, derived by exact combinatorial enumeration, suffices to falsify the null hypothesis of homogeneous conformance rates between families at any conventional significance threshold.

This pattern finds coherent interpretation in light of the literature on **format bias** in preference-post-trained models. Zheng et al. (2023) and Wu and Aji (2023) document that implicit format-based rewards — operating either through human evaluators or judge models — induce systematic inflation of stylistic markers such as lists, *bullet points*, bold headings, and enumerations, at the expense of *prompt* fidelity. The operational motivation of this bias is direct: responses structured as marked items are perceived as more professional and readable by human evaluators in general-purpose assistant interfaces, and the reward signal internalizes this preference as a dominant attractor in the generation space.

Liu et al. (2025), in the framework of **GuideEval**, offer the behavioral-theoretical complement necessary to the interpretation of the finding: the framework decomposes the tutorial competence of a model into three distinct phases — Perception of the student's cognitive state, Orchestration of the tutorial response, and Elicitation of reflection — and demonstrates that failures in the Orchestration phase typically manifest as rigidity toward format instruction, with the model retreating to output patterns strongly entrenched in post-training. In terms of Liu et al.'s scheme, the anomaly observed in the Llama 3.2 line is precisely an Orchestration failure: the model *perceives* the task correctly (assisting the student) and *would elicit* questions, but the intermediate stage of behavioral modulation of the response collapses to the enumeration attractor conditioned by its generalist post-training. The present study contributes to the literature on two aspects. **First**, it demonstrates that the formatting bias is **resistant to explicit counter-specification in natural language under zero-shot regime**: the *system prompt* univocally declares the expected type, and yet the enumeration attractor prevails in 100 % of the calls. **Second**, it evidences that the bias constitutes an **architectural signature consistent across scales** of the same family — a fact that suggests the origin of the phenomenon in the institutional post-training procedure adopted by the team responsible for the 3.2 line, rather than in particularities of an isolated *checkpoint*. The operational implication, however, requires the rigorous qualification provided by Subsection 5.3: in the absence of external syntactic coercion **and under pure zero-shot regime** — the standard conditions of most economically viable educational deployments —, the Llama 3.2 family is not deployable as structured-tutoring infrastructure in Brazilian Portuguese; under minimal contextual anchoring by demonstration (*one-shot*), however, conformance is fully recovered, which reclassifies the finding as a **reversible zero-shot bias** rather than as the model's categorial compositional incapacity.

### 5.2 The Multidimensional Collapse of Phi-3 Mini

The failure of `phi3:mini` is qualitatively distinct and more severe. Analysis of the outputs reveals that the model not only typologically violates the `pontos_fortes` field — emitted in 100 % of calls as an *array* —, but **entirely replaces the declared schema** with its own structure, built around unsolicited fields `erro`, `correção`, `texto_original`, and `texto_proposto`. Additionally, 20.5 % of calls present `perguntas_reflexivas` as `NoneType` or composed of nested non-*string* elements, configuring progressive deterioration of contract fidelity as generation advances. The pairwise comparison Phi-3 mini vs. Qwen 2.5 3B (Fisher exact two-sided: 0/39 vs. 39/39; *p* < 10⁻¹⁵) and Phi-3 mini vs. Llama 3 8B (Fisher exact two-sided: 0/39 vs. 39/39; *p* < 10⁻¹⁵) confirm that Phi-3's separation from the structurally adherent models is statistically of the same magnitude as the Llama 3.2 family's separation, justifying its analytical bracketing in the same regime of zero-shot non-adherence.

More grave, however, is the **pedagogical inversion** of the *prompt*: the model, trained predominantly on English-language corpora for general-purpose assistant use cases, assumes a corrective-prescriptivist posture in flagrant violation of the explicit directive of the *system prompt* — "value linguistic varieties and orality marks" —, producing, for instance, outputs in which it classifies the legitimate colloquialism *"tava"* as an error to be corrected to *"estava"* and, in sequence, **hallucinates a non-existent grammatical rule** by prescribing the form *"lera"* (pluperfect) as replacement for the form *"leu"* (simple past), correctly employed by the student.

This double-violation pattern — structural and pedagogical — confirms the general hypothesis of Wu and Aji (2023) on the imperfect transferability of instruction habits across distinct linguistic-pragmatic domains. The model, optimized for an Anglocentric conversational regime in which explicit correction is virtuous, transports this habit into a pedagogical-linguistic context in Brazilian Portuguese in which it is harmful, and does so even under counter-instruction in natural language. The combination observed in Phi-3 — structural collapse, pedagogical inversion, temporal instability, and quadruple verbosity relative to peers — configures a testimonial case of the transferability limit of Anglocentric SLMs to educational tasks in Brazilian Portuguese, even when the model is nominally declared multilingual by its developers.

The phenomenon of Phi-3's inflated verbosity — 471 mean tokens against the 104 to 145 range of the other models — additionally finds echo in **MathTutorBench** by Macina et al. (2025), which systematizes, in an adjacent domain (mathematical tutoring), the finding that off-the-shelf models tend to superimpose thematic expertise over pedagogical competence, transforming the tutorial act into an extended expository monologue rather than brief oriented maieutics. Phi-3's verbal excess observed in this study is therefore not a particularity of tokenization or instance noise — it is a local manifestation of a systemic pattern of post-trained generalist models, which conflate output volume with tutorial quality, in direct prejudice of the focal and dialogic regime that defines Socratic maieutics (Paul; Elder, 2007).

### 5.3 Robustness Analysis of the Llama 3.2 Architectural Finding via Controlled Counter-Experiment

The perfect uniformity of divergence observed in the Llama 3.2 family — 78 calls, two architectural sizes, zero conformant responses in the main protocol — imposes, by sound scientific practice, deliberate examination of competing hypotheses that would reduce the finding to an instrumental artifact before sustaining it as a behavioral signature of the model. To this end, the secondary protocol described in Subsection 3.8 was integrally executed, totaling 80 additional calls under the same local inference stack. Table 3 synthesizes the outcomes.

**Table 3.** Structural conformance rate of the Llama 3.2 family under falsification isolations.

| Isolation | Experimental condition | Llama 3.2 1B | Llama 3.2 3B |
|---|---|---:|---:|
| Baseline | `temperature = 0.2`, zero-shot (main protocol) | 0/39 (0.0 %) | 0/39 (0.0 %) |
| **E1** | `temperature = 0.0`, zero-shot | 0/13 (0.0 %) | 0/13 (0.0 %) |
| **E2** | `temperature = 0.2`, *one-shot* in-context | **11/12 (91.7 %)**¹ | **12/12 (100.0 %)** |
| **E2b** | `temperature = 0.0`, *one-shot* in-context | **9/12 (75.0 %)**² | **12/12 (100.0 %)** |
| **E3** | Identical payload via `curl`, outside Python layer | 1/1 (typological failure reproduced) | 1/1 (typological failure reproduced) |

¹ The single non-conformance of the 1B in E2 derives from HTTP *timeout*, not from a structural violation of the response actually returned. ² Idem for 3/12 of the 1B in E2b — timeouts associated with the context-budget increase introduced by the demonstrative pair of *one-shot*, with no implication on the typological conformance of the completed calls.

The joint reading of the four isolations sustains three interlinked conclusions, of falsificationist nature, on the nature of the finding.

**First conclusion — the bias is deterministic, not stochastic.** In E1, the complete suppression of sampling variability by `temperature = 0.0` produces no conformance; on the contrary, the 3B model converges to the structural attractor `pontos_fortes = list[str], cardinality = 2` in 12 of the 13 scenarios, exhibiting the near-degeneration profile typical of bias encoded in the weight space. Hypotheses that would attribute divergence to sampling noise or instability across repetitions are therefore falsified.

**Second conclusion — the bias is in the model, not in the client stack.** In E3, transmission of the same JSON payload to the Ollama endpoint via `curl`, eliminating any mediation by the Python `requests` library, integrally reproduces the typological-divergence pattern observed in the main protocol — `pontos_fortes` returned as a list, JSON syntactically valid, other keys consistent. Hypotheses that would attribute divergence to interference of the client transport layer, HTTP headers, payload encoding, or `messages` array serialization are therefore falsified.

**Third conclusion — the bias is one of zero-shot obedience, not of compositional incapacity.** In E2, the precedence of a single `user`/`assistant` pair exhibiting the canonical gold response for scenario 1 produces total reversal of divergence: the 3B model reaches 12/12 conformance in the twelve subsequent scenarios, and the 1B model reaches 11/12 (with the single exception attributable to transport *timeout*, not format failure). The stability of this reversal is confirmed in E2b, in which the combination of *one-shot* with `temperature = 0.0` preserves 100 % conformance in the 3B. The reversal is corroborated by Fisher's exact test on the 2×2 condition-by-conformance contingency: for Llama 3.2 3B, zero-shot baseline (0/39 conformant) versus *one-shot* condition (12/12 conformant) yields Fisher exact two-sided *p* = 6.3 × 10⁻¹²; for Llama 3.2 1B, baseline (0/39) versus *one-shot* (11/11 conformant, excluding one HTTP timeout) yields *p* = 2.7 × 10⁻¹¹. The epistemic inference is direct: the Llama 3.2 family models **possess the compositional capacity** to produce `pontos_fortes` as monolithic string respecting the declared schema; what is compromised is obedience to this specification when provided exclusively in natural language under zero-shot regime, without contextual demonstration. The enumeration attractor is dominant only in the absence of a contrary demonstrative anchor.

This set of conclusions repositions the Subsection 5.1 finding with added precision. The Llama 3.2 family does not exhibit categorial incapacity to operate as a structured tutor — it exhibits a **reversible zero-shot bias**, in the strict sense of Liu et al. (2025): failure in the Orchestration phase of the tutorial response when the operational regime does not provide a demonstrative reference, with full recovery when such reference is provided. This characterization has three implications:

1. **Methodological implication for the paper.** The choice of `qwen2.5:3b-instruct` as base model for subsequent pedagogical fine-tuning remains justified — among the models evaluated, it is the only one conformant under zero-shot, and zero-shot is the regime of lowest engineering cost in the classroom. But the justification is no longer "Llama 3.2 is not deployable" and becomes "Qwen 2.5 3B is the only one that dispenses additional prompting engineering to guarantee structural contract".
2. **Operational implication for alternative deployments.** A valid intermediate route is established for schools or municipal networks that, for pedagogical or technical-sovereignty reasons, prefer the Llama 3.2 family: the additional engineering cost consists of keeping a ~300-token demonstrative pair in the context per call, a moderate budget increase but with an observable latency penalty, as registered by the *timeouts* in E2/E2b over the 1B.
3. **Implication for the literature on format bias.** The present study contributes controlled experimental evidence that the bias documented by Zheng et al. (2023), Wu and Aji (2023), and Liu et al. (2025) **is not absolute**: it is a function of the operational regime adopted. This empirical refinement, derived from a directed falsification protocol, offers a basis for future studies on the computational economy of educational *prompt engineering* as a mitigator of post-training bias in off-the-shelf SLMs.

### 5.4 Synthesis of Inferential Comparisons

Table 4 consolidates the seven Fisher's exact test outcomes referenced throughout Subsections 5.1–5.3, for unified reviewer consultation. All comparisons are two-sided. *p*-values reported as *p* < 10⁻¹⁵ correspond to outcomes below the floating-point precision floor of the SciPy implementation employed; the actual exact probability, derived by combinatorial enumeration, is below this threshold by orders of magnitude.

**Table 4.** Synthesis of pairwise Fisher exact tests on 2×2 conformance contingencies.

| # | Comparison | Group A (conf./n) | Group B (conf./n) | Fisher exact *p* (two-sided) |
|---|---|---:|---:|---:|
| F1 | Llama 3.2 1B vs. Qwen 2.5 1.5B | 0 / 39 | 38 / 39 | *p* < 10⁻¹⁵ |
| F2 | Llama 3.2 3B vs. Qwen 2.5 3B | 0 / 39 | 39 / 39 | *p* < 10⁻¹⁵ |
| F3 | Llama 3.2 3B vs. Gemma 2 2B | 0 / 39 | 38 / 39 | *p* < 10⁻¹⁵ |
| F4 | Phi-3 mini vs. Qwen 2.5 3B | 0 / 39 | 39 / 39 | *p* < 10⁻¹⁵ |
| F5 | Phi-3 mini vs. Llama 3 8B | 0 / 39 | 39 / 39 | *p* < 10⁻¹⁵ |
| F6 | Llama 3.2 1B: zero-shot baseline vs. *one-shot* (E2) | 0 / 39 | 11 / 11 | *p* = 2.7 × 10⁻¹¹ |
| F7 | Llama 3.2 3B: zero-shot baseline vs. *one-shot* (E2) | 0 / 39 | 12 / 12 | *p* = 6.3 × 10⁻¹² |

The seven tests jointly sustain the inferential framework of the paper: the four cross-family architectural separations (F1–F5) reject homogeneous-conformance nulls at any conventional threshold and identify the Llama 3.2 and Phi-3 families as statistically distinguishable from the structurally conformant population; the two paired-condition reversals (F6–F7) reject the null of zero-shot–invariance for the Llama 3.2 family and statistically corroborate the reclassification of its divergence as a reversible obedience bias. The conditional maximum-likelihood odds ratio is degenerate in all seven contrasts due to zero cells in the contingency tables; the exact *p*-value alone constitutes the reportable effect, in line with standard practice for categorical comparisons under extreme proportion regimes.

## 6. Qualitative Analysis: Pedagogical Adherence of the Conformant Model

The joint reading of Sections 4 and 5 isolates `qwen2.5:3b-instruct` as the unique configuration among the *deployable* models simultaneously satisfying all non-functional requirements: mean latency of 2.906 s (below the HCI threshold), controlled variability (CV = 19.0 %), and full adherence (0/39) to the JSON contract without recourse to external coercion. This result, however, **does not authorize optimistic inference about the model's pedagogical adequacy**, as demonstrated in the additional qualitative inspection below.

Applying the metalinguistic criterion described in Subsection 3.6 to the 13 responses of the first repetition of `qwen2.5:3b-instruct`, it is observed that **only 6 of 13 responses (46.2 %) mobilize any terminology of the cohesion taxonomy** — pronominalization, lexical repetition, connective, argumentative operator, temporal marker, juxtaposition. In the seven remaining scenarios (53.8 %), the model shifts the interlocution to the **thematic-narrative plane of the literary work cited** by the student (characters, plot, setting), commenting elements of the literary source rather than evaluating the textuality of the production. As an illustration, the response to the scenario on Referential Cohesion — in which the student text repeats eight times the noun phrase *"a cartomante"* across four consecutive sentences — merely observes "good structure, clear beginning, and conclusion that highlights the importance of reading", without any mention of the excessive lexical repetition that constituted the target phenomenon of the scenario.

This constitutes a **categorial task failure**: the model conflates *what the student wrote* with *what the student wrote about*, and loses the central pedagogical object of the Socratic intervention oriented by metalinguistic rubric. Even in scenarios in which some taxonomy term is evoked, the approach is predominantly declarative — the model *names* the linguistic phenomenon without leading the student to *reflect* on how it operates in the produced text, contradicting the dialogic Socratic structure prescribed by the rubric (Paul; Elder, 2007).

The reading of this finding finds direct theoretical support in **MathTutorBench** by Macina et al. (2025), which documents, in an adjacent educational domain, the existence of a **systematic trade-off between thematic expertise and pedagogical competence** in off-the-shelf models: the same model capable of correctly discussing the content of a literary work or problem tends to fail as a tutor when faced with the task of leading the student through progressive questioning, retreating to an expository-thematic regime. The behavior here observed in `qwen2.5:3b-instruct` is a local manifestation of this phenomenon: the model is proficient at conversing *about* "A Cartomante" as a literary work — produces reasonable commentary on structure, reading, and plot — but fails to sustain the metalinguistic-Socratic stance that would reposition the focus on the student's text as a linguistic artifact open to problematization in light of Koch's taxonomy. Complementarily, the GuideEval framework of Liu et al. (2025) categorizes this failure mode as joint deficiency in the Perception phases (the model does not detect the target cohesive phenomenon) and Elicitation (even when it detects, it does not conduct questioning that makes the student operate on the text itself), confirming that adherence to format and pedagogical adequacy constitute logically independent dimensions of a model's tutorial competence.

## 7. Conclusion

This study conducted a controlled diagnostic evaluation of eight open Small Language Models, executed locally under infrastructure restrictions compatible with the material reality of the Brazilian public school, against a metalinguistic rubric derived from the textual-cohesion taxonomy of Ingedore Koch. The structural-conformance dimension produced a sharp result: among models in the *deployable* range (up to 3.8 billion parameters), only **Qwen 2.5 3B-Instruct** combines integral adherence to the JSON contract declared in natural language, mean latency comfortably situated below the Human–Computer Interaction threshold for synchronous tasks, and low variability across repetitions — constituting the only evaluated configuration that simultaneously satisfies, without recourse to external grammatical coercion, all non-functional requirements for educational deployment.

The reading of this result, however, does not authorize optimistic inference about the model's pedagogical adequacy. Systematic qualitative inspection of responses evidences that, although structurally conformant, the model presents **partial and unstable adherence to Koch's metalinguistic rubric**, mobilizing it in only 46 % of scenarios and operating predominantly in a thematic-surface layer in the remaining 54 %.

This finding, articulated with the architectural findings discussed in Section 5 and the falsification protocol reported in Subsection 5.3, sustains the central conclusion of the study: **the open language models contemporaneously available off-the-shelf, within their range of computational viability for Brazilian public schools, are insufficient for the task of Socratic tutoring of writing in Brazilian Portuguese grounded in a fine metalinguistic rubric, under zero-shot regime**. The insufficiency manifests in two distinct regimes: (i) **regime of zero-shot structural non-adherence**, exhibited by the Llama 3.2 and Phi-3 families, in which the model violates the syntactic-typological contract even under explicit natural-language specification — characterized, in the case of the Llama 3.2 family, by an obedience bias demonstrably reversible via minimal contextual anchoring (*one-shot*), and therefore distinguishable from compositional incapacity; and (ii) **regime of structural adherence with pedagogical superficiality**, exemplified by Qwen 2.5 3B-Instruct, in which the model respects the format but operates predominantly in a thematic-surface layer, without systematically mobilizing the theoretical taxonomy required by the task.

The simultaneous persistence of these two failure regimes — across models from architecturally distinct families, trained by diverse institutions, and optimized for predominantly Anglophone markets — converges to the diagnosis that the task of Socratic tutoring in Brazilian Portuguese for basic education **is not addressed in zero-shot regime by off-the-shelf generalist models** and demands, as necessary scientific unfolding, the development of **specialized models through supervised fine-tuning on curated pedagogical corpora in Brazilian Portuguese**, aligned with the metalinguistic rubric specific to the school domain. The alternative route via *prompt engineering* with demonstrative anchoring, made viable by the reversibility documented in Subsection 5.3, remains technically available, but presupposes an operational regime whose costs in context budget and latency must be weighed against the savings obtained in training. Such unfolding, outside the scope of the present diagnosis, constitutes the subsequent research agenda of this investigation.

## Acknowledgments

The author thanks his advisor, Prof. Dr. Marcelo Magalhães Foohs, and his co-advisor, Profa. Dra. Rosa Maria Vicari, both at the Graduate Program in Informatics in Education (PPGIE) of the Federal University of Rio Grande do Sul (UFRGS), for their guidance throughout this investigation. The author also thanks PPGIE/UFRGS for institutional support and the Coordination for the Improvement of Higher Education Personnel (CAPES) for the doctoral scholarship funding.

---

## References

ABDIN, M. et al. **Phi-3 Technical Report: A Highly Capable Language Model Locally on Your Phone**. arXiv:2404.14219, 2024. Available at: https://arxiv.org/abs/2404.14219.

BRASIL. **Lei nº 13.709, de 14 de agosto de 2018**. Brazilian General Data Protection Law (LGPD). Brasília, DF: Presidency of the Republic, 2018.

CARD, S. K.; ROBERTSON, G. G.; MACKINLAY, J. D. The information visualizer, an information workspace. In: **Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (CHI '91)**. New Orleans: ACM Press, 1991. p. 181–186.

CGI.br/NIC.br/Cetic.br. **Survey on the use of information and communication technologies in Brazilian schools: TIC Educação 2023**. São Paulo: Brazilian Internet Steering Committee, 2024.

GEMMA TEAM (Google DeepMind). **Gemma 2: Improving Open Language Models at a Practical Size**. arXiv:2408.00118, 2024. Available at: https://arxiv.org/abs/2408.00118.

GRATTAFIORI, A. et al. **The Llama 3 Herd of Models**. arXiv:2407.21783, 2024. Available at: https://arxiv.org/abs/2407.21783.

KASNECI, E. et al. ChatGPT for good? On opportunities and challenges of large language models for education. **Learning and Individual Differences**, v. 103, 102274, 2023. DOI: 10.1016/j.lindif.2023.102274.

KOCH, I. G. V. **A coesão textual** [Textual cohesion]. 22. ed. São Paulo: Contexto, 2018. [1st edition: 1989]

KOCH, I. G. V. **Introdução à linguística textual: trajetória e grandes temas** [Introduction to textual linguistics: trajectory and great themes]. 2. ed. São Paulo: Contexto, 2020.

KOCH, I. G. V.; ELIAS, V. M. **Escrever e argumentar** [Writing and arguing]. São Paulo: Contexto, 2016.

LIU, Y.; LI, C.; ZHANG, T.; WANG, M.; ZHU, Q.; LI, J.; HUANG, H. **Discerning Minds or Generic Tutors? Evaluating Instructional Guidance Capabilities in Socratic LLMs**. arXiv:2508.06583, 2025. Available at: https://arxiv.org/abs/2508.06583.

MACINA, J.; DAHEIM, N.; HAKIMI, I.; KAPUR, M.; GUREVYCH, I.; SACHAN, M. MathTutorBench: A Benchmark for Measuring Open-ended Pedagogical Capabilities of LLM Tutors. In: **Proceedings of EMNLP 2025**. Singapore: ACL, 2025. Preprint: arXiv:2502.18940. Available at: https://arxiv.org/abs/2502.18940.

NIELSEN, J. **Usability Engineering**. San Francisco: Morgan Kaufmann, 1993.

PAUL, R.; ELDER, L. Critical Thinking: The Art of Socratic Questioning. **Journal of Developmental Education**, v. 31, n. 1, p. 36–37, 2007.

TLILI, A. et al. What if the devil is my guardian angel: ChatGPT as a case study of using chatbots in education. **Smart Learning Environments**, v. 10, n. 1, art. 15, 2023. DOI: 10.1186/s40561-023-00237-x.

WU, M.; AJI, A. F. **Style Over Substance: Evaluation Biases for Large Language Models**. arXiv:2307.03025, 2023. Available at: https://arxiv.org/abs/2307.03025.

YANG, A. et al. (Qwen Team). **Qwen2.5 Technical Report**. arXiv:2412.15115, 2024. Available at: https://arxiv.org/abs/2412.15115.

ZHENG, L. et al. Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. In: **Advances in Neural Information Processing Systems 36 (NeurIPS 2023)**. New Orleans: 2023.
