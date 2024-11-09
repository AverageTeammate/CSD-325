# jacob Cannamela
# CSD 325
# 11/9/2024
# Module 4 assignment

import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

# adding in a menu to list the options - one of the changes 
def initial_menu():
    """Display the menu options to the user."""
    print("\nPlease select an option:")
    print("1. High Temperatures")
    print("2. Low Temperatures")
    print("3. Exit")

# adding in a function to read the file and create the list/dataframe - one of the changes
def read_weather_data(filename):
    """Read dates and temperatures from the CSV file."""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # initialize lists for dates, highs, and lows - one of the changes 
        dates, highs, lows = [], [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                # finding the highs 
                high = int(row[5])
                # finding the lows
                low = int(row[6])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

    return dates, highs, lows

# setting up the matplotlib graph 
def plot_temperatures(dates, temperatures, title, color):
    """Plot the temperatures using the specified color and title."""
    fig, ax = plt.subplots()
    ax.plot(dates, temperatures, c=color)

    # Format plot
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

# getting the file 
filename = 'C:\\Users\\Jacob\\OneDrive\\Documents\\School\\CSD325-A339 Advanced Python\\sitka_weather\\sitka_weather_2018_simple.csv'
dates, highs, lows = read_weather_data(filename)

while True:
    # get user input
    initial_menu()
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        # Plot high temperatures in red
        plot_temperatures(dates, highs, "Daily High Temperatures - 2018", 'red')
    elif choice == '2':
        # Plot low temperatures in blue
        plot_temperatures(dates, lows, "Daily Low Temperatures - 2018", 'blue')
    elif choice == '3':
        # Exit message
        print("Thank you for using the weather data viewer. Goodbye!")
        sys.exit()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
