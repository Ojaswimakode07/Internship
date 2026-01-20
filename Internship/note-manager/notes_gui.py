import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

NOTES_FOLDER = "notes"

def save_note():
    if not os.path.exists(NOTES_FOLDER):
        os.mkdir(NOTES_FOLDER)

    content = text.get("1.0", tk.END).strip()
    if not content:
        messagebox.showwarning("Warning", "Note cannot be empty")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"note_{timestamp}.txt"

    with open(os.path.join(NOTES_FOLDER, filename), "w") as file:
        file.write(content)

    text.delete("1.0", tk.END)
    messagebox.showinfo("Success", "Note saved successfully")

# GUI Window
root = tk.Tk()
root.title("Simple Note Manager")
root.geometry("400x300")

label = tk.Label(root, text="Write your note:")
label.pack()

text = tk.Text(root, height=10, width=40)
text.pack()

button = tk.Button(root, text="Save Note", command=save_note)
button.pack(pady=10)

root.mainloop()
