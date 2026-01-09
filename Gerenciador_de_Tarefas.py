tarefas = []                                              # cria a lista tarefas
concluidas = []                                           # cria a lista concluidas

def ad_tarefas():                                         # cria a funcao ad_tarefas
    tarefa = input("Anotar Tarefa: ")                     # define a variavel tarefas como oq vc escrever, input permite isso
    tarefas.append(tarefa)                                # adiciona o item tarefa na lista tarefas, o append adiciona um item no final de uma lista
    
def listar_tarefas():                                     # cria a funcao listar_tarefas
    print("\n--- Lista de Tarefas ---")                   # printa um texto, \n cria um alinha em branco, um espaco em cima do texto
    for i, t in enumerate(tarefas):                       # percorre a lista tarefas pegando AO MESMO TEMPO o índice (i) e o valor (t).
        print(f"{i} - {t}")                               # é uma f-string, para printar o texto junto com variaveis. f diz que dentro das chaves { } tem variáveis ou expressões que devem ser substituídas pelo valor delas.

def concluir_tarefas():                                   # cria a funcao concluir_tarefas
    for i, t in enumerate(tarefas):                       # percorre a lista tarefas pegando AO MESMO TEMPO o índice (i) e o valor (t).
        print(f"{i} - {t}")                               # é uma f-string, para printar o texto junto com variaveis. f diz que dentro das chaves { } tem variáveis ou expressões que devem ser substituídas pelo valor delas.
        
    num = int(input("Qual tarefa deseja concluir?: "))    # define num como oq vc digitar, int faz o valor digitado vem como texto, então int() converte esse texto para número inteiro.
    tarefa_concluida = tarefas.pop(num)                   # .pop(num) remove da lista tarefas o item que está no índice num e devolve o valor removido, e você guarda ele na variável tarefa_concluida.
    concluidas.append(tarefa_concluida)                   # adiciona tarefa_concluida no final da lista concluidas, .append adiciona no final da lista
    print("Tarefa concluida!! ")                          # printa um texto

def excluir_tarefas():                                    # cria a funcao excluir_tarefas
    for i, t in enumerate(tarefas):                       # percorre a lista tarefas pegando AO MESMO TEMPO o índice (i) e o valor (t).
        print(f"{i} - {t}")                               # é uma f-string, para printar o texto junto com variaveis. f diz que dentro das chaves { } tem variáveis ou expressões que devem ser substituídas pelo valor delas.

    num = int(input("Qual tarefa deseja excluir?: "))     # define num como oq vc digitar, int faz o valor digitado vem como texto, então int() converte esse texto para número inteiro.
    tarefa_excluida = tarefas.pop(num)                    # remove o item da lista tarefas na posição num. retorna esse item removido e guarda na variável tarefa_excluida.
    print(f"Tarefa {tarefa_excluida} excluida!")          # mostra na tela o texto "Tarefa X excluída!", onde X é o valor da variável tarefa_excluida.
     

while True:                                               # o código dentro desse while vai rodar para sempre, até você usar um comando que interrompa, como:
    print("\n")
    print("--- Gerenciador de Tarefas ---")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Concluir tarefa")
    print("4. Excluir tarefa")
    print("5. Sair do programa")


    op = input("Escolha uma opção: ")                     # Lê a opção digitada pelo usuário
    print("\n")                                           # Pula uma linha para organizar

    if op == "1":                                         # Se o usuário escolheu 1
        ad_tarefas()                                      # chama a função para adicionar tarefas

    elif op == "2":                                       # Se o usuário escolheu 2
        listar_tarefas()                                  # chama a função que lista as tarefas

    elif op == "3":                                       # Se o usuário escolheu 3
        concluir_tarefas()                                # chama a função para concluir tarefas

    elif op == "4":                                       # Se o usuário escolheu 4
        excluir_tarefas()                                 # chama a função que exclui tarefas

    elif op == "5":                                       # Se o usuário escolheu 5
        print("Saindo do programa...")                    # Mensagem de saída
        break                                             # Encerra o loop while True

    else:                                                 # Se digitou algo diferente de 1 a 5
        print("Opção inválida!!")                         # Informa que é inválido
        print(" ")                                        # Pula uma linha

