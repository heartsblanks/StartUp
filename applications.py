import tkinter as tk
from tkinter import ttk
from application_treeview import ApplicationTreeview


class Applications:
    def __init__(self):
        self.applications = []
        self.app_treeview = ApplicationTreeview()

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
            self.treeview = self.app_treeview.create(self.app_window, scrollbar)

            # Add "Open" button
            open_button = ttk.Button(self.app_window, text="Open", command=self.open_selected)
            open_button.pack(padx=10, pady=5, side="bottom")
        except Exception as e:
            print(f"An error occurred while running the Applications class: {e}")

    def open_selected(self):
        try:
            # Get selected items
            items = self.treeview.selection()

            # Get locations of selected applications
            locations = []
            for item in items:
                location = self.app_treeview.get_location(item)
                locations.append(location)

            # Open selected applications
            for location in locations:
                # Do something with the location
                print(location)
        except Exception as e:
            print(f"An error occurred while opening the application: {e}")
