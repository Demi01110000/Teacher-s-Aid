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
    plt.xlabel('Studenti')
    plt.ylabel('Průměrné známky')
    plt.title('Průměrné znamky studentů')

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')

    # Remove 'Color' column from the DataFrame before displaying
    data.drop(columns=['Color'], inplace=True)

    # Show the plot
    plt.show()

def class_overview(data):
    # Extract subject columns dynamically from the DataFrame
    subject_columns = data.columns[3:]  # Assuming that columns from 3 onwards are subjects

    # Calculate the average grades for each student
    data['Average'] = round(data[subject_columns].mean(axis=1), 0)  # Round to the nearest whole number

    # Replace NaN values in 'Average' column with a default value (e.g., 0)
    data['Average'].fillna(0, inplace=True)

    # Count the frequency of each whole grade (1 to 5)
    grade_counts = data['Average'].value_counts().sort_index()

    # Create a pie chart for the class grade distribution
    plt.pie(grade_counts, labels=grade_counts.index, autopct='%1.1f%%', startangle=90, colors=['green', 'pink', 'brown', 'orange', 'lightblue'])

    # Add title
    plt.title('Frekvence známek')

    # Show the plot
    plt.show()