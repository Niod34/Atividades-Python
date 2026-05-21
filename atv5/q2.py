import requests

# a) Faz a requisição para a API do GitHub
resposta = requests.get("https://api.github.com")

# b) Exiba os dados retornados pela API (em formato JSON)
print(resposta.json())