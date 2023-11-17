import tkinter as tk
from tkinter import ttk
from visualization import plot_bar_chart
from data_table import DataTableApp  # Import the DataTableApp class

class MainApp:
    def __init__(self, data):
        self.root = tk.Tk()
        self.root.title("Vizualizace výkonu studentů")
        self.root.geometry('500x250')
        # GUI components and layout go here
        # For simplicity, you can start with a basic window and a button to trigger visualization

        self.btn_visualize = ttk.Button(self.root, text="Visualize Data", command=self.visualize_data)
        self.btn_visualize.pack()

        self.btn_show_table = ttk.Button(self.root, text="Show Data Table", command=self.show_data_table)
        self.btn_show_table.pack()

        self.data = data

    def visualize_data(self):
        # Call functions from the visualization module
        plot_bar_chart(self.data)

    def show_data_table(self):
        # Create and run the DataTableApp
        table_app = DataTableApp(self.data)
        table_app.run()

    def run(self):
        self.root.mainloop()

