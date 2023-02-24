import json
import tkinter as tk
from tkinter import ttk


class AddItems:
    def __init__(self, category_name):
        self.category_name = category_name
        self.window = tk.Toplevel()
        self.window.title("Add new item")

        self.create_form()
        self.create_buttons()

    def create_form(self):
        form_frame = ttk.Frame(self.window, padding=20)
        form_frame.pack()

        name_label = ttk.Label(form_frame, text="Name:")
        self.name_entry = ttk.Entry(form_frame)
        location_label = ttk.Label(form_frame, text="Location/URL:")
        self.location_entry = ttk.Entry(form_frame)

        name_label.grid(row=0, column=0, sticky="W")
        self.name_entry.grid(row=0, column=1, sticky="W")
        location_label.grid(row=1, column=0, sticky="W")
        self.location_entry.grid(row=1, column=1, sticky="W")

    def create_buttons(self):
        button_frame = ttk.Frame(self.window, padding=20)
        button_frame.pack()

        submit_button = ttk.Button(button_frame, text="Submit", command=self.submit)
        submit_button.pack(side="left", padx=5)

        quit_button = ttk.Button(button_frame, text="Quit", command=self.window.destroy)
        quit_button.pack(side="left", padx=5)

    def submit(self):
        name = self.name_entry.get()
        location = self.location_entry.get()
        item = {"Name": name, "Location": location}

        # Save item to JSON file
        with open("Constants.json", "r+") as f:
            data = json.load(f)
            data[self.category_name].append(item)
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()

        self.window.destroy()

    def run(self):
        self.window.mainloop()
