import tkinter as tk

win = tk.Tk()

value = tk.DoubleVar()
scale = tk.Scale(win, from_=0, to=100, orient=tk.VERTICAL, variable=value)
scale.pack(anchor=tk.CENTER)

def selected():
    selection = 'Value: ' + str(value.get())
    label.config(text=selection)
    label.after(50, selected)

label = tk.Label(win)
label.pack()

selected()

win.mainloop()