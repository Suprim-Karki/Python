# import tkinter as tk
# from tkinter import *

# root = tk.Tk()
# root.geometry("400x400")
# root.title("Counter")
# root.config(bg="cyan")
# count = 0

# def increase():
#     global count
#     count += 1
#     label.config(text=f"Count : {count}")

# Label(root, text="Click to increase count").pack()
# btn = Button(root, text="Click", command=increase).pack()

# # Separate creation and packing of the label
# label = Label(root, text="Count : 0")
# label.pack()

# root.mainloop()

import tkinter as tk
from tkinter import *
from tkinter import messagebox

root = tk.Tk()
root.geometry("400x400")
root.title("Counter")
root.config(bg="cyan")

# def checkPrime():
#     c=0
#     x=entry.get()
#     n=int(entry.get())
#     if(n<=2):
#         label.config(text="Prime")
#     else:
#         for i in range(2,len(x)-1):
#             if n % i == 0:
#                 label.config(text="Not Prime")
#                 return
#     label.config(text=f"{n} is Prime")

# Label(root, text="Enter a number").pack()
# entry=Entry(root)
# entry.pack()
# btn = Button(root, text="Click to check prime", command=checkPrime).pack()

# # Separate creation and packing of the label
# label = Label(root, text="")
# label.pack()



def quit_func():
    print("Lol")
    check = messagebox.askquestion("Quit?", "Are you sure you want to quit? ")
    if check == "yes":
        root.destroy()
    else:
        messagebox.showinfo("Continue", "Continue")


quit_btn = Button(root,text="Quit",command=quit_func)
quit_btn.pack()



root.mainloop()