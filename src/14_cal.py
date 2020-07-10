"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
- If the user doesn't specify any input, your program should
  print the calendar for the current month. The 'datetime'
  module may be helpful for this.
- If the user specifies one argument, assume they passed in a
  month and render the calendar for that month of the current year.
- If the user specifies two arguments, assume they passed in
  both the month and the year. Render the calendar for that
  month and year.
- Otherwise, print a usage statement to the terminal indicating
  the format that your program expects arguments to be given.
  Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

# if user doesn't specify input, display current month and current year
if len(sys.argv) == 1:
  print(calendar.month(datetime.now().year, datetime.now().month))

# if user only provides one argument, display the provided month and the current year
elif len(sys.argv) == 2:
  # check if argument is a number
  if sys.argv[1].isnumeric():
    # typecast the argument from a string to an int
    month = int(sys.argv[1])
    # if the provided argument is in the range of 1 to 12, display calendar for that month
    if month > 0 and month < 13:
      print(calendar.month(datetime.now().year, month))
    else:
      print("Please provide a number from 1 to 12 for the calendar month you'd like to see")
  # if the argument provided isn't a number, throw an error
  else:
    print("Please provide a valid number for the calendar month you'd like to see")

# if user provides two arguments, display provided month and provided year
elif len(sys.argv) == 3:
  # check if argument is a number
  if sys.argv[1].isnumeric() and sys.argv[2].isnumeric():
    # typecast the arguments from a string to an int
    month = int(sys.argv[1])
    year = int(sys.argv[2])
    # check if the month is in the range of 1 to 12
    if month > 0 and month < 13:
      print(calendar.month(year, month))
    else:
      print("Please provide a number from 1 to 12 for the calendar month you'd like to see")

  # if the argument provided isn't a number, throw an error
  else:
    print("Please provide proper argument input. When invoking this file, the format should look like 14_cal.py [month] [year] or just 14_cal.py for a calendar of the current month and year")