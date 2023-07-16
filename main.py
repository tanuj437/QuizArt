import tkinter as tk
from tkinter import ttk
import os

def run_virtual_painter():
    os.system("Virtual Painter\painter.py")

def run_quiz_master():
    os.system("QuizMaster\cam.py")

root = tk.Tk()
root.title("QuizArt")
root.geometry("300x200")
root.configure(bg="#F0F0F0")  # Set background color

# Create custom style for card-shaped buttons
style = ttk.Style()
style.configure("CardButton.TButton",
                
                background="#FF9933",
            
                relief="raised",
                borderwidth=2,
                width=20,
                height=100,
                padding=(10, 10, 10, 10),
                font=("Arial", 14))
style.map("CardButton.TButton",
          background=[('active', "#FF9933"), ('!active', "#FF9933")])

# Create Virtual Painter button
painter_button = ttk.Button(
    root,
    text="Virtual Painter",
    command=run_virtual_painter,
    style="CardButton.TButton"
)
painter_button.pack(pady=10)

# Create Quiz Master button
quiz_button = ttk.Button(
    root,
    text="Quiz Master",
    command=run_quiz_master,
    style="CardButton.TButton"
)
quiz_button.pack(pady=10)
text_label = tk.Label(root, text="Press 'Q' to quit")
text_label.pack(pady=10)

root.mainloop()
