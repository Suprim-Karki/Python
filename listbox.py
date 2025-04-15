from tkinter import *

root=Tk()

def submit():
    item=[]
    for index in listbox.curselection():
        item.append(listbox.get(index))
    print("You have ordered: ")
    for i in item:
        print(i)
def add():
    item=entryBox.get()
    listbox.insert(listbox.size()-1,item)
    listbox.config(height=listbox.size())
def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())

listbox=Listbox(root, bg="#F7FFDE",width=12,selectmode=MULTIPLE)
listbox.pack()
listbox.insert(0,"Pizza")
listbox.insert(1,"Pasta")
listbox.insert(2,"Garlic")
listbox.insert(3,"Egg")
listbox.insert(4,"Roast")

listbox.config(height=listbox.size())

entryBox=Entry(root)
entryBox.pack()

submitBtn=Button(root,text="Submit",command=submit)
submitBtn.pack()

addBtn=Button(root,text="Add",command=add)
addBtn.pack()

deleteBtn=Button(root,text="Delete",command=delete)
deleteBtn.pack()


root.mainloop()
