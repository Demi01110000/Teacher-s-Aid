import pandas as pd
import matplotlib.pyplot as plt

def plot_bar_chart(data):
    # Calculate the average grades for each student
    data['Average'] = data[['Maths', 'Czech']].mean(axis=1)

    # Create a bar chart
    plt.bar(data['Name'] + ' ' + data['Surname'], data['Average'], color='skyblue')

    # Add labels and title
    plt.xlabel('Students')
    plt.ylabel('Average Grades')
    plt.title('Average Grades for Students')

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')

    # Show the plot
    plt.show()
