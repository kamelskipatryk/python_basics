import tkinter as tk

window = tk.Tk()

label_1 = tk.Label(window, text='Label 1', bg='red')
label_1.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

label_2 = tk.Label(window, text='Label 2', bg='silver')
label_2.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)

button_1 = tk.Button(window, bg='red', text='button 1')
button_1.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

button_2 = tk.Button(window, bg='yellow', text='button 2')
button_2.pack(side=tk.RIGHT, expand=True, fill=tk.Y)

window.mainloop()






