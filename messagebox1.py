from tkinter import *
from tkinter import messagebox  # Importing necessary modules

def show_info_message():
    messagebox.showinfo("Info", "This is an information message!")

def show_yes_no_message():
    result = messagebox.askyesno("Yes No", "Do you want to continue?")
    if result:
        messagebox.showinfo("Response", "You clicked Yes!")
    else:
        messagebox.showinfo("Response", "You clicked No!")

def main():
    myMsgApp = Tk()
    myMsgApp.title("Messagebox Examples")

    info_button = Button(myMsgApp, text="Show Info Message", command=show_info_message)
    info_button.pack()

    yes_no_button = Button(myMsgApp, text="Show Yes/No Message", command=show_yes_no_message)
    yes_no_button.pack()

    myMsgApp.mainloop()

main()