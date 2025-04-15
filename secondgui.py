import tkinter as tk

root = tk.Tk()
root.title("User Form")
root.geometry("400x250")  # Adjust window size

# Change background color
root.config(bg="Teal")  # Set background color to light blue

# First Name Entry (Left)
tk.Label(root, text="First").grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
entry_first = tk.Entry(root, width=15)
entry_first.grid(row=0, column=1, padx=5, pady=5, sticky="w")

# Last Name Entry (Right)
tk.Label(root, text="Last").grid(row=0, column=2, padx=5, pady=5, sticky="e")
entry_last = tk.Entry(root, width=15)
entry_last.grid(row=0, column=3, padx=5, pady=5, sticky="e")

# Gender Selection (Radio Buttons)
tk.Label(root, text="Gender").grid(row=1, column=0, padx=5, pady=5, sticky="w")
gender_var = tk.StringVar(value="Male")  # Default value

tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=1, column=1, sticky="w")
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=1, column=2, sticky="w")

# Description Box
tk.Label(root, text="Describe yourself:").grid(row=2, column=0, columnspan=4, padx=5, pady=5, sticky="w")
text_desc = tk.Text(root, height=4, width=40)
text_desc.grid(row=3, column=0, columnspan=4, padx=5, pady=5)

# Thank You (Centered at bottom)
thank_you_label = tk.Label(root, text="Thank You!", font=("Arial", 12, "bold"))
thank_you_label.grid(row=4, column=0, columnspan=4, pady=10)

root.mainloop()