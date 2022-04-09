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
print(len(spam)) # Prints 3
