import tkinter as tk
from core import operations

window = tk.Tk()

#Window title and size
window.title("Calculadora")
window.geometry("300x400")

for coluna in range(4):
    window.columnconfigure(coluna, weight=1)
for linha in range(6):
    window.rowconfigure(linha, weight=1)

#This will create a display for the calculator
display = tk.Entry(window, font=("Arial", 20))
display.grid(row=0, column=0, columnspan=4, sticky="nsew")

def add_number(number):
    display.insert(tk.END, str(number))
def add_operator(operator):
    display.insert(tk.END, str(operator))
    
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

for i, operator in enumerate(operators):
    button = tk.Button(
        window,
        text = operator,
        command = lambda op=operator: add_operator(op)
    )

    button.grid(row=i + 1, column=3, sticky="nsew")

window.mainloop()

