import tkinter as tk
from tkinter import ttk
import json
import os

class Applications:
    def __init__(self):
        self.applications = []
        self.create_application_list()

    def run(self):
        try:
            # Create new window
            self.app_window = tk.Toplevel()
            self.app_window.title("Applications")
            self.app_window.geometry("600x400")

            # Add scrollbar
            scrollbar = ttk.Scrollbar(self.app_window)
            scrollbar.pack(side="right", fill="y")

            # Add treeview
            self.treeview = ttk.Treeview(self.app_window, yscrollcommand=scrollbar.set)
            self.treeview.pack(fill="both", padx=10, pady=10, expand=True)
            scrollbar.config(command=self.treeview.yview)

            # Add columns
            self.treeview["columns"] = ("location")
            self.treeview.column("#0", width=200, minwidth=200, stretch=tk.NO)
            self.treeview.column("location", width=400, minwidth=400, stretch=tk.NO)
            self.treeview.heading("#0", text="Name", anchor=tk.W)
            self.treeview.heading("location", text="Location", anchor=tk.W)

            # Add data to treeview
            self.add_data_to_treeview(self.applications, "")

            # Add "Open" button
            open_button = ttk.Button(self.app_window, text="Open", command=self.open_selected)
            open_button.pack(padx=10, pady=5, side="bottom")

        except Exception as e:
            print(f"An error occurred while running the Applications class: {e}")

    def create_application_list(self):
        try:
            with open("Constants.json") as f:
                data = json.load(f)
                applications = data["Applications"]
                self.build_application_list(applications)
        except Exception as e:
            print(f"An error occurred while creating the application list: {e}")

    def build_application_list(self, applications, parent=None):
        try:
            for app in applications:
                if "Children" in app:
                    name = app["Name"]
                    location = app["Location"]
                    children = app["Children"]
                    node = self.treeview.insert(parent, "end", text=name, open=False)
                    self.build_application_list(children, node)
                    self.applications.append({"name": name, "location": location, "parent": parent})
                else:
                    name = app["Name"]
                    location = app["Location"]
                    self.treeview.insert(parent, "end", text=name, values=(location,))
                    self.applications.append({"name": name, "location": location, "parent": parent})
        except Exception as e:
            print(f"An error occurred while building the application list: {e}")

    def add_data_to_treeview(self, data, parent):
        try:
            for item in data:
                name = item["name"]
                location = item["location"]
                node = self.treeview.insert(item["parent"], "end", text=name, values=(location,))
        except Exception as e:
            print(f"An error occurred while adding data to treeview: {e}")

    def open_selected(self):
        try:
            # Get selected items
            items = self.treeview.selection()

            # Get locations of selected applications
            locations = []
            for item in items:
                location = self.get_location(item)
                locations.append(location)

            # Open selected applications
            for location in locations:
                self.open_application(location)

        except Exception as e:
            print(f"An error occurred while opening the selected applications: {e}")

    def get_location(self, item):
        try:
            # Get location of item
            values = self.treeview.item(item)["values"]
            if values:
                return values[0]
            else:
                # Get location of parent
                parent = self.treeview.parent(item)
                return self.get_location(parent)
        except Exception as e:
            print(f"An error occurred while getting the location of the selected item: {e}")

    def open_application(self, location):
        try:
            self.app_window.withdraw() # Hide the applications window
            app_window = tk.Toplevel()
            app_window.title("Application")
            app_window.geometry("600x400")
            # Do something with the location
        except Exception as e:
            print(f"An error occurred while opening the application: {e}")
