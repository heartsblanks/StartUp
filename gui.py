import tkinter as tk
from tkinter import ttk
import logging

from check_json import JSONValidator
from applications import Applications
from websites import Websites
from add_items import AddItems
from delete_items import DeleteItems
from broker_functions import BrokerFunctions
from favourites import Favourites


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
        self.create_radio_button("Applications", Applications)
        self.create_radio_button("Websites", Websites)
        self.create_radio_button("Add new items", AddItems)
        self.create_radio_button("Delete items", DeleteItems)
        self.create_radio_button("Stop broker", BrokerFunctions)
        self.create_radio_button("Start broker", BrokerFunctions)

        # Create favourites frame
        favourites_frame = ttk.LabelFrame(master, text="Favourites")
        favourites_frame.pack(fill="both", padx=10, pady=10)

        # Create favourites buttons
        self.create_favourites_radio_buttons(favourites_frame)

        # Create quit button
        quit_button = ttk.Button(master, text="Quit", command=master.quit)
        quit_button.pack(side="bottom", padx=10, pady=10)

    def create_radio_button(self, name, cls):
        try:
            button = ttk.Radiobutton(self.master, text=name, command=cls().run)
            button.pack(fill="x", padx=10, pady=5)
        except Exception as e:
            logging.error(f"An error occurred while creating the {name} button: {e}")

    def create_favourites_radio_buttons(self, frame):
        try:
            with open("Constants.json") as json_file:
                data = json.load(json_file)
                for fav in data["Favourites"]:
                    button = ttk.Radiobutton(frame, text=fav["Name"], command=lambda fav=fav: Favourites().run(fav["Location"]))
                    button.pack(fill="x", padx=10, pady=5)
        except Exception as e:
            logging.error(f"An error occurred while creating the favourites buttons: {e}")
