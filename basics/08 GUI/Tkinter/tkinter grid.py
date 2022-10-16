import tkinter as tk

window = tk.Tk()

b1 = tk.Button(window, bg='red', text='Button 1')
b1.grid(row=0, column=0, ipadx=5, ipady=5)

b2 = tk.Button(window, bg='green', text='Button 2')
b2.grid(row=0, column=1, ipadx=5, ipady=5)

b3 = tk.Button(window, bg='silver', text='Button 3')
b3.grid(row=0, column=2, ipadx=5, ipady=5, rowspan=2, sticky='ns')

b4 = tk.Button(window, bg='yellow', text='Button 4')
b4.grid(row=1, column=0, ipadx=5, ipady=5)

b5 = tk.Button(window, bg='yellow', text='Button 5')
b5.grid(row=1, column=1, ipadx=5, ipady=5)

#b6 = tk.Button(window, bg='yellow', text='Button 6')
#b6.grid(row=1, column=2, ipadx=5, ipady=5)

b7 = tk.Button(window, bg='red', text='Button 7')
b7.grid(row=2, column=0, ipadx=5, ipady=5, columnspan=3, sticky='ew')

window.mainloop()