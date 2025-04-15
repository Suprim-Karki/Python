import tkinter as tk
from PIL import Image, ImageTk # Pillow Library

root = tk.Tk()
root.title("Image in Tkinter")

# tk_image = tk.PhotoImage(file="mountain.png")  # Use a PNG or GIF image # tk.PhotoImage does not support resizing.

image = Image.open("mountain.png")  
image = image.resize((10, 10))  # Resize to (width=300, height=200)
tk_image = ImageTk.PhotoImage(image) # Convert to Tkinter-compatible image

label = tk.Label(root, image=tk_image)
label.pack()

root.mainloop()


'''import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Image in Tkinter")
root.geometry("700x300")

tk_image = tk.PhotoImage(file="mountain.png") 
def show_img():
    label = tk.Label(root, image=tk_image)
    label.grid(row=1,column=0,columnspan=3)
def hide_img():
    Label(root,text="",height=20,width=70).grid(row=1,column=0,columnspan=2)

def quit_func():
    root.quit()''


show_btn=Button(root,text="Show Image",command=show_img)
show_btn.grid(row=0,column=0,padx=10,pady=30)
hide_btn=Button(root,text="Hide Image",command=hide_img)
hide_btn.grid(row=0,column=1,padx=10,pady=30)
quit_btn=Button(root,text="Quit",command=quit_func)
quit_btn.grid(row=0,column=2)
Label(root,text="",height=20,width=70).grid(row=1,column=0,columnspan=3)


root.mainloop()'''

