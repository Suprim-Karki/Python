import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")

# Create a ttk Style instance
style = ttk.Style()

# Define a custom label style (without affecting 'TLabel')
style.configure(
    'CustomRed.TLabel',  # Unique style name
    background='red',
    foreground='white',
    font=('Arial', 12, 'bold'),
    padding=10
)

# Create labels with different styles
label1 = ttk.Label(root, text="Default Label", style="TLabel")  # Uses default theme
label2 = ttk.Label(root, text="Custom Red Label", style="CustomRed.TLabel")  # Uses custom style
# label = ttk.Label(root, text="Custom Label", background="red", foreground="white") #inline styling; won't affect other label

# Pack the labels
label1.pack(pady=10)
label2.pack(pady=10)

# Run the main loop
root.mainloop()