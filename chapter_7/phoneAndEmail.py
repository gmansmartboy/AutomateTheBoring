#! python3
# phoneAndEmail.py - Finds phone numbers, email addresses, and urls on the clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    ([-a-zA-Z0-9._%\+-/]+)            # email address 
    (@)
    ([-a-zA-Z0-9\._\+-])              # domain
    )''', re.VERBOSE)

urlRegex = re.compile(r'''(
    ((http|https)://)                 # http(s)://
    ([-a-zA-Z0-9\._%\+-/]+)             # domain
    )''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

for urls in urlRegex.findall(text):
	matches.append(urls[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers, email addresses, or urls found.')
