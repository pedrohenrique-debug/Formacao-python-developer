conta = 300
contador = 0

while (True):
    print("1- Sacar")
    print("2- Depositar")
    print("3- Visualizar Extrato")
    print("0- Sair")
    opcao = int(input("Digite a opção desejada: "))
    match opcao:
        case 1:
            if contador > 3:
                print("Você atingiu o limite de 3 saques hoje. Tente novamente amanhã")
            else:
                sacar = float(input("Qual valor deseja sacar? "))
                if sacar > 500:
                    while(True):
                        print("O limite de saque é de R$ 500.00 tente novamente com um valor menor")
                        sacar = float(input("Qual valor deseja sacar? "))
                        if sacar <= 500:
                            break
                elif sacar > conta:
                    while(True):
                        print("Saldo da conta é menor que o valor do saque, tente novamente com um valor menor")
                        sacar = float(input("Qual valor deseja sacar? "))
                        if sacar <= conta:
                            conta -= sacar
                            break

                else:
                    conta -= sacar
        case 2:
            while(True):
                depositar = float(input("Quanto deseja depositar? "))
                if depositar <= 0:
                    print("Não é possivel depositar valor menor ou igual a 0")
                else:
                    break
            conta += depositar

        case 3:
            print(f"R${conta:.2f}")
        case 0:
            break
    contador += 1 
    
