import json
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox

class Websites:
    def __init__(self):
        self.websites = []

    def run(self):
        try:
            # Create window
            website_window = tk.Toplevel()
            website_window.title("Websites")
            website_window.geometry("400x400")

            # Add treeview
            treeview = ttk.Treeview(website_window)
            treeview.pack(fill="both", padx=10, pady=10, expand=True)

            # Add columns
            treeview["columns"] = ("url")
            treeview.column("#0", width=200, minwidth=200, stretch="no")
            treeview.column("url", width=400, minwidth=400, stretch="no")
            treeview.heading("#0", text="Name", anchor="w")
            treeview.heading("url", text="URL", anchor="w")

            # Load websites from JSON
            with open("Constants.json") as f:
                data = json.load(f)
                websites = data["Websites"]

                for website in websites:
                    name = website["Name"]
                    url = website["Url"]
                    treeview.insert("", "end", text=name, values=(url,))
                    self.websites.append({"name": name, "url": url})

            # Add "Open" button
            open_button = ttk.Button(website_window, text="Open", command=self.open_selected)
            open_button.pack(padx=10, pady=5, side="bottom")

            # Add "Quit" button
            quit_button = ttk.Button(website_window, text="Quit", command=website_window.destroy)
            quit_button.pack(padx=10, pady=5, side="bottom")

        except Exception as e:
            print(f"An error occurred while creating the websites window: {e}")

    def get_url(self, item):
        for website in self.websites:
            if website["name"] == item["text"]:
                return website["url"]
        return None

    def open_selected(self):
        try:
            # Get selected items
            items = treeview.selection()

            if not items:
                # Show error message if no item is selected
                messagebox.showerror("Error", "Please select at least one website to open.")
                return

            # Get URLs of selected websites
            urls = []
            for item in items:
                url = self.get_url(treeview.item(item))
                if url:
                    urls.append(url)

            # Open selected websites
            for url in urls:
                subprocess.Popen(url)

        except Exception as e:
            print(f"An error occurred while opening the selected websites: {e}")
