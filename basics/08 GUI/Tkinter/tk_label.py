import tkinter as tk
from PIL import Image
from PIL import ImageTk
import os

script_dir = os.path.dirname(__file__)
os.chdir(script_dir)

window = tk.Tk()
window.title('Application')
logo = ImageTk.PhotoImage(Image.open('autumn.png'))

label_1 = tk.Label(window, 
        text ='Hello World!',
        foreground ='white',
        background ='black',
        width =20, # ilość znaków
        height =3, # ilość lini
        cursor ='dot',
        font = 'Times 18 bold italic underline',
        anchor= tk.CENTER, # umiejscowienie tekstu wewn label
        padx = 5,
        pady = 5
        )
label_1.pack()

label_2 = tk.Label(window, text='Hello again!')
label_2.pack()

label_3 = tk.Label(window,
        text = 'Halo halo',
        image = logo,
        width=200,
        height=200,
        compound=tk.CENTER,
        foreground ='white'
        )
label_3.pack()

label_3.config(text='Haloooooo') # dynamiczna zmiana np. tekstu

window.mainloop()
