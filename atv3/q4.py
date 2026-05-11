notas = []
for i in range(1, 6):
    nota = float(input(f"Digite a nota {i}: "))
    notas.append(nota)

media = sum(notas) / 5
print(f"Média final: {media:.1f}")

if media >= 6.0:
    print("Situação: Aprovado")
else:
    print("Situação: Reprovado")