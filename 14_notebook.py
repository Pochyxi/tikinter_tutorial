from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Il nostro programma")
root.geometry('600x400')
root.iconbitmap('./img/mushroom_super.ico')

# creo l'intero notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10, fill=BOTH, expand=True)

# i frame rappresentano i contenitori
frame1 = ttk.Frame(notebook, width=400, height=280)
frame2 = ttk.Frame(notebook, width=400, height=280)

# li inseriamo
frame1.pack(fill=BOTH, expand=True)
frame2.pack(fill=BOTH, expand=True)

# creiamo le tab che visualizzeranno i contenitori (i menu)
notebook.add(frame1, text='tab1')
notebook.add(frame2, text='tab2')

# insieriamo del contenuto all'interno dei contenitori
label1 = Label(frame1, text='ciao')
label1.pack()
label2 = Label(frame2, text='buongiorno')
label2.pack()

root.mainloop()
