nome = input("Digite uma resposta: ")
with open("respostas.txt", "w") as arquivo:
    arquivo.write("Resposta do usuário: " + nome )

print("Resposta armazenada com sucesso!")
