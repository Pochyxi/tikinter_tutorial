from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Il nostro programma")
root.geometry('600x400')
root.iconbitmap('./img/mushroom_super.ico')
# meglio conosciuta come tabella

# qui creiamo le nostre tre colonne
colonne = ('nome', 'cognome', 'email')
# qui creiamo la nostra tabella
tabella = ttk.Treeview(root,
                       columns=colonne,
                       show='headings')  # serve per mostrare i titoli delle colonne

# di seguito le colonne
tabella.heading('nome', text='Nome')
tabella.heading('cognome', text='cognome')
tabella.heading('email', text='email')

# popolo la mia tabella
righe = []
for n in range(1, 50):
    righe.append((f'nome {n}', f'cognome {n}', f'email {n}'))

# una volta popolato la mia lista creo le righe
for riga in righe:
    tabella.insert('', END, values=riga)

# posiziono la tabella con il layout grid
tabella.grid(row=0, column=0, sticky='nsew')

# creo una scrollbar e la inserisco nella tabella
scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=tabella.yview)
scrollbar.grid(row=0, column=1, sticky='ns')
tabella.configure(yscrollcommand=scrollbar.set)

root.mainloop()
