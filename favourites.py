import json
import logging
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox
from favourites_treeview import FavouritesTreeview
from window_base import BaseWindow


class FavouritesWindow(BaseWindow):
    def __init__(self, master):
        super().__init__(master, "Favourites")

        # Add favourites treeview
        self.favourites_treeview = FavouritesTreeview(self.window_frame)
        self.favourites_treeview.treeview.pack(fill="both", padx=10, pady=10, expand=True)

        # Add "Open" button
        open_button = ttk.Button(self.window_frame, text="Open", command=self.favourites_treeview.open_selected)
        open_button.pack(padx=10, pady=5, side="bottom")

        # Add "Quit" button
        quit_button = ttk.Button(self.window_frame, text="Quit", command=self.close_window)
        quit_button.pack(padx=10, pady=5, side="bottom")


class Favourites:
    def __init__(self, favourites_frame):
        self.favourites_frame = favourites_frame

    def open_favourites(self):
        try:
            # Create favourites window
            favourites_window = FavouritesWindow(self.favourites_frame)

        except Exception as e:
            logging.error(f"An error occurred while opening the favourites window: {e}")
