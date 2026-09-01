import tkinter as tk
from core import operations

window = tk.Tk()

#Window title and size
window.title("Calculadora")
window.geometry("300x400")

#This will create a display for the calculator
display = tk.Entry(window)
display.grid(row=0, column=0)


window.mainloop()

