import sys
import time

# Print a welcome message when the program starts
print("\nWelcome to InfoTechCenter V1.0\n")

x = 0  # Initialize a counter variable 'x'
ellipsis = 0  # Initialize 'ellipsis' to keep track of how many dots to print

# Start a loop that will run 20 times
while x != 20:
    x += 1  # Increment the counter by 1

    # Create a message that adds dots to simulate booting progress
    message = ("Infotech Center System Booting" + "." * ellipsis)
    ellipsis += 1  # Increment the number of dots (ellipsis)

    # Write the message to the console, overwriting the previous line
    sys.stdout.write("\r" + message)

    # Pause the program for 0.5 seconds to simulate a delay in booting
    time.sleep(.5)

    # Reset the ellipsis counter to 0 after reaching 3 dots (so it cycles 0-3)
    if ellipsis == 4:
        ellipsis = 0

    # When 'x' reaches 20, print the final message and break the loop
    if x == 20:
        print("\n\nOperating System Booted Up - Retina Scanned - Access Granted")
