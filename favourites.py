import json
import tkinter as tk
from tkinter import ttk


class Favourites:
    def __init__(self, frame):
        self.frame = frame
        self.favourites_vars = []
        self.load_favourites()

    def create_check_buttons(self):
        try:
            for fav in self.favourites:
                var = tk.BooleanVar()
                check_button = ttk.Checkbutton(self.frame, text=fav["Name"], variable=var)
                check_button.pack(fill="x", padx=10, pady=5)
                self.favourites_vars.append(var)
        except Exception as e:
            print(f"An error occurred while creating the favourites buttons: {e}")

    def load_favourites(self):
        try:
            with open("Constants.json") as f:
                data = json.load(f)
                self.favourites = data["Favourites"]
        except Exception as e:
            print(f"An error occurred while loading the favourites: {e}")

    def get_selected(self):
        return [i for i, v in enumerate(self.favourites_vars) if v.get()]
