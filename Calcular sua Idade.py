while True:                                                             # enquanto for verdadeiro
    print("-------------------------------------")                      # printa uma linha para separar
    ano_nascimento = int(input("Digite seu ano de nascimento: "))       # input permite digitar seu ano de nascimento e int trasnforma em numero
    ano_atual = 2025                                                    # define a variavel ano atual como 2025
    idade = ano_atual - ano_nascimento                                  # define a variavel idade sendo o resultado de ano atual menos anos nascimento
    print("Voce tem", idade, "anos")                                    # printa o resultado na tela, idade puxa o resultado para a tela tambem
  