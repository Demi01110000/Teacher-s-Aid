from gui import MainApp
from data_handling import load_data
import os
# from visualization import plot_bar_chart

# Load data from CSV file using Pandas
# data = load_data('teachersAid/tridni_kniha.csv')  # Use / instead of \ for path
# instead of the relative path I am using the absolute path because it stopped working

# Get the absolute path to the directory containing the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the CSV file
file_path = os.path.join(script_dir, 'tridni_kniha.csv')

# Load data using the absolute path
data = load_data(file_path)


# Create the GUI and pass the data
app = MainApp(data)

# Start the main loop
app.run()
