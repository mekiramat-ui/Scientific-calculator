
import tkinter as tk
from tkinter import ttk
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)

        self.expression = ""
        self.input_text = tk.StringVar()

        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 14), padding=10)
        self.style.configure("TFrame", background="#f0f0f0")

        self.create_widgets()

    def create_widgets(self):
        input_frame = ttk.Frame(self.root, style="TFrame")
        input_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        input_field = tk.Entry(input_frame, textvariable=self.input_text, font=("Arial", 24), bd=0, insertwidth=2, width=14, borderwidth=0, highlightthickness=0, justify='right')
        input_field.grid(row=0, column=0, columnspan=4, ipady=10)

        buttons_frame = ttk.Frame(self.root, style="TFrame")
        buttons_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        buttons = [
            ('sin', 1, 0), ('cos', 1, 1), ('tan', 1, 2), ('log', 1, 3),
            ('ln', 2, 0), (')', 2, 1), ('(', 2, 2), ('^', 2, 3),
            ('sqrt', 3, 0), ('7', 3, 1), ('8', 3, 2), ('9', 3, 3),
            ('C', 4, 0), ('4', 4, 1), ('5', 4, 2), ('6', 4, 3),
            ('<-', 5, 0), ('1', 5, 1), ('2', 5, 2), ('3', 5, 3),
            ('/', 6, 0), ('*', 6, 1), ('-', 6, 2), ('+', 6, 3),
            ('0', 7, 0), ('.', 7, 1), ('pi', 7, 2), ('=', 7, 3),
        ]

        for (text, row, col) in buttons:
            button = ttk.Button(buttons_frame, text=text, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew", padx=1, pady=1)

        for i in range(8):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char in ('sin', 'cos', 'tan', 'log', 'ln', 'sqrt'):
            self.expression += f"{char}("
        elif char == '=':
            self.calculate()
        elif char == 'C':
            self.clear()
        elif char == '<-':
            self.backspace()
        else:
            self.expression += str(char)
        self.input_text.set(self.expression)

    def calculate(self):
        try:
            # Replace scientific function names with math module calls
            self.expression = self.expression.replace('sin', 'math.sin')
            self.expression = self.expression.replace('cos', 'math.cos')
            self.expression = self.expression.replace('tan', 'math.tan')
            self.expression = self.expression.replace('log', 'math.log10')
            self.expression = self.expression.replace('ln', 'math.log')
            self.expression = self.expression.replace('sqrt', 'math.sqrt')
            self.expression = self.expression.replace('pi', 'math.pi')
            self.expression = self.expression.replace('e', 'math.e')
            self.expression = self.expression.replace('^', '**')

            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except:
            self.input_text.set("Error")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.input_text.set("")

    def backspace(self):
        self.expression = self.expression[:-1]
        self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop()
