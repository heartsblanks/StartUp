import tkinter as tk
from tkinter import ttk
import json
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
        favourites = Favourites(favourites_frame)

        # Create "Open" button
        open_button = ttk.Button(master, text="Open", command=favourites.open_favourites)
        open_button.pack(padx=10, pady=5, side="bottom")

        # Create quit button
        quit_button = ttk.Button(master, text="Quit", command=master.quit)
        quit_button.pack(side="bottom", padx=10, pady=10)

        self.favourites = favourites

    def create_button(self, name, cls):
        try:
            button = ttk.Button(self.master, text=name, command=cls().run)
            button.pack(fill="x", padx=10, pady=5)
        except Exception as e:
            print(f"An error occurred while creating the {name} button: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    InstallOrchestrationGUI(root)
    root.mainloop()

