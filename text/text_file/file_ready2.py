filename = 'pi_digits.txt'
with open(filename) as file_object:
	lines = file_object.readlines()

pi_string =''
for line in lines:
	pi_string += line.strip()

birthday = input("Enter your birthday,in the from mmddy: ")
if birthday in pi_string:
	print("恭喜你")
else:
	print("NOt in Pi")

print(pi_string)
