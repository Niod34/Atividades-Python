with open("tarefas.txt", "w") as arquivo:
    for i in range(3):
        tarefa = input(f"Digite a tarefa {i+1}: ")
        arquivo.write(tarefa + "\n")