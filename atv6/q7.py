while True:
    pergunta = input("Faça uma pergunta (ou digite 'sair' para fechar): ").strip().lower()
    
    if pergunta == "sair":
        print("Atendimento encerrado. Até logo!")
        break # O break interrompe o loop imediatamente
        
    print("Processando sua pergunta...")