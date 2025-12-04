def cadastro():                                                 # cria a função cadastro
    
    print("")                                                   # cria uma linha vazia
    print("=== CADASTRO DE USUÁRIO ===")                        # exibe o texto
    usuario = input("Digite seu usuario: ")                     # define usuario como oq vc digitar
    senha = input("Digite sua senha: ")                         # define senha como oq vc digitar

    with open("Cadastro.txt","w") as arquivo:                   # bre o arquivo Cadastro.txt no modo "w" (write). APAGA TUDO que já existia no arquivo antes. Cria o arquivo se não existir. O with fecha o arquivo automaticamente no final.
        arquivo.write(f"{usuario},{senha}\n")
    
    print("Cadastro salvo com sucesso!!!")                      # exibe o texto

def login():                                                    # cria a função login
    
    print("")                                                   # cria uma linha vazia
    print("=== LOGIN DE USUARIO ===")                           # exibe o texto
    usuario = input("Digite aq seu usuario: ")                  # define usuario como oq vc digitar
    senha = input("Digite aq a senha: ")                        # define senha como oq vc digitar
    
    with open("Cadastro.txt","r") as arquivo:                   # Abre o arquivo no modo "r" (read). Lê todo o conteúdo do arquivo e guarda dentro da variável conteudo.
        conteudo = arquivo.read()

    if usuario in conteudo:                                     # se usuario em conteudo, printa um texto
        print("Usuario logado com sucesso!!!")
    else:                                                       # senão, printa outro texto
        print("Usuario não encontrado, tente novamente")

    if senha in conteudo:                                       # se senha em conteudo, printa um texto
        print("Senha logada com sucesso!!!")
    else:                                                       # senão, printa outro texto
        print("Senha não encontrada, tente novamente")



while True:                                                     # se for verdadeiro, inicia o loop
    
    print("")                                                   # printa uma linha vazia
    print("===== Sistema =====")                                # exibe um texto
    print("1) Cadastro")                                        # exibe um texto
    print("2) Login")                                           # exibe um texto
    print("3) Sair")                                            # exibe um texto

    opc = input("Escolha uma opção: ")                          # depine opc como a opção que vc digitar

    if opc == "1":                                              # se opc for igual a 1, chama e executa a função cadastro
        cadastro()
    elif opc == "2":                                            # senão, se opc for igual a 2, chama e executa a função login
        login()
    elif opc == "3":                                            # senão, se opc for igual a 3, sai do programa, break para o loop
        print("Saindo do Sistema...")
        break
    else:                                                       # senão, printa um texto
        print("Opção invalida, tente novamente")
