import tkinter as tk

win = tk.Tk()

def radio_clicked():
    print('radio_value:', radio_value.get())

radio_value = tk.IntVar()

radio_1 = tk.Radiobutton(win, text='Option 1', variable=radio_value, value=1, command=radio_clicked)
radio_2 = tk.Radiobutton(win, text='Option 2', variable=radio_value, value=2, command=radio_clicked)
radio_3 = tk.Radiobutton(win, text='Option 3', variable=radio_value, value=3, command=radio_clicked)

radio_1.pack()
radio_2.pack()
radio_3.pack()

win.mainloop()