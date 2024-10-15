# Print a decorative line to separate sections in the console output
print("\n**********************\n")

# Indicate that the program is related to weather forecasting and vehicle response
print("Weather Branch\n")

# Import necessary libraries
import random  # Used to randomly select a weather condition
from time import sleep  # Used to pause the program for a short period to simulate processing


# Define the 'weather' function that randomly selects a weather condition
def weather():
    # List of possible weather conditions
    weatherForecast = ["snowy", "blizzard", "rainy", "windy", "icy", "sunny"]

    # Use random.choice() to select one condition from the list
    weatherCondition = random.choice(weatherForecast)

    # Return the selected weather condition
    return weatherCondition


# Call the 'weather' function to generate a weather alert and store it in 'weatherAlert'
weatherAlert = weather()


# Define the 'vehicleResponseSystem' function to react to different weather conditions
def vehicleResponseSystem():
    # Check if the weather is 'snowy'
    if weatherAlert == "snowy":
        print("\nThe National Weather Service has updated our alarm by 30 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)  # Pause for 1 second to simulate system processing
        print("\nVRS system has been engaged only allowing you to drive 55mph.")

    # Check if the weather is 'blizzard'
    elif weatherAlert == "blizzard":
        print("\nThe National Weather Service has updated our alarm by 45 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)  # Pause for 1 second
        print("\nVRS system has been engaged only allowing you to drive 45mph.")

    # Check if the weather is 'rainy'
    elif weatherAlert == "rainy":
        print("\nThe National Weather Service has updated our alarm by 15 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS system has been engaged only allowing you to drive 65mph.")

    # Check if the weather is 'windy'
    elif weatherAlert == "windy":
        print("\nThe National Weather Service has updated our alarm by 5 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS system has been engaged only allowing you to drive 70mph.")

    # Check if the weather is 'icy'
    elif weatherAlert == "icy":
        print("\nThe National Weather Service has updated our alarm by 50 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS system has been engaged only allowing you to drive 30mph.")

    # If none of the above conditions match, assume the weather is 'sunny' or clear
    else:
        print("The NWS is calling for", weatherAlert, "skies, drive carefully to get to your destination!")
        sleep(1)
        print("\nVRS system has been disengaged.")


# Call the 'vehicleResponseSystem' function to execute the program's response based on the weather alert
vehicleResponseSystem()
