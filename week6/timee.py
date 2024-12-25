# Convert the total seconds into a more readable format (HH:MM:SS)
# The function takes a total number of seconds as input
# Calculate the number of full days (optional) and remaining seconds
def convert(seconds):
    seconds = seconds % (24 * 3600)  # Find the remaining seconds after removing full days (24 hours)

    # Calculate the number of full hours
    hour = seconds // 3600           # Divide remaining seconds by 3600 to get the number of full hours

    # Update seconds to reflect only the remaining seconds after hours
    seconds %= 3600                  # Take the remainder after dividing by 3600

    # Calculate the number of full minutes
    minutes = seconds // 60          # Divide remaining seconds by 60 to get the number of full minutes

    # Update seconds to reflect only the remaining seconds after minutes
    seconds %= 60                    # Take the remainder after dividing by 60

    # Format the output as HH:MM:SS
    return "The time is + %d:%02d:%02d" % (hour, minutes, seconds)  # Return the formatted time string
n= int(input("Enter the seconds"))
print(convert(n))


#For the Print formatting
    # return" So the time is %d hour %d minutes %d seconds" % (hour, minutes, seconds)
# print(f"So the time is {hour} hour {minutes} minutes {seconds} seconds")