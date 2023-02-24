import tkinter as tk
from tkinter import ttk
from applications import Applications


class ApplicationWindow:
    def __init__(self):
        self.applications = Applications()

    def create(self, master):
        try:
            button = ttk.Button(master, text="Applications", command=self.applications.run)
            button.pack(fill="x", padx=10, pady=5)
        except Exception as e:
            print(f"An error occurred while creating the Applications button: {e}")
