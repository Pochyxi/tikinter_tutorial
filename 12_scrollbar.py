from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Il nostro programma")
root.geometry('600x400')
root.iconbitmap('./img/mushroom_super.ico')

# configuro nella root una colonna
root.columnconfigure(0, weight=1)
# configuro nella root una riga
root.rowconfigure(0, weight=1)

# questo è la tupla che contiene stringhe
linguaggi = (
    'javascript', 'java', 'c', 'c++', 'python', 'php', 'ruby', 'go', 'javascript', 'java', 'c', 'c++', 'python', 'php',
    'ruby', 'go', 'javascript', 'java', 'c', 'c++', 'python', 'php', 'ruby', 'go', 'javascript', 'java', 'c', 'c++',
    'python', 'php', 'ruby', 'go')
# questa è la variabile da inserire nella listbox come listvariable
linguaggio_selezionato = StringVar(value=linguaggi)

# creo una listbox e la inserisco
list_box = Listbox(root, listvariable=linguaggio_selezionato, height=6, selectmode='extended')
list_box.grid(column=0, row=0, sticky='nwes')

scroll_bar = ttk.Scrollbar(root, orient='vertical', command=list_box.yview)
scroll_bar.grid(row=0, column=1, sticky='ns')

list_box['yscrollcommand'] = scroll_bar.set

root.mainloop()
