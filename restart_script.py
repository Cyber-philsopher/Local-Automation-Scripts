import tkinter as tk
from tkinter import messagebox
import os

def restart_system():
    result = messagebox.askquestion("It's time you restart your system", "Do you want to restart the system?")
    if result == 'yes':
        os.system("shutdown /r /t 1")  # Restart the system after 1 second

# Create the root window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Prompt the user to restart the system
restart_system()

# Run the Tkinter event loop
root.mainloop()
 
