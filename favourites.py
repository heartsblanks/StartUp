import tkinter as tk
from tkinter import ttk
import json
import subprocess
from tkinter import messagebox


class Favourites:
    def __init__(self, favourites_frame):
        self.favourites_frame = favourites_frame
        self.favourites_vars = []
        self.favourites_treeview = None

    def create_check_buttons(self):
        try:
            with open("Constants.json") as f:
                data = json.load(f)
                favourites = data["Favourites"]
                for fav in favourites:
                    fav_label = fav["Name"]
                    category_frame = ttk.LabelFrame(self.favourites_frame, text=fav_label)
                    category_frame.pack(fill="both", padx=10, pady=5, expand=True)
                    for item in fav["Items"]:
                        var = tk.BooleanVar()
                        item_name = item["Name"]
                        check_button = ttk.Checkbutton(category_frame, text=item_name, variable=var)
                        check_button.pack(fill="x", padx=10, pady=5)
                        self.favourites_vars.append(var)
        except Exception as e:
            print(f"An error occurred while creating the favourites checkbuttons: {e}")

    def get_selected(self):
        selected = [i for i, v in enumerate(self.favourites_vars) if v.get()]
        return selected

    def open_favourites(self):
        try:
            # Get the selected favourites
            selected = self.get_selected()
            if not selected:
                messagebox.showinfo("Error", "Please select at least one favourite to open.")
                return

            # Create favourites window
            favourites_window = tk.Toplevel(self.favourites_frame.master)
            favourites_window.title("Favourites")
            favourites_window.geometry("600x400")

            # Add scrollbar
            scrollbar = ttk.Scrollbar(favourites_window)
            scrollbar.pack(side="right", fill="y")

            # Add favourites treeview
            self.favourites_treeview = FavouritesTreeview()
            self.favourites_treeview.create(favourites_window, scrollbar)

            # Add "Open" button
            open_button = ttk.Button(favourites_window, text="Open", command=self.favourites_treeview.open_selected)
            open_button.pack(padx=10, pady=5, side="bottom")

            # Add "Quit" button
            quit_button = ttk.Button(favourites_window, text="Quit", command=favourites_window.destroy)
            quit_button.pack(padx=10, pady=5, side="bottom")

        except Exception as e:
            print(f"An error occurred while opening the selected favourites: {e}")
