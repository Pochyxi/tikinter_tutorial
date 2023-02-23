from tkinter import *
from tkinter import ttk
from calendar import month_name

root = Tk()
root.title("Il nostro programma")
root.geometry('600x400')
root.iconbitmap('./img/mushroom_super.ico')

mese_selezionato = StringVar()
combobox = ttk.Combobox(root, textvariable=mese_selezionato)
# impostiamo i values che sono il risultato di un ciclo for fatto sui mesi
combobox['values'] = [month_name[m] for m in range(1, 13)]
# impostiamo lo stato su readonly così da non permettere di scrivere nella combobox
combobox['state'] = 'readonly'

combobox.pack(fill=X, padx=10, pady=10)


def on_combobox_selected(event):
    print(mese_selezionato.get())


combobox.bind('<<ComboboxSelected>>', on_combobox_selected)


root.mainloop()
