palavra =  input("Digite uma palavra; ")

if palavra in ["ótimo", "bom", "excelente", "feliz", "maravilhoso"]:
    sentimento = "Positivo"
    
elif palavra in ["ruim", "péssimo", "triste", "horrível", "odio"]:
    sentimento = "Negativo"
    
else:
    sentimento = "Neutro"

print("Sentimento identificado:", sentimento)