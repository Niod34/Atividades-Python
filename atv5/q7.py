import json

pergunta = input("Digite sua pergunta: ")

chatbot = {
    "pergunta": pergunta,
    "resposta": "Essa é uma resposta automática do chatbot."
}

dados_json = json.dumps(chatbot, indent=4, ensure_ascii=False)

print(dados_json)