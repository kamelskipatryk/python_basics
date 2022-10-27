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
        win.geometry('260x130')
        self.expression_field = tk.Entry(win, textvariable=self.equation_str_var)
        self.expression_field.grid(columnspan = 4, ipadx=60)

        # przechodzenie po klawiaturze
        row_index = 0
        while row_index < len(self.calculator_keyboard):
            calc_row = self.calculator_keyboard[row_index]

            column_index = 0
            while column_index < len(calc_row):
                button_text = calc_row[column_index]
                button = tk.Button(win, text=button_text, height=1, width=8, fg='black', bg='silver', command= lambda v=button_text: self.button_pressed(v))
                button.grid(row = row_index + 1, column=column_index)
                column_index += 1
            
            row_index += 1

    def button_pressed(self, value):
        print('button pressed:', value)

        if value == 'C':
            self.expression_str = ''
            self.equation_str_var.set('')
            return

        if value == '=':
            result = str( eval(self.expression_str) )
            self.expression_str = result
            self.equation_str_var.set(result)
            return
        
        self.expression_str += str(value)
        self.equation_str_var.set( self.expression_str )


calculator = Calculator(win)
win.mainloop()












win.mainloop()