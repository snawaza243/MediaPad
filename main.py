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
#                  MediaPad Home View                 #
#######################################################
import os
import tkinter.messagebox
from tkinter import messagebox
from tkinter import filedialog,simpledialog
from tkinter.scrolledtext import ScrolledText
import tkinter as tk
from tkinter import ttk
from tkinter import *
 


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
engine = pyttsx3.init()

# Notepad
def create_window0(title):
    window = tk.Toplevel(root)
    window.title(title)
    window.iconbitmap(r'C:/Users/snawa/OneDrive/Documents/GitHub/MediaPad/component/mpi.ico')
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
        window.title("Notepad")

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

    def cmdAbout():     #help menu About option
        label = messagebox.showinfo("About Notepad", "Notepad by - \nMediaPad")

    #notepad menu items
    notepadMenu = Menu(window)
    window.configure(menu=notepadMenu)

    #file menu
    fileMenu = Menu(notepadMenu, tearoff = False)
    notepadMenu.add_cascade(label='File', menu = fileMenu)

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
    helpMenu.add_command(label='About Notepad', command = cmdAbout)

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
def create_window1(title):
    window = tk.Toplevel(root)
    window.title(title)

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

    # exit function for button
    def exit():
        window.destroy()

    # About info function for about button
    def aboutinfo():
        tkinter.messagebox.showinfo(
            "MediaPad", "\nThank you for using this application.\n\nCheck update at www.mediapad.com/update\n\nMail us for more info. snawaza243@gmail.com\n\n\n\t\t\tMediaPad")

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


    bTranslate1 = Button(window, text="Translate", width=8, relief=RIDGE, borderwidth=2, font=(
        'verdana', 10, 'bold'), cursor="hand2", command=translate)
    bTranslate1.place(x=10, y=315)

    bclear1 = Button(window, text="Clear", width=8, relief=RIDGE, borderwidth=2,
                    font=('verdana', 10, 'bold'), cursor="hand2", command=clear)
    bclear1.place(x=115, y=315)

    bcopy1 = Button(window, text="Copy ", width=8, relief=RIDGE, borderwidth=2,
                    font=('verdana', 10, 'bold'), cursor="hand2", command=clear)
    bcopy1.place(x=220, y=315)



    babout1 = Button(window, text="About", relief=RIDGE, borderwidth=2, bg="lightgreen",
                    font=('verdana', 10, 'bold'), cursor="hand2", command=aboutinfo)
    babout1.place(x=380, y=315)


    bexit1 = Button(window, text="Exit", relief=RIDGE, borderwidth=2, bg="red",
                    font=('verdana', 10, 'bold'), cursor="hand2", command=exit)
    bexit1.place(x=467, y=315)
    window.mainloop()
    
# Text to voice
def create_window2(title):
    window = tk.Toplevel(root)
    window.title(title)
    window.geometry('530x330')
    window.maxsize(530, 350)
    window.minsize(530, 350)
    # window.iconbitmap(r'mpi.ico')
    # window = tk.Tk()
    # window.iconbitmap('mpi.ico')

    window.iconbitmap(r'C:/Users/snawa/OneDrive/Documents/GitHub/MediaPad/component/mpi.ico')
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
    ltranslate = Label(window, text="Text to Voice",
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

# Voice to text
def create_window3(title):
    window = tk.Toplevel(root)
    window.title(title)

    # window = tk.Tk()
    window.geometry('530x330')
    window.maxsize(530, 350)
    window.minsize(530, 350)

    # p1 = PhotoImage(file = 'info.png')
    # # Setting icon of master window
    # window.iconphoto(False, p1)
    # # window.iconbitmap(r'mpi.ico')



    window.iconbitmap(r'C:/Users/snawa/OneDrive/Documents/GitHub/MediaPad/component/mpi.ico')



    Msg = StringVar()

    # text area
    t1 = Text(window, width=62, height=10, borderwidth=2,
            pady=5, padx=5, relief=RIDGE)
    t1.place(x=10, y=100)
    # Function to Reset


    def Reset():
        t1.set("")

    # Function to Convert Text to Speech in Python

    def clear():
        t1.delete(1.0, 'end')
    # exit function for button


    def exit():
        window.destroy()

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
                window.title(os.path.basename(file) + " - Notepad ")
        else:
            f = open(file, "w")
            f.write(t1.get(1.0, END))
            f.close()


    def Copyt():
        t1.event_generate(("<<Copy>>"))


    # Ringht click menu list in  text area
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

    # instruction label
    ltranslate = Label(window, text="Voice to  Text",
                    font=("Century Gothic", 22, "bold"))
    ltranslate.place(x=160, y=15)
    button4 = Button(window, text="Record", relief=RIDGE, borderwidth=3, width=8,
                    font=('verdana', 10, 'bold'), cursor="hand2", command=recordnow)
    button4.place(x=10, y=315)

    button5 = Button(window, text="Save", relief=RIDGE, borderwidth=3, width=8, 
                    font=('verdana', 10, 'bold'), cursor="hand2", command=saveFile)
    button5.place(x=110, y=315)

    button6 = Button(window, text="Copy", relief=RIDGE, borderwidth=3, width=8,
                    font=('verdana', 10, 'bold'), cursor="hand2", command=Copyt)
    button6.place(x=200, y=315)

    button7 = Button(window, text="Clear", relief=RIDGE, borderwidth=3, width=8,
                    font=('verdana', 10, 'bold'), cursor="hand2", command=Reset)
    button7.place(x=290, y=315)


    # Buttons of bottom line


    babout1 = Button(window, text="About", relief=RIDGE, borderwidth=2, bg="lightgreen", width=8,
                    font=('verdana', 10, 'bold'), cursor="hand2", command=aboutinfo)
    babout1.place(x=380, y=315)

    bexit1 = Button(window, text="Exit", relief=RIDGE, borderwidth=2, bg="red", width=5,
                    font=('verdana', 10, 'bold'), cursor="hand2", command=exit)
    bexit1.place(x=467, y=315)
    window.mainloop()



root = tk.Tk()
root.title('MediaPad: Home')
root.geometry('530x400')
root.maxsize(530, 400)
root.minsize(530, 400)
root.iconbitmap(r'C:/Users/snawa/OneDrive/Documents/GitHub/MediaPad/component/mpi.ico')

# root.iconbitmap(r'C:/Users/snawa/Desktop/Py_Pro_01_2.9/mpi.ico')

frame = Frame(root, width=530, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open(
    "C:/Users/snawa/OneDrive/Documents/GitHub/MediaPad/component/bgs.png"))
# Create a Label Widget to display the text or Image
label = Label(frame, image=img)
label.pack()

# Function to call root file poth

def aboutinfo():
    tkinter.messagebox.showinfo(
        "MediaPad", "\nThank you for using this application.\n\nCheck update at www.mediapad.com/update\n\nMail us for more info. snawaza243@gmail.com\n\n\n\t\t\tMediaPad")

def exit():
    root.destroy()

lhead = Label(root,  text="MediaPad", font=( "Century Gothic", 32, "bold"), bg='white')
lhead.place(x=160, y=20)


# Create the buttons
projectTitle0 = "MediaPad: Notepad"
projectTitle1 = "MediaPad: Translator"
projectTitle2 = "MediaPad: Text-to-Voice"
projectTitle3 = "MediaPad: Voice-to-text"

color0High = "#0011cc"
color0Low = "#0011aa"
color1High = "#990099"
color1Low = "#990044"
color2High = "#0099aa"
color2Low = "#006688"
color3High = "#88bb22"
color3Low = "#88bb66"


button0 = Button(root, text="Notepad", width=34, height=2, command=lambda: create_window0(projectTitle0), relief=RIDGE, borderwidth=3, font=('verdana', 11, 'bold'), cursor="hand2",bg=color0High, fg="white", activebackground=color0Low, activeforeground="white")
button1 = Button(root, text="Translator", width=34, height=2, command=lambda: create_window1(projectTitle1), relief=RIDGE, borderwidth=3, font=('verdana', 11, 'bold'), cursor="hand2",bg=color1High, fg="white", activebackground=color1Low, activeforeground="white")
button2 = Button(root, text="Text-to-Voice",width=34, height=2, command=lambda: create_window2(projectTitle2), relief=RIDGE, borderwidth=3, font=('verdana', 11, 'bold'), cursor="hand2",bg=color2High, fg="white", activebackground=color2Low, activeforeground="white")
button3 = Button(root, text="Voice-to-text", width=34, height=2, command=lambda: create_window3(projectTitle3), relief=RIDGE, borderwidth=3, font=('verdana', 11, 'bold'), cursor="hand2",bg=color3High, fg="white", activebackground=color3Low, activeforeground="white")



button0.bind("<Enter>", lambda e: button0.config(bg=color0Low))
button0.bind("<Leave>", lambda e: button0.config(bg=color0High))
button1.bind("<Enter>", lambda e: button1.config(bg=color1Low))
button1.bind("<Leave>", lambda e: button1.config(bg=color1High))
button2.bind("<Enter>", lambda e: button2.config(bg=color2Low))
button2.bind("<Leave>", lambda e: button2.config(bg=color2High))
button3.bind("<Enter>", lambda e: button3.config(bg=color3Low))
button3.bind("<Leave>", lambda e: button3.config(bg=color3High))


button0.place(x=115, y=100 + 10)
button1.place(x=115, y=160 + 10)
button2.place(x=115, y=220 + 10)
button3.place(x=115, y=280 + 10)

bAbout = Button(root, text="About", relief=RIDGE, borderwidth=1, font=( 'verdana', 10, 'bold'), cursor="hand2", bg='light blue', command=aboutinfo)
bAbout.place(anchor='center', x=425, y=375)

buttonexitM = Button(root, text="Exit", relief=RIDGE, borderwidth=1, font=('verdana', 10, 'bold'), cursor="hand2", bg='red', command=exit)
buttonexitM.place(anchor='center', x=486, y=375)
root.mainloop()