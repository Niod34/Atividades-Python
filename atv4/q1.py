nome = input("Digite o nome de usuário: ")
with open("usuarios.txt", "w") as arquivo:
    arquivo.write(nome)
