import tkinter as tk
from tkinter import ttk
import json
from tkinter import messagebox

from check_json import JSONValidator
from applications import Applications
from websites import Websites
from add_items import AddItems
from delete_items import DeleteItems
from broker_functions import BrokerFunctions
from favourites import Favourites
from favourites_treeview import FavouritesTreeview


class InstallOrchestrationGUI:
    def __init__(self, master):
        self.master = master
        master.title("Install Orchestration")

        # Create JSON validator
        validator = JSONValidator("Constants.json")
        validator.validate()

        # Set up logging
        # logging.basicConfig(filename='install_orchestration.log', level=logging.ERROR)

        # Create buttons
        self.create_button("Applications", Applications)
        self.create_button("Websites", Websites)
        self.create_button("Add new items", AddItems)
        self.create_button("Delete items", DeleteItems)
        self.create_button("Stop broker", BrokerFunctions)
        self.create_button("Start broker", BrokerFunctions)

        # Create favourites button
        favourites_button = ttk.Button(master, text="Favourites", command=self.show_favourites)
        favourites_button.pack(fill="x", padx=10, pady=5)

        # Create quit button
        quit_button = ttk.Button(master, text="Quit", command=master.quit)
        quit_button.pack(side="bottom", padx=10, pady=10)

    def create_button(self, name, cls):
        try:
            button = ttk.Button(self.master, text=name, command=cls().run)
            button.pack(fill="x", padx=10, pady=5)
        except Exception as e:
            print(f"An error occurred while creating the {name} button: {e}")

    def show_favourites(self):
        try:
            # Create new window
            fav_window = tk.Toplevel()
            fav_window.title("Favourites")
            fav_window.geometry("600x400")

            # Add scrollbar
            scrollbar = ttk.Scrollbar(fav_window)
            scrollbar.pack(side="right", fill="y")

            # Create Favourites Treeview
            self.treeview = FavouritesTreeview()
            self.treeview.create(fav_window, scrollbar)

            # Add "Open" button
            open_button = ttk.Button(fav_window, text="Open", command=self.open_selected_favourites)
            open_button.pack(padx=10, pady=5, side="bottom")

            # Add "Quit" button
            quit_button = ttk.Button(fav_window, text="Quit", command=fav_window.destroy)
            quit_button.pack(padx=10, pady=5, side="bottom")

        except Exception as e:
            print(f"An error occurred while creating the Favourites window: {e}")

    def open_selected_favourites(self):
        try:
            # Get selected items
            items = self.treeview.treeview.selection()

            if not items:
                # Show error message if no item is selected
                tk.messagebox.showerror("Error", "Please select at least one favourite to open.")
                return

            # Get locations of selected applications
            locations = []
            for item in items:
                location = self.treeview.get_location(item)
                if location:
                    locations.append(location)

            # Open selected applications
            for location in locations:
                subprocess.Popen(location)

        except Exception as e:
            logging.error(f"An error occurred while opening the selected favourites: {e}")


