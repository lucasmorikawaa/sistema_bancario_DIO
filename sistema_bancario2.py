saldo = 0
opcao = 0
limite = 0
LIMITE_DE_SAQUE = 3
extrato = ""

while opcao != 4:

    opcao = int(input("""
============= SISTEMA BANCARIO =============
    
            [1] Deposito
            [2] Saque
            [3] Extrato
            [4] Sair

        Selecione uma das opções: """))

    if opcao == 1:
        print("\n==================== Deposito ====================")
        deposito = int(input("\nDigite o valor que você deseja depositar: "))

        if deposito > 0:
            saldo += deposito

            print(f"\nDeposito realizado com sucesso! \nAqui está seu saldo atual: R$ {saldo:.2f}")

            extrato += f"Deposito: R$ {deposito:.2f}\n"
        else:
            print("\nVoce nao pode depositar valores negativos!")

    elif opcao == 2:
        print("\n==================== Saque ====================")
        saque = int(input("\nDigite o valor que voce deseja sacar: "))

        if saque > saldo:
            print(f"\nSaldo insuficiente! \nSeu saldo atual: R$ {saldo:.2f}")
            while saque > saldo:
                saque = int(input("\nDigite o valor que voce deseja sacar novamente: "))
                saldo -= saque

                print(f"\nSaque realizado com sucesso! \nSeu saldo atual: R$ {saldo:.2f}")

        else:

            limite += 1

            if limite > LIMITE_DE_SAQUE:
                print(f"\nVocê atingiu o limite de saque diário!")

            else:
                if saque <= 500:
                    saldo -= saque
                    extrato += f"Saque: R$ {saque:.2f}\n"

                    print(f"\nSaque realizado com sucesso! \nSeu saldo atual: R$ {saldo}")
                else:
                    print("\nO limite maximo de saque é R$ 500!")

    elif opcao == 3:
         print("\n==================== Extrato ====================")
         print("Nao foram realizados movimentações!" if not extrato else extrato)
         print(f"Saldo: R$ {saldo:.2f}")

           

        

        

        