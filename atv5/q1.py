import requests

# Consulta a API
resposta = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
dados = resposta.json()

# Extrai e exibe apenas o valor atual (bid)
valor_dolar = dados["USDBRL"]["bid"]
print(valor_dolar)