import tkinter as tk

win = tk.Tk()

def spin_value():
    label.config(text= str(spin.get()))

spin = tk.Spinbox(win, from_=0, to=50, command=spin_value)
spin.pack()

label = tk.Label(win)
label.pack()


win.mainloop()