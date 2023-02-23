from tkinter import *
from tkinter import ttk

# creazione del menu che si pare al click del tasto destro del mouse

root = Tk()
root.title("Il nostro programma")
root.geometry('600x400')
root.iconbitmap('./img/mushroom_super.ico')

# creo un frame che si prenderà tutta la dimensione disponibile della root
frame = Frame(root, background='red')
frame.pack(expand=True, fill=BOTH)

# creo il menu, tearoff=0 seerve per non far comparire la linea fastidiosa
ctx_menu = Menu(root, tearoff=0)
# di seguito aggiungo i comandi
ctx_menu.add_command(label='Taglia')
ctx_menu.add_command(label='Copia')
ctx_menu.add_command(label='Incolla')
# aggiungo un separatore
ctx_menu.add_separator()
ctx_menu.add_command(label='Prova')


# la funzione che verrà attivata al click del tasto destro del mouse
def ctx_menu_popup(event):
    try:
        ctx_menu.tk_popup(event.x_root, event.y_root)
    finally:
        ctx_menu.grab_release()


# qui collego la premuta del tasto destro all'apertura del menu
frame.bind('<Button-3>', ctx_menu_popup)

root.mainloop()
