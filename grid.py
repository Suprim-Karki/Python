import tkinter as tk
root=tk.Tk()
root.title("My First Gui")
root.geometry("400x300")

tk.Label(root, text="Username:").grid(row=0,column=0)
tk.Label(root, text="Password:",font=("Arial Bold",14)).grid(row=2, column=2, rowspan=1)

tk.Label(root,text="Hello",bg="Cyan").place(x=100,y=100)


tk.Entry(root).grid(row=0,column=1)
root.mainloop()