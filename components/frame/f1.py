import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dropdown Demo")
        
        # create the dropdown menu
        self.options = ["Option 1", "Option 2", "Option 3"]
        self.selected_option = tk.StringVar(self)
        self.selected_option.set(self.options[0])
        dropdown = tk.OptionMenu(self, self.selected_option, *self.options, command=self.on_dropdown_change)
        dropdown.pack(pady=10)
        
        # create the initial frame
        self.current_frame = self.create_frame("Option 1")
        self.current_frame.pack(pady=10)
        
    def create_frame(self, option):
        """Create a new frame based on the selected option."""
        frame = tk.Frame(self)
        if option == "Option 1":
            label = tk.Label(frame, text="Frame for Option 1")
            label.pack()
        elif option == "Option 2":
            label = tk.Label(frame, text="Frame for Option 2")
            label.pack()
        elif option == "Option 3":
            label = tk.Label(frame, text="Frame for Option 3")
            label.pack()
        return frame
    
    def on_dropdown_change(self, option):
        """Handler for when the dropdown selection changes."""
        self.current_frame.destroy()
        self.current_frame = self.create_frame(option)
        self.current_frame.pack(pady=10)
        
if __name__ == "__main__":
    app = App()
    app.mainloop()