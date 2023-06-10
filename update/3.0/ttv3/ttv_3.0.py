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
from tkinter import messagebox, Label, Button, filedialog, PhotoImage, font
import requests
import json

from tktooltip import ToolTip
import emoji
import time


window = tk.Tk()
window.title("MediaPad | Text2Voice")
window.geometry('530x330')
window.maxsize(530, 350)
window.minsize(530, 350)
window.iconbitmap(r'C:/Users/snawa/OneDrive/Documents/GitHub/MediaPad/app/icon.ico')

frame = Frame(window, width=530, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open(
    "C:/Users/snawa/OneDrive/Documents/GitHub/MediaPad/app/bg (3).jpg"))
# Create a Label Widget to display the text or Image
label = Label(frame, image=img)
label.pack()




# Function to Convert Text to Speech in Python
def clear():
    t1.delete(1.0, 'end')
    clicked_text.config(text= "Text clear")
    clicked_text.after(3000, lambda: clicked_text.config(text=""))
    
# exit function for button
def exit():
    window.destroy()

# About info function for about button
def about_info():
    tk.messagebox.showinfo( "About", "Thank you for using Mediapad! We hope that our notepad, translator, voice to text, and text to voice features are helping you be more productive and efficient.\n\n\nDid you know that Mediapad supports translation for multiple languages, including English, Spanish, French, German, any languages? Give it a try and see how easy it is to communicate in different languages.\n\nNeed to take a break from typing? Try out our voice to text feature and dictate your notes and messages instead.\n\nWant to listen to your notes or messages instead of reading them? Our text to voice feature can convert your written text into spoken words, making it easier for you to absorb information.\n\nHave a question or feedback for us? Feel free to reach out to us at snawaza243@gmail.com and we'll be happy to assist you.")

def on_stop_button_click():
    global engine
    if engine:
        engine.stop()

Msg = tk.StringVar()
t1 = tk.Text(window, width=62, height=10,  pady=5, padx=5)
t1.insert(tk.END, Msg.get())
t1.place(x=10, y=100)
engine = pyttsx3.init()


def on_gender_select(*args):
    """
    Update the selected gender variable when the dropdown menu changes
    """
    gender = gender_var.get()
    clicked_text.config(text= "You chooses: "+gender)
    # clicked_text.after(3000, lambda: clicked_text.config(text=""))
    

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
        threading.Thread.start()
        current_info_label.after(2000, text="Speaking English - Male")
        clicked_text.config(text= "Playing: "+gender)
        # clicked_text.after(3000, lambda: clicked_text.config(text=""))

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
        clicked_text.config(text= "Playing: "+gender)
        # clicked_text.after(3000, lambda: clicked_text.config(text=""))

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
        clicked_text.config(text= "Playing: "+gender)
        # clicked_text.after(3000, lambda: clicked_text.config(text=""))
        
    elif gender == 'Hindi - Male Hera':
        # speak_hi_female()
        engine = pyttsx3.init()
        engine.setProperty('voice', 'Hi')
        text = t1.get("1.0", tk.END)
        print("Speak Hindi - Male Hera:\n"+ text)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
        clicked_text.config(text= "Playing: "+gender)
        # clicked_text.after(3000, lambda: clicked_text.config(text=""))

    elif gender == 'Hindi - Female Tara':
        # speak_hi_female()
        engine = pyttsx3.init()
        engine.setProperty('voice', 'Hindi')
        text = t1.get("1.0", tk.END)
        print("Speak Hindi - Female Hera:\n"+ text)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
        clicked_text.config(text= "Playing: "+gender)
        # clicked_text.after(3000, lambda: clicked_text.config(text=""))

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
        clicked_text.config(text= "Saved in "+gender + "as " + filename)

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
        clicked_text.config(text= "Saved in "+gender + " as " + filename)

    elif gender =='Hindi - Female':
        text = t1.get("1.0", tk.END)
        Message = text
        speech = gTTS(text=Message)

        basename = "mp_ttv_h_f"
        suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        filename = "_".join([basename, suffix])
        speech.save(filename+'.mp3')
        print("Speak Hindi - Female:\n"+ filename + "\n"+ text)
        # playsound(filename+'.mp3')
        clicked_text.config(text= "Saved in "+gender + " as " + filename)

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
        clicked_text.config(text= "Saved in "+gender + " as " + filename)


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
        clicked_text.config(text= "Saved in "+gender + " as " + filename)


start_color = "#32CD32"
stop_color = "#FF0000"
save_color = "#1E90FF"
copy_color = "#FFA500"
clear_color = "#808080"

play_color = "#2ecc71"
save_color = "#f39c12"
drop_color = "#3498db"
stop_color = "#e74c3c"
reset_color = "#95a5a6"
about_color = "#9b59b6"
exit_color = "#e74c3c"

# window heading label
title_t2v = Label(window, text="Text to Voice", bg='white', font=("Century Gothic", 22, "bold"))
title_t2v.place(x=160, y=15)


speak_button = tk.Button(window, text='Play', bg=play_color,  width=8, font=('Century Gothic', 10, ), cursor="hand2", command=on_speak_button_click)
speak_button.place(x=10, y=280)

save_button = tk.Button(window, text='Save', bg=save_color,  width=8, font=('Century Gothic', 10, ), cursor="hand2", command=on_save_button_click)

save_button.place(x=110, y=280)


gender_var = tk.StringVar()
gender_var.set('Select Language')  # Set the default value of the dropdown to Male
gender_var.trace('w', on_gender_select)  # Call on_gender_select when the dropdown value changes

gender_menu = tk.OptionMenu(window, gender_var, 'Select Language', 'English - Male', 'English - Female', 'Hindi - Female', 'Hindi - Nemale Tara', 'Hindi - Male Heera')
gender_menu.config( width=18, bg=drop_color, cursor="hand2", )
ToolTip(gender_menu, msg="Choose Language/Gender")
gender_menu.place(x=205, y=280)


# Buttons of bottom line
stop_btn = Button(window, text="Stop", bg=stop_color, width=8, font=('Century Gothic', 10,), cursor="hand2", command=on_stop_button_click)
stop_btn.place(x=370, y=280)

reset_btn = Button(window, text="Reset",  bg=reset_color, width=6, font=('Century Gothic', 10,), cursor="hand2", command=clear)
reset_btn.place(x=460, y=280)

# current action notification
clicked_text = Label(window, text="",  anchor="w",  borderwidth=4, width="42", font=('Century Gothic', 10,), cursor="hand2")
clicked_text.place(x=10, y=315)


about_btn = Button(window, text="About", relief=RIDGE, bg=about_color, borderwidth=2, width=8, font=('Century Gothic', 10,), cursor="hand2", command=about_info)
about_btn.place(x=370, y=315)

exit_btn = Button(window, text="Exit", relief=RIDGE, bg='red', width=6, font=('Century Gothic', 10,), cursor="hand2", command=exit)
exit_btn.place(x=460, y=315)
window.mainloop()
