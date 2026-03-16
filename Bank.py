while True:
    print("\n" + "="*30)
    print("         PYTHON BANK       ")
    print("="*30)

    # ÁREA DE ACESSO (O que o usuário vê antes de logar)
    print("1) Criar Nova Conta")
    print("2) Fazer Login")
    print("0) Sair do Sistema")
    print("-"*30)

    # ÁREA DO CLIENTE (Aparece após o login ser True)
    print("--- OPERAÇÕES BANCÁRIAS ---")
    print("3) Depósito")
    print("4) Saque (Sake)")
    print("5) Ver Extrato")
    print("6) Transferências (Pix)")

    print("\n--- SERVIÇOS E CRÉDITO ---")
    print("7) Empréstimo")
    print("8) Investimentos")
    print("9) Pagamento de Contas")

    print("\n--- GESTÃO E SEGURANÇA ---")
    print("10) Alterar Senha")
    print("11) Bloquear/Desbloquear Cartão")
    print("12) Ver Dados do Perfil")
    print("13) Listar Todos os Clientes (Adm)")
    print("="*30)

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Obrigado por usar o Python Bank. Até logo!")
        break
