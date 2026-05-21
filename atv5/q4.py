import requests

# 1. Consulte a API para o país 'brazil'
resposta = requests.get("https://restcountries.com/v3.1/name/brazil")
dados = resposta.json()

# Como a API sempre retorna uma lista [ ], pegamos o primeiro item [0]
pais = dados[0]

# 2. Exiba as informações solicitadas
print("País:", pais["name"]["common"])
print("Capital:", pais["capital"][0])
print("População:", pais["population"])