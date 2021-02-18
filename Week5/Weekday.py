#Program that outputs whether or not today is a weekday
#Author: Brendan Tunney

# This imports python's datetime module

import datetime

# Weekday function returns days as an integer (0 for Monday up to 6 for Sunday)

dayOfWeek = datetime.datetime.today().weekday()

if dayOfWeek < 5:
    print ("Unfortunately, it is a weekday. Get back to work!")
else:
    print ("Its the weekend, but still too early for cans!")

# Referenced W3 Schools, Stackoverflow & Pythonic