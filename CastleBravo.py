
import sys
import time
import random  # Used for random weather selection
from time import sleep  # Used to simulate a pause in the program
import random
from time import sleep

# ANSI escape sequences for coloring
GREEN = '\033[92m'
RESET = '\033[0m'

# Print a welcome message when the program starts in green
print(GREEN + "\nWelcome to InfoTechCenter V1.0\n" + RESET)

timeToSleep = 2 #variable to set the time library to 2 seconds when called
time.sleep(timeToSleep) #calling the time to sleep library with the variable timeToSleep value

x = 0  # Initialize a counter variable 'x'
ellipsis = 0  # Initialize 'ellipsis' to keep track of how many dots to print

# Start a loop that will run 20 times
while x != 20:
    x += 1  # Increment the counter by 1

    # Create a message that adds dots to simulate booting progress
    message = ("InfoTech Center System Booting" + "." * ellipsis)
    ellipsis += 1  # Increment the number of dots (ellipsis)

    # Write the message to the console, overwriting the previous line
    sys.stdout.write("\r" + message)

    # Pause the program for 0.5 seconds to simulate a delay in booting
    time.sleep(1)

    # Reset the ellipsis counter to 0 after reaching 3 dots (so it cycles 0-3)
    if ellipsis == 4:
        ellipsis = 0

# When 'x' reaches 20, print the final message and break the loop in green
print("\n\n" + GREEN + "Operating System Booted Up - Retina Scanned - Access Granted" + RESET)

print("\n**********************************************************************\n")



# Function to randomly select a weather condition
def weather():
    weather_forecast = ["snowy", "blizzard", "rainy", "windy", "icy", "sunny"]
    return random.choice(weather_forecast)  # Return a random weather condition

# Store the weather alert
weather_alert = weather()

# Dictionary to store alarm delays and speed limits for different weather conditions
weather_responses = {
    "snowy": {"delay": 30, "speed": 55},
    "blizzard": {"delay": 45, "speed": 45},
    "rainy": {"delay": 15, "speed": 65},
    "windy": {"delay": 5, "speed": 70},
    "icy": {"delay": 50, "speed": 30},
}

# Function to determine the appropriate vehicle response based on the weather condition
def vehicle_response_system():
    if weather_alert in weather_responses:
        response = weather_responses[weather_alert]
        print(
            f"\nThe National Weather Service has updated our alarm by {response['delay']} minutes "
            f"because of the forecast of {weather_alert} weather conditions."
        )
        sleep(1)
        print(f"\nVRS system has been engaged only allowing you to drive {response['speed']}mph.")
    else:
        print(f"The NWS is calling for {weather_alert} skies, drive carefully to get to your destination!")
        sleep(1)
        print("\nVRS system has been disengaged.")

# Print decorative output and call the vehicle response system

print("Weather Branch\n")
vehicle_response_system()




# Print decorative lines and program title
print("\n**********************************************************************\n")
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
    return f"Your gas tank is Quarter full. The closest gas station is {station}, which is {miles} miles away."

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
