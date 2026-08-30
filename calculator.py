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
    print("1.Somar")
    print("2.Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Sair")



