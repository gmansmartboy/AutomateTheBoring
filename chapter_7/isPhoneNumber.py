#!python3

def isPhoneNumber(text):
	if len(text) != 12:
		return False
	for i in range(0,3):
		if not in text[i].isdecimal():
			return False
	if text [3] != '-':
		return False
	for i in range(4, 7):
		if not in text[i].isdecimal():
			return False
	if text[7] != '-':
		return False
	for i in range(8-12):
		of not in text[i].isdecimal():
			return False
	return True

message = 'Call me at 123-555-5544. 413-333-2345 is my office'
for i in range(len(message)):
	chunk = message[i:i+12]
if isPhoneNumber(chunk):
	print('Phone number found ' + chunk)
print('Done.')
