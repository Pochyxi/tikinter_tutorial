from tkinter import *
from tkinter import ttk, scrolledtext

root = Tk()
root.title("Il nostro programma")
root.geometry('600x400')
root.iconbitmap('./img/mushroom_super.ico')

scrolledtxt = scrolledtext.ScrolledText(root, width=50, height=50)
scrolledtxt.pack(fill=BOTH, side=LEFT, expand=True)

root.mainloop()
