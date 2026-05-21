soma_notas = 0

for i in range(1, 4):
    nota = float(input(f"Digite a {i}ª nota: "))
    soma_notas += nota  

media = soma_notas / 3

print(f"\nMédia final: {media:.2f}")

if media >= 9.0:
    print("Excelente desempenho")
elif media >= 7.0:
    print("Bom desempenho")
else:
    print("Desempenho insuficiente")