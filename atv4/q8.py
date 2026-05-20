palavra = input("Digite a palavra: ")

if palavra == "bom" or palavra == "ótimo":
    resultado = "Positivo"
else:
    resultado = "Negativo"

arquivo = open("sentimentos.txt", "w")
arquivo.write(resultado)
arquivo.close()