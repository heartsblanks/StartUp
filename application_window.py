import json
import logging
import subprocess
import tkinter as tk
from tkinter import ttk

from window_base import WindowBase


class ApplicationsWindow(WindowBase):
    def __init__(self):
        super().__init__("Applications")

    def create_form(self):
        super().create_form()

        location_label = ttk.Label(self.form_frame, text="Location:")
        self.location_entry = ttk.Entry(self.form_frame)
        location_label.grid(row=2, column=0, sticky="W")
        self.location_entry.grid(row=2, column=1, sticky="W")

    def create_buttons(self):
        super().create_buttons()

        self.add_items_button = ttk.Button(self.button_frame, text="Add Items", command=self.add_items)
        self.add_items_button.pack(side="left", padx=5)

    def add_items(self):
        from add_items import AddItems

        add_items_window = AddItems()
        add_items_window.category_name = "Applications"
        add_items_window.run()

    def load_items(self):
        try:
            with open("Constants.json") as f:
                data = json.load(f)
                applications = data["Applications"]

                for application in applications:
                    name = application["Name"]
                    location = application["Location"]
                    self.treeview.insert("", "end", text=name, values=(location,))

        except Exception as e:
            logging.error(f"An error occurred while loading the applications: {e}")

    def open_selected(self):
        try:
            # Get selected item
            item = self.treeview.selection()[0]
            name = self.treeview.item(item, "text")
            location = self.treeview.item(item, "values")[0]

            # Open selected application
            subprocess.Popen(location)

        except Exception as e:
            logging.error(f"An error occurred while opening the selected application: {e}")
