import tkinter as tk
import pyttsx3

def speak_male():
    """
    Speak a male voice using the pyttsx3 library
    """
    engine = pyttsx3.init()
    engine.setProperty('voice', 'english+m3')
    engine.say('Hello, I am a male voice')
    engine.runAndWait()

def speak_female():
    """
    Speak a female voice using the pyttsx3 library
    """
    engine = pyttsx3.init()
    engine.setProperty('voice', 'english+f3')
    engine.say('Hello, I am a female voice')
    engine.runAndWait()

def on_gender_select(*args):
    """
    Call the corresponding function based on the selected gender
    """
    gender = gender_var.get()
    if gender == 'Male':
        speak_male()
    elif gender == 'Female':
        speak_female()

# Create a GUI window with a Text widget, a dropdown menu, and a button
root = tk.Tk()
root.title('Gender Selector')

text_input = tk.Text(root, height=10, width=50)
text_input.pack()

gender_var = tk.StringVar()
gender_var.set('Male')  # Set the default value of the dropdown to Male
gender_var.trace('w', on_gender_select)  # Call on_gender_select when the dropdown value changes

gender_menu = tk.OptionMenu(root, gender_var, 'Male', 'Female')
gender_menu.pack()

root.mainloop()