"""Fisher exact tests on 2x2 contingency tables for the SLM benchmark.

Runs all pairwise categorical comparisons needed to support the paper claims:
- Cross-family divergence rates (matched scale)
- Phi-3 vs structurally conformant models
- Zero-shot vs one-shot conformance within Llama 3.2

Outputs:
  analises/inferential_results.json  (machine readable)
  stdout summary in publication-ready format
"""
import json
from pathlib import Path
from scipy.stats import fisher_exact

ROOT = Path(__file__).resolve().parent.parent


def divergent(raw_response: str) -> bool:
    """Mirror of mine_benchmark.py's classifier."""
    if not raw_response:
        return True
    try:
        parsed = json.loads(raw_response)
    except json.JSONDecodeError:
        return True
    if not isinstance(parsed, dict):
        return True
    pf = parsed.get("pontos_fortes")
    if not (isinstance(pf, str) and pf.strip()):
        return True
    pr = parsed.get("perguntas_reflexivas")
    if not isinstance(pr, list) or len(pr) == 0 \
       or any(not isinstance(x, str) for x in pr):
        return True
    return False


def conformance_counts(records, model_id):
    n = 0
    conf = 0
    for r in records:
        if r.get("modelo_testado") == model_id and "resposta_ia" in r:
            n += 1
            if not divergent(r.get("resposta_ia", "")):
                conf += 1
    return conf, n


def fisher_2x2(a_conf, a_n, b_conf, b_n, label):
    """Returns dict with conf rates, Fisher p-value, OR.

    Contingency table:        conformant | divergent
                       A:       a_conf      a_n-a_conf
                       B:       b_conf      b_n-b_conf
    """
    table = [[a_conf, a_n - a_conf],
             [b_conf, b_n - b_conf]]
    odds_ratio, p_value = fisher_exact(table, alternative="two-sided")
    return {
        "label": label,
        "A_conformant": f"{a_conf}/{a_n}",
        "B_conformant": f"{b_conf}/{b_n}",
        "table": table,
        "odds_ratio": odds_ratio if odds_ratio != float("inf") else "inf",
        "p_value": p_value,
    }


def fmt_p(p):
    if p < 1e-15:
        return f"p < 1e-15"
    if p < 1e-3:
        return f"p = {p:.2e}"
    return f"p = {p:.4f}"


def main():
    # main corpus (312 calls)
    main_records = json.loads((ROOT / "data" / "results" / "round_1_main_models.json").read_text()) \
                 + json.loads((ROOT / "data" / "results" / "round_2_complementary_models.json").read_text())
    # counter-experiment corpus
    cx_records = json.loads((ROOT / "data" / "results" / "counter_experiment_llama32.json").read_text())

    models = [
        "qwen2.5:1.5b-instruct", "qwen2.5:3b-instruct",
        "llama3.2:1b", "llama3.2:3b",
        "gemma2:2b", "gemma2:9b",
        "llama3:8b", "phi3:mini",
    ]
    counts = {m: conformance_counts(main_records, m) for m in models}

    print("=== Baseline conformance (n=39 per model) ===")
    for m, (c, n) in counts.items():
        rate = 100 * c / n if n else float("nan")
        print(f"  {m:<28} {c}/{n}  ({rate:.1f}%)")
    print()

    results = []

    # F1-F2: Llama 3.2 vs Qwen 2.5 at matched scale
    results.append(fisher_2x2(*counts["llama3.2:1b"], *counts["qwen2.5:1.5b-instruct"],
                              "F1: Llama 3.2 1B vs Qwen 2.5 1.5B"))
    results.append(fisher_2x2(*counts["llama3.2:3b"], *counts["qwen2.5:3b-instruct"],
                              "F2: Llama 3.2 3B vs Qwen 2.5 3B"))
    # F3: Llama 3.2 vs Gemma 2 at matched scale (3B vs 2B closest)
    results.append(fisher_2x2(*counts["llama3.2:3b"], *counts["gemma2:2b"],
                              "F3: Llama 3.2 3B vs Gemma 2 2B"))
    # F4-F5: Phi-3 vs conformant references
    results.append(fisher_2x2(*counts["phi3:mini"], *counts["qwen2.5:3b-instruct"],
                              "F4: Phi-3 mini vs Qwen 2.5 3B"))
    results.append(fisher_2x2(*counts["phi3:mini"], *counts["llama3:8b"],
                              "F5: Phi-3 mini vs Llama 3 8B"))

    # F6-F7: zero-shot vs one-shot within Llama 3.2 (E2 experiment, temp=0.2)
    def cx_counts(experiment, model):
        n, c, timeouts = 0, 0, 0
        for r in cx_records:
            if r.get("experimento") == experiment and r.get("modelo") == model:
                if "erro" in r and "timeout" in str(r.get("erro","")).lower():
                    timeouts += 1
                    continue
                n += 1
                if r.get("conforme"):
                    c += 1
        return c, n, timeouts

    c1b_e2, n1b_e2, t1b = cx_counts("E2_fewshot", "llama3.2:1b")
    c3b_e2, n3b_e2, t3b = cx_counts("E2_fewshot", "llama3.2:3b")

    print(f"E2 1B: {c1b_e2}/{n1b_e2} conformant ({t1b} timeouts excluded)")
    print(f"E2 3B: {c3b_e2}/{n3b_e2} conformant ({t3b} timeouts excluded)")
    print()

    results.append(fisher_2x2(*counts["llama3.2:1b"], c1b_e2, n1b_e2,
                              "F6: Llama 3.2 1B  zero-shot vs one-shot (E2)"))
    results.append(fisher_2x2(*counts["llama3.2:3b"], c3b_e2, n3b_e2,
                              "F7: Llama 3.2 3B  zero-shot vs one-shot (E2)"))

    print("=== Fisher exact 2x2 (two-sided) ===\n")
    for r in results:
        print(f"{r['label']}")
        print(f"  A: {r['A_conformant']}    B: {r['B_conformant']}")
        print(f"  Table: {r['table']}")
        print(f"  OR = {r['odds_ratio']},   {fmt_p(r['p_value'])}")
        print()

    out = ROOT / "analises" / "inferential_results.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(results, indent=2, default=str), encoding="utf-8")
    print(f"saved {out}")


if __name__ == "__main__":
    main()
