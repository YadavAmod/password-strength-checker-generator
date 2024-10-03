import tkinter as tk
from tkinter import ttk
import random
import string
import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one number")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include at least one special character")

    strength = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"][min(score, 4)]
    return strength, feedback

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

class PasswordApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Password Strength Checker and Generator")
        self.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Enter Password:").pack(pady=5)
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.pack(pady=5)

        ttk.Button(self, text="Check Strength", command=self.check_strength).pack(pady=5)

        self.strength_label = ttk.Label(self, text="")
        self.strength_label.pack(pady=5)

        self.feedback_label = ttk.Label(self, text="", wraplength=350)
        self.feedback_label.pack(pady=5)

        ttk.Button(self, text="Generate Password", command=self.generate_and_show).pack(pady=5)

        self.generated_password = ttk.Label(self, text="")
        self.generated_password.pack(pady=5)

    def check_strength(self):
        password = self.password_entry.get()
        strength, feedback = check_password_strength(password)
        self.strength_label.config(text=f"Strength: {strength}")
        self.feedback_label.config(text="\n".join(feedback))

    def generate_and_show(self):
        password = generate_password()
        self.generated_password.config(text=f"Generated Password: {password}")

if __name__ == "__main__":
    app = PasswordApp()
    app.mainloop()