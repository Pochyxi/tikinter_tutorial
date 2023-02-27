from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Il nostro programma")
root.geometry('600x400')
root.iconbitmap('./img/mushroom_super.ico')
# una grid è semplicemente una griglia

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

frame1 = Frame(root, background='red', height=200, width=200)
frame2 = Frame(root, background='purple', height=200, width=200)
frame3 = Frame(root, background='yellow', height=200, width=200)
frame4 = Frame(root, background='cyan', height=200, width=200)

frame1.grid(column=0, row=0)
frame2.grid(column=1, row=0)
frame3.grid(column=0, row=1)
frame4.grid(column=1, row=1)

root.mainloop()
