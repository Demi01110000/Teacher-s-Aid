import pandas as pd
import matplotlib.pyplot as plt

def plot_bar_chart(data):
    # Extract subject columns dynamically from the DataFrame so that we can add subjects 
    # into the csv file and it doesn't affect the visualization
    subject_columns = data.columns[3:]  # Assuming that columns from 3 onwards are subjects

    # Calculate the average grades for each student
    data['Average'] = round(data[subject_columns].mean(axis=1), 1)

    # Replace NaN values in 'Average' column with a default value (e.g., 0)
    data['Average'].fillna(0, inplace=True)

    # Determine color based on average grade by using cut to create segments
    data['Color'] = pd.cut(data['Average'], bins=[0, 1.5, 2.5, 3.5, 4.5, 5], labels=['green', 'yellowgreen', 'yellow', 'orange', 'red'])

    # Create a bar chart with colored bars
    plt.bar(data['Jmeno'] + ' ' + data['Přijmení'], data['Average'], color=data['Color'])

    # Add labels and title
    plt.xlabel('Students')
    plt.ylabel('Average Grades')
    plt.title('Average Grades for Students')

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')

    # Remove 'Color' column from the DataFrame before displaying
    data.drop(columns=['Color'], inplace=True)

    # Show the plot
    plt.show()
