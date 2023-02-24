import tkinter as tk
from tkinter import ttk
import json

from applications import Applications


class ApplicationWindow:
    def __init__(self):
        self.favourites_data = None
        self.applications = Applications()

    def create(self, master):
        try:
            # Load favourites data from Constants.json
            with open("Constants.json") as f:
                data = json.load(f)
                self.favourites_data = data.get("Favourites", {})

            # Create a button for each category
            for category, items in self.favourites_data.items():
                button = ttk.Button(master, text=category, command=lambda items=items: self.applications.run_from_favourites(items))
                button.pack(fill="x", padx=10, pady=5)

        except Exception as e:
            print(f"An error occurred while creating the Applications button: {e}")
