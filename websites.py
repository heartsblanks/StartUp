import json
import tkinter as tk
from tkinter import ttk
from window_base import WindowBase
from treeview_base import TreeviewBase
from add_items import AddItems


class Websites:
    def __init__(self, parent):
        self.parent = parent
        self.websites_treeview = WebsitesTreeview(self.parent)
        self.add_website_button = ttk.Button(self.parent, text="Add Website", command=self.add_website)
        self.add_website_button.pack(pady=10)

    def add_website(self):
        add_items = AddItems()
        add_items.run()
        name = add_items.name_entry.get()
        location = add_items.location_entry.get()
        if name and location:
            item = {"Name": name, "Url": location}
            self.websites_treeview.add_item(item)


class WebsitesTreeview(TreeviewBase):
    def __init__(self, master):
        super().__init__(master)

    def create_treeview(self):
        # Add columns
        self.treeview["columns"] = ("url",)
        self.treeview.column("#0", width=200, minwidth=200, stretch="no")
        self.treeview.column("url", width=400, minwidth=400, stretch="no")
        self.treeview.heading("#0", text="Name", anchor="w")
        self.treeview.heading("url", text="URL", anchor="w")

        # Load items from JSON
        try:
            with open("Constants.json") as f:
                data = json.load(f)
                websites = data["Websites"]

                for website in websites:
                    name = website["Name"]
                    url = website["Url"]
                    item = {"Name": name, "Url": url}
                    self.add_item(item)
        except Exception as e:
            print(f"An error occurred while loading the websites: {e}")

    def get_item_location(self, item):
        return self.treeview.item(item, "values")[0]


class WebsitesWindow(WindowBase):
    def __init__(self, master):
        super().__init__(master, "Websites")

        self.websites_treeview = WebsitesTreeview(self.window)
        self.create_window()

    def create_window(self):
        self.add_scrollbar(self.websites_treeview.treeview)
        self.add_buttons(self.websites_treeview.treeview)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Websites")
    root.geometry("600x400")

    websites = Websites(root)

    root.mainloop()
