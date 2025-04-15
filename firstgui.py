import tkinter as tk
from tkinter import Checkbutton

root=tk.Tk()
root.title("My First Gui")
root.geometry("400x300")
label = tk.Label(root, text="Hello")
label.pack()
entry=tk.Entry(root, width=20)
entry.pack()
button=tk.Button(root, text="Click Me", command="")
button.pack()

text_box= tk.Text(root, height=5, width=40)
text_box.pack()

chk_state = tk.BooleanVar()
chk_state.set(True)
chk=Checkbutton(root,text="Aapke Toothpaste Mei Namak Hai?",var=chk_state)
chk.pack()

radio1=tk.Radiobutton(root, text="Option 1", value="Option 1")
radio2=tk.Radiobutton(root, text="Option 2", value="Option 2")
radio1.pack()
radio2.pack()



# Start the event loop
root.mainloop()