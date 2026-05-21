pergunta = input("Digite sua pergunta para a IA: ")

arquivo = open("historico_ia.txt", "w", encoding="utf-8")
arquivo.write(pergunta)
arquivo.close()

print("Pergunta salva no histórico com sucesso!")