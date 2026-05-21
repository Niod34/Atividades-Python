import requests
import json

# URL da API pública
url = "https://pokeapi.co/api/v2/pokemon/pikachu"

# Fazendo a requisição
resposta = requests.get(url)

# Convertendo os dados para JSON
dados = resposta.json()

# Salvando em um arquivo JSON
with open("dados_api.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)

print("Dados salvos com sucesso em dados_api.json")