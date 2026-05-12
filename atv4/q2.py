mensagem = input("Digite uma mensagem: ")
with open("mensagem.txt", "w") as arquivo:
    arquivo.write(mensagem)