import tkinter as tk
import pyttsx3


def speak_english_male():
    """
    Speak in English Male voice using the pyttsx3 library
    """
    engine = pyttsx3.init()
    engine.setProperty('voice', 'english+m3')
    engine.say('Hello, I am an English male voice')
    engine.runAndWait()

def speak_english_female():
    """
    Speak in English Female voice using the pyttsx3 library
    """
    engine = pyttsx3.init()
    engine.setProperty('voice', 'english+f3')
    engine.say('Hello, I am an English female voice')
    engine.runAndWait()

def speak_hindi_female():
    """
    Speak in Hindi Female voice using the pyttsx3 library
    """
    print("speaking Hindi female")
    engine = pyttsx3.init()
    engine.setProperty('voice', 'hindi+f3')
    engine.say('नमस्ते, मैं हिंदी में बोलती हूँ')
    engine.runAndWait()

def on_language_select(*args):
    """
    Update the selected language variable when the dropdown menu changes
    """
    language = language_var.get()

def on_speak_button_click():
    """
    Call the corresponding function based on the selected language and speak the voice
    """
    language = language_var.get()
    if language == 'English - Male':
        speak_english_male()
    elif language == 'English - Female':
        speak_english_female()
    elif language == 'Hindi - Female':
        speak_hindi_female()

# Create a GUI window with a Text widget, a dropdown menu, and a button
window = tk.Tk()
window.title('Language Selector')

text_input = tk.Text(window, height=10, width=50)
text_input.pack()

language_var = tk.StringVar()
language_var.set('Select Language')  # Set the default value of the dropdown to "Select Language"
language_var.trace('w', on_language_select)  # Call on_language_select when the dropdown value changes
language_var.set('English - Male')  # Set a default value other than "Select Language"
language_var.set('Select Language')  # Set back the default value to "Select Language"

# style = tk.ttk.Style()  # Create a new Style object
# style.configure('TMenubutton', font=('Verdana', 10, 'bold'))  # Set the font of the OptionMenu

language_menu = tk.OptionMenu(window, language_var, 'Select Language', 'English - Male', 'English - Female', 'Hindi - Female')
language_var.set('Select Language')  # Set back the default value to "Select Language"
language_menu.pack()

speak_button = tk.Button(window, text='Speak', command=on_speak_button_click)
speak_button.pack()

window.mainloop()