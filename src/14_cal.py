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

# note: check argv and others
argvlength = len(sys.argv)
# - use method datetime.now().year & datetime.now().month
# - store both in variable year & month
users_input = input()

if argvlength == 1:
# - if no input, 
#       default to todays date. 
  month = datetime.now().month
  year = datetime.now().year

elif argvlength == 2:
# - elif one input, 
#       render specified month and were going to use the current year.
  year = datetime.now().year
  month = int(sys.argv[1])

elif argvlength == 3:
# - elif two inputs, 
#       the first will be the month, 2nd will be the year. will use those for the calendar.
  month = int(sys.argv[1])  
  year = int(sys.argv[2])
else:
# - else more than two inputs, send error message.
  print('usage: 14_cal.py [month] [year]')
  # exit program
  sys.exit(1)

cal = calendar.TextCalendar()
cal.prmonth(year, month)