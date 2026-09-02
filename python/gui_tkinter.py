import tkinter as tk
from core import operations

#This will create a list of numbers for the calculator (0 is placed separately, spanning the bottom row)
number_rows = ["7", "8", "9", "4", "5", "6", "1", "2", "3"]
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
window.geometry("300x450")

#This will create a grid layout for the calculator
for coluna in range(4):
    window.columnconfigure(coluna, weight=1)
for linha in range(6):
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

    #Here we check if the result is None, which means that the operation was invalid (like division by zero)
    if result is None:
        display.delete(0, tk.END)
        display.insert(tk.END, "Erro: Divisão por zero")
        accumulated_result = None
        pending_operator = None 
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

def backspace():
    current_text = display.get()
    if current_text:
        display.delete(len(current_text) - 1, tk.END)
#This will create the number buttons 7-9, 4-6, 1-3, aligned in a 3x3 grid
for i, number in enumerate(number_rows):
    button = tk.Button(
        window,
        text=number,
        bg="lightgray",
        fg="black",
        command=lambda num=number: add_number(num)
    )

    line = i // 3 + 2
    column = i % 3

    button.grid(row=line, column=column, sticky="nsew")

#This will create the "0" button, spanning the first three columns of the bottom row
button_zero = tk.Button(window,text="0",bg="lightgray",fg="black",command=lambda: add_number("0"))
button_zero.grid(row=5, column=0, columnspan=3, sticky="nsew")

#This will create the operator buttons, each aligned with its matching row of numbers
button_divide = tk.Button(window, text="/", bg="orange", fg="white", command=lambda: add_operator("/"))
button_divide.grid(row=1, column=3, sticky="nsew")

#This will create the operator buttons, each aligned with its matching row of numbers
button_multiply = tk.Button(window, text="*", bg="orange", fg="white", command=lambda: add_operator("*"))
button_multiply.grid(row=2, column=3, sticky="nsew")

#This will create the operator buttons, each aligned with its matching row of numbers
button_subtract = tk.Button(window, text="-", bg="orange", fg="white", command=lambda: add_operator("-"))
button_subtract.grid(row=3, column=3, sticky="nsew")

#This will create the operator buttons, each aligned with its matching row of numbers
button_add = tk.Button(window, text="+", bg="orange", fg="white", command=lambda: add_operator("+"))
button_add.grid(row=4, column=3, sticky="nsew")

#This will create the equal button for the calculator
button_equal = tk.Button(window,text="=",bg="green",fg="white",command=calculate)
button_equal.grid(row=5, column=3, sticky="nsew")

#This will create the clear button, spanning the first two columns of the top row
button_clear = tk.Button(window,text="C",bg="red",fg="white",command=clear_all)
button_clear.grid(row=1, column=0, columnspan=2, sticky="nsew")

#This will create the backspace button for the calculator
button_backspace = tk.Button(window,text="←",bg="lightgray",fg="black",command=backspace)
button_backspace.grid(row=1, column=2, sticky="nsew")

window.mainloop()