import matplotlib.pyplot as plt

def plot_bar_chart(data):
    # Calculate the average grades for each student
    data['Average'] = data[['Maths', 'Czech']].mean(axis=1)

    # Create a bar chart
    plt.bar(data['Name'] + ' ' + data['Surname'], data['Average'], color='skyblue')

    # Add labels and title
    plt.xlabel('Studenti')
    plt.ylabel('Průměrné známky')
    plt.title('Pruměrné známky studentů')

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')

    # Show the plot
    plt.show()


