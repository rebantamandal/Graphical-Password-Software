import tkinter as tk
from tkinter import messagebox
from image_mod import load_image
from insert import get_user, create_table

create_table()

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - Graphical Password Auth")

        tk.Label(root, text="Username:").pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        self.sequence = []
        self.assets = ["assets/img1.png", "assets/img2.png", "assets/img3.png"]

        tk.Label(root, text="Click images in your password sequence:").pack()
        self.frame = tk.Frame(root)
        self.frame.pack()

        for img_path in self.assets:
            img = load_image(img_path)
            btn = tk.Button(self.frame, image=img, command=lambda p=img_path: self.add_to_sequence(p))
            btn.image = img
            btn.pack(side="left", padx=5)

        self.login_btn = tk.Button(root, text="Login", command=self.login_user)
        self.login_btn.pack(pady=10)

    def add_to_sequence(self, img_path):
        self.sequence.append(img_path)

    def login_user(self):
        username = self.username_entry.get()
        stored_sequence = get_user(username)
        if not stored_sequence:
            messagebox.showerror("Error", "User not found!")
            return

        entered_sequence = ",".join(self.sequence)
        if entered_sequence == stored_sequence:
            messagebox.showinfo("Success", "Login successful!")
            dashboard = tk.Toplevel(self.root)
            tk.Label(dashboard, text=f"Welcome, {username}!", font=("Arial", 14)).pack(pady=20)
            tk.Button(dashboard, text="Logout", command=dashboard.destroy).pack(pady=10)
        else:
            messagebox.showerror("Error", "Invalid password sequence!")
