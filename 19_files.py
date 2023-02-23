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

    # PER APRIRE E LEGGERE IL FILE
    # filename = filedialog.askopenfilename(title='Apri un file', initialdir="/", filetypes=filetypes)
    # print(filename)
    # f = open(filename, 'r')
    # data = f.read()
    # print(data.split('\n'))

    # PER SALVARE UN NUOVO FILE
    f = filedialog.asksaveasfile(mode='w', title='salva file', defaultextension=".txt")
    data = "La mia banda suona il rock!"
    f.write(data)
    f.close()


bottone = ttk.Button(root, text='apri file', command=apri_file)
bottone.pack(expand=True)

root.mainloop()
