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
#              Voice to Text GUI,Functions            #
#######################################################
# //////////////////// || In Process || \\\\\\\\\\\\\\\\\\\\ #

from playsound import playsound
from cProfile import label
import imp
from tkinter import *
import tkinter as tk
import pyttsx3
from asyncore import read
from math import factorial
from tkinter.filedialog import asksaveasfilename
import os
import tkinter.messagebox
from googletrans import Translator
engine = pyttsx3.init()

root = tk.Tk()
root.title('MediaPad | Voice to Text')
root.geometry('530x330')
root.maxsize(530, 350)
root.minsize(530, 350)

# p1 = PhotoImage(file = 'info.png')
# # Setting icon of master window
# root.iconphoto(False, p1)
# # root.iconbitmap(r'mpi.ico')



root.iconbitmap(r'C:/Users/snawa/OneDrive/Documents/GitHub/MediaPad/component/mpi.ico')



Msg = StringVar()

# text area
t1 = Text(root, width=62, height=10, borderwidth=2,
          pady=5, padx=5, relief=RIDGE)
t1.place(x=10, y=100)
# Function to Reset


def Reset():
    t1.set("")

# Function to Convert Text to Speech in Python

def clear():
    t1.delete(1.0, 'end')
# exigt function for button


def exit():
    root.destroy()

# About infor function for about button
def aboutinfo():
    tkinter.messagebox.showinfo(
        "About", "Hello user!\n\nWe very thankful to using our product and always ready to solve your all possible problems.\n\nCheck update!\nwww.mediapad.com/update\n\nIf you are facing any problem please let us know and contact us at snawaza243@gmail.com\n\n\n\t\t\t\tMediaPad Team!")


# Python program to translate
# speech to text and text to speech

def recordnow():
    import speech_recognition as sr
    import pyttsx3

    # Initialize the recognizer
    r = sr.Recognizer()

    # Function to convert text to
    # speech
    def SpeakText(command):

        # Initialize the engine
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()

    # Loop infinitely for user to
    # speak

    while(1):

        # Exception handling to handle
        # exceptions at the runtime
        try:

            # use the microphone as source for input.
            with sr.Microphone() as source2:

                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                r.adjust_for_ambient_noise(source2, duration=0.2)

                # listens for the user's input
                audio2 = r.listen(source2)

                # Using google to recognize audio
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()

                print("Did you say "+MyText)
                tv1 = "Did you say "+MyText
                t1.insert(1.0, 'end', tv1)
                SpeakText(MyText)

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            tv2 = "Could not request results; {0}".format(e)
            t1.insert(1.0, 'end', tv2)

        except sr.UnknownValueError:
            print("unknown error occured")
            tv3 = "unknown error occured"
            t1.insert(1.0, 'end', tv3)


# saving text file

def saveFile():
    global file

    if file == None:

        file = asksaveasfilename(defaultextension=".txt", filetypes=[
                                 ("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(t1.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad ")
    else:
        f = open(file, "w")
        f.write(t1.get(1.0, END))
        f.close()


def Copyt():
    t1.event_generate(("<<Copy>>"))


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

# instruction label
ltranslate = Label(root, text="Voice into Text",
                   font=("Century Gothic", 22, "bold"))
ltranslate.place(x=160, y=15)
button4 = Button(root, text="Record", relief=RIDGE, borderwidth=3,
                 font=('verdana', 10, 'bold'), cursor="hand2", command=recordnow)
button4.place(x=10, y=280)

button5 = Button(root, text="Save", relief=RIDGE, borderwidth=3,
                 font=('verdana', 10, 'bold'), cursor="hand2", command=saveFile)
button5.place(x=110, y=280)

button6 = Button(root, text="Copy", relief=RIDGE, borderwidth=3,
                 font=('verdana', 10, 'bold'), cursor="hand2", command=Copyt)
button6.place(x=200, y=280)

button7 = Button(root, text="Clear", relief=RIDGE, borderwidth=3,
                 font=('verdana', 10, 'bold'), cursor="hand2", command=Reset)
button7.place(x=290, y=280)


# Buttons of bottom line
bhomt1 = Button(root, text="Home", relief=RIDGE, borderwidth=2,
                font=('verdana', 10, 'bold'), cursor="hand2", command=clear)
bhomt1.place(x=10, y=315)


bt2a1 = Button(root, text="Translate", relief=RIDGE, borderwidth=2,
               font=('verdana', 10, 'bold'), cursor="hand2", command=clear)
bt2a1.place(x=110, y=315)

bv2t1 = Button(root, text="Text To Voice", relief=RIDGE, borderwidth=2,
               font=('verdana', 10, 'bold'), cursor="hand2", command=clear)
bv2t1.place(x=235, y=315)

babout1 = Button(root, text="About", relief=RIDGE, borderwidth=2,
                 font=('verdana', 10, 'bold'), cursor="hand2", command=aboutinfo)
babout1.place(x=380, y=315)


bexit1 = Button(root, text="Exit", relief=RIDGE, borderwidth=2,
                font=('verdana', 10, 'bold'), cursor="hand2", command=exit)
bexit1.place(x=467, y=315)
root.mainloop()
