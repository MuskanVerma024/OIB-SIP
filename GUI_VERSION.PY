import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def update_total_length(*args):
    total = letters_var.get() + numbers_var.get() + symbols_var.get()
    length_label.config(text=f"Total Password Length: {total}")

def generate_password():
    n_letters = letters_var.get()
    n_numbers = numbers_var.get()
    n_symbols = symbols_var.get()

    if n_letters == 0 and n_numbers == 0 and n_symbols == 0:
        messagebox.showwarning("Input Error", "Please select at least one character type.")
        return

    password_list = []

    password_list += [random.choice(string.ascii_letters) for _ in range(n_letters)]
    password_list += [random.choice(string.digits) for _ in range(n_numbers)]
    password_list += [random.choice(string.punctuation) for _ in range(n_symbols)]

    random.shuffle(password_list)
    password = ''.join(password_list)
    result_var.set(password)

def copy_to_clipboard():
    password = result_var.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Copy Error", "No password to copy.")

# GUI Setup
root = tk.Tk()
root.title("🔐 Advanced Password Generator")
root.geometry("420x450")
root.config(bg="#f0f4f7", padx=20, pady=20)

# Variables
letters_var = tk.IntVar(value=6)
numbers_var = tk.IntVar(value=2)
symbols_var = tk.IntVar(value=2)
result_var = tk.StringVar()

# Heading
tk.Label(root, text="🔐 Password Generator", font=("Arial", 18, "bold"), bg="#f0f4f7").pack(pady=10)

# Sliders
tk.Label(root, text="Number of Letters:", font=("Arial", 12), bg="#f0f4f7").pack(anchor="w")
tk.Scale(root, from_=0, to=20, orient="horizontal", variable=letters_var, command=update_total_length).pack(fill="x")

tk.Label(root, text="Number of Numbers:", font=("Arial", 12), bg="#f0f4f7").pack(anchor="w")
tk.Scale(root, from_=0, to=20, orient="horizontal", variable=numbers_var, command=update_total_length).pack(fill="x")

tk.Label(root, text="Number of Symbols:", font=("Arial", 12), bg="#f0f4f7").pack(anchor="w")
tk.Scale(root, from_=0, to=20, orient="horizontal", variable=symbols_var, command=update_total_length).pack(fill="x")

# Total length
length_label = tk.Label(root, text="", font=("Arial", 12, "italic"), bg="#f0f4f7", fg="#555")
length_label.pack(pady=5)
update_total_length()

# Buttons
tk.Button(root, text="Generate Password", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=generate_password).pack(pady=10)

# Result entry
tk.Entry(root, textvariable=result_var, font=("Courier", 14), width=30, justify="center").pack(pady=5)

# Copy button
tk.Button(root, text="Copy to Clipboard", font=("Arial", 11), bg="#2196F3", fg="white", command=copy_to_clipboard).pack(pady=5)

# Footer
tk.Label(root, text="Internship Project — Muskan Verma", font=("Arial", 9, "italic"), bg="#f0f4f7", fg="#888").pack(side="bottom", pady=10)

root.mainloop()
