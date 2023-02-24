import json
from tkinter import ttk


class FavouritesTreeview:
    def __init__(self):
        self.favourites = []
        self.treeview = None

    def create(self, master, scrollbar):
        try:
            # Add treeview
            self.treeview = ttk.Treeview(master, yscrollcommand=scrollbar.set)
            self.treeview.pack(fill="both", padx=10, pady=10, expand=True)
            scrollbar.config(command=self.treeview.yview)

            # Add columns
            self.treeview["columns"] = ("location")
            self.treeview.column("#0", width=200, minwidth=200, stretch="no")
            self.treeview.column("location", width=400, minwidth=400, stretch="no")
            self.treeview.heading("#0", text="Name", anchor="w")
            self.treeview.heading("location", text="Location/URL", anchor="w")

            # Load favourites from JSON
            with open("Constants.json") as f:
                data = json.load(f)
                favourites = data["Favourites"]

                for category in favourites:
                    category_node = self.treeview.insert("", "end", text=category["Name"], open=False)

                    for item in category["Items"]:
                        item_name = item["Name"]
                        item_location = item["Location"] if "Location" in item else item["Url"]
                        self.treeview.insert(category_node, "end", text=item_name, values=(item_location,))
                        self.favourites.append({"name": item_name, "location": item_location})

        except Exception as e:
            print(f"An error occurred while creating the favourites treeview: {e}")

    def get_location(self, item):
        for fav in self.favourites:
            if fav["name"] == self.treeview.item(item)["text"]:
                return fav["location"]
        return None

    def open_selected(self):
        try:
            # Get selected items
            items = self.treeview.selection()

            if not items:
                # Show error message if no item is selected
                messagebox.showerror("Error", "Please select at least one favourite to open.")
                return

            # Get locations of selected favourites
            locations = []
            for item in items:
                location = self.get_location(item)
                if location:
                    locations.append(location)

            # Open selected favourites
            for location in locations:
                subprocess.Popen(location)

        except Exception as e:
            logging.error(f"An error occurred while opening the selected favourites: {e}")
