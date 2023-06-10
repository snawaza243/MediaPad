import tkinter as tk
import speech_recognition as sr
import threading
import winsound

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
                    text_box.insert(tk.END, "Could not understand audio\n")
                except sr.RequestError as e:
                    text_box.insert(tk.END, "Could not request results; {0}\n".format(e))

    # Create a new thread for recording
    thread = threading.Thread(target=record_thread)
    # Set the thread as a daemon so that it will terminate when the main thread terminates
    thread.daemon = True
    # Start the thread
    thread.start()

def stop_record():
    global recording
    recording = False

def copy_text():
    # Get the text from the text box
    text = text_box.get("1.0", tk.END)
    # Copy the text to the clipboard
    window.clipboard_clear()
    window.clipboard_append(text)

def clear_text():
    # Clear the text box
    text_box.delete("1.0", tk.END)

def show_about():
    # Display the About dialog box
    tk.messagebox.showinfo("About", "Voice to Text App v1.0\nDeveloped by Your Name")

def exit_app():
    # Exit the application
    window.destroy()

# Create the GUI window
window = tk.Tk()
window.title("Voice to Text App")

# Create the text box to display the recognized text
text_box = tk.Text(window, height=10, width=50)
text_box.pack()

# Create the Record button to start recording
record_button = tk.Button(window, text="Record", command=start_record)
record_button.pack()

# Create the Stop button to stop recording
stop_button = tk.Button(window, text="Stop", command=stop_record)
stop_button.pack()

# Create the Copy button to copy the recognized text to the clipboard
copy_button = tk.Button(window, text="Copy", command=copy_text)
copy_button.pack()

# Create the Clear button to clear the text box
clear_button = tk.Button(window, text="Clear", command=clear_text)
clear_button.pack()

# Create the About button to display the About dialog box
about_button = tk.Button(window, text="About", command=show_about)
about_button.pack()

# Create the Exit button to exit the application
exit_button = tk.Button(window, text="Exit", command=exit_app)
exit_button.pack()

# Beep to indicate that the microphone is on
winsound.Beep(440, 200)

# Start the GUI event loop
window.mainloop()