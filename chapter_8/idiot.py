#! python3 
# idiot.py - Keep an idiot busy for hours.

import pyinputplus as pyip

while True: 
    prompt = 'Want to know how to keep an idiot busy for hours?\n'

    response = pyip.inputYesNo(prompt)
    if response == 'no':
        break
print('Have an nice day.')

