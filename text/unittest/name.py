
from name_function import get_formatted_name1

print("Enter q to quit at any.")
while True:
	first = input("\nPlease give me a first name: ")
	if first == 'q':
		break
	last = input("Please give me a last name: ")
	if last == 'q':
		break
	
	formatted_name = get_formatted_name1(first, last)
	print("Neatly formatted name: " + formatted_name + ".")
