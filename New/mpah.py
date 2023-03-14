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
#                  MediaPad Home                      #
#######################################################
import os
from tkinter import *
import tkinter as tk
import pyttsx3
import tkinter.messagebox
import tkinter as tk
from tkinter import *
from hyperlink import*
import webbrowser
from functools import partial
from PIL import ImageTk, Image
engine = pyttsx3.init()

rootHome = tk.Tk()
rootHome.title('MediaPad | Home')
rootHome.geometry('530x350')
rootHome.maxsize(530, 350)
rootHome.minsize(530, 350)
rootHome.iconbitmap(r'C:/Users/snawa/OneDrive/Documents/GitHub/MediaPad/component/mpi.ico')

frame = Frame(rootHome, width=530, height=350)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open(
    "C:/Users/snawa/OneDrive/Documents/GitHub/MediaPad/component/bgs.png"))
# Create a Label Widget to display the text or Image
HoveBgLabel = Label(frame, image=img)
HoveBgLabel.pack()

# Function to call rootHome file path
def aboutBtnInfoFun():
    tkinter.messagebox.showinfo("MediaPad", "\nThank you for using this application.\n\nKeep Check update at www.mediapad.com/update\n\nIf you have any query then contact with use snawaza243@gmail.com\n\n\n\t\t\tMediaPad")

def exit():
    rootHome.destroy()

def transBtnFunHover_1(e):
    transBtn.config(background='OrangeRed3', foreground="white")

def transBtnFunHover_0(e):
    transBtn.config(background='SystemButtonFace', foreground='black')

def t2vBtnFunHover_1(e):
    t2vBtn.config(background='OrangeRed3', foreground="white")

def t2vBtnFunHover_0(e):
    t2vBtn.config(background='SystemButtonFace', foreground='black')

def v2tBtnFunHover_1(e):
    v2tBtn.config(background='OrangeRed3', foreground="white")

def v2tBtnFunHover_0(e):
    v2tBtn.config(background='SystemButtonFace', foreground='black')

def root2Fun():
    # Toplevel object which will be treated as a new window
    root2 = Toplevel(rootHome)
    
    # sets the title & geometry of the Toplevel widget
    root2.title('MediaPad | Translate')
    root2.geometry('530x330')
    root2.maxsize(530, 350)
    root2.minsize(530, 350)
    root2.iconbitmap(r'C:/Users/snawa/OneDrive/Documents/GitHub/MediaPad/component/mpi.ico')


    
    
homeTitleText = Label(rootHome,  text="MediaPad", font=("Century Gothic", 32, "bold"), bg='white')
homeTitleText.place(x=160, y=20)

# button hovering
transBtn = Button(rootHome, text="Translator", width=30, height=2, relief=RIDGE, borderwidth=3, font=('verdana', 11, 'bold'), cursor="hand2", command=root2Fun)
transBtn.place(x=115, y=100)
transBtn.bind('<Enter>', transBtnFunHover_1)
transBtn.bind('<Leave>', transBtnFunHover_0)

t2vBtn = Button(rootHome, text="Text-to-Voice", width=30, height=2,
                      relief=RIDGE, borderwidth=3, font=('verdana', 11, 'bold'), cursor="hand2")
t2vBtn.place(x=115, y=160)
t2vBtn.bind('<Enter>', t2vBtnFunHover_1)
t2vBtn.bind('<Leave>', t2vBtnFunHover_0)

v2tBtn = Button(rootHome, text="Voice-to-Text", width=30, height=2,
                      relief=RIDGE, borderwidth=3, font=('verdana', 11, 'bold'), cursor="hand2")
v2tBtn.place(x=115, y=220)
v2tBtn.bind('<Enter>', v2tBtnFunHover_1)
v2tBtn.bind('<Leave>', v2tBtnFunHover_0)

aboutBtnHome = Button(rootHome, text="About", relief=RIDGE, borderwidth=1, font=('verdana', 10, 'bold'), cursor="hand2", bg='light blue', command=aboutBtnInfoFun)
aboutBtnHome.place(anchor='center', x=425, y=325)

exitBtnHome = Button(rootHome, text="Exit", relief=RIDGE, borderwidth=1, font=('verdana', 10, 'bold'), cursor="hand2", bg='red', command=exit)
exitBtnHome.place(anchor='center', x=486, y=325)

rootHome.mainloop()
