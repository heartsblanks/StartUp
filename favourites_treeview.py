import json
import logging
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox

from treeview_base import TreeviewBase


class FavouritesTreeview(TreeviewBase):
    def __init__(self, master, favourites_frame):
        super().__init__(master, favourites_frame, columns=("location",))
        self.favourites = []
        self.create()

    def create(self):
        try:
            # Add columns
            self.column("#0", width=200, minwidth=200, stretch="no")
            self.column("location", width=400, minwidth=400, stretch="no")
            self.heading("#0", text="Name", anchor="w")
            self.heading("location", text="Location/URL", anchor="w")

            # Load favourites from JSON
            with open("Constants.json") as f:
                data = json.load(f)
                favourites = data["Favourites"]

                for category in favourites:
                    category_node = self.insert("", "end", text=category["Name"], open=False)

                    for item in category["Items"]:
                        item_name = item["Name"]
                        item_location = item.get("Location", item.get("Url", ""))
                        self.insert(category_node, "end", text=item_name, values=(item_location,))
                        self.favourites.append({"name": item_name, "location": item_location})

        except Exception as e:
            logging.error(f"An error occurred while creating the favourites treeview: {e}")

    def get_location(self, item):
        for fav in self.favourites:
            if fav["name"] == self.item(item)["text"]:
                return fav["location"]
        return None

    def open_selected(self):
        try:
            # Get selected items
            items = self.selection()

            if not items:
                # Show error message if no item is selected
                messagebox.showerror("Error", "Please select at least one favourite to open.")
                return

            # Get locations of selected favourites
            locations = []
            for item in items:
                location = self.get_location(item)
                if location:
                    locations.append(location)

            # Open selected favourites
            for location in locations:
                subprocess.Popen(location)

        except Exception as e:
            logging.error(f"An error occurred while opening the selected favourites: {e}")
