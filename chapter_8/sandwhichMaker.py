#! python3
# Sandwhich Maker - Asks users for their sandwhich preferences.

import pyinputplus as pyip

def totalCost(sandwhichesMade): 


while True: 
    
    breadType = pyip.inputMenu(['white', 'wheat', 'sourdough'])
    proteinType = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'])
    cheeseYesNo = pyip.inputYesNo(prompt = 'Would you like cheese?')

    if cheeseYesNo == yes:
        cheeseType = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'])
    mayo = pyip.inputYesNo(prompt = 'Would you like mayo?')
    numberOfSandwhiches = pyip,inputInt(prompt = 'How many sandwhiches do you want?')
