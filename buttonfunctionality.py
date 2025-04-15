import tkinter as tk
from tkinter import *
from tkinter import ttk

myApp = Tk()

# Functionality: Button click event
def button_click1():
    """
    - In this tkinter program, label is a global label widget that updates dynamically when the user clicks the button. 
    - It does not return a value like a typical function in Python. 
    - Instead, it modifies the GUI elements directly.
    - tkinter functions do not need to return text, they just update the displayed content dynamically
    - button_click1() modifies label using .config(text=...).
    """
    label.config(text="Button clicked!",background="Cyan")
    button1.config(text="Button clicked!",background="Cyan")
    

# Creating Button widgets
button1 = ttk.Button(myApp, text="Click me", style='Custom.TButton', command=button_click1)
button1.pack() 

# Functionality: Label widget for displaying messages
label = ttk.Label(myApp, text="Click the button to see a message.")
label.pack()

myApp.mainloop()