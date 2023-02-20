from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Il nostro programma")
# la geometry serve a specificare la dimensione della finestra(primi due valori separati dalla x)
# e il posizionamento della finestra quando aperta(primo valore distanza che manterrà dall'alto, secondo valore
# distanza che manterrà da sinistra)
root.geometry("550x600+50+50")
# metodo per settare l'icona del programma
root.iconbitmap('./img/mushroom_super.ico')
# crea un'immagine che sarà possibile inserire all'interno di un label
photo = PhotoImage(file='img/emoji.png')

# crea un elemento di testo con delle proprietà
label = Label(text='Ciao \n ciao sono Adiener',  # text ----> specifica il testo dell'elemento
              background='red',  # background ----> specifica il colore di sfondo dell'elemento
              padx=50,  # padx ----> determina il padding orizzontale dell'elemento
              pady=50,  # pady ----> determina il padding verticale dell'elemento
              foreground='white',  # foreground ----> specifica il colore di sfondo del testo dell'elemento
              font=('Helvetica', 20),  # font ----> specifica il font dell'elemento e la dimensione dell'elemento
              cursor='circle',  # cursor ----> specifica la tipologia di cursore quando si passa sopra l'elemento
              justify='right',  # justify ----> determina la posizione del testo quando esso è su più righe
              image=photo,  # image ----> specifica l'immagine
              compound='top'  # specifica dove si deve posizionare l'immagine nei confront9i del testo
              )
label.pack()

root.mainloop()
