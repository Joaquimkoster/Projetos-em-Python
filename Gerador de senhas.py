import random                                                         # serve para você usar funções que geram números aleatórios ou fazem escolhas aleatórias no Python.

while True:                                                           # se for verdadeiro, inicia o loop
    print("====== Gerador De Senhas ======")                          # printa o texto
    carac = int(input("Digite o numero de caracteres: "))             # define a variavel carac como o numero que vc deseja, int trasnformar em numero para usar no codigo
    menor = 10**(carac - 1)                                           # define a variavel menor, Isso calcula o menor número possível com a quantidade de caracteres que você quer.
    maior = (10**carac) - 1                                           # define a variavel maior, Isso calcula o maior número possível com a quantidade de dígitos que você escolheu.
    senha = random.randint(menor, maior)                              # define a variavel senha, é uma função do módulo random que gera um número inteiro aleatório entre menor e maior
    print(senha)                                                      # printa o texto
    
    resposta =  input("Deseja sair do programa? (s/n): ").lower()     # define resposta como s ou n, lower trasforma tudo em minusculo, inclusive oq vc digitar
    
    if resposta == "s":                                               # se resposta for igual s, printa um texto, e break para o loop
        print("Saindo do sistema... Tchau")
        break
    
    elif resposta == "n":                                             # senão, se resposta for igual n, printa um texto, e retorna ao inicio
        print("Continuando...")
    
    else:                                                             # senão, printa um texto
        print("Opção invalida, Tente novamente")