from tkinter import *

r=Tk()
r.geometry("300x300")
r.title("Frames")

frameee=Frame(r,bg="blue",bd=5,relief=RAISED)
frameee.place(x=100,y=100)
Button(frameee,width=3,text="W").pack(side=TOP)
Button(frameee,width=3,text="A").pack(side=LEFT)
Button(frameee,width=3,text="S").pack(side=LEFT)
Button(frameee,width=3,text="D").pack(side=LEFT)












r.mainloop()