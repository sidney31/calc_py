import tkinter as tk
from tkinter import ttk


class View(tk.Tk):
    def __init__(self, controller) -> None:
        super().__init__()
        self.controller = controller 
        

    def main(self):
        self.title("Калькулятор")
        self.resizable(width=False, height=False)
        self.iconbitmap(default="resources\\icon.ico")

        self.res = tk.StringVar()
        self.RootFrame = ttk.Frame(self)
        self.RootFrame.pack(padx=10, pady=10)
 
        buttons = [
            ["!", "√", "e", "%", "←", "C"],
            ["x²", "ʸ√x", "ln", "lg", "logᵧ", "÷"],
            ["xʸ", "π", 7, 8, 9, "×"],
            ["(", "tg", 4, 5, 6, "-"],
            [")","cos", 1, 2, 3, "+"],
            [",", "sin", 0, "00", ".", "="],
        ]

        EnterField = ttk.Entry(self.RootFrame,
                               state="disable",
                               textvariable=self.res, 
                               justify="right")
         
        EnterField.pack(side="top", fill="x")

        ButtonFrame = ttk.Frame(self.RootFrame, height=250, width=250)
        ButtonFrame.pack(side="bottom")

        for x in range(6):
            for y in range(6):
                btn = ttk.Button(ButtonFrame,
                                 text = f"{buttons[x][y]}",
                                 command = lambda button = buttons[x][y]: self.controller.ButtonHandler(button))
                btn.grid(row = x, column=y, ipady=5, ipadx=0)

        self.mainloop()

# +, 
# -, 
# /, 
# *, 
# %, 
# !, 
# ^2,
# ^x,
# sqrt, 
# x^sqrt, 
# sin, 
# cos, 
# tg, 
# ln10, 
# lne, 
# pi, 
# e, 
# C, 
# C<