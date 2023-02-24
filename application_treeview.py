import json
import logging
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox

from treeview_base import TreeviewBase


class ApplicationTreeview(TreeviewBase):
    def __init__(self, master):
        super().__init__(master)

        # Add columns
        self.treeview["columns"] = ("location",)
        self.treeview.column("#0", width=200, minwidth=200, stretch="no")
        self.treeview.column("location", width=400, minwidth=400, stretch="no")
        self.treeview.heading("#0", text="Name", anchor="w")
        self.treeview.heading("location", text="Location", anchor="w")

        # Load applications from JSON
        try:
            with open("Constants.json") as f:
                data = json.load(f)
                applications = data["Applications"]

                for app in applications:
                    name = app["Name"]
                    location = app["Location"]
                    self.treeview.insert("", "end", text=name, values=(location,))
                    self.items.append({"name": name, "location": location})

        except Exception as e:
            logging.error(f"An error occurred while creating the application treeview: {e}")

    def open_selected(self):
        try:
            # Get selected items
            items = self.treeview.selection()

            if not items:
                # Show error message if no item is selected
                messagebox.showerror("Error", "Please select at least one application to open.")
                return

            # Open selected applications
            for item in items:
                location = self.get_location(item)
                if location:
                    subprocess.Popen(location)

        except Exception as e:
            logging.error(f"An error occurred while opening the selected applications: {e}")    
