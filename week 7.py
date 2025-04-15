import tkinter as tk
from tkinter import *

r=Tk()
r.geometry("400x400")
r.config(bg="lightblue")


count=0
def counter():
    global count
    count+=1
    c.config(text=count)
    change()

Label(r,text="Tap Count").grid(row=0,column=0,padx=10,pady=10)
c = Label(r,text="0")
c.grid(row=0, column=1,padx=10,pady=10)

btn = Button(r,text="Click Me!",command=counter,relief=SUNKEN)
btn.grid(row=1,column=0,padx=10,pady=10)

def quit():
    r.destroy()

quitbtn = Button(r,text="Quit",command=quit)
quitbtn.grid(row=1,column=1)

# 3
# c=0
# def change():
#     global c
#     c+=1
#     if c%2==0:
#         color_btn.config(text="Even",bg="red")
#     else:
#         color_btn.config(text="Odd",bg="blue")

# color=Label(r,text="Colour").grid(row=0,column=3)

# color_btn=Button(r,text="Even",bg="red",command=change)
# color_btn.grid(row=1,column=3)

# 4
# x=0
# def change():
#     global x
#     x+=1
#     if x % 3 == 0:
#         color_btn.config(bg="red", padx=5, width=3)
#         color_btn.grid(row=1, column=2)
#     elif x % 3 == 1:
#         color_btn.config(bg="yellow", padx=5, width=3)
#         color_btn.grid(row=2, column=2)
#     else:
#         color_btn.config(bg="green", padx=5, width=3)
#         color_btn.grid(row=4, column=2)

x=0
def change():
    global x
    x+=1
    if x % 4 == 0:
        color_btn.config(bg="green", padx=5, width=3)
        color_btn.grid(row=1, column=2)
        color_btn2.grid_forget()
    elif x % 4 == 1:
        color_btn.config(bg="yellow", padx=5, width=3)
        color_btn.grid(row=2, column=2)
        color_btn2.grid_forget()
    elif x % 4 == 2:
        color_btn.config(bg="red", padx=5, width=3)
        color_btn.grid(row=4, column=2)
        color_btn2.grid_forget()
    else:
        color_btn.config(bg="red", padx=5, width=3)
        color_btn.grid(row=4, column=2)
        color_btn2.grid(row=2,column=2)


color=Label(r,text="Colour").grid(row=0,column=2)
# Label(r,text="",height=1,width=0).grid(row=3,column=0)
r.grid_rowconfigure(3, minsize=20) 

color_btn=Button(r,bg="green",command=change,padx=5,width=3)
color_btn2=Button(r,bg="yellow",command=change,padx=5,width=3)



color_btn2.grid_forget()


color_btn.grid(row=1,column=2)

# Qn No - 09
photoimg = PhotoImage('thinking.jpg')
photo_label = Label(text="Test",image=photoimg,compound=BOTTOM)
photo_label.grid(row=4, column=3)

r.mainloop()
