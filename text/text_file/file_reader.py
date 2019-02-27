
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents.rstrip())
	
	
filename = 'pi_digits.txt'
with open(filename) as file_o:
	for line in file_o:
		print(line)
