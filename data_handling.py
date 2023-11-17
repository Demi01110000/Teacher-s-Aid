import pandas as pd

def load_data(file_path):
    # Read data from CSV file into a Pandas DataFrame
    return pd.read_csv(file_path, sep=';')

