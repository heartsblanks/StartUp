import json
import logging
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox

from application_treeview import ApplicationTreeview
from application_window import ApplicationsWindow
from window_base import WindowBase
from add_items import AddItems


class Applications(WindowBase):
    def __init__(self, parent):
        super().__init__(parent)
        self.treeview = ApplicationTreeview(self.main_frame)
        self.treeview.pack(fill="both", expand=True)

        self.create_menu()
        self.create_toolbar()

    def create_menu(self):
        menu_bar = tk.Menu(self.parent)
        self.parent.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=False)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Quit", command=self.parent.quit)

        edit_menu = tk.Menu(menu_bar, tearoff=False)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Add Application", command=self.add_application)

    def create_toolbar(self):
        toolbar = ttk.Frame(self.parent, padding=5)
        toolbar.pack(side="top", fill="x")

        add_button = ttk.Button(toolbar, text="Add", command=self.add_application)
        add_button.pack(side="left")

        delete_button = ttk.Button(toolbar, text="Delete", command=self.delete_selected)
        delete_button.pack(side="left", padx=5)

        launch_button = ttk.Button(toolbar, text="Launch", command=self.launch_selected)
        launch_button.pack(side="left")

    def add_application(self):
        AddItems(self.treeview, "Applications")

    def delete_selected(self):
        self.treeview.delete_selected()

    def launch_selected(self):
        selected = self.treeview.selection()

        if not selected:
            messagebox.showinfo("Error", "Please select at least one application to launch.")
            return

        for item in selected:
            location = self.treeview.get_location(item)
            if location:
                try:
                    subprocess.Popen(location)
                except Exception as e:
                    logging.error(f"An error occurred while opening the selected application: {e}")
            else:
                logging.error(f"Location not found for selected application: {item}")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Applications")
    root.geometry("800x600")

    app = Applications(root)

    root.mainloop()
