#Import all the necessary libraries
from tkinter import *
import tkinter as tk

#Define the tkinter instance
win=  tk.Tk()
win.title("Rounded Button")

#Define the size of the tkinter frame
win.geometry("700x300")

#Define the working of the button

def my_command():
   text.config(text= "You have clicked Me...")

#Import the image using PhotoImage function
click_btn= PhotoImage(file='b1.png')

#Let us create a label for button event
img_label= Label(image=click_btn)

#Let us create a dummy button and pass the image
button= Button(win, image=click_btn,command= my_command,
borderwidth=0)
button.pack(pady=30)

text= Label(win, text= "")
text.pack(pady=30)

win.mainloop()