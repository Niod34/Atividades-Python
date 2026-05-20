genero = input("Digite o gênero: ")

if genero == "ação":
    filme = "Mad Max"
elif genero == "comédia":
    filme = "Gente Grande"
else:
    filme = "Titanic"

arquivo = open("recomendacoes.txt", "w")
arquivo.write(filme)
arquivo.close()