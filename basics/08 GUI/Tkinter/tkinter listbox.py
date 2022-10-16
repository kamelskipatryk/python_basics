import tkinter as tk

win = tk.Tk()
scrollbar = tk.Scrollbar(win)

list_box = tk.Listbox(win, selectmode=tk.MULTIPLE)

scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
list_box.pack(fill=tk.Y)
scrollbar.config(command=list_box.yview)
list_box.config(yscrollcommand=scrollbar.set)

for i in range(1,11):
    list_box.insert(tk.END, str(i))

label = tk.Label(win)
label.pack()

def check_list():
    selected_indices = list_box.curselection()
    selected_langs = ",".join([list_box.get(i) for i in selected_indices])
    label.config(text=str(selected_langs))
    label.after(200, check_list)

check_list()

win.mainloop()