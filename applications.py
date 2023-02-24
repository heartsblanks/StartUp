import tkinter as tk
from tkinter import ttk
import logging

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

            # Load applications from JSON
            self.treeview.load_applications()

            # Add "Open" button
            open_button = ttk.Button(app_window, text="Open", command=self.open_selected)
            open_button.pack(padx=10, pady=5, side="bottom")

        except Exception as e:
            logging.error(f"An error occurred while running the Applications class: {e}")

    def open_selected(self):
        try:
            # Get selected items
            items = self.treeview.treeview.selection()

            # Get locations of selected applications
            locations = []
            for item in items:
                location = self.treeview.get_location(item)
                if location:
                    locations.append(location)

            # Open selected applications
            for location in locations:
                self.open_application(location)

        except Exception as e:
            logging.error(f"An error occurred while opening the selected applications: {e}")

    def open_application(self, location):
        try:
            app_window = tk.Toplevel()
            app_window.title("Application")
            app_window.geometry("600x400")
            # Do something with the location
        except Exception as e:
            logging.error(f"An error occurred while opening the application: {e}")
