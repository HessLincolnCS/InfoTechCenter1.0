# Print decorative lines for better visual separation in output
print("\n*****************************\n")

# Indicate the start of the gasoline branch process
print("Gasoline Branch\n")

# Import the random module for generating random values
# Import the sleep function to simulate a pause in program execution
import random
from time import sleep

# Function to randomly determine the current gas level
def gasLevelGauge():
    # List of possible gas levels
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    # Return a random gas level from the list
    return random.choice(gasLevelList)

# Function to randomly select a nearby gas station
def gasStations():
    # List of available gas stations
    gasStationsList = ["VP", "Shell", "Meijer", "Sams Club",
                       "Marathon", "Mobile", "Speedway", "Circle K"]
    # Return a random gas station from the list
    return random.choice(gasStationsList)

# Function to alert the user based on the gas level and provide directions to the nearest station
def gasLevelAlert():
    # Generate a random distance (in miles) to the nearest station if gas is low
    milesToGasStationLow = round(random.uniform(1, 25), 1)  # Range: 1 to 25 miles
    milesToGasStationQuarterTank = round(random.uniform(25.1, 58), 1)  # Range: 25.1 to 58 miles

    # Get the current gas level using the gasLevelGauge function
    gasLevelIndicator = gasLevelGauge()

    # Check the gas level and print corresponding messages
    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***\n")
        sleep(2)  # Simulate a pause for dramatic effect
        print("Calling Triple AAA")  # Emergency assistance message

    elif gasLevelIndicator == "Low":
        print("Your gas tank is extremely low, checking GPS for the closest gas station")
        sleep(2)  # Simulate loading time
        # Display the closest gas station and the distance to it
        print("The closest gas station is", gasStations(),
              "which is", milesToGasStationLow, "miles away.")

    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is on a quarter of a tank, checking GPS for the closest gas station")
        sleep(2)  # Simulate loading time
        # Provide the nearest gas station and the distance to it
        print("The closest gas station is", gasStations(),
              "which is", milesToGasStationQuarterTank, "miles away.")

    elif gasLevelIndicator == "Half Tank":
        # Message for when the gas tank is half full
        print("Your gas tank is half full which is plenty to get to your destination.")

    elif gasLevelIndicator == "Three Quarter Tank":
        # Message for when the gas tank is three quarters full
        print("Your gas tank is three quarters full.")

    else:
        # Message for a full tank
        print("Your gas tank is full!!! Vroom Vroom")

# Call the gasLevelAlert function to execute the program logic
gasLevelAlert()
