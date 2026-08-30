def sum(a,b):
    return a + b

def substract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return "Erro: Não é possivel dividir por zero(0)."
    return a / b


def show_menu():
    print("\n======CALCULADORA======")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Sair")


while True:
    show_menu()

    opcao = input("Digite uma opção: ")

    if opcao == "0":
        print("Calculadora Encerrada!")
        break
    if opcao not in ["1","2","3","4"]:
        print("Opção inválida!")
        continue

    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Digite apenas números.")
        continue

    if opcao == "1":
        resultado = sum(numero1, numero2)

    elif opcao == "2":
        resultado = substract(numero1, numero2)

    elif opcao == "3":
        resultado = multiply(numero1, numero2)

    elif opcao == "4":
        resultado = divide(numero1, numero2)

    print(f"Resultado: {resultado}")
