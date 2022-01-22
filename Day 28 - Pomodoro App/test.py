# from tkinter import *
#
# root = Tk()
#
# button = Button(root, text="Click me!")
# img = PhotoImage(file="tomato.png") # make sure to add "/" not "\"
# button.config(image=img)
# button.pack() # Displaying the button
#
# root.mainloop()

import tkinter as tk

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="This should be centered")
        label.grid(row=1, column=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).grid(sticky="nsew")
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.mainloop()