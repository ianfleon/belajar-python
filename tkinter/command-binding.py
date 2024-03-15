import tkinter as tk
from tkinter import ttk

# Init Tk Object
root = tk.Tk()

# Callback Function when Event Listener
def button_clicked(msg = "Yo"):
    print("Btn Clicked! " + msg)

# Run Bind function without param.
# button = ttk.Button(root, text="Click Me", command=button_clicked)
    
# Run Bind function using param.
button = ttk.Button(
    root,
    text="Tekan Saya", 
    command=lambda: button_clicked("Yuhu")
)

# Assign Widget to Root
button.pack()

# Run App
root.mainloop()