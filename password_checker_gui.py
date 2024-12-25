import tkinter as tk
from tkinter import messagebox
import re

# Function to evaluate the password strength
def check_password_strength(password):
    score = 0
    if len(password) < 8:
        return "Weak: Password too short!", "red"
    if not re.search(r'[A-Z]', password):
        return "Weak: Add at least one uppercase letter!", "red"
    if not re.search(r'[a-z]', password):
        return "Weak: Add at least one lowercase letter!", "red"
    if not re.search(r'[0-9]', password):
        return "Weak: Add at least one number!", "red"
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Weak: Add at least one special character!", "red"
    
    return "Strong: Good password!", "green"

# Function to suggest improvements for weak passwords
def suggest_improvements(password):
    improvements = []
    if len(password) < 8:
        improvements.append("Make it at least 8 characters long.")
    if not re.search(r'[A-Z]', password):
        improvements.append("Add an uppercase letter.")
    if not re.search(r'[a-z]', password):
        improvements.append("Add a lowercase letter.")
    if not re.search(r'[0-9]', password):
        improvements.append("Include numbers.")
    if not re.search(r'[!@#$%^&*(),.?":{}_`|<>]', password):
        improvements.append("Use special characters.")
    return improvements

# Function to handle the button click event and show results
def evaluate_password():
    password = entry.get()
    result, color = check_password_strength(password)

    # Update strength meter
    strength_meter.config(bg=color)
    strength_label.config(text=f"Strength: {result}")

    # Display suggestions for improvement
    suggestions = suggest_improvements(password)
    messagebox.showinfo("Password Strength", f"{result} Password\n\nSuggestions:\n" + "\n".join(suggestions))

# Create the main window (root)
root = tk.Tk()
root.title("Password Strength Checker")

# Set up the layout of the GUI
tk.Label(root, text="Enter Password:").pack()

entry = tk.Entry(root, show="*")  # The show="*" hides the password characters
entry.pack()

# Strength Meter (Progress Bar)
strength_meter = tk.Label(root, width=30, height=2, relief="solid", bg="gray")
strength_meter.pack(pady=10)

# Password strength label
strength_label = tk.Label(root, text="Strength: ", font=('Arial', 12))
strength_label.pack()

# Button to check the password
tk.Button(root, text="Check", command=evaluate_password).pack()

# Run the application
root.mainloop()
