import json

# Abrindo o arquivo JSON
with open("questao5.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

# Exibindo os dados
print("Nome:", dados["nome"])
print("Idade:", dados["idade"])