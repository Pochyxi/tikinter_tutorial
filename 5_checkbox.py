from tkinter import *
from tkinter import ttk


# Su tkinter si chiamano Check Buttons

def premo_check():
    label = Label(text=nome.get())
    label.pack()


root = Tk()
root.title("Il nostro programma")
root.geometry("600x400+50+50")
root.iconbitmap('./img/mushroom_super.ico')

nome = StringVar()
check = Checkbutton(text='Ciao',
                    font=('Helvetica', 24),
                    command=premo_check,  # la funzione che verrà chiamata in causa al click del check
                    variable=nome,  # la variabile che rappresenta il valore della checkbox
                    offvalue='luca',  # specifica che se la checkbox è deselezionata assumerà il seguente valore
                    onvalue='marco')  # specifica che se la checkbox selezionata assumerà il seguente valore
check.pack()

root.mainloop()
