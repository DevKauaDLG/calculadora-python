print("Escolha uma opção para realizar uma operação")
print("1 - Soma")
print("2 - Subtração")
print("3 - Divisão")
print("4 - Multiplicação")

escolha = int(input("Escolha: "))

if escolha in [1, 2, 3, 4]:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == 1:
        print(f"A soma desses números é {num1 + num2}")
    elif escolha == 2:
        print(f"A subtração desses números é {num1 - num2}")
    elif escolha == 3:
        if num2 == 0:
            print("Não é possível dividir por zero")
        else:
            print(f"A divisão desses números é {num1 / num2}")
    elif escolha == 4:
        print(f"A multiplicação desses números é {num1 * num2}")
else:
    print("Opção inválida")