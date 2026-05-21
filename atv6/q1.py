pergunta = input("Digite sua pergunta: ").lower()

if "python" in pergunta:
    resposta = "Python é uma linguagem de programação fantástica e muito usada em IA!"
elif "tempo" in pergunta or "clima" in pergunta:
    resposta = "Não consigo olhar a janela agora, mas espero que esteja um belo dia!"
elif "nome" in pergunta:
    resposta = "Eu sou o seu assistente virtual de Inteligência Artificial."
else:
    resposta = "Interessante! Ainda estou aprendendo sobre isso e não sei a resposta estruturada."

# c) Exiba a resposta na tela
print(resposta)