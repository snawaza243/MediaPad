import tkinter as tk
import requests
import json
import tkinter.messagebox as messagebox

def get_random_dev_joke():
    url = f"https://sv443.net/jokeapi/v2/joke/Programming?blacklistFlags=nsfw,religious,political,racist,sexist&format=json&lang=en&safe-mode"
    response = requests.get(url)
    data = json.loads(response.content)
    if data["type"] == "single":
        joke = data["joke"]
    else:
        joke = f"{data['setup']} {data['delivery']}"
    messagebox.showinfo("Random Developer Joke", joke)

# Example usage
root = tk.Tk()
button = tk.Button(root, text="Get Random Developer Joke", command=get_random_dev_joke)
button.pack()
root.mainloop()