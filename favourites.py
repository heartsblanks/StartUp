import logging
from tkinter import ttk
from favourites_treeview import FavouritesTreeview


class Favourites:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def run(self):
        self.logger.info("Favourites selected.")

        # Create favourites window
        favourites_window = tk.Toplevel(self.master)
        favourites_window.title("Favourites")
        favourites_window.geometry("600x400")

        # Add scrollbar
        scrollbar = ttk.Scrollbar(favourites_window)
        scrollbar.pack()
        # Add favourites treeview
        favourites_treeview = FavouritesTreeview()
        favourites_treeview.create(favourites_window, scrollbar)

        # Add "Open" button
        open_button = ttk.Button(favourites_window, text="Open", command=favourites_treeview.open_selected)
        open_button.pack(padx=10, pady=5, side="bottom")

        # Add "Quit" button
        quit_button = ttk.Button(favourites_window, text="Quit", command=favourites_window.destroy)
        quit_button.pack(padx=10, pady=5, side="bottom")
