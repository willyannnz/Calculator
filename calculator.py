def sum(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return "Erro: Não é possivel dividir por zero(0)."
    return a / b

operations = {
    "1": sum,
    "2": subtract,
    "3": multiply,
    "4": divide
}

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
    if opcao not in operations:
        print("Opção inválida!")
        continue

    try:
        number1 = float(input("Digite o primeiro número: "))
        number2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Digite apenas números.")
        continue
    function = operations[opcao]
    result = function(number1, number2)

    if result is None:
        print("Erro: Operação inválida.")
    else:
        print(f"Resultado: {result}")

