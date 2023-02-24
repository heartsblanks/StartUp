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
        open_button = ttk.Button(favourites_frame, text="Open", command=favourites.open_favourites)
        open_button.pack(padx=10, pady=5, side="bottom")

        self.favourites = favourites

        # Set focus to the first button
        self.master.bind("<Return>", self.focus_next_widget)
        self.master.bind("<KP_Enter>", self.focus_next_widget)
        self.master.bind("<Down>", self.focus_next_widget)

    def create_button(self, name, cls):
        try:
            button = ttk.Button(self.master, text=name, command=cls().run)
            button.pack(fill="x", padx=10, pady=5)
        except Exception as e:
            print(f"An error occurred while creating the {name} button: {e}")

    def focus_next_widget(self, event):
        event.widget.tk_focusNext().focus()


def main():
    root = tk.Tk()
    app = InstallOrchestrationGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
