import requests
import json
import time

from prompts import SYSTEM_PROMPT

# 1. Matriz de Testes baseada no Modelo de Dados e Ingedore Koch
MATRIZ_TESTES = [
    {
        "cenario_id": 1,
        "foco_koch": "Coesão Referencial (Ambiguidade por pronominalização inadequada)",
        "conteudo": "Vilela era muito amigo de Camilo. Ele descobriu a traição com sua esposa. Então ele mandou um bilhete para ele ir à sua casa. Quando o homem chegou lá, ele estava com uma arma e atirou nele."
    },
    {
        "cenario_id": 2,
        "foco_koch": "Coesão Sequencial (Uso contraditório de operadores argumentativos)",
        "conteudo": "Camilo era cético, portanto não acreditava na cartomante. Ele foi até a casa dela, embora ela tenha garantido que o futuro dele com Rita seria feliz. Vilela atirou nos dois, contudo o triângulo amoroso chegou ao fim."
    },
    {
        "cenario_id": 3,
        "foco_koch": "Coesão Referencial (Falta de elipse e repetição lexical excessiva)",
        "conteudo": "A cartomante morava em uma casa velha. A cartomante olhou as cartas em cima da mesa. A cartomante sorriu para Camilo e segurou a mão dele. A cartomante falou que Rita realmente amava Camilo e que nada de mal ia acontecer."
    },
    {
        "cenario_id": 4,
        "foco_koch": "Coesão Sequencial (Desorganização de marcadores temporais e espaciais)",
        "conteudo": "Camilo entrou na sala de Vilela. Rita estava morta e cheia de sangue no chão. Camilo estava na carruagem pensando na cartomante. Vilela agarrou Camilo pela gola e atirou duas vezes. O bilhete dizia para ele ir rápido."
    },
    {
        "cenario_id": 5,
        "foco_koch": "Coesão Sequencial (Justaposição extrema sem estabelecimento de relações lógico-semânticas)",
        "conteudo": "Camilo recebeu as cartas anônimas. O amor por Rita era perigoso. Vilela mandou um bilhete urgente. Camilo ficou com muito medo. Camilo desviou o caminho. Ele foi consultar a cartomante."
    }
]

# 2. System Prompt — fonte única em prompts.py (importado acima)

MODELOS_PARA_TESTAR = ["llama3:8b", "gemma2:9b"]
RELATORIO_FINAL = []

print("🚀 Iniciando o Benchmark Automatizado no MacBook Pro M5...\n")

for modelo in MODELOS_PARA_TESTAR:
    print(f"--- Avaliando o Modelo: {modelo} ---")

    for cenario in MATRIZ_TESTES:
        print(f"Processando Cenário {cenario['cenario_id']} ({cenario['foco_koch']})...")

        # Estrutura de dados exigida pela API do Ollama
        payload = {
            "model": modelo,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": cenario["conteudo"]}
            ],
            "stream": False,
            "format": "json",  # Força o modelo local a responder em JSON
            "options": {
                "temperature": 0.2  # Baixa temperatura para o modelo seguir rigorosamente a rubrica
            }
        }

        # Medição de latência conforme a instrumentação de pesquisa da tese
        start_time = time.time()

        try:
            # 🔗 AQUI ESTÁ A CONEXÃO REAL COM O SEU OLLAMA LOCAL:
            response = requests.post(
                "http://localhost:11434/api/chat",
                json=payload,
                timeout=60
            )
            end_time = time.time()

            # Processamento da resposta do servidor local
            latencia_ms = int((end_time - start_time) * 1000)
            data = response.json()

            output_texto = data["message"]["content"]

            # Extração de telemetria nativa do Ollama (para o seu modelo de dados)
            tokens_input = data.get("prompt_eval_count", 0)
            tokens_output = data.get("eval_count", 0)

            # Persistência temporária na lista de resultados (simulando a tabela FeedbackIA)
            RELATORIO_FINAL.append({
                "modelo_testado": modelo,
                "cenario_id": cenario["cenario_id"],
                "foco_teorico": cenario["foco_koch"],
                "latencia_ms": latencia_ms,
                "tokens_input": tokens_input,
                "tokens_output": tokens_output,
                "resposta_ia": output_texto
            })

            print(f"✅ Cenário {cenario['cenario_id']} Concluído em {latencia_ms}ms | Tokens Out: {tokens_output}")

        except Exception as e:
            print(f"❌ Erro de conexão com o Ollama no cenário {cenario['cenario_id']}: {str(e)}")

# 4. Exportação dos logs do experimento para arquivo JSON
with open("resultados_benchmark_brutos.json", "w", encoding="utf-8") as f:
    json.dump(RELATORIO_FINAL, f, indent=2, ensure_ascii=False)

print("\n🏆 Experimento Concluído! Resultados salvos em 'resultados_benchmark_brutos.json'.")
