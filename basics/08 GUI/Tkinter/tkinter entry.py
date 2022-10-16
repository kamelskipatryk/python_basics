import tkinter as tk

win = tk.Tk()
win.geometry("500x200")

tk.Label(win, text='First name:').grid(row=0, column=0)

entry = tk.Entry(win)
entry.grid(row=0,column=1)
entry.insert(0, 'hello') # wpisane od początku, nie przez usera

def show_data():
    print('Entry data:', entry.get())
    entry.delete(0, 'end') # kasujemy od poczatku do końca z pola entry po kliknięciu w button

button_1 = tk.Button(win, text='show info', command=show_data).grid(row=1) # column domyślnie 0

win.mainloop()
