from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Il nostro programma")
root.geometry("600x400+50+50")
root.iconbitmap('./img/mushroom_super.ico')

genere = StringVar()
r1 = ttk.Radiobutton(root, text='maschio', value='m', variable=genere)
r1.pack()
r2 = ttk.Radiobutton(root, text='femmina', value='f', variable=genere)
r2.pack()

button = ttk.Button(root, text='stampa genere, guarda sul Run', command=lambda: print(genere.get()))
button.pack()

taglia_selezionata = StringVar()
taglie = (
    ('Small', 'S'),
    ('Medium', 'M'),
    ('Large', 'L'),
    ('Extra large', 'XL'),
)

for taglia in taglie:
    r = ttk.Radiobutton(root, text=taglia[0], value=taglia[1], variable=taglia_selezionata)
    r.pack(padx=5, pady=5)

button_prova = ttk.Button(root, text='Seleziona una taglia e premimi', command=lambda: print(taglia_selezionata.get()))
button_prova.pack()

root.mainloop()

