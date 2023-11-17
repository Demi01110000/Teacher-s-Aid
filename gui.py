import tkinter as tk
from tkinter import ttk
from visualization import plot_bar_chart

class MainApp:
    def __init__(self, data):
        self.root = tk.Tk()
        self.root.title("Student Performance Visualization")
        
        # GUI components and layout go here
        # For simplicity, you can start with a basic window and a button to trigger visualization

        self.btn_visualize = ttk.Button(self.root, text="Visualize Data", command=self.visualize_data)
        self.btn_visualize.pack()

        self.data = data

    def visualize_data(self):
        # Call functions from the visualization module
        plot_bar_chart(self.data)

    def run(self):
        self.root.mainloop()
