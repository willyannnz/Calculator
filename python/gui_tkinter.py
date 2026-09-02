import tkinter as tk
from core import operations

#This will create a list of numbers and operators for the calculator
numbers = ["7", "8", "9", "4", "5", "6", "1", "2", "3", "0"]
operators = ["+", "-", "*", "/"]
#Here the operator_map will map the operator to the corresponding operation in the operations dictionary
operator_map = {
    "+": "1",
    "-": "2",
    "*": "3",
    "/": "4"
}

#This will create a variable to store the accumulated result and the pending operator
accumulated_result = None
pending_operator = None

#Window creation
window = tk.Tk()

#Window title and size
window.title("Calculadora")
window.geometry("300x400")

#This will create a grid layout for the calculator
for coluna in range(4):
    window.columnconfigure(coluna, weight=1)
for linha in range(5):
    window.rowconfigure(linha, weight=1)

#This will create a display for the calculator
display = tk.Entry(window, font=("Arial", 20))
display.grid(row=0, column=0, columnspan=4, sticky="nsew")

#This will add numbers to the display when the buttons are pressed
def add_number(number):
    display.insert(tk.END, str(number))

#This will apply the pending operation (if any) and store the new operator,
#so we can chain as many operations as the user wants (2 + 3 + 5 + ...)
def add_operator(operation):
    global accumulated_result, pending_operator

    current_number = float(display.get())

    if accumulated_result is None:
        #first number typed: nothing to accumulate yet
        accumulated_result = current_number
    else:
        #there's already a pending operation: apply it before storing the new one
        function = operations[operator_map[pending_operator]]
        accumulated_result = function(accumulated_result, current_number)

    pending_operator = operation

    display.delete(0, tk.END)


#This will apply the last pending operation and show the final result
def calculate():
    global accumulated_result, pending_operator

    #Here we check if there's a pending operation to apply, if not we just return the current number
    if pending_operator is None:
        #no operation to apply, just return the current number
        display.delete(0, tk.END)
        display.insert(tk.END, "Digite uma operação antes de calcular")
        return 


    current_number = float(display.get())

    function = operations[operator_map[pending_operator]]
    result = function(accumulated_result, current_number)

    if result is None:
        display.delete(0, tk.END)
        display.insert(tk.END, "Erro: Divisão por zero")
        return


    display.delete(0, tk.END)
    display.insert(tk.END, str(result))

    #reset so the next calculation starts clean
    accumulated_result = None
    pending_operator = None

def clear_all():
    global accumulated_result, pending_operator
    accumulated_result = None
    pending_operator = None
    display.delete(0, tk.END)

#This will create the buttons numbers for the calculator
for i, number in enumerate(numbers):
    button = tk.Button(
        window,
        text = number,
        command = lambda num=number: add_number(num)
    )

    line = i // 3 + 1
    column = i % 3

    button.grid(row=line, column=column, sticky="nsew")


#This will create the operator buttons for the calculator
for i, operation in enumerate(operators):
    button = tk.Button(
        window,
        text=operation,
        command=lambda op=operation: add_operator(op)
    )

    button.grid(row=i + 1, column=3, sticky="nsew")

#This will create the equal button for the calculator
button_equal = tk.Button(
    window,
    text="=",
    command=calculate
)
button_equal.grid(row=4, column=1, sticky="nsew")

#This will create the clear button for the calculator
button_clear = tk.Button(
    window,
    text="C",
    command=clear_all
)
button_clear.grid(row=4, column=2, sticky="nsew")

window.mainloop()

