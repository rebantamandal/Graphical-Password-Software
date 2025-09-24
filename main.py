import tkinter as tk
import gui
import gui2

class MainLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("Graphical Password Authentication")

        tk.Label(root, text="Graphical Password Authentication System",
                 font=("Arial", 14, "bold")).pack(pady=20)

        tk.Button(root, text="Register", width=20, height=2,
                  command=self.open_register).pack(pady=10)

        tk.Button(root, text="Login", width=20, height=2,
                  command=self.open_login).pack(pady=10)

    def open_register(self):
        reg_window = tk.Toplevel(self.root)
        gui2.RegisterWindow(reg_window)

    def open_login(self):
        login_window = tk.Toplevel(self.root)
        gui.LoginWindow(login_window)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainLauncher(root)
    root.mainloop()
