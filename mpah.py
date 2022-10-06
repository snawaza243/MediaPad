import os
from tkinter import *
import tkinter as tk
import pyttsx3
import tkinter.messagebox
import tkinter as tk
import pyttsx3
from tkinter import *
from hyperlink import*
import webbrowser
from functools import partial

from PIL import ImageTk, Image
engine = pyttsx3.init()


################################################################
# Title       : MediaPad | Home                                #
# Authos(s)   : 11202722,                                      #
# Co-ordinate : Rajeev Gupta Sir                               #
# Affiliation :                                                #
# Address     : MMDU, Mullana Ambala                           #
# Date        : 16/06/2022                                     #
# Version     : 2.8                                            #
################################################################


root = tk.Tk()
root.title('MediaPad | Home')
root.geometry('530x350')
root.maxsize(530, 350)
root.minsize(530, 350)
root.iconbitmap(r'C:/Users/snawa/Desktop/Py_Pro_01_2.9/mpi.ico')

frame = Frame(root, width=530, height=350)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open(
    "C:/Users/snawa\Desktop/Py_Pro_01_2.9/back.png"))
# Create a Label Widget to display the text or Image
label = Label(frame, image=img)
label.pack()

# Function to call root file poth


def translatewindow():
    # progpathcwd = os.getcwd()
    progpathf = __file__
    os.startfile(progpathf)


def aboutinfo():
    tkinter.messagebox.showinfo(
        
        "MediaPad", "\nThank you for usnig this application.\n\nCheck update at www.mediapad.com/update\n\nMail us for more info. snawaza243@gmail.com\n\n\n\t\t\tMediaPad")


def exit():
    root.destroy()

# Functions for Play&Save Audio Windows
def homepage(args):
    print("Home")


def opentranslate(args):
    progpathf = __file__
    os.startfile(progpathf)


def onbtn1(e):
    btranslate.config(background='OrangeRed3', foreground="white")


def ofbtn1(e):
    btranslate.config(background='SystemButtonFace', foreground='black')


def onbtn2(e):
    btexttoaudio.config(background='OrangeRed3', foreground="white")


def ofbtn2(e):
    btexttoaudio.config(background='SystemButtonFace', foreground='black')


def onbtn3(e):
    bvoicetotext.config(background='OrangeRed3', foreground="white")


def ofbtn3(e):
    bvoicetotext.config(background='SystemButtonFace', foreground='black')


lhead = Label(root,  text="MediaPad", font=(
    "Century Gothic", 32, "bold"), bg='white')
lhead.place(x=160, y=20)


# button hovering


btranslate = Button(root, text="Translator", width=30, height=2, relief=RIDGE,
                    borderwidth=3, font=('verdana', 11, 'bold'), cursor="hand2",)
btranslate.place(x=115, y=100)
btranslate.bind('<Enter>', onbtn1)
btranslate.bind('<Leave>', ofbtn1)


btexttoaudio = Button(root, text="Text-to-Audio", width=30, height=2,
                      relief=RIDGE, borderwidth=3, font=('verdana', 11, 'bold'), cursor="hand2")
btexttoaudio.place(x=115, y=160)
btexttoaudio.bind('<Enter>', onbtn2)
btexttoaudio.bind('<Leave>', ofbtn2)

bvoicetotext = Button(root, text="Voice-to-Text", width=30, height=2,
                      relief=RIDGE, borderwidth=3, font=('verdana', 11, 'bold'), cursor="hand2")
bvoicetotext.place(x=115, y=220)
bvoicetotext.bind('<Enter>', onbtn3)
bvoicetotext.bind('<Leave>', ofbtn3)


bAbout = Button(root, text="About", relief=RIDGE, borderwidth=1, font=(
    'verdana', 10, 'bold'), cursor="hand2", bg='light blue', command=aboutinfo)
bAbout.place(anchor='center', x=425, y=325)

buttonexitM = Button(root, text="Exit", relief=RIDGE, borderwidth=1,
                     font=('verdana', 10, 'bold'), cursor="hand2", bg='red', command=exit)
buttonexitM.place(anchor='center', x=486, y=325)


root.mainloop()
