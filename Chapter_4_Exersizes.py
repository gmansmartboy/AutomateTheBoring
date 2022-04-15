# Notes taken from Al Sweigart's book, 
# 'Automate the Boring Stuff with Python'
# https://automatetheboringstuff.com

# Lists in Python
# Lists with ints. 
spam = [1, 2, 3]
print('spam = ' + str(spam))

# Lists with string
eggs = ['cat', 'bat', 'rat', 'elephant']
print('eggs = ' + str(eggs))

# Getting individual values in a list with indexes
print(eggs[0])
print('The ' + eggs[0] + ' ate the ' + eggs[1] + '.')

# The following will produce an index error:
#print(spam[1000])
# The following will produce a type error:
#spam[1.0]

# The following will not produce a type error:
print(spam[int(1.0)])

# List can contain other lists
spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print('spam =  ' + str(spam))
print(spam[0])  # Prints ['cat', 'bat']
print(spam[0][1])  #Prints 'bat'
print(spam[1][4])  # Prints 50

# The integer value -1 refers to the last index in a list
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam)
print(spam[-1]) # Prints 'elephant'
print(spam[-3]) # Prints 'bat'

print('The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.')
# Prints 'The elephant is afraid of the bat.'

# A slice can get several values from a list,
# in the form of a new list. 
spam = ['cat', 'bat', 'rat', 'elephant']
print('spam = ' + str(spam))
print(spam[1:3]) # Prints ['bat', 'rat']
print(spam[0:-1]) # Prints ['cat', 'bat', 'rat']

# Leaving out the first index is the same as using 0,
# or the beginning of the list.
# Leaving out the second index is the same as using
# the length of the list.

spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[:2]) # Prints  ['cat', 'bat']
print (spam[1:]) # Prints ['bat', 'rat', 'elephant']
print(spam[:]) # Prints ['cat', 'bat', 'rat', 'elephant']

# The len() function will return the number of
# values that are in a list value passed to it.
spam = ['cat', 'bat', 'rat', 'elephant']
print(len(spam)) # Prints 4

# Changing values in a list with indexes.
spam = ['cat', 'bat', 'rat', 'elephant']
print('spam = ' + str(spam))
spam[1] = 'aardvark'
print(spam) # Prints ['cat', 'aardvark', 'rat', 'elephant']
spam[2] = spam[1]
print(spam) # Prints ['cat', 'aardvark', 'aardvark', 'elephant']
spam[-1] = 12345
print(spam) # Prints ['cat', 'aardvark', 'aardvark', 12345]

# List concatenation and List Replication.
print([1, 2, 3] + ['A', 'B', 'C'])
# Prints [1, 2, 3, 'A', 'B', 'C']

# Removing Values from Lists with del Statements
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam) # Prints ['cat', 'bat', 'rat', 'elephant']
del spam[2] # Deletes 'rat'
print(spam) # Prints ['cat', 'bat', 'elephant']
del spam[2] # Deletes 'bat'
print(spam) # Prints ['cat', 'elephant']

# Working with Lists
# You can use a single variable that contains a list value.
# This new version uses a single list and can store
# any number of cats that the user types in.

catNames = []
while True:
  print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
  name = input()
  if name == '':
    break
  catNames = catNames + [name] # List concatination
print('The cat names are: ')
for name in catNames:
  print('  ' + name)

  # Using for Loops with Lists
for i in range(4):
  print(i)  # Prints 0-3
  
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
  for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
    
# The in and not in Operators #
# You can determine whether a value is or isn’t
# in a list with the in and not in operators. 
print(['hello', 'hi', 'howdy', 'heyas'])
'howdy' in ['hello', 'hi', 'howdy', 'heyas']  # Evaluates to True


# The Multiple Assignment Trick #
# The multiple assignment trick (technically called
# tuple unpacking) is a shortcut that lets you assign
# multiple variables with the values in a list in
# one line of code.

cat = ['fat', 'gray', 'loud']
size, color, disposition = cat
# The number of variables and the length of the list must
# be exactly equal, or Python will give you a ValueError:


# Using the enumerate() Function with Lists # 
# On each iteration of the loop, enumerate() will return
# two values: the index of the item in the list, and 
# the item in the list itself.

supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
print('supplies = ' + str(supplies))
for index, item in enumerate(supplies):
print('Index ' + str(index) + ' in supplies is: ' + item)



