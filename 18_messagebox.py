from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import title

root = Tk()
root.title("Il nostro programma")
root.geometry('600x400')
root.iconbitmap('./img/mushroom_super.ico')


def show_message():
    simply_message = messagebox.showinfo(title='Errore', message="questo è un messaggio di errore!")
    domanda_tattica = messagebox.askokcancel(title='we wagliò', message='BudkaStroooong')

    if domanda_tattica:
        root.destroy()


button = ttk.Button(root, text="Mostra messaggio", command=show_message)
button.pack(fill=BOTH, padx=10, pady=10)

root.mainloop()
