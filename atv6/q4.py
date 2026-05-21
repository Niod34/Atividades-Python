import json

dados_envio = {
    "usuario": "Saulo",
    "servico": "Chatbot-IA",
    "requisicao": {
        "pergunta": "Como funciona o fluxo de uma API?"
    }
}


json_formatado = json.dumps(dados_envio, indent=4, ensure_ascii=False)

print(json_formatado)