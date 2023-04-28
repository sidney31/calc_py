import tkinter as tk
from tkinter import ttk

class View(tk.Tk):
    
    def __init__(self, controller) -> None:
        super().__init__()
        self.controller = controller 
        
    def main(self):
        self.title("Калькулятор")
        self.resizable(width=False, height=False) #запрет на изменение размера окна

        self.res = tk.StringVar() # переменная для результата

        self.RootFrame = ttk.Frame(self) #родительский контейнер для удобного позиционирование всех элементов 
        self.RootFrame.pack(padx=10, pady=10)
 
        #матрица, определяющая значение кнопки и ее координаты на сетке
        buttons = [
            ["ln", "lg", "!", "C", "←"],
            ["e",  "π", "(", ")", "÷"],
            ["sin", "√", "ʸ√x", "%", "×"],
            ["cos", 7, 8, 9, "+"],
            ["tan", 4, 5, 6, "-"],
            ["x²", 1, 2, 3, "="],
            ["xʸ", "00", 0, ","],
        ]

        #поле вывода
        Output = ttk.Label(self.RootFrame, textvariable=self.res, anchor="sw", font=("Arial", 14), background="#d6d6d6")
        Output.pack(side="top", fill="x")

        #поле для кнопок
        ButtonFrame = ttk.Frame(self.RootFrame, height=250, width=250)
        ButtonFrame.pack(side="bottom")

        #расположение кнопок по сетке
        for x in range(7):
            for y in range(5):
                if x == 6 and y == 4:
                    continue

                btn = ttk.Button(ButtonFrame,
                                 text = f"{buttons[x][y]}",
                                 command = lambda button = buttons[x][y]: self.controller.ButtonHandler(button)) #создание кнопки, привязка к ней функции, в аргумент которой передается значение кнопки
                btn.grid(row = x, 
                         column = y, 
                         ipady = 23 if x == 5 and y == 4 else 5, 
                         ipadx = 0, 
                         rowspan = 2 if x == 5 and y == 4 else 1) 

        self.mainloop()
