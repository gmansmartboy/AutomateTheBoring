#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords into clipboard.
#        py.exe mcb.pyw delete - Removes keyword from list.
#        py.exe mcb.pyw delete all - Removes all keywords from list.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save': 
    mcbShelf[sys.argv[2]] = pyperclip.paste()
   
# Delete clipboard content.    
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    # Delete all content
    if sys.argv[2] == 'all': 
        mcbShelf.clear() 
    # Delete element
    else:
        del mcbShelf[sys.argv[2]] 

# List keywords and load content.
elif len(sys.argv) == 2: 
    if sys.argv[1].lower() == 'list': 
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()


