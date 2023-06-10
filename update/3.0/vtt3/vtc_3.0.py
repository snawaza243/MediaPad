import tkinter as tk
import speech_recognition as sr
import threading
import winsound
from tkinter import Frame, messagebox, Label, Button, filedialog, PhotoImage
from tkinter import RIDGE
import requests
import json

from PIL import ImageTk, Image  # pip install pillow for image
from tktooltip import ToolTip
import emoji
import time
import re


# Create the GUI window
window = tk.Tk()
window.title("Voice to Text App")

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
        with open(file_name, "w") as f:
            f.write(text)
    clicked_text.config(text= "Text saved")
    clicked_text.after(2000, lambda: clicked_text.config(text=""))
    
def get_random_dev_joke():
    url = f"https://sv443.net/jokeapi/v2/joke/Programming?blacklistFlags=nsfw,religious,political,racist,sexist&format=json&lang=en&safe-mode"
    response = requests.get(url)
    data = json.loads(response.content)
    if data["type"] == "single":
        joke = data["joke"]
    else:
        joke = f"{data['setup']} {data['delivery']}"
    messagebox.showinfo("Random Developer Joke", joke)

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

# Create the Record button to start recording
# button bg color
start_color = "#32CD32"
stop_color = "#FF0000"
save_color = "#1E90FF"
copy_color = "#FFA500"
clear_color = "#808080"


record_btn = Button(window, text="Start", bg=start_color,  width=8, font=('Century Gothic', 10,), cursor="hand2", command=start_record)
record_btn.place(x=10, y=280)

# record button with fun
stop_btn = Button(window, text="Stop", bg=stop_color,  width=8, font=('Century Gothic', 10,), cursor="hand2", command=stop_record)
stop_btn.place(x=105, y=280)

# save button with fun

save_btn = Button(window, text="Save", bg=save_color,   width=8, font=('Century Gothic', 10,), cursor="hand2", command=save_text)
save_btn.place(x=200, y=280)

# copy button with fun
copy_btn = Button(window, text="Copy", bg=copy_color,   width=8, font=('Century Gothic', 10,), cursor="hand2", command=copy_text)
copy_btn.place(x=290, y=280)

# clean button with fun
clear_btn = Button(window, text="Clear", bg=clear_color,  width=8, font=('Century Gothic', 10,), cursor="hand2", command=clear_text)
clear_btn.place(x=380, y=280)


# random developer joke

click_btn= PhotoImage(file='smile.png')

#Let us create a label for button event
img_label= Label(image=click_btn)

#Let us create a dummy button and pass the image
joke_btn= Button(window, image=click_btn, borderwidth=0, cursor="hand2", command=get_random_dev_joke)
ToolTip(joke_btn, msg="See Today Developer Joke")

joke_btn.place(x=475, y=275)




# # show the action update text
# clicked_text = Label(window, text=" ",   borderwidth=2,  font=('', 10, 'bold'), cursor="hand2")
# clicked_text.place(x=10, y=315)

# current action notification
clicked_text = Label(window, text="",  anchor="w",  borderwidth=4, width="42", font=('Century Gothic', 10,), cursor="hand2")
clicked_text.place(x=10, y=315)


about_btn = Button(window, text="About", relief=RIDGE,   borderwidth=2, bg="lightgreen", width=8, font=('Century Gothic', 10,), cursor="hand2", command=show_about)
about_btn.place(x=380, y=315)

exit_btn = Button(window, text="Exit", relief=RIDGE,  borderwidth=2, bg="red", width=5, font=('Century Gothic', 10,), cursor="hand2", command=exit)
exit_btn.place(x=467, y=315)

exit_btn = Button(window, text="Exit", relief=RIDGE, bg='red', width=6, font=('Century Gothic', 10,), cursor="hand2", command=exit_app)
exit_btn.place(x=460, y=315)



# Start the GUI event loop
window.mainloop()