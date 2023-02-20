from tkinter import *
from tkinter import ttk


def saluta():
    print("Ho cliccato il bottone")


root = Tk()
root.title("Il nostro programma")
root.geometry("800x600+50+50")
root.iconbitmap('./img/mushroom_super.ico')

button = Button(text='disabilitato',
                background='red', # colore di sfondo
                foreground='white',# colore del contenuto
                width=20,
                borderwidth=10, # spessore del bordo
                # command=saluta) #  funzione richiamata al click
                command=lambda: root.quit())

# button.state(['disabled']) ----> verrà generato un errore dato che il bottone non può essere disabilitato in questo
# modo
button['state'] = 'disabled'

# button.pack()
# button2 = ttk.Button(text='disabilitato ttk',
# command=lambda: root.quit())
# button2.state(['disabled'])
# button2.pack()

photo = PhotoImage(file='./img/emoji.png')
buttonImg = Button(image=photo, text='ti lovvo', compound='bottom')
buttonImg.pack(ipadx=50, ipady=50)

root.mainloop()
