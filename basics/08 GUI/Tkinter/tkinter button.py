import tkinter as tk

window = tk.Tk()

def button_clicked():
    print('clicked!')
    quit()

button = tk.Button(
    window,
    text='Quit',
    bd=10, # border(px)
    fg='red',
    bg='green',
    activeforeground='black',
    activebackground='silver',
    font='Times 18 bold',
    height=3,
    width=20,
    padx=10,
    pady=10,
    relief='groove', #styl obramowania
    command=button_clicked
)

button.pack()
window.mainloop()