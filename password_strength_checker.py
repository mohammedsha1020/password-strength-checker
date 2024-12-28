import tkinter as tk
from tkinter import ttk
import re

def check_password_strength(password):
    length_criteria = len(password) >= 8
    upper_case_criteria = re.search(r'[A-Z]', password) is not None
    lower_case_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None #Changes as for the need

    criteria_met = sum([length_criteria, upper_case_criteria, lower_case_criteria,
                        digit_criteria, special_char_criteria])

    if criteria_met == 5:
        return "Very Strong", "#4CAF50", 100  # Green
    elif criteria_met == 4:
        return "Strong", "#8BC34A", 80  # Light Green
    elif criteria_met == 3:
        return "Moderate", "#FFC107", 60  # Yellow
    elif criteria_met == 2:
        return "Weak", "#FF9800", 40  # Orange
    else:
        return "Very Weak", "#F44336", 20  # Red

def update_strength(event):
    password = password_entry.get()
    strength, color, value = check_password_strength(password)
    strength_label.config(text=strength, bg=color)
    progress_bar['value'] = value
    progress_bar['style'] = 'TProgressbar'  # Reset style to default
    progress_bar['maximum'] = 100  # Set maximum value for the progress bar

    # Change the color of the progress bar based on strength
    if strength == "Very Strong":
        progress_bar['style'] = 'green.Horizontal.TProgressbar'
    elif strength == "Strong":
        progress_bar['style'] = 'lightgreen.Horizontal.TProgressbar'
    elif strength == "Moderate":
        progress_bar['style'] = 'yellow.Horizontal.TProgressbar'
    elif strength == "Weak":
        progress_bar['style'] = 'orange.Horizontal.TProgressbar'
    else:
        progress_bar['style'] = 'red.Horizontal.TProgressbar'

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

# Create a title label
title_label = tk.Label(root, text="Password Strength Checker", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=20)

# Create a label for password entry
label = tk.Label(root, text="Enter your password:", font=("Helvetica", 12), bg="#f0f0f0")
label.pack(pady=10)

# Create a password entry field
password_entry = tk.Entry(root, show='*', width=30, font=("Helvetica", 12))
password_entry.pack(pady=10)

# Bind the key release event to the update_strength function
password_entry.bind("<KeyRelease>", update_strength)

# Create a label to display the strength
strength_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), width=20, height=2)
strength_label.pack(pady=20)

# Create a progress bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.pack(pady=20)

# Define styles for the progress bar
style = ttk.Style()
style.configure("TProgressbar", thickness=10)
style.configure("green.Horizontal.TProgressbar", bg="#4CAF50")
style.configure("lightgreen.Horizontal.TProgressbar", bg="#8BC34A")
style.configure("yellow.Horizontal.TProgressbar", bg="#FFC107")
style.configure("orange.Horizontal.TProgressbar", bg="#FF9800")
style.configure("red.Horizontal.TProgressbar", bg="#F44336")

# Run the application
root.mainloop()
