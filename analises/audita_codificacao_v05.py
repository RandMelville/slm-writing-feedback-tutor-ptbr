"""Auditoria de completude das duas codificações v0.5 (39 devolutivas do qwen2.5:3b-instruct).

Roda ANTES de qualquer cálculo de concordância. Não calcula κ, não corrige nada e não
escreve nos arquivos congelados: só descreve o que está preenchido e o que não está.

Checagens (Protocolo v0.5, seções 3.0, 3.1 e 5):
  1. cobertura      -- 39 linhas, IDs R01..R39, os mesmos nos dois arquivos
  2. domínio        -- toda célula FM/FP/MTL em {0, 1, vazio}
  3. vazios         -- contagem e lista por coluna (mede a diferença de convenção A x B)
  4. regra 3.0      -- proibido FPxx = 1 com FMxx != 1
  5. evidência      -- todo FMxx = 1 exige "Evidência FMxx" não vazia
  6. justificativa  -- todo FPxx = 1 exige "Justificativa FPxx" não vazia
  7. MTL            -- lista os ID sem MTL (a 2ª passada do procedimento)
  8. observações    -- imprime as linhas com "Observações" preenchida

Entrada: data/codificacao_v05_respostas/codificacao_{A,B}_<AAAA-MM-DD>.xlsx, aba "Codificação".
Uso: python3 analises/audita_codificacao_v05.py
"""
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RESPOSTAS = ROOT / "data" / "codificacao_v05_respostas"
ABA = "Codificação"

FMS = [f"FM{i:02d}" for i in range(1, 9)]
FPS = [f"FP{i:02d}" for i in range(1, 9)]
IDS_ESPERADOS = [f"R{i:02d}" for i in range(1, 40)]

COLUNAS = ["ID", "Texto do aluno", "Devolutiva"]
for i in range(1, 9):
    COLUNAS += [f"FM{i:02d}", f"Evidência FM{i:02d}", f"FP{i:02d}", f"Justificativa FP{i:02d}"]
COLUNAS += ["MTL", "Observações"]


def localiza():
    """Devolve {'A': path, 'B': path}, pegando o arquivo mais recente de cada codificadora."""
    achados = {}
    for rotulo in ("A", "B"):
        candidatos = sorted(RESPOSTAS.glob(f"codificacao_{rotulo}_*.xlsx"))
        if not candidatos:
            sys.exit(
                f"ERRO: nenhum codificacao_{rotulo}_*.xlsx em {RESPOSTAS.relative_to(ROOT)}/\n"
                "Baixe cada planilha do Drive em Arquivo > Baixar > Microsoft Excel (.xlsx)\n"
                "e salve com esse nome antes de rodar a auditoria."
            )
        achados[rotulo] = candidatos[-1]
    return achados


def celula(v):
    """Normaliza uma célula binária. Devolve 0, 1, None (vazia) ou a string crua (inválida)."""
    if v is None or (isinstance(v, float) and pd.isna(v)):
        return None
    if isinstance(v, str):
        v = v.strip()
        if v == "":
            return None
        try:
            v = float(v)
        except ValueError:
            return str(v)
    if isinstance(v, (int, float)) and float(v) in (0.0, 1.0):
        return int(v)
    return str(v)


def texto(v):
    """True se a célula de evidência/justificativa tem conteúdo."""
    if v is None or (isinstance(v, float) and pd.isna(v)):
        return False
    return str(v).strip() != ""


def audita(rotulo, caminho, out):
    def p(linha=""):
        out.append(linha)

    p(f"{'=' * 72}")
    p(f"CODIFICADORA {rotulo}  --  {caminho.name}")
    p(f"{'=' * 72}")

    df = pd.read_excel(caminho, sheet_name=ABA)

    # 0. cabeçalho
    faltando = [c for c in COLUNAS if c not in df.columns]
    if faltando:
        p(f"[cabeçalho] AUSENTES: {faltando}")
        p("  auditoria interrompida para esta planilha.")
        return None
    extras = [c for c in df.columns if c not in COLUNAS]
    p(f"[cabeçalho] 37 colunas esperadas presentes" + (f"; extras ignoradas: {extras}" if extras else ""))

    # 1. cobertura
    ids = [str(x).strip() for x in df["ID"].tolist()]
    p(f"[cobertura] {len(ids)} linhas de dados")
    ausentes = [i for i in IDS_ESPERADOS if i not in ids]
    repetidos = sorted({i for i in ids if ids.count(i) > 1})
    inesperados = [i for i in ids if i not in IDS_ESPERADOS]
    if ausentes:
        p(f"[cobertura] FALTAM: {ausentes}")
    if repetidos:
        p(f"[cobertura] REPETIDOS: {repetidos}")
    if inesperados:
        p(f"[cobertura] FORA DA FAIXA R01-R39: {inesperados}")
    if not (ausentes or repetidos or inesperados):
        p("[cobertura] OK, R01 a R39 sem falta nem repetição")

    binarias = FMS + FPS + ["MTL"]
    invalidos, vazios, viola30, sem_evid, sem_just, sem_mtl, obs = [], {}, [], [], [], [], []

    for _, linha in df.iterrows():
        rid = str(linha["ID"]).strip()
        for col in binarias:
            v = celula(linha[col])
            if v is None:
                vazios.setdefault(col, []).append(rid)
            elif v not in (0, 1):
                invalidos.append(f"{rid}/{col} = {v!r}")
        for i in range(1, 9):
            fm, fp = celula(linha[f"FM{i:02d}"]), celula(linha[f"FP{i:02d}"])
            if fp == 1 and fm != 1:
                viola30.append(f"{rid}/FP{i:02d} = 1 com FM{i:02d} = {fm}")
            if fm == 1 and not texto(linha[f"Evidência FM{i:02d}"]):
                sem_evid.append(f"{rid}/FM{i:02d}")
            if fp == 1 and not texto(linha[f"Justificativa FP{i:02d}"]):
                sem_just.append(f"{rid}/FP{i:02d}")
        if celula(linha["MTL"]) is None:
            sem_mtl.append(rid)
        if texto(linha["Observações"]):
            obs.append((rid, str(linha["Observações"]).strip()))

    # 2. domínio
    p(f"[domínio] valores fora de {{0, 1, vazio}}: {len(invalidos)}")
    for x in invalidos:
        p(f"           {x}")

    # 3. vazios
    n_fm = sum(len(v) for c, v in vazios.items() if c in FMS)
    n_fp = sum(len(v) for c, v in vazios.items() if c in FPS)
    n_mtl = len(vazios.get("MTL", []))
    p(f"[vazios] FM: {n_fm}  |  FP: {n_fp}  |  MTL: {n_mtl}  (de 39 linhas x 17 decisões)")
    for col in binarias:
        if col in vazios:
            quais = "todas as linhas" if len(vazios[col]) == len(ids) else ", ".join(vazios[col])
            p(f"         {col}: {len(vazios[col])} -> {quais}")

    # 4. regra 3.0
    p(f"[regra 3.0] FP = 1 com FM != 1: {len(viola30)}")
    for x in viola30:
        p(f"            {x}")

    # 5. evidência
    p(f"[evidência] FM = 1 sem trecho copiado: {len(sem_evid)}")
    for x in sem_evid:
        p(f"            {x}")

    # 6. justificativa
    p(f"[justificativa] FP = 1 sem justificativa: {len(sem_just)}")
    for x in sem_just:
        p(f"                {x}")

    # 7. MTL
    p(f"[MTL] linhas sem MTL: {len(sem_mtl)}" + (f" -> {', '.join(sem_mtl)}" if sem_mtl else ""))

    # 8. observações
    p(f"[observações] linhas com registro: {len(obs)}")
    for rid, txt in obs:
        p(f"              {rid}: {txt}")
    p()

    return {
        "linhas": len(ids), "invalidos": len(invalidos), "vazios_fm": n_fm,
        "vazios_fp": n_fp, "vazios_mtl": n_mtl, "viola30": len(viola30),
        "sem_evid": len(sem_evid), "sem_just": len(sem_just), "obs": len(obs),
    }


def main():
    arquivos = localiza()
    out = []
    resumo = {}
    for rotulo, caminho in arquivos.items():
        resumo[rotulo] = audita(rotulo, caminho, out)

    out.append("=" * 72)
    out.append("RESUMO")
    out.append("=" * 72)
    campos = [
        ("linhas", "linhas de dados"), ("invalidos", "valores inválidos"),
        ("vazios_fm", "FM vazias"), ("vazios_fp", "FP vazias"), ("vazios_mtl", "MTL vazias"),
        ("viola30", "FP=1 com FM!=1"), ("sem_evid", "FM=1 sem evidência"),
        ("sem_just", "FP=1 sem justificativa"), ("obs", "linhas com observação"),
    ]
    out.append(f"{'':<26}{'A':>8}{'B':>8}")
    for chave, rotulo in campos:
        a = resumo["A"][chave] if resumo["A"] else "-"
        b = resumo["B"][chave] if resumo["B"] else "-"
        out.append(f"{rotulo:<26}{a:>8}{b:>8}")

    texto_final = "\n".join(out)
    print(texto_final)

    destino = ROOT / "analises" / "auditoria_codificacao_v05.txt"
    destino.write_text(texto_final + "\n", encoding="utf-8")
    print(f"\nRelatório salvo em {destino.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
