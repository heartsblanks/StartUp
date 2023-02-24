import json
from tkinter import ttk
import tkinter as tk

class ApplicationTreeview:
    def __init__(self):
        self.applications = []
        self.treeview = None

    def create(self, master, scrollbar):
        try:
            # Add treeview
            self.treeview = ttk.Treeview(master, yscrollcommand=scrollbar.set)
            self.treeview.pack(fill="both", padx=10, pady=10, expand=True)
            scrollbar.config(command=self.treeview.yview)

            # Add columns
            self.treeview["columns"] = ("location")
            self.treeview.column("#0", width=200, minwidth=200, stretch=tk.NO)
            self.treeview.column("location", width=400, minwidth=400, stretch=tk.NO)
            self.treeview.heading("#0", text="Name", anchor=tk.W)
            self.treeview.heading("location", text="Location", anchor=tk.W)

            # Load applications from JSON
            with open("Constants.json") as f:
                data = json.load(f)
                applications = data["Applications"]
                self.build_application_list(applications, "")

        except Exception as e:
            print(f"An error occurred while creating the application treeview: {e}")

    def build_application_list(self, applications, parent):
        try:
            for app in applications:
                if "Children" in app:
                    name = app["Name"]
                    location = app["Location"]
                    children = app["Children"]
                    node = self.treeview.insert(parent, "end", text=name, open=False)
                    self.build_application_list(children, node)
                    self.applications.append({"name": name, "location": location, "node": node})
                else:
                    name = app["Name"]
                    location = app["Location"]
                    node = self.treeview.insert(parent, "end", text=name, values=(location,))
                    self.applications.append({"name": name, "location": location, "node": node})
                    check_button = ttk.Checkbutton(self.treeview, variable=tk.BooleanVar(value=False))
                    self.treeview.window_create(node, 2, window=check_button)

        except Exception as e:
            print(f"An error occurred while building the application list: {e}")

    def get_selected(self):
        items = self.treeview.selection()
        if not items:
            return None
        locations = []
        for item in items:
            location = self.get_location(item)
            locations.append(location)
        return locations

    def get_location(self, item):
        return self.treeview.set(item, "location")
