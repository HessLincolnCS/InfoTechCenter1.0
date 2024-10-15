print("\n**********************************************************************\n")

import random  # Used for random weather selection
from time import sleep  # Used to simulate a pause in the program

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

