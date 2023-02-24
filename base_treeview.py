import json
import logging
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox


class BaseTreeView:
    def __init__(self, master, favourites_frame, data_file, treeview_columns, treeview_headings):
        self.favourites_frame = favourites_frame
        self.favourites = []
        self.treeview = None
        self.scrollbar = None
        self.data_file = data_file
        self.treeview_columns = treeview_columns
        self.treeview_headings = treeview_headings
        self.create(master)

    def create(self, master):
        try:
            # Add scrollbar
            self.scrollbar = ttk.Scrollbar(self.favourites_frame)
            self.scrollbar.pack(side="right", fill="y")

            # Add treeview
            self.treeview = ttk.Treeview(self.favourites_frame, yscrollcommand=self.scrollbar.set)
            self.treeview.pack(fill="both", padx=10, pady=10, expand=True)
            self.scrollbar.config(command=self.treeview.yview)

            # Add columns
            self.treeview["columns"] = self.treeview_columns
            for column in self.treeview_columns:
                self.treeview.column(column, width=400, minwidth=400, stretch="no")
            for heading in self.treeview_headings:
                self.treeview.heading(heading["column"], text=heading["text"], anchor=heading["anchor"])

            # Load favourites from JSON
            with open(self.data_file) as f:
                data = json.load(f)
                favourites = data["Favourites"]

                for category in favourites:
                    category_node = self.treeview.insert("", "end", text=category["Name"], open=False)

                    for item in category["Items"]:
                        item_name = item["Name"]
                        item_values = []
                        for column in self.treeview_columns:
                            if column == "#0":
                                item_values.append(item_name)
                            else:
                                if column in item:
                                    item_values.append(item[column])
                                else:
                                    item_values.append("")
                        self.treeview.insert(category_node, "end", values=item_values)
                        self.favourites.append({"name": item_name, "values": item_values})

        except Exception as e:
            logging.error(f"An error occurred while creating the treeview: {e}")

    def get_item_values(self, item):
        item_values = []
        for i, column in enumerate(self.treeview_columns):
            item_values.append(self.treeview.set(item, column))
        return item_values

    def get_selected_items(self):
        selected_items = []
        for item in self.treeview.selection():
            item_values = self.get_item_values(item)
            selected_items.append({"item": item, "values": item_values})
        return selected_items

    def open_selected_items(self):
        try:
            # Get selected items
            items = self.get_selected_items()

            if not items:
                # Show error message if no item is selected
                messagebox.showerror("Error", "Please select at least one item to open.")
                return

            # Get locations of selected items
            locations = []
            for item in items:
                location = item["values"][1]
                if location:
                    locations.append(location)

            # Open selected items
            for location in locations:
                subprocess.Popen(location)

        except Exception as e:
            logging.error(f"An error occurred while opening the selected items: {e}")
