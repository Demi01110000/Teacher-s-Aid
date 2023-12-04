import tkinter as tk
from tkinter import ttk
from visualization import plot_bar_chart, class_overview
from data_table import DataTableApp  # Import the DataTableApp class

class MainApp:
    def __init__(self, data):
        self.root = tk.Tk()
        self.root.title("Vizualizace výkonu studentů")
        self.root.geometry('600x300')  # Adjusted window size

        # Use a style to customize the appearance of widgets
        self.style = ttk.Style()

        # Change the color palette
        self.style.theme_use('clam')  # Choose a different theme (e.g., 'clam', 'alt', 'default')

        # Set the color of buttons
        self.style.configure('TButton', font=('Arial', 12), foreground='black', background='#66c2ff')  # Change button color

        # Add a title label
        title_label = ttk.Label(self.root, text="Třídní Výkazy", font=('Arial', 16, 'bold'))
        title_label.pack(pady=10)  # Add padding to separate the title from buttons

        # GUI components and layout go here
        # For simplicity, you can start with a basic window and a button to trigger visualization

        # Visualize Data Button
        self.btn_visualize = ttk.Button(self.root, text="Vizualizace známek žáků", command=self.visualize_data)
        self.btn_visualize.pack(pady=10)

        # Show Data Table Button
        self.btn_show_table = ttk.Button(self.root, text="Přehled třídy", command=self.show_data_table)
        self.btn_show_table.pack(pady=10)

        # New button for Class Overview
        self.btn_class_overview = ttk.Button(self.root, text="Známky třídy", command=self.show_class_overview)
        self.btn_class_overview.pack(pady=10)

        self.data = data

    def visualize_data(self):
        # Call functions from the visualization module
        plot_bar_chart(self.data)

    def show_data_table(self):
        # Create and run the DataTableApp
        table_app = DataTableApp(self.data)
        table_app.run()

    def show_class_overview(self):
        # Call the new function to visualize class overview
        class_overview(self.data)

    def run(self):
        self.root.mainloop()

