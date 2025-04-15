import tkinter as tk
root = tk.Tk()
root.geometry("300x400")
root.title("My gui")
root.config(background="Teal")

tk.Label(root, text="Hello", font=("Ariel",40,"bold"), fg="Cyan", bg="Magenta", relief="raised",bd=10).pack() #sunken
# tk.Entry().grid(row=1,column=4, columnspan=5, rowspan=10)
def submit():
    first_name = entry_first.get().strip()
    print("Hello"+first_name)
entry_first = tk.Entry(root, width=15)
entry_first.pack()
tk.Button(root,text="Submit",command=submit).pack()

cs=tk.BooleanVar()
cs.set(True)
tk.Checkbutton(root, variable=cs, text="Click",).pack()

tk.Radiobutton(root,text="O1", value="O1").pack()
tk.Radiobutton(root,text="O2", value="O2").pack()
tk.Radiobutton(root,text="O3", value="O3").pack()


root.mainloop()



    