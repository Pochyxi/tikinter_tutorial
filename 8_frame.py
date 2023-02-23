from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Il nostro programma")
root.geometry('600x400')
root.iconbitmap('./img/mushroom_super.ico')

# il label frame è un semplice contenitore adatto a creare layout complessi, con l'aggiunta di un testo
label_frame = LabelFrame(root, padx=10, pady=50, height=100, width=400, text='Sono un LabelFreame')
label_frame.pack(fill=BOTH,
                 expand=True)  # la proprietà 'expand' impostata su true dirà di prendersi tutto lo spazio disponibile
# il frame è simile al LabelFrame solo che non è possibile aggiungere il testo
frame2 = Frame(root, background='yellow', padx=10, pady=50, height=100, width=400)
frame2.pack(fill=BOTH,  # la proprietà fill specifica quali lati devono essere riempiti dal frame
            expand=True)
frame3 = Frame(root, background='green', padx=10, pady=50, height=100, width=400)
frame3.pack(fill=BOTH, expand=True)

button1 = ttk.Button(label_frame, text='ciao')
button1.pack()
button2 = ttk.Button(frame2, text='hola')
button2.pack()
button3 = ttk.Button(frame3, text='hello')
button3.pack()

root.mainloop()
