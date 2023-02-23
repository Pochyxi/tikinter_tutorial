from tkinter import *
from tkinter import ttk
from tkinter import filedialog

root = Tk()
root.title("Il nostro programma")
root.geometry('600x400')
root.iconbitmap('./img/mushroom_super.ico')


def apri_file():
    filetypes = (
        ('file di testo', '*.txt'),
        ('tutti i file', '*.*')
    )
    f = filedialog.asksaveasfile(mode='w', title='apri un file', initialdir='/', filetypes=filetypes)
    data = " wqweqwe qasdasd sdfsdfso"
    f.write(data)
    f.close()


bottone = ttk.Button(root, text='apri file', command=apri_file)
bottone.pack(expand=True)

root.mainloop()
