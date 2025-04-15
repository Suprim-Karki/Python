from tkinter import *  # import tkinter library
from tkinter import ttk

myImgApp = Tk()  # Create a basic window - myImgApp
myImgApp.title("Lecture 9 Image Demo")  # Give a name to the window
myImgApp.geometry("300x300")  # Set the window size
myImgApp.configure(background="LightBlue2")  

# Function to handle button click to show image
def showImg():
    default = "mountain.png"
    imgDefault = PhotoImage(file=default)
    imgDefault = imgDefault.subsample(1, 1)

    print("image: " + str(imgDefault))

    # Set up label to show image
    imgLabel = Label(myImgApp, image=imgDefault)
    imgLabel.grid(row=4, column=0, sticky=NE)
    imgLabel.image = imgDefault  # Keep a reference to avoid garbage collection

# Create buttons
showImgButton = ttk.Button(myImgApp, text="Show Image", command=showImg)
showImgButton.grid(row=2, column=0, sticky=E)

QuitButton = ttk.Button(myImgApp, text="Quit", command=myImgApp.destroy)
QuitButton.grid(row=2, column=1, sticky=E)

myImgApp.mainloop()  # Keeps the window alive, listening for events