from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Il nostro programma')
root.geometry('400x400')
root.iconbitmap('./img/mushroom_super.ico')


def login():
    print('Questa è la mail inserita: ', email_entry.get())
    print('Questa è la password inserita: ', password_entry.get())


# CREAZIONE INPUT EMAIL
label_email = ttk.Label(root, text='Email')
label_email.pack(padx=5, pady=5)

email = StringVar()
email_entry = ttk.Entry(root, textvariable=email)
email_entry.pack(padx=5, pady=5)
# email_entry.focus() # All'avvio verrà inpostato il focus su questo elemento

# CREAZIONE INPUT PASSWORD
label_password = ttk.Label(root, text='password')
label_password.pack(padx=5, pady=5)

password = StringVar()
password_entry = ttk.Entry(root, textvariable=password, show='*')
password_entry.pack(padx=5, pady=5)

# CREAZIONE BUTTON LOGIN
button = ttk.Button(root, text='Login', command=login)
button.pack(padx=5, pady=5)
root.mainloop()
