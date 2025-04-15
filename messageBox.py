from tkinter import *
from tkinter import ttk, messagebox, filedialog  # Importing necessary modules
import os
import shutil

def show_info_message():
    messagebox.showinfo("Info", "This is an information message!")

def show_warning_message():
    messagebox.showwarning("Warning", "This is a warning message!")

def show_error_message():
    messagebox.showerror("Error", "This is an error message!")

def show_question_message():
    result = messagebox.askquestion("Question", "Do you want to continue?")
    if result == "yes":
        messagebox.showinfo("Response", "You clicked Yes!")
    else:
        messagebox.showinfo("Response", "You clicked No!")

def show_ok_cancel_message():
    result = messagebox.askokcancel("OK Cancel", "Do you want to proceed?")
    if result:
        messagebox.showinfo("Response", "You clicked OK!")
    else:
        messagebox.showinfo("Response", "You clicked Cancel!")

def show_yes_no_message():
    result = messagebox.askyesno("Yes No", "Do you want to continue?")
    if result:
        messagebox.showinfo("Response", "You clicked Yes!")
    else:
        messagebox.showinfo("Response", "You clicked No!")

def show_retry_cancel_message():
    result = messagebox.askretrycancel("Retry Cancel", "Do you want to retry?")
    if result:
        messagebox.showinfo("Response", "You clicked Retry!")
    else:
        messagebox.showinfo("Response", "You clicked Cancel!")

def main():
    myMsgApp = Tk()
    myMsgApp.title("Messagebox Examples")

    info_button = Button(myMsgApp, text="Show Info Message", command=show_info_message)
    info_button.pack()

    warning_button = Button(myMsgApp, text="Show Warning Message", command=show_warning_message)
    warning_button.pack()

    error_button = Button(myMsgApp, text="Show Error Message", command=show_error_message)
    error_button.pack()

    question_button = Button(myMsgApp, text="Show Question Message", command=show_question_message)
    question_button.pack()

    ok_cancel_button = Button(myMsgApp, text="Show OK/Cancel Message", command=show_ok_cancel_message)
    ok_cancel_button.pack()

    yes_no_button = Button(myMsgApp, text="Show Yes/No Message", command=show_yes_no_message)
    yes_no_button.pack()

    retry_cancel_button = Button(myMsgApp, text="Show Retry/Cancel Message", command=show_retry_cancel_message)
    retry_cancel_button.pack()

    myMsgApp.mainloop()


main()