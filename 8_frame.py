from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Il nostro programma")
root.geometry('600x400')
root.iconbitmap('./img/mushroom_super.ico')

frame1 = LabelFrame(root, padx=10, pady=50, height=100, width=400, text='Sono un LabelFreame')
frame2 = Frame(root, background='yellow', padx=10, pady=50, height=100, width=400)
frame3 = Frame(root, background='green', padx=10, pady=50, height=100, width=400)
frame1.pack(fill=BOTH, expand=True)
frame2.pack(fill=BOTH, expand=True)
frame3.pack(fill=BOTH, expand=True)

button1 = ttk.Button(frame1, text='ciao')
button1.pack()
button2 = ttk.Button(frame2, text='hola')
button2.pack()
button2 = ttk.Button(frame3, text='hello')
button2.pack()


root.mainloop()
