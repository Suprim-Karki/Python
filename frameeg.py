from tkinter import *
import tkinter as tk

def calculate():
    try:
        len_val = int(lengthVal.get())
        wid_val = int(widthVal.get())
        print(len_val, wid_val)  # Debugging output
        area = len_val * wid_val
        print(area)  # Debugging output
        showArea.configure(text=area)  # Display calculated area
    except ValueError:
        showArea.configure(text="Error")  # Handle invalid inputs

def reset():
    lengthField.delete(0, END)
    widthField.delete(0, END)
    showArea.configure(text="")  # Clear the result label

myApp = Tk()
myApp.title("Frames & Entry Demo version 1")
myApp.geometry("500x500")
myApp.configure(background="LightBlue2")
myApp.resizable(True, True)

## Create Frames
btnFrame = LabelFrame(myApp, text="Menu panel:", height=40, width=300)
btnFrame.configure(background="beige")
btnFrame.grid(row=0, column=0, pady=10, sticky="NW")

calcFrame = LabelFrame(myApp, text="Results frame", height=100, width=500)
calcFrame.grid(row=2, column=0, sticky="NW")
calcFrame.configure(background="teal")

## Add buttons
rectBtn = tk.Button(btnFrame, text="Rectangle", width=10, command=calculate)
rectBtn.grid(row=0, column=0)

clearBtn = tk.Button(btnFrame, text="Clear", width=10, command=reset)
clearBtn.grid(row=0, column=1)

quitBtn = tk.Button(btnFrame, text="Quit", width=10, command=myApp.destroy)
quitBtn.grid(row=0, column=3)
 
## Add Input Fields for Area Calculation
lengthVal = StringVar()
widthVal = StringVar()

lengthField = Entry(calcFrame, textvariable=lengthVal, width=5)
lengthField.grid(row=2, column=2, padx=10, pady=10)

widthField = Entry(calcFrame, textvariable=widthVal, width=5)
widthField.grid(row=3, column=2, padx=10, pady=10)

## Labels
Label(calcFrame, text="Length:").grid(row=2, column=1, padx=5, pady=5, sticky="e")
Label(calcFrame, text="Width:").grid(row=3, column=1, padx=5, pady=5, sticky="e")

labelArea = Label(calcFrame, text="Area:", width=10)
labelArea.grid(row=4, column=1)

showArea = Label(calcFrame, text="", width=10)
showArea.grid(row=4, column=2)

myApp.mainloop()