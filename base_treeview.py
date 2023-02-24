import tkinter as tk
from tkinter import ttk


class BaseTreeview:
    def __init__(self, master, scrollbar, columns):
        self.favourites_frame = master
        self.favourites = []
        self.treeview = None
        self.scrollbar = None
        self.columns = columns
        self.create(scrollbar)

    def create(self, scrollbar):
        try:
            # Add scrollbar
            self.scrollbar = ttk.Scrollbar(self.favourites_frame)
            self.scrollbar.pack(side="right", fill="y")

            # Add treeview
            self.treeview = ttk.Treeview(self.favourites_frame, yscrollcommand=self.scrollbar.set)
            self.treeview.pack(fill="both", padx=10, pady=10, expand=True)
            self.scrollbar.config(command=self.treeview.yview)

            # Add columns
            self.treeview["columns"] = self.columns
            for column in self.columns:
                self.treeview.column(column, width=400, minwidth=400, stretch="no")
                self.treeview.heading(column, text=column, anchor="w")

        except Exception as e:
            logging.error(f"An error occurred while creating the treeview: {e}")
