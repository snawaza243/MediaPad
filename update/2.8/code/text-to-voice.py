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
#              Text 2 Audio GUI,Functions             #
#######################################################
import datetime
from playsound import playsound
from cProfile import label
import imp
from tkinter import *
import tkinter as tk
from tkinter import ttk 
from PIL import ImageTk, Image  # pip install pillow for image
from tkinter import messagebox
from gtts import gTTS
import pyttsx3
engine = pyttsx3.init()

window = tk.Tk()
window.title('MediaPad | Text 2 Audio')
window.geometry('530x330')
window.maxsize(530, 350)
window.minsize(530, 350)
# window.iconbitmap(r'mpi.ico')
# window = tk.Tk()
# window.iconbitmap('mpi.ico')

window.iconbitmap(r'C:/Users/snawa/OneDrive/Documents/GitHub/MediaPad/app/icon.ico')
Msg = StringVar()
# Entry


t1 = Entry(window, textvariable=Msg, width='85', )
t1.place(x=10, y=100)

# Function to Reset
def Reset():
    Msg.set("")

# Function to Convert Text to Speech in Python
def clear():
    t1.delete(1.0, 'end')
    
# exit function for button
def exit():
    window.destroy()

# About info function for about button
def aboutinfo():
    tk.messagebox.showinfo(
        "About", "Hello user!\n\nWe very thankful to using our product and always ready to solve your all possible problems.\n\nCheck update!\nwww.mediapad.com/update\n\nIf you are facing any problem please let us know and contact us at help@snawaz.com\n\n\n\t\t\t\tMediaPad Team!")

# male text to speech english version


def playM():
    engine = pyttsx3.init()
    engine.setProperty("rate", 130)
    engine.say(t1.get())
    print(engine.say(t1.get()))
    engine.runAndWait()

# female text to speech english version


def playF():
    # speech rate
    engine.setProperty('rate', 125)

    # speech volume
    engine.setProperty('volume', 1.0)

    # speech voices id
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    engine.say(t1.get())
    engine.runAndWait()
    engine.stop()

    engine.save_to_file(t1, '.mp3')
    engine.runAndWait()

# female text to speech hindi version
def PlayF_Hindi():
    Message = t1.get()
    speech = gTTS(text=Message)
    speech.save('mpa_mHi.mp3')
    playsound('mpa_mHi.mp3')

# saving audio in male version


def saveM():
    """ RATE"""
    engine.setProperty('rate', 125)

    """VOLUME"""
    engine.setProperty('volume', 1.0)

    """VOICE"""
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    texttakeing = t1.get()
    print(texttakeing)

    """Saving Voice to a file"""
    basename = "mpa_mEn"
    suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    filename = "_".join([basename, suffix])

    engine.save_to_file(texttakeing, filename+'test.mp3')
    engine.runAndWait()

# saving audio in female version


def saveF():
    mytext = t1.get()
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    print(mytext)
    basename = "mpa_fEn"
    suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    filename = "_".join([basename, suffix])
    myobj.save(filename+".mp3")


# Right click menu list in  text area
m = Menu(window, tearoff=0)
m.add_command(label="Cut",)
m.add_command(label="Copy")
m.add_command(label="Paste")
m.add_command(label="Select All")
m.add_separator()
m.add_command(label="Undo")


def do_popup(event):
    try:
        m.tk_popup(event.x_window, event.y_window)
    finally:
        m.grab_release()


t1.bind("<Button-3>", do_popup)

# window heading label
ltranslate = Label(window, text="Text into Audio",
                   font=("Century Gothic", 22, "bold"))
ltranslate.place(x=160, y=15)



# Button for text to voice
bplaym = Button(window, text="ENG-M", relief=RIDGE, borderwidth=3, width=8,
                font=('verdana', 10, 'bold'), cursor="hand2", command=playM)
bplaym.place(x=10, y=280)

bplayf = Button(window, text="ENG-F", relief=RIDGE, borderwidth=3, width=8,
                font=('verdana', 10, 'bold'), cursor="hand2", command=playF)
bplayf.place(x=115, y=280)

bplayf = Button(window, text="HIN-F", relief=RIDGE, borderwidth=3, width=8,
                font=('verdana', 10, 'bold'), cursor="hand2", command=PlayF_Hindi)
bplayf.place(x=220, y=280)

# instruction label
male = Label(window, text="M/ F: Male/ Female", bg="white", padx=15, width=17, pady=5)
male.place(x=370, y=280)


bsavem = Button(window, text="Save-M", relief=RIDGE, borderwidth=3, width=8,
                font=('verdana', 10, 'bold'), cursor="hand2", command=saveM)
bsavem.place(x=10, y=315)

bsavef = Button(window, text="Save-F", relief=RIDGE, borderwidth=3, width=8,
                font=('verdana', 10, 'bold'), cursor="hand2", command=saveF)
bsavef.place(x=115, y=315)

bstop = Button(window, text="--", relief=RIDGE, borderwidth=3, width=8,
               font=('verdana', 10, 'bold'), cursor="hand2")
bstop.place(x=220, y=315)


# Buttons of bottom line


babout1 = Button(window, text="About", relief=RIDGE, borderwidth=2, bg="lightgreen", width=8,
                 font=('verdana', 10, 'bold'), cursor="hand2", command=aboutinfo)
babout1.place(x=370, y=315)
bexit1 = Button(window, text="Exit", relief=RIDGE, borderwidth=2, bg="red", width=5,
                font=('verdana', 10, 'bold'), cursor="hand2", command=exit)
bexit1.place(x=467, y=315)
window.mainloop()
