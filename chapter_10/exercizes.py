# The shutil Module
# Copying Files and Folders
import shutil, os
from pathlib import Path
p = Path.home()
shutil.copy(p / 'spam.txt', p / 'some_folder')
shutil.copy(p / 'eggs.txt', p / 'some_folder/eggs2.txt')

# shutil.copytree() will copy an entire folder and every folder and file contained in it.
import os
from pathlib import Path
for filename in Path.home().glob('*.rxt'):
    #os.unlink(filename)
    print(filename)
# Moving and Renaming Files and Folders
import shutil
shutil.move('C:\\bacon.txt', 'C:\\eggs')

# The destination path can also specify a filename. 
# In the following example, the source file is moved and renamed.
shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt')

# But if there is no eggs folder, then move() will 
# rename bacon.txt to a file named eggs.
shutil.move('C:\\bacon.txt', 'C:\\eggs')

# Permanently Deleting Files and Folders
# ''' You can delete a single file or a single empty folder
#  with functions in the os module, whereas to delete a folder 
# and all of its contents, you use the shutil module.

# Calling os.unlink(path) will delete the file at path.
# Calling os.rmdir(path) will delete the folder at path. This folder must be empty of any files or folders.
# Calling shutil.rmtree(path) will remove the folder at path, and all files and folders it contains will also be deleted.
# Be careful when using these functions in your programs! 
# It’s often a good idea to first run your program 
# with these calls commented out'''

import os
from pathlib import Path
for filename in Path.home().glob('*.rxt'):  # Typo in here
    os.unlink(filename)		# Permenant file delete!
# Instead use the following.

import os
from pathlib import Path
for filename in Path.home().glob('*.rxt'):
    #os.unlink(filename)
    print(filename)	# Print file name of file to be deleted.

# Using send2trash
import send2trash
baconFile = open('bacon.txt', 'a')	# Creates the file.
baconFile.write('Bacon is not a vegetable.')

# Prints '25'
baconFile.close()
send2trash.send2trash('bacon.txt')

# Example of a program that used the os.walk() function.

import os

for folderName, subfolders, filenames in os.walk('C:\\delicious'):
	print('The current folder is ' + folderName)

	for subfolder in subfolders:
		print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

	for filename in filenames:
		print('FILE INSIDE ' + folderName + ': '+ filename)

	print('')
## Reading ZIP Files
# To read the contents of a ZIP file, first you must create 
# a ZipFile object. To create a ZipFile object, call the 
# zipfile.ZipFile() function, passing it a string of the 
# .ZIP file’s filename.

import zipfile, os

from pathlib import Path
p = Path.home()
exampleZip = zipfile.ZipFile(p / 'example.zip')
exampleZip.namelist()
# Prints ['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']
spamInfo = exampleZip.getinfo('spam.txt')
spamInfo.file_size
# Prints fils size
spamInfo.compress_size
# Prints compressed file size
f'Compressed file is {round(spamInfo.file_size / spamInfo.compress_size, 2)}x smaller!'
# Prints  'Compressed file is x-times smaller!'
exampleZip.close()

# Extracting from ZIP Files

import zipfile, os
from pathlib import Path
p = Path.home()
exampleZip = zipfile.ZipFile(p / 'example.zip')
exampleZip.extractall()
exampleZip.close()

# The extract() method for ZipFile objects will extract
# a single file from the ZIP file.
exampleZip.extract('spam.txt')
# Prints 'C:\\spam.txt'
exampleZip.extract('spam.txt', 'C:\\some\\new\\folders')
# Prints 'C:\\some\\new\\folders\\spam.txt

# Creating and Adding to ZIP Files
# To create your own compressed ZIP files, you must open the
# ZipFile object in write mode by passing 'w' as the second
# argument.
# The second argument is the compression type parameter, which
# tells the computer what algorithm it should use to compress
# the files; you can set this value to zipfile.ZIP_DEFLATED.

import zipfile
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
