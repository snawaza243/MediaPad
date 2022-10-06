import datetime
from playsound import playsound
from cProfile import label
import imp
from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter
from PIL import ImageTk, Image  # pip install pillow for image
from tkinter import messagebox
from gtts import gTTS
import pyttsx3
engine = pyttsx3.init()

root = tk.Tk()
root.title('MediaPad | Text 2 Audio')
root.geometry('530x330')
root.maxsize(530, 350)
root.minsize(530, 350)
# root.iconbitmap(r'mpi.ico')
# root = tk.Tk()
# root.iconbitmap('mpi.ico')

root.iconbitmap(r'mpi.ico')



################################################################
# Title       : MediaPad | Text2Audio                          #
# Authors(s)  : 11202722, 23                                   #
# Co-ordinator: Dr. Rajeev Gupta Sir                           #
# Affiliation :                                                #
# Address     : MMDU, Mullana Ambala                           #
# Date        : 16/06/2022                                     #
# Version     : 2.0                                            #
################################################################

#######################################################
#              Text 2 Audio GUI,Functions             #
#######################################################

Msg = StringVar()
# Entry
t1 = Entry(root, textvariable=Msg, width='83',)
t1.place(x=10, y=100)

# Function to Reset
def Reset():
    Msg.set("")

# Function to Convert Text to Speech in Python


def clear():
    t1.delete(1.0, 'end')
# exigt function for button


def exit():
    root.destroy()

# About infor function for about button


def aboutinfo():
    tkinter.messagebox.showinfo(
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


# Ringht click menu list in  text area
m = Menu(root, tearoff=0)
m.add_command(label="Cut",)
m.add_command(label="Copy")
m.add_command(label="Paste")
m.add_command(label="Slect All")
m.add_separator()
m.add_command(label="Undo")


def do_popup(event):
    try:
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()


t1.bind("<Button-3>", do_popup)

# window headgin label
ltranslate = Label(root, text="Text into Audio",
                   font=("Century Gothic", 22, "bold"))
ltranslate.place(x=160, y=15)


# instruction label
male = Label(root, text="M = Male")
male.place(x=430, y=240)

female = Label(root, text="F = Female")
female.place(x=430, y=260)
# Button for text to voice
bplaym = Button(root, text="Play-M", relief=RIDGE, borderwidth=3,
                font=('verdana', 10, 'bold'), cursor="hand2", command=playM)
bplaym.place(x=10, y=280)

bplayf = Button(root, text="Play-F", relief=RIDGE, borderwidth=3,
                font=('verdana', 10, 'bold'), cursor="hand2", command=playF)
bplayf.place(x=88, y=280)

bplayf = Button(root, text="Play-F (Hindi)", relief=RIDGE, borderwidth=3,
                font=('verdana', 10, 'bold'), cursor="hand2", command=PlayF_Hindi)
bplayf.place(x=165, y=280)

bsavem = Button(root, text="Save-M", relief=RIDGE, borderwidth=3,
                font=('verdana', 10, 'bold'), cursor="hand2", command=saveM)
bsavem.place(x=295, y=280)

bsavef = Button(root, text="Save-F", relief=RIDGE, borderwidth=3,
                font=('verdana', 10, 'bold'), cursor="hand2", command=saveF)
bsavef.place(x=380, y=280)

bstop = Button(root, text="Stop", relief=RIDGE, borderwidth=3,
               font=('verdana', 10, 'bold'), cursor="hand2", command=saveF)
bstop.place(x=461, y=280)


# Buttons of bottom line
bhomt1 = Button(root, text="Home", relief=RIDGE, borderwidth=2,
                font=('verdana', 10, 'bold'), cursor="hand2", command=clear)
bhomt1.place(x=10, y=315)


bt2a1 = Button(root, text="Translate", relief=RIDGE, borderwidth=2,
               font=('verdana', 10, 'bold'), cursor="hand2", command=clear)
bt2a1.place(x=101, y=315)

bv2t1 = Button(root, text="Voice2Text", relief=RIDGE, borderwidth=2,
               font=('verdana', 10, 'bold'), cursor="hand2", command=clear)
bv2t1.place(x=253, y=315)

babout1 = Button(root, text="About", relief=RIDGE, borderwidth=2,
                 font=('verdana', 10, 'bold'), cursor="hand2", command=aboutinfo)
babout1.place(x=380, y=315)


bexit1 = Button(root, text="Exit", relief=RIDGE, borderwidth=2,
                font=('verdana', 10, 'bold'), cursor="hand2", command=exit)
bexit1.place(x=467, y=315)
root.mainloop()
