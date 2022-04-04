"""Calendar Maker. 
Create monthly calendars, saved to a text file and fit for printing."""

import datetime

# Set up the constants.
DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December')

print('Calendar Maker.')

while True: # Loop to get a year from the user.
    print('Enter the year for the calendar: ')
    response = input('> ')
    
    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break
    
    print('Please enter a numeric year, like 2023.')
    continue
    
while True: # Loop to get a month from the user.
    print('Enter the month for the calendar, 1-12: ')
    response = input('> ')
    
    if not response.isdecimal():
        print('Please enter a numeric month like 3 for March.')
        continue
        
    month = int(response)
    if 1 <= month <= 12:
        break
        
    print('Please enter a number from 1 to 12.')
    
def getCalendarFor(year, month):
    calText = '' # calText will contain the string of our calendar.
    
    # Put the month and year at the top of the calendar.
    calText += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'
    
    # Add thedays of the week labels to the calendar.
    # (!) Try changing this to abbreviations: sun, mon etc.
    calText += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....\
    Friday....Saturday..\n'
    
    # The horizontal line string that seperate weeks.
    weekSeperator = ('+----------' * 7) + '+\n'
    
    # The blank rows have ten spaces in between the | day seperators.
    blankRow = ('|          ' * 7) + '|\n'
    
    # Get the first date in the month. (The datetime module handles all
    # the complicated calendar stuff for us here.)
    currentDate = datetime.date(year, month, 1)
    
    while True: # Loop over each week in the month.
        calText += weekSeperator
        
        # dayNumberRow is the row with the day number labels.
        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1) # Go to next day.
        dayNumberRow += '|\n' # Add the vertical line after saturday.
        
        # Add the day number row and 3 blank rows to the calendar text.
        calText += dayNumberRow
        for i in range(3): # (!) Try changing the 4 to a 5 or 10.
            calText += blankRow
            
        # Check if we're donw with the month.
        if currentDate.month != month:
            break
            
        # Add the horizontal line at the very bottom of the calendar.
        calText += weekSeperator
        return calText
    
calText = getCalendarFor(year, month)
print(calText) # Display the calendar.

# Save the calendar to a text file.
