import json
from tkinter import ttk


class ApplicationTreeview:
    def __init__(self):
        self.applications = []
        self.treeview = None

    def create(self, master, scrollbar):
        try:
            # Add treeview
            self.treeview = ttk.Treeview(master, yscrollcommand=scrollbar.set, show="tree")
            self.treeview.pack(fill="both", padx=10, pady=10, expand=True)
            scrollbar.config(command=self.treeview.yview)

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
                    children = app["Children"]
                    node = self.treeview.insert(parent, "end", text=name, open=False)
                    self.build_application_list(children, node)
                    self.applications.append(name)
                else:
                    name = app["Name"]
                    self.treeview.insert(parent, "end", text=name)
                    self.applications.append(name)

        except Exception as e:
            print(f"An error occurred while building the application list: {e}")
