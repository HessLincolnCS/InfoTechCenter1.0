import random
from time import sleep

# Print decorative lines and program title
print("\n*****************************\n")
print("Gasoline Branch\n")

# Function to randomly determine the current gas level
def gasLevelGauge():
    return random.choice([
        "Empty", "Low", "Quarter Tank", "Half Tank",
        "Three Quarter Tank", "Full Tank"
    ])

# Function to randomly select a nearby gas station
def gasStations():
    return random.choice([
        "VP", "Shell", "Meijer", "Sams Club",
        "Marathon", "Mobile", "Speedway", "Circle K"
    ])

# Function to generate a message for the nearest gas station
def nearestGasStationMessage(miles_range):
    station = gasStations()
    miles = round(random.uniform(*miles_range), 1)
    return f"The closest gas station is {station}, which is {miles} miles away."

# Function to alert the user based on the gas level
def gasLevelAlert():
    gas_level = gasLevelGauge()

    # Dictionary mapping gas levels to messages and logic
    alerts = {
        "Empty": "***WARNING - YOU ARE ON EMPTY***\nCalling Triple AAA",
        "Low": nearestGasStationMessage((1, 25)),
        "Quarter Tank": nearestGasStationMessage((25.1, 58)),
        "Half Tank": "Your gas tank is half full, which is plenty to get to your destination.",
        "Three Quarter Tank": "Your gas tank is three quarters full.",
        "Full Tank": "Your gas tank is full!!! Vroom Vroom"
    }

    # Display the corresponding message based on the gas level
    print(alerts[gas_level])

    # Add a brief delay for low gas levels to simulate processing time
    if gas_level in ["Empty", "Low", "Quarter Tank"]:
        sleep(2)

# Execute the gas level alert
gasLevelAlert()
