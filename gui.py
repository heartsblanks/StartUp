import tkinter as tk
from tkinter import ttk
import json
from tkinter import messagebox
import logging
import subprocess

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
        logging.basicConfig(filename='install_orchestration.log', level=logging.ERROR)

        # Create buttons
        self.create_button("Applications", Applications)
        self.create_button("Websites", Websites)
        self.create_button("Add new items", AddItems)
        self.create_button("Delete items", DeleteItems)
        self.create_button("Stop broker", BrokerFunctions)
        self.create_button("Start broker", BrokerFunctions)

        # Create favourites frame
        favourites_frame = ttk.LabelFrame(master, text="Favourites")
        favourites_frame.pack(fill="both", padx=10, pady=10)

        # Create favourites checkbuttons
        self.create_favourites_check_buttons(favourites_frame)

        # Create "Open" button
        open_button = ttk.Button(master, text="Open", command=self.open_favourites)
        open_button.pack(padx=10, pady=5, side="bottom")

        # Create quit button
        quit_button = ttk.Button(master, text="Quit", command=master.quit)
        quit_button.pack(side="bottom", padx=10, pady=10)

    def create_button(self, name, cls):
        try:
            button = ttk.Button(self.master, text=name, command=cls().run)
            button.pack(fill="x", padx=10, pady=5)
        except Exception as e:
            print(f"An error occurred while creating the {name} button: {e}")

    def create_favourites_check_buttons(self, frame):
        try:
            with open("Constants.json") as f:
                data = json.load(f)
                favourites = data["Favourites"]
                self.favourites_vars = []
                for fav in favourites:
                    var = tk.BooleanVar()
                    check_button = ttk.Checkbutton(frame, text=fav["Name"], variable=var)
                    check_button.pack(fill="x", padx=10, pady=5)
                    self.favourites_vars.append(var)
        except Exception as e:
            print(f"An error occurred while creating the favourites buttons: {e}")

    def open_favourites(self):
        try:
            # Get the selected favourites
            selected = [i for i, v in enumerate(self.favourites_vars) if v.get()]
            if not selected:
                messagebox.showinfo("Error", "Please select at least one favourite to open.")
                return

            with open("Constants.json") as f:
                data = json.load(f)
                favourites = data["Favourites"]
                selected_favourites = [favourites[i] for i in selected]
                for fav in selected_favourites:
                    location = fav["Location"]
                    subprocess.Popen(location)

        except Exception as e:
            print(f"An error occurred while opening the selected favourites: {e}")
