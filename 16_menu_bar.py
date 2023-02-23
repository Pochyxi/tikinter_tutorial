from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Il nostro programma")
root.geometry('600x400')
root.iconbitmap('./img/mushroom_super.ico')

# creo il mio menu
menubar = Menu(root)
# inserisco il menù nella root
root.config(menu=menubar)

# creo la box che conterrà i vari elementi del menu
file_menu = Menu(menubar, tearoff=0)
# queste sono le singole voci del menu
file_menu.add_command(label='New', command=root.quit)
file_menu.add_command(label='Open', command=root.quit)


# creo un sottomenu all'interno del box menu
file_altro_submenu = Menu(file_menu, tearoff=0)

# aggiungo una voce al sottomenu
file_altro_submenu.add_command(label='buongiorno')

# questo è il nome del box che si apre al click
menubar.add_cascade(label='File', menu=file_menu)
file_menu.add_cascade(label='Altro', menu=file_altro_submenu)

# separatore a forma di linea
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)

root.mainloop()
