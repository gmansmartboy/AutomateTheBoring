#! python3
# dateDetection - detect dates in the DD/MM/YYYY format.

import re

# regular expression for DD/MM/YYYY
dateRegex = re.compile(r'''(
	(\d{2})			# date
	(\s|-|/)		# seperator
	(\d{2})			# month
	(\s|-|/)		# seperator
	(\d{4})			# year
	)''', re.VERBOSE)

inputText = ('01-01-0999 and 22-11-0110')
matches = []

# search for dates in string
for groups in dateRegex.findall(inputText):
    joinDates = '/'.join([groups[1], groups[3], groups[5]])
    matches.append(joinDates)

# TODO: write strings into variables named 'month', 'day', 'year'
matchedDates = ()

day, month, year = (''), (''), ('')
for dateStrings in dateRegex.findall(matches):


# TODO: detect valid dates

# TODO: Write code to detect 30 day months
    # april, june, september, november have 30 days
    # february has 28-29 days, all others have 31 days
    

# TODO: print results
if len(matches) > 0:
    print('\n'.join(matches))
else: 
    print('No matches found')
