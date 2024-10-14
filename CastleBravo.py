import sys
import time

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