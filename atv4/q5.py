nome = input("Digite o nome de usuário: ")
with open("acessos.txt", "a") as arquivo:
    arquivo.write("\nNome: " + nome )
