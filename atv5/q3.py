import json

# Criando um dicionário simulando uma resposta de IA
resposta_ia = {
    "pergunta": "O que é Inteligência Artificial?",
    "resposta": "Inteligência Artificial é a capacidade de máquinas simularem a inteligência humana."
}

# Convertendo o dicionário para JSON
dados_json = json.dumps(resposta_ia, indent=4, ensure_ascii=False)

# Exibindo o resultado
print(dados_json)