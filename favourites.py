import json
import tkinter as tk
from tkinter import ttk


class Favourites:
    def __init__(self, favourites_frame):
        self.favourites = []
        self.favourites_vars = []
        self.favourites_frame = favourites_frame

    def create_check_buttons(self):
        try:
            with open("Constants.json") as f:
                data = json.load(f)
                favourites = data["Favourites"]
                for fav in favourites:
                    var = tk.BooleanVar()
                    check_button = ttk.Checkbutton(self.favourites_frame, text=fav["Name"], variable=var)
                    check_button.pack(fill="x", padx=10, pady=5)
                    self.favourites_vars.append(var)
                    self.favourites.append({"name": fav["Name"], "location": fav["Location"]})
        except Exception as e:
            print(f"An error occurred while creating the favourites check buttons: {e}")

    def get_selected(self):
        selected = [fav for fav, var in zip(self.favourites, self.favourites_vars) if var.get()]
        return selected
