while True:
    mensagem = input("Você: ").lower()
    
    if mensagem == "oi":
        print("Chatbot: Olá! Como posso ajudar?")
    elif mensagem == "tchau":
        print("Chatbot: Até logo!")
        break
    else:
        print("Chatbot: Não entendi sua mensagem")