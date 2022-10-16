import tkinter as tk

win = tk.Tk()

scrollbar = tk.Scrollbar(win)
text_box = tk.Text(win, height=5, width=30,padx=5,pady=5, font='Times 18 bold')

scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_box.pack(side=tk.LEFT, fill=tk.Y)

scrollbar.config(command=text_box.yview)
text_box.config(yscrollcommand=scrollbar.set)

text_box.insert(tk.END, 'hello worldldldld \n heloo two times')

print('text data:', text_box.get(1.0, 'end'))


win.mainloop()