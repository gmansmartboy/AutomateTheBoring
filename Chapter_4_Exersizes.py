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
