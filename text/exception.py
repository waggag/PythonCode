try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero!")

def count_words(filename):
	"""计算一个文件包含多少单词"""
	try:
		with open(filename) as f_object:
			contents = f_object.read()
	except FileNotFoundError:
		msg = "Sorry,the file "+ filename+" does not exist"
		print(msg)
	else:
		#计算文件大概包含多少单词
		words = contents.split()
		num_words = len(words)
		print("The file "+filename+" has about " +str(num_words)+" words.")
		
filename = 'alice.txt'
count_words(filename)
