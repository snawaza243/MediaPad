import tkinter as tk
import tkinter.messagebox as messagebox
import webbrowser

def show_hyperlink_message():
    hyperlink = "https://www.google.com"
    message = "Click here to visit Google"
    response = messagebox.askyesno("Hyperlink Message", message)
    if response == True:
        webbrowser.open_new(hyperlink)

# Example usage:
root = tk.Tk()

button = tk.Button(root, text="Show Hyperlink Message", command=show_hyperlink_message)
button.pack()

root.mainloop()