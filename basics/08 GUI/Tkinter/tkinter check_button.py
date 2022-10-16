import tkinter as tk

win = tk.Tk()

def value_changed():
    if cb_value.get() == 0:
        print('Chech button is of')
    if cb_value.get() == 1:
        print('Chech button is on')


cb_value = tk.IntVar(value=0)
c_1 = tk.Checkbutton(win, text='accept tos', variable=cb_value, onvalue=1, offvalue=0, command=value_changed)
c_1.grid(row=0)




win.mainloop()