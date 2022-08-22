#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the keyboard.

import pyperclip
text = pyperclip.paste()

# TODO: Separate line and add stars.
lines = text.split('\n')
for i in range(len(lines)):     # Loop through all the "lines" list.
    lines[i] = '* ' + lines[i]  # Add star to each string in "lines" list.
text = '\n'.join(lines)

pyperclip.copy(text)

