from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import keyword
import re


root = Tk()
root.title("TIKINDERBUENO")
root.geometry('600x400')
root.iconbitmap('./img/mushroom_super.ico')
root.state('zoomed')

txtwidget = Text(root)


def apri_file():
    filetypes = (
        ('file di testo', '*.txt'),
        ('tutti i file', '*.*')
    )

    # PER APRIRE E LEGGERE IL FILE
    filename = filedialog.askopenfilename(title='Apri un file', initialdir="/", filetypes=filetypes)
    print(filename)
    f = open(filename, 'r')
    data = f.read()
    print(data.split('\n'))
    for line in data:
        txtwidget.insert(END, line)
    txtwidget.pack(expand=1, fill=BOTH)

    color_keywords_python(data)

    # PER SALVARE UN NUOVO FILE
    # f = filedialog.asksaveasfile(mode='w', title='salva file', defaultextension=".txt")
    # data = "La mia banda suona il rock!"
    # f.write(data)
    # f.close()


bottone = ttk.Button(root, text='apri file', command=apri_file)
bottone.pack(expand=True)


# adding a tag to a part of text specifying the indices
def highlight_text(tag_name, lineno, start_char, end_char, bg_color=None, fg_color=None):
    txtwidget.tag_add(tag_name, f'{lineno}.{start_char}', f'{lineno}.{end_char}')
    txtwidget.tag_config(tag_name, background=bg_color, foreground=fg_color)


def color_keywords_python(stringa):
    splitto_per_riga = stringa.split("\n")
    print('----DI SEGUITO LISTA SPLITTATA PER RIGA----')
    print(splitto_per_riga)
    print()

    for riga in splitto_per_riga:
        numero_riga = splitto_per_riga.index(riga) + 1
        print('----QUESTA E\' LA RIGA ' + str(numero_riga) + '----')
        print()

        parole_riservate = keyword.kwlist
        riga_splittata = riga.split()
        parole_indicizzate = [(ele.start(), ele.end() - 1) for ele in re.finditer(r'\S+', riga)]
        print('----Di seguito la riga ' + str(numero_riga) + ' splittata')
        print('--> ', riga_splittata)

        if len(riga_splittata) and riga_splittata[0] == '#':
            highlight_text('riga' + str(numero_riga), numero_riga, start_char=1, end_char=len(riga), fg_color='gray')
            continue

        for parola in riga_splittata:
            index_parola = riga_splittata.index(parola)

            if "(" in parola:
                index_parentesi = parola.index("(")
                lunghezza_parola = len(parola)
                differenza = lunghezza_parola - index_parentesi
                print('Lunghezza della parola: ', lunghezza_parola)
                print('Trovata parentesi all\'indice ', index_parentesi)
                highlight_text('parola_parentesi' + str(index_parola), lineno=numero_riga,
                               start_char=parole_indicizzate[index_parola][0],
                               end_char=parole_indicizzate[index_parola][1] + 1 - differenza, fg_color='blue')

            if "." in parola:
                index_parentesi = parola.index(".")
                lunghezza_parola = len(parola)
                differenza = lunghezza_parola - index_parentesi

                print('Lunghezza della parola: ', lunghezza_parola)
                print('Trovato punto all\'indice ', index_parentesi)

                indice_partenza = parole_indicizzate[index_parola][0]
                indice_finale = parole_indicizzate[index_parola][1] + 1 - differenza
                parola_da_evidenziare = parola[indice_partenza:indice_finale]

                print(parola[indice_partenza:indice_finale])

                if '(' in parola_da_evidenziare:
                    pass
                else:
                    highlight_text('parola_punto' + str(index_parola), lineno=numero_riga,
                                   start_char=indice_partenza,
                                   end_char=indice_finale, fg_color='black')

            if parola in parole_riservate:
                # ho bisogno di prendermi dalla stringa l'inizio dell'indice del carattere e la fine
                print('(FOUND)Riga ' + str(numero_riga) + ': parola "' + parola + '" E\' una parola riservata')
                res = [(ele.start(), ele.end() - 1) for ele in re.finditer(r'\S+', stringa)]
                print('Tag_name = ', 'parola' + str(index_parola))
                print('lineno = ', numero_riga)
                print('start_char = ', parole_indicizzate[index_parola][0])
                print('end_char = ', parole_indicizzate[index_parola][1])

                highlight_text('parola' + str(index_parola), lineno=numero_riga,
                               start_char=parole_indicizzate[index_parola][0],
                               end_char=parole_indicizzate[index_parola][1] + 1, fg_color='red')
            else:
                print('Riga ' + str(numero_riga) + ': parola "' + parola + '" NON è una parola riservata')
                print()


root.mainloop()
