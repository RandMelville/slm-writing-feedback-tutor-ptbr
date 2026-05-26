"""Fisher's exact tests + Wilson 95% CIs for the SLM benchmark.

Replaces the earlier 7-pair design with a referent-based framing:
  - Table 2: each model vs qwen2.5:3b-instruct as reference
  - Table 3: each isolation (E1, E2, E2b) vs zero-shot baseline (Llama 3.2)
  - Table 4: metalinguistic adherence of the conformant model with Wilson CI

Outputs:
  analises/inferential_results.json  (machine readable)
  stdout summary in publication-ready format (APA-style p-values)
"""
import json, math
from pathlib import Path
from scipy.stats import fisher_exact

ROOT = Path(__file__).resolve().parent.parent
REFERENCE_MODEL = "qwen2.5:3b-instruct"


def divergent(raw_response: str) -> bool:
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


def wilson_ci(k: int, n: int, confidence: float = 0.95) -> tuple[float, float]:
    """Wilson score interval for a binomial proportion, in percent points."""
    if n == 0:
        return (0.0, 0.0)
    z = 1.959963984540054  # 95% normal quantile
    p = k / n
    denom = 1 + z * z / n
    center = (p + z * z / (2 * n)) / denom
    half = (z / denom) * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    lower = max(0.0, center - half) * 100
    upper = min(1.0, center + half) * 100
    return (round(lower, 1), round(upper, 1))


def fisher_2x2(a_conf: int, a_n: int, b_conf: int, b_n: int) -> dict:
    """Fisher's exact two-sided on contingency table [[a_conf, a_n-a_conf], [b_conf, b_n-b_conf]]."""
    table = [[a_conf, a_n - a_conf], [b_conf, b_n - b_conf]]
    _, p = fisher_exact(table, alternative="two-sided")
    return {"p": p, "table": table}


def fmt_p_apa(p: float) -> str:
    """APA-style p-value with significance asterisks."""
    if p < 0.001:
        return "p < 0.001 ***"
    if p < 0.01:
        return f"p = {p:.3f} **"
    if p < 0.05:
        return f"p = {p:.3f} *"
    if p >= 0.999:
        return "p = 1.000 n.s."
    return f"p = {p:.3f} n.s."


def conformance_counts(records, model_id):
    n, conf = 0, 0
    for r in records:
        if r.get("modelo_testado") == model_id and "resposta_ia" in r:
            n += 1
            if not divergent(r.get("resposta_ia", "")):
                conf += 1
    return conf, n


def main():
    main_records = json.loads((ROOT / "data" / "results" / "round_1_main_models.json").read_text()) \
                 + json.loads((ROOT / "data" / "results" / "round_2_complementary_models.json").read_text())
    cx_records  = json.loads((ROOT / "data" / "results" / "counter_experiment_llama32.json").read_text())

    models = [
        "qwen2.5:3b-instruct", "gemma2:9b", "llama3:8b",
        "qwen2.5:1.5b-instruct", "gemma2:2b",
        "llama3.2:1b", "llama3.2:3b", "phi3:mini",
    ]
    counts = {m: conformance_counts(main_records, m) for m in models}
    ref_conf, ref_n = counts[REFERENCE_MODEL]

    # === Table 2: each model vs reference model ===
    table2 = []
    for m in models:
        c, n = counts[m]
        rate = round(100 * c / n, 1)
        ci_lo, ci_hi = wilson_ci(c, n)
        if m == REFERENCE_MODEL:
            fisher_str, p = "reference", None
        else:
            f = fisher_2x2(c, n, ref_conf, ref_n)
            fisher_str, p = fmt_p_apa(f["p"]), f["p"]
        tier = "ceiling" if m in ("llama3:8b", "gemma2:9b") else "deployable"
        table2.append({
            "model": m, "k": c, "n": n, "rate_pct": rate,
            "ci95_low": ci_lo, "ci95_high": ci_hi, "tier": tier,
            "fisher_vs_ref": fisher_str, "p_value": p,
        })

    # === Table 3: each isolation vs zero-shot baseline ===
    def cx_counts(experiment, model):
        """Timeouts count in the denominator as non-conformant (conservative framing)."""
        n, c, t = 0, 0, 0
        for r in cx_records:
            if r.get("experimento") == experiment and r.get("modelo") == model:
                n += 1
                if "erro" in r and "timeout" in str(r.get("erro", "")).lower():
                    t += 1
                    continue
                if r.get("conforme"):
                    c += 1
        return c, n, t

    table3 = []
    base_1b, base_3b = counts["llama3.2:1b"], counts["llama3.2:3b"]
    for label, exp in [("E1 (zero-shot, t=0.0)", "E1_temp0"),
                       ("E2 (one-shot, t=0.2)", "E2_fewshot"),
                       ("E2b (one-shot, t=0.0)", "E2b_fewshot_temp0")]:
        c1, n1, t1 = cx_counts(exp, "llama3.2:1b")
        c3, n3, t3 = cx_counts(exp, "llama3.2:3b")
        ci_3b = wilson_ci(c3, n3) if n3 else (None, None)
        # Fisher vs baseline (3B): isolation result vs the model's own zero-shot 0/39
        f_3b = fisher_2x2(c3, n3, base_3b[0], base_3b[1]) if n3 else None
        f_1b = fisher_2x2(c1, n1, base_1b[0], base_1b[1]) if n1 else None
        table3.append({
            "isolation": label,
            "experiment": exp,
            "llama_1b": {"k": c1, "n": n1, "timeouts": t1,
                         "rate_pct": round(100*c1/n1, 1) if n1 else None,
                         "fisher_vs_baseline": fmt_p_apa(f_1b["p"]) if f_1b else "—",
                         "p_value": f_1b["p"] if f_1b else None},
            "llama_3b": {"k": c3, "n": n3, "timeouts": t3,
                         "rate_pct": round(100*c3/n3, 1) if n3 else None,
                         "ci95_low": ci_3b[0], "ci95_high": ci_3b[1],
                         "fisher_vs_baseline": fmt_p_apa(f_3b["p"]) if f_3b else "—",
                         "p_value": f_3b["p"] if f_3b else None},
        })

    # === Table 4: metalinguistic adherence — qwen2.5:3b-instruct, 6/13 ===
    k4, n4 = 6, 13
    ci4_lo, ci4_hi = wilson_ci(k4, n4)
    table4 = {
        "model": REFERENCE_MODEL,
        "scenarios_with_koch_terms": k4,
        "total_scenarios": n4,
        "rate_pct": round(100*k4/n4, 1),
        "ci95_low": ci4_lo,
        "ci95_high": ci4_hi,
    }

    # === Pretty stdout report ===
    print("=" * 78)
    print("TABLE 2 — Structural conformance per model (vs", REFERENCE_MODEL, "as reference)")
    print("=" * 78)
    print(f"{'Model':<25} {'k/n':>7} {'Rate':>7} {'Wilson 95% CI':>20} {'Tier':>11} {'Fisher vs ref':>18}")
    for r in table2:
        ci = f"[{r['ci95_low']:.1f}; {r['ci95_high']:.1f}]"
        print(f"{r['model']:<25} {r['k']}/{r['n']:<5} {r['rate_pct']:>5.1f}% {ci:>22} {r['tier']:>11} {r['fisher_vs_ref']:>18}")

    print("\n" + "=" * 78)
    print("TABLE 3 — Llama 3.2 conformance under falsification isolations (vs baseline)")
    print("=" * 78)
    print(f"{'Isolation':<28} {'1B':>12} {'3B':>12} {'Wilson 95% CI (3B)':>22} {'Fisher (3B)':>18}")
    base_ci = wilson_ci(*base_3b)
    print(f"{'Baseline (zero-shot t=0.2)':<28} {base_1b[0]}/{base_1b[1]:>4} (0.0%) {base_3b[0]}/{base_3b[1]:>4} (0.0%) [{base_ci[0]:.1f}; {base_ci[1]:.1f}]{'':>2}     —              ")
    for r in table3:
        s1 = f"{r['llama_1b']['k']}/{r['llama_1b']['n']} ({r['llama_1b']['rate_pct']:.1f}%)" if r['llama_1b']['n'] else "—"
        s3 = f"{r['llama_3b']['k']}/{r['llama_3b']['n']} ({r['llama_3b']['rate_pct']:.1f}%)" if r['llama_3b']['n'] else "—"
        ci = f"[{r['llama_3b']['ci95_low']:.1f}; {r['llama_3b']['ci95_high']:.1f}]" if r['llama_3b']['ci95_low'] is not None else "—"
        print(f"{r['isolation']:<28} {s1:>12} {s3:>12} {ci:>22} {r['llama_3b']['fisher_vs_baseline']:>18}")

    print("\n" + "=" * 78)
    print("TABLE 4 — Metalinguistic adherence of conformant model (qwen2.5:3b-instruct)")
    print("=" * 78)
    print(f"  Scenarios with Koch terminology: {table4['scenarios_with_koch_terms']}/{table4['total_scenarios']} ({table4['rate_pct']:.1f}%)")
    print(f"  Wilson 95% CI: [{table4['ci95_low']:.1f}%; {table4['ci95_high']:.1f}%]")
    print(f"  Upper bound implies absence in >= {round(100 - table4['ci95_high'])}% of scenarios")
    print(f"  Lower bound implies absence in >= {round(100 - table4['ci95_low'])}% of scenarios")

    out = ROOT / "analises" / "inferential_results.json"
    out.write_text(json.dumps({
        "reference_model": REFERENCE_MODEL,
        "table2_conformance": table2,
        "table3_counter_experiment": table3,
        "table4_metalinguistic_adherence": table4,
    }, indent=2, default=str), encoding="utf-8")
    print(f"\nsaved {out}")


if __name__ == "__main__":
    main()
