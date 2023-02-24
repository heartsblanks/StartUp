import tkinter as tk
from tkinter import ttk
import logging
import subprocess

from application_treeview import ApplicationTreeview


class Applications:
    def __init__(self):
        self.treeview = None

    def run(self):
        try:
            # Create new window
            app_window = tk.Toplevel()
            app_window.title("Applications")
            app_window.geometry("600x400")

            # Add scrollbar
            scrollbar = ttk.Scrollbar(app_window)
            scrollbar.pack(side="right", fill="y")

            # Create Application Treeview
            self.treeview = ApplicationTreeview()
            self.treeview.create(app_window, scrollbar)

            # Add "Open" button
            open_button = ttk.Button(app_window, text="Open", command=self.open_selected)
            open_button.pack(padx=10, pady=5, side="bottom")

            # Add "Quit" button
            quit_button = ttk.Button(app_window, text="Quit", command=app_window.destroy)
            quit_button.pack(padx=10, pady=5, side="bottom")

        except Exception as e:
            logging.error(f"An error occurred while running the Applications class: {e}")

    def open_selected(self):
        try:
            # Get selected items
            items = self.treeview.treeview.selection()

            if not items:
                # Show error message if no item is selected
                tk.messagebox.showerror("Error", "Please select at least one application to open.")
                return

            # Get locations of selected applications
            locations = []
            for item in items:
                location = self.treeview.get_location(item)
                if location:
                    locations.append(location)

            # Open selected applications
            for location in locations:
                subprocess.Popen(location)

        except Exception as e:
            logging.error(f"An error occurred while opening the selected applications: {e}")

    def run_from_favourites(self, items):
        try:
            # Get locations of selected applications
            locations = []
            for item in items:
                location = item["Location"]
                if location:
                    locations.append(location)

            # Open selected applications
            for location in locations:
                subprocess.Popen(location)

        except Exception as e:
            logging.error(f"An error occurred while opening the selected applications: {e}")
