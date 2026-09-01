from core import operations


def show_menu():
    print("\n======CALCULADORA======")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Sair")


while True:
    show_menu()
    option = input("Digite uma opção: ")

    if option == "0":
        print("Calculadora Encerrada!")
        break
    if option not in operations:
        print("Opção inválida!")
        continue

    try:
        number1 = float(input("Digite o primeiro número: "))
        number2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Digite apenas números.")
        continue

    function = operations[option]
    result = function(number1, number2)

    if result is None:
        if option == "4":
            print("Erro: Divisão por zero é inválida.")
        else:
            print("Erro: Operação inválida.")
    else:
        print(f"Resultado: {result}")
