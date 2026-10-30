"""
Hey there! This is a simple greeting program that checks the current time
and says hello to you based on what time of day it is.

What it does:
- Looks at the current time on your computer
- Figures out if it's morning, afternoon, evening, or night
- Prints out a friendly greeting that matches the time
- Also shows you the exact time and date
"""

# First, let's bring in the time module so we can work with the current time
import time

# Now let's grab the current time and format it nicely
# We're getting the time in hours:minutes:seconds, plus the month and year
time1 = "current time is: " + time.strftime("%H:%M:%S") + " " + time.strftime("%h,%y")

# Here's the fun part - we check what time it is and say hello accordingly!
# We look at the hour (in 24-hour format) to figure out which greeting fits best
if int(time.strftime('%H')) < 12 and int(time.strftime('%H')) >= 3:
    # It's between 3 AM and noon, so let's say good morning!
    print("good morning")
elif int(time.strftime('%H')) >= 12 and int(time.strftime('%H')) < 17:
    # It's between noon and 5 PM, perfect for a good afternoon greeting
    print("Good after noon")
elif int(time.strftime('%H')) >= 17 and int(time.strftime('%H')) >= 21:
    # It's evening time (though this should really be < 21 for 5-9 PM)
    print("good evening")
else:
    # It's late night or very early morning - time to sleep!
    print("good night, its night time")

# Finally, let's show the user what time it actually is
print(time1)

# Here's what you'll see when you run this (example at 9:00 AM):
# good morning
# current time is: 09:00:00 Oct,26