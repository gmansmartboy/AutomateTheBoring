catNames = []
while True: 
	print('Enter the name of cat ' + str(len(catNames))
            + 1 + ' (or nothing to stop.): ') 
    name = input()
	if name == '': 
		break
	cat names = catNames + [name] # list concatenation
print('The cats names are:')
for name in catNames: 
	print(' ' + name)
