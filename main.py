################################################################
# Title       : MediaPad | Home                                #
# Authors(s)  : 11202722                                       #
# Coordinator : Rajeev Gupta Sir                               #
# Affiliation :                                                #
# Address     : MMDU, Mullana Ambala                           #
# Date        : 16/06/2022 stable                                    #
# app_version_current = "v3.0.11.6.23"                         #
################################################################

import tkinter as tk
from PIL import ImageTk, Image
import random
import requests
import pyttsx3
import speech_recognition as sr
import webbrowser
import requests
import json
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog, simpledialog, messagebox
from datetime import datetime
import datetime as dt
from tkinter import ttk
from googletrans import Translator
from tkinter import Frame, StringVar, Label, Text, Button, OptionMenu, RIDGE
from gtts import gTTS
import os
import datetime
from playsound import playsound
from tkinter import filedialog, messagebox, PhotoImage,Menu
from PIL import ImageTk, Image
import threading
import speech_recognition as sr
import winsound
from tktooltip import ToolTip


engine = pyttsx3.init()

# Default data and function
app_version_current = "v3.0.11.6.23"

def about_info():
    hyperlink = "www.codesam.in"
    greed = "Thank you for using Mediapad!"
    app_info1 = "We hope that our notepad, translator, voice to text, and text to voice features are helping you be more productive and efficient. "
    app_info2 = "Did you know that Mediapad supports translation for multiple languages, including English, Spanish, French, German, any languages?Give it a try and see how easy it is to communicate in different languages. "
    app_info3 = "Need to take a break from typing? Try out our voice to text feature and dictate your notes and messages instead. "
    app_info4 = "Want to listen to your notes or messages instead of reading them? Our text to voice feature can convert your written   text into spoken words, making it easier for you to absorb information. "
    app_info5 = "Have a question or feedback for us? Feel free to reach out to us at snawaza243@gmail.com and we'll be happy to assist you. "
    about_dev1 = "About Developer:\nShahnawaz Alam is a software developer. He holds a degree in computer science from MM Deemed to be University Mullana, and has worked for several large projects in the past. "
    about_dev2 = "As the lead developer on this project, Shahnawaz was responsible for designing and implementing the software from scratch. \n\nIf you have any questions or feedback about the software, you can contact Shahnawaz at snawaza243@email.com. "
    about_dev3 = "In addition to this project, Shahnawaz has also worked on several other software projects, including web application."
    about_dev4 = "\n\nCheck our blog: www.indiantechnoera.in\n"
    app_info_merge = greed + app_info1 + "\n\n" + app_info2 + "\n\n" + app_info3 + "\n\n" + app_info4 + "\n\n"+app_info5 + "\n\n\n"
    dev_info_merge = about_dev1 +  about_dev2 + about_dev3 + about_dev4 + "\n\n\nDo you want to visit us?"
    message =  app_info_merge + dev_info_merge
    response = messagebox.askyesno("Info", message) 
    if response == True:
        webbrowser.open_new(hyperlink)
        
def exit_root():
    root.destroy();

def exit_win():
    window.destroy();

def get_random_dev_joke():
        url = f"https://sv443.net/jokeapi/v2/joke/Programming?blacklistFlags=nsfw,religious,political,racist,sexist&format=json&lang=en&safe-mode"
        response = requests.get(url)
        data = json.loads(response.content)
        if data["type"] == "single":
            joke = data["joke"]
        else:
            joke = f"{data['setup']} {data['delivery']}"
            print("Not get query you are")
        messagebox.showinfo("MediaPad | Developers Quote of the Day", joke)


start_color = "#32CD32"
stop_color = "#FF0000"
save_color = "#1E90FF"
copy_color = "#FFA500"
clear_color = "#808080"

play_color = "#2ecc71"
drop_color = "#3498db"
stop_color = "#e74c3c"
reset_color = "#95a5a6"
about_color = "#9b59b6"
exit_color = "#e74c3c"

# MediaPad | Notepad
def mp_notepad(title):
    window = tk.Toplevel(root)
    window.title(title)
    window.iconbitmap(r'C:/Users/snawa/OneDrive/Documents/GitHub/MediaPad/app/icon.ico')
    window.geometry('530x350')
    
    #the window widget
    window.resizable(0, 0) # disable the expand  
    
    #creating scrollable notepad window
    notepad = ScrolledText(window, width = 90, height = 40)
    fileName = ' '

    #defining functions for commands
    def cmdNew():     #file menu New option
        global fileName
        if len(notepad.get('1.0', END+'-1c'))>0:
            if messagebox.askyesno("Notepad", "Do you want to save changes?"):
                cmdSave()
            else:
                notepad.delete(0.0, END)
        window.title(title)

    def cmdOpen():     #file menu Open option
        fd = filedialog.askopenfile(parent = window, mode = 'r')
        t = fd.read()     #t is the text read through filedialog
        notepad.delete(0.0, END)
        notepad.insert(0.0, t)

    def cmdSave():     #file menu Save option
        fd = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt')
        if fd!= None:
            data = notepad.get('1.0', END)
        try:
            fd.write(data)
        except:
            messagebox.showerror(title="Error", message = "Not able to save file!")

    def cmdSaveAs():     #file menu Save As option
        fd = filedialog.asksaveasfile(mode='w', defaultextension = '.txt')
        t = notepad.get(0.0, END)     #t stands for the text gotten from notepad
        try:
            fd.write(t.rstrip())
        except:
            messagebox.showerror(title="Error", message = "Not able to save file!")

    def cmdExit():     #file menu Exit option
        if messagebox.askyesno("Notepad", "Are you sure you want to exit?"):
            window.destroy()

    def cmdCut():     #edit menu Cut option
        notepad.event_generate("<<Cut>>")

    def cmdCopy():     #edit menu Copy option
        notepad.event_generate("<<Copy>>")

    def cmdPaste():     #edit menu Paste option
        notepad.event_generate("<<Paste>>")

    def cmdClear():     #edit menu Clear option
        notepad.event_generate("<<Clear>>")

    def cmdFind():     #edit menu Find option
        notepad.tag_remove("Found",'1.0', END)
        find = simpledialog.askstring("Find", "Find what:")
        if find:
            idx = '1.0'     #idx stands for index
        while 1:
            idx = notepad.search(find, idx, nocase = 1, stopindex = END)
            if not idx:
                break
            lastidx = '%s+%dc' %(idx, len(find))
            notepad.tag_add('Found', idx, lastidx)
            idx = lastidx
        notepad.tag_config('Found', foreground = 'white', background = 'blue')
        notepad.bind("<1>", click)

    def click(event):     #handling click event
        notepad.tag_config('Found',background='white',foreground='black')

    def cmdSelectAll():     #edit menu Select All option
        notepad.event_generate("<<SelectAll>>")

    def cmdTimeDate():     #edit menu Time/Date option
        now = datetime.now()
        # dd/mm/YY H:M:S
        dtString = now.strftime("%d/%m/%Y %H:%M:%S")
        label = messagebox.showinfo("Time/Date", dtString)

    #notepad menu items
    notepadMenu = Menu(window)
    window.configure(menu=notepadMenu)

    #file menu
    fileMenu = Menu(notepadMenu, tearoff = False)
    notepadMenu.add_cascade(label='File', menu = fileMenu, )

    #adding options in file menu
    fileMenu.add_command(label='New', command = cmdNew)
    fileMenu.add_command(label='Open...', command = cmdOpen)
    fileMenu.add_command(label='Save', command = cmdSave)
    fileMenu.add_command(label='Save As...', command = cmdSaveAs)
    fileMenu.add_separator()
    fileMenu.add_command(label='Exit', command = cmdExit)

    #edit menu
    editMenu = Menu(notepadMenu, tearoff = False)
    notepadMenu.add_cascade(label='Edit', menu = editMenu)

    #adding options in edit menu
    editMenu.add_command(label='Cut', command = cmdCut)
    editMenu.add_command(label='Copy', command = cmdCopy)
    editMenu.add_command(label='Paste', command = cmdPaste)
    editMenu.add_command(label='Clear', command = cmdClear)
    editMenu.add_separator()
    editMenu.add_command(label='Find', command = cmdFind)
    editMenu.add_command(label='Select All', command = cmdSelectAll)
    editMenu.add_separator()
    editMenu.add_command(label='Time/Date', command = cmdTimeDate)

    #help menu
    helpMenu = Menu(notepadMenu, tearoff = False)
    notepadMenu.add_cascade(label='Help', menu = helpMenu)

    #adding options in help menu
    helpMenu.add_command(label='About Notepad', command = about_info)

    #binding keyboard shortcuts
    window.bind('<Control-n>', lambda e: cmdNew())
    window.bind('<Control-o>', lambda e: cmdOpen())
    window.bind('<Control-s>', lambda e: cmdSave())
    window.bind('<Control-Shift-S>', lambda e: cmdSaveAs())
    window.bind('<Control-q>', lambda e: cmdExit())
    window.bind('<Control-a>', lambda e: cmdSelectAll())
    window.bind('<Control-f>', lambda e: cmdFind())

    notepad.pack()
    window.mainloop()

# Translator
def mp_translator(title):
    window = tk.Toplevel(root)
    window.title(title)

    window.geometry('530x330')
    window.maxsize(530, 350)
    window.minsize(530, 350)
    window.iconbitmap(r'C:/Users/snawa/OneDrive/Documents/GitHub/MediaPad/app/icon.ico')
    Msg = StringVar()
    
    frame = Frame(window, width=530, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open( "C:/Users/snawa/OneDrive/Documents/GitHub/MediaPad/app/bg (3).jpg"))
    # Create a Label Widget to display the text or Image
    label = Label(frame, image=img)
    label.pack()



    # translate function for translate function
    def translate():
        language_1 = t1.get("1.0", "end-1c")
        cl = choose_language.get()

        if language_1 == '':
            messagebox.showerror(
                'MediaPad | Translator', 'Oo\n\nNo text to translate.\nPlease enter text in the first box.\n\n\n\t')

        # inserting output translated text into second text box t2
        else:
            t2.delete(1.0, 'end')
            translator = Translator()
            output = translator.translate(language_1, dest=cl)
            t2.insert('end', output.text)
            clicked_text.config(text= "Text translating")
            clicked_text.after(3000, lambda: clicked_text.config(text=""))

    # copy function for select option
    def copy_trans(t1, clicked_text):
        clicked_text.config(text= "Text copied")
        clicked_text.after(2000, lambda: clicked_text.config(text=""))
        text = t1.get("1.0", tk.END)
        window.clipboard_clear()
        window.clipboard_append(text)
        
    # clear function for select option
    def clear_trans(t1, clicked_text):
        t1.delete(1.0, 'end')
        # t2.delete(1.0, 'end')
        clicked_text.config(text= "Text clean")
        clicked_text.after(3000, lambda: clicked_text.config(text=""))

    def save_trans(t1, t2, clicked_text):
        fd = filedialog.asksaveasfile(mode='wb', defaultextension='.txt')
        if fd is not None:
            input_text = t1.get("1.0", tk.END)
            output_text = t2.get("1.0", tk.END)
            saving_data = "Input Data:\n" + input_text + "\n\nOutput Translated Data:\n" + output_text + "\n\n\n\n\n\n\nDear User,\nThank you for using MediaPad and we appreciate your continued support!\n\nBest regards,\nMediaPad!\n\nwww.indiantechnoera.in\nwww.codesam.in"

            try:
                fd.write(saving_data.encode('utf-8'))
                clicked_text.config(text="Translation saved to the file.")
            except Exception as e:
                messagebox.showerror(title="Error", message="Not able to save file!\n" + str(e))
                clicked_text.config(text="Not saved")


        clicked_text.after(4000, lambda: clicked_text.config(text=""))
    # exit function for button
    def exit():
        window.destroy()

    # Auto-detect language variable input & GUI
    a = tk.StringVar()
    auto_detect = ttk.Combobox(window, width=28, textvariable=a, state='readonly', font=('Century Gothic', 10, 'bold'),)

    auto_detect['values'] = ('Input : Auto-Detect Language',)
    auto_detect.place(x=22, y=70)
    auto_detect.current(0)

    # Choose destination language & GUI
    l = tk.StringVar()
    choose_language = ttk.Combobox(
        window, width=28, textvariable=l, state='readonly', font=('Century Gothic', 10, 'bold'))

    choose_language['values'] = (
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
    
    choose_language.place(x=280, y=70)
    choose_language.current(35)

    # t1 for window text area
    t1 = Text(window, width=30, height=10, borderwidth=2, pady=5, padx=5, relief=RIDGE)
    t1.place(x=10, y=100)

    # t2 for output text area
    t2 = Text(window, width=30, height=10, borderwidth=2, pady=5,  padx=5, relief=RIDGE)
    t2.place(x=260, y=100)


    title_t_ = Label(window, bg='white', text="Translate Now", font=("Century Gothic", 22, "bold"))
    title_t_.place(x=160, y=15)


    trans_btn = Button(window, text="Translate", width=8, bg=play_color, borderwidth=2, font=( 'Century Gothic', 10, ), cursor="hand2", command=translate)
    trans_btn.place(x=10, y=280)


    def on_copy_select(*args):
        copy = copy_var.get()
        
        if copy == 'Copy Input':
            copy_trans(t1, clicked_text)
        elif copy == 'Copy Output':
            copy_trans(t2, clicked_text)
        elif copy == 'Copy All':
            a = t1.get("1.0", tk.END)
            b = t2.get("1.0", tk.END)
            all_data = a+b
            window.clipboard_clear()
            window.clipboard_append(all_data)
            clicked_text.config(text= "Text copied")
            clicked_text.after(2000, lambda: clicked_text.config(text=""))

    def on_clear_select(*args):
        clear = clear_var.get()
        if clear == 'Clear Input':
            clear_trans(t1, clicked_text)
        elif clear == 'Clear Output':
            clear_trans(t2, clicked_text)
        elif clear == 'Clear All':
            t1.delete("1.0", tk.END)
            t2.delete("1.0", tk.END)
            clicked_text.config(text= "All text clear")
            clicked_text.after(2000, lambda: clicked_text.config(text=""))
            


    copy_var = tk.StringVar()
    copy_var.set('Copy Now')  
    copy_var.trace('w', on_copy_select) 
    copy_var.set('Copy') 
    

    clear_var = tk.StringVar()
    clear_var.set('Clear Now')  
    
    clear_var.trace('w', on_clear_select)  
    clear_var.set('Clear')  

    copy_choose_t = tk.OptionMenu(window, copy_var, 'Copy Input', 'Copy Output', 'Copy All')
    copy_choose_t.config(width=12, bg=copy_color, borderwidth=2, font=( 'Century Gothic', 10, ), cursor="hand2",)
    copy_choose_t.place(x=97, y=280)
    
    clear_choose_t = tk.OptionMenu(window, clear_var, 'Clear Input', 'Clear Output', 'Clear All')
    clear_choose_t.config(width=12,bg=clear_color, borderwidth=2, font=( 'Century Gothic', 10, ),  cursor="hand2",)
    clear_choose_t.place(x=236, y=280)
    
    save_btn = Button(window, text="Save All", width=16,bg=save_color, borderwidth=2, font=( 'Century Gothic', 10, ),  cursor="hand2", command=lambda:save_trans(t1,t2, clicked_text))
    save_btn.place(x=379, y=282)
    
    
    

    # current action notification
    clicked_text = Label(window, text="",  anchor="w",  borderwidth=4, width=43, font=('Century Gothic', 10,), cursor="hand2")
    clicked_text.place(x=10, y=315)

    about_btn = Button(window, text="About", relief=RIDGE,  bg=about_color, borderwidth=2, width=7, font=('Century Gothic', 10,), cursor="hand2", command=about_info)
    about_btn.place(x=380, y=315)

    exit_btn = Button(window, text="Close", relief=RIDGE,  borderwidth=2, bg="red", width=6, font=('Century Gothic', 10,), cursor="hand2", command=exit)
    exit_btn.place(x=458, y=315)

    window.mainloop()
    
# Text to voice
def mp_text2voice(title):
    window = tk.Toplevel(root)
    window.title(title)
    window.geometry('530x330')
    window.maxsize(530, 350)
    window.minsize(530, 350)

    window.iconbitmap(r'C:/Users/snawa/OneDrive/Documents/GitHub/MediaPad/app/icon.ico')
    Msg = StringVar()
    
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
        # Update the selected gender variable when the dropdown menu changes
        gender = gender_var.get()
        clicked_text.config(text= "You choose: "+gender)
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
            suffix = dt.datetime.now().strftime("%y%m%d_%H%M")
            filename = "_".join([basename, suffix])

            fileName = "cache"+filename+'.mp3'

            if os.path.exists(fileName):
                os.remove(fileName)
            speech.save(fileName)
            print("Speak Hindi - Female:\n"+ fileName +"\n" + text)
            clicked_text.config(text= "Playing: "+gender)
            playsound(fileName)
            os.remove(fileName)
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
        # Call the corresponding function based on the selected gender and speak the voice

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

    # window heading label
    title_t2v = Label(window, text="Text to Voice", bg='white', font=("Century Gothic", 22, "bold"))
    title_t2v.place(x=160, y=15)


    speak_button = tk.Button(window, text='Play', bg=play_color,  width=8, font=('Century Gothic', 10, ), cursor="hand2",   command=on_speak_button_click)
    speak_button.place(x=10, y=280)

    save_button = tk.Button(window, text='Save', bg=save_color,  width=8, font=('Century Gothic', 10, ), cursor="hand2",    command=on_save_button_click)

    save_button.place(x=110, y=280)

    gender_var = tk.StringVar()
    gender_var.set('Select Language')  # Set the default value of the dropdown to Male
    gender_var.trace('w', on_gender_select)  # Call on_gender_select when the dropdown value changes

    gender_menu = tk.OptionMenu(window, gender_var,  'English - Male', 'English - Female', 'Hindi - Female', 'Hindi - Female Tara', 'Hindi - Male Heera')
    gender_menu.config( width=18, bg=drop_color, cursor="hand2", )
    ToolTip(gender_menu, msg="Choose Language/Gender")
    gender_menu.place(x=205, y=280)


    # Buttons of bottom line
    stop_btn = Button(window, text="Stop", bg=stop_color, width=8, font=('Century Gothic', 10,), cursor="hand2",    command=on_stop_button_click)
    stop_btn.place(x=370, y=280)

    reset_btn = Button(window, text="Clear",  bg=clear_color, width=6, font=('Century Gothic', 10,), cursor="hand2", command=clear)
    reset_btn.place(x=460, y=280)

    # current action notification
    clicked_text = Label(window, text="",  anchor="w",  borderwidth=4, width="42", font=('Century Gothic', 10,), cursor="hand2")
    clicked_text.place(x=10, y=315)


    about_btn = Button(window, text="About", relief=RIDGE, bg=about_color, borderwidth=2, width=8, font=('Century Gothic', 10,),    cursor="hand2", command=about_info)
    about_btn.place(x=370, y=315)

    exit_btn = Button(window, text="Close", relief=RIDGE, bg='red', width=6, font=('Century Gothic', 10,), cursor="hand2", command=exit)
    exit_btn.place(x=460, y=315)
    window.mainloop()


# Voice to text
def mp_voice2text(title):
    window = tk.Toplevel(root)
    window.title(title)

    # window = tk.Tk()
    window.geometry('530x330')
    window.maxsize(530, 350)
    window.minsize(530, 350)

    window.iconbitmap(r'C:/Users/snawa/OneDrive/Documents/GitHub/MediaPad/app/icon.ico')
    frame = Frame(window, width=530, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)
    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open("C:/Users/snawa/OneDrive/Documents/GitHub/MediaPad/app/bg (3).jpg"))
    # Create a Label Widget to display the text or Image
    label = Label(frame, image=img)
    label.pack()

    r = sr.Recognizer()
    recording = False

    def start_record():
        global recording
        recording = True
        # Beep to indicate that recording has started
        winsound.Beep(440, 200)

        def record_thread():
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                while recording:
                    audio = r.listen(source)
                    try:
                        text = r.recognize_google(audio)
                        # Display the recognized text in the text box
                        text_box.insert(tk.END, text + '\n')
                    except sr.UnknownValueError:
                        text_box.insert(tk.END, "Could not understand voice\n")
                    except sr.RequestError as e:
                        text_box.insert(tk.END, "Could not request results; {0}\n".format(e))

        # Create a new thread for recording
        thread = threading.Thread(target=record_thread)
        # Set the thread as a daemon so that it will terminate when the main thread terminates
        thread.daemon = True
        # Start the thread
        thread.start()
        clicked_text.config(text= "Recording started...")

    def stop_record():
        clicked_text.config(text= "Recording stopped.")
        clicked_text.after(2000, lambda: clicked_text.config(text=""))
        global recording
        recording = False

    def copy_text():
        clicked_text.config(text= "Text copied")
        clicked_text.after(2000, lambda: clicked_text.config(text=""))
        # Get the text from the text box
        text = text_box.get("1.0", tk.END)
        # Copy the text to the clipboard
        window.clipboard_clear()
        window.clipboard_append(text)

    def clear_text():
        clicked_text.config(text= "Text clean")
        clicked_text.after(2000, lambda: clicked_text.config(text=""))
        # Clear the text box
        text_box.delete("1.0", tk.END)

    def save_text():
        # Get the text from the text box
        text = text_box.get("1.0", tk.END)
        # Ask the user to choose a file name to save the text
        file_name = filedialog.asksaveasfilename(defaultextension=".txt")
        # Save the text to the chosen file
        if file_name:
            try:
                with open(file_name, "wb") as f:
                    f.write(text.encode('utf-8'))
                    clicked_text.config(text="Data saved to the file.")
            except Exception as e:
                messagebox.showerror(title="Error", message="Not able to save file!\n" + str(e))
                clicked_text.config(text="Not saved")
                



    
    def show_about():
        # Display the About dialog box
        tk.messagebox.showinfo("About", "Voice to Text App v1.0\nDeveloped by Your Name")   

    def exit_app():
        # Exit the application
        window.destroy()

    # Create the text box to display the recognized text
    text_box = tk.Text(window, width=62, height=10, borderwidth=2, pady=5, padx=5)
    # text_box.pack()
    text_box.place(x=10, y=100)


    # label
    title_v2t = Label(window, text="Voice to Text",highlightthickness=0, highlightbackground="white", bg='white' ,font=("Century Gothic", 22, "bold"))
    title_v2t.place(x=160, y=15) 

    # start button with fun
    record_btn = Button(window, text="Start", bg=start_color,  width=8, font=('Century Gothic', 10,), cursor="hand2", command=start_record)
    record_btn.place(x=10, y=280)
    
    stop_btn = Button(window, text="Stop", bg=stop_color,  width=8, font=('Century Gothic', 10,), cursor="hand2", command=stop_record)
    stop_btn.place(x=105, y=280)
    
    # copy button with fun
    copy_btn = Button(window, text="Copy", bg=copy_color,   width=8, font=('Century Gothic', 10,), cursor="hand2", command=copy_text)
    copy_btn.place(x=200, y=280)
    
    
    # save button with fun
    save_btn = Button(window, text="Save", bg=save_color,   width=8, font=('Century Gothic', 10,), cursor="hand2", command=save_text)
    save_btn.place(x=290, y=280)

    # clean button with fun
    clear_btn = Button(window, text="Clear", bg=clear_color,  width=16, font=('Century Gothic', 10,), cursor="hand2", command=clear_text)
    clear_btn.place(x=380, y=280)



    # current action notification
    clicked_text = Label(window, text="",  anchor="w",  borderwidth=4, width="43", font=('Century Gothic', 10,), cursor="hand2")
    clicked_text.place(x=10, y=315)


    about_btn = Button(window, text="About", relief=RIDGE,   borderwidth=2, bg=about_color, width=8, font=('Century Gothic', 10,), cursor="hand2", command=about_info)
    about_btn.place(x=380, y=315)

    exit_btn = Button(window, text="Close", relief=RIDGE,  borderwidth=2, bg="red", width=5, font=('Century Gothic', 10,), cursor="hand2", command=exit_app)
    exit_btn.place(x=466, y=315)

    # Start the GUI event loop
    window.mainloop()



####################### Home ####################
root = tk.Tk()
root.title('MediaPad | Home')
root.geometry('530x400')
root.maxsize(530, 400)
root.minsize(530, 400)
root.iconbitmap(r'C:/Users/snawa/OneDrive/Documents/GitHub/MediaPad/app/icon.ico')

frame = Frame(root, width=530, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("C:/Users/snawa/OneDrive/Documents/GitHub/MediaPad/app/bg (3).jpg"))
# Create a Label Widget to display the text or Image
label = Label(frame, image=img)
label.pack()


def exit():
    root.destroy()

title_home_lab = Label(root,  text="MediaPad", font=( "Century Gothic", 32, "bold"), bg='white')
title_home_lab.place(x=175, y=20)


# Create the buttons
projectTitle0 = "MediaPad | Notepad"
projectTitle1 = "MediaPad | Translator"
projectTitle2 = "MediaPad | Text to Voice"
projectTitle3 = "MediaPad | Voice to Text"

# color0High = "#0011cc"
# color0Low = "#0011aa"
# color1High = "#990099"
# color1Low = "#990044"
# color2High = "#0099aa"
# color2Low = "#006688"
# color3High = "#88bb22"
# color3Low = "#88bb66"


color0High = "#009688"
color0Low = "#00796B"
color1High = "#FF5722"
color1Low = "#E64A19"
color2High = "#2196F3"
color2Low = "#1976D2"
color3High = "#B0BEC5"
color3Low = "#808080"

# random developer joke
click_btn= PhotoImage(file='C:/Users/snawa/OneDrive/Documents/GitHub/MediaPad/app/quote.png')
#Let us create a label for button event
img_label= Label(image=click_btn)
#Let us create a dummy button and pass the image
joke_btn= Button(root, image=click_btn, borderwidth=0, cursor="hand2", bg='white', command=get_random_dev_joke)
ToolTip(joke_btn, msg="Todays Developer Quote")
joke_btn.place(x=147, y=5)


mp_face_them_1= PhotoImage(file='C:/Users/snawa/OneDrive/Documents/GitHub/MediaPad/app/mp-face-1.png')
mp_face_them_11= Label(image=mp_face_them_1, bg='white', padx=10)
mp_face_them_11.place(x=35+20, y=110+5)

mp_face_them_2= PhotoImage(file='C:/Users/snawa/OneDrive/Documents/GitHub/MediaPad/app/mp-face-2.png')
mp_face_them_22= Label(image=mp_face_them_2, bg='white', padx=10)
mp_face_them_22.place(x=35+20, y=170+5)

mp_face_them_3= PhotoImage(file='C:/Users/snawa/OneDrive/Documents/GitHub/MediaPad/app/mp-face-3.png')
mp_face_them_33= Label(image=mp_face_them_3, bg='white', padx=10)
mp_face_them_33.place(x=35+20, y=230+5)

mp_face_them_4= PhotoImage(file='C:/Users/snawa/OneDrive/Documents/GitHub/MediaPad/app/mp-face-4.png')
mp_face_them_44= Label(image=mp_face_them_4, bg='white', padx=10)
mp_face_them_44.place(x=35+20, y=290+5)






mp_nm_btn = Button(root, text="Notepad",       width=34, height=2, command=lambda: mp_notepad(projectTitle0),      font=('Century Gothic', 12, 'bold'), cursor="hand2", borderwidth=2, bg=color0High, fg="white", activebackground=color0Low, activeforeground="white", )
mp_tr_btn = Button(root, text="Translator",    width=34, height=2, command=lambda: mp_translator(projectTitle1),   font=('Century Gothic', 12, 'bold'), cursor="hand2", borderwidth=2, bg=color1High, fg="white", activebackground=color1Low, activeforeground="white", )
mp_ttv_btn = Button(root, text="Text 2 Voice", width=34, height=2, command=lambda: mp_text2voice(projectTitle2),   font=('Century Gothic', 12, 'bold'), cursor="hand2", borderwidth=2, bg=color2High, fg="white", activebackground=color2Low, activeforeground="white", )
mp_vtt_btn = Button(root, text="Voice 2 text", width=34, height=2, command=lambda: mp_voice2text(projectTitle3),   font=('Century Gothic', 12, 'bold'), cursor="hand2", borderwidth=2, bg=color3High, fg="white", activebackground=color3Low, activeforeground="white", )

mp_nm_btn.bind("<Enter>", lambda e: mp_nm_btn.config(bg=color0Low))
mp_nm_btn.bind("<Leave>", lambda e: mp_nm_btn.config(bg=color0High))
mp_tr_btn.bind("<Enter>", lambda e: mp_tr_btn.config(bg=color1Low))
mp_tr_btn.bind("<Leave>", lambda e: mp_tr_btn.config(bg=color1High))
mp_ttv_btn.bind("<Enter>", lambda e: mp_ttv_btn.config(bg=color2Low))
mp_ttv_btn.bind("<Leave>", lambda e: mp_ttv_btn.config(bg=color2High))
mp_vtt_btn.bind("<Enter>", lambda e: mp_vtt_btn.config(bg=color3Low))
mp_vtt_btn.bind("<Leave>", lambda e: mp_vtt_btn.config(bg=color3High))

mp_nm_btn.place(x=115, y=100 + 10)
mp_tr_btn.place(x=115, y=160 + 10)
mp_ttv_btn.place(x=115, y=220 + 10)
mp_vtt_btn.place(x=115, y=280 + 10)




version_date = Label(root,  text=app_version_current, font=( "Century Gothic", 10, ), bg='white')
version_date.place(x=55, y=370)


about_btn = Button(root, text="About", relief=RIDGE,   borderwidth=2, bg=about_color, width=8, font=('Century Gothic', 10,), cursor="hand2", command=about_info)
about_btn.place(anchor='center', x=392, y=375)

exit_btn = Button(root, text="Exit", relief=RIDGE,  borderwidth=2, bg="red", width=7, font=('Century Gothic', 10,), cursor="hand2", command=exit)
exit_btn.place(anchor='center', x=478, y=375)



root.mainloop()