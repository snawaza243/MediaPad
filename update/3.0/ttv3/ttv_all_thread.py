import os
import tkinter.messagebox
from tkinter import messagebox
from tkinter import filedialog,simpledialog
from tkinter.scrolledtext import ScrolledText
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tktooltip import ToolTip
import pyttsx3
from hyperlink import*
import webbrowser
from functools import partial
import re
from datetime import datetime
from PIL import ImageTk, Image
from PIL import ImageTk, Image  # pip install pillow
from googletrans import Translator  # pip install googletrans==3.1.0a0

import datetime
from playsound import playsound
from cProfile import label
import imp
from PIL import ImageTk, Image  # pip install pillow for image
from gtts import gTTS
import pyttsx3

import tkinter as tk
import speech_recognition as sr
import threading
import winsound
from tkinter import messagebox, Label, Button, filedialog, PhotoImage
import requests
import json

from tktooltip import ToolTip
import emoji
import time


engine = pyttsx3.init()
window = tk.Tk()
window.geometry('530x330')
window.maxsize(530, 350)
window.minsize(530, 350)
window.iconbitmap(r'C:/Users/snawa/OneDrive/Documents/GitHub/MediaPad/app/icon.ico')
engine = pyttsx3.init()

# Function to Reset
def Reset():
    # Msg.set("")
    t1.delete(1.0, 'end')    

# Function to Convert Text to Speech in Python
def clear():
    t1.delete(1.0, 'end')
    
# exit function for button
def exit():
    window.destroy()

# About info function for about button
def about_info():
    tk.messagebox.showinfo(
        "About", "Hello user!\n\nWe very thankful to using our product and always ready to solve your all possible problems.\n\nCheck update!\nwww.mediapad.com/update\n\nIf you are facing any problem please let us know and contact us at help@snawaz.com\n\n\n\t\t\t\tMediaPad Team!")




def on_stop_button_click():
    """
    Stop the current speech
    """
    global engine
    if engine:
        engine.stop()


Msg = tk.StringVar()
t1 = tk.Text(window, width=62, height=10,  pady=5, padx=5)
t1.insert(tk.END, Msg.get())
t1.place(x=10, y=100)


# window heading label
title_t2v = Label(window, text="Text to Voice", font=("Century Gothic", 22, "bold"))
title_t2v.place(x=160, y=15)



def on_gender_select(*args):
    """
    Update the selected gender variable when the dropdown menu changes
    """
    gender = gender_var.get()

def on_speak_button_click():
    gender = gender_var.get()
    if gender == 'English - Male':
        # speak_male()
        engine = pyttsx3.init()
        engine.setProperty("rate", 130)
        engine.setProperty('voice', 'english+m3')
        text = t1.get("1.0", tk.END)
        engine.say(text)
        print("Speak English - Male:\n"+ text)
        engine.runAndWait()

    elif gender == 'English - Female':
        # speak_male()
        engine = pyttsx3.init()
        engine.setProperty('rate', 125)
        engine.setProperty('volume', 1.0)
        
        # speech voices id
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        
        text = t1.get("1.0", tk.END)
        engine.say(text)
        print("Speak English - Female:\n"+ text)
        engine.runAndWait()
        engine.stop()
        
    elif gender == 'Hindi - Female':

        text = t1.get("1.0", tk.END)
        Message = text
        speech = gTTS(text=Message)

        basename = "file"
        suffix = datetime.datetime.now().strftime("%y%m%d_%H%M")
        filename = "_".join([basename, suffix])
        
        fileName = "cache"+filename+'.mp3'
        
        if os.path.exists(fileName):
            os.remove(fileName)
        speech.save(fileName)
        print("Speak Hindi - Female:\n"+ fileName +  text)
        playsound(fileName)
        os.remove(fileName)
 
    elif gender == 'Hindi - Male Hera':
        # speak_hi_female()
        engine = pyttsx3.init()
        engine.setProperty('voice', 'Hi')
        text = t1.get("1.0", tk.END)
        print("Speak Hindi - Male Hera:\n"+ text)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
        
    elif gender == 'Hindi - Female Tara':
        # speak_hi_female()
        engine = pyttsx3.init()
        engine.setProperty('voice', 'Hindi')
        text = t1.get("1.0", tk.END)
        print("Speak Hindi - Female Hera:\n"+ text)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
        
stop_dict = {'stop': False}

def on_speak_button_click():
    gender = gender_var.get()
    text = t1.get("1.0", tk.END)
    def speak():
        # Initialize the text-to-speech engine and set the properties
        if gender == 'English - Male':
            engine = pyttsx3.init()
            engine.setProperty("rate", 130)
            engine.setProperty('voice', 'english+m3')
        elif gender == 'English - Female':
            engine = pyttsx3.init()
            engine.setProperty('rate', 125)
            engine.setProperty('volume', 1.0)
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
        elif gender == 'Hindi - Female':
            text = t1.get("1.0", tk.END)
            Message = text
            speech = gTTS(text=Message)
            basename = "file"
            suffix = datetime.datetime.now().strftime("%y%m%d_%H%M")
            filename = "_".join([basename, suffix])
            fileName = "cache"+filename+'.mp3'
            if os.path.exists(fileName):
                os.remove(fileName)
            speech.save(fileName)
            print("Speak Hindi - Female:\n"+ fileName +  text)
            playsound(fileName)
            os.remove(fileName)
        
        elif gender == 'Hindi - Male Hera':
            engine = pyttsx3.init()
            engine.setProperty('voice', 'Hi')
        elif gender == 'Hindi - Female Tara':
            engine = pyttsx3.init()
            engine.setProperty('voice', 'Hindi')

        # Loop through the text and speak it in chunks
        text_chunks = text.split('\n')
        for chunk in text_chunks:
            if stop_dict['stop']: # Check if the speech should be stopped
                break
            engine.say(chunk)
            engine.runAndWait()

        # Stop the engine and reset the stop_speaking flag
        engine.stop()
        stop_dict['stop'] = True

    threading.Thread(target=speak).start()

def on_stop_button_click():
    stop_dict['stop'] = True
    
    
def on_save_button_click():
    """
    Call the corresponding function based on the selected gender and speak the voice
    """
    
    gender = gender_var.get()
    
    if gender == 'English - Male':
        engine = pyttsx3.init()
        engine.setProperty("rate", 130)
        engine.setProperty('voice', 'english+m3')
        
        text = t1.get("1.0", tk.END)        
        basename = "mp_ttv_e_m"
        suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        filename = "_".join([basename, suffix])
        print("Save English - Male:\n"+ filename + "\n"+ text)
        engine.save_to_file(text, filename+'test.mp3')
        engine.runAndWait()

    elif gender == 'English - Female':
        engine = pyttsx3.init()
        engine.setProperty('rate', 125)
        engine.setProperty('volume', 1.0)
        
        # speech voices id
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        
        text = t1.get("1.0", tk.END)        
        basename = "mp_ttv_e_f"
        suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        filename = "_".join([basename, suffix])
        print("Save English - Female:\n"+ filename + "\n"+ text)
        engine.save_to_file(text, filename+'test.mp3')
        engine.runAndWait()
        
    elif gender =='Hindi - Female':
        text = t1.get("1.0", tk.END)
        Message = text
        speech = gTTS(text=Message)

        basename = "mp_ttv_h_f"
        suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        filename = "_".join([basename, suffix])
        speech.save(filename+'.mp3')
        print("Speak Hindi - Female:\n"+ filename + "\n"+ text)
        playsound(filename+'.mp3')
        
    elif gender =='Hindi - Male Hera':
        
        engine = pyttsx3.init()
        engine.setProperty("rate", 130)
        engine.setProperty('voice', 'Hi')
        
        text = t1.get("1.0", tk.END)        
        basename = "mp_ttv_h_m_h"
        suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        filename = "_".join([basename, suffix])
        print("Save Hindi - Male Hera:\n"+ filename + "\n"+ text)
        engine.save_to_file(text, filename+'test.mp3')
        engine.runAndWait()
        
        
    elif gender == 'Hindi - Female Tara':
        engine = pyttsx3.init()
        engine.setProperty("rate", 130)
        engine.setProperty('voice', 'Hi')
        
        text = t1.get("1.0", tk.END)        
        basename = "mp_ttv_h_m_t"
        suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        filename = "_".join([basename, suffix])
        print("Save Hindi - Male Tara:\n"+ filename + "\n"+ text)
        engine.save_to_file(text, filename+'test.mp3')
        engine.runAndWait()

speak_button = tk.Button(window, text='Play',relief=RIDGE,  width=8, font=('verdana', 10, 'bold'), cursor="hand2", command=on_speak_button_click)
speak_button.place(x=10, y=280)

save_button = tk.Button(window, text='Save',  width=8, font=('verdana', 10, 'bold'), cursor="hand2", command=on_save_button_click)
save_button.place(x=115, y=280)


gender_var = tk.StringVar()
gender_var.set('Select Language')  # Set the default value of the dropdown to Male
gender_var.trace('w', on_gender_select)  # Call on_gender_select when the dropdown value changes

gender_menu = tk.OptionMenu(window, gender_var, 'Select Language', 'English - Male', 'English - Female', 'Hindi - Female',)
gender_menu.config(width=15)
gender_menu.place(x=220, y=280)



# Buttons of bottom line
stop_btn = Button(window, text="Stop", relief=RIDGE, width=8, font=('verdana', 10, 'bold'), cursor="hand2", command=on_stop_button_click)
stop_btn.place(x=370, y=280)

reset_btn = Button(window, text="Reset", relief=RIDGE, width=5, font=('verdana', 10, 'bold'), cursor="hand2", command=Reset)
reset_btn.place(x=467, y=280)

# Buttons of bottom line
about_btn = Button(window, text="About", relief=RIDGE, borderwidth=2, bg="lightgreen", width=8, font=('verdana', 10, 'bold'), cursor="hand2", command=about_info)
about_btn.place(x=370, y=315)

exit_btn = Button(window, text="Exit", relief=RIDGE, borderwidth=2, bg="red", width=5, font=('verdana', 10, 'bold'), cursor="hand2", command=exit)
exit_btn.place(x=467, y=315)

window.mainloop()
