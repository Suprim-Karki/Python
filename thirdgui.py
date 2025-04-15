import tkinter as tk
import json

root = tk.Tk()
root.title("User Form")
root.geometry("400x300")
root.config(bg="lightblue")

# First Name Entry
tk.Label(root, text="First Name", bg="yellow", relief="solid", bd=2).grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_first = tk.Entry(root, width=15)
entry_first.grid(row=0, column=1, padx=5, pady=5, sticky="w")

# Last Name Entry
tk.Label(root, text="Last Name", bg="yellow", relief="solid", bd=2).grid(row=0, column=2, padx=5, pady=5, sticky="w")
entry_last = tk.Entry(root, width=15)
entry_last.grid(row=0, column=3, padx=5, pady=5, sticky="w")

# Gender Selection
tk.Label(root, text="Gender").grid(row=1, column=0, padx=5, pady=5, sticky="w")
gender_var = tk.StringVar(value="Male")
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=1, column=1, sticky="w")
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=1, column=2, sticky="w")

# Description Box
tk.Label(root, text="Describe yourself:").grid(row=2, column=0, columnspan=4, padx=5, pady=5, sticky="w")
text_desc = tk.Text(root, height=4, width=40)
text_desc.grid(row=3, column=0, columnspan=4, padx=5, pady=5)

# Thank You Label (Hidden Initially)
thank_you_label = tk.Label(root, text="Thank You!", font=("Arial", 12, "bold"), fg="green")
thank_you_label.grid(row=5, column=0, columnspan=4, pady=10)
thank_you_label.grid_remove()  # Hide initially

# Form Submitted Message Label (Hidden Initially)
submitted_label = tk.Label(root, text="Form has been submitted!", font=("Arial", 10), fg="blue")
submitted_label.grid(row=6, column=0, columnspan=4, pady=5)
submitted_label.grid_remove()  # Hide initially

# Submit Button Function
def submit_form():
    first_name = entry_first.get().strip()
    last_name = entry_last.get().strip()
    description = text_desc.get("1.0", tk.END).strip()

    # if not first_name or not last_name:
    #     print("Error: First and Last name are required!")
    #     return  # Prevent submission if fields are empty

    data = {
        "First Name": first_name,
        "Last Name": last_name,
        "Gender": gender_var.get(),
        "Description": description
    }

    print("Form Data (as JSON):")
    print(json.dumps(data, indent=4, ensure_ascii=False))
    print("Form has been submitted!")  # Message in console

    thank_you_label.grid()  # Show "Thank You!" message
    submitted_label.grid()  # Show "Form submitted!" message in the window

# Submit Button
submit_btn = tk.Button(root, text="Submit", command=submit_form)
submit_btn.grid(row=4, column=0, columnspan=4, pady=10)

root.mainloop()