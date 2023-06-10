import tkinter as tk
import speech_recognition as sr

r = sr.Recognizer()

def record():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            # Display the recognized text in the text box
            text_box.insert(tk.END, text + '\n')
        except sr.UnknownValueError:
            text_box.insert(tk.END, "Could not understand audio\n")
        except sr.RequestError as e:
            text_box.insert(tk.END, "Could not request results; {0}\n".format(e))

# Create the GUI window
window = tk.Tk()
window.title("Voice to Text App")

# Create the text box to display the recognized text
text_box = tk.Text(window, height=10, width=50)
text_box.pack()

# Create the Record button to start recording
record_button = tk.Button(window, text="Record", command=record)
record_button.pack()

# Start the GUI event loop
window.mainloop()