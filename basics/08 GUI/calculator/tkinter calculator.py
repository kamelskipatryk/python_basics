import tkinter as tk

win = tk.Tk()
win.title('Calculator')

class Calculator:
    def __init__(self, win):
        self.equation_str_var = tk.StringVar() # działanie
        self.expression_str = '' # wyrażenie
        self.calculator_keyboard = [
            ['7','8','9','+'],
            ['4','5','6','-'],
            ['1','2','3','*'],
            ['0', 'C','=','/']
        ]
        self.prepare_gui(win)

    def prepare_gui(self, win):
        

calculator = Calculator(win)












win.mainloop()