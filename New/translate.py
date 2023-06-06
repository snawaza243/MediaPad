################################################################
# Title       : MediaPad | Home                                #
# Authors(s)  : 11202722                                       #
# Coordinator : Rajeev Gupta Sir                               #
# Affiliation :                                                #
# Address     : MMDU, Mullana Ambala                           #
# Date        : 16/06/2022                                     #
# Version     : 2.8                                            #
################################################################
#######################################################
#              Text 2 Text Language Translate         #
#######################################################

from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter
from PIL import ImageTk, Image  # pip install pillow
from googletrans import Translator  # pip install googletrans==3.1.0a0
from tkinter import messagebox

window = tk.Tk()
window.title('MediaPad | Translate')
window.geometry('530x330')
window.maxsize(530, 350)
window.minsize(530, 350)
window.iconbitmap(r'C:/Users/snawa/OneDrive/Documents/GitHub/MediaPad/component/mpi.ico')



# translate function for translate function
def translate():
    language_1 = t1.get("1.0", "end-1c")
    cl = choose_langauge.get()

    # cheking first language
    if language_1 == '':
        messagebox.showerror(
            'MediaPad : Translator', 'Oo\n\nNo text to translate.\nPlease enter text in the first box.\n\n\n\t\t\t\tMediaPad')

    # inserting output translated text into second text box t2
    else:
        t2.delete(1.0, 'end')
        translator = Translator()
        output = translator.translate(language_1, dest=cl)
        t2.insert('end', output.text)


# clear function for button
def clear():
    t1.delete(1.0, 'end')
    t2.delete(1.0, 'end')

# exigt function for button


def exit():
    window.destroy()

# About infor function for about button

def aboutinfo():
    tkinter.messagebox.showinfo(
        "MediaPad", "\nThank you for usnig this application.\n\nCheck update at www.mediapad.com/update\n\nMail us for more info. snawaza243@gmail.com\n\n\n\t\t\tMediaPad")

#######################################################
#              Translateor GUI                        #
#######################################################


# Auto-detect language variable input & GUI
a = tk.StringVar()
auto_detect = ttk.Combobox(
    window, width=20, textvariable=a, state='readonly', font=('verdana', 10, 'bold'),)

auto_detect['values'] = ('Auto-Detect Language',)
auto_detect.place(x=30, y=70)
auto_detect.current(0)

# Choose destination language & GUI
l = tk.StringVar()
choose_langauge = ttk.Combobox(
    window, width=20, textvariable=l, state='readonly', font=('verdana', 10, 'bold'))

choose_langauge['values'] = (
    'Afrikaans',
    'Albanian',
    'Arabic',
    'Armenian',
    'Azerbaijani',
    'Basque',
    'Belarusian',
    'Bengali',
    'Bosnian',
    'Bulgarian',
    'Catalan',
    'Cebuano',
    'Chichewa',
    'Chinese',
    'Corsican',
    'Croatian',
    'Czech',
    'Danish',
    'Dutch',
    'English',
    'Esperanto',
    'Estonian',
    'Filipino',
    'Finnish',
    'French',
    'Frisian',
    'Galician',
    'Georgian',
    'German',
    'Greek',
    'Gujarati',
    'Haitian Creole',
    'Hausa',
    'Hawaiian',
    'Hebrew',
    'Hindi',
    'Hmong',
    'Hungarian',
    'Icelandic',
    'Igbo',
    'Indonesian',
    'Irish',
    'Italian',
    'Japanese',
    'Javanese',
    'Kannada',
    'Kazakh',
    'Khmer',
    'Kinyarwanda',
    'Korean',
    'Kurdish',
    'Kyrgyz',
    'Lao',
    'Latin',
    'Latvian',
    'Lithuanian',
    'Luxembourgish',
    'Macedonian',
    'Malagasy',
    'Malay',
    'Malayalam',
    'Maltese',
    'Maori',
    'Marathi',
    'Mongolian',
    'Myanmar',
    'Nepali',
    'Norwegian'
    'Odia',
    'Pashto',
    'Persian',
    'Polish',
    'Portuguese',
    'Punjabi',
    'Romanian',
    'Russian',
    'Samoan',
    'Scots Gaelic',
    'Serbian',
    'Sesotho',
    'Shona',
    'Sindhi',
    'Sinhala',
    'Slovak',
    'Slovenian',
    'Somali',
    'Spanish',
    'Sundanese',
    'Swahili',
    'Swedish',
    'Tajik',
    'Tamil',
    'Tatar',
    'Telugu',
    'Thai',
    'Turkish',
    'Turkmen',
    'Ukrainian',
    'Urdu',
    'Uyghur',
    'Uzbek',
    'Vietnamese',
    'Welsh',
    'Xhosa'
    'Yiddish',
    'Yoruba',
    'Zulu',
)
choose_langauge.place(x=290, y=70)
choose_langauge.current(35)

# t1 for window text area
t1 = Text(window, width=30, height=10, borderwidth=2,
          pady=5, padx=5, relief=RIDGE)
t1.place(x=10, y=100)

# t2 for output text area
t2 = Text(window, width=30, height=10, borderwidth=2,
          pady=5,  padx=5, relief=RIDGE)
t2.place(x=260, y=100)


# Ringht click menu list in output text are
m = Menu(window, tearoff=0)
m.add_command(label="Cut",)
m.add_command(label="Copy")
m.add_command(label="Paste")
m.add_command(label="Slect All")
m.add_separator()
m.add_command(label="Undo")


def do_popup(event):
    try:
        m.tk_popup(event.x_window, event.y_window)
    finally:
        m.grab_release()


t1.bind("<Button-3>", do_popup)
t2.bind("<Button-3>", do_popup)

lTranslate = Label(window, text="Transtale Now",
                   font=("Century Gothic", 22, "bold"))
lTranslate.place(x=160, y=15)


bTranslate1 = Button(window, text="Translate", relief=RIDGE, borderwidth=2, font=(
    'verdana', 10, 'bold'), cursor="hand2", command=translate)
bTranslate1.place(x=10, y=280)

bclear1 = Button(window, text="Clear", relief=RIDGE, borderwidth=2,
                 font=('verdana', 10, 'bold'), cursor="hand2", command=clear)
bclear1.place(x=120, y=280)

bcopy1 = Button(window, text="Copy ", relief=RIDGE, borderwidth=2,
                font=('verdana', 10, 'bold'), cursor="hand2", command=clear)
bcopy1.place(x=200, y=280)



babout1 = Button(window, text="About", relief=RIDGE, borderwidth=2, bg="lightgreen",
                 font=('verdana', 10, 'bold'), cursor="hand2", command=aboutinfo)
babout1.place(x=380, y=280)


bexit1 = Button(window, text="Exit", relief=RIDGE, borderwidth=2, bg="red",
                font=('verdana', 10, 'bold'), cursor="hand2", command=exit)
bexit1.place(x=467, y=280)
window.mainloop()
