usuario_cadastrado = "admin"
senha_cadastrada = "1234"

usuario = input("Digite o usuário: ").lower()
senha = input("Digite a senha: ").lower()

if usuario == usuario_cadastrado and senha == senha_cadastrada:
    print("Acesso permitido")
else:
    print("Acesso negado")