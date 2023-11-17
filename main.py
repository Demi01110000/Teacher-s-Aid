from gui import MainApp
from data_handling import load_data
from visualization import plot_bar_chart

# Load data from CSV file using Pandas
data = load_data('teachersAid/A_7.csv')  # Use / instead of \ for path

# Create the GUI and pass the data
app = MainApp(data)

# Start the main loop
app.run()
