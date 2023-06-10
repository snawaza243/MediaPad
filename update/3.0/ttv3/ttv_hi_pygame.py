from gtts import gTTS
import pygame
import tkinter as tk

pygame.init()

def text_to_speech():
    """
    Convert text to speech using the gTTS library and play the speech using the pygame library
    """
    text = text_input.get()
    language = 'en'
    speech = gTTS(text=text, lang=language)
    speech.save("speech.mp3")

    pygame.mixer.music.load("speech.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pass

def clear_text():
    """
    Clear the text input field
    """
    text_input.delete(0, tk.END)

# Create a GUI window with text input and buttons for generating and playing speech
root = tk.Tk()
root.title('Text to Speech')


text_input = tk.Entry(root, width=50)
text_input.pack()

generate_button = tk.Button(root, text='Generate Speech', command=text_to_speech)
generate_button.pack()

clear_button = tk.Button(root, text='Clear Text', command=clear_text)
clear_button.pack()

root.mainloop()

pygame.quit()