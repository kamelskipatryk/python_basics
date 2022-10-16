import tkinter as tk

window = tk.Tk()

label_1 = tk.Label(window, text='Label 1')
label_1.place(x=0, y=20, width=50, height=35)

label_2 = tk.Label(window, text='Label 2', bg='red')
label_2.place(x=70, y=70, width=90, height=35)

window.mainloop()



