from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Il nostro programma")
root.geometry("600x400+50+50")
root.iconbitmap('./img/mushroom_super.ico')
# root.resizable(False,
#                False)  # Permette di ridimensionare o meno la finestra(prima parametro larghezza e secondo altezza)

root.minsize(400, 100)  # specifica la dimensione minima della finestra
root.maxsize(1000, 1000)  # specifica la dimensione massima della finestra

# root.attributes('-alpha', 0.5) # opacità della finestra

# root.attributes('-topmost', 1) #  la finestra sarà sempre visibile sopra le altre

# root.lift()  # la finestra comparirà davanti a tutte le altre finestre

# root.lower()  # la finestra comparirà dietro alle altre finestre

root.mainloop()  # tiene il programma costantemente aperto
