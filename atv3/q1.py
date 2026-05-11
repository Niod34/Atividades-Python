genero = input("Escolha um gênero (ação, comédia ou terror): ").lower()

if genero == "ação":
    print("Recomendação: Mad Max: Estrada da Fúria.")
elif genero == "comédia":
    print("Recomendação: Superbad.")
elif genero == "terror":
    print("Recomendação: Corra.")
else:
    print("Gênero não reconhecido.")