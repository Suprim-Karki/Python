from tkinter import *
from tkinter import ttk, messagebox, filedialog  # Importing necessary modules
import os
import shutil

path = "img/"
def addFile():
    filetypes = (("Image files", "*.png;*.jpg;*.jpeg;*.gif"), ("All files", "*.*")) # "All files", "*.*" allows the user to see and select any file.
    
    selectFile = filedialog.askopenfilename(initialdir="./", title = "Select File", filetypes = filetypes)
    if selectFile:
        print(selectFile)
        check = messagebox.askquestion("Add a New File", "Are you sure you want to add a new file? ")
        print('check: ' , check)
        if check == "yes":
            shutil.copy(selectFile, "./newFiles/")
        else:
            messagebox.showinfo("Add a New File", "Changed your mind, file not added")

myFileDialogApp = Tk()
myFileDialogApp.title("myFileDialogApp-Demo") 
myFileDialogApp.geometry("200x100")
myFileDialogApp.configure(background = "LightBlue2")
style = ttk.Style()
style.theme_use('alt')
style.configure('TButton', background = 'black', foreground = 'white', width = 12, borderwidth=1, focusthickness=3, focuscolor='blue')
style.map('TButton', background=[('active','red')])

addFileButton = ttk.Button(myFileDialogApp, text = "Add File", command = addFile)
addFileButton.grid(row = 2, column = 1, sticky = E)

myFileDialogApp.mainloop()