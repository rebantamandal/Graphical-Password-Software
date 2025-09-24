import tkinter as tk
from tkinter import messagebox
from image_mod import load_image
from insert import insert_user, create_table

create_table()

class RegisterWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Register - Graphical Password Auth")

        tk.Label(root, text="Username:").pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        self.sequence = []
        self.assets = ["assets/img1.png", "assets/img2.png", "assets/img3.png"]

        tk.Label(root, text="Click images to set your password sequence:").pack()
        self.frame = tk.Frame(root)
        self.frame.pack()

        for img_path in self.assets:
            img = load_image(img_path)
            btn = tk.Button(self.frame, image=img, command=lambda p=img_path: self.add_to_sequence(p))
            btn.image = img
            btn.pack(side="left", padx=5)

        self.register_btn = tk.Button(root, text="Register", command=self.register_user)
        self.register_btn.pack(pady=10)

    def add_to_sequence(self, img_path):
        self.sequence.append(img_path)

    def register_user(self):
        username = self.username_entry.get()
        if not username or not self.sequence:
            messagebox.showerror("Error", "Please enter username and select password sequence.")
            return
        sequence_str = ",".join(self.sequence)
        if insert_user(username, sequence_str):
            messagebox.showinfo("Success", "User registered successfully!")
            self.root.destroy()
        else:
            messagebox.showerror("Error", "Username already exists!")
