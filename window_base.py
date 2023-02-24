import tkinter as tk
from tkinter import ttk


class WindowBase:
    def __init__(self, title):
        self.window = tk.Toplevel()
        self.window.title(title)

        self.create_widgets()

    def create_widgets(self):
        pass

    def run(self):
        self.window.mainloop()
