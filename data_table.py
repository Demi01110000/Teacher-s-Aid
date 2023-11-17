import tkinter as tk
from tkinter import ttk
from data_handling import load_data

class DataTableApp:
    def __init__(self, data):
        self.root = tk.Tk()
        self.root.title("Data Table")

        self.data = data

        self.create_table()

    def create_table(self):
        # Create Treeview widget
        self.tree = ttk.Treeview(self.root)

        # Define columns
        self.tree["columns"] = tuple(self.data.columns)

        # Format columns
        for col in self.tree["columns"]:
            self.tree.column(col, anchor="center")
            self.tree.heading(col, text=col)

        # Insert data into the table
        for index, row in self.data.iterrows():
            self.tree.insert("", "end", values=tuple(row))

        # Pack the Treeview widget
        self.tree.pack(expand=True, fill=tk.BOTH)

    def run(self):
        self.root.mainloop()
