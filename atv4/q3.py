nota1 = input("Digite a primeira nota: ")
nota2 = input("Digite a segunda nota: ")

with open("notas.txt", "w") as arquivo:
    arquivo.write(f"Nota 1: {nota1}\nNota 2: {nota2}")