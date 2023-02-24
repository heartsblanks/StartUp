import tkinter as tk
from tkinter import ttk
import webbrowser
import json

from check_json import JSONValidator


class Applications:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Applications")

        # Read the JSON file
        with open("Constants.json", "r") as f:
            data = json.load(f)

        # Get a list of all the applications
        self.applications = []
        for app in data["Applications"]:
            self.applications.append(app)
            if "Children" in app:
                for child in app["Children"]:
                    self.applications.append(child)

        # Create the checkboxes
        self.checkbox_vars = []
        self.checkboxes = []
        for app in self.applications:
            var = tk.BooleanVar()
            self.checkbox_vars.append(var)
            checkbox = ttk.Checkbutton(self.window, text=app["Name"], variable=var, command=self.update_child_checkboxes)
            checkbox.pack()

            if "Children" in app:
                # Indent the child checkboxes
                checkbox.configure(style="Indent1.TCheckbutton")

                # Create the child checkboxes
                for child in app["Children"]:
                    child_var = tk.BooleanVar()
                    self.checkbox_vars.append(child_var)
                    child_checkbox = ttk.Checkbutton(self.window, text=child["Name"], variable=child_var, command=self.update_parent_checkbox)
                    child_checkbox.pack()

                    # Indent the child checkboxes
                    child_checkbox.configure(style="Indent2.TCheckbutton")

        # Create the "Open" button
        open_button = ttk.Button(self.window, text="Open", command=self.open_selected)
        open_button.pack(pady=10)

    def update_child_checkboxes(self):
        """
        Updates the state of child checkboxes based on their parent checkbox state.
        """
        for app in self.applications:
            if "Children" in app:
                parent_checkbox_var = self.checkbox_vars[self.applications.index(app)]
                for child in app["Children"]:
                    child_checkbox_var = self.checkbox_vars[self.applications.index(child)]
                    child_checkbox_var.set(parent_checkbox_var.get())

    def update_parent_checkbox(self):
        """
        Updates the state of the parent checkbox based on the state of its child checkboxes.
        """
        for app in self.applications:
            if "Children" in app:
                parent_checkbox_var = self.checkbox_vars[self.applications.index(app)]
                child_checkboxes_vars = [self.checkbox_vars[self.applications.index(child)] for child in app["Children"]]
                if all(var.get() for var in child_checkboxes_vars):
                    parent_checkbox_var.set(True)
                elif any(var.get() for var in child_checkboxes_vars):
                    parent_checkbox_var.set(True)
                else:
                    parent_checkbox_var.set(False)

    def open_selected(self):
        """
        Opens the applications that the user has selected.
        """
        for app, var in zip(self.applications, self.checkbox_vars):
            if var.get():
                if "Children" in app:
                    for child in app["Children"]:
                        if child["Location"]:
                            webbrowser.open(child["Location"])
                elif app["Location"]:
                    webbrowser.open(app["Location"])

    def run(self):
        self.window.mainloop()
