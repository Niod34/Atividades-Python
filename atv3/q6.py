positivas = ["bom", "ótimo", "excelente", "legal"]
total_positivo = 0

print("Digite palavras (ou 'sair' para encerrar):")
while True:
    palavra = input("> ").lower()
    if palavra == 'sair':
        break
    if palavra in positivas:
        total_positivo += 1

print(f"Total de palavras positivas identificadas: {total_positivo}")