palavra = input("Digite uma palavra para análise: ").lower()

if palavra in ["bom", "ótimo", "excelente", "maravilhoso"]:
    print("Classificação: Positivo")
elif palavra in ["ruim", "péssimo", "horrível", "fraco"]:
    print("Classificação: Negativo")
else:
    print("Classificação: Neutro")