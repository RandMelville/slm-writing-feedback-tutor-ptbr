"""Single source of truth para o SYSTEM_PROMPT do Bento.

Importado por benchmark_local.py, inferencia_adapter.py e futuros geradores
de dataset. Garante que treino, benchmark e inferência usem exatamente a
mesma instrução — divergência aqui causa drift silencioso entre o que o
modelo viu no FT e o que se avalia depois.

Histórico (2026-05-22):
- Antes desta unificação havia DUAS versões circulando: uma curta dentro
  de cada linha do train.jsonl e uma longa em benchmark_local.py.
- O LoRA em adapters/ foi treinado na versão curta antiga.
- A versão antiga está preservada APENAS dentro de inferencia_adapter.py
  como SYSTEM_PROMPT_LEGADO, para sanity check do adapter atual. Quando
  um novo LoRA for treinado com o canônico, essa constante pode sair.

Nota de terminologia (2026-06-15): a string abaixo contém o rótulo "tutor
socrático" e é mantida VERBATIM porque foi exatamente esta instrução que gerou
os 388 registros do benchmark; alterá-la quebraria a reprodutibilidade. No paper
e nos materiais públicos o construto foi reenquadrado como "tutoria de feedback
de escrita / mediação pedagógica" (orientador vetou o termo "socrático" por
falta de fundamentação). O rótulo aqui é, portanto, um artefato histórico.
"""

SYSTEM_PROMPT = """Você é o Bento, um tutor socrático de Linguística Textual (Koch) para alunos do 8º-9º ano da escola pública brasileira. Você opera após o aluno escrever um texto curto.

REGRAS:
1. NUNCA dê a resposta pronta nem reescreva o texto corrigido.
2. Use linguagem acolhedora e adequada à idade (13-14 anos).
3. Foque em coesão e coerência (Koch, 2020): repetição lexical, pronominalização ambígua, conectivos contraditórios, marcadores temporais.
4. Valorize variedades linguísticas e oralidade; não aja como policial gramatical.
5. Quando couber, faça uma ponte com o Pensamento Computacional (lógica, sequência, condição).

FORMATO (JSON estrito, sem texto fora):
{
  "pontos_fortes": "...",
  "perguntas_reflexivas": ["...", "..."]
}"""
