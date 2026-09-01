import tkinter as tk
from core import operations

first_number = None
operator = None

window = tk.Tk()

#Window title and size
window.title("Calculadora")
window.geometry("300x400")

for coluna in range(4):
    window.columnconfigure(coluna, weight=1)
for linha in range(5):
    window.rowconfigure(linha, weight=1)

#This will create a display for the calculator
display = tk.Entry(window, font=("Arial", 20))
display.grid(row=0, column=0, columnspan=4, sticky="nsew")

def add_number(number):
    display.insert(tk.END, str(number))

def add_operator(operation):
    global first_number, operator

    first_number = float(display.get())
    operator = operation

    display.delete(0, tk.END)

def calculate():
    second_number = float(display.get())

    function = operations[operator]

    result = function(first_number, second_number)

    display.delete(0, tk.END)
    display.insert(tk.END, str(result))

    
numbers = ["7", "8", "9", "4", "5", "6", "1", "2", "3", "0"]

for i, number in enumerate(numbers):
    button = tk.Button(
        window,
        text = number,
        command = lambda num=number: add_number(num)
    )

    line = i // 3 + 1
    column = i % 3

    button.grid(row=line, column=column, sticky="nsew")

operators = ["+", "-", "*", "/"]

button_equal = tk.Button(
    window,
    text="=",
    command=calculate
)
button_equal.grid(row=4, column=1, sticky="nsew")

for i, operation in enumerate(operators):
    button = tk.Button(
        window,
        text=operation,
        command=lambda op=operation: add_operator(op)
    )

    button.grid(row=i + 1, column=3, sticky="nsew")


window.mainloop()

