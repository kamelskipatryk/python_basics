
import tkinter as tk

win = tk.Tk()

def menu_item_selected():
    print('menu item selected')

def menu_item_close_selected():
    print('Application has been closed.')
    quit()

root_menu = tk.Menu(win)

file_menu = tk.Menu(root_menu)
file_menu.add_command(label='New', command=menu_item_selected)
file_menu.add_command(label='Open', command=menu_item_selected)
file_menu.add_command(label='Save', command=menu_item_selected)
file_menu.add_command(label='Save as', command=menu_item_selected)
file_menu.add_separator()
file_menu.add_command(label='Close', command=menu_item_close_selected)

edit_menu = tk.Menu(root_menu)
edit_menu.add_command(label='Cut', command=menu_item_selected)
edit_menu.add_command(label='Copy', command=menu_item_selected)
edit_menu.add_command(label='Paste', command=menu_item_selected)
edit_menu.add_command(label='Config', command=menu_item_selected)

root_menu.add_cascade(label='File', menu=file_menu)
root_menu.add_cascade(label='Edit', menu=edit_menu)
win.config(menu=root_menu)


win.mainloop()