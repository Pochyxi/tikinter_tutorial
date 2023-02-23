from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Il nostro programma")
root.geometry('600x400')
root.iconbitmap('./img/mushroom_super.ico')
# il layout pack accoda gli elementi

label1 = Label(root, text='Label 1', background='green', foreground='white')
label1.pack(ipadx=10, ipady=10, fill=X)
# padx rappresenta lo spazio esterno orizzontale
# pady rappresenta lo spazio esterno verticale
# ipadx rappresenta lo spazio interno orizzontale
# ipady rappresenta lo spazio interno verticale
label2 = Label(root, text='Label 2', background='red', foreground='white')
label2.pack(ipadx=10, ipady=10, fill=X)

label3 = Label(root, text='Label 3', background='blue', foreground='white')
label3.pack(ipadx=10, ipady=10, fill=X)

label4 = Label(root, text='Label 4', background='orange', foreground='white')
label4.pack(ipadx=10, ipady=10, fill=BOTH, expand=True, side=LEFT)  # side specifica il posizionamento del Label

label5 = Label(root, text='Label 5', background='yellow', foreground='white')
label5.pack(ipadx=10, ipady=10, fill=BOTH, expand=True, side=LEFT)

label6 = Label(root, text='Label 6', background='purple', foreground='white')
label6.pack(ipadx=10, ipady=10, fill=BOTH, expand=True, side=LEFT)

root.mainloop()
